# Suarez --- HackerEarth

## Problem Summary

We are given `N` segments (intervals):

``` text
[L1, R1]
[L2, R2]
...
[LN, RN]
```

The length of a segment `[L, R]` is:

``` text
R - L + 1
```

For every query `(K, X)`, we need to find the **K-th smallest segment by
length among all segments that contain point `X`**.

A segment `[L, R]` contains `X` when:

``` text
L <= X <= R
```

If fewer than `K` segments contain `X`, the answer is:

``` text
-1
```

With large values of `N` and `Q`, checking every segment for every query
would be too slow.

------------------------------------------------------------------------

## Brute-Force Approach

For each query `(K, X)`:

1.  Check all `N` intervals.
2.  Keep intervals satisfying:

``` text
L <= X <= R
```

3.  Calculate their lengths.
4.  Sort the lengths.
5.  Return the `K`-th smallest one.

If there are `Q` queries, this can require approximately:

``` text
O(Q * N log N)
```

which is not practical when both `N` and `Q` are large.

We therefore need to process the queries together.

------------------------------------------------------------------------

# Optimized Approach

The optimized solution combines three ideas:

1.  **Sort intervals by length**
2.  **Fenwick Tree (Binary Indexed Tree)**
3.  **Parallel Binary Search**

------------------------------------------------------------------------

## Observation 1 --- Sort Segments by Length

Sort all intervals in increasing order of:

``` text
R - L + 1
```

Suppose the sorted lengths are:

``` text
2, 4, 5, 7, 10
```

For a query `(K, X)`, imagine considering only the first `m` intervals.

Ask:

> How many of the first `m` intervals contain `X`?

Suppose for a particular `X` the intervals of lengths:

``` text
2, 5, 10
```

contain it.

Then as we increase the prefix size:

``` text
Prefix        # intervals containing X

1                       1
2                       1
3                       2
4                       2
5                       3
```

For `K = 2`, the condition:

``` text
count >= K
```

looks like:

``` text
false false true true true
```

This condition is **monotonic**.

Therefore we can binary-search for the first prefix where:

``` text
count >= K
```

The interval at that position gives the K-th smallest length.

------------------------------------------------------------------------

# Observation 2 --- Counting Intervals Containing X

During a binary-search round, suppose we have currently activated a
prefix of the intervals sorted by length.

We need to answer:

``` text
How many active intervals contain X?
```

This is a range-add / point-query problem.

For an interval:

``` text
[L, R]
```

use a difference-array idea:

``` text
+1 at L
-1 after R
```

Using a Fenwick tree:

``` cpp
BIT.add(L, +1);
BIT.add(R + 1, -1);
```

Then:

``` cpp
BIT.sum(X)
```

returns the number of active intervals containing `X`.

------------------------------------------------------------------------

## Example

For:

``` text
[3, 7]
```

we conceptually add:

``` text
position 3 : +1
position 8 : -1
```

The prefix sum becomes:

``` text
Position:  1 2 3 4 5 6 7 8 9
Count:     0 0 1 1 1 1 1 0 0
```

Therefore:

``` text
BIT.sum(5) = 1
```

which tells us that point `5` is covered by one active interval.

------------------------------------------------------------------------

# Observation 3 --- Coordinate Compression

Coordinates `L`, `R`, and `X` may be very large.

A Fenwick tree cannot be allocated directly over a huge coordinate
range.

So collect all relevant coordinates:

``` text
all L values
all R values
all query X values
```

Sort them and remove duplicates.

Then map each original coordinate to:

``` text
1, 2, 3, ..., M
```

This is **coordinate compression**.

The relative ordering is preserved, which is all we need.

------------------------------------------------------------------------

# Observation 4 --- Parallel Binary Search

We could binary-search separately for every query, but repeatedly
rebuilding the interval coverage structure would be expensive.

Instead, perform the binary searches for **all queries simultaneously**.

For every query maintain:

``` text
low[i]
high[i]
```

Its current midpoint is:

``` cpp
mid = low[i] + (high[i] - low[i]) / 2;
```

Group queries according to their current `mid`.

Then sweep through the intervals once in increasing length order.

As interval `i` becomes active:

``` cpp
BIT.add(interval[i].l, +1);
BIT.add(interval[i].r + 1, -1);
```

When we reach a query whose midpoint is `i`, calculate:

``` cpp
count = BIT.sum(queryPoint);
```

If:

``` text
count >= K
```

then the answer is at `mid` or earlier:

``` cpp
high = mid;
```

Otherwise:

``` cpp
low = mid + 1;
```

Repeat until:

``` text
low == high
```

for every query.

------------------------------------------------------------------------

# Complete C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

struct Interval
{
    int len;
    int l;
    int r;
};

struct Query
{
    int k;
    int x;
};

class Fenwick
{
private:
    vector<int> bit;
    int n;

public:
    Fenwick(int n) : n(n), bit(n + 2, 0)
    {
    }

    void add(int idx, int value)
    {
        while (idx <= n)
        {
            bit[idx] += value;
            idx += idx & -idx;
        }
    }

    int sum(int idx)
    {
        int result = 0;

        while (idx > 0)
        {
            result += bit[idx];
            idx -= idx & -idx;
        }

        return result;
    }

    void clear()
    {
        fill(bit.begin(), bit.end(), 0);
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<pair<int, int>> inputIntervals(n);
    vector<int> coordinates;

    for (int i = 0; i < n; ++i)
    {
        int l, r;
        cin >> l >> r;

        inputIntervals[i] = {l, r};

        coordinates.push_back(l);
        coordinates.push_back(r);
    }

    int q;
    cin >> q;

    vector<Query> queries(q);

    for (int i = 0; i < q; ++i)
    {
        cin >> queries[i].k >> queries[i].x;

        coordinates.push_back(queries[i].x);
    }

    // --------------------------------------------------
    // Coordinate Compression
    // --------------------------------------------------

    sort(coordinates.begin(), coordinates.end());

    coordinates.erase(
        unique(coordinates.begin(), coordinates.end()),
        coordinates.end()
    );

    auto getPosition = [&](int x)
    {
        return int(
            lower_bound(
                coordinates.begin(),
                coordinates.end(),
                x
            ) - coordinates.begin()
        ) + 1;
    };

    // --------------------------------------------------
    // Build compressed intervals
    // --------------------------------------------------

    vector<Interval> intervals;
    intervals.reserve(n);

    for (auto [l, r] : inputIntervals)
    {
        intervals.push_back(
        {
            r - l + 1,
            getPosition(l),
            getPosition(r)
        });
    }

    // Sort intervals by length.
    sort(
        intervals.begin(),
        intervals.end(),
        [](const Interval &a, const Interval &b)
        {
            return a.len < b.len;
        }
    );

    // Compressed position of every query point.
    vector<int> queryPosition(q);

    for (int i = 0; i < q; ++i)
    {
        queryPosition[i] = getPosition(queries[i].x);
    }

    // --------------------------------------------------
    // Parallel Binary Search
    // --------------------------------------------------

    // Search over interval indices [0, n].
    //
    // n represents:
    // fewer than K intervals contain X.

    vector<int> low(q, 0);
    vector<int> high(q, n);

    Fenwick bit(coordinates.size() + 2);

    bool changed = true;

    while (changed)
    {
        changed = false;

        vector<vector<int>> bucket(n);

        // Group queries according to current midpoint.
        for (int i = 0; i < q; ++i)
        {
            if (low[i] < high[i])
            {
                changed = true;

                int mid =
                    low[i] + (high[i] - low[i]) / 2;

                if (mid < n)
                {
                    bucket[mid].push_back(i);
                }
            }
        }

        if (!changed)
            break;

        bit.clear();

        // Activate intervals from smallest to largest.
        for (int i = 0; i < n; ++i)
        {
            bit.add(intervals[i].l, +1);
            bit.add(intervals[i].r + 1, -1);

            // Process all queries whose current
            // binary-search midpoint is i.
            for (int queryId : bucket[i])
            {
                int count =
                    bit.sum(queryPosition[queryId]);

                if (count >= queries[queryId].k)
                {
                    high[queryId] = i;
                }
                else
                {
                    low[queryId] = i + 1;
                }
            }
        }
    }

    // --------------------------------------------------
    // Output
    // --------------------------------------------------

    for (int i = 0; i < q; ++i)
    {
        if (low[i] >= n)
        {
            cout << -1 << '\n';
        }
        else
        {
            cout << intervals[low[i]].len << '\n';
        }
    }

    return 0;
}
```

------------------------------------------------------------------------

# Why the Solution Works

For every query `(K, X)`, define:

``` text
f(m) = number of intervals among indices [0 ... m]
       that contain X
```

Because increasing `m` only adds intervals:

``` text
f(m + 1) >= f(m)
```

Therefore:

``` text
f(m) >= K
```

is monotonic.

So binary search can locate the first `m` satisfying this condition.

Since the intervals are sorted by length, the interval at that first
valid index is exactly the **K-th smallest interval containing X**.

The Fenwick tree efficiently computes `f(m)` during each sweep.

Parallel binary search lets all queries share the same interval sweeps.

------------------------------------------------------------------------

# Time Complexity

Let:

``` text
N = number of intervals
Q = number of queries
M = number of unique compressed coordinates
```

where:

``` text
M <= 2N + Q
```

## Coordinate Compression

Sorting coordinates:

``` text
O((N + Q) log(N + Q))
```

Mapping coordinates with binary search:

``` text
O((N + Q) log(N + Q))
```

## Sorting Intervals

``` text
O(N log N)
```

## Parallel Binary Search

Binary search needs approximately:

``` text
O(log N)
```

rounds.

During each round:

-   `N` intervals are added to the Fenwick tree.
-   Up to `Q` query-point prefix sums are performed.

Each Fenwick operation costs:

``` text
O(log M)
```

Therefore:

``` text
O((N + Q) log M log N)
```

Since:

``` text
M = O(N + Q)
```

we can write the overall complexity as:

``` text
O((N + Q) log(N + Q) log N)
```

plus the initial sorting costs.

------------------------------------------------------------------------

# Space Complexity

We store:

``` text
Intervals              O(N)
Queries                O(Q)
Compressed coordinates O(N + Q)
Fenwick tree           O(N + Q)
Binary-search arrays   O(Q)
Buckets                O(N + Q)
```

Therefore the overall auxiliary/storage complexity is:

``` text
O(N + Q)
```

------------------------------------------------------------------------

# Interview Thought Process

A useful way to derive the solution is:

``` text
Need K-th smallest interval containing X
                 |
                 v
Sort intervals by length
                 |
                 v
Ask whether first m intervals contain
at least K intervals covering X
                 |
                 v
Condition is monotonic
                 |
                 v
Binary search on m
                 |
                 v
Need fast count of intervals covering X
                 |
                 v
Range add + point query
                 |
                 v
Fenwick Tree
                 |
                 v
Many queries binary-search simultaneously
                 |
                 v
Parallel Binary Search
```

The central insight is:

> After sorting intervals by length, the K-th smallest interval
> containing `X` is the earliest prefix containing at least `K`
> intervals that cover `X`.

That converts the K-th-order-statistic problem into a monotonic decision
problem that can be solved with **parallel binary search + Fenwick
tree**.
