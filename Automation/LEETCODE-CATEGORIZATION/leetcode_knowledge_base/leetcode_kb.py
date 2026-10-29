#!/usr/bin/env python3
"""Build a private, resumable topic-wise LeetCode C++ interview knowledge base.
Python 3.9+; pip install requests beautifulsoup4
Never print or persist LEETCODE_SESSION/csrftoken.
"""
import argparse
import collections
import hashlib
import html
import json
import os
from pathlib import Path
import random
import re
import sys
import time

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit('Install dependencies: python3 -m pip install requests beautifulsoup4')

BASE = 'https://leetcode.com'
QUERY_LIST = '''query problemsetQuestionList($categorySlug:String,$limit:Int,$skip:Int,$filters:QuestionListFilterInput){problemsetQuestionList:questionList(categorySlug:$categorySlug,limit:$limit,skip:$skip,filters:$filters){total:totalNum questions:data{questionId questionFrontendId title titleSlug difficulty topicTags{name slug} status isPaidOnly}}}'''
QUERY_DETAIL = '''query questionData($titleSlug:String!){question(titleSlug:$titleSlug){questionId questionFrontendId title titleSlug content difficulty isPaidOnly topicTags{name slug} codeSnippets{lang langSlug code} hints}}'''
QUERY_SUBS = '''query submissionList($offset:Int!,$limit:Int!,$questionSlug:String!){questionSubmissionList(offset:$offset,limit:$limit,questionSlug:$questionSlug){lastKey hasNext submissions{id statusDisplay lang timestamp}}}'''
QUERY_CODE = '''query submissionDetails($submissionId:Int!){submissionDetails(submissionId:$submissionId){code lang statusDisplay}}'''
QUERY_CODE_ALT = '''query submissionDetails($submissionId:Int!){submissionDetails(submissionId:$submissionId){code}}'''

# Pattern order is deliberate: the first match becomes the primary topic.
PATTERNS = [
 ('Monotonic Stack / Queue', ('monotonic-stack','monotonic-queue')),
 ('Sliding Window / Two Pointers', ('sliding-window','two-pointers')),
 ('Binary Search / Answer Search', ('binary-search',)),
 ('Tree DP / Rerooting', ('tree-dp','rerooting')),
 ('Dynamic Programming', ('dynamic-programming','memoization')),
 ('Graph Traversal / Shortest Path', ('graph','shortest-path','breadth-first-search','depth-first-search','topological-sort','union-find','minimum-spanning-tree','strongly-connected-component')),
 ('Tree / Trie', ('tree','binary-tree','binary-search-tree','trie','segment-tree','binary-indexed-tree')),
 ('Greedy / Intervals', ('greedy','intervals')),
 ('Backtracking / Bitmask', ('backtracking','bitmask','bitmask-dp')),
 ('Heap / Priority Queue', ('heap-priority-queue',)),
 ('Prefix Sum / Difference Array', ('prefix-sum','difference-array')),
 ('Hashing / Frequency Counting', ('hash-table','counting','rolling-hash','hash-function')),
 ('String Algorithms', ('string','string-matching','suffix-array','kmp','z-function')),
 ('Math / Number Theory', ('math','number-theory','combinatorics','geometry','probability-and-statistics')),
 ('Sorting / Divide and Conquer', ('sorting','divide-and-conquer','merge-sort','quickselect')),
 ('Linked List / Pointers', ('linked-list',)),
 ('Bit Manipulation', ('bit-manipulation',)),
 ('Stack / Queue', ('stack','queue','design')),
 ('Simulation / Implementation', ('simulation','array','matrix')),
]
STRUCTURES = {
 'hash-table':'Hash map / hash set', 'heap-priority-queue':'Priority queue / heap',
 'monotonic-stack':'Monotonic stack', 'monotonic-queue':'Monotonic deque',
 'segment-tree':'Segment tree', 'binary-indexed-tree':'Fenwick tree',
 'union-find':'Disjoint set union', 'trie':'Trie', 'binary-tree':'Binary tree',
 'tree':'Tree adjacency list', 'graph':'Graph adjacency list',
 'linked-list':'Linked list', 'queue':'Queue', 'stack':'Stack',
 'prefix-sum':'Prefix-sum array', 'bitmask':'Bitmask',
 'sorting':'Sorted array', 'array':'Array / vector', 'matrix':'2D array / matrix',
 'dynamic-programming':'DP array / memo table', 'string':'String',
}
RECOGNITION = {
 'Monotonic Stack / Queue':'Nearest greater/smaller element, next boundary, or a window extremum.',
 'Sliding Window / Two Pointers':'Contiguous range with an invariant; advance boundaries without rescanning.',
 'Binary Search / Answer Search':'Monotone feasibility predicate or ordered search space.',
 'Tree DP / Rerooting':'Combine answers from children, sometimes transfer parent contribution.',
 'Dynamic Programming':'Overlapping subproblems; choose state, transition, base case, and order.',
 'Graph Traversal / Shortest Path':'Reachability, connected components, dependencies, or minimum path.',
 'Tree / Trie':'Hierarchical traversal, ancestor queries, prefix lookup, or range structure.',
 'Greedy / Intervals':'Locally optimal choices with an exchange or ordering argument.',
 'Backtracking / Bitmask':'Enumerate choices while pruning; compress subsets as masks.',
 'Heap / Priority Queue':'Repeatedly select the current min/max or maintain top-k candidates.',
 'Prefix Sum / Difference Array':'Turn repeated range sums or range updates into constant-time arithmetic.',
 'Hashing / Frequency Counting':'Fast membership, duplicate detection, counting, or complement lookup.',
 'String Algorithms':'Prefix/suffix structure, substring matching, or character constraints.',
 'Math / Number Theory':'Exploit arithmetic invariants, divisibility, or combinatorial counting.',
 'Sorting / Divide and Conquer':'Order elements to expose structure or split into manageable halves.',
 'Linked List / Pointers':'Rewire node links while preserving ownership and pointer invariants.',
 'Bit Manipulation':'Use XOR, bit masks, bit positions, or binary representation.',
 'Stack / Queue':'LIFO/FIFO processing, parser state, or online operations.',
 'Simulation / Implementation':'Directly model operations, states, and edge cases.',
}

class Client:
    def __init__(self, delay, retries):
        self.delay, self.retries = delay, retries
        self.session = requests.Session()
        self.session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36', 'Referer':BASE+'/problemset/', 'Origin':BASE})
        token = os.environ.get('LEETCODE_SESSION', '').strip()
        csrf = os.environ.get('csrftoken', os.environ.get('CSRF_TOKEN', '')).strip()
        if token: self.session.cookies.set('LEETCODE_SESSION', token, domain='.leetcode.com')
        if csrf:
            self.session.cookies.set('csrftoken', csrf, domain='.leetcode.com')
            self.session.headers['x-csrftoken'] = csrf
        self.auth = bool(token)

    def graphql(self, query, variables):
        for attempt in range(self.retries):
            try:
                response = self.session.post(BASE+'/graphql/', json={'query':query,'variables':variables}, timeout=35)
                if response.status_code in (403,429,500,502,503,504):
                    raise RuntimeError('HTTP '+str(response.status_code))
                response.raise_for_status()
                data = response.json()
                if data.get('errors'):
                    raise RuntimeError('; '.join(str(x.get('message','GraphQL error')) for x in data['errors']))
                time.sleep(self.delay)
                return data.get('data') or {}
            except (requests.RequestException, ValueError, RuntimeError) as exc:
                if attempt+1 == self.retries: raise RuntimeError(str(exc)) from exc
                time.sleep(min(30, (2**attempt)+random.random()))
        return {}

    def code(self, sid):
        errors = []
        for query in (QUERY_CODE, QUERY_CODE_ALT):
            try:
                result = self.graphql(query, {'submissionId': int(sid)})
                entry = result.get('submissionDetails') or {}
                if entry.get('code'):
                    return entry['code']
                errors.append('GraphQL submissionDetails returned no code')
            except RuntimeError as exc:
                errors.append('GraphQL: ' + str(exc))
        # Some LeetCode deployments expose submission source through the
        # authenticated submission-detail page rather than GraphQL.
        try:
            response = self.session.get(BASE + '/submissions/detail/' + str(sid) + '/', timeout=35)
            if response.status_code != 200:
                errors.append('detail page HTTP ' + str(response.status_code))
            else:
                soup = BeautifulSoup(response.text, 'html.parser')
                node = soup.find('script', id='__NEXT_DATA__')
                if node and node.string:
                    payload = json.loads(node.string)
                    def find_code(obj):
                        if isinstance(obj, dict):
                            for key in ('code', 'submissionCode'):
                                if isinstance(obj.get(key), str) and ('\n' in obj[key] or 'class ' in obj[key]):
                                    return obj[key]
                            for value in obj.values():
                                found = find_code(value)
                                if found: return found
                        elif isinstance(obj, list):
                            for value in obj:
                                found = find_code(value)
                                if found: return found
                        return ''
                    code = find_code(payload)
                    if code: return code
                errors.append('detail page contained no extractable code')
        except (requests.RequestException, ValueError) as exc:
            errors.append('detail page: ' + str(exc))
        raise RuntimeError('; '.join(errors))


def read_json(path, default=None):
    if not path.exists(): return default
    try: return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError): return default


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    tmp.replace(path)


def clean_html(source):
    if not source: return ''
    soup = BeautifulSoup(source, 'html.parser')
    for tag in soup(['script','style']): tag.decompose()
    for pre in soup.find_all('pre'):
        pre.replace_with('\n```\n'+pre.get_text('\n', strip=False).strip()+'\n```\n')
    for img in soup.find_all('img'):
        if img.get('src'): img.replace_with('[Figure: '+img['src']+']')
    for tag in soup.find_all(['p','li','h1','h2','h3']): tag.insert_before('\n')
    text = soup.get_text(' ', strip=False)
    text = html.unescape(text)
    text = re.sub(r'[ \t]+',' ',text)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    return text.strip()


def categorise(tags, code):
    slugs = {t['slug'] for t in tags if t.get('slug')}
    matched = [name for name, aliases in PATTERNS if slugs.intersection(aliases)]
    primary = matched[0] if matched else 'Other / Unclassified'
    ds = sorted({v for k,v in STRUCTURES.items() if k in slugs})
    if code:
        clues = [('unordered_map','Hash map'),('unordered_set','Hash set'),('priority_queue','Priority queue'),
                 ('deque<','Deque'),('queue<','Queue'),('stack<','Stack'),('set<','Ordered set'),
                 ('map<','Ordered map'),('vector<','Vector'),('bitset<','Bitset')]
        ds.extend(label for needle,label in clues if needle in code)
    return primary, matched, sorted(set(ds))


def analysis_for(record):
    # No fabricated complexity: only metadata-derived recognition and a review marker.
    primary = record['primary_topic']
    return {'approach_summary': RECOGNITION.get(primary,'Inspect constraints and derive an invariant.'),
            'analysis_source':'topic-tag heuristic; NOT a verified per-solution explanation',
            'time_complexity':'Needs manual or AI-assisted code analysis',
            'space_complexity':'Needs manual or AI-assisted code analysis'}


def fetch_solved(client, root, refresh):
    path = root/'cache'/'solved_catalog.json'
    if path.exists() and not refresh: return read_json(path, [])
    items, skip = [], 0
    while True:
        data = client.graphql(QUERY_LIST, {'categorySlug':'','limit':100,'skip':skip,'filters':{'status':'AC'}})
        payload = data.get('problemsetQuestionList') or {}
        page = payload.get('questions') or []
        if not page and skip == 0:
            # Fallback category; LeetCode changes this endpoint from time to time.
            data = client.graphql(QUERY_LIST, {'categorySlug':'','limit':100,'skip':skip,'filters':{'status':'AC'}})
            payload = data.get('problemsetQuestionList') or {}
            page = payload.get('questions') or []
        if not page: break
        items.extend(page)
        skip += len(page)
        print('Solved catalog:',len(items),'/',payload.get('total','?'), file=sys.stderr)
        save_json(path, items)
        if skip >= int(payload.get('total') or skip): break
    return items


def fetch_accepted_cpp(client, slug, max_pages, debug=False):
    errors = []
    seen = collections.Counter()
    for page in range(max_pages):
        data = client.graphql(QUERY_SUBS, {'offset':page*20,'limit':20,'questionSlug':slug})
        obj = data.get('questionSubmissionList') or {}
        submissions = obj.get('submissions') or []
        if debug:
            print(f'[debug] {slug}: page={page+1}, submissions={len(submissions)}, hasNext={obj.get("hasNext")}', file=sys.stderr)
        for sub in submissions:
            lang = str(sub.get('lang') or '').lower()
            status = str(sub.get('statusDisplay') or '')
            seen[(lang,status)] += 1
            if status.lower() == 'accepted' and ('cpp' in lang or 'c++' in lang):
                try:
                    code = client.code(sub['id'])
                    if code: return code, str(sub['id']), 'accepted_cpp_submission'
                except RuntimeError as exc:
                    errors.append(f'submission {sub["id"]}: {exc}')
                    if debug: print('[debug] '+errors[-1],file=sys.stderr)
        if not obj.get('hasNext') or not submissions: break
    if debug:
        print('[debug] languages/statuses:', dict(seen), file=sys.stderr)
    if errors:
        return '', '', 'submission_code_access_failed: ' + ' | '.join(errors[:2])
    if not seen:
        return '', '', 'submission_history_empty_or_inaccessible'
    return '', '', 'no_accepted_cpp_in_scanned_history'


def load_local_cpp(folder, frontend_id, slug):
    if not folder: return ''
    base = Path(folder)
    for name in (frontend_id+'.cpp', slug+'.cpp', frontend_id+'.md',slug+'.md'):
        path = base/name
        if path.is_file():
            raw = path.read_text(encoding='utf-8')
            if path.suffix == '.cpp': return raw
            match = re.search(r'```(?:cpp|c\+\+)\s*\n(.*?)\n```', raw, re.S|re.I)
            if match: return match.group(1)
    return ''


def process_one(client, root, item, local_folder, max_pages, refresh, debug=False):
    slug = item['titleSlug']
    cache = root/'cache'/'problems'/ (slug+'.json')
    if cache.exists():
        old = read_json(cache)
        if old and old.get('code'):
            return old
        # Automatically retry missing code rather than preserving a failed lookup.
        if old and old.get('code_source') == 'local_solution_file':
            return old
    detail = client.graphql(QUERY_DETAIL, {'titleSlug':slug}).get('question') or {}
    code = load_local_cpp(local_folder, str(item.get('questionFrontendId') or ''), slug)
    sid = ''
    source = 'local_solution_file' if code else 'missing'
    if not code:
        try: code, sid, source = fetch_accepted_cpp(client, slug, max_pages, debug)
        except RuntimeError as exc: source = 'submission_lookup_failed: '+str(exc)
    tags = detail.get('topicTags') or item.get('topicTags') or []
    primary, secondary, structures = categorise(tags, code)
    record = {
        'id':str(detail.get('questionFrontendId') or item.get('questionFrontendId') or ''),
        'title':detail.get('title') or item.get('title') or slug,
        'slug':slug,'url':BASE+'/problems/'+slug+'/',
        'difficulty':detail.get('difficulty') or item.get('difficulty'),
        'premium':bool(detail.get('isPaidOnly', item.get('isPaidOnly',False))),
        'tags':[x.get('name','') for x in tags],
        'primary_topic':primary,'related_topics':secondary,'data_structures':structures,
        'description':clean_html(detail.get('content')),
        'code':code,'code_source':source,'submission_id':sid,
    }
    record.update(analysis_for(record))
    save_json(cache, record)
    return record


def safe_name(name): return re.sub(r'[^a-zA-Z0-9_-]+','_',name).strip('_')


def render_entry(r, include_desc):
    tags = ', '.join(r['tags']) or 'Not available'
    ds = ', '.join(r['data_structures']) or 'Not inferred'
    result = [f"## {r['id']}. {r['title']}", f"**Problem:** {r['url']}",
              f"**Difficulty:** {r['difficulty']} | **Premium:** {'Yes' if r['premium'] else 'No'}",
              f"**Tags:** {tags}",f"**Primary pattern:** {r['primary_topic']}",
              f"**Related patterns:** {', '.join(r['related_topics']) or 'None'}",
              f"**Data structures (inferred):** {ds}",
              f"**Pattern recognition:** {r['approach_summary']}",
              f"**Approach verification:** {r['analysis_source']}",
              f"**Time complexity:** {r['time_complexity']}",
              f"**Space complexity:** {r['space_complexity']}"]
    if include_desc:
        result += ['### Problem description',r['description'] or '_Description unavailable (check login or Premium access)._']
    result += ['### C++ solution',f"**Source:** {r['code_source']}"]
    result += ['```cpp\n'+r['code'].rstrip()+'\n```' if r['code'] else '_Accepted C++ source unavailable. No code fabricated._','']
    return '\n\n'.join(result)


def build(root, include_desc):
    files = sorted((root/'cache'/'problems').glob('*.json'))
    rows = [read_json(p) for p in files]
    rows = [r for r in rows if isinstance(r,dict)]
    groups = collections.defaultdict(list)
    for r in rows: groups[r['primary_topic']].append(r)
    topic_dir = root/'topics'
    topic_dir.mkdir(parents=True,exist_ok=True)
    for old in topic_dir.glob('*.md'): old.unlink()
    index = ['# LeetCode Interview Knowledge Base', '',
             f"Indexed problems: **{len(rows)}**. C++ code available: **{sum(bool(r['code']) for r in rows)}**.",
             '', '**Important:** Pattern recognition is heuristic; time/space complexity is deliberately not guessed. ',
             'Only accepted-submission code or explicitly provided local code is included. Keep this private, especially Premium statements.', '',
             '## Topics', '']
    for name, members in sorted(groups.items(),key=lambda x:(-len(x[1]),x[0])):
        filename=safe_name(name)+'.md'
        members.sort(key=lambda r:(int(r['id']) if r['id'].isdigit() else 999999,r['title']))
        content=['# '+name, '', f'**Problems:** {len(members)}', '',
                 '## Quick revision checklist', '', RECOGNITION.get(name,''), '',
                 '## Problem index', '']
        for r in members:
            content.append(f"- [{r['id']}. {r['title']}](#{safe_name(r['id']+'-'+r['title']).lower().replace('_','-')}) — {r['difficulty']}; code: {'yes' if r['code'] else 'missing'}")
        content.append('\n---\n')
        content.extend(render_entry(r, include_desc) for r in members)
        (topic_dir/filename).write_text('\n'.join(content),encoding='utf-8')
        index.append(f'- [{name}](topics/{filename}) — **{len(members)}** problems')
    missing = [r for r in rows if not r['code']]
    index += ['', '## Missing accepted C++ code', '',f'{len(missing)} problem(s). See `missing_code.csv`.', '',
              '## Review workflow', '',
              '1. Review each topic recognition rule, then try problems without looking at the solution.',
              '2. Add a verified per-problem approach and complexity after inspecting the actual code.',
              '3. Re-run with `--build-only` to regenerate Markdown from cached records.', '']
    (root/'README.md').write_text('\n'.join(index),encoding='utf-8')
    import csv
    with (root/'missing_code.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f);w.writerow(['id','title','url','status'])
        for r in missing:w.writerow([r['id'],r['title'],r['url'],r['code_source']])
    print(f'Wrote {len(groups)} topic files, {len(rows)} problems, {len(missing)} missing code.')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',default='leetcode_kb_output')
    p.add_argument('--delay',type=float,default=1.0)
    p.add_argument('--retries',type=int,default=4)
    p.add_argument('--max-submission-pages',type=int,default=10)
    p.add_argument('--max-problems',type=int,default=0,help='Test a small number first; 0 means all')
    p.add_argument('--local-solutions',help='Optional folder with ID.cpp, slug.cpp, ID.md or slug.md')
    p.add_argument('--refresh',action='store_true',help='Refetch problem details/submissions, retaining successful code')
    p.add_argument('--refresh-catalog',action='store_true',help='Refetch the complete solved catalog')
    p.add_argument('--debug',action='store_true',help='Print submission retrieval diagnostics (never tokens)')
    p.add_argument('--build-only',action='store_true',help='Regenerate Markdown from cache without network')
    p.add_argument('--no-descriptions',action='store_true')
    args=p.parse_args()
    root=Path(args.output);root.mkdir(parents=True,exist_ok=True)
    if args.build_only:
        build(root,not args.no_descriptions);return
    client=Client(max(0,args.delay),max(1,args.retries))
    if not client.auth: print('Warning: LEETCODE_SESSION not set; private/Premium/solved data may be unavailable.',file=sys.stderr)
    try: catalog=fetch_solved(client,root,args.refresh_catalog)
    except RuntimeError as exc: sys.exit('Could not load solved catalog: '+str(exc))
    if not catalog: sys.exit('No solved problems returned. Verify login, CSRF token, and LeetCode GraphQL availability.')
    print('Solved catalog entries:',len(catalog),file=sys.stderr)
    if args.max_problems:catalog=catalog[:args.max_problems]
    failures=[]
    for i,item in enumerate(catalog,1):
        slug=item.get('titleSlug')
        if not slug: continue
        try:
            r=process_one(client,root,item,args.local_solutions,args.max_submission_pages,args.refresh,args.debug)
            print(f"[{i}/{len(catalog)}] {r['id']} {slug} | {'C++' if r['code'] else 'NO C++'}",file=sys.stderr)
        except Exception as exc:
            failures.append({'slug':slug,'error':str(exc)})
            print(f'[{i}/{len(catalog)}] FAILED {slug}: {exc}',file=sys.stderr)
        if i%25==0:
            save_json(root/'cache'/'failures.json',failures)
            build(root,not args.no_descriptions)
    save_json(root/'cache'/'failures.json',failures)
    build(root,not args.no_descriptions)
    if failures: print(f'{len(failures)} problems failed; rerun to retry cached gaps.',file=sys.stderr)

if __name__=='__main__':main()
