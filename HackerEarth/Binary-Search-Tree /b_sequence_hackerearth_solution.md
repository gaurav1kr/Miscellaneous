# B-Sequence — HackerEarth

## Problem Summary

A sequence is a **B-sequence** if:

- it is strictly increasing first,
- then strictly decreasing,
- the decreasing part may be absent,
- the maximum element appears exactly once,
- every other element appears at most twice,
- any element appearing in the decreasing part must also appear in the increasing part.

For each query value `val`, insert it only if the sequence remains a valid B-sequence.

After each query, print the current size of the sequence.

After all queries, print the final B-sequence.

---

## Key Observation

A valid B-sequence can be viewed as:

```text
Increasing part:
all distinct values in ascending order

Decreasing part:
all values that appear twice, in descending order
```

Example:

```text
1 2 5 2
```

can be represented as:

```text
Increasing values:
1 2 5

Values occurring twice:
2
```

Therefore we do not need to physically insert elements into the middle of a vector after every operation.

We only need to track how many times every value currently occurs:

```text
0 -> value is absent
1 -> value appears once
2 -> value already appears twice
```

---

## Insertion Rules

Let the current maximum value be `mx`.

For a query value `val`:

### Case 1 — `val == mx`

The maximum element must occur exactly once, so reject the insertion.

### Case 2 — `val > mx`

`val` becomes the new maximum:

```text
frequency[val] = 1
mx = val
size++
```

### Case 3 — `val < mx`

If `frequency[val] == 0`, this is its first occurrence and it belongs to the increasing part.

If `frequency[val] == 1`, this is its second occurrence and it belongs to the decreasing part.

If `frequency[val] == 2`, reject it.

---

## Optimized Approach

A direct `set`-based solution works, but every insertion/search costs `O(log N)` and tree nodes add memory overhead.

A faster and lower-memory approach is to use **coordinate compression** plus a byte-frequency array.

Since values may be as large as `10^9`, we cannot index an array directly by value.

Instead:

1. Read the initial sequence.
2. Read all query values.
3. Sort the query values and remove duplicates.
4. Give each distinct query value a compressed ID.
5. Maintain:

```cpp
unsigned char freq[M];
```

where:

```text
0 = absent
1 = appears once
2 = appears twice
```

The initial sequence is already a valid B-sequence, so we can identify its increasing part and decreasing part and initialize the frequencies only for values that may appear in future queries.

At the end, reconstruct the sequence by merging:

```text
initial increasing values + accepted new values
```

for the increasing side, and:

```text
initial decreasing values + values with frequency 2
```

for the decreasing side.

---

## C++17 Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

static const int MAXN = 100000 + 5;
static const int MAXQ = 100000 + 5;

static int initialSeq[MAXN];
static int queryVal[MAXQ];
static int compressed[MAXQ];

// 0 = absent, 1 = once, 2 = twice
static unsigned char freq[MAXQ];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    int mx = INT_MIN;

    for (int i = 0; i < N; ++i)
    {
        cin >> initialSeq[i];
        mx = max(mx, initialSeq[i]);
    }

    int Q;
    cin >> Q;

    for (int i = 0; i < Q; ++i)
    {
        cin >> queryVal[i];
        compressed[i] = queryVal[i];
    }

    // Coordinate compression on query values.
    sort(compressed, compressed + Q);

    int M = unique(
        compressed,
        compressed + Q
    ) - compressed;

    auto findId = [&](int x)
    {
        return int(
            lower_bound(
                compressed,
                compressed + M,
                x
            ) - compressed
        );
    };

    // Find the peak of the initial B-sequence.
    int peak = 0;

    while (
        peak + 1 < N &&
        initialSeq[peak] < initialSeq[peak + 1]
    )
    {
        ++peak;
    }

    // Initialize frequencies for query-relevant values
    // from the increasing part.
    for (int i = 0; i <= peak; ++i)
    {
        int x = initialSeq[i];

        auto it = lower_bound(
            compressed,
            compressed + M,
            x
        );

        if (it != compressed + M && *it == x)
        {
            freq[it - compressed] = 1;
        }
    }

    // Values in the decreasing part are second occurrences.
    for (int i = peak + 1; i < N; ++i)
    {
        int x = initialSeq[i];

        auto it = lower_bound(
            compressed,
            compressed + M,
            x
        );

        if (it != compressed + M && *it == x)
        {
            freq[it - compressed] = 2;
        }
    }

    int currentSize = N;

    // Process queries.
    for (int i = 0; i < Q; ++i)
    {
        int val = queryVal[i];

        // Current maximum cannot appear twice.
        if (val == mx)
        {
            cout << currentSize << '\n';
            continue;
        }

        int id = findId(val);

        // New maximum.
        if (val > mx)
        {
            mx = val;
            freq[id] = 1;

            ++currentSize;

            cout << currentSize << '\n';
            continue;
        }

        // val < mx

        if (freq[id] == 0)
        {
            freq[id] = 1;
            ++currentSize;
        }
        else if (freq[id] == 1)
        {
            freq[id] = 2;
            ++currentSize;
        }

        // freq == 2 -> reject

        cout << currentSize << '\n';
    }

    // Print increasing part by merging
    // initial increasing values and accepted query values.
    int i = 0;
    int j = 0;

    while (i <= peak || j < M)
    {
        int a =
            (i <= peak)
            ? initialSeq[i]
            : INT_MAX;

        int b =
            (j < M)
            ? compressed[j]
            : INT_MAX;

        if (a < b)
        {
            cout << a << ' ';
            ++i;
        }
        else if (b < a)
        {
            if (freq[j] >= 1)
                cout << b << ' ';

            ++j;
        }
        else
        {
            cout << a << ' ';

            ++i;
            ++j;
        }
    }

    // Print decreasing part by merging
    // initial decreasing values and query values
    // whose final frequency is 2.
    int di = peak + 1;
    int qj = M - 1;

    while (di < N || qj >= 0)
    {
        int a =
            (di < N)
            ? initialSeq[di]
            : INT_MIN;

        int b =
            (qj >= 0 && freq[qj] == 2)
            ? compressed[qj]
            : INT_MIN;

        if (qj >= 0 && freq[qj] != 2)
        {
            --qj;
            continue;
        }

        if (a > b)
        {
            cout << a << ' ';
            ++di;
        }
        else if (b > a)
        {
            cout << b << ' ';
            --qj;
        }
        else
        {
            if (a != INT_MIN)
                cout << a << ' ';

            ++di;
            --qj;
        }
    }

    cout << '\n';

    return 0;
}
```

---

## Example

Initial sequence:

```text
1 2 5 2
```

Queries:

```text
5
1
3
2
```

Processing:

```text
5 -> reject, because it is the maximum
1 -> second occurrence allowed
3 -> first occurrence allowed
2 -> reject, because it already occurs twice
```

Final sequence:

```text
1 2 3 5 2 1
```

---

## Time Complexity

Let:

```text
N = initial sequence size
Q = number of queries
M = number of distinct query values
```

with:

```text
M <= Q
```

Coordinate compression:

```text
O(Q log Q)
```

Initial frequency setup:

```text
O(N log Q)
```

Each query finds its compressed ID with binary search:

```text
O(log Q)
```

All queries:

```text
O(Q log Q)
```

Final merge/output:

```text
O(N + Q)
```

Therefore overall:

```text
O((N + Q) log Q)
```

---

## Space Complexity

Main arrays:

```text
initialSeq    O(N)
queryVal      O(Q)
compressed    O(Q)
freq          O(Q)
```

Therefore:

```text
O(N + Q)
```

For maximum constraints, algorithm-controlled memory is roughly:

```text
initialSeq      ~ 400 KB
queryVal        ~ 400 KB
compressed      ~ 400 KB
freq            ~ 100 KB
--------------------------------
total           ~ 1.3 MB
```

This excludes C++ runtime/process overhead reported by the judge.

---

## Interview Thought Process

```text
Need to preserve B-sequence
          |
          v
Each non-maximum value may occur at most twice
          |
          v
Only occurrence count 0 / 1 / 2 matters
          |
          v
Maximum must occur exactly once
          |
          v
No need to insert into the actual sequence each time
          |
          v
Track counts only
          |
          v
Values may be as large as 1e9
          |
          v
Coordinate compression
          |
          v
Byte-frequency array
          |
          v
Reconstruct final ordered sequence at the end
```

The core idea is:

> **Do not maintain the B-sequence itself during every insertion. Maintain only occurrence counts, then reconstruct the valid sequence at the end.**
