# Min-Max Difference Operations --- HackerEarth

## Problem Summary

You are given an array `A` of size `N`.

In one operation:

1.  Remove the smallest element `mn`.
2.  Remove the largest element `mx`.
3.  Insert their difference:

``` text
mx - mn
```

After every operation, the size of the array decreases by `1`.

There are `Q` queries. Each query gives an integer `K`, and we must
print the sum of all elements after exactly `K` operations.

Constraints:

``` text
2 <= N <= 10^5
1 <= Q <= 10^5
0 <= A[i] <= 10^9
0 <= K < N
```

------------------------------------------------------------------------

## Key Observation 1 --- How Does the Sum Change?

Suppose the current sum is:

``` text
S
```

and:

``` text
mn = minimum element
mx = maximum element
```

The operation removes:

``` text
mn + mx
```

and inserts:

``` text
mx - mn
```

Therefore:

``` text
newSum
= S - mn - mx + (mx - mn)
```

Simplifying:

``` text
newSum = S - 2 * mn
```

So the maximum cancels out completely from the sum formula.

The key formula is:

``` text
S(new) = S(old) - 2 * minimum
```

We still need the maximum to determine the new value `mx - mn` that must
be inserted.

------------------------------------------------------------------------

## Key Observation 2 --- Precompute All Answers

The sequence of operations is deterministic.

Starting from the same array:

``` text
after 0 operations -> always the same sum
after 1 operation  -> always the same sum
after 2 operations -> always the same sum
...
```

Therefore we should **not simulate the operations independently for
every query**.

Instead, precompute:

``` text
ans[k] = sum after exactly k operations
```

for every:

``` text
0 <= k < N
```

Then each query is answered immediately:

``` cpp
cout << ans[K];
```

This reduces each query to `O(1)`.

------------------------------------------------------------------------

## Data Structure

For every operation we need to:

-   get the minimum,
-   get the maximum,
-   remove one occurrence of each,
-   insert `maximum - minimum`.

A C++ `multiset` supports all these operations in `O(log N)`.

It also handles duplicate values naturally.

------------------------------------------------------------------------

## Important Duplicate Detail

We must remove the minimum first:

``` cpp
auto itMin = s.begin();
long long mn = *itMin;
s.erase(itMin);
```

Then obtain the maximum from the remaining multiset:

``` cpp
auto itMax = prev(s.end());
long long mx = *itMax;
s.erase(itMax);
```

This correctly handles cases where the minimum and maximum values are
equal or where duplicates exist.

------------------------------------------------------------------------

## C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    multiset<long long> s;

    long long sum = 0;

    for (int i = 0; i < N; ++i)
    {
        long long x;
        cin >> x;

        s.insert(x);
        sum += x;
    }

    // ans[k] = sum after exactly k operations
    vector<long long> ans(N);

    ans[0] = sum;

    // Precompute the result after every possible
    // number of operations.
    for (int k = 1; k < N; ++k)
    {
        // Current minimum.
        auto itMin = s.begin();
        long long mn = *itMin;

        s.erase(itMin);

        // Current maximum after removing one minimum.
        auto itMax = prev(s.end());
        long long mx = *itMax;

        s.erase(itMax);

        // Insert their difference.
        s.insert(mx - mn);

        // newSum = oldSum - 2 * minimum
        sum -= 2LL * mn;

        ans[k] = sum;
    }

    // Every query is now O(1).
    while (Q--)
    {
        int K;
        cin >> K;

        cout << ans[K] << '\n';
    }

    return 0;
}
```

------------------------------------------------------------------------

## Sample Walkthrough

Input:

``` text
5 2
3 2 1 5 4
1
2
```

Initially, after sorting conceptually:

``` text
1 2 3 4 5
```

Initial sum:

``` text
15
```

Therefore:

``` text
ans[0] = 15
```

### Operation 1

``` text
minimum = 1
maximum = 5
```

Remove:

``` text
1 and 5
```

Insert:

``` text
5 - 1 = 4
```

The array becomes:

``` text
2 3 4 4
```

Using the sum formula:

``` text
newSum
= 15 - 2 * 1
= 13
```

Therefore:

``` text
ans[1] = 13
```

### Operation 2

Current array:

``` text
2 3 4 4
```

So:

``` text
minimum = 2
maximum = 4
```

Insert:

``` text
4 - 2 = 2
```

The new array is:

``` text
2 3 4
```

and:

``` text
newSum
= 13 - 2 * 2
= 9
```

Therefore:

``` text
ans[2] = 9
```

Queries:

``` text
K = 1 -> 13
K = 2 -> 9
```

Output:

``` text
13
9
```

------------------------------------------------------------------------

## Why `long long` Is Required

Since:

``` text
N <= 10^5
A[i] <= 10^9
```

the initial sum can be as large as:

``` text
10^5 * 10^9 = 10^14
```

which does not fit in a 32-bit `int`.

Therefore array values involved in arithmetic and all sums should use:

``` cpp
long long
```

------------------------------------------------------------------------

## Time Complexity

Building the multiset requires:

``` text
O(N log N)
```

There are `N-1` possible operations.

For every operation we perform:

-   minimum access/removal,
-   maximum access/removal,
-   one insertion.

Each costs at most:

``` text
O(log N)
```

So precomputation costs:

``` text
O(N log N)
```

Each query is:

``` text
O(1)
```

For `Q` queries:

``` text
O(Q)
```

Overall:

``` text
Time = O(N log N + Q)
```

------------------------------------------------------------------------

## Space Complexity

The multiset stores at most `N` elements:

``` text
O(N)
```

The answer array stores `N` sums:

``` text
O(N)
```

Therefore:

``` text
Space = O(N)
```

------------------------------------------------------------------------

## Problem-Solving Thought Process

``` text
Operation:
remove min and max
insert max - min

        |
        v

Need sum after operation

        |
        v

newSum =
oldSum - min - max + (max - min)

        |
        v

max cancels

        |
        v

newSum = oldSum - 2*min

        |
        v

Still need min/max to construct next array

        |
        v

Use multiset

        |
        v

Q can be 10^5

        |
        v

Do not repeat simulation for every query

        |
        v

Precompute ans[0 ... N-1]

        |
        v

Each query becomes O(1)
```

------------------------------------------------------------------------

## Key Takeaways

The two main ideas are:

> **The sum after one operation changes by exactly `-2 * minimum`.**

and:

> **Because the process is deterministic, simulate all `N-1` operations
> once and precompute the answer for every possible `K`.**

Final complexity:

``` text
Time  : O(N log N + Q)
Space : O(N)
```
