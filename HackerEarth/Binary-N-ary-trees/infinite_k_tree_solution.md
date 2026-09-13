# Infinite K-Tree --- HackerEarth

## Problem

We are given an **infinite K-ary tree**.

For a node `X`, its children are:

``` text
K*X, K*X + 1, ..., K*X + (K-1)
```

Therefore, for any node `X > 1`, its parent can be found directly as:

``` text
parent(X) = X / K
```

using integer division.

Every edge initially has weight `1`.

There are two types of queries:

1.  Find the total weighted distance between two nodes `u` and `v`.
2.  Increase the weight of every edge on the path between `u` and `v` by
    `w`.

Because the tree is infinite, explicitly constructing it is impossible.

------------------------------------------------------------------------

## Key Observation 1 --- The Tree Is Implicit

We never need to construct the tree.

For any node:

``` cpp
parent = node / K;
```

So we can always move upward toward the root.

For example, if `K = 2`:

``` text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

For node `5`:

``` text
5 / 2 = 2
2 / 2 = 1
```

So its path toward the root is:

``` text
5 -> 2 -> 1
```

------------------------------------------------------------------------

## Key Observation 2 --- Represent an Edge by Its Child

Consider the edge:

``` text
x -> parent(x)
```

Since:

``` text
parent(x) = x / K
```

the edge is uniquely identified by `x`.

Therefore, instead of storing:

``` text
(child, parent)
```

we can simply use:

``` text
child
```

as the key.

For example:

``` text
extra[10]
```

represents the additional weight added to:

``` text
10 -> 10/K
```

------------------------------------------------------------------------

## Key Observation 3 --- Store Only Modified Edges

Initially every edge has weight:

``` text
1
```

There are infinitely many edges, so we obviously cannot store them.

Instead, maintain:

``` cpp
unordered_map<long long, long long> extra;
```

where:

``` text
extra[x]
```

contains only the additional weight added to the edge:

``` text
x -> x/K
```

Thus:

``` text
actual edge weight = 1 + extra[x]
```

If `x` is not present in the map:

``` text
edge weight = 1
```

This keeps memory proportional only to edges affected by update queries.

------------------------------------------------------------------------

## Finding the LCA

We need to find the path between `u` and `v`.

A standard way is:

1.  Find the depth of `u`.
2.  Find the depth of `v`.
3.  Move the deeper node upward until both nodes are at the same depth.
4.  Move both upward simultaneously until:

``` text
u == v
```

That node is their **Lowest Common Ancestor (LCA)**.

------------------------------------------------------------------------

## Calculating Depth

Because we can find a parent with:

``` text
x = x / K
```

we can calculate depth as:

``` cpp
long long depthOf(long long x, long long K)
{
    long long depth = 0;

    while (x > 1)
    {
        x /= K;
        depth++;
    }

    return depth;
}
```

------------------------------------------------------------------------

## Query Type 1 --- Find Distance

Suppose we want the weighted distance between:

``` text
u and v
```

First bring them to the same depth.

If:

``` text
depth(u) > depth(v)
```

then repeatedly:

``` text
answer += weight(u -> parent(u))
u = parent(u)
```

Do the equivalent operation for `v` if it is deeper.

Once they are at the same depth, move both upward:

``` text
while (u != v)
```

For every step:

``` text
answer += edgeWeight(u)
answer += edgeWeight(v)

u /= K
v /= K
```

When they become equal, we have reached their LCA.

------------------------------------------------------------------------

## Query Type 2 --- Increase Path Weight

For an update:

``` text
increase every edge between u and v by w
```

we perform exactly the same upward traversal.

Instead of reading edge weights, update:

``` cpp
extra[u] += w;
```

or:

``` cpp
extra[v] += w;
```

for every traversed edge.

Again, stop once:

``` text
u == v
```

because the common node is the LCA and there is no edge between the LCA
and itself.

------------------------------------------------------------------------

## C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using int64 = long long;

// extra[x] = additional weight on edge (x -> x/K)
//
// Every edge initially has weight 1.
// Therefore:
//
// actual weight = 1 + extra[x]
unordered_map<int64, int64> extra;


int64 depthOf(int64 x, int64 K)
{
    int64 depth = 0;

    while (x > 1)
    {
        x /= K;
        depth++;
    }

    return depth;
}


int64 edgeWeight(int64 x)
{
    auto it = extra.find(x);

    if (it == extra.end())
        return 1;

    return 1 + it->second;
}


int64 getDistance(int64 u, int64 v, int64 K)
{
    int64 du = depthOf(u, K);
    int64 dv = depthOf(v, K);

    int64 answer = 0;

    // Bring u and v to the same depth.

    while (du > dv)
    {
        answer += edgeWeight(u);

        u /= K;
        du--;
    }

    while (dv > du)
    {
        answer += edgeWeight(v);

        v /= K;
        dv--;
    }

    // Both nodes now have the same depth.
    // Move upward until they meet at their LCA.

    while (u != v)
    {
        answer += edgeWeight(u);
        answer += edgeWeight(v);

        u /= K;
        v /= K;
    }

    return answer;
}


void increasePath(int64 u,
                  int64 v,
                  int64 w,
                  int64 K)
{
    int64 du = depthOf(u, K);
    int64 dv = depthOf(v, K);

    // Bring both nodes to the same depth.

    while (du > dv)
    {
        extra[u] += w;

        u /= K;
        du--;
    }

    while (dv > du)
    {
        extra[v] += w;

        v /= K;
        dv--;
    }

    // Move both nodes upward until their LCA.

    while (u != v)
    {
        extra[u] += w;
        extra[v] += w;

        u /= K;
        v /= K;
    }
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int64 K, Q;
    cin >> K >> Q;

    while (Q--)
    {
        int type;
        cin >> type;

        if (type == 1)
        {
            int64 u, v;
            cin >> u >> v;

            cout << getDistance(u, v, K)
                 << '\n';
        }
        else
        {
            int64 u, v, w;
            cin >> u >> v >> w;

            increasePath(u, v, w, K);
        }
    }

    return 0;
}
```

------------------------------------------------------------------------

## Example of an Update

Suppose the path between two nodes contains:

``` text
8 -> 4 -> 2 -> 1
```

and an update adds:

``` text
w = 5
```

to the relevant edges.

Instead of modifying a tree, we store:

``` text
extra[8] += 5
extra[4] += 5
extra[2] += 5
```

Now the corresponding edge weights are:

``` text
8 -> 4 : 1 + 5 = 6
4 -> 2 : 1 + 5 = 6
2 -> 1 : 1 + 5 = 6
```

An untouched edge still has weight `1`.

------------------------------------------------------------------------

## Why We Do Not Need to Build the Tree

At first glance, the problem looks difficult because the tree is
infinite.

But the infinite size is actually a clue.

We only need to move **upward**, and the parent is mathematically known:

``` text
parent(x) = x / K
```

Therefore:

``` text
No adjacency list
No TreeNode objects
No BFS
No complete tree construction
```

are required.

------------------------------------------------------------------------

## Complexity

Let:

``` text
M = max(u, v)
```

The depth of a node is approximately:

``` text
O(log_K M)
```

Therefore each query takes:

``` text
O(log_K M)
```

expected time apart from the expected `O(1)` hash-map operations.

### Memory

We store only edges that have received additional weight:

``` text
O(number of modified edges)
```

rather than storing the infinite tree.

------------------------------------------------------------------------

## Interview Approach

A good way to explain the reasoning is:

``` text
Tree is infinite
      |
      v
Cannot construct the tree
      |
      v
Look for mathematical parent relationship
      |
      v
parent(x) = x / K
      |
      v
Path queries can be solved by moving upward
      |
      v
Bring nodes to same depth
      |
      v
Move both toward LCA
      |
      v
Store only modified edge weights
```

The two most important insights are:

1.  **The infinite tree is implicit; `x / K` gives the parent.**
2.  **An edge can be uniquely represented by its child node, so only
    modified edges need to be stored.**

These observations turn an apparently infinite-tree problem into a small
`O(log_K M)` traversal per query.
