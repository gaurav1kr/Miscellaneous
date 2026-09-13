# Make X the Mode — HackerEarth

## Problem Summary

You are given an array `A` of `N` numbers and an integer `X`.

In one operation, you can choose any index `i` and change:

```text
A[i] -> X
```

Find the minimum number of operations required to make `X` the **mode** of the array.

A number is the mode only when its frequency is **strictly greater** than the frequency of every other number.

---

## Key Observation

Let the current frequency of `X` be:

```text
fx
```

Suppose we perform `k` operations.

Each operation converts some non-`X` element into `X`, so the new frequency of `X` becomes:

```text
fx + k
```

For `X` to be the mode, every other value must have frequency strictly smaller than this.

Therefore every other frequency must satisfy:

```text
frequency < fx + k
```

or equivalently:

```text
frequency <= fx + k - 1
```

---

## Mandatory Conversions

Suppose another number currently occurs `c` times.

After `k` operations, the maximum frequency it is allowed to have is:

```text
limit = fx + k - 1
```

If:

```text
c <= limit
```

we do not necessarily need to change any occurrence of this number.

But if:

```text
c > limit
```

at least:

```text
c - limit
```

occurrences of this number must be converted into `X`.

Therefore, for a candidate number of operations `k`:

```text
required =
Σ max(0, c - (fx + k - 1))
```

where `c` ranges over frequencies of all values other than `X`.

If:

```text
required <= k
```

then `k` operations are sufficient.

---

## Why Binary Search Works

If `k` operations are sufficient, then using more operations will also be sufficient.

So feasibility has the form:

```text
false false false ... true true true
```

This monotonic property allows us to binary-search the minimum valid `k`.

Search range:

```text
0 <= k <= N - fx
```

because in the worst case we can convert every non-`X` element into `X`.

---

## Efficient Feasibility Check

We could scan every distinct frequency for every binary-search step, but we can do better.

Store all frequencies except `freq[X]` in:

```cpp
vector<int> cnt;
```

Sort them and build prefix sums.

For candidate `k`:

```text
limit = fx + k - 1
```

Use `upper_bound` to find the first frequency greater than `limit`.

Suppose all frequencies after that position have:

```text
count = numberOfLarge
sum   = sumOfLarge
```

Then the mandatory number of conversions is:

```text
required =
sumOfLarge - numberOfLarge * limit
```

This computes the feasibility check without scanning every frequency.

---

## C++17 Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--)
    {
        int N;
        long long X;

        cin >> N >> X;

        unordered_map<long long, int> freq;
        freq.reserve(2 * N);

        for (int i = 0; i < N; ++i)
        {
            long long v;
            cin >> v;

            ++freq[v];
        }

        int fx = freq[X];

        vector<int> cnt;

        for (auto &[value, f] : freq)
        {
            if (value != X)
                cnt.push_back(f);
        }

        sort(cnt.begin(), cnt.end());

        int m = cnt.size();

        vector<long long> prefix(m + 1, 0);

        for (int i = 0; i < m; ++i)
        {
            prefix[i + 1] =
                prefix[i] + cnt[i];
        }

        auto possible = [&](int k) -> bool
        {
            long long target =
                (long long)fx + k;

            long long limit =
                target - 1;

            int pos =
                upper_bound(
                    cnt.begin(),
                    cnt.end(),
                    limit
                ) - cnt.begin();

            long long numberOfLarge =
                m - pos;

            long long sumOfLarge =
                prefix[m] - prefix[pos];

            long long required =
                sumOfLarge -
                numberOfLarge * limit;

            return required <= k;
        };

        int low = 0;
        int high = N - fx;

        while (low < high)
        {
            int mid =
                low + (high - low) / 2;

            if (possible(mid))
            {
                high = mid;
            }
            else
            {
                low = mid + 1;
            }
        }

        cout << low << '\n';
    }

    return 0;
}
```

---

## Example 1

```text
N = 3
X = 1

A = [1, 1, 3]
```

Frequencies:

```text
1 -> 2
3 -> 1
```

`1` already occurs more frequently than every other value.

Therefore:

```text
answer = 0
```

---

## Example 2

```text
N = 4
X = 1

A = [1, 1, 3, 3]
```

Initially:

```text
1 -> 2
3 -> 2
```

There is a tie, so `1` is **not** the mode.

Perform one operation:

```text
3 -> 1
```

The array can become:

```text
[1, 1, 1, 3]
```

Now:

```text
1 -> 3
3 -> 1
```

Therefore:

```text
answer = 1
```

---

## Time Complexity

Let:

```text
D = number of distinct values
```

Building the frequency table:

```text
Expected O(N)
```

Sorting the frequencies:

```text
O(D log D)
```

Building prefix sums:

```text
O(D)
```

Binary search performs:

```text
O(log N)
```

iterations.

Each feasibility check uses `upper_bound`:

```text
O(log D)
```

Therefore the overall complexity is:

```text
O(N + D log D + log N * log D)
```

Since:

```text
D <= N
```

this is easily fast enough for typical constraints.

---

## Space Complexity

The frequency map stores at most `D` values:

```text
O(D)
```

The sorted frequency vector and prefix-sum array also use:

```text
O(D)
```

Therefore:

```text
Space Complexity = O(D)
```

and in the worst case:

```text
O(N)
```

---

## Interview / Problem-Solving Thought Process

```text
Need X to be unique mode
        |
        v
Suppose we perform k operations
        |
        v
freq(X) becomes fx + k
        |
        v
Every other frequency must be <= fx + k - 1
        |
        v
Large frequency groups must lose elements
        |
        v
required = Σ max(0, c - limit)
        |
        v
k is feasible if required <= k
        |
        v
Feasibility is monotonic
        |
        v
Binary search minimum k
        |
        v
Sort frequencies + prefix sums
for fast feasibility checks
```

### Core Idea

> For a candidate `k`, calculate how many non-`X` elements are **forced** to change so that every competing frequency becomes smaller than `freq(X) + k`. If that number is at most `k`, then `k` operations are sufficient.
