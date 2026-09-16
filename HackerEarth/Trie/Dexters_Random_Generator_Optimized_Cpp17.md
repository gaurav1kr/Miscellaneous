# Dexter's Random Generator --- Optimized C++17 Solution

## Approach

For a query `(u, v)`, the random generator performs:

``` text
(X1, Y1) = Process(u, v)
(X2, Y2) = Process(u, v)

A = X1 XOR Y1
B = X2 XOR Y2

return abs(A - B)
```

In `Process(u, v)`:

-   `X` can independently be either `A[u]` or `A[v]`.
-   `Y` can be `A[r]`, where `r` is any node on the path from `u` to
    `v`.

Therefore, the set of possible XOR values is:

``` text
A[u] XOR A[r]
A[v] XOR A[r]
```

for every node `r` on the path `u -> v`.

### Key Observation

Both `u` and `v` themselves belong to the path.

Hence `0` is always achievable:

``` text
A[u] XOR A[u] = 0
```

and also:

``` text
A[v] XOR A[v] = 0
```

The query asks for the maximum possible:

``` text
abs(A - B)
```

where `A` and `B` are two independently generated XOR values.

Since all XOR values are non-negative and `0` is achievable, the maximum
absolute difference is simply the largest achievable XOR value.

So the query reduces to:

``` text
max(
    max over r on path(u,v) of A[u] XOR A[r],
    max over r on path(u,v) of A[v] XOR A[r]
)
```

We therefore need an efficient way to answer:

> Given nodes `u`, `v` and a value `x`, find the maximum `x XOR A[r]`
> over every node `r` on the tree path `u -> v`.

------------------------------------------------------------------------

## Persistent Binary Trie

Root the tree at node `1`.

For every tree node `u`, build a persistent binary trie:

``` text
root[u]
```

containing all values:

``` text
A[x]
```

for nodes `x` on the path:

``` text
1 -> u
```

The trie for a child reuses almost all nodes from its parent's trie and
creates only one new path for `A[child]`.

Since:

``` text
A[i] <= 10^9
```

31 bits (`30 ... 0`) are sufficient.

------------------------------------------------------------------------

## Extracting a Tree Path

Let:

``` text
w = LCA(u, v)
```

and:

``` text
p = parent[w]
```

The multiset of values on the path `u -> v` can be represented by:

``` text
root[u] + root[v] - root[w] - root[p]
```

Why?

-   `root[u]` contains the root-to-`u` path.
-   `root[v]` contains the root-to-`v` path.
-   Their common prefix up to `w` is counted twice.
-   Subtracting `root[w]` and `root[parent[w]]` removes the unwanted
    duplicate prefix while retaining `w` exactly once.

Thus, while traversing the persistent trie, the number of path values
available in a branch is:

``` text
cnt(child from root[u])
+ cnt(child from root[v])
- cnt(child from root[w])
- cnt(child from root[parent[w]])
```

------------------------------------------------------------------------

## Maximum XOR on a Path

To maximize:

``` text
x XOR A[r]
```

process bits from most significant to least significant.

Suppose the current bit of `x` is `b`.

We prefer a path value with bit:

``` text
b XOR 1
```

because that makes the XOR bit equal to `1`.

Using the four persistent trie roots, check whether at least one value
from the actual `u -> v` path exists in that preferred branch.

If yes:

-   take that branch;
-   set the corresponding bit in the answer.

Otherwise, take the same-bit branch.

This greedily constructs the maximum possible XOR.

------------------------------------------------------------------------

## LCA

Binary lifting is used to find:

``` text
LCA(u, v)
```

in:

``` text
O(log N)
```

time.

An iterative traversal is used to determine parents and depths so that a
tree shaped like a chain of `10^5` nodes does not cause recursive DFS
stack overflow.

------------------------------------------------------------------------

## C++17 Code

``` cpp
#include <bits/stdc++.h>
using namespace std;

static constexpr int MAX_BIT = 30;
static constexpr int LOG = 18;   // 2^17 > 1e5

struct TrieNode {
    int child[2];
    int cnt;

    TrieNode() {
        child[0] = child[1] = 0;
        cnt = 0;
    }
};

class PersistentTrie {
private:
    vector<TrieNode> tr;

public:
    PersistentTrie(int maxNodes) {
        tr.reserve(maxNodes);

        // Node 0 = null node
        tr.emplace_back();
    }

    int insert(int oldRoot, int x) {

        int newRoot = (int)tr.size();
        tr.push_back(tr[oldRoot]);
        tr[newRoot].cnt++;

        int oldNode = oldRoot;
        int newNode = newRoot;

        for (int bit = MAX_BIT; bit >= 0; --bit) {

            int b = (x >> bit) & 1;

            int oldChild = tr[oldNode].child[b];

            int newChild = (int)tr.size();
            tr.push_back(tr[oldChild]);

            tr[newChild].cnt++;

            tr[newNode].child[b] = newChild;

            oldNode = oldChild;
            newNode = newChild;
        }

        return newRoot;
    }

    /*
        Find maximum XOR of x with any value on path u-v.

        Multiset of path values:

            root[u]
          + root[v]
          - root[lca]
          - root[parent(lca)]

        root[node] contains all A-values from root of tree
        to node, inclusive.
    */
    int maxXorOnPath(
        int rootU,
        int rootV,
        int rootLca,
        int rootParentLca,
        int x
    ) const {

        int u = rootU;
        int v = rootV;
        int l = rootLca;
        int p = rootParentLca;

        int result = 0;

        for (int bit = MAX_BIT; bit >= 0; --bit) {

            int b = (x >> bit) & 1;

            // To maximize XOR, prefer opposite bit.
            int wanted = b ^ 1;

            int cu = tr[u].child[wanted];
            int cv = tr[v].child[wanted];
            int cl = tr[l].child[wanted];
            int cp = tr[p].child[wanted];

            int available =
                tr[cu].cnt +
                tr[cv].cnt -
                tr[cl].cnt -
                tr[cp].cnt;

            if (available > 0) {

                result |= (1 << bit);

                u = cu;
                v = cv;
                l = cl;
                p = cp;
            }
            else {

                int same = b;

                u = tr[u].child[same];
                v = tr[v].child[same];
                l = tr[l].child[same];
                p = tr[p].child[same];
            }
        }

        return result;
    }
};


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    vector<int> A(N + 1);

    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }

    vector<vector<int>> graph(N + 1);

    for (int i = 0; i < N - 1; ++i) {

        int u, v;
        cin >> u >> v;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    /*
        Each insertion creates about 32 trie nodes.

        N <= 1e5
        => around 3.2 million nodes.
    */
    PersistentTrie trie((N + 5) * 32);

    vector<int> root(N + 1, 0);
    vector<int> depth(N + 1, 0);

    vector<array<int, LOG>> up(N + 1);

    /*
        Iterative traversal to avoid stack overflow
        on a chain of 1e5 nodes.
    */
    vector<int> order;
    order.reserve(N);

    vector<int> parent(N + 1, 0);

    parent[1] = 0;
    depth[1] = 0;

    order.push_back(1);

    for (int i = 0; i < (int)order.size(); ++i) {

        int u = order[i];

        for (int v : graph[u]) {

            if (v == parent[u])
                continue;

            parent[v] = u;
            depth[v] = depth[u] + 1;

            order.push_back(v);
        }
    }

    /*
        Build persistent tries and binary-lifting table
        in parent-before-child order.
    */
    for (int u : order) {

        root[u] =
            trie.insert(root[parent[u]], A[u]);

        up[u][0] = parent[u];

        for (int j = 1; j < LOG; ++j) {
            up[u][j] =
                up[up[u][j - 1]][j - 1];
        }
    }

    auto lca = [&](int u, int v) {

        if (depth[u] < depth[v])
            swap(u, v);

        int diff = depth[u] - depth[v];

        for (int j = LOG - 1; j >= 0; --j) {

            if (diff & (1 << j))
                u = up[u][j];
        }

        if (u == v)
            return u;

        for (int j = LOG - 1; j >= 0; --j) {

            if (up[u][j] != up[v][j]) {
                u = up[u][j];
                v = up[v][j];
            }
        }

        return up[u][0];
    };


    while (Q--) {

        int u, v;
        cin >> u >> v;

        int w = lca(u, v);

        int parentW = parent[w];

        /*
            Possible XOR values include:

                A[u] XOR A[r]
                A[v] XOR A[r]

            for every r on path u-v.

            Zero is always achievable, so the maximum
            absolute difference equals the maximum
            possible XOR value.
        */

        int ansFromU =
            trie.maxXorOnPath(
                root[u],
                root[v],
                root[w],
                root[parentW],
                A[u]
            );

        int ansFromV =
            trie.maxXorOnPath(
                root[u],
                root[v],
                root[w],
                root[parentW],
                A[v]
            );

        cout << max(ansFromU, ansFromV) << '\n';
    }

    return 0;
}
```

------------------------------------------------------------------------

## Time Complexity

Let:

``` text
B = 31
```

be the number of relevant bits.

### Tree Traversal

Finding parent and depth for every node:

``` text
O(N)
```

### LCA Preprocessing

For every node, build `LOG` binary ancestors:

``` text
O(N log N)
```

### Persistent Trie Construction

Each of the `N` values is inserted through 31 bit levels:

``` text
O(N * B)
```

Since `B = 31`, this is effectively linear in `N`.

### Each Query

LCA:

``` text
O(log N)
```

Two maximum-XOR path queries:

``` text
2 * O(B)
```

Therefore:

``` text
O(log N + B)
```

With fixed 31-bit integers:

``` text
O(log N)
```

per query.

### Total

``` text
O(N log N + N * B + Q * (log N + B))
```

For fixed 31-bit values:

``` text
O((N + Q) log N)
```

------------------------------------------------------------------------

## Space Complexity

### Tree

Adjacency list:

``` text
O(N)
```

### Binary Lifting

``` text
O(N log N)
```

### Persistent Trie

Each inserted value creates approximately 32 new nodes:

``` text
O(N * B)
```

### Other Arrays

`parent`, `depth`, `root`, and `A`:

``` text
O(N)
```

### Total

``` text
O(N log N + N * B)
```

For fixed 31-bit values:

``` text
O(N log N)
```

------------------------------------------------------------------------

## Trade-offs

### Advantages

-   Handles `N, Q <= 10^5`.
-   Each query is very fast.
-   Persistent trie efficiently restricts XOR search to a tree path.
-   Binary lifting gives efficient LCA queries.
-   No per-query traversal of the actual tree path is required.
-   Iterative tree traversal avoids recursion-depth problems.
-   The query reduction from maximum absolute difference to maximum XOR
    significantly simplifies the problem.

### Disadvantages

-   Persistent tries use substantial memory because each tree node
    creates roughly 32 trie nodes.
-   Binary lifting adds another `O(N log N)` memory structure.
-   Implementation is more complex than ordinary tree traversal.
-   The fixed `MAX_BIT = 30` relies on the constraint `A[i] <= 10^9`.
-   If node values were updated dynamically, this static persistent-trie
    approach would no longer be sufficient without a more advanced
    structure.

------------------------------------------------------------------------

## Summary

The main reduction is:

``` text
Query(u,v)

    ↓

Possible values:
A[u] XOR A[r]
A[v] XOR A[r]

for r on path(u,v)

    ↓

0 is always achievable

    ↓

Maximum absolute difference
= maximum achievable XOR

    ↓

Two maximum-XOR-on-tree-path queries
```

Use:

``` text
LCA + Persistent Binary Trie
```

to answer each path query efficiently.

Final complexities:

``` text
Preprocessing:
O(N log N + 31N)

Each Query:
O(log N + 31)

Space:
O(N log N + 31N)
```
