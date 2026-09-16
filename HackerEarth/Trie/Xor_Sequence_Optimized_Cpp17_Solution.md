# Xor Sequence --- Optimized C++17 Solution

## Problem Statement

You are given a sequence:

``` text
a1, a2, ..., an
```

and need to answer `m` online queries.

For each query, two integers `x` and `y` are given. The actual range
`[l, r]` depends on the answer to the previous query:

``` text
l = min(((x + ans * t) mod n) + 1,
        ((y + ans * t) mod n) + 1)

r = max(((x + ans * t) mod n) + 1,
        ((y + ans * t) mod n) + 1)
```

Here:

-   `ans` is the answer to the previous query.
-   Initially, `ans = 0`.
-   `t` is either `0` or `1`.

For the resulting interval `[l, r]`, choose a pair `(i, j)` satisfying:

``` text
l <= i <= j <= r
```

and maximize:

``` text
ai XOR ai+1 XOR ... XOR aj
```

For every query, output this maximum subarray XOR.

### Constraints

``` text
1 <= n, m <= 20000
0 <= t <= 1
0 <= x, y, ai <= 10^9
```

The queries must be answered online because the next range may depend on
the previous answer.

------------------------------------------------------------------------

## Key Observation --- Prefix XOR

Define the prefix XOR array:

``` text
P[0] = 0

P[i] = a1 XOR a2 XOR ... XOR ai
```

Then the XOR of any subarray `[i, j]` is:

``` text
ai XOR ai+1 XOR ... XOR aj
= P[j] XOR P[i-1]
```

Therefore, for a query `[l, r]`, we need to maximize:

``` text
P[j] XOR P[i-1]
```

where:

``` text
l <= i <= j <= r
```

This is exactly the maximum XOR of any two prefix-XOR values in:

``` text
P[l-1 ... r]
```

So the original problem becomes:

> For each online query, find the maximum XOR pair in a range of the
> prefix-XOR array.

------------------------------------------------------------------------

## Why Standard Offline Techniques Do Not Fit

A common approach for range queries is Mo's algorithm.

However, here the actual query range depends on:

``` text
ans
```

which is the result of the previous query.

Therefore, we cannot know all actual query ranges in advance when
`t = 1`.

The queries must be processed in input order.

We need an online data structure.

------------------------------------------------------------------------

# Approach

The solution combines:

1.  **Prefix XOR**
2.  **Square Root Decomposition**
3.  **Persistent Binary Trie**

The prefix XOR transformation converts maximum subarray XOR into maximum
XOR pair.

Square-root decomposition handles most of a query using precomputed
answers.

A persistent binary trie efficiently handles the small leftover part of
each query.

------------------------------------------------------------------------

# 1. Prefix XOR Transformation

For the original array:

``` text
a[1 ... n]
```

construct:

``` text
pref[0 ... n]
```

where:

``` cpp
pref[0] = 0;

pref[i] = pref[i - 1] ^ a[i];
```

For a query:

``` text
[l, r]
```

we need the maximum XOR pair among:

``` text
pref[l - 1 ... r]
```

Notice that the prefix array contains:

``` text
N = n + 1
```

elements.

------------------------------------------------------------------------

# 2. Persistent Binary Trie

A binary trie allows us to find:

``` text
maximum (x XOR y)
```

for a given `x` among a collection of numbers.

Since:

``` text
ai <= 10^9
```

31 bits (`30 ... 0`) are sufficient.

## Persistent Version

We create trie roots such that:

``` text
root[k]
```

contains:

``` text
pref[0], pref[1], ..., pref[k-1]
```

Therefore, the values:

``` text
pref[L ... R]
```

are represented by the difference between:

``` text
root[L]
root[R + 1]
```

Every trie node stores:

``` cpp
int child[2];
int cnt;
```

When querying a range, the number of available values in a child is:

``` text
count(rightRoot child)
-
count(leftRoot child)
```

This lets us determine whether that bit branch contains any value from
the requested range.

------------------------------------------------------------------------

# Maximum XOR Trie Query

Suppose we want to maximize:

``` text
x XOR y
```

At each bit, if the bit of `x` is:

``` text
b
```

we prefer:

``` text
b XOR 1
```

in `y`.

Why?

Because:

``` text
b XOR (b XOR 1) = 1
```

and setting a higher bit to `1` always produces a larger result than any
combination of lower bits.

If the preferred branch contains a value from the requested range, take
it.

Otherwise, use the same-bit branch.

------------------------------------------------------------------------

# 3. Square Root Decomposition

Let:

``` text
BLOCK ≈ sqrt(N)
```

For this implementation:

``` cpp
BLOCK = 145;
```

which is suitable for:

``` text
N <= 20001
```

There are approximately:

``` text
N / BLOCK
```

blocks.

For each block starting at position:

``` text
start = block * BLOCK
```

precompute:

``` text
best[block][r]
```

where:

``` text
best[block][r]
```

is the maximum XOR pair among:

``` text
pref[start ... r]
```

------------------------------------------------------------------------

# Precomputing `best`

For every block start:

1.  Create an empty binary trie.
2.  Insert `pref[start]`.
3.  Extend the right endpoint from `start + 1` to `N - 1`.
4.  For each new `pref[r]`, find its maximum XOR against all previously
    inserted values.
5.  Update the running maximum.
6.  Store it in:

``` text
best[block][r]
```

Thus:

``` text
best[b][R]
```

instantly answers a range whose left endpoint is exactly the beginning
of block `b`.

------------------------------------------------------------------------

# Processing a Query

Suppose the transformed prefix range is:

``` text
[L, R]
```

where:

``` text
L = l - 1
R = r
```

Find the first block boundary greater than or equal to `L`:

``` cpp
boundary =
    ((L + BLOCK - 1) / BLOCK) * BLOCK;
```

The range becomes:

``` text
[L ........ boundary-1] [boundary ........ R]
       left fringe          aligned suffix
```

The left fringe contains fewer than `BLOCK` elements.

------------------------------------------------------------------------

## Case 1 --- Both Values Are in the Aligned Suffix

The maximum XOR pair entirely inside:

``` text
[boundary, R]
```

has already been precomputed:

``` cpp
answer = best[boundary / BLOCK][R];
```

------------------------------------------------------------------------

## Case 2 --- At Least One Value Is in the Left Fringe

For every:

``` text
i in [L, boundary-1]
```

find the maximum:

``` text
pref[i] XOR pref[j]
```

where:

``` text
i < j <= R
```

using the persistent trie.

The trie query searches:

``` text
pref[i+1 ... R]
```

This covers:

-   one endpoint in the fringe and one in the suffix;
-   both endpoints inside the fringe.

Therefore, all possible pairs are considered.

------------------------------------------------------------------------

# C++17 Implementation

``` cpp
#include <bits/stdc++.h>
using namespace std;

static const int MAX_BIT = 30;

struct Node {
    int child[2];
    int cnt;

    Node() {
        child[0] = child[1] = 0;
        cnt = 0;
    }
};

class PersistentTrie {
private:
    vector<Node> tr;

public:
    PersistentTrie(int maxNodes = 1) {
        tr.reserve(maxNodes);
        tr.push_back(Node()); // null node = 0
    }

    int insert(int previousRoot, int x) {
        int newRoot = (int)tr.size();
        tr.push_back(tr[previousRoot]);
        tr[newRoot].cnt++;

        int curNew = newRoot;
        int curOld = previousRoot;

        for (int bit = MAX_BIT; bit >= 0; --bit) {
            int b = (x >> bit) & 1;

            int oldChild = tr[curOld].child[b];

            int newChild = (int)tr.size();
            tr.push_back(tr[oldChild]);
            tr[newChild].cnt++;

            tr[curNew].child[b] = newChild;

            curNew = newChild;
            curOld = oldChild;
        }

        return newRoot;
    }

    // Maximum x XOR y where y belongs to the represented range
    int maxXor(
        int rootBeforeL,
        int rootThroughR,
        int x
    ) const {
        int leftRoot = rootBeforeL;
        int rightRoot = rootThroughR;

        int answer = 0;

        for (int bit = MAX_BIT; bit >= 0; --bit) {
            int b = (x >> bit) & 1;
            int wanted = b ^ 1;

            int rightChild = tr[rightRoot].child[wanted];
            int leftChild = tr[leftRoot].child[wanted];

            int available =
                tr[rightChild].cnt - tr[leftChild].cnt;

            if (available > 0) {
                answer |= (1 << bit);

                rightRoot = rightChild;
                leftRoot = leftChild;
            }
            else {
                rightRoot = tr[rightRoot].child[b];
                leftRoot = tr[leftRoot].child[b];
            }
        }

        return answer;
    }
};


// Temporary trie used while preprocessing block answers
class BinaryTrie {
private:
    struct TNode {
        int child[2];

        TNode() {
            child[0] = child[1] = -1;
        }
    };

    vector<TNode> tr;

public:
    BinaryTrie() {
        tr.reserve(700000);
        tr.emplace_back();
    }

    void clear() {
        tr.clear();
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
        int ans = 0;

        for (int bit = MAX_BIT; bit >= 0; --bit) {
            int b = (x >> bit) & 1;
            int wanted = b ^ 1;

            if (tr[node].child[wanted] != -1) {
                ans |= (1 << bit);
                node = tr[node].child[wanted];
            }
            else {
                node = tr[node].child[b];
            }
        }

        return ans;
    }
};


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, t;
    cin >> n >> m >> t;

    vector<int> a(n + 1);
    vector<int> pref(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        pref[i] = pref[i - 1] ^ a[i];
    }

    int N = n + 1;

    // ------------------------------------------------------------
    // Persistent trie over prefix XOR values
    //
    // root[k] contains:
    // pref[0 ... k-1]
    // ------------------------------------------------------------

    PersistentTrie persistent((N + 5) * 32);

    vector<int> root(N + 1, 0);

    for (int i = 0; i < N; ++i) {
        root[i + 1] =
            persistent.insert(root[i], pref[i]);
    }

    // ------------------------------------------------------------
    // Square-root decomposition
    // ------------------------------------------------------------

    const int BLOCK = 145;

    int numBlocks =
        (N + BLOCK - 1) / BLOCK;

    /*
        best[b][r]

        Maximum XOR pair among:

            pref[startOfBlock(b) ... r]
    */

    vector<vector<int>> best(
        numBlocks,
        vector<int>(N, 0)
    );

    BinaryTrie tempTrie;

    for (int b = 0; b < numBlocks; ++b) {

        int start = b * BLOCK;

        tempTrie.clear();
        tempTrie.insert(pref[start]);

        int currentBest = 0;

        best[b][start] = 0;

        for (int r = start + 1; r < N; ++r) {

            currentBest = max(
                currentBest,
                tempTrie.maxXor(pref[r])
            );

            tempTrie.insert(pref[r]);

            best[b][r] = currentBest;
        }
    }

    // ------------------------------------------------------------
    // Process online queries
    // ------------------------------------------------------------

    long long ans = 0;

    while (m--) {
        long long x, y;
        cin >> x >> y;

        int l = min(
            (int)((x + ans * t) % n) + 1,
            (int)((y + ans * t) % n) + 1
        );

        int r = max(
            (int)((x + ans * t) % n) + 1,
            (int)((y + ans * t) % n) + 1
        );

        /*
            Original range:
                [l, r]

            Prefix-XOR range:
                [l-1, r]
        */

        int L = l - 1;
        int R = r;

        // First block boundary >= L
        int boundary =
            ((L + BLOCK - 1) / BLOCK) * BLOCK;

        int answer = 0;

        /*
            Use precomputed result for the aligned suffix.
        */
        if (boundary <= R) {
            int b = boundary / BLOCK;

            answer = best[b][R];
        }

        /*
            Process the small left fringe.
        */
        int fringeEnd =
            min(R, boundary - 1);

        for (int i = L;
             i <= fringeEnd;
             ++i) {

            if (i + 1 <= R) {

                /*
                    Search pref[i+1 ... R].

                    root[i+1] contains pref[0 ... i]
                    root[R+1] contains pref[0 ... R]
                */

                int candidate =
                    persistent.maxXor(
                        root[i + 1],
                        root[R + 1],
                        pref[i]
                    );

                answer =
                    max(answer, candidate);
            }
        }

        ans = answer;

        cout << ans << '\n';
    }

    return 0;
}
```

------------------------------------------------------------------------

# Correctness

We prove the algorithm in three steps.

## Lemma 1 --- Subarray XOR Becomes a Prefix-XOR Pair

For any:

``` text
l <= i <= j <= r
```

the XOR of subarray `[i, j]` is:

``` text
pref[j] XOR pref[i-1]
```

Both prefix indices belong to:

``` text
[l-1, r]
```

Conversely, any two indices:

``` text
p < q
```

inside:

``` text
[l-1, r]
```

correspond to the valid subarray:

``` text
[p+1, q]
```

Therefore, the maximum subarray XOR in `[l,r]` equals the maximum XOR
pair in:

``` text
pref[l-1 ... r]
```

------------------------------------------------------------------------

## Lemma 2 --- `best[b][R]` Covers the Aligned Suffix

For block `b`, preprocessing starts with:

``` text
pref[start]
```

and adds every subsequent value one at a time.

Before inserting `pref[r]`, the trie contains:

``` text
pref[start ... r-1]
```

Querying the trie with `pref[r]` therefore finds the best pair whose
second endpoint is `r`.

Taking the maximum over all such right endpoints gives exactly the
maximum XOR pair in:

``` text
pref[start ... R]
```

Thus:

``` text
best[b][R]
```

is correct.

------------------------------------------------------------------------

## Lemma 3 --- Fringe Queries Cover Every Remaining Pair

The query range is divided into:

``` text
fringe + aligned suffix
```

Pairs entirely inside the aligned suffix are handled by:

``` text
best[b][R]
```

For every index `i` in the fringe, the persistent trie finds the maximum
XOR between:

``` text
pref[i]
```

and every later value:

``` text
pref[i+1 ... R]
```

Therefore this includes:

-   pairs entirely inside the fringe;
-   pairs crossing from the fringe to the aligned suffix.

Thus every possible pair in `[L,R]` is considered.

Combining Lemmas 1--3 proves that the algorithm returns the maximum
subarray XOR for every query.

------------------------------------------------------------------------

# Time Complexity

Let:

``` text
N = n + 1
B = block size
```

and let the binary trie depth be:

``` text
31
```

## Prefix XOR

``` text
O(N)
```

------------------------------------------------------------------------

## Persistent Trie Construction

Each prefix value creates at most 32 trie nodes.

Therefore:

``` text
O(31N)
```

which is effectively:

``` text
O(N log MAX_VALUE)
```

------------------------------------------------------------------------

## Block Preprocessing

There are approximately:

``` text
N / B
```

block starts.

For each block start, we scan up to `N` values.

Each trie insertion/query takes:

``` text
O(31)
```

Therefore:

``` text
O((N / B) * N * 31)
```

or:

``` text
O(N² log MAX_VALUE / B)
```

With:

``` text
N <= 20001
B = 145
```

this is practical.

------------------------------------------------------------------------

## Per Query

The aligned suffix is answered in:

``` text
O(1)
```

The left fringe contains fewer than:

``` text
B
```

elements.

For each fringe element, one persistent-trie query costs:

``` text
O(31)
```

Therefore:

``` text
O(B * 31)
```

or:

``` text
O(B log MAX_VALUE)
```

With `B = 145`, this is roughly a few thousand simple trie operations
per query.

------------------------------------------------------------------------

# Space Complexity

## Prefix Arrays

``` text
O(N)
```

## Persistent Trie

Each of the `N` prefix values creates approximately 32 nodes:

``` text
O(31N)
```

## Precomputed `best`

There are approximately:

``` text
N / B
```

blocks, and each stores up to `N` answers:

``` text
O(N² / B)
```

Therefore total memory is:

``` text
O(N log MAX_VALUE + N² / B)
```

For `N <= 20001` and `B = 145`, this fits within the intended memory
constraints.

------------------------------------------------------------------------

# Trade-offs

## Advantages

-   Supports **online queries**, including the `t = 1` case.
-   Converts maximum subarray XOR into a much cleaner maximum XOR-pair
    problem.
-   Persistent trie performs range-restricted maximum XOR queries
    efficiently.
-   Square-root decomposition reduces each online query to fewer than
    `B` trie queries.
-   Avoids recomputing the answer for the entire `[l,r]` range.
-   Works within the relatively moderate `n, m <= 20000` constraints.

## Disadvantages

-   Preprocessing is heavier than a simple trie solution.
-   The `best` table requires `O(N²/B)` memory.
-   Persistent tries use more memory than ordinary tries because each
    insertion creates new nodes.
-   Performance depends on the block size.
-   The implementation is more complex than standard maximum subarray
    XOR.
-   This approach is designed around the moderate `N = 20000`
    constraint; for much larger `N`, a more sophisticated data structure
    would be necessary.

------------------------------------------------------------------------

# Why Not Compute Each Query Directly?

A direct solution could build a trie for every query and process:

``` text
pref[l-1 ... r]
```

This costs:

``` text
O((r-l+1) * 31)
```

per query.

In the worst case:

``` text
O(N * M * 31)
```

With:

``` text
N, M <= 20000
```

this is far too expensive.

The square-root decomposition reduces the work per query to
approximately:

``` text
O(sqrt(N) * 31)
```

after preprocessing.

------------------------------------------------------------------------

# Why Not Mo's Algorithm?

Mo's algorithm is effective for offline range queries.

However, when:

``` text
t = 1
```

the actual query range depends on the previous answer:

``` text
l, r depend on ans
```

Therefore query `k+1` cannot be decoded until query `k` has been
answered.

The queries cannot be freely reordered.

Hence an online solution is required.

------------------------------------------------------------------------

# Summary

The central transformation is:

``` text
Maximum subarray XOR in a[l ... r]

            ↓

Maximum XOR pair in:

pref[l-1 ... r]
```

Then split the prefix range into:

``` text
small left fringe + block-aligned suffix
```

Use:

``` text
best[block][R]
```

for the aligned suffix and a:

``` text
Persistent Binary Trie
```

for pairs involving the fringe.

Final complexities are approximately:

``` text
Preprocessing:
O(N² * 31 / B)

Per Query:
O(B * 31)

Persistent Trie:
O(N * 31)

Space:
O(N² / B + N * 31)
```

For:

``` text
N <= 20001
B ≈ 145
```

this provides an efficient online solution.
