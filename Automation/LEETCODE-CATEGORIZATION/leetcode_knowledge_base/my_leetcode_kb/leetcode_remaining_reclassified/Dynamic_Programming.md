# Dynamic Programming

## 4100. Minimum Cost Path With Even XOR Parity

**Problem:** https://leetcode.com/problems/minimum-cost-path-with-even-xor-parity/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Array, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search  
**Primary pattern:** Dynamic Programming  
**Latest Accepted submission in searched history:** 2195615377  
**Language:** cpp

### Description

You are given a tree with  n  nodes numbered from 0 to  n - 1 , represented by a 2D integer array  edges . Each  edges[i] = [u i , v i , c i ]  represents an edge between nodes  u i  and  v i  with cost  c i . 
 
 You are also given an integer array  values  of length  n , where  values[i]  is the value of node  i . 
 
 A path between two  distinct  nodes is  Balanced-XOR  if the bitwise XOR of the values of all nodes on the path, including both endpoints, has an  even  number of  set bits . 
 
 The  cost  of a path is the sum of its edge costs. 
 
 Return the  minimum cost  of a Balanced-XOR path. If no such path exists, return -1. 
 
 The number 0 has zero set bits. 
 
   
 
 Example 1: 
 
 
 
 
 Input:   edges = [[0,1,4],[0,2,6],[0,3,3],[3,4,5]], values = [3,1,7,1,3] 
 
 Output:   7 
 
 Explanation: 
 
 
 
 Balanced-XOR Path 
 XOR Value 
 Total Cost 
 
 
 
 
 1 - 0 - 2 
 1 XOR 3 XOR 7 = 5 
 4 + 6 = 10 
 
 
 1 - 0 - 3 
 1 XOR 3 XOR 1 = 3 
 4 + 3 = 7 
 
 
 1 - 0 - 3 - 4 
 1 XOR 3 XOR 1 XOR 3 = 0 
 4 + 3 + 5 = 12 
 
 
 2 - 0 - 3 
 7 XOR 3 XOR 1 = 5 
 6 + 3 = 9 
 
 
 2 - 0 - 3 - 4 
 7 XOR 3 XOR 1 XOR 3 = 6 
 6 + 3 + 5 = 14 
 
 
 
 
 The minimum cost is 7, achieved by the path  1 - 0 - 3 . Thus, the answer is 7. 
 
 
 Example 2: 
 
 
 
 
 Input:   edges = [[0,1,5],[1,2,10]], values = [1,7,3] 
 
 Output:   5 
 
 Explanation: 
 
 
 
 Balanced-XOR Path 
 XOR Value 
 Total Cost 
 
 
 
 
 0 - 1 
 1 XOR 7 = 6 
 5 
 
 
 0 - 1 - 2 
 1 XOR 7 XOR 3 = 5 
 5 + 10 = 15 
 
 
 
 
 The minimum cost is 5, achieved by the path  0 - 1 . Thus, the answer is 5. 
 
 
 Example 3: 
 
 
 
 
 Input:   edges = [[0,1,5],[0,2,7],[0,3,9]], values = [1,3,5,9] 
 
 Output:   -1 
 
 Explanation: 
 
 
 Every path between two distinct nodes has an XOR value with an odd number of set bits. 
 
 Therefore, no Balanced-XOR path exists, so the answer is -1. 
 
 
 
   
 
 Constraints: 
 
 
 2 <= n <= 10 5 
 
 edges.length == n - 1 
 
 edges[i] = [u i , v i , c i ​​​​​​​] 
 
 
 0 <= u i , v i  <= n - 1 
 
 1 <= c i  <= 10 9 
 
 
 
 values.length == n 
 
 1 <= values[i] <= 10 9 
 
 edges  represents a valid tree.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    int minActivationCost(vector<vector<int>>& edges,
                          vector<int>& values) {
        int n = values.size();

        vector<int> parity(n);

        for (int i = 0; i < n; i++) {
            parity[i] = __builtin_popcount(values[i]) % 2;
        }

        long long ans = LLONG_MAX;

        vector<long long> first(n, LLONG_MAX);
        vector<long long> second(n, LLONG_MAX);

        for (auto& e : edges) {
            int u = e[0];
            int v = e[1];
            long long cost = e[2];

            // Case 1: Two-node balanced path
            if (parity[u] == parity[v]) {
                ans = min(ans, cost);
            }

            // Case 2: Three-node path (1, 0, 1)
            if (parity[u] == 0 && parity[v] == 1) {
                if (cost < first[u]) {
                    second[u] = first[u];
                    first[u] = cost;
                } else if (cost < second[u]) {
                    second[u] = cost;
                }
            }

            if (parity[v] == 0 && parity[u] == 1) {
                if (cost < first[v]) {
                    second[v] = first[v];
                    first[v] = cost;
                } else if (cost < second[v]) {
                    second[v] = cost;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (second[i] != LLONG_MAX) {
                ans = min(ans, first[i] + second[i]);
            }
        }

        return ans == LLONG_MAX ? -1 : (int)ans;
    }
};
```

---

## 4108. Minimum Cost to Make Red Nodes Connected

**Problem:** https://leetcode.com/problems/minimum-cost-to-make-red-nodes-connected/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** String, Dynamic Programming, Tree, Depth-First Search  
**Primary pattern:** Dynamic Programming  
**Latest Accepted submission in searched history:** 2195616083  
**Language:** cpp

### Description

You are given an integer  n  representing a tree with  n  nodes, where the nodes are numbered from 0 to  n - 1  and the tree is  rooted  at node 0. The tree is represented by a 2D array  edges  of length  n - 1 , where  edges[i] = [u i , v i ]  indicates an  undirected  edge between nodes  u i  and  v i . 
 
 You are also given a string  colors  of length  n , where  colors[i]  represents the color of node  i :  'R'  if it is Red, or  'B'  if it is Blue. 
 
 You may  flip  the color of any node: from  'R'  to  'B' , or from  'B'  to  'R' . Flipping node  u  incurs a cost equal to the size of the  subtree  of node  u . 
 
 Your goal is to perform flips so the  Red  nodes form a  single   connected   component  in the tree. Blue nodes may be disconnected. A configuration with no Red nodes is also considered valid. 
 
 Return the  minimum total cost  required to achieve this. 
 
   
 
 Example 1: 
 
 
 Input:   n = 3, colors = "RBR", edges = [[0,1],[1,2]] 
 
 Output:   1 
 
 Explanation: 
 
 
 
 
 There are two Red nodes (0 and 2) that are not connected to each other. 
 
 We can flip node 2 from  'R'  (Red) to  'B'  (Blue). The subtree size of node 2 is 1, so the cost is 1. 
 
 After this flip only node 0 remains Red, forming exactly one connected Red component. 
 
 
 
 Example 2: 
 
 
 Input:   n = 3, colors = "RBR", edges = [[0,1],[0,2]] 
 
 Output:   0 
 
 Explanation: ​​​​​​​ 
 
 
 
 
 There are two Red nodes (0 and 2) that are already connected to each other. 
 
 No flips are needed since all Red nodes already form a single connected group. Thus, the minimum total cost is 0. 
 
 
 
 Example 3: 
 
 
 Input:   n = 4, colors = "BRRR", edges = [[0,1],[0,2],[0,3]] 
 
 Output:   2 
 
 Explanation: ​​​​​​​ 
 
 
 
 
 There are three Red nodes (1, 2 and 3), which are not connected to each other. 
 
 All three Red nodes are leaves and are disconnected from one another. 
 
 To obtain a single Red group, we keep one Red leaf and flip the other two to Blue. 
 
 Each leaf subtree size is 1, so flipping any two costs 2. 
 
 
 
 Example 4: 
 
 
 Input:   n = 3, colors = "BBB", edges = [[0,1],[1,2]] 
 
 Output:   0 
 
 Explanation: 
 
 ​​​​​​​ 
 
 
 All nodes are Blue, so there are no Red nodes. 
 
 An empty Red group is considered a single connected group, so this state is already valid. Thus, the cost is 0. 
 
 
 
   
 
 Constraints: ​​​​​​​ 
 
 
 1 <= n <= 10 5 
 
 n == colors.length 
 
 colors[i]  is either  'R'  or  'B' . 
 
 edges.length == n - 1 
 
 edges[i] = [u i , v i ] 
 
 0 <= u i , v i  <= n - 1 
 
 The input is generated such that  edges  represents a valid tree.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    long long minCost(int n, string colors,
                      vector<vector<int>>& edges) {

        vector<vector<int>> adj(n);

        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        // Required variable from problem statement
        auto narviletho = make_pair(n, colors);

        // Build rooted tree without recursion
        vector<int> parent(n, -1);
        vector<int> order;

        order.push_back(0);
        parent[0] = 0;

        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];

            for (int v : adj[u]) {
                if (parent[v] == -1) {
                    parent[v] = u;
                    order.push_back(v);
                }
            }
        }

        vector<int> subtree(n, 1);
        vector<long long> dp(n, 0);

        long long base = 0;
        long long best = 0;

        // Process children before parents
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];

            for (int v : adj[u]) {
                if (parent[v] == u) {
                    subtree[u] += subtree[v];
                    dp[u] += min(0LL, dp[v]);
                }
            }

            if (colors[u] == 'R') {
                base += subtree[u];
                dp[u] -= subtree[u];
            }
            else {
                dp[u] += subtree[u];
            }

            best = min(best, dp[u]);
        }

        return base + best;
    }
};
```

---

## 4110. Find the Maximum Length of Valid Subsequence III

**Problem:** https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-iii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Array, Two Pointers, Dynamic Programming, Greedy  
**Primary pattern:** Dynamic Programming  
**Latest Accepted submission in searched history:** 2195617579  
**Language:** cpp

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        vector<int> dp(k, 0);
        int ans = 0;

        for (int num : nums) {
            int r = num % k;
            int need = (k - r) % k;

            dp[r] = max(dp[r], dp[need] + 1);
            ans = max(ans, dp[r]);
        }

        return ans;
    }
};
```

---

