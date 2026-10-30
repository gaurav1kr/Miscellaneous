# Sorting / Divide and Conquer

**Problems:** 46

## Quick revision checklist

Order elements to expose structure or split into manageable halves.

## Problem index

- [56. Merge Intervals](#56-merge-intervals) — Medium; code: yes
- [147. Insertion Sort List](#147-insertion-sort-list) — Medium; code: yes
- [164. Maximum Gap](#164-maximum-gap) — Medium; code: yes
- [190. Reverse Bits](#190-reverse-bits) — Easy; code: yes
- [191. Number of 1 Bits](#191-number-of-1-bits) — Easy; code: yes
- [252. Meeting Rooms](#252-meeting-rooms) — Easy; code: yes
- [274. H-Index](#274-h-index) — Medium; code: yes
- [414. Third Maximum Number](#414-third-maximum-number) — Easy; code: yes
- [747. Largest Number At Least Twice of Others](#747-largest-number-at-least-twice-of-others) — Easy; code: yes
- [950. Reveal Cards In Increasing Order](#950-reveal-cards-in-increasing-order) — Medium; code: yes
- [1051. Height Checker](#1051-height-checker) — Easy; code: yes
- [1200. Minimum Absolute Difference](#1200-minimum-absolute-difference) — Easy; code: yes
- [1274. Number of Ships in a Rectangle](#1274-number-of-ships-in-a-rectangle) — Hard; code: yes
- [1288. Remove Covered Intervals](#1288-remove-covered-intervals) — Medium; code: yes
- [1329. Sort the Matrix Diagonally](#1329-sort-the-matrix-diagonally) — Medium; code: yes
- [1333. Filter Restaurants by Vegan-Friendly, Price and Distance](#1333-filter-restaurants-by-vegan-friendly-price-and-distance) — Medium; code: yes
- [1491. Average Salary Excluding the Minimum and Maximum Salary](#1491-average-salary-excluding-the-minimum-and-maximum-salary) — Easy; code: yes
- [1502. Can Make Arithmetic Progression From Sequence](#1502-can-make-arithmetic-progression-from-sequence) — Easy; code: yes
- [1619. Mean of Array After Removing Some Elements](#1619-mean-of-array-after-removing-some-elements) — Easy; code: yes
- [1637. Widest Vertical Area Between Two Points Containing No Points](#1637-widest-vertical-area-between-two-points-containing-no-points) — Easy; code: yes
- [1756. Design Most Recently Used Queue](#1756-design-most-recently-used-queue) — Medium; code: yes
- [1887. Reduction Operations to Make the Array Elements Equal](#1887-reduction-operations-to-make-the-array-elements-equal) — Medium; code: yes
- [1913. Maximum Product Difference Between Two Pairs](#1913-maximum-product-difference-between-two-pairs) — Easy; code: yes
- [2164. Sort Even and Odd Indices Independently](#2164-sort-even-and-odd-indices-independently) — Easy; code: yes
- [2191. Sort the Jumbled Numbers](#2191-sort-the-jumbled-numbers) — Medium; code: yes
- [2274. Maximum Consecutive Floors Without Special Floors](#2274-maximum-consecutive-floors-without-special-floors) — Medium; code: yes
- [2545. Sort the Students by Their Kth Score](#2545-sort-the-students-by-their-kth-score) — Medium; code: yes
- [2580. Count Ways to Group Overlapping Ranges](#2580-count-ways-to-group-overlapping-ranges) — Medium; code: yes
- [2655. Find Maximal Uncovered Ranges](#2655-find-maximal-uncovered-ranges) — Medium; code: yes
- [2733. Neither Minimum nor Maximum](#2733-neither-minimum-nor-maximum) — Easy; code: yes
- [2740. Find the Value of the Partition](#2740-find-the-value-of-the-partition) — Medium; code: yes
- [2751. Robot Collisions](#2751-robot-collisions) — Hard; code: yes
- [2860. Happy Students](#2860-happy-students) — Medium; code: yes
- [2943. Maximize Area of Square Hole in Grid](#2943-maximize-area-of-square-hole-in-grid) — Medium; code: yes
- [3010. Divide an Array Into Subarrays With Minimum Cost I](#3010-divide-an-array-into-subarrays-with-minimum-cost-i) — Easy; code: yes
- [3011. Find if Array Can Be Sorted](#3011-find-if-array-can-be-sorted) — Medium; code: yes
- [3169. Count Days Without Meetings](#3169-count-days-without-meetings) — Medium; code: yes
- [3394. Check if Grid can be Cut into Sections](#3394-check-if-grid-can-be-cut-into-sections) — Medium; code: yes
- [3446. Sort Matrix by Diagonals](#3446-sort-matrix-by-diagonals) — Medium; code: yes
- [3537. Fill a Special Grid](#3537-fill-a-special-grid) — Medium; code: yes
- [3567. Minimum Absolute Difference in Sliding Submatrix](#3567-minimum-absolute-difference-in-sliding-submatrix) — Medium; code: yes
- [3631. Sort Threats by Severity and Exploitability](#3631-sort-threats-by-severity-and-exploitability) — Medium; code: yes
- [3769. Sort Integers by Binary Reflection](#3769-sort-integers-by-binary-reflection) — Easy; code: yes
- [3774. Absolute Difference Between Maximum and Minimum K Elements](#3774-absolute-difference-between-maximum-and-minimum-k-elements) — Easy; code: yes
- [3951. Minimum Energy to Maintain Brightness](#3951-minimum-energy-to-maintain-brightness) — Medium; code: yes
- [3975. Filter Occupied Intervals](#3975-filter-occupied-intervals) — Medium; code: yes

---

## 56. Merge Intervals

**Problem:** https://leetcode.com/problems/merge-intervals/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Quicksort

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n) output; O(log n) sort stack

**Complexity reasoning:** Sorts the intervals, then merges them in one pass; the result stores up to n intervals.

### Problem description

Given an array of intervals  where intervals[i] = [start i , end i ] , merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input . 

 Example 1: 
 
```
Input:
 intervals = [[1,3],[2,6],[8,10],[15,18]]

Output:
 [[1,6],[8,10],[15,18]]

Explanation:
 Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

 Example 2: 
 
```
Input:
 intervals = [[1,4],[4,5]]

Output:
 [[1,5]]

Explanation:
 Intervals [1,4] and [4,5] are considered overlapping.
```

 Example 3: 
 
```
Input:
 intervals = [[4,7],[1,4]]

Output:
 [[1,7]]

Explanation:
 Intervals [1,4] and [4,7] are considered overlapping.
```

 Constraints: 

 1 <= intervals.length <= 10 4 
 
 intervals[i].length == 2 
 
 0 <= start i <= end i <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) 
    {
        vector<vector<int>> result ;
        size_t interval_size = intervals.size() ;
        sort(intervals.begin() , intervals.end()) ;
        for(int i=0;i<interval_size;i++)
        {
            if(result.empty() || (result.back()[1]<intervals[i][0]) )
            {
                vector<int> v = {intervals[i][0] , intervals[i][1]} ;
                result.push_back(v) ;
            }
            else
            {
                result.back()[1] = max(result.back()[1] , intervals[i][1]) ;
            }
        }
        return result ;
    }
};
```


## 147. Insertion Sort List

**Problem:** https://leetcode.com/problems/insertion-sort-list/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Linked List / Pointers

**Data structures (inferred):** Linked list, Sorted array

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Each node scans the already sorted prefix to find its insertion position; links are rearranged in place with one dummy node.

### Problem description

Given the head of a singly linked list, sort the list using insertion sort , and return the sorted list's head . 
 
 The steps of the insertion sort algorithm: 

 Insertion sort iterates, consuming one input element each repetition and growing a sorted output list. 
 
 At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there. 
 
 It repeats until no input elements remain. 

 The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration. 
 [Figure: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif] 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/03/04/sort1linked-list.jpg] 
 
```
Input:
 head = [4,2,1,3]

Output:
 [1,2,3,4]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/03/04/sort2linked-list.jpg] 
 
```
Input:
 head = [-1,5,3,4,0]

Output:
 [-1,0,3,4,5]
```

 Constraints: 

 The number of nodes in the list is in the range [1, 5000] . 
 
 -5000 <= Node.val <= 5000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution 
{
public:
    ListNode* insertionSortList(ListNode* head) 
    {
        if (head == nullptr) 
        {
            return head;
        }

        ListNode* helper = new ListNode(0); 
        ListNode* cur = head; 
        ListNode* pre = helper; 
        ListNode* next = nullptr; 

        
        while (cur != nullptr) 
        {
            next = cur->next;
            
            while (pre->next != nullptr && pre->next->val < cur->val) 
            {
                pre = pre->next;
            }
            
            cur->next = pre->next;
            pre->next = cur;
            pre = helper;
            cur = next;
        }

        return helper->next;
    }
};
```


## 164. Maximum Gap

**Problem:** https://leetcode.com/problems/maximum-gap/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Bucket Sort, Radix Sort, Pigeonhole Principle

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** The implementation calls std::sort and then scans adjacent sorted values once; it does not use the linear-time bucket method.

### Problem description

Given an integer array nums , return the maximum difference between two successive elements in its sorted form . If the array contains less than two elements, return 0 . 
 
 You must write an algorithm that runs in linear time and uses linear extra space. 

 Example 1: 
 
```
Input:
 nums = [3,6,9,1]

Output:
 3

Explanation:
 The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
```

 Example 2: 
 
```
Input:
 nums = [10]

Output:
 0

Explanation:
 The array contains less than 2 elements, therefore return 0.
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 0 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    int maximumGap(vector<int>& nums) 
    {
        int size_nums = nums.size() ;
        sort(nums.begin() , nums.end()) ;
        int max = INT_MIN ;
        for(int i=0;i<size_nums-1;i++)
        {
            max = (nums[i+1] - nums[i]) > max ?  (nums[i+1] - nums[i]) : max ;
        }
        return (max==INT_MIN)?0:max ;
    }
};
```


## 190. Reverse Bits

**Problem:** https://leetcode.com/problems/reverse-bits/

**Difficulty:** Easy | **Premium:** No

**Tags:** Divide and Conquer, Bit Manipulation

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** The loop always processes exactly 32 bits using shifts and masks.

### Problem description

Reverse bits of a given 32 bits signed integer. 

 Example 1: 

 Input: n = 43261596 
 
 Output: 964176192 
 
 Explanation: 

 Integer 
 Binary 

 43261596 
 00000010100101000001111010011100 

 964176192 
 00111001011110000010100101000000 

 Example 2: 

 Input: n = 2147483644 
 
 Output: 1073741822 
 
 Explanation: 

 Integer 
 Binary 

 2147483644 
 01111111111111111111111111111100 

 1073741822 
 00111111111111111111111111111110 

 Constraints: 

 0 <= n <= 2 31 - 2 
 
 n is even. 

 Follow up: If this function is called many times, how would you optimize it?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        for (int i = 0; i < 32; ++i) {
            result = (result << 1) | (n & 1);
            n >>= 1;
        }
        return result;
    }
};
```


## 191. Number of 1 Bits

**Problem:** https://leetcode.com/problems/number-of-1-bits/

**Difficulty:** Easy | **Premium:** No

**Tags:** Divide and Conquer, Bit Manipulation

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1) for 32-bit integers

**Space complexity:** O(1)

**Complexity reasoning:** At most 32 iterations shift n right and count the least significant bit.

### Problem description

Given a positive integer n , write a function that returns the number of set bits in its binary representation (also known as the Hamming weight ). 

 Example 1: 

 Input: n = 11 
 
 Output: 3 
 
 Explanation: 
 
 The input binary string 1011 has a total of three set bits. 

 Example 2: 

 Input: n = 128 
 
 Output: 1 
 
 Explanation: 
 
 The input binary string 10000000 has a total of one set bit. 

 Example 3: 

 Input: n = 2147483645 
 
 Output: 30 
 
 Explanation: 
 
 The input binary string 1111111111111111111111111111101 has a total of thirty set bits. 

 Constraints: 

 1 <= n <= 2 31 - 1 

 Follow up: If this function is called many times, how would you optimize it?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n) {
            count += n & 1;
            n >>= 1;
        }
        return count;
    }
};
```


## 252. Meeting Rooms

**Problem:** https://leetcode.com/problems/meeting-rooms/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Sorting, Quicksort

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** Sorts intervals and checks each adjacent pair once.

### Problem description

You are given an array of meeting times  intervals where intervals[i] = [start i , end i ] . 
 
 A person can attend all meetings if no two meeting intervals overlap. Meetings ending at time t and starting at time t do not overlap. 
 
 ​​​​​​​Return true if a person can attend all meetings. Otherwise, return false . 

 Example 1: 
 
```
Input:
 intervals = [[0,30],[5,10],[15,20]]

Output:
 false
```
 
 Example 2: 
 
```
Input:
 intervals = [[7,10],[2,4]]

Output:
 true
```

 Constraints: 

 0 <= intervals.length <= 10 4 
 
 intervals[i].length == 2 
 
 0 <= start i < end i <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
public:
    bool canAttendMeetings(vector< vector< int >>& intervals)
    {
        sort(intervals.begin(), intervals.end());
        for (int i = 1; i < (int) intervals.size();++i) if(intervals[i][0] < intervals[i - 1][1])
        {
            return false;
        }
        return true;
    }
};
```


## 274. H-Index

**Problem:** https://leetcode.com/problems/h-index/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Counting Sort

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** Descending sort dominates the following linear scan for the h-index.

### Problem description

Given an array of integers citations where citations[i] is the number of citations a researcher received for their i th paper, return the researcher's h-index . 
 
 According to the definition of h-index on Wikipedia : The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times. 

 Example 1: 
 
```
Input:
 citations = [3,0,6,1,5]

Output:
 3

Explanation:
 [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
```

 Example 2: 
 
```
Input:
 citations = [1,3,1]

Output:
 1
```

 Constraints: 

 n == citations.length 
 
 1 <= n <= 5000 
 
 0 <= citations[i] <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.rbegin(), citations.rend());
        int h = 0;
        while (h < citations.size() && citations[h] > h) {
            h++;
        }
        return h;
    }
};
```


## 414. Third Maximum Number

**Problem:** https://leetcode.com/problems/third-maximum-number/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Ordered set, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** An ordered set is kept at size at most three, making every insertion and deletion constant-bounded.

### Problem description

You are given an integer array nums . 
 
 Return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number. 

 Example 1: 
 
```
Input:
 nums = [3,2,1]

Output:
 1

Explanation:

The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
```

 Example 2: 
 
```
Input:
 nums = [1,2]

Output:
 2

Explanation:

The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
```

 Example 3: 
 
```
Input:
 nums = [2,2,3,1]

Output:
 1

Explanation:

The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
```

 Constraints: 

 1 <= nums.length <= 10 4 
 
 -2 31 <= nums[i] <= 2 31 - 1 

 Follow up: Can you find an O(n) solution?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> maxSet;
        for (int num : nums) {
            maxSet.insert(num);
            if (maxSet.size() > 3) {
                maxSet.erase(maxSet.begin());
            }
        }
        return maxSet.size() == 3 ? *maxSet.begin() : *maxSet.rbegin();
    }
};
```


## 747. Largest Number At Least Twice of Others

**Problem:** https://leetcode.com/problems/largest-number-at-least-twice-of-others/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One pass tracks the largest and second-largest values and the largest index.

### Problem description

You are given an integer array nums where the largest integer is unique . 
 
 Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise . 

 Example 1: 
 
```
Input:
 nums = [3,6,1,0]

Output:
 1

Explanation:
 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
```

 Example 2: 
 
```
Input:
 nums = [1,2,3,4]

Output:
 -1

Explanation:
 4 is less than twice the value of 3, so we return -1.
```

 Constraints: 

 2 <= nums.length <= 50 
 
 0 <= nums[i] <= 100 
 
 The largest element in nums is unique.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int largest = -1, second = -1, index = -1;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] > largest) {
                second = largest;
                largest = nums[i];
                index = i;
            } else second = max(second, nums[i]);
        }
        return largest >= 2LL * second ? index : -1;
    }
};
```


## 950. Reveal Cards In Increasing Order

**Problem:** https://leetcode.com/problems/reveal-cards-in-increasing-order/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Queue, Sorting, Simulation

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Queue, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Sorting dominates; the queue of n indices and output vector each use linear storage. Note: the final iteration accesses queue.front() after popping its last element, which is undefined behavior.

### Problem description

You are given an integer array deck . There is a deck of cards where every card has a unique integer. The integer on the i th card is deck[i] . 
 
 You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck. 
 
 You will do the following steps repeatedly until all cards are revealed: 

 Take the top card of the deck, reveal it, and take it out of the deck. 
 
 If there are still cards in the deck then put the next top card of the deck at the bottom of the deck. 
 
 If there are still unrevealed cards, go back to step 1. Otherwise, stop. 

 Return an ordering of the deck that would reveal the cards in increasing order . 
 
 Note that the first entry in the answer is considered to be the top of the deck. 

 Example 1: 
 
```
Input:
 deck = [17,13,11,2,3,5,7]

Output:
 [2,13,3,11,5,17,7]

Explanation:
 
We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom. The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom. The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom. The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom. The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom. The deck is now [13,17].
We reveal 13, and move 17 to the bottom. The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.
```

 Example 2: 
 
```
Input:
 deck = [1,1000]

Output:
 [1,1000]
```

 Constraints: 

 1 <= deck.length <= 1000 
 
 1 <= deck[i] <= 10 6 
 
 All the values of deck are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
 {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) 
    {
        sort(deck.begin() , deck.end()) ;
        int n = deck.size();
        int i=0;
        queue<int> deck_queue;
        vector<int> ans(n);
        while(i<n)
        {
            deck_queue.push(i++);
        }

        for(i=0;i<n;i++)
        {
            ans[deck_queue.front()] = deck[i];
            deck_queue.pop() ;
            deck_queue.push(deck_queue.front()) ;
            deck_queue.pop() ;
        }
        return ans ;
    }
};
```


## 1051. Height Checker

**Problem:** https://leetcode.com/problems/height-checker/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting, Counting Sort, Bubble Sort

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + 101)

**Space complexity:** O(101)

**Complexity reasoning:** Counts heights in a fixed 101-element array; the expected-height pointer only advances through the fixed range once.

### Problem description

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the i th student in line. 
 
 You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the i th student in line ( 0-indexed ). 
 
 Return the number of indices where heights[i] != expected[i] . 

 Example 1: 
 
```
Input:
 heights = [1,1,4,2,1,3]

Output:
 3

Explanation:
 
heights: [1,1,
4
,2,
1
,
3
]
expected: [1,1,
1
,2,
3
,
4
]
Indices 2, 4, and 5 do not match.
```

 Example 2: 
 
```
Input:
 heights = [5,1,2,3,4]

Output:
 5

Explanation:

heights: [
5
,
1
,
2
,
3
,
4
]
expected: [
1
,
2
,
3
,
4
,
5
]
All indices do not match.
```

 Example 3: 
 
```
Input:
 heights = [1,2,3,4,5]

Output:
 0

Explanation:

heights: [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
```

 Constraints: 

 1 <= heights.length <= 100 
 
 1 <= heights[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int count[101] = {};
        for (int h : heights) ++count[h];
        int expected = 1, mismatch = 0;
        for (int h : heights) {
            while (count[expected] == 0) ++expected;
            if (h != expected) ++mismatch;
            --count[expected];
        }
        return mismatch;
    }
};
```


## 1200. Minimum Absolute Difference

**Problem:** https://leetcode.com/problems/minimum-absolute-difference/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n) output; O(log n) sort stack

**Complexity reasoning:** Sorts the input, then scans adjacent differences, storing up to n-1 minimum-difference pairs.

### Problem description

Given an array of distinct integers arr , find all pairs of elements with the minimum absolute difference of any two elements. 
 
 Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows 

 a, b are from arr 
 
 a < b 
 
 b - a equals to the minimum absolute difference of any two elements in arr 

 Example 1: 
 
```
Input:
 arr = [4,2,1,3]

Output:
 [[1,2],[2,3],[3,4]]

Explanation: 
The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
```

 Example 2: 
 
```
Input:
 arr = [1,3,6,10,15]

Output:
 [[1,3]]
```

 Example 3: 
 
```
Input:
 arr = [3,8,-10,23,19,-4,-14,27]

Output:
 [[-14,-10],[19,23],[23,27]]
```

 Constraints: 

 2 <= arr.length <= 10 5 
 
 -10 6 <= arr[i] <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        vector<vector<int>> result;
        int minDiff = INT_MAX;

        for (int i = 1; i < arr.size(); i++) {
            int diff = arr[i] - arr[i-1];
            if (diff < minDiff) {
                minDiff = diff;
                result.clear();
            }
            if (diff == minDiff) {
                result.push_back({arr[i-1], arr[i]});
            }
        }
        return result;
    }
};
```


## 1274. Number of Ships in a Rectangle

**Problem:** https://leetcode.com/problems/number-of-ships-in-a-rectangle/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Divide and Conquer, Interactive

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(s log A) with s ships and A grid points; O(A) worst case

**Space complexity:** O(log A) recursion stack

**Complexity reasoning:** A rectangle is halved recursively; empty regions are pruned by hasShips. At each depth at most O(s) occupied rectangles branch, with logarithmic depth. With unrestricted s, the search may visit O(A) cells.

### Problem description

(This problem is an interactive problem .) 
 
 Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship. 
 
 You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary. 
 
 Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle. 
 
 Submissions making more than 400 calls to hasShips will be judged Wrong Answer . Also, any solutions that attempt to circumvent the judge will result in disqualification. 

 Example : 
 [Figure: https://assets.leetcode.com/uploads/2019/07/26/1445_example_1.PNG] 
 
```
Input:
 
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]

Output:
 3

Explanation:
 From [0,0] to [4,4] we can count 3 ships within the range.
```

 Example 2: 
 
```
Input:
 ans = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]

Output:
 3
```

 Constraints: 

 On the input ships is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given hasShips API, without knowing the ships position. 
 
 0 <= bottomLeft[0] <= topRight[0] <= 1000 
 
 0 <= bottomLeft[1] <= topRight[1] <= 1000 
 
 topRight != bottomLeft

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    int count(Sea& sea, int x1, int y1, int x2, int y2) {
        if (x1 > x2 || y1 > y2 || !sea.hasShips({x2, y2}, {x1, y1})) {
            return 0;
        }
        if (x1 == x2 && y1 == y2) {
            return 1;
        }
        if (x2 - x1 >= y2 - y1) {
            int mid = x1 + (x2 - x1) / 2;
            return count(sea, x1, y1, mid, y2)
                 + count(sea, mid + 1, y1, x2, y2);
        }
        int mid = y1 + (y2 - y1) / 2;
        return count(sea, x1, y1, x2, mid)
             + count(sea, x1, mid + 1, x2, y2);
    }

public:
    int countShips(Sea sea, vector<int> topRight, vector<int> bottomLeft) {
        return count(sea, bottomLeft[0], bottomLeft[1],
                     topRight[0], topRight[1]);
    }
};
```


## 1288. Remove Covered Intervals

**Problem:** https://leetcode.com/problems/remove-covered-intervals/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** Sorts by ascending start and descending end, then makes one pass tracking the farthest endpoint.

### Problem description

Given an array intervals where intervals[i] = [l i , r i ] represent the interval [l i , r i ) , remove all intervals that are covered by another interval in the list. 
 
 The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d . 
 
 Return the number of remaining intervals . 

 Example 1: 
 
```
Input:
 intervals = [[1,4],[3,6],[2,8]]

Output:
 2

Explanation:
 Interval [3,6] is covered by [2,8], therefore it is removed.
```

 Example 2: 
 
```
Input:
 intervals = [[1,4],[2,3]]

Output:
 1
```

 Constraints: 

 1 <= intervals.length <= 1000 
 
 intervals[i].length == 2 
 
 0 <= l i < r i <= 10 5 
 
 All the given intervals are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](auto& a, auto& b) {
            return a[0] < b[0] || (a[0] == b[0] && a[1] > b[1]);
        });

        int count = 0, end = 0;
        for (auto& i : intervals) {
            if (i[1] > end) {
                ++count;
                end = i[1];
            }
        }
        return count;
    }
};
```


## 1329. Sort the Matrix Diagonally

**Problem:** https://leetcode.com/problems/sort-the-matrix-diagonally/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Matrix

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Hash map, Ordered map, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn log(min(m,n))) expected

**Space complexity:** O(mn)

**Complexity reasoning:** Groups all mn cells by diagonal, sorts each diagonal, then writes elements back. Hash-map operations are expected constant time.

### Problem description

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0] , where mat is a 6 x 3 matrix, includes cells mat[2][0] , mat[3][1] , and mat[4][2] . 
 
 Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/01/21/1482_example_1_2.png] 
 
```
Input:
 mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]

Output:
 [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
```

 Example 2: 
 
```
Input:
 mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]

Output:
 [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
```

 Constraints: 

 m == mat.length 
 
 n == mat[i].length 
 
 1 <= m, n <= 100 
 
 1 <= mat[i][j] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        unordered_map<int, vector<int>> diagonals;
        int m = mat.size(), n = mat[0].size();
        
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                diagonals[i - j].push_back(mat[i][j]);

        for (auto& [key, vec] : diagonals)
            sort(vec.begin(), vec.end(), greater<int>());

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                mat[i][j] = diagonals[i - j].back();
                diagonals[i - j].pop_back();
            }

        return mat;
    }
};
```


## 1333. Filter Restaurants by Vegan-Friendly, Price and Distance

**Problem:** https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + f log f)

**Space complexity:** O(f + log f)

**Complexity reasoning:** Filters n restaurants, sorts the f matching rows, then creates the f-element ID result; sorting needs logarithmic stack space.

### Problem description

Given the array restaurants where   restaurants[i] = [id i , rating i , veganFriendly i , price i , distance i ] . You have to filter the restaurants using three filters. 
 
 The veganFriendly filter will be either true (meaning you should only include restaurants with veganFriendly i set to true) or false  (meaning you can include any restaurant). In addition, you have the filters  maxPrice and maxDistance  which are the maximum value for price and distance of restaurants you should consider respectively. 
 
 Return the array of restaurant IDs after filtering, ordered by rating from highest to lowest. For restaurants with the same rating, order them by id from highest to lowest. For simplicity veganFriendly i and veganFriendly take value 1 when it is true , and 0 when it is false . 

 Example 1: 
 
```
Input:
 restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10

Output:
 [3,1,5] 

Explanation: 

The restaurants are:
Restaurant 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
Restaurant 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
Restaurant 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
Restaurant 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
Restaurant 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1] 
After filter restaurants with veganFriendly = 1, maxPrice = 50 and maxDistance = 10 we have restaurant 3, restaurant 1 and restaurant 5 (ordered by rating from highest to lowest).
```

 Example 2: 
 
```
Input:
 restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10

Output:
 [4,3,2,1,5]

Explanation:
 The restaurants are the same as in example 1, but in this case the filter veganFriendly = 0, therefore all restaurants are considered.
```

 Example 3: 
 
```
Input:
 restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3

Output:
 [4,5]
```

 Constraints: 

 1 <= restaurants.length <= 10^4 
 
 restaurants[i].length == 5 
 
 1 <= id i , rating i , price i , distance i <= 10^5 
 
 1 <= maxPrice, maxDistance <= 10^5 
 
 veganFriendly i and  veganFriendly  are 0 or 1. 
 
 All id i are distinct.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> filterRestaurants(vector<vector<int>>& restaurants, int veganFriendly,
                                  int maxPrice, int maxDistance) {
        vector<vector<int>> filtered;
        for (auto& r : restaurants) {
            if ((veganFriendly == 0 || r[2] == 1) &&
                r[3] <= maxPrice && r[4] <= maxDistance) {
                filtered.push_back(r);
            }
        }

        sort(filtered.begin(), filtered.end(), [](auto& a, auto& b) {
            return a[1] == b[1] ? a[0] > b[0] : a[1] > b[1];
        });

        vector<int> res;
        for (auto& r : filtered) res.push_back(r[0]);
        return res;
    }
};
```


## 1491. Average Salary Excluding the Minimum and Maximum Salary

**Problem:** https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One scan computes sum, minimum, and maximum without allocating collections.

### Problem description

You are given an array of unique integers salary where salary[i] is the salary of the i th employee. 
 
 Return the average salary of employees excluding the minimum and maximum salary . Answers within 10 -5 of the actual answer will be accepted. 

 Example 1: 
 
```
Input:
 salary = [4000,3000,1000,2000]

Output:
 2500.00000

Explanation:
 Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
```

 Example 2: 
 
```
Input:
 salary = [1000,2000,3000]

Output:
 2000.00000

Explanation:
 Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
```

 Constraints: 

 3 <= salary.length <= 100 
 
 1000 <= salary[i] <= 10 6 
 
 All the integers of salary are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double average(vector<int>& salary) {
        int total = 0, mn = INT_MAX, mx = INT_MIN;
        for (int s : salary) {
            total += s;
            mn = min(mn, s);
            mx = max(mx, s);
        }
        return (total - mn - mx) / (double)(salary.size() - 2);
    }
};
```


## 1502. Can Make Arithmetic Progression From Sequence

**Problem:** https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** Sorts the array and verifies the difference between each consecutive pair.

### Problem description

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same. 
 
 Given an array of numbers arr , return true if the array can be rearranged to form an arithmetic progression . Otherwise, return false . 

 Example 1: 
 
```
Input:
 arr = [3,5,1]

Output:
 true

Explanation: 
We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
```

 Example 2: 
 
```
Input:
 arr = [1,2,4]

Output:
 false

Explanation: 
There is no way to reorder the elements to obtain an arithmetic progression.
```

 Constraints: 

 2 <= arr.length <= 1000 
 
 -10 6 <= arr[i] <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int diff = arr[1] - arr[0];
        for (int i = 2; i < arr.size(); ++i)
            if (arr[i] - arr[i - 1] != diff)
                return false;
        return true;
    }
};
```


## 1619. Mean of Array After Removing Some Elements

**Problem:** https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** Sorting dominates summing the middle 90% of the sorted array.

### Problem description

Given an integer array arr , return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements. 
 
 Answers within 10 -5 of the actual answer will be considered accepted. 

 Example 1: 
 
```
Input:
 arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]

Output:
 2.00000

Explanation:
 After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.
```

 Example 2: 
 
```
Input:
 arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]

Output:
 4.00000
```

 Example 3: 
 
```
Input:
 arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]

Output:
 4.77778
```

 Constraints: 

 20 <= arr.length <= 1000 
 
 arr.length is a multiple of 20 . 
 
 0 <= arr[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    double trimMean(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int n = arr.size(), k = n / 20;
        double sum = 0;
        for (int i = k; i < n - k; ++i) sum += arr[i];
        return sum / (n - 2 * k);
    }
};
```


## 1637. Widest Vertical Area Between Two Points Containing No Points

**Problem:** https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Copies x-coordinates into a vector, sorts them, and scans consecutive gaps.

### Problem description

Given n points on a 2D plane where points[i] = [x i , y i ] , Return  the widest vertical area between two points such that no points are inside the area. 
 
 A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width. 
 
 Note that points on the edge of a vertical area are not considered included in the area. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/19/points3.png] ​
 
```
Input:
 points = [[8,7],[9,9],[7,4],[9,7]]

Output:
 1

Explanation:
 Both the red and the blue area are optimal.
```

 Example 2: 
 
```
Input:
 points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]

Output:
 3
```

 Constraints: 

 n == points.length 
 
 2 <= n <= 10 5 
 
 points[i].length == 2 
 
 0 <= x i , y i  <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> x;
        for (auto& p : points) x.push_back(p[0]);
        sort(x.begin(), x.end());
        int ans = 0;
        for (int i = 1; i < (int)x.size(); ++i)
            ans = max(ans, x[i] - x[i - 1]);
        return ans;
    }
};
```


## 1756. Design Most Recently Used Queue

**Problem:** https://leetcode.com/problems/design-most-recently-used-queue/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Linked List, Divide and Conquer, Design, Simulation, Doubly-Linked List, Sqrt Decomposition, Treap, Splay Tree

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Linked List / Pointers, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Linked list, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n) construction; O(n) per fetch

**Space complexity:** O(n)

**Complexity reasoning:** The constructor builds n values; vector::erase shifts up to n elements and push_back is amortized constant time.

### Problem description

Design a queue-like data structure that moves the most recently used element to the end of the queue. 
 
 Implement the MRUQueue class: 

 MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n] . 
 
 int fetch(int k) moves the k th element (1-indexed) to the end of the queue and returns it. 

 Example 1: 
 
```
Input:

["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]

Output:

[null, 3, 6, 2, 2]

Explanation:

MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3
rd
 element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5
th
 element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2
nd
 element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // The 8
th
 element (2) is already at the end of the queue so just return it.
```

 Constraints: 

 1 <= n <= 2000 
 
 1 <= k <= n 
 
 At most 2000 calls will be made to fetch . 

 Follow up: Finding an O(n) algorithm per fetch is a bit easy. Can you find an algorithm with a better complexity for each fetch call?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class MRUQueue {
    vector<int> values;
public:
    MRUQueue(int n) {
        for (int i = 1; i <= n; ++i) values.push_back(i);
    }
    int fetch(int k) {
        int value = values[k - 1];
        values.erase(values.begin() + k - 1);
        values.push_back(value);
        return value;
    }
};
```


## 1887. Reduction Operations to Make the Array Elements Equal

**Problem:** https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** Sorts the numbers and traverses adjacent values from right to left once.

### Problem description

Given an integer array nums , your goal is to make all elements in nums equal. To complete one operation, follow these steps: 

 Find the largest value in nums . Let its index be i ( 0-indexed ) and its value be largest . If there are multiple elements with the largest value, pick the smallest i . 
 
 Find the next largest value in nums strictly smaller than largest . Let its value be nextLargest . 
 
 Reduce nums[i] to nextLargest . 

 Return the number of operations to make all elements in nums equal . 

 Example 1: 
 
```
Input:
 nums = [5,1,3]

Output:
 3

Explanation:
 It takes 3 operations to make all elements in nums equal:
1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [
3
,1,3].
2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [
1
,1,3].
3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,
1
].
```

 Example 2: 
 
```
Input:
 nums = [1,1,1]

Output:
 0

Explanation:
 All elements in nums are already equal.
```

 Example 3: 
 
```
Input:
 nums = [1,1,2,2,3]

Output:
 4

Explanation:
 It takes 4 operations to make all elements in nums equal:
1. largest = 3 at index 4. nextLargest = 2. Reduce nums[4] to 2. nums = [1,1,2,2,
2
].
2. largest = 2 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,
1
,2,2].
3. largest = 2 at index 3. nextLargest = 1. Reduce nums[3] to 1. nums = [1,1,1,
1
,2].
4. largest = 2 at index 4. nextLargest = 1. Reduce nums[4] to 1. nums = [1,1,1,1,
1
].
```

 Constraints: 

 1 <= nums.length <= 5 * 10 4 
 
 1 <= nums[i] <= 5 * 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int size = nums.size();
        int ans = 0;
        for (int i = size - 1; i > 0; --i) {
            if (nums[i - 1] != nums[i]) {
                ans += size - i;
            }
        }
        return ans;
    }
};
```


## 1913. Maximum Product Difference Between Two Pairs

**Problem:** https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting, Quicksort

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** Sorts all numbers, then calculates the difference from the two smallest and two largest.

### Problem description

The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d) . 

 For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16 . 

 Given an integer array nums , choose four distinct indices w , x , y , and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized . 
 
 Return the maximum such product difference . 

 Example 1: 
 
```
Input:
 nums = [5,6,2,7,4]

Output:
 34

Explanation:
 We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
```

 Example 2: 
 
```
Input:
 nums = [4,2,5,9,7,4,8]

Output:
 64

Explanation:
 We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.
```

 Constraints: 

 4 <= nums.length <= 10 4 
 
 1 <= nums[i] <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        return (nums[n-1] * nums[n-2]) - (nums[0] * nums[1]);
    }
};
```


## 2164. Sort Even and Odd Indices Independently

**Problem:** https://leetcode.com/problems/sort-even-and-odd-indices-independently/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Splits n elements into two vectors, sorts each parity group, and writes the sorted values back.

### Problem description

You are given a 0-indexed integer array nums . Rearrange the values of nums according to the following rules: 

 Sort the values at odd indices of nums in non-increasing order.

 For example, if nums = [4, 1 ,2, 3 ] before this step, it becomes [4, 3 ,2, 1 ] after. The values at odd indices 1 and 3 are sorted in non-increasing order. 

 Sort the values at even indices of nums in non-decreasing order.

 For example, if nums = [ 4 ,1, 2 ,3] before this step, it becomes [ 2 ,1, 4 ,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order. 

 Return the array formed after rearranging the values of nums . 

 Example 1: 
 
```
Input:
 nums = [4,1,2,3]

Output:
 [2,3,4,1]

Explanation:
 
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,
1
,2,
3
] to [4,
3
,2,
1
].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [
4
,1,
2
,3] to [
2
,3,
4
,1].
Thus, the array formed after rearranging the values is [2,3,4,1].
```

 Example 2: 
 
```
Input:
 nums = [2,1]

Output:
 [2,1]

Explanation:
 
Since there is exactly one odd index and one even index, no rearrangement of values takes place.
The resultant array formed is [2,1], which is the same as the initial array.
```

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> sortEvenOdd(vector<int>& nums) {
        vector<int> a,b;
        for(int i=0;i<(int)nums.size();++i) (i%2?b:a).push_back(nums[i]);
        sort(a.begin(),a.end());sort(b.rbegin(),b.rend());
        for(int i=0;i<(int)nums.size();++i) nums[i]=(i%2?b[i/2]:a[i/2]);
        return nums;
    }
};
```


## 2191. Sort the Jumbled Numbers

**Problem:** https://leetcode.com/problems/sort-the-jumbled-numbers/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n · d)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** stable_sort performs O(n log n) mapped-value comparisons; each comparison converts up to d digits for both values. stable_sort may additionally allocate O(n) temporary storage, with implementation-dependent fallback.

### Problem description

You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system. 
 
 The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9 . 
 
 You are also given another integer array nums . Return the array nums sorted in non-decreasing order based on the mapped values of its elements. 
 
 Notes: 

 Elements with the same mapped values should appear in the same relative order as in the input. 
 
 The elements of nums should only be sorted based on their mapped values and not be replaced by them. 

 Example 1: 
 
```
Input:
 mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]

Output:
 [338,38,991]

Explanation:
 
Map the number 991 as follows:
1. mapping[9] = 6, so all occurrences of the digit 9 will become 6.
2. mapping[1] = 9, so all occurrences of the digit 1 will become 9.
Therefore, the mapped value of 991 is 669.
338 maps to 007, or 7 after removing the leading zeros.
38 maps to 07, which is also 7 after removing leading zeros.
Since 338 and 38 share the same mapped value, they should remain in the same relative order, so 338 comes before 38.
Thus, the sorted array is [338,38,991].
```

 Example 2: 
 
```
Input:
 mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]

Output:
 [123,456,789]

Explanation:
 789 maps to 789, 456 maps to 456, and 123 maps to 123. Thus, the sorted array is [123,456,789].
```

 Constraints: 

 mapping.length == 10 
 
 0 <= mapping[i] <= 9 
 
 All the values of mapping[i] are unique . 
 
 1 <= nums.length <= 3 * 10 4 
 
 0 <= nums[i] < 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 vector<int> sortJumbled(vector<int>& mapping,vector<int>& nums) {
  auto val=[&](int x){if(!x)return (long long)mapping[0]; long long y=0,p=1;while(x){y+=mapping[x%10]*p;p*=10;x/=10;}return y;};
  stable_sort(nums.begin(),nums.end(),[&](int a,int b){return val(a)<val(b);});return nums;
 }
};
```


## 2274. Maximum Consecutive Floors Without Special Floors

**Problem:** https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** Sorts special floors and scans adjacent gaps once.

### Problem description

Alice manages a company and has rented some floors of a building as office space. Alice has decided some of these floors should be special floors , used for relaxation only. 
 
 You are given two integers bottom and top , which denote that Alice has rented all the floors from bottom to top ( inclusive ). You are also given the integer array special , where special[i] denotes a special floor that Alice has designated for relaxation. 
 
 Return the maximum number of consecutive floors without a special floor . 

 Example 1: 
 
```
Input:
 bottom = 2, top = 9, special = [4,6]

Output:
 3

Explanation:
 The following are the ranges (inclusive) of consecutive floors without a special floor:
- (2, 3) with a total amount of 2 floors.
- (5, 5) with a total amount of 1 floor.
- (7, 9) with a total amount of 3 floors.
Therefore, we return the maximum number which is 3 floors.
```

 Example 2: 
 
```
Input:
 bottom = 6, top = 8, special = [7,6,8]

Output:
 0

Explanation:
 Every floor rented is a special floor, so we return 0.
```

 Constraints: 

 1 <= special.length <= 10 5 
 
 1 <= bottom <= special[i] <= top <= 10 9 
 
 All the values of special are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {public:int maxConsecutive(int bottom,int top,vector<int>& special){sort(special.begin(),special.end());int ans=special[0]-bottom;for(int i=1;i<(int)special.size();++i)ans=max(ans,special[i]-special[i-1]-1);return max(ans,top-special.back());} };
```


## 2545. Sort the Students by Their Kth Score

**Problem:** https://leetcode.com/problems/sort-the-students-by-their-kth-score/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Matrix

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n · k)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** Sorts n rows of length k+1 by one score; row swaps/moves during sorting can cost O(k) each.

### Problem description

There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score , where each row represents one student and score[i][j] denotes the score the i th student got in the j th exam. The matrix score contains distinct integers only. 
 
 You are also given an integer k . Sort the students (i.e., the rows of the matrix) by their scores in the k th  ( 0-indexed ) exam from the highest to the lowest. 
 
 Return the matrix after sorting it. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/11/30/example1.png] 
 
```
Input:
 score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2

Output:
 [[7,5,11,2],[10,6,9,1],[4,8,3,15]]

Explanation:
 In the above diagram, S denotes the student, while E denotes the exam.
- The student with index 1 scored 11 in exam 2, which is the highest score, so they got first place.
- The student with index 0 scored 9 in exam 2, which is the second highest score, so they got second place.
- The student with index 2 scored 3 in exam 2, which is the lowest score, so they got third place.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/11/30/example2.png] 
 
```
Input:
 score = [[3,4],[5,6]], k = 0

Output:
 [[5,6],[3,4]]

Explanation:
 In the above diagram, S denotes the student, while E denotes the exam.
- The student with index 1 scored 5 in exam 0, which is the highest score, so they got first place.
- The student with index 0 scored 3 in exam 0, which is the lowest score, so they got second place.
```

 Constraints: 

 m == score.length 
 
 n == score[i].length 
 
 1 <= m, n <= 250 
 
 1 <= score[i][j] <= 10 5 
 
 score consists of distinct integers. 
 
 0 <= k < n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 vector<vector<int>> sortTheStudents(vector<vector<int>>& score,int k){
  sort(score.begin(),score.end(),[&](const vector<int>& a,const vector<int>& b){return a[k]>b[k];});return score;
 }
};
```


## 2580. Count Ways to Group Overlapping Ranges

**Problem:** https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) sort stack

**Complexity reasoning:** Sorts ranges and scans them once, doubling the answer whenever a disjoint component begins.

### Problem description

You are given a 2D integer array ranges where ranges[i] = [start i , end i ] denotes that all integers between start i and end i (both inclusive ) are contained in the i th range. 
 
 You are to split ranges into two (possibly empty) groups such that: 

 Each range belongs to exactly one group. 
 
 Any two overlapping ranges must belong to the same group. 

 Two ranges are said to be overlapping  if there exists at least one integer that is present in both ranges. 

 For example, [1, 3] and [2, 5] are overlapping because 2 and 3 occur in both ranges. 

 Return the total number of ways to split ranges into two groups . Since the answer may be very large, return it modulo 10 9 + 7 . 

 Example 1: 
 
```
Input:
 ranges = [[6,10],[5,15]]

Output:
 2

Explanation:
 
The two ranges are overlapping, so they must be in the same group.
Thus, there are two possible ways:
- Put both the ranges together in group 1.
- Put both the ranges together in group 2.
```

 Example 2: 
 
```
Input:
 ranges = [[1,3],[10,20],[2,5],[4,8]]

Output:
 4

Explanation:
 
Ranges [1,3], and [2,5] are overlapping. So, they must be in the same group.
Again, ranges [2,5] and [4,8] are also overlapping. So, they must also be in the same group. 
Thus, there are four possible ways to group them:
- All the ranges in group 1.
- All the ranges in group 2.
- Ranges [1,3], [2,5], and [4,8] in group 1 and [10,20] in group 2.
- Ranges [1,3], [2,5], and [4,8] in group 2 and [10,20] in group 1.
```

 Constraints: 

 1 <= ranges.length <= 10 5 
 
 ranges[i].length == 2 
 
 0 <= start i <= end i <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int countWays(vector<vector<int>>& ranges){sort(ranges.begin(),ranges.end());long long ans=1;int end=-1;for(auto &r:ranges){if(r[0]>end)ans=ans*2%1000000007;end=max(end,r[1]);}return ans;}};
```


## 2655. Find Maximal Uncovered Ranges

**Problem:** https://leetcode.com/problems/find-maximal-uncovered-ranges/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(r log r)

**Space complexity:** O(r) output; O(log r) sort stack

**Complexity reasoning:** Sorts r covered intervals and scans them to emit at most r+1 uncovered gaps.

### Problem description

You are given an integer n  which is the length of a 0-indexed array nums , and a 0-indexed 2D-array ranges , which is a list of sub-ranges of nums  (sub-ranges may overlap ). 
 
 Each row ranges[i] has exactly 2 cells: 

 ranges[i][0] , which shows the start of the i th range (inclusive) 
 
 ranges[i][1] , which shows the end of the i th range (inclusive) 

 These ranges cover some cells of nums  and leave some cells uncovered. Your task is to find all of the uncovered ranges with maximal length. 
 
 Return a 2D-array answer of the uncovered ranges, sorted by the starting point in ascending order . 
 
 By all of the  uncovered ranges with maximal length, we mean satisfying two conditions: 

 Each uncovered cell should belong to exactly one sub-range 
 
 There should not exist  two ranges (l 1 , r 1 ) and (l 2 , r 2 ) such that r 1 + 1 = l 2 

 Example 1: 
 
```
Input:
 n = 10, ranges = [[3,5],[7,8]]

Output:
 [[0,2],[6,6],[9,9]]

Explanation:
 The ranges (3, 5) and (7, 8) are covered, so if we simplify the array nums to a binary array where 0 shows an uncovered cell and 1 shows a covered cell, the array becomes [0,0,0,1,1,1,0,1,1,0] in which we can observe that the ranges (0, 2), (6, 6) and (9, 9) aren't covered.
```

 Example 2: 
 
```
Input:
 n = 3, ranges = [[0,2]]

Output:
 []

Explanation: 
In this example, the whole of the array nums is covered and there are no uncovered cells so the output is an empty array.
```

 Example 3: 
 
```
Input:
 n = 7, ranges = [[2,4],[0,3]]

Output:
 [[5,6]]

Explanation:
 The ranges (0, 3) and (2, 4) are covered, so if we simplify the array nums to a binary array where 0 shows an uncovered cell and 1 shows a covered cell, the array becomes [1,1,1,1,1,0,0] in which we can observe that the range (5, 6) is uncovered.
```

 Constraints: 

 1 <= n <= 10 9 
 
 0 <= ranges.length <= 10 6 
 
 ranges[i].length = 2 
 
 0 <= ranges[i][j] <= n - 1 
 
 ranges[i][0] <= ranges[i][1]

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> findMaximalUncoveredRanges(int n, vector<vector<int>>& ranges) {
        sort(ranges.begin(), ranges.end());
        vector<vector<int>> answer;
        int start = 0;
        for (const auto& r : ranges) {
            if (r[0] > start) answer.push_back({start, r[0] - 1});
            start = max(start, r[1] + 1);
        }
        if (start < n) answer.push_back({start, n - 1});
        return answer;
    }
};
```


## 2733. Neither Minimum nor Maximum

**Problem:** https://leetcode.com/problems/neither-minimum-nor-maximum/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Only the first three numbers are copied and sorted, so both work and storage are bounded by constants.

### Problem description

Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number. 
 
 Return the selected integer. 

 Example 1: 
 
```
Input:
 nums = [3,2,1,4]

Output:
 2

Explanation:
 In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.
```

 Example 2: 
 
```
Input:
 nums = [1,2]

Output:
 -1

Explanation:
 Since there is no number in nums that is neither the maximum nor the minimum, we cannot select a number that satisfies the given condition. Therefore, there is no answer.
```

 Example 3: 
 
```
Input:
 nums = [2,1,3]

Output:
 2

Explanation:
 Since 2 is neither the maximum nor the minimum value in nums, it is the only valid answer.
```

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100 
 
 All values in nums are distinct

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int findNonMinOrMax(vector<int>& nums){if(nums.size()<3)return -1;vector<int>a={nums[0],nums[1],nums[2]};sort(a.begin(),a.end());return a[1];}};
```


## 2740. Find the Value of the Partition

**Problem:** https://leetcode.com/problems/find-the-value-of-the-partition/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) auxiliary for std::sort

**Complexity reasoning:** Sorting dominates the single O(n) adjacent-gap scan.

### Problem description

You are given a positive integer array nums . 
 
 Partition nums into two arrays,  nums1 and nums2 , such that: 

 Each element of the array nums belongs to either the array nums1 or the array nums2 . 
 
 Both arrays are non-empty . 
 
 The value of the partition is minimized . 

 The value of the partition is |max(nums1) - min(nums2)| . 
 
 Here, max(nums1) denotes the maximum element of the array nums1 , and min(nums2) denotes the minimum element of the array nums2 . 
 
 Return the integer denoting the value of such partition . 

 Example 1: 
 
```
Input:
 nums = [1,3,2,4]

Output:
 1

Explanation:
 We can partition the array nums into nums1 = [1,2] and nums2 = [3,4].
- The maximum element of the array nums1 is equal to 2.
- The minimum element of the array nums2 is equal to 3.
The value of the partition is |2 - 3| = 1. 
It can be proven that 1 is the minimum value out of all partitions.
```

 Example 2: 
 
```
Input:
 nums = [100,1,10]

Output:
 9

Explanation:
 We can partition the array nums into nums1 = [10] and nums2 = [100,1].
- The maximum element of the array nums1 is equal to 10.
- The minimum element of the array nums2 is equal to 1.
The value of the partition is |10 - 1| = 9.
It can be proven that 9 is the minimum value out of all partitions.
```

 Constraints: 

 2 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int findValueOfPartition(vector<int>& nums){sort(nums.begin(),nums.end());int ans=INT_MAX;for(int i=1;i<(int)nums.size();++i)ans=min(ans,nums[i]-nums[i-1]);return ans;}};
```


## 2751. Robot Collisions

**Problem:** https://leetcode.com/problems/robot-collisions/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Stack, Sorting, Simulation

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Stack, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Sorting the index order costs O(n log n); each robot enters and leaves the collision stack at most once. The index, stack, and answer vectors take O(n) space.

### Problem description

There are n 1-indexed robots, each having a position on a line, health, and movement direction. 
 
 You are given 0-indexed integer arrays positions , healths , and a string directions ( directions[i] is either 'L' for left or 'R' for right ). All integers in positions are unique . 
 
 All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide . 
 
 If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one . The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line. 
 
 Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final health of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array. 
 
 Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur. 
 
 Note: The positions may be unsorted. 

 Example 1: 
 
 [Figure: https://assets.leetcode.com/uploads/2023/05/15/image-20230516011718-12.png] 
 
```
Input:
 positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"

Output:
 [2,17,9,15,10]

Explanation:
 No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].
```

 Example 2: 
 
 [Figure: https://assets.leetcode.com/uploads/2023/05/15/image-20230516004433-7.png] 
 
```
Input:
 positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"

Output:
 [14]

Explanation:
 There are 2 collisions in this example. Firstly, robot 1 and robot 2 will collide, and since both have the same health, they will be removed from the line. Next, robot 3 and robot 4 will collide and since robot 4's health is smaller, it gets removed, and robot 3's health becomes 15 - 1 = 14. Only robot 3 remains, so we return [14].
```

 Example 3: 
 
 [Figure: https://assets.leetcode.com/uploads/2023/05/15/image-20230516005114-9.png] 
 
```
Input:
 positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"

Output:
 []

Explanation:
 Robot 1 and robot 2 will collide and since both have the same health, they are both removed. Robot 3 and 4 will collide and since both have the same health, they are both removed. So, we return an empty array, [].
```

 Constraints: 

 1 <= positions.length == healths.length == directions.length == n <= 10 5 
 
 1 <= positions[i], healths[i] <= 10 9 
 
 directions[i] == 'L' or directions[i] == 'R' 
 
 All values in positions are distinct

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int> survivedRobotsHealths(vector<int>& positions,vector<int>& healths,string directions){int n=positions.size();vector<int>order(n);iota(order.begin(),order.end(),0);sort(order.begin(),order.end(),[&](int a,int b){return positions[a]<positions[b];});vector<int>st;for(int i:order){if(directions[i]=='R'){st.push_back(i);continue;}while(!st.empty()&&healths[i]>0){int j=st.back();if(healths[j]<healths[i]){healths[j]=0;--healths[i];st.pop_back();}else if(healths[j]==healths[i]){healths[j]=healths[i]=0;st.pop_back();}else{--healths[j];healths[i]=0;}}}vector<int>ans;for(int x:healths)if(x>0)ans.push_back(x);return ans;}};
```


## 2860. Happy Students

**Problem:** https://leetcode.com/problems/happy-students/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Enumeration

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) auxiliary for std::sort

**Complexity reasoning:** Sorting dominates the O(n) scan of valid selection boundaries.

### Problem description

You are given a 0-indexed integer array nums of length n where n is the total number of students in the class. The class teacher tries to select a group of students so that all the students remain happy. 
 
 The i th student will become happy if one of these two conditions is met: 

 The student is selected and the total number of selected students is strictly greater than nums[i] . 
 
 The student is not selected and the total number of selected students is strictly less than nums[i] . 

 Return the number of ways to select a group of students so that everyone remains happy. 

 Example 1: 
 
```
Input:
 nums = [1,1]

Output:
 2

Explanation:
 
The two possible ways are:
The class teacher selects no student.
The class teacher selects both students to form the group. 
If the class teacher selects just one student to form a group then the both students will not be happy. Therefore, there are only two possible ways.
```

 Example 2: 
 
```
Input:
 nums = [6,0,3,3,6,7,2,7]

Output:
 3

Explanation:
 
The three possible ways are:
The class teacher selects the student with index = 1 to form the group.
The class teacher selects the students with index = 1, 2, 3, 6 to form the group.
The class teacher selects all the students to form the group.
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 0 <= nums[i] < nums.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:int countWays(vector<int>& nums){sort(nums.begin(),nums.end());int n=nums.size(),ans=(nums[0]>0);for(int i=1;i<n;++i)if(nums[i-1]<i&&nums[i]>i)++ans;if(nums[n-1]<n)++ans;return ans;}};
```


## 2943. Maximize Area of Square Hole in Grid

**Problem:** https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(h log h + v log v)

**Space complexity:** O(log h + log v) auxiliary for sorting

**Complexity reasoning:** The two bar lists are sorted separately and each scanned once to find the longest consecutive run; h and v are their lengths.

### Problem description

You are given the two integers, n and m and two integer arrays, hBars and vBars . The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1 . 
 
 You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. Note that other bars are fixed and cannot be removed. 
 
 Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none). 

 Example 1: 
 
 [Figure: https://assets.leetcode.com/uploads/2023/11/05/screenshot-from-2023-11-05-22-40-25.png] 

 Input: n = 2, m = 1, hBars = [2,3], vBars = [2] 
 
 Output: 4 
 
 Explanation: 
 
 The left image shows the initial grid formed by the bars. The horizontal bars are [1,2,3,4] , and the vertical bars are  [1,2,3] . 
 
 One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2. 

 Example 2: 
 
 [Figure: https://assets.leetcode.com/uploads/2023/11/04/screenshot-from-2023-11-04-17-01-02.png] 

 Input: n = 1, m = 1, hBars = [2], vBars = [2] 
 
 Output: 4 
 
 Explanation: 
 
 To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2. 

 Example 3: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/03/12/unsaved-image-2.png] 

 Input: n = 2, m = 3, hBars = [2,3], vBars = [2,4] 
 
 Output: 4 
 
 Explanation: 
 
 One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4. 

 Constraints: 

 1 <= n <= 10 9 
 
 1 <= m <= 10 9 
 
 1 <= hBars.length <= 100 
 
 2 <= hBars[i] <= n + 1 
 
 1 <= vBars.length <= 100 
 
 2 <= vBars[i] <= m + 1 
 
 All values in hBars are distinct. 
 
 All values in vBars are distinct.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution{int run(vector<int>& a){sort(a.begin(),a.end());int best=1,cur=1;for(int i=1;i<(int)a.size();i++){cur=(a[i]==a[i-1]+1)?cur+1:1;best=max(best,cur);}return best+1;}public:int maximizeSquareHoleArea(int n,int m,vector<int>& hBars,vector<int>& vBars){int side=min(run(hBars),run(vBars));return side*side;}};
```


## 3010. Divide an Array Into Subarrays With Minimum Cost I

**Problem:** https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting, Enumeration

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One pass maintains the two smallest elements after index zero.

### Problem description

You are given an array of integers nums of length n . 
 
 The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3 . 
 
 You need to divide nums into 3 disjoint contiguous subarrays . 
 
 Return the minimum possible sum of the cost of these subarrays . 

 Example 1: 
 
```
Input:
 nums = [1,2,3,12]

Output:
 6

Explanation:
 The best possible way to form 3 subarrays is: [1], [2], and [3,12] at a total cost of 1 + 2 + 3 = 6.
The other possible ways to form 3 subarrays are:
- [1], [2,3], and [12] at a total cost of 1 + 2 + 12 = 15.
- [1,2], [3], and [12] at a total cost of 1 + 3 + 12 = 16.
```

 Example 2: 
 
```
Input:
 nums = [5,4,3]

Output:
 12

Explanation:
 The best possible way to form 3 subarrays is: [5], [4], and [3] at a total cost of 5 + 4 + 3 = 12.
It can be shown that 12 is the minimum cost achievable.
```

 Example 3: 
 
```
Input:
 nums = [10,3,1,1]

Output:
 12

Explanation:
 The best possible way to form 3 subarrays is: [10,3], [1], and [1] at a total cost of 10 + 1 + 1 = 12.
It can be shown that 12 is the minimum cost achievable.
```

 Constraints: 

 3 <= n <= 50 
 
 1 <= nums[i] <= 50

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int minimumCost(vector<int>& nums){int a=INT_MAX,b=INT_MAX;for(int i=1;i<(int)nums.size();++i){int x=nums[i];if(x<a)b=a,a=x;else if(x<b)b=x;}return nums[0]+a+b;}};
```


## 3011. Find if Array Can Be Sorted

**Problem:** https://leetcode.com/problems/find-if-array-can-be-sorted/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Bit Manipulation, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** The input is copied, each contiguous equal-popcount run is sorted, and the result is checked in O(n). The copied vector uses O(n) space.

### Problem description

You are given a 0-indexed array of positive integers nums . 
 
 In one operation , you can swap any two adjacent elements if they have the same number of set bits . You are allowed to do this operation any number of times ( including zero ). 
 
 Return true if you can sort the array in ascending order, else return false . 

 Example 1: 
 
```
Input:
 nums = [8,4,2,30,15]

Output:
 true

Explanation:
 Let's look at the binary representation of every element. The numbers 2, 4, and 8 have one set bit each with binary representation "10", "100", and "1000" respectively. The numbers 15 and 30 have four set bits each with binary representation "1111" and "11110".
We can sort the array using 4 operations:
- Swap nums[0] with nums[1]. This operation is valid because 8 and 4 have one set bit each. The array becomes [4,8,2,30,15].
- Swap nums[1] with nums[2]. This operation is valid because 8 and 2 have one set bit each. The array becomes [4,2,8,30,15].
- Swap nums[0] with nums[1]. This operation is valid because 4 and 2 have one set bit each. The array becomes [2,4,8,30,15].
- Swap nums[3] with nums[4]. This operation is valid because 30 and 15 have four set bits each. The array becomes [2,4,8,15,30].
The array has become sorted, hence we return true.
Note that there may be other sequences of operations which also sort the array.
```

 Example 2: 
 
```
Input:
 nums = [1,2,3,4,5]

Output:
 true

Explanation:
 The array is already sorted, hence we return true.
```

 Example 3: 
 
```
Input:
 nums = [3,16,8,4,2]

Output:
 false

Explanation:
 It can be shown that it is not possible to sort the input array using any number of operations.
```

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 2 8

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool canSortArray(vector<int>& nums){vector<int>a=nums;int n=a.size();for(int i=0;i<n;){int j=i+1;while(j<n&&__builtin_popcount((unsigned)a[j])==__builtin_popcount((unsigned)a[i]))++j;sort(a.begin()+i,a.begin()+j);i=j;}return is_sorted(a.begin(),a.end());}};
```


## 3169. Count Days Without Meetings

**Problem:** https://leetcode.com/problems/count-days-without-meetings/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) auxiliary for std::sort

**Complexity reasoning:** Sorting meeting intervals dominates the linear union-coverage sweep.

### Problem description

You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive). 
 
 Return the count of days when the employee is available for work but no meetings are scheduled. 
 
 Note: The meetings may overlap. 

 Example 1: 

 Input: days = 10, meetings = [[5,7],[1,3],[9,10]] 
 
 Output: 2 
 
 Explanation: 
 
 There is no meeting scheduled on the 4 th and 8 th days. 

 Example 2: 

 Input: days = 5, meetings = [[2,4],[1,3]] 
 
 Output: 1 
 
 Explanation: 
 
 There is no meeting scheduled on the 5 th day. 

 Example 3: 

 Input: days = 6, meetings = [[1,6]] 
 
 Output: 0 
 
 Explanation: 
 
 Meetings are scheduled for all working days. 

 Constraints: 

 1 <= days <= 10 9 
 
 1 <= meetings.length <= 10 5 
 
 meetings[i].length == 2 
 
 1 <= meetings[i][0] <= meetings[i][1] <= days

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int countDays(int days,vector<vector<int>>& meetings){sort(meetings.begin(),meetings.end());int covered=0,end=0;for(auto&v:meetings){int l=max(end+1,v[0]);if(l<=v[1])covered+=v[1]-l+1;end=max(end,v[1]);}return days-covered;}};
```


## 3394. Check if Grid can be Cut into Sections

**Problem:** https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Each axis check builds and sorts n projected intervals, then scans them. The temporary projection vector uses O(n) space; up to two checks are performed.

### Problem description

You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles , where rectangles[i] is in the form [start x , start y , end x , end y ] , representing a rectangle on the grid. Each rectangle is defined as follows: 

 (start x , start y ) : The bottom-left corner of the rectangle. 
 
 (end x , end y ) : The top-right corner of the rectangle. 

 Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that: 

 Each of the three resulting sections formed by the cuts contains at least one rectangle. 
 
 Every rectangle belongs to exactly one section. 

 Return true if such cuts can be made; otherwise, return false . 

 Example 1: 

 Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]] 
 
 Output: true 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/10/23/tt1drawio.png] 
 
 The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4 . Hence, output is true. 

 Example 2: 

 Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]] 
 
 Output: true 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/10/23/tc2drawio.png] 
 
 We can make vertical cuts at x = 2 and x = 3 . Hence, output is true. 

 Example 3: 

 Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]] 
 
 Output: false 
 
 Explanation: 
 
 We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false. 

 Constraints: 

 3 <= n <= 10 9 
 
 3 <= rectangles.length <= 10 5 
 
 0 <= rectangles[i][0] < rectangles[i][2] <= n 
 
 0 <= rectangles[i][1] < rectangles[i][3] <= n 
 
 No two rectangles overlap.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {bool ok(vector<vector<int>>&a,int axis){vector<pair<int,int>>v;for(auto&r:a)v.push_back({r[axis],r[axis+2]});sort(v.begin(),v.end());int groups=0,end=-1;for(auto p:v){if(groups==0||p.first>=end){groups++;end=p.second;}else end=max(end,p.second);}return groups>=3;}public:bool checkValidCuts(int n,vector<vector<int>>&rectangles){return ok(rectangles,0)||ok(rectangles,1);}};
```


## 3446. Sort Matrix by Diagonals

**Problem:** https://leetcode.com/problems/sort-matrix-by-diagonals/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Matrix

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n² log n)

**Space complexity:** O(n) auxiliary, excluding the returned matrix

**Complexity reasoning:** Each of 2n-1 diagonals is extracted, sorted, and written back; the total is O(n² log n). The largest temporary diagonal holds n elements.

### Problem description

You are given an n x n square matrix of integers grid . Return the matrix such that: 

 The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order . 
 
 The diagonals in the top-right triangle are sorted in non-decreasing order . 

 Example 1: 

 Input: grid = [[1,7,3],[9,8,2],[4,5,6]] 
 
 Output: [[8,2,3],[9,6,7],[4,5,1]] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/12/29/4052example1drawio.png] 
 
 The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order: 

 [1, 8, 6] becomes [8, 6, 1] . 
 
 [9, 5] and [4] remain unchanged. 

 The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order: 

 [7, 2] becomes [2, 7] . 
 
 [3] remains unchanged. 

 Example 2: 

 Input: grid = [[0,1],[1,2]] 
 
 Output: [[2,1],[1,0]] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/12/29/4052example2adrawio.png] 
 
 The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0] . The other diagonals are already in the correct order. 

 Example 3: 

 Input: grid = [[1]] 
 
 Output: [[1]] 
 
 Explanation: 
 
 Diagonals with exactly one element are already in order, so no changes are needed. 

 Constraints: 

 grid.length == grid[i].length == n 
 
 1 <= n <= 10 
 
 -10 5 <= grid[i][j] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<vector<int>> sortMatrix(vector<vector<int>>& grid){int n=grid.size();for(int d=-(n-1);d<n;++d){vector<int>v;for(int i=max(0,d);i<n&&i-d<n;++i)v.push_back(grid[i][i-d]);if(d>=0)sort(v.rbegin(),v.rend());else sort(v.begin(),v.end());int p=0;for(int i=max(0,d);i<n&&i-d<n;++i)grid[i][i-d]=v[p++];}return grid;}};
```


## 3537. Fill a Special Grid

**Problem:** https://leetcode.com/problems/fill-a-special-grid/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Divide and Conquer, Matrix

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(4^n) = O(s²), s = 2^n

**Space complexity:** O(4^n) output plus O(n) recursion stack

**Complexity reasoning:** Four recursive calls fill every cell of the s-by-s result exactly once; recursion depth is n.

### Problem description

You are given a non-negative integer n representing a 2 n x 2 n grid. You must fill the grid with integers from 0 to 2 2n - 1 to make it special . A grid is special if it satisfies all the following conditions: 

 All numbers in the top-right quadrant are smaller than those in the bottom-right quadrant. 
 
 All numbers in the bottom-right quadrant are smaller than those in the bottom-left quadrant. 
 
 All numbers in the bottom-left quadrant are smaller than those in the top-left quadrant. 
 
 Each of its quadrants is also a special grid. 

 Return the special 2 n x 2 n grid. 
 
 Note : Any 1x1 grid is special. 

 Example 1: 

 Input: n = 0 
 
 Output: [[0]] 
 
 Explanation: 
 
 The only number that can be placed is 0, and there is only one possible position in the grid. 

 Example 2: 

 Input: n = 1 
 
 Output: [[3,0],[2,1]] 
 
 Explanation: 
 
 The numbers in each quadrant are: 

 Top-right: 0 
 
 Bottom-right: 1 
 
 Bottom-left: 2 
 
 Top-left: 3 

 Since 0 < 1 < 2 < 3 , this satisfies the given constraints. 

 Example 3: 

 Input: n = 2 
 
 Output: [[15,12,3,0],[14,13,2,1],[11,8,7,4],[10,9,6,5]] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2025/03/05/4123example3p1drawio.png] 
 
 The numbers in each quadrant are: 

 Top-right: 3, 0, 2, 1 
 
 Bottom-right: 7, 4, 6, 5 
 
 Bottom-left: 11, 8, 10, 9 
 
 Top-left: 15, 12, 14, 13 
 
 max(3, 0, 2, 1) < min(7, 4, 6, 5) 
 
 max(7, 4, 6, 5) < min(11, 8, 10, 9) 
 
 max(11, 8, 10, 9) < min(15, 12, 14, 13) 

 This satisfies the first three requirements. Additionally, each quadrant is also a special grid. Thus, this is a special grid. 

 Constraints: 

 0 <= n <= 10

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    void fillGrid(vector<vector<int>>& a,int r,int c,int size,int base) {
        if (size==1) {a[r][c]=base;return;}
        int h=size/2, area=h*h;
        fillGrid(a,r,c+h,h,base);
        fillGrid(a,r+h,c+h,h,base+area);
        fillGrid(a,r+h,c,h,base+2*area);
        fillGrid(a,r,c,h,base+3*area);
    }
public:
    vector<vector<int>> specialGrid(int n) {
        int size=1<<n;
        vector<vector<int>> a(size,vector<int>(size));
        fillGrid(a,0,0,size,0);
        return a;
    }
};
```


## 3567. Minimum Absolute Difference in Sliding Submatrix

**Problem:** https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Matrix

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O((m-k+1)(n-k+1) k² log k)

**Space complexity:** O((m-k+1)(n-k+1) + k²)

**Complexity reasoning:** Each k-by-k window copies k² entries, sorts and deduplicates them, then scans adjacent differences. Space includes the result and one window buffer.

### Problem description

You are given an m x n integer matrix grid and an integer k . 
 
 For every contiguous k x k submatrix of grid , compute the minimum absolute difference between any two distinct values within that submatrix . 
 
 Return a 2D array ans of size (m - k + 1) x (n - k + 1) , where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid . 
 
 Note : If all elements in the submatrix have the same value, the answer will be 0. 
A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2 .

 Example 1: 

 Input: grid = [[1,8],[3,-2]], k = 2 
 
 Output: [[2]] 
 
 Explanation: 

 There is only one possible k x k submatrix: [[1, 8], [3, -2]] . 
 
 Distinct values in the submatrix are [1, 8, 3, -2] . 
 
 The minimum absolute difference in the submatrix is |1 - 3| = 2 . Thus, the answer is [[2]] . 

 Example 2: 

 Input: grid = [[3,-1]], k = 1 
 
 Output: [[0,0]] 
 
 Explanation: 

 Both k x k submatrix has only one distinct element. 
 
 Thus, the answer is [[0, 0]] . 

 Example 3: 

 Input: grid = [[1,-2,3],[2,3,5]], k = 2 
 
 Output: [[1,2]] 
 
 Explanation: 

 There are two possible k × k submatrix:

 Starting at (0, 0) : [[1, -2], [2, 3]] .

 Distinct values in the submatrix are [1, -2, 2, 3] . 
 
 The minimum absolute difference in the submatrix is |1 - 2| = 1 . 

 Starting at (0, 1) : [[-2, 3], [3, 5]] .

 Distinct values in the submatrix are [-2, 3, 5] . 
 
 The minimum absolute difference in the submatrix is |3 - 5| = 2 . 

 Thus, the answer is [[1, 2]] . 

 Constraints: 

 1 <= m == grid.length <= 30 
 
 1 <= n == grid[i].length <= 30 
 
 -10 5 <= grid[i][j] <= 10 5 
 
 1 <= k <= min(m, n)

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:
 vector<vector<int>> minAbsDiff(vector<vector<int>>& grid,int k){
  int m=grid.size(),n=grid[0].size();vector<vector<int>> ans(m-k+1,vector<int>(n-k+1));
  for(int i=0;i+k<=m;++i)for(int j=0;j+k<=n;++j){
   vector<int> a;for(int x=i;x<i+k;++x)for(int y=j;y<j+k;++y)a.push_back(grid[x][y]);
   sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());
   int best=INT_MAX;for(int t=1;t<(int)a.size();++t)best=min(best,a[t]-a[t-1]);
   ans[i][j]=best==INT_MAX?0:best;
  }return ans;
 }
};
```


## 3631. Sort Threats by Severity and Exploitability

**Problem:** https://leetcode.com/problems/sort-threats-by-severity-and-exploitability/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) auxiliary for std::sort

**Complexity reasoning:** The comparator computes constant-time weighted scores; sorting dominates. The vector is returned by value without requiring an additional full copy.

### Problem description

You are given a 2D integer array threats , where each threats[i] = [ID i , sev i ​, exp i ] 

 ID i : Unique identifier of the threat. 
 
 sev i : Indicates the severity of the threat. 
 
 exp i : Indicates the exploitability of the threat. 

 The score of a threat i is defined as: score = 2 × sev i + exp i 
 
 Your task is to return threats sorted in descending order of score . 
 
 If multiple threats have the same score, sort them by ascending ID ​​​​​​​. 

 Example 1: 

 Input: threats = [[101,2,3],[102,3,2],[103,3,3]] 
 
 Output: [[103,3,3],[102,3,2],[101,2,3]] 
 
 Explanation: 

 Threat 
 ID 
 sev 
 exp 
 Score = 2 × sev + exp 

 threats[0] 
 101 
 2 
 3 
 2 × 2 + 3 = 7 

 threats[1] 
 102 
 3 
 2 
 2 × 3 + 2 = 8 

 threats[2] 
 103 
 3 
 3 
 2 × 3 + 3 = 9 

 Sorted Order: [[103, 3, 3], [102, 3, 2], [101, 2, 3]] 

 Example 2: 

 Input: threats = [[101,4,1],[103,1,5],[102,1,5]] 
 
 Output: [[101,4,1],[102,1,5],[103,1,5]] 
 
 Explanation:​​​​​​​ 

 Threat 
 ID 
 sev 
 exp 
 Score = 2 × sev + exp 

 threats[0] 
 101 
 4 
 1 
 2 × 4 + 1 = 9 

 threats[1] 
 103 
 1 
 5 
 2 × 1 + 5 = 7 

 threats[2] 
 102 
 1 
 5 
 2 × 1 + 5 = 7 

 threats[1] and threats[2] have same score, thus sort them by ascending ID. 
 
 Sorted Order: [[101, 4, 1], [102, 1, 5], [103, 1, 5]] 

 Constraints: 

 1 <= threats.length <= 10 5 
 
 threats[i] == [ID i , sev i , exp i ] 
 
 1 <= ID i <= 10 6 
 
 1 <= sev i <= 10 9 
 
 1 <= exp i <= 10 9 
 
 All ID i are unique

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> sortThreats(vector<vector<int>>& threats) {
        sort(threats.begin(),threats.end(),[](const vector<int>& a,const vector<int>& b) {
            long long sa=2LL*a[1]+a[2],sb=2LL*b[1]+b[2];
            return sa==sb?a[0]<b[0]:sa>sb;
        });
        return threats;
    }
};
```


## 3769. Sort Integers by Binary Reflection

**Problem:** https://leetcode.com/problems/sort-integers-by-binary-reflection/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n · w)

**Space complexity:** O(log n) auxiliary for std::sort

**Complexity reasoning:** Sorting makes O(n log n) comparisons, each reversing up to w bits of two integers. For fixed-width integers w is constant, giving O(n log n) time.

### Problem description

You are given an integer array nums . 
 
 The binary reflection of a positive integer is defined as the number obtained by reversing the order of its binary digits (ignoring any leading zeros) and interpreting the resulting binary number as a decimal. 
 
 Sort the array in ascending order based on the binary reflection of each element. If two different numbers have the same binary reflection, the smaller original number should appear first. 
 
 Return the resulting sorted array. 

 Example 1: 

 Input: nums = [4,5,4] 
 
 Output: [4,4,5] 
 
 Explanation: 
 
 Binary reflections are: 

 4 -> (binary) 100 -> (reversed) 001 -> 1 
 
 5 -> (binary) 101 -> (reversed) 101 -> 5 
 
 4 -> (binary) 100 -> (reversed) 001 -> 1 
 
Sorting by the reflected values gives [4, 4, 5] . 
 
 Example 2: 

 Input: nums = [3,6,5,8] 
 
 Output: [8,3,6,5] 
 
 Explanation: 
 
 Binary reflections are: 

 3 -> (binary) 11 -> (reversed) 11 -> 3 
 
 6 -> (binary) 110 -> (reversed) 011 -> 3 
 
 5 -> (binary) 101 -> (reversed) 101 -> 5 
 
 8 -> (binary) 1000 -> (reversed) 0001 -> 1 
 
Sorting by the reflected values gives [8, 3, 6, 5] . 
Note that 3 and 6 have the same reflection, so we arrange them in increasing order of original value. 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { int rev(int x){int r=0;while(x){r=(r<<1)|(x&1);x>>=1;}return r;} public: vector<int> sortByReflection(vector<int>& nums) { sort(nums.begin(),nums.end(),[&](int a,int b){int x=rev(a),y=rev(b);return x==y?a<b:x<y;});return nums; } };
```


## 3774. Absolute Difference Between Maximum and Minimum K Elements

**Problem:** https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n + k)

**Space complexity:** O(log n) auxiliary for std::sort

**Complexity reasoning:** Sorting is followed by a k-element accumulation; k <= n, so overall O(n log n).

### Problem description

You are given an integer array nums and an integer k . 
 
 Find the absolute difference between: 

 the sum of the k largest elements in the array; and 
 
 the sum of the k smallest elements in the array. 

 Return an integer denoting this difference. 

 Example 1: 

 Input: nums = [5,2,2,4], k = 2 
 
 Output: 5 
 
 Explanation: 

 The k = 2 largest elements are 4 and 5. Their sum is 4 + 5 = 9 . 
 
 The k = 2 smallest elements are 2 and 2. Their sum is 2 + 2 = 4 . 
 
 The absolute difference is abs(9 - 4) = 5 . 

 Example 2: 

 Input: nums = [100], k = 1 
 
 Output: 0 
 
 Explanation: 

 The largest element is 100. 
 
 The smallest element is 100. 
 
 The absolute difference is abs(100 - 100) = 0 . 

 Constraints: 

 1 <= n == nums.length <= 100 
 
 1 <= nums[i] <= 100 
 
 1 <= k <= n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int absDifference(vector<int>& nums,int k) { sort(nums.begin(),nums.end());int n=nums.size(),ans=0;for(int i=0;i<k;++i)ans+=nums[n-1-i]-nums[i];return ans; } };
```


## 3951. Minimum Energy to Maintain Brightness

**Problem:** https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) auxiliary for std::sort

**Complexity reasoning:** Sorting intervals dominates the O(n) merge-and-count scan.

### Problem description

You are given an integer n , representing n light bulbs arranged in a line and indexed from 0 to n - 1 . 
 
 You are also given an integer brightness and a 2D integer array intervals , where intervals[i] = [start i , end i ] represents an inclusive time interval during which the lighting requirement must be satisfied. 
 
 At each time unit, every bulb can independently be either on or off. A bulb that is on illuminates its own position and its adjacent positions, if they exist. 
 
 The total illumination at a time unit is the number of illuminated positions. Each position is counted at most once . 
 
 For every integer time unit covered by at least one interval in intervals , the total illumination must be at least brightness . At time units not covered by any interval, all bulbs may remain off. Each bulb that is on consumes 1 unit of energy for that time unit. 
 
 Return an integer denoting the minimum total energy required. 

 Example 1: 

 Input: n = 5, brightness = 5, intervals = [[6,12]] 
 
 Output: 14 
 
 Explanation: 

 Turn on the light bulbs at positions 1 and 4. 
 
 Current state of line: 0 1 0 0 1 . 
 
 All 5 positions are illuminated, so the required brightness is reached. 
 
 The active interval has length 12 - 6 + 1 = 7 , so the total energy is 2 * 7 = 14 . 

 Example 2: 

 Input: n = 2, brightness = 1, intervals = [[0,0],[2,2]] 
 
 Output: 2 
 
 Explanation: 

 Turn on one light bulb during each active interval. 
 
 Each interval has length 1, so the total active time is 1 + 1 = 2 . 
 
 The total energy is 1 * 2 = 2 . 

 Example 3: 

 Input: n = 4, brightness = 2, intervals = [[1,3],[2,4]] 
 
 Output: 4 
 
 Explanation: 

 Turn on one light bulb. It can illuminate at least 2 positions. 
 
 The active intervals overlap, so the total active time is the length of [1,4] , which is 4. 
 
 The total energy is 1 * 4 = 4 . 

 Constraints: 

 1 <= n <= 10 6 
 
 1 <= brightness <= n 
 
 1 <= intervals.length <= 10 5 
 
 intervals[i] == [start i , end i ] 
 
 0 <= start i <= end i <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    long long minEnergy(int n,int brightness,vector<vector<int>>& intervals){
        sort(intervals.begin(),intervals.end());
        long long total=0;
        long long l=intervals[0][0],r=intervals[0][1];
        for(int i=1;i<(int)intervals.size();++i){
            long long a=intervals[i][0],b=intervals[i][1];
            if(a<=r+1) r=max(r,b);
            else{total+=r-l+1;l=a;r=b;}
        }
        total+=r-l+1;
        return total*((brightness+2LL)/3);
    }
};
```


## 3975. Filter Occupied Intervals

**Problem:** https://leetcode.com/problems/filter-occupied-intervals/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting

**Primary pattern:** Sorting / Divide and Conquer

**Related patterns:** Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Order elements to expose structure or split into manageable halves.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Sorting and merging the n occupied intervals dominates; the merged and result vectors can each hold O(n) intervals.

### Problem description

You are given a 2D integer array occupiedIntervals , where occupiedIntervals[i] = [start i , end i ] represents a time interval during which you are occupied. Each interval starts at start i and ends at end i , inclusive . These intervals may overlap . 
 
 You are also given two integers freeStart and freeEnd , which define a free time interval from freeStart to freeEnd , inclusive. 
 
 Your task is to merge all occupied intervals that overlap or touch, then remove all integer points in the free interval from the merged occupied intervals. 
 
 Two intervals touch if the second interval starts immediately after the first one ends. For example, [1, 1] and [2, 2] touch and should be merged into [1, 2] . 
 
 Return the remaining occupied intervals in sorted order. The returned intervals must be non-overlapping and must contain the minimum number of intervals possible. If there are no remaining occupied points, return an empty list. 

 Example 1: 

 Input: occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11 
 
 Output: [[2,6],[12,12],[14,16]] 
 
 Explanation: 

 After merging, the occupied intervals are [2, 8] , [10, 12] , and [14, 16] . 
 
 Excluding the free interval [7, 11] results in [2, 6] , [12, 12] , and [14, 16] . 

 Example 2: 

 Input: occupiedIntervals = [[1,5],[2,3]], freeStart = 3, freeEnd = 8 
 
 Output: [[1,2]] 
 
 Explanation: 

 After merging, the occupied interval is [1, 5] . 
 
 Excluding the free interval [3, 8] results in [1, 2] . 

 Constraints: 

 1 <= occupiedIntervals.length <= 5 * 10 4 
 
 occupiedIntervals[i].length == 2 
 
 1 <= start i <= end i <= 10 9 
 
 1 <= freeStart <= freeEnd <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> filterOccupiedIntervals(vector<vector<int>>& occupiedIntervals,
                                                 int freeStart,int freeEnd) {
        sort(occupiedIntervals.begin(),occupiedIntervals.end());
        vector<vector<int>> merged,ans;
        for(const auto& v:occupiedIntervals){
            if(merged.empty() || (long long)v[0]>1LL+merged.back()[1])
                merged.push_back(v);
            else merged.back()[1]=max(merged.back()[1],v[1]);
        }
        for(const auto& v:merged){
            int l=v[0],r=v[1];
            if(l<freeStart)ans.push_back({l,min(r,freeStart-1)});
            if(r>freeEnd)ans.push_back({max(l,freeEnd+1),r});
        }
        return ans;
    }
};
```

