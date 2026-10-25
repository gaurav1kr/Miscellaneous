#!/usr/bin/env python3
"""Export all account-unresolved LeetCode algorithm problems (free + premium).

Requires LEETCODE_SESSION and csrftoken environment variables.
Question status is account-wide, not specific to C++.
"""
import argparse
import csv
import json
import re
from html.parser import HTMLParser
from urllib.parse import urlparse
import os
import sys
import time
from pathlib import Path

import requests

URL = 'https://leetcode.com/graphql/'
QUERY = '''
query problemsetQuestionListV2($filters: QuestionFilterInput, $limit: Int, $skip: Int, $categorySlug: String) {
  problemsetQuestionListV2(filters: $filters, limit: $limit, skip: $skip, categorySlug: $categorySlug) {
    totalLength
    hasMore
    questions {
      questionFrontendId
      title
      titleSlug
      difficulty
      status
      paidOnly
    }
  }
}
'''
USER_QUERY = 'query globalData { userStatus { isSignedIn username isPremium } }'
FIELDS = ['ID', 'Title', 'Difficulty', 'Status', 'Premium', 'URL']

DETAIL_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    content
    codeSnippets { lang langSlug code }
  }
}
"""

class HTMLToMarkdown(HTMLParser):
    """Convert LeetCode statement HTML to readable Markdown without dependencies."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.pre = False
        self.code = False
        self.list_stack = []
        self.href = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'pre':
            self.out.append('\n\n```text\n')
            self.pre = True
        elif tag == 'code' and not self.pre:
            self.out.append('`')
            self.code = True
        elif tag in ('p', 'div', 'section') and not self.pre:
            self.out.append('\n\n')
        elif tag == 'br':
            self.out.append('\n')
        elif tag in ('strong', 'b'):
            self.out.append('**')
        elif tag in ('em', 'i'):
            self.out.append('*')
        elif tag in ('ul', 'ol'):
            self.list_stack.append([tag, 0])
            self.out.append('\n')
        elif tag == 'li':
            self.out.append('\n')
            if self.list_stack:
                self.list_stack[-1][1] += 1
                item = self.list_stack[-1]
                self.out.append(('%d. ' % item[1]) if item[0] == 'ol' else '- ')
            else:
                self.out.append('- ')
        elif tag == 'a':
            self.href = attrs.get('href')
            self.out.append('[' if self.href else '')
        elif tag == 'img':
            src = attrs.get('src')
            if src:
                self.out.append('![%s](%s)' % (attrs.get('alt', 'Image'), src))
        elif tag == 'sup':
            self.out.append('^(')

    def handle_endtag(self, tag):
        if tag == 'pre':
            self.out.append('\n```\n\n')
            self.pre = False
        elif tag == 'code' and self.code:
            self.out.append('`')
            self.code = False
        elif tag in ('strong', 'b'):
            self.out.append('**')
        elif tag in ('em', 'i'):
            self.out.append('*')
        elif tag in ('ul', 'ol') and self.list_stack:
            self.list_stack.pop()
            self.out.append('\n')
        elif tag == 'a' and self.href:
            self.out.append('](%s)' % self.href)
            self.href = None
        elif tag == 'sup':
            self.out.append(')')

    def handle_data(self, data):
        self.out.append(data if self.pre else re.sub(r'\s+', ' ', data))

    def result(self):
        text = ''.join(self.out)
        text = re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+', '\n\n', text)
        return text.strip()


def markdown_description(html):
    converter = HTMLToMarkdown()
    converter.feed(html)
    return converter.result()


def rows_from_batch(path):
    """Read the batch table (not duplicate checklist) in original order."""
    rows = []
    for line in path.read_text(encoding='utf-8').splitlines():
        match = re.match(r'^\|\s*\d+\s*\|\s*\[(\d+)\.\s*(.*?)\]\((https://leetcode\.com/problems/[^)]+)\)\s*\|\s*(Easy|Medium|Hard)\s*\|\s*(Not Started|Attempted)\s*\|\s*(Premium|Free)\s*\|', line)
        if match:
            number, title, url, difficulty, status, access = match.groups()
            rows.append({'ID': number, 'Title': title, 'URL': url, 'Difficulty': difficulty, 'Status': status, 'Premium': 'Yes' if access == 'Premium' else 'No'})
    if not rows:
        raise RuntimeError('No problems found in batch table: %s' % path)
    return rows


def enrich_details(session, rows, destination, delay):
    """Fetch official statements and C++ template; cache every successful fetch."""
    cache_dir = destination / '.leetcode_question_cache'
    cache_dir.mkdir(parents=True, exist_ok=True)
    lines = ['# LeetCode Problem Statements and C++11/14 Signatures', '',
             '**Problems:** %d  ' % len(rows),
             '**Source:** LeetCode GraphQL question content and C++ starter templates', '',
             '> The C++ starter template is copied from LeetCode. It is not an optimized solution.', '']
    failures = []
    for index, row in enumerate(rows, 1):
        slug = urlparse(row['URL']).path.strip('/').split('/')[-1]
        cache_path = cache_dir / (slug + '.json')
        try:
            if cache_path.exists():
                q = json.loads(cache_path.read_text(encoding='utf-8'))
            else:
                q = post(session, DETAIL_QUERY, {'titleSlug': slug}).get('question')
                if not q or not q.get('content'):
                    raise RuntimeError('LeetCode returned no question content (check Premium access)')
                cache_path.write_text(json.dumps(q, ensure_ascii=False, indent=2), encoding='utf-8')
                if delay and index < len(rows):
                    time.sleep(delay)
            snippets = q.get('codeSnippets') or []
            cpp = next((snippet.get('code') for snippet in snippets if snippet.get('langSlug') in ('cpp', 'cpp14') or snippet.get('lang') == 'C++'), None)
            lines += ['## %d. %s. %s' % (index, row['ID'], row['Title']), '',
                      '**Problem:** [%s](%s)  ' % (row['Title'], row['URL']),
                      '**Difficulty:** %s | **Status:** %s | **Access:** %s' % (row['Difficulty'], row['Status'], 'Premium' if row['Premium'] == 'Yes' else 'Free'), '',
                      '### Problem statement', '', markdown_description(q['content']), '',
                      '### LeetCode C++ starter code / required signature', '']
            if cpp:
                lines += ['```cpp', cpp.rstrip(), '```', '']
            else:
                lines += ['_No C++ starter code was returned by LeetCode; verify the signature on the problem page._', '']
            print('[%d/%d] OK %s' % (index, len(rows), slug), flush=True)
        except (RuntimeError, requests.RequestException, ValueError) as exc:
            failures.append((slug, str(exc)))
            lines += ['## %d. %s. %s' % (index, row['ID'], row['Title']), '',
                      '[Open problem](%s)' % row['URL'], '',
                      '**Fetch failed:** %s' % str(exc), '']
            print('[%d/%d] FAILED %s: %s' % (index, len(rows), slug, exc), file=sys.stderr, flush=True)
        # Checkpoint after each problem, so interruptions preserve progress.
        (destination / 'leetcode_problem_statements.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('Saved: %s' % (destination / 'leetcode_problem_statements.md'))
    print('Fetched: %d | Failed: %d' % (len(rows) - len(failures), len(failures)))
    if failures:
        print('Retry the same command: successful questions are cached, failed ones will be retried.', file=sys.stderr)



def post(session, query, variables=None, retries=3):
    for attempt in range(retries):
        try:
            response = session.post(URL, json={'query': query, 'variables': variables or {}}, timeout=35)
            if response.status_code in (401, 403, 429):
                raise RuntimeError('HTTP %s: authentication, Cloudflare, or rate limiting. Check cookies and try again later.' % response.status_code)
            try:
                result = response.json()
            except ValueError:
                raise RuntimeError('HTTP %s: non-JSON response (possibly Cloudflare): %s' % (response.status_code, response.text[:500]))
            if result.get('errors'):
                raise RuntimeError('GraphQL error (HTTP %s): %s' % (response.status_code, result['errors']))
            if not response.ok:
                raise RuntimeError('HTTP %s: %s' % (response.status_code, response.text[:700]))
            return result.get('data') or {}
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as exc:
            if attempt == retries - 1:
                raise RuntimeError('Request failed: %s' % exc)
            time.sleep(2 ** attempt)


def save_csv(path, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)



def save_markdown(path, rows, username, total_scanned, solved):
    """Write a complete, linked Markdown checklist of account-unresolved algorithms."""
    attempted = [r for r in rows if r['Status'] == 'Attempted']
    not_started = [r for r in rows if r['Status'] == 'Not Started']
    lines = [
        '# LeetCode Unresolved Algorithm Questions', '',
        '**Account:** `%s`  ' % username,
        '**Scope:** Account-level unresolved (Premium + Free); see scan summary for category scope  ',
        '**Generated:** %s  ' % time.strftime('%Y-%m-%d %H:%M:%S %Z'),
        '', '## Summary', '',
        '| Metric | Count |', '|---|---:|',
        '| Questions scanned | %d |' % total_scanned,
        '| Solved (excluded) | %d |' % solved,
        '| Unresolved in selected difficulty | %d |' % len(rows),
        '| Not Started | %d |' % len(not_started),
        '| Attempted | %d |' % len(attempted),
        '| Premium unresolved | %d |' % sum(r['Premium'] == 'Yes' for r in rows),
        '| Free unresolved | %d |' % sum(r['Premium'] == 'No' for r in rows),
        '', '> Completion status is account-wide, not C++-specific. Checkboxes are intentionally unchecked for all unresolved problems.',
        ''
    ]
    for heading, subset in [('Not Started', not_started), ('Attempted (not accepted)', attempted)]:
        lines += ['## %s (%d)' % (heading, len(subset)), '']
        for difficulty in ('Easy', 'Medium', 'Hard'):
            selected = [r for r in subset if str(r['Difficulty']).strip().lower() == difficulty.lower()]
            lines += ['### %s (%d)' % (difficulty, len(selected)), '']
            if not selected:
                lines += ['_None_', '']
                continue
            for r in selected:
                title = str(r['Title']).replace('[', r'\[').replace(']', r'\]')
                lines.append('- [ ] **%s.** [%s](%s) — %s' % (
                    r['ID'], title, r['URL'], 'Premium' if r['Premium'] == 'Yes' else 'Free'))
            lines.append('')
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')

def make_session(parser):
    cookie = os.environ.get('LEETCODE_SESSION')
    csrf = os.environ.get('csrftoken') or os.environ.get('CSRF_TOKEN')
    if not cookie or not csrf:
        parser.error('Export both LEETCODE_SESSION and csrftoken before running.')

    session = requests.Session()
    session.cookies.set('LEETCODE_SESSION', cookie, domain='.leetcode.com', path='/')
    session.cookies.set('csrftoken', csrf, domain='.leetcode.com', path='/')
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Origin': 'https://leetcode.com',
        'Referer': 'https://leetcode.com/problemset/algorithms/',
        'X-CSRFToken': csrf,
    })
    return session


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', default='.')
    parser.add_argument('--difficulty', choices=['All', 'Easy', 'Medium', 'Hard'], default='All')
    parser.add_argument('--page-size', type=int, default=50)
    parser.add_argument('--all-categories', action='store_true', help='Scan all categories (for comparison with the profile-wide unsolved count); default is Algorithms only')
    parser.add_argument('--from-csv', action='store_true', help='Regenerate Markdown from existing leetcode_unresolved.csv without API requests')
    parser.add_argument('--delay', type=float, default=1.5)
    parser.add_argument('--details', action='store_true', help='Fetch full statements and LeetCode C++ starter signatures')
    parser.add_argument('--batch-file', type=Path, help='Enrich only problems in a batch_XX.md file (no full scan)')
    args = parser.parse_args()
    if args.page_size < 1 or args.delay < 0:
        parser.error('--page-size must be >= 1 and --delay must be >= 0')
    if args.batch_file and args.from_csv:
        parser.error('Use --batch-file or --from-csv, not both')
    if args.batch_file and not args.details:
        parser.error('--batch-file requires --details')
    if args.batch_file:
        rows = rows_from_batch(args.batch_file)
        dest = Path(args.output_dir)
        dest.mkdir(parents=True, exist_ok=True)
        session = make_session(parser)
        enrich_details(session, rows, dest, args.delay)
        return
    if args.from_csv:
        dest = Path(args.output_dir)
        csv_path = dest / 'leetcode_unresolved.csv'
        if not csv_path.is_file():
            parser.error('CSV not found: %s' % csv_path)
        with csv_path.open(newline='', encoding='utf-8-sig') as f:
            rows = list(csv.DictReader(f))
        for row in rows:
            row['Difficulty'] = str(row.get('Difficulty') or '').strip().title()
        invalid = sorted(set(row['Difficulty'] for row in rows) - {'Easy', 'Medium', 'Hard'})
        if invalid:
            parser.error('Unexpected difficulty values in CSV: %s' % invalid)
        if args.details:
            session = make_session(parser)
            enrich_details(session, rows, dest, args.delay)
            return
        save_markdown(dest / 'leetcode_unresolved.md', rows, 'sinha4545',
                      len(rows), 0)
        print('Regenerated %s with %d clickable problem links.' % (
            dest / 'leetcode_unresolved.md', len(rows)))
        print('Note: scan/solved totals are unavailable in CSV-only mode.')
        return
    session = make_session(parser)
    try:
        status = (post(session, USER_QUERY).get('userStatus') or {})
        if not status.get('isSignedIn'):
            raise RuntimeError('Not authenticated. Check LEETCODE_SESSION/csrftoken; refusing to misclassify solved problems.')
        print('Signed in as: %s | Premium: %s' % (status.get('username'), status.get('isPremium')))
        if not status.get('isPremium'):
            print('Warning: account does not report Premium; premium problems will still be listed if returned.')

        offset = 0
        total = None
        seen = set()
        rows = []
        solved = 0
        status_counts = {'Solved': 0, 'Attempted': 0, 'Not Started': 0}
        category = None if args.all_categories else 'algorithms'
        print('Scope: %s | Difficulty: %s' % ('ALL categories' if args.all_categories else 'Algorithms only', args.difficulty))
        while total is None or offset < total:
            data = post(session, QUERY, {
                'categorySlug': category, 'limit': args.page_size,
                'skip': offset, 'filters': {'filterCombineType': 'ALL'},
            }).get('problemsetQuestionListV2')
            if not data:
                raise RuntimeError('Question list unavailable; LeetCode may have changed its GraphQL schema.')
            page_total = data.get('totalLength')
            if total is not None and page_total != total:
                raise RuntimeError('Catalog changed during scan (%s -> %s). Please rerun.' % (total, page_total))
            total = page_total
            questions = data.get('questions') or []
            if total is None or (not questions and offset < total):
                raise RuntimeError('Incomplete question listing; refusing to write a partial export.')
            for q in questions:
                if str(q.get('status') or '').lower() not in ('', 'ac', 'solved', 'accepted', 'notac', 'tried', 'attempted', 'not_started', 'to_do', 'todo'):
                    raise RuntimeError('Unrecognized question status %r; refusing to misclassify problems.' % q.get('status'))
                slug = q.get('titleSlug')
                if not slug:
                    raise RuntimeError('Question without titleSlug at offset %d' % offset)
                if slug in seen:
                    raise RuntimeError('Duplicate question %s: catalog pagination shifted during scan. Rerun.' % slug)
                seen.add(slug)
                raw_status = str(q.get('status') or '').lower()
                if raw_status in ('ac', 'solved', 'accepted'):
                    solved += 1
                    status_counts['Solved'] += 1
                    continue
                normalized_status = 'Attempted' if raw_status in ('notac', 'tried', 'attempted') else 'Not Started'
                status_counts[normalized_status] += 1
                if args.difficulty != 'All' and q.get('difficulty') != args.difficulty:
                    continue
                rows.append({
                    'ID': q.get('questionFrontendId', ''),
                    'Title': q.get('title', ''),
                    'Difficulty': str(q.get('difficulty') or '').strip().title(),
                    'Status': normalized_status,
                    'Premium': 'Yes' if q.get('paidOnly') else 'No',
                    'URL': 'https://leetcode.com/problems/%s/' % slug,
                })
            offset += len(questions)
            if offset > total:
                raise RuntimeError('Pagination exceeded reported catalog total.')
            if data.get('hasMore') is False and offset < total:
                raise RuntimeError('LeetCode reports no more pages before catalog total was reached.')
            print('Scanned %d/%d | unresolved selected %d' % (offset, total, len(rows)), flush=True)
            if offset < total:
                time.sleep(args.delay)

        def sortkey(row):
            identifier = str(row['ID'])
            return (0, int(identifier)) if identifier.isdigit() else (1, identifier)

        if len(seen) != total:
            raise RuntimeError('Incomplete catalog: expected %d distinct problems but got %d.' % (total, len(seen)))
        if sum(status_counts.values()) != len(seen):
            raise RuntimeError('Status counts do not reconcile; refusing partial export.')
        rows.sort(key=sortkey)
        dest = Path(args.output_dir)
        dest.mkdir(parents=True, exist_ok=True)
        attempted = [r for r in rows if r['Status'] == 'Attempted']
        new = [r for r in rows if r['Status'] == 'Not Started']
        save_csv(dest / 'leetcode_unresolved.csv', rows)
        save_csv(dest / 'leetcode_attempted.csv', attempted)
        save_csv(dest / 'leetcode_not_started.csv', new)
        save_markdown(dest / 'leetcode_unresolved.md', rows, status.get('username'), len(seen), solved)
        if args.details:
            enrich_details(session, rows, dest, args.delay)
        print('\nScanned: %d | Solved: %d | Unresolved: %d' % (len(seen), solved, len(rows)))
        print('Not started: %d | Attempted: %d' % (len(new), len(attempted)))
        print('Unresolved premium: %d | free: %d' % (
            sum(r['Premium'] == 'Yes' for r in rows), sum(r['Premium'] == 'No' for r in rows)))
        report = {
            'username': status.get('username'),
            'scope': 'all categories' if args.all_categories else 'algorithms',
            'difficulty': args.difficulty,
            'catalog_total': len(seen),
            'status_counts_all_difficulties': status_counts,
            'exported_unresolved': len(rows),
            'exported_todo': len(new),
            'exported_attempted': len(attempted),
            'premium_unresolved': sum(r['Premium'] == 'Yes' for r in rows),
            'free_unresolved': sum(r['Premium'] == 'No' for r in rows),
        }
        (dest / 'leetcode_scan_summary.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        print('Full-scope status totals: %s' % status_counts)
        print('Saved CSV, Markdown, and scan summary to %s' % dest.resolve())
        print('Note: status is account-wide, not C++-language-specific.')
    except (RuntimeError, requests.RequestException) as exc:
        print('ERROR: %s' % exc, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
