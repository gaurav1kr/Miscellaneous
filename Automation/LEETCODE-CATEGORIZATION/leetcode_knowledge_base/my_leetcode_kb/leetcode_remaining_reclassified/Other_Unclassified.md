# Other Unclassified

## 4097. Minimum Value of Merged Integers

**Problem:** https://leetcode.com/problems/minimum-value-of-merged-integers/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195614975  
**Language:** cpp

### Description

You are given an integer array  nums  of even length  n . 
 
 You have to  merge  the elements of  nums  in pairs by merging  nums[0]  with  nums[1] ,  nums[2]  with  nums[3] , and so on, until  nums[n - 2]  with  nums[n - 1] . 
 
 Return the  minimum  value among all the resulting merged integers. 
 
 To  merge  two integers, concatenate all the decimal digits of the first integer followed by all the decimal digits of the second integer. 
 
   
 
 Example 1: 
 
 
 Input:   nums = [23,55,42,21] 
 
 Output:   2355 
 
 Explanation: 
 
 
 Merging  nums[0] = 23  and  nums[1] = 55  gives 2355. 
 
 Merging  nums[2] = 42  and  nums[3] = 21  gives 4221. 
 
 The minimum value among the merged numbers is  min(2355, 4221) = 2355 . 
 
 
 
 Example 2: 
 
 
 Input:   nums = [34,7,11,11] 
 
 Output:   347 
 
 Explanation: 
 
 
 Merging  nums[0] = 34  and  nums[1] = 7  gives 347. 
 
 Merging  nums[2] = 11  and  nums[3] = 11  gives 1111. 
 
 The minimum value among the merged numbers is  min(347, 1111) = 347 . 
 
 
 
 Example 3: 
 
 
 Input:   nums = [9,20] 
 
 Output:   920 
 
 Explanation: 
 
 
 Merging  nums[0] = 9  and  nums[1] = 20  gives 920. 
 
 There is only one merged number, so the minimum value is 920. 
 
 
 
   
 
 Constraints: 
 
 
 2 <= n == nums.length <= 100 
 
 n  is even 
 
 1 <= nums[i] <= 1000

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    int minMergedInteger(vector<int>& nums) {
        int ans = INT_MAX;

        for (int i = 0; i < nums.size(); i += 2) {
            string merged = to_string(nums[i]) +
                            to_string(nums[i + 1]);

            ans = min(ans, stoi(merged));
        }

        return ans;
    }
};
```

---

## 4111. Count Consistent Subarrays I

**Problem:** https://leetcode.com/problems/count-consistent-subarrays-i/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2197466125  
**Language:** cpp

### Description

You are given an integer array  nums . 
 
 A  subarray  is called  consistent  if the  bitwise AND  of all its elements is equal to the  minimum  value of the subarray. 
 
 Return the number of  consistent subarrays  in  nums . 
 
   
 
 Example 1: 
 
 
 Input:   nums = [5,3,1,2] 
 
 Output:   6 
 
 Explanation: 
 
 The following subarrays are consistent: 
 
 
 
 Subarray 
 Values 
 Bitwise AND 
 Minimum Value 
 
 
 nums[0..0] 
 [5] 
 5 
 5 
 
 
 nums[1..1] 
 [3] 
 3 
 3 
 
 
 nums[2..2] 
 [1] 
 1 
 1 
 
 
 nums[3..3] 
 [2] 
 2 
 2 
 
 
 nums[1..2] 
 [3, 1] 
 3 AND 1 = 1 
 1 
 
 
 nums[0..2] 
 [5, 3, 1] 
 5 AND 3 AND 1 = 1 
 1 
 
 
 
 
 Therefore, the number of consistent subarrays is 6. 
 
 
 Example 2: 
 
 
 Input:   nums = [1,1,1] 
 
 Output:   6 
 
 Explanation: 
 
 For every subarray, both the bitwise AND and the minimum value are equal to 1. Therefore, the answer is 6. 
 
 
 Example 3: 
 
 
 Input:   nums = [0] 
 
 Output:   1 
 
 Explanation: 
 
 The only subarray is  [0] , whose bitwise AND and minimum value are both 0. Therefore, the answer is 1. 
 
 
   
 
 Constraints: 
 
 
 1 <= nums.length <= 100 
 
 0 <= nums[i] <= 100

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    int countConsistent(vector<int>& nums) {
        int n = nums.size();
        int count = 0;

        for (int i = 0; i < n; i++) {
            int mn = nums[i];
            int bitAnd = nums[i];

            for (int j = i; j < n; j++) {
                mn = min(mn, nums[j]);
                bitAnd &= nums[j];

                if (mn == bitAnd)
                    count++;
            }
        }

        return count;
    }
};
```

---

## 4112. Maximize Score After Zeroing Subtrees

**Problem:** https://leetcode.com/problems/maximize-score-after-zeroing-subtrees/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2197467081  
**Language:** cpp

### Description

You are given an integer array  parent  of length  n  representing a rooted tree with nodes labeled from 0 to  n - 1 , where  parent[i]  denotes the parent of node  i . The tree is rooted at node 0, so  parent[0] = -1 . 
 
 You are also given two integer arrays  op  and  score , both of length  n , where  op[i]  determines the operation allowed at node  i , and  score[i]  represents its score. 
 
 You need to process each  non- leaf  node  i  according to the following rules: 
 
 
 If  op[i] = 0 , you can choose  at most  one child of node  i  and set the scores of all nodes in that child's  subtree  to 0. 
 
 If  op[i] = 1 , you must choose  exactly  one child of node  i  and set the scores of all nodes in that child's subtree to 0. 
 
 
 Each non-leaf node must be processed exactly once. You may process the nodes in any order. 
 
 Return the  maximum possible sum  of the scores after performing the operations. 
 
   
 
 Example 1: 
 
 
 ​​​​​​​ 
 
 Input:   parent = [-1,0,0,0,1,2,3,3], op = [1,1,0,0,1,1,0,1], score = [5,6,1,2,3,2,3,-3] 
 
 Output:   16 
 
 Explanation: 
 
 One optimal way is to process the nodes in the following order: 
 
 
 Nodes 4, 5, 6, and 7 :  They are leaf nodes, so no operations are performed on them. 
 
 Node 1 :  Since  op[1] = 1 , we must select one of its children. Choose node 4, setting the scores of all nodes in its subtree (node 4) to 0. 
 
 Node 2: Since  op[2] = 0 , we may choose a child or do nothing. For this node, we do nothing. 
 
 Node 3: Since  op[3] = 0 , we may choose a child or do nothing. Choose node 7, setting the scores of all nodes in its subtree (node 7) to 0. 
 
 Node 0: Since  op[0] = 1 , we must select one of its children. Choose node 2, setting the scores of all nodes in its subtree (nodes 2 and 5) to 0. 
 
 
 After performing these operations, the scores are  [5, 6, 0, 2, 0, 0, 3, 0] , giving a total sum of 16. 
 
 No valid sequence of operations can produce a larger sum. Therefore, the answer is 16. 
 
 
 Example 2: 
 
 
 ​​​​​​​ 
 
 Input:   parent = [-1,0,0], op = [0,0,0], score = [1,2,3] 
 
 Output:   6 
 
 Explanation: 
 
 
 We only need to process node 0, since node 1 and node 2 are leaves. 
 
 Since  op[0] = 0 , we can choose to do nothing. 
 
 Therefore, all scores are preserved, giving the maximum possible sum of 6. 
 
 
 
 Example 3: 
 
 
 ​​​​​​​ 
 
 Input:   parent = [-1], op = [1], score = [-10] 
 
 Output:   -10 
 
 Explanation: 
 
 
 The only node in the tree is a leaf, so we can't process any node. 
 
 Therefore, the maximum possible score sum is -10. 
 
 
 
   
 
 Constraints: 
 
 
 1 <= n <= 10 5 
 
 n == parent.length == op.length == score.length 
 
 parent[0] == -1 
 
 0 <= parent[i] <= n - 1  for all  i  in  [1, n - 1] 
 
 0 <= op[i] <= 1 
 
 -10 4  <= score[i] <= 10 4 
 
 The input is generated such that the array  parent  represents a valid tree rooted at node 0.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    long long maxScore(vector<int>& parent,
                       vector<int>& op,
                       vector<int>& score) {
        int n = parent.size();

        vector<vector<int>> children(n);
        vector<int> degree(n, 0);
        vector<long long> dp(n, 0);
        queue<int> q;

        for (int i = 1; i < n; i++) {
            children[parent[i]].push_back(i);
            degree[parent[i]]++;
        }

        vector<long long> sum(n, 0);
        vector<long long> mn(n, LLONG_MAX);

        for (int i = 0; i < n; i++) {
            if (degree[i] == 0) {
                dp[i] = score[i];
                q.push(i);
            }
        }

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            if (u == 0)
                continue;

            int p = parent[u];

            sum[p] += dp[u];
            mn[p] = min(mn[p], dp[u]);

            degree[p]--;

            if (degree[p] == 0) {
                dp[p] = score[p] + sum[p];

                if (op[p] == 1)
                    dp[p] -= mn[p];
                else
                    dp[p] -= min(0LL, mn[p]);

                q.push(p);
            }
        }

        return dp[0];
    }
};
```

---

## 4113. Game of Divisible Sums

**Problem:** https://leetcode.com/problems/game-of-divisible-sums/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2197469425  
**Language:** cpp

### Description

Alice and Bob are playing a game with an integer array  nums . Alice goes first. 
 
 On each turn, the current player takes and removes either the  leftmost element  or, if at least two elements remain, the  two leftmost elements . 
 
 The  sum  of the elements taken in that turn determines who plays next: 
 
 
 If the sum is divisible by 3, the other player plays next. 
 
 Otherwise, the same player plays again. 
 
 
 The  score  of a player is the sum of the values of all elements that player takes. 
 
 Both players play optimally, with each player trying to  maximize  their own score. 
 
 The game ends when all elements have been taken. 
 
 Return Alice's score  minus  Bob's score. 
 
   
 
 Example 1: 
 
 
 Input:   nums = [3,6,4] 
 
 Output:   5 
 
 Explanation: 
 
 One sequence of optimal turns is as follows: 
 
 
 Alice takes the two leftmost elements. Their sum is  3 + 6 = 9 , which is divisible by 3, so Bob plays next. Alice's score is now 9, and the remaining array is  [4] . 
 
 Bob takes the only remaining element. His score is 4, and the game ends. 
 
 
 Alice's score minus Bob's score is  9 - 4 = 5 , so the answer is 5. 
 
 
 Example 2: 
 
 
 Input:   nums = [6,1,2,1,2] 
 
 Output:   12 
 
 Explanation: 
 
 One sequence of optimal turns is as follows: 
 
 
 Alice takes the two leftmost elements. Their sum is  6 + 1 = 7 , which is not divisible by 3, so Alice plays again. Her score is now 7, and the remaining array is  [2, 1, 2] . 
 
 Alice takes the leftmost element. Its value is 2, which is not divisible by 3, so Alice plays again. Her score is now  7 + 2 = 9 , and the remaining array is  [1, 2] . 
 
 Alice takes both remaining elements. Her score is now  9 + 1 + 2 = 12 , and the game ends. 
 
 
 Bob takes no elements, so his score is 0. Alice's score minus Bob's score is  12 - 0 = 12 , so the answer is 12. 
 
 
 Example 3: 
 
 
 Input:   nums = [3,3,4,5] 
 
 Output:   -3 
 
 Explanation: 
 
 One sequence of optimal turns is as follows: 
 
 
 Alice takes the two leftmost elements. Their sum is  3 + 3 = 6 , which is divisible by 3, so Bob plays next. Alice's score is now 6, and the remaining array is  [4, 5] . 
 
 Bob takes both remaining elements. His score is  4 + 5 = 9 , and the game ends. 
 
 
 Alice's score minus Bob's score is  6 - 9 = -3 , so the answer is -3. 
 
 
   
 
 Constraints: 
 
 
 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    long long maxDifference(vector<int>& nums) {
        int n = nums.size();
        vector<long long> dp(n + 2, 0);

        for (int i = n - 1; i >= 0; i--) {
            long long sum = nums[i];

            if (sum % 3 == 0)
                dp[i] = sum - dp[i + 1];
            else
                dp[i] = sum + dp[i + 1];

            if (i + 1 < n) {
                sum = (long long)nums[i] + nums[i + 1];

                long long score;

                if (sum % 3 == 0)
                    score = sum - dp[i + 2];
                else
                    score = sum + dp[i + 2];

                dp[i] = max(dp[i], score);
            }
        }

        return dp[0];
    }
};
```

---

## 4114. Count Consistent Subarrays II

**Problem:** https://leetcode.com/problems/count-consistent-subarrays-ii/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2197471481  
**Language:** cpp

### Description

You are given an integer array  nums . 
 
 A  subarray  is called  consistent  if the  bitwise AND  of all its elements is equal to the  minimum  value of the subarray. 
 
 Return the number of  consistent subarrays  in  nums . 
 
   
 
 Example 1: 
 
 
 Input:   nums = [5,3,1,2] 
 
 Output:   6 
 
 Explanation: 
 
 The following subarrays are consistent: 
 
 
 
 Subarray 
 Values 
 Bitwise AND 
 Minimum Value 
 
 
 nums[0..0] 
 [5] 
 5 
 5 
 
 
 nums[1..1] 
 [3] 
 3 
 3 
 
 
 nums[2..2] 
 [1] 
 1 
 1 
 
 
 nums[3..3] 
 [2] 
 2 
 2 
 
 
 nums[1..2] 
 [3, 1] 
 3 AND 1 = 1 
 1 
 
 
 nums[0..2] 
 [5, 3, 1] 
 5 AND 3 AND 1 = 1 
 1 
 
 
 
 
 Therefore, the number of consistent subarrays is 6. 
 
 
 Example 2: 
 
 
 Input:   nums = [1,1,1] 
 
 Output:   6 
 
 Explanation: 
 
 For every subarray, both the bitwise AND and the minimum value are equal to 1. Therefore, the answer is 6. 
 
 
 Example 3: 
 
 
 Input:   nums = [0] 
 
 Output:   1 
 
 Explanation: 
 
 The only subarray is  [0] , whose bitwise AND and minimum value are both 0. Therefore, the answer is 1. 
 
 
   
 
 Constraints: 
 
 
 1 <= nums.length <= 2 * 10 ​​​​​​​5 
 
 0 <= nums[i] <= 10 6

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    long long countConsistent(vector<int>& nums) {
        int n = nums.size();

        vector<int> left(n), right(n);
        stack<int> st;

        // Previous strictly smaller element
        for (int i = 0; i < n; i++) {
            while (!st.empty() && nums[st.top()] >= nums[i])
                st.pop();

            left[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }

        while (!st.empty())
            st.pop();

        // Next smaller or equal element
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && nums[st.top()] > nums[i])
                st.pop();

            right[i] = st.empty() ? n : st.top();
            st.push(i);
        }

        vector<int> lastZero(31, -1);

        // Restrict left boundary using bitwise AND
        for (int i = 0; i < n; i++) {
            for (int b = 0; b < 31; b++) {
                if ((nums[i] & (1 << b)) == 0)
                    lastZero[b] = i;
                else
                    left[i] = max(left[i], lastZero[b]);
            }
        }

        vector<int> nextZero(31, n);

        // Restrict right boundary using bitwise AND
        for (int i = n - 1; i >= 0; i--) {
            for (int b = 0; b < 31; b++) {
                if ((nums[i] & (1 << b)) == 0)
                    nextZero[b] = i;
                else
                    right[i] = min(right[i], nextZero[b]);
            }
        }

        long long ans = 0;

        for (int i = 0; i < n; i++) {
            ans += 1LL * (i - left[i]) *
                   (right[i] - i);
        }

        return ans;
    }
};
```

---

## 4115. Sum of Compatible Numbers in Range II

**Problem:** https://leetcode.com/problems/sum-of-compatible-numbers-in-range-ii/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2198977270  
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
    static const long long MOD = 1000000007LL;

    long long solve(long long n, long long limit) {
        if (limit < 0) return 0;

        long long cnt = 1, sum = 0;
        long long ans = 0;
        long long prefix = 0;

        for (int i = 50; i >= 0; i--) {
            long long bit = 1LL << i;

            if (limit & bit) {
                // Choose 0 at this bit, making x smaller
                if ((n & bit) == 0) {
                    // Remaining lower bits are handled below
                }
            }
        }

        // Digit DP: count and sum for tight/loose states
        long long count[2] = {0, 1};
        long long total[2] = {0, 0};

        for (int i = 50; i >= 0; i--) {
            long long nextCount[2] = {0, 0};
            long long nextTotal[2] = {0, 0};

            int bound = (limit >> i) & 1;

            for (int tight = 0; tight <= 1; tight++) {
                for (int b = 0; b <= 1; b++) {
                    if (b && (n & (1LL << i)))
                        continue;

                    if (tight && b > bound)
                        continue;

                    int nt = tight && (b == bound);

                    long long ways = count[tight];
                    long long value = (1LL << i) % MOD;

                    nextCount[nt] =
                        (nextCount[nt] + ways) % MOD;

                    nextTotal[nt] =
                        (nextTotal[nt] + total[tight]
                         + ways * b % MOD * value) % MOD;
                }
            }

            for (int j = 0; j < 2; j++) {
                count[j] = nextCount[j];
                total[j] = nextTotal[j];
            }
        }

        return (total[0] + total[1]) % MOD;
    }

public:
    int sumOfGoodIntegers(long long n, long long k) {
        long long right = solve(n, n + k);
        long long left = solve(n, n - k - 1);

        return (right - left + MOD) % MOD;
    }
};
```

---
