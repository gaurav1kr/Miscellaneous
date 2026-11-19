# Sliding Window Two Pointers

## 4109. Count Valid Suffix Sorts II

**Problem:** https://leetcode.com/problems/count-valid-suffix-sorts-ii/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Array, Hash Table, Sliding Window, Rolling Hash, String Matching, Counting, Hash Function  
**Primary pattern:** Sliding Window Two Pointers  
**Latest Accepted submission in searched history:** 2195617330  
**Language:** cpp

### Description

You are given two integer arrays  nums  and  target  of lengths  n  and  m , respectively, where  n <= m . 
 
 For each index  i , consider sorting the  suffix   nums[i..n - 1]  of the original array in  non-increasing order . 
 
 Return an integer array  ans  of length  m - n + 1 , where  ans[k]  is the number of indices  i  for which the resulting array equals  target[k..k + n - 1] . 
 
 A  suffix  of an array is a  subarray  that begins at any index and extends to its end. 
 
   
 
 Example 1: 
 
 
 Input:   nums = [2,2,3], target = [2,2,3,2,1,3,2,2] 
 
 Output:   [1,1,0,0,0,1] 
 
 Explanation: 
 
 Sorting the suffix starting at indices 0, 1, and 2 produces  [3, 2, 2] ,  [2, 3, 2] , and  [2, 2, 3] , respectively. 
 
 
 k = 0 :  [2, 2, 3]  is produced by  i = 2 . 
 
 k = 1 :  [2, 3, 2]  is produced by  i = 1 . 
 
 k = 2, 3, 4 : None of the corresponding subarrays can be produced. 
 
 k = 5 :  [3, 2, 2]  is produced by  i = 0 . 
 
 
 Therefore, the answer is  [1, 1, 0, 0, 0, 1] . 
 
 
 Example 2: 
 
 
 Input:   nums = [5,6,5], target = [5,6,5,5,6,5] 
 
 Output:   [2,1,0,2] 
 
 Explanation: 
 
 Sorting the suffix starting at index 0 produces  [6, 5, 5] , while starting at either index 1 or 2 produces  [5, 6, 5] . 
 
 
 k = 0 :  [5, 6, 5]  is produced by  i = 1  and  i = 2 . 
 
 k = 1 :  [6, 5, 5]  is produced by  i = 0 . 
 
 k = 2 :  [5, 5, 6]  cannot be produced. 
 
 k = 3 :  [5, 6, 5]  is produced by  i = 1  and  i = 2 . 
 
 
 Therefore, the answer is  [2, 1, 0, 2] . 
 
 
   
 
 Constraints: 
 
 
 n == nums.length 
 
 m == target.length 
 
 1 <= n <= m <= 10 5 
 
 1 <= nums[i], target[i] <= 10 5

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    vector<int> countSuffix(vector<int>& nums,
                            vector<int>& target) {
        int n = nums.size();
        int m = target.size();

        // Step 1: Z-algorithm for prefix matching
        vector<int> a = nums;
        a.push_back(0);
        a.insert(a.end(), target.begin(), target.end());

        int sz = a.size();
        vector<int> z(sz, 0);

        int l = 0, r = 0;

        for (int i = 1; i < sz; i++) {
            if (i <= r)
                z[i] = min(r - i + 1, z[i - l]);

            while (i + z[i] < sz &&
                   a[z[i]] == a[i + z[i]]) {
                z[i]++;
            }

            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }

        // Step 2: Sliding window frequency matching
        vector<int> freq(100001, 0);
        int different = 0;

        auto update = [&](int x, int delta) {
            if (freq[x] != 0)
                different--;

            freq[x] += delta;

            if (freq[x] != 0)
                different++;
        };

        for (int x : nums)
            update(x, 1);

        for (int i = 0; i < n; i++)
            update(target[i], -1);

        // Step 3: Precompute last ascent
        vector<int> last(m, -1);

        for (int i = 1; i < m; i++) {
            last[i] = last[i - 1];

            if (target[i - 1] < target[i])
                last[i] = i - 1;
        }

        // Step 4: Process each window
        vector<int> ans;

        for (int k = 0; k <= m - n; k++) {
            if (k > 0) {
                update(target[k - 1], 1);
                update(target[k + n - 1], -1);
            }

            if (different != 0) {
                ans.push_back(0);
                continue;
            }

            int p = min(n, z[n + 1 + k]);
            int end = k + n - 1;

            int q = max(0, last[end] - k + 1);

            ans.push_back(
                max(0, min(p, n - 1) - q + 1)
            );
        }

        return ans;
    }
};
```

---

