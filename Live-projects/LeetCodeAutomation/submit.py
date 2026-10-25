#!/usr/bin/env python3
"""LeetCode Markdown -> Chrome Selenium, using an existing debugging Chrome session."""
import argparse
import csv
import hashlib
import re
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

LINK = re.compile(r'https://leetcode\.com/problems/([a-z0-9-]+)/?')
CODE = re.compile(r'```(?:cpp|c\+\+|cc)\s*\n(.*?)\n```', re.I | re.S)
FIELDS = ['url', 'sha256', 'verdict', 'timestamp', 'details']


def parse_markdown(path):
    text = path.read_text(encoding='utf-8')
    matches = list(LINK.finditer(text))
    items, seen = [], set()
    for i, match in enumerate(matches):
        url = 'https://leetcode.com/problems/' + match.group(1) + '/'
        if url in seen:
            print('Warning: duplicate URL ignored:', url, flush=True)
            continue
        seen.add(url)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        found = CODE.search(text, match.end(), end)
        code = found.group(1).strip() + '\n' if found else None
        items.append((url, code))
    if not items:
        raise ValueError('No LeetCode links found')
    return items


def load_accepted(path):
    accepted = set()
    if path.exists():
        with path.open(newline='', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                if row.get('verdict', '').strip().lower() == 'accepted':
                    accepted.add(row.get('url', ''))
    return accepted


def log_result(path, url, code, verdict, details=''):
    new = not path.exists() or path.stat().st_size == 0
    with path.open('a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            writer.writeheader()
        writer.writerow(dict(url=url, sha256=hashlib.sha256(code.encode()).hexdigest(),
                             verdict=verdict, timestamp=time.strftime('%Y-%m-%d %H:%M:%S'),
                             details=details[:1000]))


def editor_status(driver, code=None):
    # Only return serializable data to Selenium, not Monaco editor objects.
    return driver.execute_script(r"""
        const value = arguments[0];
        const state = (function(){
            if (!window.monaco || !window.monaco.editor || !window.monaco.editor.getEditors)
                return {ok:false, reason:'Monaco not ready'};
            const visible=window.monaco.editor.getEditors().filter(e => {
                const n=e.getDomNode();
                return n && n.isConnected && n.getBoundingClientRect().width>0 &&
                       n.getBoundingClientRect().height>0;
            });
            if (visible.length!==1) return {ok:false, reason:'Visible editors: '+visible.length};
            const e=visible[0], m=e.getModel();
            if (!m) return {ok:false, reason:'No model'};
            if (!/cpp|c\+\+|cxx/i.test(m.getLanguageId()))
                return {ok:false, reason:'Select C++14; language is '+m.getLanguageId()};
            return {ok:true, editor:e, model:m};
        })();
        if (!state.ok) return state;
        const actual=state.editor.getValue();
        return {ok:true, matches:value===null || actual===value,
                length:actual.length, modelUri:String(state.model.uri),
                language:state.model.getLanguageId()};
    """, code)


def set_cpp_editor(driver, code, timeout):
    # Wait for hydration/saved-code restoration to settle BEFORE inserting code.
    # Recheck after writing: LeetCode can still restore the model asynchronously.
    end=time.monotonic()+timeout
    last=None
    while time.monotonic()<end:
        state=editor_status(driver)
        if state.get('ok'):
            identity=(state['modelUri'], state['length'])
            if identity==last:
                break
            last=identity
        else:
            last=None
        time.sleep(1)
    else:
        raise RuntimeError('C++ Monaco editor never stabilized: '+str(state))

    for attempt in range(1, 5):
        outcome=driver.execute_script(r"""
            const expected=arguments[0];
            if (!window.monaco || !window.monaco.editor.getEditors) return {ok:false,reason:'No Monaco'};
            const es=window.monaco.editor.getEditors().filter(e => {
                const n=e.getDomNode(); return n && n.isConnected &&
                  n.getBoundingClientRect().width>0 && n.getBoundingClientRect().height>0;
            });
            if(es.length!==1 || !es[0].getModel()) return {ok:false,reason:'Editor changed'};
            if(!/cpp|c\+\+|cxx/i.test(es[0].getModel().getLanguageId()))
                return {ok:false,reason:'Editor not C++'};
            es[0].setValue(expected);
            es[0].focus();
            return {ok:es[0].getValue()===expected};
        """, code)
        if not outcome.get('ok'):
            raise RuntimeError('Unable to write code to visible Monaco editor: '+str(outcome))
        # Verify the entire code remains identical across several seconds.
        stable=True
        for _ in range(5):
            time.sleep(1)
            state=editor_status(driver, code)
            if not state.get('ok') or not state.get('matches'):
                stable=False
                print('  Editor overwritten after insertion; retrying (%d/4)' % attempt, flush=True)
                break
        if stable:
            return
    raise RuntimeError('LeetCode keeps overwriting the editor; NOT submitting')


def choose_cpp(driver):
    # Do not silently overwrite code in a different language.
    language = driver.execute_script('''
        if (!window.monaco || !window.monaco.editor) return null;
        const models = window.monaco.editor.getModels();
        return models.length ? models[0].getLanguageId() : null;
    ''')
    if language and not re.search(r'cpp|c\+\+|cxx', language, re.I):
        raise RuntimeError('Editor language is %s, not C++; select C++14 manually' % language)


def find_submit(driver):
    selectors = [
        (By.CSS_SELECTOR, '[data-e2e-locator="console-submit-button"]'),
        (By.XPATH, '//button[normalize-space()="Submit"]'),
        (By.XPATH, '//*[@role="button" and normalize-space()="Submit"]'),
    ]
    for how, locator in selectors:
        for element in driver.find_elements(how, locator):
            if element.is_displayed() and element.is_enabled():
                return element
    return None


VERDICTS = ('Accepted', 'Wrong Answer', 'Time Limit Exceeded', 'Memory Limit Exceeded',
            'Runtime Error', 'Compile Error', 'Compilation Error', 'Output Limit Exceeded')


def verdict(driver):
    # The verdict is often on the submissions detail page, with adjacent test-count text.
    text = driver.find_element(By.TAG_NAME, 'body').text
    for label in VERDICTS:
        if re.search(r'(?m)^\s*' + re.escape(label) + r'(?=\s|$)', text):
            return label
    return None


def submit(driver, url, code, timeout):
    print('  Navigating to ' + url, flush=True)
    driver.get(url)
    print('  Checking Monaco editor...', flush=True)
    set_cpp_editor(driver, code, timeout)
    button=WebDriverWait(driver, timeout).until(lambda d: find_submit(d))
    state=editor_status(driver, code)
    if not state.get('ok') or not state.get('matches'):
        raise RuntimeError('Editor differs from Markdown before Submit; NOT submitting: '+str(state))
    before_url=driver.current_url
    print('  Editor verified. Clicking Submit...', flush=True)
    button.click()
    start=time.monotonic()
    while time.monotonic()-start < timeout:
        current_url=driver.current_url
        # Only trust a result on a NEW numeric submission detail page.
        match=re.search(r'/submissions/(\d+)/?', current_url)
        if match:
            v=verdict(driver)
            if v:
                return v, 'Submission '+match.group(1)+' at '+current_url
        time.sleep(1)
    return 'Unknown/Timeout', 'Could not verify a new submission detail page: '+driver.current_url


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('markdown', type=Path)
    p.add_argument('--execute', action='store_true', help='Actually submit; default is dry-run')
    p.add_argument('--limit', type=int, default=0, help='Maximum number of entries from the start of the batch')
    p.add_argument('--start', type=int, default=1, help='1-based first entry to process (default: 1)')
    p.add_argument('--delay', type=float, default=15, help='Seconds between submissions')
    p.add_argument('--timeout', type=int, default=180)
    p.add_argument('--port', type=int, default=9222)
    p.add_argument('--page-timeout', type=int, default=60)
    p.add_argument('--results', type=Path, default=None)
    p.add_argument('--mark-accepted', action='append', default=[], metavar='SLUG',
                   help='Record a manually verified Accepted problem slug, without submitting it')
    args = p.parse_args()
    items = parse_markdown(args.markdown)
    if args.start < 1 or args.start > len(items):
        p.error('--start must be between 1 and %d' % len(items))
    if args.limit < 0:
        p.error('--limit cannot be negative')
    if args.limit:
        items = items[:args.limit]
    items = list(enumerate(items, 1))[args.start - 1:]
    results = args.results or args.markdown.with_name(args.markdown.stem + '_results.csv')
    accepted = load_accepted(results)
    for slug in args.mark_accepted:
        slug = slug.strip('/').split('/')[-1]
        matches = [(url, code) for _, (url, code) in items if url.rstrip('/').endswith('/' + slug)]
        if len(matches) != 1:
            p.error('Problem slug not found uniquely in Markdown: ' + slug)
        url, code = matches[0]
        if code is None:
            p.error('Cannot mark a problem with no C++ solution: ' + slug)
        if url not in accepted:
            log_result(results, url, code, 'Accepted', 'Manually verified on LeetCode')
            accepted.add(url)
            print('Marked Accepted (verified by user): ' + url, flush=True)
    print('Selected %d entries (%d with C++ code, %d without); execute=%s; results=%s' % (len(items), sum(code is not None for _, (_, code) in items), sum(code is None for _, (_, code) in items), args.execute, results), flush=True)
    if not args.execute:
        for i, (url, code) in items:
            print('%03d %s (%s)%s' % (i, url, str(len(code)) + ' chars' if code else 'NO C++ CODE', ' [accepted]' if url in accepted else ''))
        print('Dry-run complete. No browser opened, no submissions made.')
        return
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:%d' % args.port)
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as exc:
        p.error('Cannot connect to Chrome debugging port %d. Start Chrome with --remote-debugging-port=%d and a separate --user-data-dir. Details: %s' % (args.port, args.port, exc))
    driver.set_page_load_timeout(args.page_timeout)
    driver.set_script_timeout(max(30, args.timeout))
    try:
        for i, (url, code) in items:
            if code is None:
                print('[original #%d] Skip: no C++ code: %s' % (i, url), flush=True)
                continue
            if url in accepted:
                print('[original #%d] Skip accepted: %s' % (i, url), flush=True)
                continue
            print('[original #%d] Submitting %s' % (i, url), flush=True)
            try:
                print('  Opening problem and waiting for stable C++ editor...', flush=True)
                result, details = submit(driver, url, code, args.timeout)
            except Exception as e:
                result, details = 'Automation Error', str(e)
                screenshot = args.markdown.parent / ('error_%03d.png' % i)
                try:
                    driver.save_screenshot(str(screenshot))
                    details += ' screenshot=' + str(screenshot)
                except Exception:
                    pass
            print('  -> %s %s' % (result, details[:200]), flush=True)
            log_result(results, url, code, result, details)
            if result == 'Accepted':
                accepted.add(url)
            if result in ('Automation Error', 'Unknown/Timeout'):
                print('Stopping for safety. Retry with --start %d after checking the submission history.' % i, flush=True)
                break
            time.sleep(max(0, args.delay))
    finally:
        # Do not close the user's attached Chrome session.
        pass


if __name__ == '__main__':
    main()
