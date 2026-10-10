#!/usr/bin/env python3
"""Export authenticated LeetCode Dynamic Programming problem status.

Requires: pip install requests pandas openpyxl
Set LEETCODE_SESSION and LEETCODE_CSRF environment variables.
"""
import os
import sys
import time
from pathlib import Path

import pandas as pd
import requests

URL = 'https://leetcode.com/graphql/'
PAGE_SIZE = 100
QUERY = '''
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(categorySlug: $categorySlug, limit: $limit, skip: $skip, filters: $filters) {
    total: totalNum
    questions: data {
      questionFrontendId
      title
      titleSlug
      difficulty
      status
      topicTags { name slug }
    }
  }
}
'''


def session_from_environment():
    token = os.getenv('LEETCODE_SESSION', '').strip()
    csrf = os.getenv('LEETCODE_CSRF', '').strip()
    if not token or not csrf:
        raise RuntimeError('Set LEETCODE_SESSION and LEETCODE_CSRF in your terminal before running.')
    session = requests.Session()
    session.cookies.set('LEETCODE_SESSION', token, domain='.leetcode.com')
    session.cookies.set('csrftoken', csrf, domain='.leetcode.com')
    session.headers.update({
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Origin': 'https://leetcode.com',
        'Referer': 'https://leetcode.com/problemset/',
        'x-csrftoken': csrf,
        'User-Agent': 'Mozilla/5.0 (compatible; LeetCodeDPTracker/1.0)',
    })
    return session


def graphql(session, variables):
    response = session.post(URL, json={'query': QUERY, 'variables': variables}, timeout=30)
    if response.status_code != 200:
        # Avoid dumping full HTML responses or potentially sensitive headers/cookies.
        try:
            error = response.json()
            details = str(error.get('errors', error))[:1200]
        except ValueError:
            details = 'Non-JSON response (possibly a block or authentication challenge).'
        raise RuntimeError(f'LeetCode HTTP {response.status_code}: {details}')
    try:
        payload = response.json()
    except ValueError as exc:
        raise RuntimeError('LeetCode returned non-JSON data.') from exc
    if payload.get('errors'):
        raise RuntimeError(f'LeetCode GraphQL error: {str(payload["errors"])[:1200]}')
    data = (payload.get('data') or {}).get('problemsetQuestionList')
    if data is None:
        raise RuntimeError('Unexpected GraphQL response: missing problemsetQuestionList.')
    return data


def fetch_dp_problems(session):
    problems = []
    skip = 0
    while True:
        result = graphql(session, {
            'categorySlug': '',
            'limit': PAGE_SIZE,
            'skip': skip,
            'filters': {'tags': ['dynamic-programming']},
        })
        batch = result.get('questions') or []
        total = result.get('total')
        problems.extend(batch)
        print(f'Fetched {len(problems)} / {total if total is not None else "?"} DP problems')
        if not batch or (total is not None and len(problems) >= total):
            break
        skip += len(batch)
        time.sleep(0.6)
    return problems


def main():
    session = session_from_environment()
    problems = fetch_dp_problems(session)
    if not problems:
        raise RuntimeError('No DP problems returned. API filters may have changed.')

    rows = []
    for problem in problems:
        if not problem:
            continue
        tags = {tag.get('slug') for tag in problem.get('topicTags') or []}
        if 'dynamic-programming' not in tags:
            continue
        raw_status = problem.get('status')
        if raw_status == 'ac':
            status = 'Solved'
        elif raw_status in ('notac', None):
            status = 'Unsolved' if raw_status == 'notac' else 'Unknown'
        else:
            status = 'Unknown'
        rows.append({
            'Problem ID': problem.get('questionFrontendId'),
            'Title': problem.get('title'),
            'Difficulty': problem.get('difficulty'),
            'Status': status,
            'URL': 'https://leetcode.com/problems/' + problem['titleSlug'] + '/',
        })

    if not rows:
        raise RuntimeError('No tagged DP problems returned. LeetCode API may have changed.')
    df = pd.DataFrame(rows).drop_duplicates(subset=['URL'])
    if (df['Status'] == 'Unknown').all():
        raise RuntimeError('LeetCode did not return solved statuses. Check login cookies; no misleading report was generated.')
    solved = df[df['Status'] == 'Solved'].copy()
    summary = pd.DataFrame([
        {'Difficulty': d, 'Solved': int((solved['Difficulty'] == d).sum()),
         'Total': int((df['Difficulty'] == d).sum())}
        for d in ('Easy', 'Medium', 'Hard')
    ])
    out = Path.cwd()
    df.to_csv(out / 'all_dp_problems.csv', index=False)
    solved.to_csv(out / 'solved_dp_problems.csv', index=False)
    with pd.ExcelWriter(out / 'leetcode_dp_tracker.xlsx', engine='openpyxl') as writer:
        solved.to_excel(writer, sheet_name='Solved DP', index=False)
        df.to_excel(writer, sheet_name='All DP', index=False)
        summary.to_excel(writer, sheet_name='Summary', index=False)
        for sheet in writer.sheets.values():
            sheet.freeze_panes = 'A2'
            sheet.auto_filter.ref = sheet.dimensions
            for col, width in {'A': 16, 'B': 52, 'C': 17, 'D': 17, 'E': 65}.items():
                sheet.column_dimensions[col].width = width
    print('\nDP problems:', len(df))
    print('Solved:', len(solved))
    print(summary.to_string(index=False))
    print('\nCreated: leetcode_dp_tracker.xlsx, solved_dp_problems.csv, all_dp_problems.csv')
    if (df['Status'] == 'Unknown').any():
        print('WARNING: Some problems have unknown status. Verify your authentication.')


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, requests.RequestException) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
