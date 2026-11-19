# Greedy Intervals

## 4098. Minimize the Maximum Value of GCD-Connected Array

**Problem:** https://leetcode.com/problems/minimize-the-maximum-value-of-gcd-connected-array/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Math, Greedy, Number Theory  
**Primary pattern:** Greedy Intervals  
**Latest Accepted submission in searched history:** 2195615129  
**Language:** cpp

### Description

You are given three integers  n ,  index , and  value . 
 
 An integer array  nums  of length  n  is called  GCD-Connected  if: 
 
 
 nums[i] > 0  for  0 <= i <= n - 1 . 
 
 nums[i] < nums[i + 1]  for  0 <= i <= n - 2 . 
 
 nums[index] = value . 
 
 gcd (nums[i], nums[i + 1]) > 1  for  0 <= i <= n - 2 . 
 
 
 Return the  minimum  possible maximum value,  nums[n - 1] , among all GCD-Connected arrays  nums . If no such array exists, return -1. 
 
   
 
 Example 1: 
 
 
 Input:   n = 4, index = 2, value = 8 
 
 Output:   10 
 
 Explanation: 
 
 
 The GCD-Connected array will look like: ​​​​​​​ nums = [?, ?, 8, ?]  since  nums[2] = 8 . 
 
 Since  nums[3] > 8  and  gcd(8, 9) = 1 , every valid GCD-Connected array must have  nums[3] >= 10 . 
 
 One optimal array satisfying all conditions is  [2, 4, 8, 10] . 
 
 Thus, the minimum possible value of  nums[3]  is 10. 
 
 
 
 Example 2: 
 
 
 Input:   n = 2, index = 1, value = 3 
 
 Output:   -1 
 
 Explanation: 
 
 
 The GCD-Connected array will look like:  nums = [?, 3]  since  nums[1] = 3 . 
 
 Since we need  0 < nums[0] < nums[1] = 3 , there are only two possible arrays:  [1, 3]  and  [2, 3] . Neither of them satisfies  gcd(nums[0], nums[1]) > 1 . 
 
 Therefore, no valid GCD-Connected array exists, and the answer is -1. 
 
 
 
 Example 3: 
 
 
 Input:   n = 2, index = 0, value = 3 
 
 Output:   6 
 
 Explanation: 
 
 
 The GCD-Connected array will look like:  nums = [3, ?]  since  nums[0] = 3 . 
 
 Since  nums[1] > 3  and  gcd(3, 4) = gcd(3, 5) = 1 , every valid GCD-Connected array must have  nums[1] >= 6 . 
 
 One optimal array is  [3, 6] . 
 
 Thus, the minimum possible value of  nums[1]  is 6. 
 
 
 
   
 
 Constraints: 
 
 
 2 <= n <= 10 9 
 
 1 <= value <= 10 9 
 
 0 <= index <= n - 1

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    long long minimumMaxValue(int n, int index, int value) {
        if (value == 1)
            return -1;

        // Find smallest prime factor
        long long p = value;

        for (long long i = 2; i * i <= value; i++) {
            if (value % i == 0) {
                p = i;
                break;
            }
        }

        // Check whether left side is possible
        if (index > 0) {
            long long first = (long long)value - p
                            - 2LL * (index - 1);

            if (first < 2)
                return -1;
        }

        // No elements to the right
        if (index == n - 1)
            return value;

        // Minimum possible last element
        return (long long)value + p
               + 2LL * (n - index - 2);
    }
};
```

---

