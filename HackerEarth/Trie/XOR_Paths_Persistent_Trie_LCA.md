# XOR Paths --- Persistent Binary Trie + LCA

## Problem

You are given a weighted tree with `N` nodes and `N - 1` edges.

Each edge has a weight `w`.

For every query `(u, v, x)`, consider all edge weights on the path from
node `u` to node `v`. For each edge weight `w`, calculate:

`w XOR x`

Print the **maximum XOR value** obtainable from any edge on that path.

### Constraints

-   `2 <= N, Q <= 10^5`
-   Edge weights and `x` can be as large as `10^18`
-   The graph is a tree

------------------------------------------------------------------------

## Approach

A direct traversal of the path for every query can take `O(N)` time per
query, which is too slow for `10^5` queries.

We combine two techniques:

1.  **LCA using Binary Lifting**
2.  **Persistent Binary Trie**

### 1. Root the Tree

Root the tree at node `1`.

For every node `u`, build a persistent trie containing all edge weights
on the path:

`1 -> u`

Let this trie root be `trieRoot[u]`.

If `v` is a child of `u` connected by an edge of weight `w`, then:

`trieRoot[v] = trieRoot[u] + w`

Persistence allows us to create this new version without copying the
entire trie.

------------------------------------------------------------------------

## Path Representation

For a query between nodes `u` and `v`, let:

`l = LCA(u, v)`

The multiset of edge weights on path `u -> v` is:

`Trie[u] + Trie[v] - 2 * Trie[l]`

Why?

-   `Trie[u]` contains edges from root `1` to `u`.
-   `Trie[v]` contains edges from root `1` to `v`.
-   Edges from root `1` to `LCA(u,v)` occur in both tries.
-   Therefore, subtract them twice.

Because we store **edge weights**, no extra LCA value needs to be added.

------------------------------------------------------------------------

## Maximum XOR Query

To maximize `w XOR x`, process bits from the most significant bit to the
least significant bit.

Suppose the current bit of `x` is `b`.

To make the XOR bit equal to `1`, we prefer an edge weight whose current
bit is:

`b ^ 1`

For the preferred branch, calculate how many edge weights on the actual
`u -> v` path are present there:

``` text
count =
    cnt[uBranch]
  + cnt[vBranch]
  - 2 * cnt[lcaBranch]
```

If `count > 0`, choose the opposite bit and set the current answer bit
to `1`.

Otherwise, choose the same bit as `x`.

This greedily constructs the maximum possible XOR.

------------------------------------------------------------------------

## Important 60-bit Detail

The values can be as large as `10^18`.

Since:

`10^18 < 2^60`

we must process bits `59` down to `0`.

Using only 17 or 32 bits causes wrong answers on hidden tests containing
large values.

Therefore the solution uses:

``` cpp
using ull = unsigned long long;
const int MAX_BIT = 59;
```

and bit operations such as:

``` cpp
1ULL << bit
```

------------------------------------------------------------------------

## C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;

const int MAX_BIT = 59;
const int LOG = 18;

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
    vector<TrieNode> trie;

public:
    PersistentTrie(int n) {
        trie.reserve((long long)(n + 5) * 61);
        trie.emplace_back(); // null node
    }

    int cloneNode(int node) {
        trie.push_back(trie[node]);
        return (int)trie.size() - 1;
    }

    int insert(int oldRoot, ull x) {
        int newRoot = cloneNode(oldRoot);
        trie[newRoot].cnt++;

        int oldNode = oldRoot;
        int newNode = newRoot;

        for (int bit = MAX_BIT; bit >= 0; --bit) {
            int b = (x >> bit) & 1ULL;

            int oldChild = trie[oldNode].child[b];
            int newChild = cloneNode(oldChild);

            trie[newNode].child[b] = newChild;
            trie[newChild].cnt++;

            oldNode = oldChild;
            newNode = newChild;
        }

        return newRoot;
    }

    ull maxXor(int rootU, int rootV, int rootLCA, ull x) {
        int nodeU = rootU;
        int nodeV = rootV;
        int nodeL = rootLCA;

        ull answer = 0;

        for (int bit = MAX_BIT; bit >= 0; --bit) {
            int b = (x >> bit) & 1ULL;

            // Prefer opposite bit to make XOR bit = 1.
            int wanted = b ^ 1;

            int uChild = trie[nodeU].child[wanted];
            int vChild = trie[nodeV].child[wanted];
            int lChild = trie[nodeL].child[wanted];

            int countWanted =
                trie[uChild].cnt +
                trie[vChild].cnt -
                2 * trie[lChild].cnt;

            if (countWanted > 0) {
                answer |= (1ULL << bit);

                nodeU = uChild;
                nodeV = vChild;
                nodeL = lChild;
            } else {
                int same = b;

                nodeU = trie[nodeU].child[same];
                nodeV = trie[nodeV].child[same];
                nodeL = trie[nodeL].child[same];
            }
        }

        return answer;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    vector<vector<pair<int, ull>>> graph(N + 1);

    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        ull w;

        cin >> u >> v >> w;

        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }

    PersistentTrie persistentTrie(N);

    vector<int> depth(N + 1);
    vector<int> trieRoot(N + 1);

    static int up[100005][LOG];
    memset(up, 0, sizeof(up));

    queue<int> qu;
    vector<bool> visited(N + 1, false);

    qu.push(1);
    visited[1] = true;

    depth[1] = 0;
    trieRoot[1] = 0;

    while (!qu.empty()) {
        int u = qu.front();
        qu.pop();

        for (auto [v, w] : graph[u]) {
            if (visited[v])
                continue;

            visited[v] = true;
            depth[v] = depth[u] + 1;

            up[v][0] = u;

            for (int j = 1; j < LOG; ++j) {
                up[v][j] =
                    up[up[v][j - 1]][j - 1];
            }

            trieRoot[v] =
                persistentTrie.insert(trieRoot[u], w);

            qu.push(v);
        }
    }

    auto getLCA = [&](int a, int b) {
        if (depth[a] < depth[b])
            swap(a, b);

        int diff = depth[a] - depth[b];

        for (int j = LOG - 1; j >= 0; --j) {
            if (diff & (1 << j))
                a = up[a][j];
        }

        if (a == b)
            return a;

        for (int j = LOG - 1; j >= 0; --j) {
            if (up[a][j] != up[b][j]) {
                a = up[a][j];
                b = up[b][j];
            }
        }

        return up[a][0];
    };

    while (Q--) {
        int u, v;
        ull x;

        cin >> u >> v >> x;

        int lca = getLCA(u, v);

        cout << persistentTrie.maxXor(
                    trieRoot[u],
                    trieRoot[v],
                    trieRoot[lca],
                    x)
             << '\n';
    }

    return 0;
}
```

------------------------------------------------------------------------

## Correctness

For each node, its persistent trie stores exactly the edge weights from
the root to that node.

For a query `(u, v, x)`, combining the three trie versions as:

`Trie[u] + Trie[v] - 2 * Trie[LCA(u,v)]`

leaves exactly the edge weights on the path from `u` to `v`.

At every bit, choosing a stored bit opposite to the corresponding bit of
`x` produces XOR bit `1`, which is always better than XOR bit `0` at the
most significant undecided position.

The subtree counts tell us whether such an edge exists on the requested
path. Therefore, greedily choosing the opposite branch whenever its path
count is positive constructs the maximum possible XOR.

------------------------------------------------------------------------

## Time Complexity

### Preprocessing

Binary lifting:

`O(N log N)`

Persistent trie construction:

`O(60 * N)`

### Each Query

LCA:

`O(log N)`

Maximum XOR trie traversal:

`O(60)`

Therefore:

`O(log N + 60) = O(log N)` per query.

### Overall

`O(N log N + 60N + Q(log N + 60))`

which is effectively:

`O((N + Q) log N)`

for the given constraints.

------------------------------------------------------------------------

## Space Complexity

Binary lifting table:

`O(N log N)`

Persistent trie:

`O(60 * N)`

Adjacency list:

`O(N)`

Therefore the total space complexity is:

`O(N log N + 60N)`

which is effectively:

`O(N log N)`.

------------------------------------------------------------------------

## Key Takeaways

-   Use **LCA** to split a tree path using root-to-node information.
-   Use a **Persistent Binary Trie** to maintain a separate root-to-node
    edge-weight set for every node efficiently.
-   Use subtree counts from three trie versions to determine whether a
    desired bit exists on the queried path.
-   For values up to `10^18`, always process **60 bits** (`59` through
    `0`) and use a 64-bit integer type.
