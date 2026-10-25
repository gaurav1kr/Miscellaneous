# LeetCode Automation Setup and Execution

This guide explains how to set up the Python environment, generate problem batches, configure LeetCode authentication, and run the submission script.

## 1. Install Python and Create a Virtual Environment

Ensure Python 3 and `pip` are installed. Then create and activate a virtual environment:

```bash
python3 -m venv leetcode-env
source leetcode-env/bin/activate
python -m pip install --upgrade pip
```

## 2. Install Required Packages

Install the packages referenced in the original setup notes:

```bash
python -m pip install selenium playwright requests beautifulsoup4 markdownify
```

## 3. Generate Problem Batches

Run the unresolved-problems script:

```bash
python leetcode_unresolved_complete.py \
  --difficulty All \
  --output-dir ./remaining_algorithms
```

The script creates multiple problem batches in `remaining_algorithms/`. Combine the required batches into one Markdown file named **`final_batch.md`** before submission.

## 4. Configure LeetCode Authentication

1. Open [LeetCode](https://leetcode.com/) and sign in.
2. Press **F12** to open Developer Tools.
3. Go to **Application → Cookies → https://leetcode.com** (the domain may appear as `www.leetcode.com`).
4. Locate the cookies named `LEETCODE_SESSION` and `csrftoken`.
5. Set their values as environment variables in your terminal:

```bash
read -rsp 'LEETCODE_SESSION: ' LEETCODE_SESSION; echo
export LEETCODE_SESSION

read -rsp 'LEETCODE_CSRFTOKEN: ' LEETCODE_CSRFTOKEN; echo
export LEETCODE_CSRFTOKEN
```

> **Security:** Treat these cookie values as passwords. Never commit them to Git or paste them into shared logs or files.

## 5. Run the Submission Script

After preparing `final_batch.md` and setting the environment variables, run:

```bash
python -u submit.py final_batch.md \
  --execute \
  --start 1 \
  --delay 60 \
  --timeout 180
```

### Command Options

| Option | Value | Purpose |
|---|---|---|
| Input file | `final_batch.md` | Markdown file containing problem solutions |
| `--execute` | — | Enables actual submissions |
| `--start` | `1` | Starts processing at entry 1 |
| `--delay` | `60` | Delay setting passed to the script |
| `--timeout` | `180` | Timeout setting passed to the script |

> **Note:** The exact behavior and units of the options depend on your `submit.py` implementation.
