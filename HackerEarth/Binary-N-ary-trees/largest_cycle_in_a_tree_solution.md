# Largest Cycle in a Tree --- HackerEarth

## Problem

You are given a tree containing `N` nodes and `N - 1` edges.

You are allowed to add one new edge between two nodes. Since the
original graph is a tree, there is exactly one path between any two
nodes.

Adding an edge between nodes `A` and `B` therefore creates a cycle
consisting of:

``` text
the existing path from A to B
+
the newly added edge A-B
```

The objective is to choose the two nodes so that the resulting cycle is
as large as possible.

------------------------------------------------------------------------

## Main Observation

Suppose the distance between nodes `A` and `B` in the original tree is:

``` text
distance(A, B)
```

After adding a new edge directly between them, the cycle contains:

``` text
distance(A, B) + 1
```

edges.

Therefore, maximizing the cycle means maximizing:

``` text
distance(A, B)
```

So the actual problem is:

> Find two nodes having the maximum distance from each other in the
> tree.

This is exactly the **diameter of a tree**.

------------------------------------------------------------------------

## Example

Consider:

``` text
          1
         / \
        2   3
       /     \
      4       5
               \
                6
```

The longest path is:

``` text
4 -> 2 -> 1 -> 3 -> 5 -> 6
```

Therefore, the diameter endpoints are:

``` text
4 and 6
```

If we add an edge:

``` text
4 -------- 6
```

we create:

``` text
4 -> 2 -> 1 -> 3 -> 5 -> 6 -> 4
```

which is the largest possible cycle.

------------------------------------------------------------------------

## How to Find the Tree Diameter

A standard property of trees allows us to find the diameter using two
BFS/DFS traversals.

### Step 1

Start BFS from any node, for example:

``` text
1
```

Find the node farthest from `1`.

Call this node:

``` text
A
```

`A` will be one endpoint of some diameter.

### Step 2

Run BFS again, this time starting from `A`.

Find the node farthest from `A`.

Call this node:

``` text
B
```

Then:

``` text
A <---- longest path ----> B
```

is a diameter of the tree.

Therefore, adding an edge between:

``` text
A and B
```

produces the maximum possible cycle.

------------------------------------------------------------------------

## Why Two BFS Traversals Work

Starting from an arbitrary node does not necessarily give us the
diameter immediately.

However, in a tree, a farthest node reached from an arbitrary starting
node can be chosen as an endpoint of a diameter.

So:

``` text
Arbitrary node
      |
      | BFS
      v
Farthest node A
      |
      | BFS
      v
Farthest node B
```

gives the diameter endpoints:

``` text
A ---------------- B
```

------------------------------------------------------------------------

## C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> graph;

// Returns:
// {farthest node, distance to that node}
pair<int, int> bfs(int start)
{
    int n = graph.size() - 1;

    vector<int> dist(n + 1, -1);

    queue<int> q;

    q.push(start);
    dist[start] = 0;

    int farthest = start;

    while (!q.empty())
    {
        int node = q.front();
        q.pop();

        for (int child : graph[node])
        {
            if (dist[child] == -1)
            {
                dist[child] = dist[node] + 1;

                q.push(child);

                if (dist[child] > dist[farthest])
                {
                    farthest = child;
                }
            }
        }
    }

    return {farthest, dist[farthest]};
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    graph.resize(n + 1);

    // A tree with N nodes contains N - 1 edges.
    for (int i = 0; i < n - 1; i++)
    {
        int u, v;
        cin >> u >> v;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    // First BFS:
    // Find one endpoint of the diameter.
    auto [A, distanceFromStart] = bfs(1);

    // Second BFS:
    // Find the opposite endpoint.
    auto [B, diameter] = bfs(A);

    // Adding an edge between A and B creates
    // the maximum possible cycle.
    cout << A << " " << B << '\n';

    return 0;
}
```

------------------------------------------------------------------------

## Dry Run

Consider:

``` text
          1
         / \
        2   3
       /     \
      4       5
               \
                6
```

### First BFS

Start from:

``` text
1
```

Distances:

``` text
1 -> 0
2 -> 1
3 -> 1
4 -> 2
5 -> 2
6 -> 3
```

The farthest node is:

``` text
A = 6
```

### Second BFS

Now start from `6`.

Distances include:

``` text
6 -> 0
5 -> 1
3 -> 2
1 -> 3
2 -> 4
4 -> 5
```

The farthest node is:

``` text
B = 4
```

Therefore the diameter is:

``` text
6 -> 5 -> 3 -> 1 -> 2 -> 4
```

and the answer can be:

``` text
6 4
```

Adding:

``` text
6 ----- 4
```

creates the largest cycle.

------------------------------------------------------------------------

## Complexity

Each BFS visits every node and every edge once.

For a tree:

``` text
Vertices = N
Edges    = N - 1
```

Therefore one BFS takes:

``` text
O(N)
```

We perform two BFS traversals:

``` text
O(N) + O(N) = O(N)
```

### Time Complexity

``` text
O(N)
```

### Space Complexity

The adjacency list, distance array, and BFS queue require:

``` text
O(N)
```

memory.

------------------------------------------------------------------------

## BFS vs DFS

The same technique can be implemented using DFS.

However, iterative BFS has an advantage for very deep trees: it avoids
recursion-stack overflow.

For example, consider a tree shaped like:

``` text
1 - 2 - 3 - 4 - 5 - ... - N
```

A recursive DFS may require recursion depth `N`.

BFS avoids that problem, so it is a safe choice for large constraints.

------------------------------------------------------------------------

## Interview Thought Process

A good way to derive the solution is:

``` text
We can add one edge
        |
        v
Adding an edge creates one cycle
        |
        v
Cycle = existing path + new edge
        |
        v
New edge always contributes exactly 1
        |
        v
Therefore maximize existing path length
        |
        v
Longest path in a tree
        |
        v
TREE DIAMETER
        |
        v
Find diameter with two BFS traversals
```

The main insight is:

> **The largest cycle is obtained by connecting the two endpoints of a
> tree diameter.**

Once this transformation is recognized, the problem becomes a standard
`O(N)` tree-diameter problem.
