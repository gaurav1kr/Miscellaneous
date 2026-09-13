# MST Revisited — HackerEarth

## Problem Summary

You are given an undirected connected graph with:

```text
N vertices
N weighted edges
```

The graph has no self-loops or parallel edges and remains connected after every query.

Because a connected graph with `N` vertices and `N` edges has exactly one cycle, the graph is always **unicyclic**.

Each query gives five encoded integers:

```text
x1 x2 x3 x4 x5
```

Let `ans` be the previous query answer, or `0` for the first query.

Decode:

```text
shift = ans % 100

a = x1 + shift
b = x2 + shift
u = x3 + shift
v = x4 + shift
c = x5 + shift
```

Then:

```text
delete edge (a,b)
add edge (u,v) with weight c
output MST cost
```

Constraints:

```text
3 <= N <= 300000
1 <= Q <= 300000
edge weight <= 1000000
```

So recomputing the MST from scratch after every query is too slow.

---

# Approach

## Main Observation

A connected graph with:

```text
N vertices
N edges
```

contains exactly one cycle.

Therefore the graph can always be represented as:

```text
spanning tree of N - 1 edges
+
1 extra edge
```

Suppose the extra edge joins `u` and `v`.

Then the unique cycle consists of:

```text
tree path from u to v
+
extra edge (u,v)
```

To obtain an MST, remove the maximum-weight edge on that cycle.

Therefore:

```text
MST cost
=
sum of all graph edge weights
-
maximum edge weight on the unique cycle
```

This reduces the problem to maintaining:

```text
1. a dynamic spanning tree
2. one non-tree edge
3. maximum edge weight on a tree path
```

The appropriate data structure is a **Link-Cut Tree**.

---

## Edge-as-Node Representation

Link-Cut Trees store values on nodes, but our values are edge weights.

So represent every graph edge:

```text
u ------- v
```

as:

```text
u ---- edgeNode ---- v
```

The edge node stores the weight.

Original graph vertices store a very small value such as:

```text
-INF
```

so they never become the maximum value on a path.

Now:

```cpp
queryMax(u, v)
```

returns the maximum **edge weight** on the tree path from `u` to `v`.

---

## Initial Graph Construction

Use DSU to choose any spanning tree from the initial `N` edges.

For every edge `(u,v)`:

```text
if DSU can unite u and v:
    use it as a tree edge
else:
    it is the unique extra edge
```

Then insert only the `N-1` tree edges into the Link-Cut Tree.

This is faster than repeatedly performing Link-Cut Tree connectivity checks during initialization.

---

# Query Processing

Each query performs:

```text
delete one edge
add one edge
calculate MST
```

## Deleting an Edge

There are two cases.

### Case 1: Deleted Edge Is the Extra Edge

The maintained spanning tree stays connected.

Simply remove the extra edge:

```text
extraEdge = none
```

### Case 2: Deleted Edge Is a Tree Edge

Remove it from the Link-Cut Tree using two `cut` operations.

This may split the maintained tree into two components.

The old extra edge may reconnect the two components.

If the endpoints of that extra edge are no longer connected:

```text
promote the extra edge into the tree
```

using:

```text
link(extra.u, extraEdgeNode)
link(extraEdgeNode, extra.v)
```

Then:

```text
extraEdge = none
```

---

## Adding the New Edge

After deletion there are two possible situations.

### Situation A: `extraEdge` Is Empty

The maintained tree is connected, so the new edge creates the unique cycle.

Therefore the new edge becomes the new:

```text
extraEdge
```

### Situation B: `extraEdge` Still Exists

The maintained tree is currently split into two components.

Because the final graph is guaranteed connected, the newly added edge must reconnect those two components.

So add the new edge to the Link-Cut Tree as a tree edge.

The previous `extraEdge` remains outside the tree.

---

# Computing the MST

After deletion and insertion, the graph again has:

```text
N vertices
N edges
```

and exactly one cycle.

Let the extra edge be:

```text
(u, v, w)
```

Find the maximum edge weight on the tree path:

```cpp
maximumTreeEdge = lct.queryMax(u, v);
```

Then:

```cpp
maximumCycleEdge =
    max(w, maximumTreeEdge);
```

Finally:

```cpp
MST =
    totalWeight - maximumCycleEdge;
```

---

# Complete C++17 Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

static const int NEG_INF = -1000000007;

struct LinkCutTree
{
    int n;

    vector<int> leftChild;
    vector<int> rightChild;
    vector<int> parent;

    vector<int> value;
    vector<int> maxValue;

    vector<unsigned char> reversed;
    vector<int> stk;

    LinkCutTree(int n)
        : n(n),
          leftChild(n + 1),
          rightChild(n + 1),
          parent(n + 1),
          value(n + 1, NEG_INF),
          maxValue(n + 1, NEG_INF),
          reversed(n + 1),
          stk(n + 1)
    {
    }

    inline bool isRoot(int x)
    {
        int p = parent[x];

        return p == 0 ||
               (leftChild[p] != x &&
                rightChild[p] != x);
    }

    inline void pull(int x)
    {
        int best = value[x];

        if (leftChild[x])
            best = max(best, maxValue[leftChild[x]]);

        if (rightChild[x])
            best = max(best, maxValue[rightChild[x]]);

        maxValue[x] = best;
    }

    inline void applyReverse(int x)
    {
        if (!x)
            return;

        swap(leftChild[x], rightChild[x]);
        reversed[x] ^= 1;
    }

    inline void push(int x)
    {
        if (!reversed[x])
            return;

        applyReverse(leftChild[x]);
        applyReverse(rightChild[x]);

        reversed[x] = 0;
    }

    inline void rotate(int x)
    {
        int y = parent[x];
        int z = parent[y];

        bool xIsRight = (rightChild[y] == x);

        int middle =
            xIsRight ? leftChild[x] : rightChild[x];

        if (!isRoot(y))
        {
            if (leftChild[z] == y)
                leftChild[z] = x;
            else
                rightChild[z] = x;
        }

        parent[x] = z;

        if (xIsRight)
        {
            leftChild[x] = y;
            rightChild[y] = middle;
        }
        else
        {
            rightChild[x] = y;
            leftChild[y] = middle;
        }

        parent[y] = x;

        if (middle)
            parent[middle] = y;

        pull(y);
        pull(x);
    }

    void splay(int x)
    {
        int top = 0;
        int y = x;

        stk[top++] = y;

        while (!isRoot(y))
        {
            y = parent[y];
            stk[top++] = y;
        }

        while (top)
            push(stk[--top]);

        while (!isRoot(x))
        {
            int y = parent[x];
            int z = parent[y];

            if (!isRoot(y))
            {
                bool sameDirection =
                    (leftChild[y] == x) ==
                    (leftChild[z] == y);

                if (sameDirection)
                    rotate(y);
                else
                    rotate(x);
            }

            rotate(x);
        }

        pull(x);
    }

    void access(int x)
    {
        int last = 0;

        for (int y = x; y; y = parent[y])
        {
            splay(y);

            rightChild[y] = last;

            pull(y);

            last = y;
        }

        splay(x);
    }

    void makeRoot(int x)
    {
        access(x);
        applyReverse(x);
    }

    int findRoot(int x)
    {
        access(x);

        while (leftChild[x])
        {
            push(x);
            x = leftChild[x];
        }

        splay(x);

        return x;
    }

    bool connected(int a, int b)
    {
        if (a == b)
            return true;

        makeRoot(a);

        return findRoot(b) == a;
    }

    void link(int a, int b)
    {
        makeRoot(a);
        parent[a] = b;
    }

    void cut(int a, int b)
    {
        makeRoot(a);
        access(b);

        if (leftChild[b] == a)
        {
            leftChild[b] = 0;
            parent[a] = 0;

            pull(b);
        }
    }

    int queryMax(int a, int b)
    {
        makeRoot(a);
        access(b);

        return maxValue[b];
    }

    void setValue(int node, int val)
    {
        value[node] = val;
        maxValue[node] = val;
    }
};

struct DSU
{
    vector<int> parent;
    vector<int> size;

    DSU(int n)
        : parent(n + 1),
          size(n + 1, 1)
    {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x)
    {
        while (parent[x] != x)
        {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }

        return x;
    }

    bool unite(int a, int b)
    {
        a = find(a);
        b = find(b);

        if (a == b)
            return false;

        if (size[a] < size[b])
            swap(a, b);

        parent[b] = a;
        size[a] += size[b];

        return true;
    }
};

struct Edge
{
    int u;
    int v;
    int weight;

    int lctNode;

    bool treeEdge;
};

inline uint64_t edgeKey(int u, int v)
{
    if (u > v)
        swap(u, v);

    return
        (uint64_t(uint32_t(u)) << 32)
        | uint32_t(v);
}

struct FastHashMap
{
    size_t capacity;
    size_t mask;

    vector<uint64_t> keys;
    vector<int> values;

    // 0 = empty
    // 1 = occupied
    // 2 = deleted
    vector<unsigned char> state;

    explicit FastHashMap(size_t expected)
    {
        capacity = 1;

        while (capacity < expected * 4)
            capacity <<= 1;

        mask = capacity - 1;

        keys.resize(capacity);
        values.resize(capacity);
        state.resize(capacity);
    }

    static inline uint64_t hashValue(uint64_t x)
    {
        x += 0x9e3779b97f4a7c15ULL;

        x = (x ^ (x >> 30))
            * 0xbf58476d1ce4e5b9ULL;

        x = (x ^ (x >> 27))
            * 0x94d049bb133111ebULL;

        return x ^ (x >> 31);
    }

    void insert(uint64_t key, int value)
    {
        size_t pos = hashValue(key) & mask;
        size_t firstDeleted = capacity;

        while (true)
        {
            if (state[pos] == 0)
            {
                if (firstDeleted != capacity)
                    pos = firstDeleted;

                keys[pos] = key;
                values[pos] = value;
                state[pos] = 1;

                return;
            }

            if (state[pos] == 2)
            {
                if (firstDeleted == capacity)
                    firstDeleted = pos;
            }
            else if (keys[pos] == key)
            {
                values[pos] = value;
                return;
            }

            pos = (pos + 1) & mask;
        }
    }

    int get(uint64_t key)
    {
        size_t pos = hashValue(key) & mask;

        while (true)
        {
            if (state[pos] == 0)
                return 0;

            if (state[pos] == 1 &&
                keys[pos] == key)
            {
                return values[pos];
            }

            pos = (pos + 1) & mask;
        }
    }

    void erase(uint64_t key)
    {
        size_t pos = hashValue(key) & mask;

        while (true)
        {
            if (state[pos] == 0)
                return;

            if (state[pos] == 1 &&
                keys[pos] == key)
            {
                state[pos] = 2;
                return;
            }

            pos = (pos + 1) & mask;
        }
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;

    cin >> N >> Q;

    const int maximumEdges = N + Q + 5;

    vector<Edge> edges(maximumEdges);

    DSU dsu(N);

    FastHashMap edgeMap(N + Q + 10);

    ll totalWeight = 0;
    int extraEdge = 0;

    for (int id = 1; id <= N; ++id)
    {
        int u, v, w;

        cin >> u >> v >> w;

        edges[id].u = u;
        edges[id].v = v;
        edges[id].weight = w;
        edges[id].lctNode = N + id;
        edges[id].treeEdge = false;

        totalWeight += w;

        if (dsu.unite(u, v))
            edges[id].treeEdge = true;
        else
            extraEdge = id;

        edgeMap.insert(edgeKey(u, v), id);
    }

    int maximumLctNodes =
        N + (N + Q) + 10;

    LinkCutTree lct(maximumLctNodes);

    for (int i = 1; i <= N; ++i)
        lct.setValue(i, NEG_INF);

    for (int id = 1; id <= N; ++id)
    {
        lct.setValue(
            edges[id].lctNode,
            edges[id].weight
        );

        if (edges[id].treeEdge)
        {
            lct.link(
                edges[id].u,
                edges[id].lctNode
            );

            lct.link(
                edges[id].lctNode,
                edges[id].v
            );
        }
    }

    int edgeCount = N;
    ll answer = 0;

    for (int query = 0; query < Q; ++query)
    {
        ll x1, x2, x3, x4, x5;

        cin >> x1
            >> x2
            >> x3
            >> x4
            >> x5;

        ll shift = answer % 100;

        int a = int(x1 + shift);
        int b = int(x2 + shift);

        int u = int(x3 + shift);
        int v = int(x4 + shift);

        int w = int(x5 + shift);

        uint64_t deleteKey =
            edgeKey(a, b);

        int deletedId =
            edgeMap.get(deleteKey);

        edgeMap.erase(deleteKey);

        totalWeight -=
            edges[deletedId].weight;

        if (deletedId == extraEdge)
        {
            extraEdge = 0;
        }
        else
        {
            Edge &deleted =
                edges[deletedId];

            lct.cut(
                deleted.u,
                deleted.lctNode
            );

            lct.cut(
                deleted.lctNode,
                deleted.v
            );

            deleted.treeEdge = false;

            Edge &extra =
                edges[extraEdge];

            if (!lct.connected(
                    extra.u,
                    extra.v))
            {
                lct.link(
                    extra.u,
                    extra.lctNode
                );

                lct.link(
                    extra.lctNode,
                    extra.v
                );

                extra.treeEdge = true;

                extraEdge = 0;
            }
        }

        ++edgeCount;

        int newId = edgeCount;

        edges[newId].u = u;
        edges[newId].v = v;
        edges[newId].weight = w;

        edges[newId].lctNode =
            N + newId;

        edges[newId].treeEdge = false;

        lct.setValue(
            edges[newId].lctNode,
            w
        );

        totalWeight += w;

        edgeMap.insert(
            edgeKey(u, v),
            newId
        );

        if (extraEdge == 0)
        {
            extraEdge = newId;
        }
        else
        {
            lct.link(
                u,
                edges[newId].lctNode
            );

            lct.link(
                edges[newId].lctNode,
                v
            );

            edges[newId].treeEdge = true;
        }

        Edge &extra =
            edges[extraEdge];

        int maximumTreeEdge =
            lct.queryMax(
                extra.u,
                extra.v
            );

        int maximumCycleEdge =
            max(
                extra.weight,
                maximumTreeEdge
            );

        answer =
            totalWeight
            - maximumCycleEdge;

        cout << answer << '
';
    }

    return 0;
}
```

---

# Time Complexity

Let:

```text
N = number of vertices
Q = number of queries
```

Initial DSU processing:

```text
O(N α(N))
```

Initial Link-Cut Tree construction:

```text
O(N log N)
```

Each query uses only a constant number of:

```text
cut
link
connectivity checks
path maximum queries
```

Each Link-Cut Tree operation is amortized:

```text
O(log N)
```

Therefore each query is:

```text
O(log N)
```

and total time complexity is:

```text
O((N + Q) log N)
```

amortized.

---

# Space Complexity

We store:

```text
edge data              O(N + Q)
Link-Cut Tree nodes    O(N + Q)
hash map               O(N + Q)
DSU                    O(N)
```

Therefore:

```text
Space Complexity = O(N + Q)
```

---

# Why Kruskal Per Query Is Too Slow

Rebuilding the MST using Kruskal after each query would require approximately:

```text
O(N log N)
```

per query.

For `Q` queries:

```text
O(Q * N log N)
```

With `N, Q <= 300000`, this is infeasible.

The key optimization comes from the fact that the graph is always unicyclic.

---

# Key Interview Insight

```text
Connected graph has N vertices and N edges
                  |
                  v
          Exactly one cycle
                  |
                  v
 Keep N-1 edges as a spanning tree
      + one extra edge
                  |
                  v
MST = total weight - largest edge on cycle
                  |
                  v
Need link / cut / connectivity / path maximum
                  |
                  v
            Link-Cut Tree
```

The central formula is:

```text
MST =
totalWeight
-
max(
    extraEdgeWeight,
    maximumEdgeOnTreePath(extra.u, extra.v)
)
```

That is the core of the `O((N + Q) log N)` solution.
