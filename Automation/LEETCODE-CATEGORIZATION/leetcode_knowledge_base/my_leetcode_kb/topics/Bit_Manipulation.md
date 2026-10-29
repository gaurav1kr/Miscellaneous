# Bit Manipulation

**Problems:** 44

## Quick revision checklist

Use XOR, bit masks, bit positions, or binary representation.

## Problem index

- [136. Single Number](#136-single-number) — Easy; code: yes
- [137. Single Number II](#137-single-number-ii) — Medium; code: yes
- [201. Bitwise AND of Numbers Range](#201-bitwise-and-of-numbers-range) — Medium; code: yes
- [260. Single Number III](#260-single-number-iii) — Medium; code: yes
- [393. UTF-8 Validation](#393-utf-8-validation) — Medium; code: yes
- [461. Hamming Distance](#461-hamming-distance) — Easy; code: yes
- [476. Number Complement](#476-number-complement) — Easy; code: yes
- [693. Binary Number with Alternating Bits](#693-binary-number-with-alternating-bits) — Easy; code: yes
- [868. Binary Gap](#868-binary-gap) — Easy; code: yes
- [1009. Complement of Base 10 Integer](#1009-complement-of-base-10-integer) — Easy; code: yes
- [1018. Binary Prefix Divisible By 5](#1018-binary-prefix-divisible-by-5) — Easy; code: yes
- [1318. Minimum Flips to Make a OR b Equal to c](#1318-minimum-flips-to-make-a-or-b-equal-to-c) — Medium; code: yes
- [1720. Decode XORed Array](#1720-decode-xored-array) — Easy; code: yes
- [1734. Decode XORed Permutation](#1734-decode-xored-permutation) — Medium; code: yes
- [2220. Minimum Bit Flips to Convert Number](#2220-minimum-bit-flips-to-convert-number) — Easy; code: yes
- [2419. Longest Subarray With Maximum Bitwise AND](#2419-longest-subarray-with-maximum-bitwise-and) — Medium; code: yes
- [2425. Bitwise XOR of All Pairings](#2425-bitwise-xor-of-all-pairings) — Medium; code: yes
- [2433. Find The Original Array of Prefix Xor](#2433-find-the-original-array-of-prefix-xor) — Medium; code: yes
- [2568. Minimum Impossible OR](#2568-minimum-impossible-or) — Medium; code: yes
- [2595. Number of Even and Odd Bits](#2595-number-of-even-and-odd-bits) — Easy; code: yes
- [2683. Neighboring Bitwise XOR](#2683-neighboring-bitwise-xor) — Medium; code: yes
- [2749. Minimum Operations to Make the Integer Zero](#2749-minimum-operations-to-make-the-integer-zero) — Medium; code: yes
- [2859. Sum of Values at Indices With K Set Bits](#2859-sum-of-values-at-indices-with-k-set-bits) — Easy; code: yes
- [2917. Find the K-or of an Array](#2917-find-the-k-or-of-an-array) — Easy; code: yes
- [2980. Check if Bitwise OR Has Trailing Zeros](#2980-check-if-bitwise-or-has-trailing-zeros) — Easy; code: yes
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](#2997-minimum-number-of-operations-to-make-array-xor-equal-to-k) — Medium; code: yes
- [3064. Guess the Number Using Bitwise Questions I](#3064-guess-the-number-using-bitwise-questions-i) — Medium; code: yes
- [3094. Guess the Number Using Bitwise Questions II](#3094-guess-the-number-using-bitwise-questions-ii) — Medium; code: yes
- [3133. Minimum Array End](#3133-minimum-array-end) — Medium; code: yes
- [3173. Bitwise OR of Adjacent Elements](#3173-bitwise-or-of-adjacent-elements) — Easy; code: yes
- [3199. Count Triplets with Even XOR Set Bits I](#3199-count-triplets-with-even-xor-set-bits-i) — Easy; code: yes
- [3215. Count Triplets with Even XOR Set Bits II](#3215-count-triplets-with-even-xor-set-bits-ii) — Medium; code: yes
- [3226. Number of Bit Changes to Make Two Integers Equal](#3226-number-of-bit-changes-to-make-two-integers-equal) — Easy; code: yes
- [3309. Maximum Possible Number by Binary Concatenation](#3309-maximum-possible-number-by-binary-concatenation) — Medium; code: yes
- [3314. Construct the Minimum Bitwise Array I](#3314-construct-the-minimum-bitwise-array-i) — Easy; code: yes
- [3315. Construct the Minimum Bitwise Array II](#3315-construct-the-minimum-bitwise-array-ii) — Medium; code: yes
- [3566. Partition Array into Two Equal Product Subsets](#3566-partition-array-into-two-equal-product-subsets) — Medium; code: yes
- [3595. Once Twice](#3595-once-twice) — Medium; code: yes
- [3644. Maximum K to Sort a Permutation](#3644-maximum-k-to-sort-a-permutation) — Medium; code: yes
- [3674. Minimum Operations to Equalize Array](#3674-minimum-operations-to-equalize-array) — Easy; code: yes
- [3688. Bitwise OR of Even Numbers in an Array](#3688-bitwise-or-of-even-numbers-in-an-array) — Easy; code: yes
- [3702. Longest Subsequence With Non-Zero Bitwise XOR](#3702-longest-subsequence-with-non-zero-bitwise-xor) — Medium; code: yes
- [3827. Count Monobit Integers](#3827-count-monobit-integers) — Easy; code: yes
- [3950. Exactly One Consecutive Set Bits Pair](#3950-exactly-one-consecutive-set-bits-pair) — Easy; code: yes

---

## 136. Single Number

**Problem:** https://leetcode.com/problems/single-number/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a non-empty  array of integers nums , every element appears twice except for one. Find that single one. 
 
 You must implement a solution with a linear runtime complexity and use only constant extra space. 

 Example 1: 

 Input: nums = [2,2,1] 
 
 Output: 1 

 Example 2: 

 Input: nums = [4,1,2,1,2] 
 
 Output: 4 

 Example 3: 

 Input: nums = [1] 
 
 Output: 1 

 Constraints: 

 1 <= nums.length <= 3 * 10 4 
 
 -3 * 10 4 <= nums[i] <= 3 * 10 4 
 
 Each element in the array appears twice except for one element which appears only once.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for (int num : nums) result ^= num;
        return result;
    }
};
```


## 137. Single Number II

**Problem:** https://leetcode.com/problems/single-number-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array nums where every element appears three times except for one, which appears exactly once . Find the single element and return it . 
 
 You must implement a solution with a linear runtime complexity and use only constant extra space. 

 Example 1: 
 
```
Input:
 nums = [2,2,3,2]

Output:
 3
```
 
 Example 2: 
 
```
Input:
 nums = [0,1,0,1,0,1,99]

Output:
 99
```

 Constraints: 

 1 <= nums.length <= 3 * 10 4 
 
 -2 31 <= nums[i] <= 2 31 - 1 
 
 Each element in nums appears exactly three times except for one element which appears once .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0, twos = 0;
        for (int num : nums) {
            ones = (ones ^ num) & ~twos;
            twos = (twos ^ num) & ~ones;
        }
        return ones;
    }
};
```


## 201. Bitwise AND of Numbers Range

**Problem:** https://leetcode.com/problems/bitwise-and-of-numbers-range/

**Difficulty:** Medium | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given two integers left and right that represent the range [left, right] , return the bitwise AND of all numbers in this range, inclusive . 

 Example 1: 
 
```
Input:
 left = 5, right = 7

Output:
 4
```

 Example 2: 
 
```
Input:
 left = 0, right = 0

Output:
 0
```

 Example 3: 
 
```
Input:
 left = 1, right = 2147483647

Output:
 0
```

 Constraints: 

 0 <= left <= right <= 2 31 - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int rangeBitwiseAnd(int n, int m) {
    int ans=0;
    for(int i=0;i<32;i++){
        if(((n/(1<<i))==(m/(1<<i))) && (n & (1 << i))){
            ans=(ans|(1<<i));
        }
    }
    return ans;
    }
};
```


## 260. Single Number III

**Problem:** https://leetcode.com/problems/single-number-iii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array nums , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order . 
 
 You must write an algorithm that runs in linear runtime complexity and uses only constant extra space. 

 Example 1: 
 
```
Input:
 nums = [1,2,1,3,2,5]

Output:
 [3,5]

Explanation: 
 [5, 3] is also a valid answer.
```

 Example 2: 
 
```
Input:
 nums = [-1,0]

Output:
 [-1,0]
```

 Example 3: 
 
```
Input:
 nums = [0,1]

Output:
 [1,0]
```

 Constraints: 

 2 <= nums.length <= 3 * 10 4 
 
 -2 31 <= nums[i] <= 2 31 - 1 
 
 Each integer in nums will appear twice, only two integers will appear once.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    vector<int> singleNumber(vector<int>& nums) 
    {
        long long xorr=0;
        for(int i=0;i<nums.size();i++)
        {
            xorr^=nums[i];
        }
        long long right=(xorr&xorr-1)^xorr;
        int b1=0,b2=0;
        for(int i=0;i<nums.size();i++)
        {
            if(right&nums[i]) b1^=nums[i];
            else b2^=nums[i];
        }
        return {b1,b2};
    }
};
```


## 393. UTF-8 Validation

**Problem:** https://leetcode.com/problems/utf-8-validation/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters). 
 
 A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules: 

 For a 1-byte character, the first bit is a 0 , followed by its Unicode code. 
 
 For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0 , followed by n - 1 bytes with the most significant 2 bits being 10 . 

 This is how the UTF-8 encoding would work: 
 
```
Number of Bytes | UTF-8 Octet Sequence
 | (binary)
 --------------------+-----------------------------------------
 1 | 0xxxxxxx
 2 | 110xxxxx 10xxxxxx
 3 | 1110xxxx 10xxxxxx 10xxxxxx
 4 | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```

 x denotes a bit in the binary form of a byte that may be either 0 or 1 . 
 
 Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data. 

 Example 1: 
 
```
Input:
 data = [197,130,1]

Output:
 true

Explanation:
 data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
```

 Example 2: 
 
```
Input:
 data = [235,140,4]

Output:
 false

Explanation:
 data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
```

 Constraints: 

 1 <= data.length <= 2 * 10 4 
 
 0 <= data[i] <= 255

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int remaining = 0;
        for (int byte : data) {
            if (remaining > 0) {
                if ((byte & 0xC0) != 0x80) return false;
                --remaining;
            } else if ((byte & 0x80) == 0) {
                continue;
            } else if ((byte & 0xE0) == 0xC0) {
                remaining = 1;
            } else if ((byte & 0xF0) == 0xE0) {
                remaining = 2;
            } else if ((byte & 0xF8) == 0xF0) {
                remaining = 3;
            } else {
                return false;
            }
        }
        return remaining == 0;
    }
};
```


## 461. Hamming Distance

**Problem:** https://leetcode.com/problems/hamming-distance/

**Difficulty:** Easy | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

The Hamming distance between two integers is the number of positions at which the corresponding bits are different. 
 
 Given two integers x and y , return the Hamming distance between them . 

 Example 1: 
 
```
Input:
 x = 1, y = 4

Output:
 2

Explanation:

1 (0 0 0 1)
4 (0 1 0 0)
 ↑ ↑
The above arrows point to positions where the corresponding bits are different.
```

 Example 2: 
 
```
Input:
 x = 3, y = 1

Output:
 1
```

 Constraints: 

 0 <= x, y <= 2 31 - 1 

 Note: This question is the same as 2220: Minimum Bit Flips to Convert Number.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int hammingDistance(int x, int y) {
        int xor_val = x ^ y, count = 0;
        while (xor_val) {
            count += xor_val & 1;
            xor_val >>= 1;
        }
        return count;
    }
};
```


## 476. Number Complement

**Problem:** https://leetcode.com/problems/number-complement/

**Difficulty:** Easy | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

The complement of an integer is the integer you get when you flip all the 0 's to 1 's and all the 1 's to 0 's in its binary representation. 

 For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2 . 

 Given an integer num , return its complement . 

 Example 1: 
 
```
Input:
 num = 5

Output:
 2

Explanation:
 The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
```

 Example 2: 
 
```
Input:
 num = 1

Output:
 0

Explanation:
 The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
```

 Constraints: 

 1 <= num < 2 31 

 Note: This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int findComplement(int num) {
        int mask = 0, temp = num;
        while (temp) {
            mask = (mask << 1) | 1;
            temp >>= 1;
        }
        return num ^ mask;
    }
};
```


## 693. Binary Number with Alternating Bits

**Problem:** https://leetcode.com/problems/binary-number-with-alternating-bits/

**Difficulty:** Easy | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values. 

 Example 1: 
 
```
Input:
 n = 5

Output:
 true

Explanation:
 The binary representation of 5 is: 101
```

 Example 2: 
 
```
Input:
 n = 7

Output:
 false

Explanation:
 The binary representation of 7 is: 111.
```

 Example 3: 
 
```
Input:
 n = 11

Output:
 false

Explanation:
 The binary representation of 11 is: 1011.
```

 Constraints: 

 1 <= n <= 2 31 - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool hasAlternatingBits(int n) {
        int cnt = 0;
        int c = n;
        while(n > 0){
            int rem = n % 2;
            if(c % 2 == 0){
                if(rem == 0 && cnt % 2 == 0){
                    cnt++;
                }
                else if(rem == 1 && cnt % 2 == 1){
                    cnt++;
                }
                else{
                    return false;
                }
            }
            else{
                if(rem == 1 && cnt % 2 == 0){
                    cnt++;
                }
                else if(rem == 0 && cnt % 2 == 1){
                    cnt++;
                }
                else{
                    return false;
                }
            }
            n /= 2;
        }
            return true;
        }
        
};
```


## 868. Binary Gap

**Problem:** https://leetcode.com/problems/binary-gap/

**Difficulty:** Easy | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a positive integer n , find and return the longest distance between any two adjacent 1 's in the binary representation of n . If there are no two adjacent 1 's, return 0 . 
 
 Two 1 's are adjacent if there are only 0 's separating them (possibly no 0 's). The distance between two 1 's is the absolute difference between their bit positions. For example, the two 1 's in "1001" have a distance of 3. 

 Example 1: 
 
```
Input:
 n = 22

Output:
 2

Explanation:
 22 in binary is "10110".
The first adjacent pair of 1's is "
1
0
1
10" with a distance of 2.
The second adjacent pair of 1's is "10
11
0" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "
1
01
1
0" is not a valid pair since there is a 1 separating the two 1's underlined.
```

 Example 2: 
 
```
Input:
 n = 8

Output:
 0

Explanation:
 8 in binary is "1000".
There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.
```

 Example 3: 
 
```
Input:
 n = 5

Output:
 2

Explanation:
 5 in binary is "101".
```

 Constraints: 

 1 <= n <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int binaryGap(int n) {
        int last = -1, res = 0;
        for (int i = 0; n; ++i, n >>= 1) {
            if (n & 1) {
                if (last != -1)
                    res = max(res, i - last);
                last = i;
            }
        }
        return res;
    }
};
```


## 1009. Complement of Base 10 Integer

**Problem:** https://leetcode.com/problems/complement-of-base-10-integer/

**Difficulty:** Easy | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

The complement of an integer is the integer you get when you flip all the 0 's to 1 's and all the 1 's to 0 's in its binary representation. 

 For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2 . 

 Given an integer n , return its complement . 

 Example 1: 
 
```
Input:
 n = 5

Output:
 2

Explanation:
 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
```

 Example 2: 
 
```
Input:
 n = 7

Output:
 0

Explanation:
 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
```

 Example 3: 
 
```
Input:
 n = 10

Output:
 5

Explanation:
 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
```

 Constraints: 

 0 <= n < 10 9 

 Note: This question is the same as 476: https://leetcode.com/problems/number-complement/

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int bitwiseComplement(int n) {
        if (n == 0) return 1;
        int mask = 1;
        while (mask <= n) mask <<= 1;
        return n ^ (mask - 1);
    }
};
```


## 1018. Binary Prefix Divisible By 5

**Problem:** https://leetcode.com/problems/binary-prefix-divisible-by-5/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a binary array nums ( 0-indexed ). 
 
 We define x i as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit). 

 For example, if nums = [1,0,1] , then x 0 = 1 , x 1 = 2 , and x 2 = 5 . 

 Return an array of booleans answer where answer[i] is true if x i is divisible by 5 . 

 Example 1: 
 
```
Input:
 nums = [0,1,1]

Output:
 [true,false,false]

Explanation:
 The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
```

 Example 2: 
 
```
Input:
 nums = [1,1,1]

Output:
 [false,false,false]
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 nums[i] is either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& A) {
        vector<bool> res;
        int num = 0;
        for (int bit : A) {
            num = ((num << 1) + bit) % 5;
            res.push_back(num == 0);
        }
        return res;
    }
};
```


## 1318. Minimum Flips to Make a OR b Equal to c

**Problem:** https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

**Difficulty:** Medium | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given 3 positives numbers a , b and c . Return the minimum flips required in some bits of a and b to make (  a OR b == c  ). (bitwise OR operation). 
Flip operation consists of change  any  single bit 1 to 0 or change the bit 0 to 1 in their binary representation. 

 Example 1: 
 
 [Figure: https://assets.leetcode.com/uploads/2020/01/06/sample_3_1676.png] 
 
```
Input:
 a = 2, b = 6, c = 5

Output:
 3

Explanation: 
After flips a = 1 , b = 4 , c = 5 such that (
a
 OR 
b
 == 
c
)
```

 Example 2: 
 
```
Input:
 a = 4, b = 2, c = 7

Output:
 1
```

 Example 3: 
 
```
Input:
 a = 1, b = 2, c = 3

Output:
 0
```

 Constraints: 

 1 <= a <= 10^9 
 
 1 <= b <= 10^9 
 
 1 <= c <= 10^9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int minFlips(int a, int b, int c) {
        int res = 0;
        for (int i = 0; i < 32; ++i) {
            int x = (a >> i) & 1, y = (b >> i) & 1, z = (c >> i) & 1;
            if ((x | y) != z) res += z ? 1 : x + y;
        }
        return res;
    }
};
```


## 1720. Decode XORed Array

**Problem:** https://leetcode.com/problems/decode-xored-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There is a hidden integer array arr that consists of n non-negative integers. 
 
 It was encoded into another integer array encoded of length n - 1 , such that encoded[i] = arr[i] XOR arr[i + 1] . For example, if arr = [1,0,2,1] , then encoded = [1,2,3] . 
 
 You are given the encoded array. You are also given an integer first , that is the first element of arr , i.e. arr[0] . 
 
 Return the original array arr . It can be proved that the answer exists and is unique. 

 Example 1: 
 
```
Input:
 encoded = [1,2,3], first = 1

Output:
 [1,0,2,1]

Explanation:
 If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
```

 Example 2: 
 
```
Input:
 encoded = [6,2,7,3], first = 4

Output:
 [4,2,0,7,4]
```

 Constraints: 

 2 <= n <= 10 4 
 
 encoded.length == n - 1 
 
 0 <= encoded[i] <= 10 5 
 
 0 <= first <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 vector<int> decode(vector<int>& encoded,int first){
  vector<int> ans{first};for(int x:encoded)ans.push_back(ans.back()^x);return ans;
 }
};
```


## 1734. Decode XORed Permutation

**Problem:** https://leetcode.com/problems/decode-xored-permutation/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There is an integer array perm that is a permutation of the first n positive integers, where n is always odd . 
 
 It was encoded into another integer array encoded of length n - 1 , such that encoded[i] = perm[i] XOR perm[i + 1] . For example, if perm = [1,3,2] , then encoded = [2,1] . 
 
 Given the encoded array, return the original array perm . It is guaranteed that the answer exists and is unique. 

 Example 1: 
 
```
Input:
 encoded = [3,1]

Output:
 [1,2,3]

Explanation:
 If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
```

 Example 2: 
 
```
Input:
 encoded = [6,5,4,6]

Output:
 [2,4,1,5,3]
```

 Constraints: 

 3 <= n < 10 5 
 
 n  is odd. 
 
 encoded.length == n - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        int n = encoded.size() + 1;
        int total = 0, odd = 0;
        for (int i = 1; i <= n; ++i) total ^= i;
        for (int i = 1; i < encoded.size(); i += 2) odd ^= encoded[i];

        vector<int> perm(n);
        perm[0] = total ^ odd;
        for (int i = 1; i < n; ++i)
            perm[i] = perm[i - 1] ^ encoded[i - 1];
        return perm;
    }
};
```


## 2220. Minimum Bit Flips to Convert Number

**Problem:** https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

**Difficulty:** Easy | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0 . 

 For example, for x = 7 , the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110 , flip the second bit from the right to get 101 , flip the fifth bit from the right (a leading zero) to get 10111 , etc. 

 Given two integers start and goal , return the minimum number of bit flips to convert start to goal . 

 Example 1: 
 
```
Input:
 start = 10, goal = 7

Output:
 3

Explanation:
 The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 101
0
 -> 101
1
.
- Flip the third bit from the right: 1
0
11 -> 1
1
11.
- Flip the fourth bit from the right: 
1
111 -> 
0
111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.
```

 Example 2: 
 
```
Input:
 start = 3, goal = 4

Output:
 3

Explanation:
 The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
- Flip the first bit from the right: 01
1
 -> 01
0
.
- Flip the second bit from the right: 0
1
0 -> 0
0
0.
- Flip the third bit from the right: 
0
00 -> 
1
00.
It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.
```

 Constraints: 

 0 <= start, goal <= 10 9 

 Note: This question is the same as 461: Hamming Distance.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 int minBitFlips(int start,int goal){int x=start^goal,ans=0;while(x){x&=x-1;++ans;}return ans;}
};
```


## 2419. Longest Subarray With Maximum Bitwise AND

**Problem:** https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation, Brainteaser

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of size n . 
 
 Consider a non-empty subarray from nums that has the maximum possible bitwise AND . 

 In other words, let k be the maximum value of the bitwise AND of any subarray of nums . Then, only subarrays with a bitwise AND equal to k should be considered. 

 Return the length of the longest such subarray . 
 
 The bitwise AND of an array is the bitwise AND of all the numbers in it. 
 
 A subarray is a contiguous sequence of elements within an array. 

 Example 1: 
 
```
Input:
 nums = [1,2,3,3,2,2]

Output:
 2

Explanation:

The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
```

 Example 2: 
 
```
Input:
 nums = [1,2,3,4]

Output:
 1

Explanation:

The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int longestSubarray(vector<int>& nums){int mx=*max_element(nums.begin(),nums.end()),cur=0,ans=0;for(int x:nums){cur=x==mx?cur+1:0;ans=max(ans,cur);}return ans;}};
```


## 2425. Bitwise XOR of All Pairings

**Problem:** https://leetcode.com/problems/bitwise-xor-of-all-pairings/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation, Brainteaser

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two 0-indexed arrays, nums1 and nums2 , consisting of non-negative integers. Let there be another array, nums3 , which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once ). 
 
 Return the bitwise XOR of all integers in nums3 . 

 Example 1: 
 
```
Input:
 nums1 = [2,1,3], nums2 = [10,2,5,0]

Output:
 13

Explanation:

A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.
```

 Example 2: 
 
```
Input:
 nums1 = [1,2], nums2 = [3,4]

Output:
 0

Explanation:

All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
```

 Constraints: 

 1 <= nums1.length, nums2.length <= 10 5 
 
 0 <= nums1[i], nums2[j] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int xorAllNums(vector<int>& nums1,vector<int>& nums2){int ans=0;if(nums2.size()%2)for(int x:nums1)ans^=x;if(nums1.size()%2)for(int x:nums2)ans^=x;return ans;}};
```


## 2433. Find The Original Array of Prefix Xor

**Problem:** https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array pref of size n . Find and return the array arr of size n that satisfies : 

 pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i] . 

 Note that ^ denotes the bitwise-xor operation. 
 
 It can be proven that the answer is unique . 

 Example 1: 
 
```
Input:
 pref = [5,2,0,3,1]

Output:
 [5,7,2,3,2]

Explanation:
 From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
```

 Example 2: 
 
```
Input:
 pref = [13]

Output:
 [13]

Explanation:
 We have pref[0] = arr[0] = 13.
```

 Constraints: 

 1 <= pref.length <= 10 5 
 
 0 <= pref[i] <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: vector<int> findArray(vector<int>& pref){vector<int>a=pref;for(int i=(int)a.size()-1;i>0;--i)a[i]=pref[i]^pref[i-1];return a;} };
```


## 2568. Minimum Impossible OR

**Problem:** https://leetcode.com/problems/minimum-impossible-or/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation, Brainteaser

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash set, Ordered set, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 0-indexed  integer array nums . 
 
 We say that an integer x is expressible from nums if there exist some integers 0 <= index 1 < index 2 < ... < index k < nums.length for which nums[index 1 ] | nums[index 2 ] | ... | nums[index k ] = x . In other words, an integer is expressible if it can be written as the bitwise OR of some subsequence of nums . 
 
 Return the minimum positive non-zero integer  that is not expressible from nums . 

 Example 1: 
 
```
Input:
 nums = [2,1]

Output:
 4

Explanation:
 1 and 2 are already present in the array. We know that 3 is expressible, since nums[0] | nums[1] = 2 | 1 = 3. Since 4 is not expressible, we return 4.
```

 Example 2: 
 
```
Input:
 nums = [5,3,2]

Output:
 1

Explanation:
 We can show that 1 is the smallest number that is not expressible.
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int minImpossibleOR(vector<int>& nums) { unordered_set<int> st(nums.begin(),nums.end()); for(int x=1;;x<<=1) if(!st.count(x)) return x; } };
```


## 2595. Number of Even and Odd Bits

**Problem:** https://leetcode.com/problems/number-of-even-and-odd-bits/

**Difficulty:** Easy | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a positive integer n . 
 
 Let even denote the number of even indices in the binary representation of n with value 1. 
 
 Let odd denote the number of odd indices in the binary representation of n with value 1. 
 
 Note that bits are indexed from right to left in the binary representation of a number. 
 
 Return the array [even, odd] . 

 Example 1: 

 Input: n = 50 
 
 Output: [1,2] 
 
 Explanation: 
 
 The binary representation of 50 is 110010 . 
 
 It contains 1 on indices 1, 4, and 5. 

 Example 2: 

 Input: n = 2 
 
 Output: [0,1] 
 
 Explanation: 
 
 The binary representation of 2 is 10 . 
 
 It contains 1 only on index 1. 

 Constraints: 

 1 <= n <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int> evenOddBit(int n){vector<int> ans(2);int i=0;while(n){ans[i&1]+=n&1;n>>=1;i++;}return ans;}};
```


## 2683. Neighboring Bitwise XOR

**Problem:** https://leetcode.com/problems/neighboring-bitwise-xor/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A 0-indexed array derived with length n is derived by computing the bitwise XOR  (⊕) of adjacent values in a binary array original of length n . 
 
 Specifically, for each index i in the range [0, n - 1] : 

 If i = n - 1 , then derived[i] = original[i] ⊕ original[0] . 
 
 Otherwise, derived[i] = original[i] ⊕ original[i + 1] . 

 Given an array derived , your task is to determine whether there exists a valid binary array original that could have formed derived . 
 
 Return true if such an array exists or false otherwise. 

 A binary array is an array containing only 0's and 1's 

 Example 1: 
 
```
Input:
 derived = [1,1,0]

Output:
 true

Explanation:
 A valid original array that gives derived is [0,1,0].
derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1 
derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0
```

 Example 2: 
 
```
Input:
 derived = [1,1]

Output:
 true

Explanation:
 A valid original array that gives derived is [0,1].
derived[0] = original[0] ⊕ original[1] = 1
derived[1] = original[1] ⊕ original[0] = 1
```

 Example 3: 
 
```
Input:
 derived = [1,0]

Output:
 false

Explanation:
 There is no valid original array that gives derived.
```

 Constraints: 

 n == derived.length 
 
 1 <= n <= 10 5 
 
 The values in derived  are either 0's or 1's

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool doesValidArrayExist(vector<int>&derived){int x=0;for(int v:derived)x^=v;return x==0;}};
```


## 2749. Minimum Operations to Make the Integer Zero

**Problem:** https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

**Difficulty:** Medium | **Premium:** No

**Tags:** Bit Manipulation, Brainteaser, Enumeration

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two integers num1 and num2 . 
 
 In one operation, you can choose integer i in the range [0, 60] and subtract 2 i + num2 from num1 . 
 
 Return the integer denoting the minimum number of operations needed to make num1 equal to 0 . 
 
 If it is impossible to make num1 equal to 0 , return -1 . 

 Example 1: 
 
```
Input:
 num1 = 3, num2 = -2

Output:
 3

Explanation:
 We can make 3 equal to 0 with the following operations:
- We choose i = 2 and subtract 2
2
 + (-2) from 3, 3 - (4 + (-2)) = 1.
- We choose i = 2 and subtract 2
2
 + (-2) from 1, 1 - (4 + (-2)) = -1.
- We choose i = 0 and subtract 2
0
 + (-2) from -1, (-1) - (1 + (-2)) = 0.
It can be proven, that 3 is the minimum number of operations that we need to perform.
```

 Example 2: 
 
```
Input:
 num1 = 5, num2 = 7

Output:
 -1

Explanation:
 It can be proven, that it is impossible to make 5 equal to 0 with the given operation.
```

 Constraints: 

 1 <= num1 <= 10 9 
 
 -10 9  <= num2 <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int makeTheIntegerZero(int num1,int num2){for(int k=1;k<=60;++k){long long v=(long long)num1-1LL*k*num2;if(v>=k&&__builtin_popcountll((unsigned long long)v)<=k)return k;}return -1;}};
```


## 2859. Sum of Values at Indices With K Set Bits

**Problem:** https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 0-indexed integer array nums and an integer k . 
 
 Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation. 
 
 The set bits in an integer are the 1 's present when it is written in binary. 

 For example, the binary representation of 21 is 10101 , which has 3 set bits. 

 Example 1: 
 
```
Input:
 nums = [5,10,1,5,2], k = 1

Output:
 13

Explanation:
 The binary representation of the indices are: 
0 = 000
2

1 = 001
2

2 = 010
2

3 = 011
2

4 = 100
2 

Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
Hence, the answer is nums[1] + nums[2] + nums[4] = 13.
```

 Example 2: 
 
```
Input:
 nums = [4,3,2,1], k = 2

Output:
 1

Explanation:
 The binary representation of the indices are:
0 = 00
2

1 = 01
2

2 = 10
2

3 = 11
2

Only index 3 has k = 2 set bits in its binary representation.
Hence, the answer is nums[3] = 1.
```

 Constraints: 

 1 <= nums.length <= 1000 
 
 1 <= nums[i] <= 10 5 
 
 0 <= k <= 10

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:int sumIndicesWithKSetBits(vector<int>& nums,int k){int ans=0;for(int i=0;i<(int)nums.size();++i)if(__builtin_popcount((unsigned)i)==k)ans+=nums[i];return ans;}};
```


## 2917. Find the K-or of an Array

**Problem:** https://leetcode.com/problems/find-the-k-or-of-an-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums , and an integer k . Let's introduce  K-or operation by extending the standard bitwise OR. In K-or, a bit position in the result is set to 1  if at least k numbers in nums have a 1 in that position. 
 
 Return the K-or of nums . 

 Example 1: 

 Input: nums = [7,12,9,8,9,15], k = 4 
 
 Output: 9 
 
 Explanation: 
 
 Represent numbers in binary: 

 Number 
 Bit 3 
 Bit 2 
 Bit 1 
 Bit 0 

 7 
 0 
 1 
 1 
 1 

 12 
 1 
 1 
 0 
 0 

 9 
 1 
 0 
 0 
 1 

 8 
 1 
 0 
 0 
 0 

 9 
 1 
 0 
 0 
 1 

 15 
 1 
 1 
 1 
 1 

 Result = 9 
 1 
 0 
 0 
 1 

 Bit 0 is set in 7, 9, 9, and 15. Bit 3 is set in 12, 9, 8, 9, and 15. 
Only bits 0 and 3 qualify. The result is (1001) 2 = 9 . 

 Example 2: 

 Input: nums = [2,12,1,11,4,5], k = 6 
 
 Output: 0 
 
 Explanation:  No bit appears as 1 in all six array numbers, as required for K-or with k = 6 . Thus, the result is 0. 

 Example 3: 

 Input: nums = [10,8,5,9,11,6,8], k = 1 
 
 Output: 15 
 
 Explanation: Since k == 1 , the 1-or of the array is equal to the bitwise OR of all its elements. Hence, the answer is 10 OR 8 OR 5 OR 9 OR 11 OR 6 OR 8 = 15 . 

 Constraints: 

 1 <= nums.length <= 50 
 
 0 <= nums[i] < 2 31 
 
 1 <= k <= nums.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution{public:int findKOr(vector<int>& nums,int k){int ans=0;for(int b=0;b<31;b++){int c=0;for(int x:nums)c+=(x>>b)&1;if(c>=k)ans|=1<<b;}return ans;}};
```


## 2980. Check if Bitwise OR Has Trailing Zeros

**Problem:** https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array of positive integers nums . 
 
 You have to check if it is possible to select two or more elements in the array such that the bitwise OR of the selected elements has at least one trailing zero in its binary representation. 
 
 For example, the binary representation of 5 , which is "101" , does not have any trailing zeros, whereas the binary representation of 4 , which is "100" , has two trailing zeros. 
 
 Return true if it is possible to select two or more elements whose bitwise OR has trailing zeros, return false otherwise . 

 Example 1: 
 
```
Input:
 nums = [1,2,3,4,5]

Output:
 true

Explanation:
 If we select the elements 2 and 4, their bitwise OR is 6, which has the binary representation "110" with one trailing zero.
```

 Example 2: 
 
```
Input:
 nums = [2,4,8,16]

Output:
 true

Explanation: 
If we select the elements 2 and 4, their bitwise OR is 6, which has the binary representation "110" with one trailing zero.
Other possible ways to select elements to have trailing zeroes in the binary representation of their bitwise OR are: (2, 8), (2, 16), (4, 8), (4, 16), (8, 16), (2, 4, 8), (2, 4, 16), (2, 8, 16), (4, 8, 16), and (2, 4, 8, 16).
```

 Example 3: 
 
```
Input:
 nums = [1,3,5,7,9]

Output:
 false

Explanation:
 There is no possible way to select two or more elements to have trailing zeros in the binary representation of their bitwise OR.
```

 Constraints: 

 2 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool hasTrailingZeros(vector<int>& nums){int c=0;for(int x:nums)c+=(x%2==0);return c>=2;}};
```


## 2997. Minimum Number of Operations to Make Array XOR Equal to K

**Problem:** https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 0-indexed integer array nums and a positive integer k . 
 
 You can apply the following operation on the array any number of times: 

 Choose any element of the array and flip a bit in its binary representation. Flipping a bit means changing a 0 to 1 or vice versa. 

 Return the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to k . 
 
 Note that you can flip leading zero bits in the binary representation of elements. For example, for the number (101) 2 you can flip the fourth bit and obtain (1101) 2 . 

 Example 1: 
 
```
Input:
 nums = [2,1,3,4], k = 1

Output:
 2

Explanation:
 We can do the following operations:
- Choose element 2 which is 3 == (011)
2
, we flip the first bit and we obtain (010)
2
 == 2. nums becomes [2,1,2,4].
- Choose element 0 which is 2 == (010)
2
, we flip the third bit and we obtain (110)
2
 = 6. nums becomes [6,1,2,4].
The XOR of elements of the final array is (6 XOR 1 XOR 2 XOR 4) == 1 == k.
It can be shown that we cannot make the XOR equal to k in less than 2 operations.
```

 Example 2: 
 
```
Input:
 nums = [2,0,2,0], k = 0

Output:
 0

Explanation:
 The XOR of elements of the array is (2 XOR 0 XOR 2 XOR 0) == 0 == k. So no operation is needed.
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 0 <= nums[i] <= 10 6 
 
 0 <= k <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int minOperations(vector<int>& nums,int k){for(int x:nums)k^=x;return __builtin_popcount((unsigned)k);}};
```


## 3064. Guess the Number Using Bitwise Questions I

**Problem:** https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Bit Manipulation, Interactive

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There is a number n that you have to find. 
 
 There is also a pre-defined API int commonSetBits(int num) , which returns the number of bits where both n and num are 1 in that position of their binary representation. In other words, it returns the number of set bits in n & num , where & is the bitwise AND operator. 
 
 Return the number n . 

 Example 1: 

 Input: n = 31 
 
 Output: 31 
 
 Explanation: It can be proven that it's possible to find 31 using the provided API. 

 Example 2: 

 Input: n = 33 
 
 Output: 33 
 
 Explanation: It can be proven that it's possible to find 33 using the provided API. 

 Constraints: 

 1 <= n <= 2 30 - 1 
 
 0 <= num <= 2 30 - 1 
 
 If you ask for some num out of the given range, the output wouldn't be reliable.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int findNumber() {
        int ans=0;
        for (int bit=0;bit<30;++bit)
            if (commonSetBits(1<<bit)) ans|=1<<bit;
        return ans;
    }
};
```


## 3094. Guess the Number Using Bitwise Questions II

**Problem:** https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Bit Manipulation, Interactive

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There is a number n between 0 and 2 30 - 1 (both inclusive) that you have to find. 
 
 There is a pre-defined API int commonBits(int num) that helps you with your mission. But here is the challenge, every time you call this function, n changes in some way. But keep in mind, that you have to find the initial value of n . 
 
 commonBits(int num) acts as follows: 

 Calculate count which is the number of bits where both n and num have the same value in that position of their binary representation. 
 
 n = n XOR num 
 
 Return count . 

 Return the number n . 
 
 Note: In this world, all numbers are between 0 and 2 30 - 1 (both inclusive), thus for counting common bits, we see only the first 30 bits of those numbers. 

 Constraints: 

 0 <= n <= 2 30 - 1 
 
 0 <= num <= 2 30 - 1 
 
 If you ask for some num out of the given range, the output wouldn't be reliable.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int findNumber(){int z=commonBits(0),ones=0,ans=0;for(int i=0;i<29;++i){int baseline=z+2*ones-i;int q=commonBits(1<<i);if(q==baseline+1){ans|=1<<i;++ones;}}if(30-z-ones)ans|=1<<29;return ans;}};
```


## 3133. Minimum Array End

**Problem:** https://leetcode.com/problems/minimum-array-end/

**Difficulty:** Medium | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two integers n and x . You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1 , nums[i + 1] is greater than nums[i] , and the result of the bitwise AND operation between all elements of nums is x . 
 
 Return the minimum possible value of nums[n - 1] . 

 Example 1: 

 Input: n = 3, x = 4 
 
 Output: 6 
 
 Explanation: 
 
 nums can be [4,5,6] and its last element is 6. 

 Example 2: 

 Input: n = 2, x = 7 
 
 Output: 15 
 
 Explanation: 
 
 nums can be [7,15] and its last element is 15. 

 Constraints: 

 1 <= n, x <= 10 8

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:long long minEnd(int n,int x){long long v=(long long)n-1,ans=x;for(int b=0;v;++b)if(((ans>>b)&1LL)==0){if(v&1)ans|=1LL<<b;v>>=1;}return ans;}};
```


## 3173. Bitwise OR of Adjacent Elements

**Problem:** https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array nums of length n , return an array answer of length n - 1 such that answer[i] = nums[i] | nums[i + 1] where | is the bitwise OR operation. 

 Example 1: 

 Input: nums = [1,3,7,15] 
 
 Output: [3,7,15] 

 Example 2: 

 Input: nums = [8,4,2] 
 
 Output: [12,6] 

 Example 3: 

 Input: nums = [5,4,9,11] 
 
 Output: [5,13,11] 

 Constraints: 

 2 <= nums.length <= 100 
 
 0 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> orArray(vector<int>& nums) {
        vector<int> ans;
        for (int i = 1; i < (int)nums.size(); ++i) ans.push_back(nums[i - 1] | nums[i]);
        return ans;
    }
};
```


## 3199. Count Triplets with Even XOR Set Bits I

**Problem:** https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given three integer arrays a , b , and c , return the number of triplets (a[i], b[j], c[k]) , such that the bitwise XOR of the elements of each triplet has an even number of set bits .

 Example 1: 

 Input: a = [1], b = [2], c = [3] 
 
 Output: 1 
 
 Explanation: 
 
 The only triplet is (a[0], b[0], c[0]) and their XOR is: 1 XOR 2 XOR 3 = 00 2 . 

 Example 2: 

 Input: a = [1,1], b = [2,3], c = [1,5] 
 
 Output: 4 
 
 Explanation: 
 
 Consider these four triplets: 

 (a[0], b[1], c[0]) : 1 XOR 3 XOR 1 = 011 2 
 
 (a[1], b[1], c[0]) : 1 XOR 3 XOR 1 = 011 2 
 
 (a[0], b[0], c[1]) : 1 XOR 2 XOR 5 = 110 2 
 
 (a[1], b[0], c[1]) : 1 XOR 2 XOR 5 = 110 2 

 Constraints: 

 1 <= a.length, b.length, c.length <= 100 
 
 0 <= a[i], b[i], c[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int tripletCount(vector<int>& a, vector<int>& b, vector<int>& c) {
        auto parityCounts = [](const vector<int>& v) {
            array<long long, 2> cnt = {{0, 0}};
            for (int x : v) {
                int parity = __builtin_parity((unsigned)x);
                ++cnt[parity];
            }
            return cnt;
        };
        auto A = parityCounts(a), B = parityCounts(b), C = parityCounts(c);
        long long answer = 0;
        for (int i = 0; i < 2; ++i)
            for (int j = 0; j < 2; ++j)
                answer += A[i] * B[j] * C[i ^ j];
        return (int)answer;
    }
};
```


## 3215. Count Triplets with Even XOR Set Bits II

**Problem:** https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given three integer arrays a , b , and c , return the number of triplets (a[i], b[j], c[k]) , such that the bitwise XOR between the elements of each triplet has an even number of set bits .

 Example 1: 

 Input: a = [1], b = [2], c = [3] 
 
 Output: 1 
 
 Explanation: 
 
 The only triplet is (a[0], b[0], c[0]) and their XOR is: 1 XOR 2 XOR 3 = 00 2 . 

 Example 2: 

 Input: a = [1,1], b = [2,3], c = [1,5] 
 
 Output: 4 
 
 Explanation: 
 
 Consider these four triplets: 

 (a[0], b[1], c[0]) : 1 XOR 3 XOR 1 = 011 2 
 
 (a[1], b[1], c[0]) : 1 XOR 3 XOR 1 = 011 2 
 
 (a[0], b[0], c[1]) : 1 XOR 2 XOR 5 = 110 2 
 
 (a[1], b[0], c[1]) : 1 XOR 2 XOR 5 = 110 2 

 Constraints: 

 1 <= a.length, b.length, c.length <= 10 5 
 
 0 <= a[i], b[i], c[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    long long tripletCount(vector<int>& a,vector<int>& b,vector<int>& c) {
        long long A[2]={},B[2]={},C[2]={};
        for (int x:a) ++A[__builtin_parity((unsigned)x)];
        for (int x:b) ++B[__builtin_parity((unsigned)x)];
        for (int x:c) ++C[__builtin_parity((unsigned)x)];
        return A[0]*B[0]*C[0]+A[0]*B[1]*C[1]
             + A[1]*B[0]*C[1]+A[1]*B[1]*C[0];
    }
};
```


## 3226. Number of Bit Changes to Make Two Integers Equal

**Problem:** https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

**Difficulty:** Easy | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two positive integers n and k . 
 
 You can choose any bit in the binary representation of n that is equal to 1 and change it to 0. 
 
 Return the number of changes needed to make n equal to k . If it is impossible, return -1. 

 Example 1: 

 Input: n = 13, k = 4 
 
 Output: 2 
 
 Explanation: 
Initially, the binary representations of n and k are n = (1101) 2 and k = (0100) 2 . 
We can change the first and fourth bits of n . The resulting integer is n = ( 0 10 0 ) 2 = k . 

 Example 2: 

 Input: n = 21, k = 21 
 
 Output: 0 
 
 Explanation: 
 n and k are already equal, so no changes are needed. 

 Example 3: 

 Input: n = 14, k = 13 
 
 Output: -1 
 
 Explanation: 
It is not possible to make n equal to k . 

 Constraints: 

 1 <= n, k <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int minChanges(int n,int k) { if((n&k)!=k) return -1; return __builtin_popcount((unsigned)(n^k)); } };
```


## 3309. Maximum Possible Number by Binary Concatenation

**Problem:** https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation, Enumeration

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array of integers nums of size 3. 
 
 Return the maximum possible number whose binary representation can be formed by concatenating the binary representation of all elements in nums in some order. 
 
 Note that the binary representation of any number does not contain leading zeros. 

 Example 1: 

 Input: nums = [1,2,3] 
 
 Output: 30 
 
 Explanation: 
 
 Concatenate the numbers in the order [3, 1, 2] to get the result "11110" , which is the binary representation of 30. 

 Example 2: 

 Input: nums = [2,8,16] 
 
 Output: 1296 
 
 Explanation: 
 
 Concatenate the numbers in the order [2, 8, 16] to get the result "10100010000" , which is the binary representation of 1296. 

 Constraints: 

 nums.length == 3 
 
 1 <= nums[i] <= 127

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int maxGoodNumber(vector<int>&nums){sort(nums.begin(),nums.end());int best=0;do{int v=0;for(int x:nums){int bits=32-__builtin_clz((unsigned)x);v=(v<<bits)|x;}best=max(best,v);}while(next_permutation(nums.begin(),nums.end()));return best;} };
```


## 3314. Construct the Minimum Bitwise Array I

**Problem:** https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array nums consisting of n prime integers. 
 
 You need to construct an array ans of length n , such that, for each index i , the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i] , i.e. ans[i] OR (ans[i] + 1) == nums[i] . 
 
 Additionally, you must minimize each value of ans[i] in the resulting array. 
 
 If it is not possible to find such a value for ans[i] that satisfies the condition , then set ans[i] = -1 . 

 Example 1: 

 Input: nums = [2,3,5,7] 
 
 Output: [-1,1,4,3] 
 
 Explanation: 

 For i = 0 , as there is no value for ans[0] that satisfies ans[0] OR (ans[0] + 1) = 2 , so ans[0] = -1 . 
 
 For i = 1 , the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 3 is 1 , because 1 OR (1 + 1) = 3 . 
 
 For i = 2 , the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 5 is 4 , because 4 OR (4 + 1) = 5 . 
 
 For i = 3 , the smallest ans[3] that satisfies ans[3] OR (ans[3] + 1) = 7 is 3 , because 3 OR (3 + 1) = 7 . 

 Example 2: 

 Input: nums = [11,13,31] 
 
 Output: [9,12,15] 
 
 Explanation: 

 For i = 0 , the smallest ans[0] that satisfies ans[0] OR (ans[0] + 1) = 11 is 9 , because 9 OR (9 + 1) = 11 . 
 
 For i = 1 , the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 13 is 12 , because 12 OR (12 + 1) = 13 . 
 
 For i = 2 , the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 31 is 15 , because 15 OR (15 + 1) = 31 . 

 Constraints: 

 1 <= nums.length <= 100 
 
 2 <= nums[i] <= 1000 
 
 nums[i] is a prime number.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: vector<int> minBitwiseArray(vector<int>&nums){vector<int>a;for(int x:nums){if(x==2){a.push_back(-1);continue;}int b=0;while(x&(1LL<<b))++b;a.push_back(x^(1<<(b-1)));}return a;} };
```


## 3315. Construct the Minimum Bitwise Array II

**Problem:** https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array nums consisting of n prime integers. 
 
 You need to construct an array ans of length n , such that, for each index i , the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i] , i.e. ans[i] OR (ans[i] + 1) == nums[i] . 
 
 Additionally, you must minimize each value of ans[i] in the resulting array. 
 
 If it is not possible to find such a value for ans[i] that satisfies the condition , then set ans[i] = -1 . 

 Example 1: 

 Input: nums = [2,3,5,7] 
 
 Output: [-1,1,4,3] 
 
 Explanation: 

 For i = 0 , as there is no value for ans[0] that satisfies ans[0] OR (ans[0] + 1) = 2 , so ans[0] = -1 . 
 
 For i = 1 , the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 3 is 1 , because 1 OR (1 + 1) = 3 . 
 
 For i = 2 , the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 5 is 4 , because 4 OR (4 + 1) = 5 . 
 
 For i = 3 , the smallest ans[3] that satisfies ans[3] OR (ans[3] + 1) = 7 is 3 , because 3 OR (3 + 1) = 7 . 

 Example 2: 

 Input: nums = [11,13,31] 
 
 Output: [9,12,15] 
 
 Explanation: 

 For i = 0 , the smallest ans[0] that satisfies ans[0] OR (ans[0] + 1) = 11 is 9 , because 9 OR (9 + 1) = 11 . 
 
 For i = 1 , the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 13 is 12 , because 12 OR (12 + 1) = 13 . 
 
 For i = 2 , the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 31 is 15 , because 15 OR (15 + 1) = 31 . 

 Constraints: 

 1 <= nums.length <= 100 
 
 2 <= nums[i] <= 10 9 
 
 nums[i] is a prime number.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: vector<int> minBitwiseArray(vector<int>&nums){vector<int>a;for(int x:nums){if(x==2){a.push_back(-1);continue;}int b=0;while(x&(1LL<<b))++b;a.push_back(x^(1<<(b-1)));}return a;} };
```


## 3566. Partition Array into Two Equal Product Subsets

**Problem:** https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation, Recursion, Enumeration

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums containing distinct positive integers and an integer target . 
 
 Determine if you can partition nums into two non-empty disjoint subsets , with each element belonging to exactly one subset, such that the product of the elements in each subset is equal to target . 
 
 Return true if such a partition exists and false otherwise. 
A subset of an array is a selection of elements of the array.

 Example 1: 

 Input: nums = [3,1,6,8,4], target = 24 
 
 Output: true 
 
 Explanation: The subsets [3, 8] and [1, 6, 4] each have a product of 24. Hence, the output is true. 

 Example 2: 

 Input: nums = [2,5,3,7], target = 15 
 
 Output: false 
 
 Explanation: There is no way to partition nums into two non-empty disjoint subsets such that both subsets have a product of 15. Hence, the output is false. 

 Constraints: 

 3 <= nums.length <= 12 
 
 1 <= target <= 10 15 
 
 1 <= nums[i] <= 100 
 
 All elements of nums are distinct .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:
 bool checkEqualPartitions(vector<int>& nums,long long target){
  int n=nums.size();
  for(int mask=1;mask<(1<<n)-1;++mask){
   long long a=1,b=1;
   for(int i=0;i<n;++i){long long &p=(mask>>i&1)?a:b;if(p<=target)p*=nums[i];}
   if(a==target&&b==target)return true;
  }
  return false;
 }
};
```


## 3595. Once Twice

**Problem:** https://leetcode.com/problems/once-twice/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . In this array: 

 Exactly one element appears once . 

 Exactly one element appears twice . 

 All other elements appear exactly three times . 

 Return an integer array of length 2, where the first element is the one that appears once , and the second is the one that appears twice . 
 
 Your solution must run in O(n) time and O(1) space. 

 Example 1: 

 Input: nums = [2,2,3,2,5,5,5,7,7] 
 
 Output: [3,7] 
 
 Explanation: 
 
 The element 3 appears once , and the element 7 appears twice . The remaining elements each appear three times . 

 Example 2: 

 Input: nums = [4,4,6,4,9,9,9,6,8] 
 
 Output: [8,6] 
 
 Explanation: 
 
 The element 8 appears once , and the element 6 appears twice . The remaining elements each appear three times . 

 Constraints: 

 3 <= nums.length <= 10 5 
 
 -2 31 <= nums[i] <= 2 31 - 1 
 
 nums.length is a multiple of 3. 
 
 Exactly one element appears once, one element appears twice, and all other elements appear three times.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> onceTwice(vector<int>& nums) {
        uint32_t one = 0, two = 0;
        for (int x : nums) {
            uint32_t v = static_cast<uint32_t>(x);
            uint32_t newOne = (one ^ v) & ~two;
            uint32_t newTwo = (two ^ v) & ~newOne;
            one = newOne;
            two = newTwo;
        }
        uint32_t diff = one ^ two;
        uint32_t bit = diff & (~diff + 1u);
        uint32_t a = 0, b = 0;
        // For the distinguishing bit, one appears once and two appears twice.
        // Residual ternary counters for each partition identify the numbers.
        uint32_t aOne = 0, aTwo = 0, bOne = 0, bTwo = 0;
        for (int x : nums) {
            uint32_t v = static_cast<uint32_t>(x);
            uint32_t &o = (v & bit) ? aOne : bOne;
            uint32_t &t = (v & bit) ? aTwo : bTwo;
            uint32_t no = (o ^ v) & ~t;
            uint32_t nt = (t ^ v) & ~no;
            o = no;
            t = nt;
        }
        if (aOne & bit) { a = aOne; b = bTwo; }
        else { a = bOne; b = aTwo; }
        return {static_cast<int>(a), static_cast<int>(b)};
    }
};
```


## 3644. Maximum K to Sort a Permutation

**Problem:** https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of length n , where nums is a permutation of the numbers in the range [0..n - 1] . 
 
 You may swap elements at indices i and j only if nums[i] AND nums[j] == k , where AND denotes the bitwise AND operation and k is a non-negative integer. 
 
 Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. If nums is already sorted, return 0. 

 Example 1: 

 Input: nums = [0,3,2,1] 
 
 Output: 1 
 
 Explanation: 
 
 Choose k = 1 . Swapping nums[1] = 3 and nums[3] = 1 is allowed since nums[1] AND nums[3] == 1 , resulting in a sorted permutation: [0, 1, 2, 3] . 

 Example 2: 

 Input: nums = [0,1,3,2] 
 
 Output: 2 
 
 Explanation: 
 
 Choose k = 2 . Swapping nums[2] = 3 and nums[3] = 2 is allowed since nums[2] AND nums[3] == 2 , resulting in a sorted permutation: [0, 1, 2, 3] . 

 Example 3: 

 Input: nums = [3,2,1,0] 
 
 Output: 0 
 
 Explanation: 
 
 Only k = 0 allows sorting since no greater k allows the required swaps where nums[i] AND nums[j] == k . 

 Constraints: 

 1 <= n == nums.length <= 10 5 
 
 0 <= nums[i] <= n - 1 
 
 nums is a permutation of integers from 0 to n - 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 int sortPermutation(vector<int>& nums){int ans=-1;for(int i=0;i<(int)nums.size();++i)if(nums[i]!=i)ans&=nums[i];return ans==-1?0:ans;}
};
```


## 3674. Minimum Operations to Equalize Array

**Problem:** https://leetcode.com/problems/minimum-operations-to-equalize-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Bit Manipulation, Brainteaser

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of length n . 
 
 In one operation, choose any subarray nums[l...r] ( 0 <= l <= r < n ) and replace each element in that subarray with the bitwise AND of all elements. 
 
 Return the minimum number of operations required to make all elements of nums equal. 
A subarray is a contiguous non-empty sequence of elements within an array.

 Example 1: 

 Input: nums = [1,2] 
 
 Output: 1 
 
 Explanation: 
 
 Choose nums[0...1] : (1 AND 2) = 0 , so the array becomes [0, 0] and all elements are equal in 1 operation. 

 Example 2: 

 Input: nums = [5,5,5] 
 
 Output: 0 
 
 Explanation: 
 
 nums is [5, 5, 5] which already has all elements equal, so 0 operations are required. 

 Constraints: 

 1 <= n == nums.length <= 100 
 
 1 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int minOperations(vector<int>& nums){for(int x:nums)if(x!=nums[0])return 1;return 0;} };
```


## 3688. Bitwise OR of Even Numbers in an Array

**Problem:** https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Bit Manipulation, Simulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . 
 
 Return the bitwise OR of all even numbers in the array. 
 
 If there are no even numbers in nums , return 0. 

 Example 1: 

 Input: nums = [1,2,3,4,5,6] 
 
 Output: 6 
 
 Explanation: 
 
 The even numbers are 2, 4, and 6. Their bitwise OR equals 6. 

 Example 2: 

 Input: nums = [7,9,11] 
 
 Output: 0 
 
 Explanation: 
 
 There are no even numbers, so the result is 0. 

 Example 3: 

 Input: nums = [1,8,16] 
 
 Output: 24 
 
 Explanation: 
 
 The even numbers are 8 and 16. Their bitwise OR equals 24. 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int evenNumberBitwiseORs(vector<int>& nums){int ans=0;for(int x:nums)if(x%2==0)ans|=x;return ans;} };
```


## 3702. Longest Subsequence With Non-Zero Bitwise XOR

**Problem:** https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . 
 
 Return the length of the longest subsequence in nums whose bitwise XOR is non-zero . If no such subsequence exists, return 0. 

 Example 1: 

 Input: nums = [1,2,3] 
 
 Output: 2 
 
 Explanation: 
 
 One longest subsequence is [2, 3] . The bitwise XOR is computed as 2 XOR 3 = 1 , which is non-zero. 

 Example 2: 

 Input: nums = [2,3,4] 
 
 Output: 3 
 
 Explanation: 
 
 The longest subsequence is [2, 3, 4] . The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5 , which is non-zero. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 0 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public: int longestSubsequence(vector<int>& nums) {int x=0;for(int v:nums)x^=v;if(x)return nums.size();for(int v:nums)if(v)return nums.size()-1;return 0;}};
```


## 3827. Count Monobit Integers

**Problem:** https://leetcode.com/problems/count-monobit-integers/

**Difficulty:** Easy | **Premium:** No

**Tags:** Bit Manipulation, Enumeration

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer n . 
 
 An integer is called Monobit if all bits in its binary representation are the same. 
 
 Return the count of Monobit integers in the range [0, n] (inclusive). 

 Example 1: 

 Input: n = 1 
 
 Output: 2 
 
 Explanation: 

 The integers in the range [0, 1] have binary representations "0" and "1" . 
 
 Each representation consists of identical bits. Thus, the answer is 2. 

 Example 2: 

 Input: n = 4 
 
 Output: 3 
 
 Explanation: 

 The integers in the range [0, 4] include binaries "0" , "1" , "10" , "11" , and "100" . 
 
 Only 0, 1 and 3 satisfy the Monobit condition. Thus, the answer is 3. 

 Constraints: 

 0 <= n <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int countMonobit(int n) {
        int ans=1;
        long long x=1;
        while(x<=n){ ++ans; x=(x<<1)|1; }
        return ans;
    }
};
```


## 3950. Exactly One Consecutive Set Bits Pair

**Problem:** https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

**Difficulty:** Easy | **Premium:** No

**Tags:** Bit Manipulation

**Primary pattern:** Bit Manipulation

**Related patterns:** Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Use XOR, bit masks, bit positions, or binary representation.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer n . 
 
 Return true if its binary representation contains exactly one adjacent pair of  set bits , and false otherwise. 

 Example 1: 

 Input: n = 6 
 
 Output: true 
 
 Explanation: 

 Binary representation of 6 is 110 . 
 
 There is exactly one adjacent pair of set bits ( "11" ). Thus, the answer is true ​​​​​​​. 

 Example 2: 

 Input: n = 5 
 
 Output: false 
 
 Explanation: 

 Binary representation of 5 is 101 . 
 
 There is no adjacent pair of set bits. Thus, the answer is false ​​​​​​​. 

 Constraints: 

 0 <= n <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool consecutiveSetBits(int n) {
        int pairs = 0;
        while (n > 1) {
            if ((n & 3) == 3) ++pairs;
            n >>= 1;
        }
        return pairs == 1;
    }
};
```

