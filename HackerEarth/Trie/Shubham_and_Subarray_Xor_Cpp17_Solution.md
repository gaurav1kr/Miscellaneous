# Shubham and Subarray Xor --- C++17 Solution

## Problem Statement

You are given an array of `n` integers:

``` text
a1, a2, ..., an
```

Find the maximum value of XOR of the sums of two **disjoint subarrays**.

Choose:

``` text
1 <= l1 <= r1 < l2 <= r2 <= n
```

and maximize:

``` text
sum(l1, r1) XOR sum(l2, r2)
```

where:

``` text
sum(l, r) = a[l] + a[l+1] + ... + a[r]
```

### Input

-   The first line contains `n`, the number of array elements.
-   The second line contains `n` integers `a1, a2, ..., an`.

### Output

Print the maximum possible XOR value.

### Constraints

``` text
1 <= n <= 500
1 <= ai <= 100
```

------------------------------------------------------------------------

## Key Observation

The two selected subarrays must satisfy:

``` text
r1 < l2
```

Instead of trying all four endpoints directly, process the **starting
position of the second subarray**.

Suppose:

``` text
rightL
```

is the starting position of the second subarray.

Then every valid first subarray must end before `rightL`.

Therefore, before processing `rightL`, we maintain a Binary Trie
containing the sums of **all subarrays whose right endpoint is less than
`rightL`**.

Then enumerate every second subarray starting at `rightL`, calculate its
sum, and query the trie for the first-subarray sum that maximizes XOR
with it.

This automatically guarantees that the two subarrays are disjoint.

------------------------------------------------------------------------

# Prefix Sums

Use prefix sums to calculate any subarray sum in `O(1)`.

Define:

``` text
prefix[0] = 0
prefix[i] = a1 + a2 + ... + ai
```

Then:

``` text
sum(l, r) = prefix[r] - prefix[l - 1]
```

This allows us to enumerate subarrays efficiently.

------------------------------------------------------------------------

# Binary Trie

We need to repeatedly solve:

> Given a second-subarray sum `x`, find a previously inserted
> first-subarray sum `y` maximizing `x XOR y`.

A binary trie is ideal for this.

Since:

``` text
n <= 500
ai <= 100
```

the maximum possible subarray sum is:

``` text
500 * 100 = 50000
```

and:

``` text
50000 < 2^16
```

Therefore bits:

``` text
15 ... 0
```

are sufficient.

------------------------------------------------------------------------

## Maximum XOR Query

At each bit, suppose the current bit of `x` is:

``` text
b
```

To maximize XOR, we prefer the opposite bit:

``` text
b XOR 1
```

because:

``` text
b XOR (b XOR 1) = 1
```

A `1` at a more significant bit always gives a larger XOR value than any
combination of lower bits.

Therefore:

1.  Try the opposite-bit child.
2.  If it exists, take it and set that bit in the result.
3.  Otherwise, follow the same-bit child.

This greedily produces the maximum XOR.

------------------------------------------------------------------------

# Processing the Array

Let:

``` text
rightL
```

be the start of the second subarray.

We process:

``` text
rightL = 2 ... n
```

Before considering second subarrays starting at `rightL`, let:

``` text
leftR = rightL - 1
```

Insert every subarray ending exactly at `leftR`:

``` text
[1, leftR]
[2, leftR]
...
[leftR, leftR]
```

into the trie.

Because previous iterations already inserted subarrays ending before
`leftR`, after this insertion the trie contains **all subarray sums
whose ending position is strictly less than `rightL`**.

Now enumerate:

``` text
[rightL, rightL]
[rightL, rightL+1]
...
[rightL, n]
```

For each second-subarray sum, query the trie for its maximum XOR
partner.

------------------------------------------------------------------------

# Example

Consider:

``` text
n = 4
a = [1, 2, 1, 3]
```

One optimal choice is:

``` text
first subarray  = [1, 2]
sum = 1 + 2 = 3

second subarray = [3, 4]
sum = 1 + 3 = 4
```

Therefore:

``` text
3 XOR 4 = 7
```

So the answer is:

``` text
7
```

------------------------------------------------------------------------

# C++17 Implementation

``` cpp
#include <bits/stdc++.h>
using namespace std;

class BinaryTrie {
private:
    struct Node {
        int child[2];

        Node() {
            child[0] = child[1] = -1;
        }
    };

    vector<Node> tr;

    static constexpr int MAX_BIT = 15;

public:
    BinaryTrie() {
        tr.reserve(100000);
        tr.emplace_back();
    }

    void insert(int x) {
        int node = 0;

        for (int bit = MAX_BIT; bit >= 0; --bit) {
            int b = (x >> bit) & 1;

            if (tr[node].child[b] == -1) {
                tr[node].child[b] = (int)tr.size();
                tr.emplace_back();
            }

            node = tr[node].child[b];
        }
    }

    int maxXor(int x) const {
        int node = 0;
        int result = 0;

        for (int bit = MAX_BIT; bit >= 0; --bit) {
            int b = (x >> bit) & 1;
            int opposite = b ^ 1;

            if (tr[node].child[opposite] != -1) {
                result |= (1 << bit);
                node = tr[node].child[opposite];
            } else {
                node = tr[node].child[b];
            }
        }

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> a(n + 1);
    vector<int> pref(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        pref[i] = pref[i - 1] + a[i];
    }

    BinaryTrie trie;

    int answer = 0;

    /*
        rightL = starting position of the second subarray.

        Before processing rightL, insert all first-subarray
        sums ending at rightL - 1.

        The trie therefore contains all subarray sums
        whose right endpoint is < rightL.
    */
    for (int rightL = 2; rightL <= n; ++rightL) {

        int leftR = rightL - 1;

        // Add all subarrays ending exactly at leftR.
        for (int leftL = 1; leftL <= leftR; ++leftL) {

            int leftSum =
                pref[leftR] - pref[leftL - 1];

            trie.insert(leftSum);
        }

        // Try every second subarray starting at rightL.
        for (int rightR = rightL; rightR <= n; ++rightR) {

            int rightSum =
                pref[rightR] - pref[rightL - 1];

            answer = max(
                answer,
                trie.maxXor(rightSum)
            );
        }
    }

    cout << answer << '\n';

    return 0;
}
```

------------------------------------------------------------------------

# Correctness

We prove that the algorithm considers every valid pair of disjoint
subarrays.

## Invariant

Before processing a second-subarray starting position `rightL`, the trie
contains the sums of every subarray:

``` text
[l1, r1]
```

such that:

``` text
r1 < rightL
```

### Why?

At iteration `rightL`, we insert all subarrays ending at:

``` text
rightL - 1
```

All subarrays ending before that were inserted during earlier
iterations.

Therefore, after insertion, the trie contains exactly the candidate
first-subarray sums that can appear before a second subarray starting at
`rightL`.

------------------------------------------------------------------------

## Every Valid Pair Is Considered

Take any valid pair:

``` text
[l1, r1]
[l2, r2]
```

with:

``` text
r1 < l2
```

When:

``` text
rightL = l2
```

is processed, the first-subarray sum:

``` text
sum(l1, r1)
```

is already present in the trie because:

``` text
r1 < l2
```

The inner loop eventually reaches:

``` text
rightR = r2
```

and calculates:

``` text
sum(l2, r2)
```

The trie query considers every valid first-subarray sum and returns the
one giving the maximum XOR with this second-subarray sum.

Thus the XOR value of every valid pair is considered, and the global
maximum is returned.

------------------------------------------------------------------------

# Time Complexity

Let the trie depth be:

``` text
B = 16
```

because all subarray sums are at most `50000`.

## Prefix Sum Construction

``` text
O(n)
```

## First-Subarray Insertions

Each subarray sum is inserted once.

The number of subarrays is:

``` text
O(n^2)
```

and every trie insertion takes:

``` text
O(B)
```

Therefore:

``` text
O(n^2 * B)
```

## Second-Subarray Queries

There are also:

``` text
O(n^2)
```

possible second subarrays.

Each maximum-XOR query takes:

``` text
O(B)
```

Therefore:

``` text
O(n^2 * B)
```

## Overall

``` text
O(n^2 * log(MAX_SUM))
```

Since:

``` text
MAX_SUM <= 50000
```

the trie has only 16 levels.

Thus, for this problem:

``` text
O(16 * n^2)
```

which is effectively:

``` text
O(n^2)
```

for the fixed constraints.

With:

``` text
n <= 500
```

this is easily fast enough.

------------------------------------------------------------------------

# Space Complexity

The prefix arrays require:

``` text
O(n)
```

space.

The trie stores the binary representations of inserted subarray sums.

There are:

``` text
O(n^2)
```

subarray sums, and each insertion can theoretically create up to 16
nodes.

Therefore the general upper bound is:

``` text
O(n^2 * log(MAX_SUM))
```

However, trie prefixes are heavily shared, and the value domain is small
(`0 ... 50000`), so the actual memory usage is much smaller.

For the given constraints, memory usage is comfortably within the limit.

------------------------------------------------------------------------

# Trade-offs

## Advantages

-   Simple and efficient.
-   Directly enforces the non-overlapping condition.
-   Uses prefix sums for `O(1)` subarray-sum calculation.
-   Binary trie gives fast maximum-XOR queries.
-   Avoids trying all four endpoints.
-   No complicated preprocessing or advanced range-query structure is
    required.
-   Performs well for `n <= 500`.

## Disadvantages

-   Still enumerates `O(n^2)` candidate subarrays.
-   Binary trie requires additional memory compared with a brute-force
    integer array.
-   The fixed `MAX_BIT = 15` depends on the problem constraints.
-   For significantly larger `n`, the `O(n^2)` enumeration would become
    too expensive.

------------------------------------------------------------------------

# Why Not Brute Force?

A direct brute-force solution could choose:

``` text
l1, r1, l2, r2
```

independently.

That leads to approximately:

``` text
O(n^4)
```

possibilities.

Even with prefix sums making each subarray sum `O(1)`, the number of
endpoint combinations remains too large.

The trie approach reduces this to:

``` text
O(n^2 * log(MAX_SUM))
```

by storing all valid first-subarray sums and efficiently finding the
best partner for every second-subarray sum.

------------------------------------------------------------------------

# Summary

The core idea is to process the **starting position of the second
subarray**.

For every `rightL`:

``` text
1. Insert all subarray sums ending at rightL - 1.
2. The trie now contains every valid first-subarray sum.
3. Enumerate every second subarray starting at rightL.
4. Query the trie for the maximum XOR partner.
```

Using prefix sums and a binary trie gives:

``` text
Time:
O(n^2 * log(MAX_SUM))

Space:
O(n^2 * log(MAX_SUM)) worst case
```

With:

``` text
n <= 500
MAX_SUM <= 50000
```

the trie depth is only 16, making this solution fast and practical.
