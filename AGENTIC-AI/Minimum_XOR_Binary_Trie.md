# Minimum XOR

## Problem

You are given `q` queries of two types:

1.  `1 X` --- Append the value `X` to the current array.

2.  `2 X K` --- For every element `A[i]` in the current array,
    calculate:

    `A[i] XOR X`

    Sort all these XOR values and print the **K-th smallest** value.

### Constraints

-   `1 <= q <= 100000`
-   `1 <= X <= 10^18`
-   For a type-2 query, `K <= current array size`

------------------------------------------------------------------------

## Approach

A direct solution would calculate `A[i] XOR X` for every element and
sort the results for each type-2 query. This would be too slow for up to
`10^5` queries.

We use a **Binary Trie (Bitwise Trie)**.

Since `X <= 10^18 < 2^60`, every number can be represented using 60
bits, from bit `59` down to bit `0`.

Each trie node contains:

-   `child[0]` --- next node for bit `0`
-   `child[1]` --- next node for bit `1`
-   `cnt` --- number of inserted values passing through this node

### Insertion

To insert a number `x`:

1.  Start at the root.
2.  Examine bits from `59` down to `0`.
3.  Follow/create the child corresponding to the current bit.
4.  Increment `cnt` along the path.

### Finding the K-th Minimum XOR

For query `2 X K`, we want the K-th smallest value among:

`X XOR A[0], X XOR A[1], ...`

Process bits from most significant to least significant.

Suppose the current bit of `X` is `b`.

If we choose a stored number having the same bit `b`, then:

`b XOR b = 0`

An XOR value with `0` at the current most-significant undecided bit is
smaller than one having `1`. Therefore, we first consider the trie
branch `child[b]`.

Let `sameCount` be the number of stored values in that branch.

-   If `K <= sameCount`, the K-th smallest XOR lies in this branch. Move
    to `child[b]`.

-   Otherwise, all `sameCount` values are smaller than the required
    answer. Subtract them:

    `K -= sameCount`

    Then move to `child[b ^ 1]` and set the corresponding bit in the
    answer to `1`.

Repeating this for all 60 bits constructs the K-th minimum XOR value
directly, without creating or sorting the XOR array.

------------------------------------------------------------------------

## C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;

struct Node {
    int child[2];
    int cnt;

    Node() {
        child[0] = child[1] = -1;
        cnt = 0;
    }
};

class BinaryTrie {
private:
    vector<Node> trie;

public:
    BinaryTrie() {
        trie.reserve(6000005);   // ~1e5 * 60 nodes
        trie.emplace_back();     // root
    }

    void insert(ull x) {
        int node = 0;
        trie[node].cnt++;

        for (int bit = 59; bit >= 0; --bit) {
            int b = (x >> bit) & 1ULL;

            if (trie[node].child[b] == -1) {
                trie[node].child[b] = (int)trie.size();
                trie.emplace_back();
            }

            node = trie[node].child[b];
            trie[node].cnt++;
        }
    }

    ull kthMinXor(ull x, int k) {
        int node = 0;
        ull answer = 0;

        for (int bit = 59; bit >= 0; --bit) {
            int b = (x >> bit) & 1ULL;

            // Same bit makes the XOR bit 0.
            int same = trie[node].child[b];

            int sameCount = 0;
            if (same != -1) {
                sameCount = trie[same].cnt;
            }

            if (k <= sameCount) {
                // K-th smallest is among values
                // having XOR bit 0.
                node = same;
            } else {
                // Skip all values having XOR bit 0.
                k -= sameCount;

                // XOR bit must now be 1.
                answer |= (1ULL << bit);

                node = trie[node].child[b ^ 1];
            }
        }

        return answer;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;

    BinaryTrie trie;

    while (q--) {
        int type;
        cin >> type;

        if (type == 1) {
            ull x;
            cin >> x;

            trie.insert(x);
        } else {
            ull x;
            int k;
            cin >> x >> k;

            cout << trie.kthMinXor(x, k) << '\n';
        }
    }

    return 0;
}
```

------------------------------------------------------------------------

## Why This Works

At every bit position, XOR values whose current bit is `0` are smaller
than XOR values whose current bit is `1`, assuming all more-significant
bits are already equal.

The trie stores the number of values available under every prefix. This
allows us to determine how many candidate XOR values would have `0` at
the current bit.

We can therefore skip entire groups of smaller XOR values and locate the
K-th value in the same way that an order-statistics structure locates
the K-th element.

------------------------------------------------------------------------

## Time Complexity

There are 60 relevant bits.

### Insert

Each insertion traverses exactly 60 trie levels:

`O(60) = O(1)`

### K-th Minimum XOR Query

Each query also traverses exactly 60 levels:

`O(60) = O(1)`

### Overall

For `q` queries:

`O(60 * q) = O(q)`

The factor 60 is fixed by the maximum value of `X`.

------------------------------------------------------------------------

## Space Complexity

Each inserted number can create at most 60 new trie nodes.

For `N` inserted values:

`O(60 * N) = O(N)`

In the worst case, for `N = 100000`, the trie can contain roughly 6
million nodes.

------------------------------------------------------------------------

## Key Takeaway

The important observation is that to minimize XOR at any bit, we prefer
a stored bit equal to the corresponding bit of `X`.

By storing subtree counts in a binary trie, this greedy XOR property can
be extended from finding the minimum XOR to finding the **K-th minimum
XOR** efficiently.
