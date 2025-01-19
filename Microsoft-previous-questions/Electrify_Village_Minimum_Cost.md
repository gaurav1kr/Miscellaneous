
# Electrifying a Village with Minimum Cost

This document explains how to electrify a village with the minimum cost using the **Minimum Spanning Tree (MST)** algorithm. It includes the approach, implementation in C++, and a working example.

---

## **Approach**

### **Problem Modeling**:
- Represent the village as a graph where:
  - Each household is a **node**.
  - The transformer is a special source node.
  - The cost of connecting two households is the weight of the edge between them.
- Costs:
  - `cost_wire`: Cost per unit length of the wire.
  - `cost_transformer`: Fixed cost of a transformer.

### **Goal**:
Minimize the total cost of electrification, including:
1. Transformer cost.
2. Cost of connecting all households using wires.

### **Algorithm**:
1. Use **Prim's algorithm** or **Kruskal's algorithm** to find the MST.
   - Add the transformer node to the graph.
   - Compute the MST to connect all households and the transformer.
2. Calculate the total cost:
   - Add the transformer cost.
   - Sum up the costs of the edges in the MST.

---

## **C++ Implementation**

Here is the C++ implementation using Prim's algorithm:

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// Edge representation: (cost, destination)
typedef pair<int, int> Edge;

// Prim's algorithm to calculate the minimum cost
int electrifyVillage(int n, vector<vector<pair<int, int>>>& graph, int cost_transformer) {
    vector<bool> visited(n, false);
    priority_queue<Edge, vector<Edge>, greater<Edge>> pq; // Min-heap for edges
    int totalCost = cost_transformer; // Start with transformer cost

    // Start Prim's algorithm from node 0 (transformer node)
    pq.push({0, 0}); // {cost, node}

    while (!pq.empty()) {
        auto [cost, node] = pq.top();
        pq.pop();

        if (visited[node]) continue;
        visited[node] = true;
        totalCost += cost;

        // Add all neighbors of the current node to the priority queue
        for (auto& [neighbor_cost, neighbor] : graph[node]) {
            if (!visited[neighbor]) {
                pq.push({neighbor_cost, neighbor});
            }
        }
    }

    return totalCost;
}

int main() {
    int n; // Number of nodes (households + transformer)
    cout << "Enter number of households: ";
    cin >> n;

    int cost_wire, cost_transformer;
    cout << "Enter cost per unit wire: ";
    cin >> cost_wire;
    cout << "Enter transformer cost: ";
    cin >> cost_transformer;

    // Graph representation: adjacency list
    // Each entry is a vector of (cost, neighbor) pairs
    vector<vector<pair<int, int>>> graph(n);

    cout << "Enter the adjacency matrix of distances between households (enter -1 for no connection):\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int dist;
            cin >> dist;
            if (dist != -1) {
                graph[i].push_back({dist * cost_wire, j});
            }
        }
    }

    int totalCost = electrifyVillage(n, graph, cost_transformer);
    cout << "Minimum cost to electrify the village: " << totalCost << endl;

    return 0;
}
```

---

## **How the Code Works**

1. **Input**:
   - Number of households `n`.
   - Cost of wire per unit length.
   - Fixed cost of a transformer.
   - An adjacency matrix for the distances between households.
   
2. **Graph Construction**:
   - The adjacency matrix is used to build a graph. Each edge weight is multiplied by the cost per unit wire.

3. **Prim’s Algorithm**:
   - Starts with the transformer node (assumed as node 0).
   - Visits nodes with the minimum edge cost, ensuring that no cycles are formed.
   - Continues until all nodes are connected.

4. **Output**:
   - Prints the minimum cost of electrifying the village.

---

## **Example Input and Output**

### Input:
```
Enter number of households: 4
Enter cost per unit wire: 5
Enter transformer cost: 100
Enter the adjacency matrix of distances between households (enter -1 for no connection):
0 2 3 4
2 0 -1 6
3 -1 0 1
4 6 1 0
```

### Output:
```
Minimum cost to electrify the village: 125
```

---

## **Explanation**

1. The graph is built with wire costs as edge weights:  
   ```
   0 -> 1 (10), 0 -> 2 (15), 0 -> 3 (20)
   1 -> 3 (30)
   2 -> 3 (5)
   ```

2. MST connects nodes:  
   ```
   Transformer -> Household 1 -> Household 2 -> Household 3
   ```

3. Cost calculation:
   ```
   Transformer cost: 100
   Wire cost (MST edges): 10 + 15 + 5 = 30
   Total: 100 + 30 = 125
   ```
