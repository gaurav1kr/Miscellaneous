# Work Schedule — All Possible Schedules

## Problem Statement

Implement the function:

```cpp
vector<string> findSchedules(int workHours, int dayHours, string pattern);
```

Given a weekly work schedule represented by a string `pattern`, generate **all possible schedules** whose total working hours equal `workHours`.

- Each digit in `pattern` is a fixed number of hours for that day and must remain unchanged.
- Each `?` is an unknown number of hours that can be replaced by an integer from `0` to `dayHours`, inclusive.
- The sum of the hours across the completed schedule must equal `workHours`.
- Return every valid completed schedule as a string, in ascending order of the values assigned to the unknown positions.

**Note:** In this problem, `dayHours` limits the values used to replace `?`. Fixed digits are preserved even if they are greater than `dayHours`, as in the example below.

### Example

**Input**

```text
workHours = 24
dayHours = 4
pattern = "08??840"
```

**Output**

```text
0804840
0813840
0822840
0831840
0840840
```

**Explanation:** The fixed digits add up to `0 + 8 + 8 + 4 + 0 = 20`, leaving `24 - 20 = 4` hours for the two `?` positions. The valid pairs are `(0,4)`, `(1,3)`, `(2,2)`, `(3,1)`, and `(4,0)`.

## Approach — Backtracking (Original Solution)

1. Traverse the pattern and subtract all fixed digits from `workHours`. This gives the hours still to assign.
2. Start a recursive DFS at index `0`.
3. If the current position contains a fixed digit, leave it unchanged and recurse to the next position.
4. If the current position is `?`, try every value from `0` to `dayHours` that does not exceed the remaining hours.
5. For each choice, replace `?` with the digit, subtract the chosen hours, and recurse to the next position.
6. Once all positions have been processed, save the completed schedule **only if the remaining hours equal zero**.
7. Restore the `?` after exploring its choices, so other combinations can be tried.

This is the **original DFS/backtracking approach**, not the later optimized version that directly calculates the last unknown value.

## C++11/14 Code

```cpp
#include <bits/stdc++.h>
using namespace std;

void dfs(int index, int remaining, int dayHours,
         string &pattern, vector<string> &ans) {

    if (index == pattern.size()) {
        if (remaining == 0)
            ans.push_back(pattern);
        return;
    }

    if (pattern[index] != '?') {
        dfs(index + 1, remaining, dayHours, pattern, ans);
        return;
    }

    for (int i = 0; i <= dayHours && i <= remaining; i++) {
        pattern[index] = '0' + i;
        dfs(index + 1, remaining - i, dayHours, pattern, ans);
    }

    pattern[index] = '?';
}

vector<string> findSchedules(int workHours, int dayHours,
                             string pattern) {
    vector<string> ans;

    for (char c : pattern) {
        if (c != '?')
            workHours -= c - '0';
    }

    if (workHours < 0)
        return ans;

    dfs(0, workHours, dayHours, pattern, ans);
    return ans;
}
```

## Complexity Analysis

Let:

- `n` = length of `pattern`
- `k` = number of `?` characters
- `D` = `dayHours`

**Time complexity:** `O(n + (D + 1)^k * n)` in the worst case, including copying completed schedules into the result. Each unknown position has up to `D + 1` choices, so there can be up to `(D + 1)^k` combinations. Checking and storing a valid schedule takes `O(n)` time.

**Auxiliary space complexity:** `O(n)` for the recursive call stack, excluding the output.

**Output space:** `O(S * n)`, where `S` is the number of valid schedules returned.

## Interview Summary

> I first subtract the fixed working hours from the weekly total. Then I use backtracking to replace each question mark with a value from zero to the daily limit. I track the remaining hours and add a schedule to the result only when all positions are filled and the remaining hours are zero.
