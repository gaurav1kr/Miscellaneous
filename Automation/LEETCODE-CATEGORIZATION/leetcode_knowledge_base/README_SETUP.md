# Private LeetCode C++ Interview Knowledge Base

This is a **local collector**, not a hosted service. It uses LeetCode's unofficial GraphQL endpoints, which can change, rate-limit, or refuse requests. Your solved list and Premium content require an authenticated session. A solved problem may have only a Java/Python submission or inaccessible submission source; those entries are flagged rather than filled with invented code.

## Install

```bash
python3 -m venv leetcode-kb-env
source leetcode-kb-env/bin/activate
python3 -m pip install -r requirements.txt
```

## Authentication

Export your existing browser session tokens **in your own terminal** (never paste them into chat or a script). Keep them out of shell history and screenshots.

```bash
read -rsp 'LEETCODE_SESSION: ' LEETCODE_SESSION; echo
export LEETCODE_SESSION
read -rsp 'csrftoken: ' csrftoken; echo
export csrftoken
```

## Run a 5-problem smoke test first

```bash
python3 leetcode_kb.py --max-problems 5 --output ./my_leetcode_kb
```

Then process the full catalog (resumes from per-problem JSON cache):

```bash
python3 leetcode_kb.py --output ./my_leetcode_kb --delay 1.5
```

If you already have your own C++ solutions named `50.cpp`, `powx-n.cpp`, `50.md`, or `powx-n.md`, place them in one directory and use:

```bash
python3 leetcode_kb.py --output ./my_leetcode_kb --local-solutions ./my_cpp_solutions
```

The collector prioritizes local files over online accepted submissions. Local code is labeled as local and is **not** claimed to be Accepted. To retry missing code after obtaining more submissions, use `--refresh` (this re-fetches everything); to rebuild topic Markdown offline, use `--build-only`.

## Output

- `my_leetcode_kb/README.md` — topic index and counts.
- `my_leetcode_kb/topics/*.md` — per-topic problem list, descriptions, pattern recognition, DS inference, and available C++ code.
- `my_leetcode_kb/missing_code.csv` — gaps to resolve.
- `my_leetcode_kb/cache/problems/*.json` — resumable private records.
- `my_leetcode_kb/cache/failures.json` — transient failures.

**Accuracy limitation:** This first version classifies by LeetCode topic tags plus simple source-code clues. The approach is a **topic-level recognition hint**, not a proven problem-specific explanation. Time and space complexity require actual code review; the script marks them as unverified rather than guessing. For exhaustive interview prep, a second offline enrichment pass can analyze each accepted C++ solution and attach manually reviewed complexity, invariant, edge cases, and alternative approaches.

**Privacy:** Session cookies stay in environment variables; the script does not write them to files. Treat generated Premium descriptions and your solutions as private, and do not publish them without checking applicable terms and rights.
