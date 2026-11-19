# Sorting Divide and Conquer

## 4101. Find All Numbers Disappeared in an Array III

**Problem:** https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-iii/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Array, Sorting  
**Primary pattern:** Sorting Divide and Conquer  
**Latest Accepted submission in searched history:** 2195615514  
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
    vector<vector<int>> findDisappearedNumbers(
        vector<int>& nums, int lower, int upper) {

        sort(nums.begin(), nums.end());

        vector<vector<int>> ans;
        int start = lower;

        for (int num : nums) {
            if (num < start)
                continue;

            if (num > upper)
                break;

            if (num > start) {
                ans.push_back({start, num - 1});
            }

            start = num + 1;
        }

        if (start <= upper) {
            ans.push_back({start, upper});
        }

        return ans;
    }
};
```

---

