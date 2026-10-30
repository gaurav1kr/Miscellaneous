# Simulation / Implementation

**Problems:** 159

## Quick revision checklist

Directly model operations, states, and edge cases.

## Problem index

- [54. Spiral Matrix](#54-spiral-matrix) — Medium; code: yes
- [57. Insert Interval](#57-insert-interval) — Medium; code: yes
- [59. Spiral Matrix II](#59-spiral-matrix-ii) — Medium; code: yes
- [157. Read N Characters Given Read4](#157-read-n-characters-given-read4) — Easy; code: yes
- [158. Read N Characters Given read4 II - Call Multiple Times](#158-read-n-characters-given-read4-ii---call-multiple-times) — Hard; code: yes
- [163. Missing Ranges](#163-missing-ranges) — Easy; code: yes
- [228. Summary Ranges](#228-summary-ranges) — Easy; code: yes
- [289. Game of Life](#289-game-of-life) — Medium; code: yes
- [422. Valid Word Square](#422-valid-word-square) — Easy; code: yes
- [485. Max Consecutive Ones](#485-max-consecutive-ones) — Easy; code: yes
- [495. Teemo Attacking](#495-teemo-attacking) — Easy; code: yes
- [498. Diagonal Traverse](#498-diagonal-traverse) — Medium; code: yes
- [566. Reshape the Matrix](#566-reshape-the-matrix) — Easy; code: yes
- [661. Image Smoother](#661-image-smoother) — Easy; code: yes
- [665. Non-decreasing Array](#665-non-decreasing-array) — Medium; code: yes
- [674. Longest Continuous Increasing Subsequence](#674-longest-continuous-increasing-subsequence) — Easy; code: yes
- [717. 1-bit and 2-bit Characters](#717-1-bit-and-2-bit-characters) — Easy; code: yes
- [755. Pour Water](#755-pour-water) — Medium; code: yes
- [766. Toeplitz Matrix](#766-toeplitz-matrix) — Easy; code: yes
- [794. Valid Tic-Tac-Toe State](#794-valid-tic-tac-toe-state) — Medium; code: yes
- [835. Image Overlap](#835-image-overlap) — Medium; code: yes
- [849. Maximize Distance to Closest Person](#849-maximize-distance-to-closest-person) — Medium; code: yes
- [867. Transpose Matrix](#867-transpose-matrix) — Easy; code: yes
- [885. Spiral Matrix III](#885-spiral-matrix-iii) — Medium; code: yes
- [896. Monotonic Array](#896-monotonic-array) — Easy; code: yes
- [915. Partition Array into Disjoint Intervals](#915-partition-array-into-disjoint-intervals) — Medium; code: yes
- [941. Valid Mountain Array](#941-valid-mountain-array) — Easy; code: yes
- [985. Sum of Even Numbers After Queries](#985-sum-of-even-numbers-after-queries) — Medium; code: yes
- [999. Available Captures for Rook](#999-available-captures-for-rook) — Easy; code: yes
- [1184. Distance Between Bus Stops](#1184-distance-between-bus-stops) — Easy; code: yes
- [1222. Queens That Can Attack the King](#1222-queens-that-can-attack-the-king) — Medium; code: yes
- [1243. Array Transformation](#1243-array-transformation) — Easy; code: yes
- [1260. Shift 2D Grid](#1260-shift-2d-grid) — Easy; code: yes
- [1272. Remove Interval](#1272-remove-interval) — Medium; code: yes
- [1287. Element Appearing More Than 25% In Sorted Array](#1287-element-appearing-more-than-25-in-sorted-array) — Easy; code: yes
- [1299. Replace Elements with Greatest Element on Right Side](#1299-replace-elements-with-greatest-element-on-right-side) — Easy; code: yes
- [1313. Decompress Run-Length Encoded List](#1313-decompress-run-length-encoded-list) — Easy; code: yes
- [1375. Number of Times Binary String Is Prefix-Aligned](#1375-number-of-times-binary-string-is-prefix-aligned) — Medium; code: yes
- [1380. Lucky Numbers in a Matrix](#1380-lucky-numbers-in-a-matrix) — Easy; code: yes
- [1389. Create Target Array in the Given Order](#1389-create-target-array-in-the-given-order) — Easy; code: yes
- [1431. Kids With the Greatest Number of Candies](#1431-kids-with-the-greatest-number-of-candies) — Easy; code: yes
- [1437. Check If All 1's Are at Least Length K Places Away](#1437-check-if-all-1-s-are-at-least-length-k-places-away) — Easy; code: yes
- [1450. Number of Students Doing Homework at a Given Time](#1450-number-of-students-doing-homework-at-a-given-time) — Easy; code: yes
- [1470. Shuffle the Array](#1470-shuffle-the-array) — Easy; code: yes
- [1503. Last Moment Before All Ants Fall Out of a Plank](#1503-last-moment-before-all-ants-fall-out-of-a-plank) — Medium; code: yes
- [1534. Count Good Triplets](#1534-count-good-triplets) — Easy; code: yes
- [1535. Find the Winner of an Array Game](#1535-find-the-winner-of-an-array-game) — Medium; code: yes
- [1550. Three Consecutive Odds](#1550-three-consecutive-odds) — Easy; code: yes
- [1560. Most Visited Sector in  a Circular Track](#1560-most-visited-sector-in-a-circular-track) — Easy; code: yes
- [1566. Detect Pattern of Length M Repeated K or More Times](#1566-detect-pattern-of-length-m-repeated-k-or-more-times) — Easy; code: yes
- [1572. Matrix Diagonal Sum](#1572-matrix-diagonal-sum) — Easy; code: yes
- [1582. Special Positions in a Binary Matrix](#1582-special-positions-in-a-binary-matrix) — Easy; code: yes
- [1583. Count Unhappy Friends](#1583-count-unhappy-friends) — Medium; code: yes
- [1599. Maximum Profit of Operating a Centennial Wheel](#1599-maximum-profit-of-operating-a-centennial-wheel) — Medium; code: yes
- [1620. Coordinate With Maximum Network Quality](#1620-coordinate-with-maximum-network-quality) — Medium; code: yes
- [1646. Get Maximum in Generated Array](#1646-get-maximum-in-generated-array) — Easy; code: yes
- [1672. Richest Customer Wealth](#1672-richest-customer-wealth) — Easy; code: yes
- [1701. Average Waiting Time](#1701-average-waiting-time) — Medium; code: yes
- [1706. Where Will the Ball Fall](#1706-where-will-the-ball-fall) — Medium; code: yes
- [1725. Number Of Rectangles That Can Form The Largest Square](#1725-number-of-rectangles-that-can-form-the-largest-square) — Easy; code: yes
- [1752. Check if Array Is Sorted and Rotated](#1752-check-if-array-is-sorted-and-rotated) — Easy; code: yes
- [1779. Find Nearest Point That Has the Same X or Y Coordinate](#1779-find-nearest-point-that-has-the-same-x-or-y-coordinate) — Easy; code: yes
- [1800. Maximum Ascending Subarray Sum](#1800-maximum-ascending-subarray-sum) — Easy; code: yes
- [1848. Minimum Distance to the Target Element](#1848-minimum-distance-to-the-target-element) — Easy; code: yes
- [1886. Determine Whether Matrix Can Be Obtained By Rotation](#1886-determine-whether-matrix-can-be-obtained-by-rotation) — Easy; code: yes
- [1909. Remove One Element to Make the Array Strictly Increasing](#1909-remove-one-element-to-make-the-array-strictly-increasing) — Easy; code: yes
- [1914. Cyclically Rotating a Grid](#1914-cyclically-rotating-a-grid) — Medium; code: yes
- [1920. Build Array from Permutation](#1920-build-array-from-permutation) — Easy; code: yes
- [1929. Concatenation of Array](#1929-concatenation-of-array) — Easy; code: yes
- [1958. Check if Move is Legal](#1958-check-if-move-is-legal) — Medium; code: yes
- [2012. Sum of Beauty in the Array](#2012-sum-of-beauty-in-the-array) — Medium; code: yes
- [2016. Maximum Difference Between Increasing Elements](#2016-maximum-difference-between-increasing-elements) — Easy; code: yes
- [2018. Check if Word Can Be Placed In Crossword](#2018-check-if-word-can-be-placed-in-crossword) — Medium; code: yes
- [2022. Convert 1D Array Into 2D Array](#2022-convert-1d-array-into-2d-array) — Easy; code: yes
- [2057. Smallest Index With Equal Value](#2057-smallest-index-with-equal-value) — Easy; code: yes
- [2061. Number of Spaces Cleaning Robot Cleaned](#2061-number-of-spaces-cleaning-robot-cleaned) — Medium; code: yes
- [2079. Watering Plants](#2079-watering-plants) — Medium; code: yes
- [2113. Elements in Array After Removing and Replacing Elements](#2113-elements-in-array-after-removing-and-replacing-elements) — Medium; code: yes
- [2155. All Divisions With the Highest Score of a Binary Array](#2155-all-divisions-with-the-highest-score-of-a-binary-array) — Medium; code: yes
- [2176. Count Equal and Divisible Pairs in an Array](#2176-count-equal-and-divisible-pairs-in-an-array) — Easy; code: yes
- [2210. Count Hills and Valleys in an Array](#2210-count-hills-and-valleys-in-an-array) — Easy; code: yes
- [2239. Find Closest Number to Zero](#2239-find-closest-number-to-zero) — Easy; code: yes
- [2257. Count Unguarded Cells in the Grid](#2257-count-unguarded-cells-in-the-grid) — Medium; code: yes
- [2293. Min Max Game](#2293-min-max-game) — Easy; code: yes
- [2303. Calculate Amount Paid in Taxes](#2303-calculate-amount-paid-in-taxes) — Easy; code: yes
- [2319. Check if Matrix Is X-Matrix](#2319-check-if-matrix-is-x-matrix) — Easy; code: yes
- [2373. Largest Local Values in a Matrix](#2373-largest-local-values-in-a-matrix) — Easy; code: yes
- [2432. The Employee That Worked on the Longest Task](#2432-the-employee-that-worked-on-the-longest-task) — Easy; code: yes
- [2482. Difference Between Ones and Zeros in Row and Column](#2482-difference-between-ones-and-zeros-in-row-and-column) — Medium; code: yes
- [2553. Separate the Digits in an Array](#2553-separate-the-digits-in-an-array) — Easy; code: yes
- [2639. Find the Width of Columns of a Grid](#2639-find-the-width-of-columns-of-a-grid) — Easy; code: yes
- [2643. Row With Maximum Ones](#2643-row-with-maximum-ones) — Easy; code: yes
- [2644. Find the Maximum Divisibility Score](#2644-find-the-maximum-divisibility-score) — Easy; code: yes
- [2660. Determine the Winner of a Bowling Game](#2660-determine-the-winner-of-a-bowling-game) — Easy; code: yes
- [2672. Number of Adjacent Elements With the Same Color](#2672-number-of-adjacent-elements-with-the-same-color) — Medium; code: yes
- [2717. Semi-Ordered Permutation](#2717-semi-ordered-permutation) — Easy; code: yes
- [2728. Count Houses in a Circular Street](#2728-count-houses-in-a-circular-street) — Easy; code: yes
- [2735. Collecting Chocolates](#2735-collecting-chocolates) — Medium; code: yes
- [2765. Longest Alternating Subarray](#2765-longest-alternating-subarray) — Easy; code: yes
- [2778. Sum of Squares of Special Elements ](#2778-sum-of-squares-of-special-elements) — Easy; code: yes
- [2798. Number of Employees Who Met the Target](#2798-number-of-employees-who-met-the-target) — Easy; code: yes
- [2855. Minimum Right Shifts to Sort the Array](#2855-minimum-right-shifts-to-sort-the-array) — Easy; code: yes
- [2899. Last Visited Integers](#2899-last-visited-integers) — Easy; code: yes
- [2908. Minimum Sum of Mountain Triplets I](#2908-minimum-sum-of-mountain-triplets-i) — Easy; code: yes
- [2923. Find Champion I](#2923-find-champion-i) — Easy; code: yes
- [2934. Minimum Operations to Maximize Last Elements in Arrays](#2934-minimum-operations-to-maximize-last-elements-in-arrays) — Medium; code: yes
- [2951. Find the Peaks](#2951-find-the-peaks) — Easy; code: yes
- [3000. Maximum Area of Longest Diagonal Rectangle](#3000-maximum-area-of-longest-diagonal-rectangle) — Easy; code: yes
- [3030. Find the Grid of Region Average](#3030-find-the-grid-of-region-average) — Medium; code: yes
- [3033. Modify the Matrix](#3033-modify-the-matrix) — Easy; code: yes
- [3038. Maximum Number of Operations With the Same Score I](#3038-maximum-number-of-operations-with-the-same-score-i) — Easy; code: yes
- [3065. Minimum Operations to Exceed Threshold Value I](#3065-minimum-operations-to-exceed-threshold-value-i) — Easy; code: yes
- [3073. Maximum Increasing Triplet Value](#3073-maximum-increasing-triplet-value) — Medium; code: yes
- [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](#3105-longest-strictly-increasing-or-strictly-decreasing-subarray) — Easy; code: yes
- [3127. Make a Square with the Same Color](#3127-make-a-square-with-the-same-color) — Easy; code: yes
- [3131. Find the Integer Added to Array I](#3131-find-the-integer-added-to-array-i) — Easy; code: yes
- [3142. Check if Grid Satisfies Conditions](#3142-check-if-grid-satisfies-conditions) — Easy; code: yes
- [3151. Special Array I](#3151-special-array-i) — Easy; code: yes
- [3175. Find The First Player to win K Games in a Row](#3175-find-the-first-player-to-win-k-games-in-a-row) — Medium; code: yes
- [3195. Find the Minimum Area to Cover All Ones I](#3195-find-the-minimum-area-to-cover-all-ones-i) — Medium; code: yes
- [3197. Find the Minimum Area to Cover All Ones II](#3197-find-the-minimum-area-to-cover-all-ones-ii) — Hard; code: yes
- [3200. Maximum Height of a Triangle](#3200-maximum-height-of-a-triangle) — Easy; code: yes
- [3285. Find Indices of Stable Mountains](#3285-find-indices-of-stable-mountains) — Easy; code: yes
- [3349. Adjacent Increasing Subarrays Detection I](#3349-adjacent-increasing-subarrays-detection-i) — Easy; code: yes
- [3353. Minimum Total Operations](#3353-minimum-total-operations) — Easy; code: yes
- [3379. Transformed Array](#3379-transformed-array) — Easy; code: yes
- [3386. Button with Longest Push Time](#3386-button-with-longest-push-time) — Easy; code: yes
- [3392. Count Subarrays of Length Three With a Condition](#3392-count-subarrays-of-length-three-with-a-condition) — Easy; code: yes
- [3417. Zigzag Grid Traversal With Skip](#3417-zigzag-grid-traversal-with-skip) — Easy; code: yes
- [3423. Maximum Difference Between Adjacent Elements in a Circular Array](#3423-maximum-difference-between-adjacent-elements-in-a-circular-array) — Easy; code: yes
- [3452. Sum of Good Numbers](#3452-sum-of-good-numbers) — Easy; code: yes
- [3502. Minimum Cost to Reach Every Position](#3502-minimum-cost-to-reach-every-position) — Easy; code: yes
- [3565. Sequential Grid Path Cover](#3565-sequential-grid-path-cover) — Medium; code: yes
- [3616. Number of Student Replacements](#3616-number-of-student-replacements) — Medium; code: yes
- [3637. Trionic Array I](#3637-trionic-array-i) — Easy; code: yes
- [3683. Earliest Time to Finish One Task](#3683-earliest-time-to-finish-one-task) — Easy; code: yes
- [3687. Library Late Fee Calculator](#3687-library-late-fee-calculator) — Easy; code: yes
- [3701. Compute Alternating Sum](#3701-compute-alternating-sum) — Easy; code: yes
- [3708. Longest Fibonacci Subarray](#3708-longest-fibonacci-subarray) — Medium; code: yes
- [3809. Best Reachable Tower](#3809-best-reachable-tower) — Medium; code: yes
- [3818. Minimum Prefix Removal to Make Array Strictly Increasing](#3818-minimum-prefix-removal-to-make-array-strictly-increasing) — Medium; code: yes
- [3819. Rotate Non Negative Elements](#3819-rotate-non-negative-elements) — Medium; code: yes
- [3833. Count Dominant Indices](#3833-count-dominant-indices) — Easy; code: yes
- [3847. Find the Score Difference in a Game](#3847-find-the-score-difference-in-a-game) — Medium; code: yes
- [3861. Minimum Capacity Box](#3861-minimum-capacity-box) — Easy; code: yes
- [3872. Longest Arithmetic Sequence After Changing At Most One Element](#3872-longest-arithmetic-sequence-after-changing-at-most-one-element) — Medium; code: yes
- [3880. Minimum Absolute Difference Between Two Values](#3880-minimum-absolute-difference-between-two-values) — Easy; code: yes
- [3909. Compare Sums of Bitonic Parts](#3909-compare-sums-of-bitonic-parts) — Medium; code: yes
- [3912. Valid Elements in an Array](#3912-valid-elements-in-an-array) — Easy; code: yes
- [3917. Count Indices With Opposite Parity](#3917-count-indices-with-opposite-parity) — Easy; code: yes
- [3925. Concatenate Array With Reverse](#3925-concatenate-array-with-reverse) — Easy; code: yes
- [3937. Minimum Operations to Make Array Modulo Alternating I](#3937-minimum-operations-to-make-array-modulo-alternating-i) — Medium; code: yes
- [3942. Minimum Operations to Sort a Permutation](#3942-minimum-operations-to-sort-a-permutation) — Medium; code: yes
- [3944. Minimum Operations to Make Array Modulo Alternating II](#3944-minimum-operations-to-make-array-modulo-alternating-ii) — Hard; code: yes
- [3979. Maximum Valid Pair Sum](#3979-maximum-valid-pair-sum) — Medium; code: yes
- [4020. Elevator Requests I](#4020-elevator-requests-i) — Easy; code: yes
- [4024. Nearest Available Drone](#4024-nearest-available-drone) — Easy; code: yes
- [4052. Cyclically Shift Rows and Columns](#4052-cyclically-shift-rows-and-columns) — Easy; code: yes
- [4062. Transform Array Using Pair Operations](#4062-transform-array-using-pair-operations) — Medium; code: yes

---

## 54. Spiral Matrix

**Problem:** https://leetcode.com/problems/spiral-matrix/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn) including output; O(1) auxiliary

**Complexity reasoning:** Each matrix cell is visited once by the shrinking spiral boundaries.

### Problem description

Given an m x n matrix , return all elements of the matrix in spiral order . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg] 
 
```
Input:
 matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output:
 [1,2,3,6,9,8,7,4,5]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg] 
 
```
Input:
 matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

Output:
 [1,2,3,4,8,12,11,10,9,5,6,7]
```

 Constraints: 

 m == matrix.length 
 
 n == matrix[i].length 
 
 1 <= m, n <= 10 
 
 -100 <= matrix[i][j] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int top = 0, bottom = matrix.size() - 1;
        int left = 0, right = matrix[0].size() - 1;

        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; ++i) result.push_back(matrix[top][i]);
            ++top;

            for (int i = top; i <= bottom; ++i) result.push_back(matrix[i][right]);
            --right;

            if (top <= bottom) {
                for (int i = right; i >= left; --i) result.push_back(matrix[bottom][i]);
                --bottom;
            }

            if (left <= right) {
                for (int i = bottom; i >= top; --i) result.push_back(matrix[i][left]);
                ++left;
            }
        }

        return result;
    }
};
```


## 57. Insert Interval

**Problem:** https://leetcode.com/problems/insert-interval/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) including output

**Complexity reasoning:** The three while loops advance the same index without revisiting intervals; the result stores at most n+1 intervals.

### Problem description

You are given an array of non-overlapping intervals intervals where intervals[i] = [start i , end i ] represent the start and the end of the i th interval and intervals is sorted in ascending order by start i . You are also given an interval newInterval = [start, end] that represents the start and end of another interval. 
 
 Two intervals are considered overlapping if they share at least one point. 
 
 Insert newInterval into intervals such that intervals is still sorted in ascending order by start i and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary). 
 
 Return intervals after the insertion . 
 
 Note that you don't need to modify intervals in-place. You can make a new array and return it. 

 Example 1: 
 
```
Input:
 intervals = [[1,3],[6,9]], newInterval = [2,5]

Output:
 [[1,5],[6,9]]
```

 Example 2: 
 
```
Input:
 intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]

Output:
 [[1,2],[3,10],[12,16]]

Explanation:
 Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

 Constraints: 

 0 <= intervals.length <= 10 4 
 
 intervals[i].length == 2 
 
 0 <= start i <= end i <= 10 5 
 
 intervals is sorted by start i in ascending order. 
 
 newInterval.length == 2 
 
 0 <= start <= end <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int i = 0, n = intervals.size();

        // Step 1: Add all intervals that end before the new interval starts
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }

        // Step 2: Merge overlapping intervals with the new interval
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]); // Update start
            newInterval[1] = max(newInterval[1], intervals[i][1]); // Update end
            i++;
        }
        result.push_back(newInterval); // Add the merged interval

        // Step 3: Add all remaining intervals
        while (i < n) {
            result.push_back(intervals[i]);
            i++;
        }

        return result;
    }
};
```


## 59. Spiral Matrix II

**Problem:** https://leetcode.com/problems/spiral-matrix-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(n²) including output; O(1) auxiliary

**Complexity reasoning:** The n-by-n result is initialized and its cells filled in spiral order.

### Problem description

Given a positive integer n , generate an n x n matrix filled with elements from 1 to n 2 in spiral order. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg] 
 
```
Input:
 n = 3

Output:
 [[1,2,3],[8,9,4],[7,6,5]]
```

 Example 2: 
 
```
Input:
 n = 1

Output:
 [[1]]
```

 Constraints: 

 1 <= n <= 20

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int> > generateMatrix(int n) {
        vector<vector<int> > vv(n, vector<int>(n));
    
        int rowStart = 0, rowEnd = n - 1;
        int colStart = 0, colEnd = n - 1;
        int cnt = 1;
    
        while(rowStart <= rowEnd && colStart <= colEnd)
        {
            for(int i = colStart; i<= colEnd; i++)
                vv[rowStart][i] = cnt++;
            rowStart++;
        
            for(int i = rowStart; i<= rowEnd; i++)
                vv[i][colEnd] = cnt++;
            colEnd--;
        
            for(int i = colEnd; i>= colStart; i--)
                vv[rowEnd][i] = cnt++;
            rowEnd--;
        
            for(int i = rowEnd; i>= rowStart; i--)
                vv[i][colStart] = cnt++;
            colStart++;
        }
    
        return vv;
    }
};
```


## 157. Read N Characters Given Read4

**Problem:** https://leetcode.com/problems/read-n-characters-given-read4/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Simulation, Interactive

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Each read4 call handles at most four characters, and at most n characters are copied; the temporary buffer has four slots.

### Problem description

Given a file and assume that you can only read the file using a given method read4 , implement a method to read n characters. 
 
 Method read4: 
 
 The API read4 reads four consecutive characters from file , then writes those characters into the buffer array buf4 . 
 
 The return value is the number of actual characters read. 
 
 Note that read4() has its own file pointer, much like FILE *fp in C. 
 
 Definition of read4: 
 
```
Parameter: char[] buf4
 Returns: int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].
```

 Below is a high-level example of how read4 works: 
 [Figure: https://assets.leetcode.com/uploads/2020/07/01/157_example.png] 
 
```
File file("abcde
"); // File is "
abcde
", initially file pointer (fp) points to 'a'
char[] buf4 = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file
```

 Method read: 
 
 By using the read4 method, implement the method read that reads n characters from file and store it in the buffer array buf . Consider that you cannot manipulate file directly. 
 
 The return value is the number of actual characters read. 
 
 Definition of read: 
 
```
Parameters: char[] buf, int n
 Returns: int

buf[] is a destination, not a source. You will need to write the results to buf[].
```

 Note: 

 Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read . 
 
 The read function will only be called once for each test case. 
 
 You may assume the destination buffer array, buf , is guaranteed to have enough space for storing n characters. 

 Example 1: 
 
```
Input:
 file = "abc", n = 4

Output:
 3

Explanation:
 After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
Note that "abc" is the file's content, not buf. buf is the destination buffer that you will have to write the results to.
```

 Example 2: 
 
```
Input:
 file = "abcde", n = 5

Output:
 5

Explanation:
 After calling your read method, buf should contain "abcde". We read a total of 5 characters from the file, so return 5.
```

 Example 3: 
 
```
Input:
 file = "abcdABCD1234", n = 12

Output:
 12

Explanation:
 After calling your read method, buf should contain "abcdABCD1234". We read a total of 12 characters from the file, so return 12.
```

 Constraints: 

 1 <= file.length <= 500 
 
 file consist of English letters and digits. 
 
 1 <= n <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
// The judge provides: int read4(char *buf4);
class Solution
{
public:
    int read(char*buf, int n)
    {
        int got = 0;
        char tmp[4];
        while (got < n)
        {
            int cnt = read4(tmp);
            if (!cnt)
            {
                break;
            }
            for (int i = 0; i < cnt && got < n;++i)
            {
                buf[got++] = tmp[i];
            }
        }
        return got;
    }
};
```


## 158. Read N Characters Given read4 II - Call Multiple Times

**Problem:** https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Simulation, Interactive

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n) per call

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Each character is copied once; the persistent read4 buffer holds four characters across calls.

### Problem description

Given a file and assume that you can only read the file using a given method read4 , implement a method read to read n characters. Your method read may be called multiple times . 
 
 Method read4: 
 
 The API read4 reads four consecutive characters from file , then writes those characters into the buffer array buf4 . 
 
 The return value is the number of actual characters read. 
 
 Note that read4() has its own file pointer, much like FILE *fp in C. 
 
 Definition of read4: 
 
```
Parameter: char[] buf4
 Returns: int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].
```

 Below is a high-level example of how read4 works: 
 [Figure: https://assets.leetcode.com/uploads/2020/07/01/157_example.png] 
 
```
File file("abcde
"); // File is "
abcde
", initially file pointer (fp) points to 'a'
char[] buf4 = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file
```

 Method read: 
 
 By using the read4 method, implement the method read that reads n characters from file and store it in the buffer array buf . Consider that you cannot manipulate file directly. 
 
 The return value is the number of actual characters read. 
 
 Definition of read: 
 
```
Parameters: char[] buf, int n
 Returns: int

buf[] is a destination, not a source. You will need to write the results to buf[].
```

 Note: 

 Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read . 
 
 The read function may be called multiple times . 
 
 Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details. 
 
 You may assume the destination buffer array, buf , is guaranteed to have enough space for storing n characters. 
 
 It is guaranteed that in a given test case the same buffer buf is called by read . 

 Example 1: 
 
```
Input:
 file = "abc", queries = [1,2,1]

Output:
 [1,2,0]

Explanation:
 The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
```

 Example 2: 
 
```
Input:
 file = "abc", queries = [4,1]

Output:
 [3,0]

Explanation:
 The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
```

 Constraints: 

 1 <= file.length <= 500 
 
 file consist of English letters and digits. 
 
 1 <= queries.length <= 10 
 
 1 <= queries[i] <= 500

### C++ solution

**Source:** accepted_cpp_submission

```cpp
// The judge provides: int read4(char *buf4);
class Solution
{
    char tmp[4];
    int pos = 0, len = 0;
public:
    int read(char*buf, int n)
    {
        int used = 0;
        while (used < n)
        {
            if (pos == len)
            {
                len = read4(tmp);
                pos = 0;
                if (!len)
                {
                    break;
                }
            }
            buf[used++] = tmp[pos++];
        }
        return used;
    }
};
```


## 163. Missing Ranges

**Problem:** https://leetcode.com/problems/missing-ranges/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) including output; O(1) auxiliary

**Complexity reasoning:** One pass checks n+1 gaps and emits at most n+1 missing ranges.

### Problem description

You are given an inclusive range [lower, upper] and a sorted unique integer array nums , where all elements are within the inclusive range. 
 
 A number x is considered missing if x is in the range [lower, upper] and x is not in nums . 
 
 Return the shortest sorted list of ranges that exactly covers all the missing numbers . That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges. 

 Example 1: 
 
```
Input:
 nums = [0,1,3,50,75], lower = 0, upper = 99

Output:
 [[2,2],[4,49],[51,74],[76,99]]

Explanation:
 The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
```

 Example 2: 
 
```
Input:
 nums = [-1], lower = -1, upper = -1

Output:
 []

Explanation:
 There are no missing ranges since there are no missing numbers.
```

 Constraints: 

 -10 9 <= lower <= upper <= 10 9 
 
 0 <= nums.length <= 100 
 
 lower <= nums[i] <= upper 
 
 All the values of nums are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
public:
    vector< vector< int >>findMissingRanges(vector< int>& nums, int lower, int upper)
    {
        vector< vector< int >>ans;
        long long prev = (long long) lower - 1;
        for (int i = 0; i <= (int) nums.size();++i)
        {
            long long cur = i == (int) nums.size() ? (long long) upper + 1 : nums[i];
            if (cur - prev >1) ans.push_back( { (int) (prev + 1), (int) (cur - 1) });
            prev = cur;
        }
        return ans;
    }
};
```


## 228. Summary Ranges

**Problem:** https://leetcode.com/problems/summary-ranges/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) including output; O(1) auxiliary

**Complexity reasoning:** The inner loop advances the outer index, so each number is processed once; emitted range strings use linear total storage under fixed-width integers.

### Problem description

You are given a sorted unique integer array nums . 
 
 A range [a,b] is the set of all integers from a to b (inclusive). 
 
 Return the smallest sorted list of ranges that cover all the numbers in the array exactly . That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums . 
 
 Each range [a,b] in the list should be output as: 

 "a->b" if a != b 
 
 "a" if a == b 

 Example 1: 
 
```
Input:
 nums = [0,1,2,4,5,7]

Output:
 ["0->2","4->5","7"]

Explanation:
 The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

 Example 2: 
 
```
Input:
 nums = [0,2,3,4,6,8,9]

Output:
 ["0","2->4","6","8->9"]

Explanation:
 The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

 Constraints: 

 0 <= nums.length <= 20 
 
 -2 31 <= nums[i] <= 2 31 - 1 
 
 All the values of nums are unique . 
 
 nums is sorted in ascending order.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> result;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int start = nums[i];
            while (i + 1 < n && nums[i] + 1 == nums[i + 1]) {
                i++;
            }
            if (start != nums[i]) {
                result.push_back(to_string(start) + "->" + to_string(nums[i]));
            } else {
                result.push_back(to_string(start));
            }
        }
        return result;
    }
};
```


## 289. Game of Life

**Problem:** https://leetcode.com/problems/game-of-life/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(m²n²)

**Space complexity:** O(mn) auxiliary per neighbor call

**Complexity reasoning:** Important: cntNeighbours takes board by value, copying the entire m-by-n matrix for every cell; this dominates the two grid passes.

### Problem description

According to Wikipedia's article : "The Game of Life , also known simply as Life , is a cellular automaton devised by the British mathematician John Horton Conway in 1970." 
 
 The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1 ) or dead (represented by a 0 ). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article): 

 Any live cell with fewer than two live neighbors dies as if caused by under-population. 
 
 Any live cell with two or three live neighbors lives on to the next generation. 
 
 Any live cell with more than three live neighbors dies, as if by over-population. 
 
 Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. 

 The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board . In this process, births and deaths occur simultaneously . 
 
 Given the current state of the board , update the board to reflect its next state. 
 
 Note that you do not need to return anything. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg] 
 
```
Input:
 board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

Output:
 [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg] 
 
```
Input:
 board = [[1,1],[1,0]]

Output:
 [[1,1],[1,1]]
```

 Constraints: 

 m == board.length 
 
 n == board[i].length 
 
 1 <= m, n <= 25 
 
 board[i][j] is 0 or 1 . 

 Follow up: 

 Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells. 
 
 In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int cntNeighbours(int i, int j, int m, int n, vector<vector<int>> board)
    {
        int cnt = 0;
        vector<int> dx = {-1,-1,-1,0,0,1,1,1};
        vector<int> dy = {-1,0,1,-1,1,-1,0,1};
        for(int k = 0; k < 8;k++)
        {
            int r, c;
            r = i + dx[k]; c = j + dy[k];
            if(r >= 0 && r < m && c >=0 && c < n)
            {
                if(board[r][c]==1||board[r][c] == 2)
                    cnt++;
            }
        }
        return cnt;
    }

    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        //add temp values
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                int cnt = cntNeighbours(i,j,m,n,board);
                if((board[i][j]== 1 ) && cnt < 2)
                    board[i][j] = 2;
                else if(board[i][j] == 0 && cnt == 3) //dead cell with 3 live neighbours
                {
                    board[i][j] = 3;
                }
                else if((board[i][j] == 1) &&cnt > 3)
                    board[i][j] = 2;
            }
        }
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(board[i][j] == 2)
                    board[i][j] = 0;
                if(board[i][j] == 3)
                    board[i][j] = 1;
            }
        }
        
    }
};
```


## 422. Valid Word Square

**Problem:** https://leetcode.com/problems/valid-word-square/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(L)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** The nested loops examine each existing character at most once; L is the total number of characters across words.

### Problem description

Given an array of strings words , return true if it forms a valid word square . 
 
 A sequence of strings forms a valid word square if the k th row and column read the same string, where 0 <= k < max(numRows, numColumns) . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/04/09/validsq1-grid.jpg] 
 
```
Input:
 words = ["abcd","bnrt","crmy","dtye"]

Output:
 true

Explanation:

The 1
st
 row and 1
st
 column both read "abcd".
The 2
nd
 row and 2
nd
 column both read "bnrt".
The 3
rd
 row and 3
rd
 column both read "crmy".
The 4
th
 row and 4
th
 column both read "dtye".
Therefore, it is a valid word square.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/04/09/validsq2-grid.jpg] 
 
```
Input:
 words = ["abcd","bnrt","crm","dt"]

Output:
 true

Explanation:

The 1
st
 row and 1
st
 column both read "abcd".
The 2
nd
 row and 2
nd
 column both read "bnrt".
The 3
rd
 row and 3
rd
 column both read "crm".
The 4
th
 row and 4
th
 column both read "dt".
Therefore, it is a valid word square.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/04/09/validsq3-grid.jpg] 
 
```
Input:
 words = ["ball","area","read","lady"]

Output:
 false

Explanation:

The 3
rd
 row reads "read" while the 3
rd
 column reads "lead".
Therefore, it is NOT a valid word square.
```

 Constraints: 

 1 <= words.length <= 500 
 
 1 <= words[i].length <= 500 
 
 words[i] consists of only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
public:
    bool validWordSquare(vector<string>& words)
    {
        for (int r = 0; r < (int)words.size(); ++r)
        {
            for (int c = 0; c < (int)words[r].size(); ++c)
            {
                if (c >= (int)words.size() ||
                    r >= (int)words[c].size() ||
                    words[r][c] != words[c][r])
                    {
                    return false;
                }
            }
        }
        return true;
    }
};
```


## 485. Max Consecutive Ones

**Problem:** https://leetcode.com/problems/max-consecutive-ones/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One pass updates the current and maximum run lengths.

### Problem description

Given a binary array nums , return the maximum number of consecutive 1 's in the array . 

 Example 1: 
 
```
Input:
 nums = [1,1,0,1,1,1]

Output:
 3

Explanation:
 The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

 Example 2: 
 
```
Input:
 nums = [1,0,1,1,0,1]

Output:
 2
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
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCount = 0, count = 0;
        for (int num : nums) {
            count = (num == 1) ? count + 1 : 0;
            maxCount = max(maxCount, count);
        }
        return maxCount;
    }
};
```


## 495. Teemo Attacking

**Problem:** https://leetcode.com/problems/teemo-attacking/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Each attack contributes its duration or the gap from the preceding attack.

### Problem description

Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1] . If Teemo attacks again before the poison effect ends, the timer for it is reset , and the poison effect will end duration seconds after the new attack. 
 
 You are given a non-decreasing integer array timeSeries , where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i] , and an integer duration . 
 
 Return the total number of seconds that Ashe is poisoned . 

 Example 1: 
 
```
Input:
 timeSeries = [1,4], duration = 2

Output:
 4

Explanation:
 Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
```

 Example 2: 
 
```
Input:
 timeSeries = [1,2], duration = 2

Output:
 3

Explanation:
 Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
```

 Constraints: 

 1 <= timeSeries.length <= 10 4 
 
 0 <= timeSeries[i], duration <= 10 7 
 
 timeSeries is sorted in non-decreasing order.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int total = 0;
        for (int i = 0; i < timeSeries.size(); ++i) {
            if (i == 0) total += duration;
            else total += min(duration, timeSeries[i] - timeSeries[i - 1]);
        }
        return total;
    }
};
```


## 498. Diagonal Traverse

**Problem:** https://leetcode.com/problems/diagonal-traverse/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Ordered map, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn log(m+n))

**Space complexity:** O(mn) including output and map

**Complexity reasoning:** Every cell is inserted into an ordered map keyed by diagonal, costing O(log(m+n)); iteration copies each diagonal vector and reverses even diagonals.

### Problem description

Given an m x n matrix mat , return an array of all the elements of the array in a diagonal order . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg] 
 
```
Input:
 mat = [[1,2,3],[4,5,6],[7,8,9]]

Output:
 [1,2,4,7,5,3,6,8,9]
```

 Example 2: 
 
```
Input:
 mat = [[1,2],[3,4]]

Output:
 [1,2,3,4]
```

 Constraints: 

 m == mat.length 
 
 n == mat[i].length 
 
 1 <= m, n <= 10 4 
 
 1 <= m * n <= 10 4 
 
 -10 5 <= mat[i][j] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
public:
        vector<int> findDiagonalOrder(vector<vector<int>>& matrix)
        {
            vector<int>ans;
            map<int,vector<int>>m;
            for(int i=0;i<matrix.size();i++)
            {
                for(int j=0;j<matrix[0].size();j++)
                {
                    m[i+j].push_back(matrix[i][j]);
                }
            }

           for(auto i:m)
           {
            if((i.first)%2 == 0)
                reverse(i.second.begin(), i.second.end());

            for(auto j: i.second)
            ans.push_back(j);
           }

        return ans;
        }

};
```


## 566. Reshape the Matrix

**Problem:** https://leetcode.com/problems/reshape-the-matrix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn) including output

**Complexity reasoning:** When dimensions match, each cell is copied once into the new r-by-c matrix; when they do not, returning mat by value also copies mn cells.

### Problem description

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data. 
 
 You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix. 
 
 The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were. 
 
 If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg] 
 
```
Input:
 mat = [[1,2],[3,4]], r = 1, c = 4

Output:
 [[1,2,3,4]]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg] 
 
```
Input:
 mat = [[1,2],[3,4]], r = 2, c = 4

Output:
 [[1,2],[3,4]]
```

 Constraints: 

 m == mat.length 
 
 n == mat[i].length 
 
 1 <= m, n <= 100 
 
 -1000 <= mat[i][j] <= 1000 
 
 1 <= r, c <= 300

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int m = mat.size(), n = mat[0].size();
        if (m * n != r * c) return mat;
        vector<vector<int>> res(r, vector<int>(c));
        for (int i = 0; i < m * n; ++i)
            res[i / c][i % c] = mat[i / n][i % n];
        return res;
    }
};
```


## 661. Image Smoother

**Problem:** https://leetcode.com/problems/image-smoother/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn) including output

**Complexity reasoning:** For each of mn cells, at most nine neighboring positions are examined.

### Problem description

An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother). 
 [Figure: https://assets.leetcode.com/uploads/2021/05/03/smoother-grid.jpg] 
 
 Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/05/03/smooth-grid.jpg] 
 
```
Input:
 img = [[1,1,1],[1,0,1],[1,1,1]]

Output:
 [[0,0,0],[0,0,0],[0,0,0]]

Explanation:

For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/05/03/smooth2-grid.jpg] 
 
```
Input:
 img = [[100,200,100],[200,50,200],[100,200,100]]

Output:
 [[137,141,137],[141,138,141],[137,141,137]]

Explanation:

For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
```

 Constraints: 

 m == img.length 
 
 n == img[i].length 
 
 1 <= m, n <= 200 
 
 0 <= img[i][j] <= 255

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    std::vector<std::vector<int>> imageSmoother(std::vector<std::vector<int>>& img) {
        int m = img.size(), n = img[0].size();
        std::vector<std::vector<int>> ans(m, std::vector<int>(n));
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                int sum = 0, count = 0;
                for (int dr = -1; dr <= 1; ++dr)
                    for (int dc = -1; dc <= 1; ++dc) {
                        int nr = r + dr, nc = c + dc;
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                            sum += img[nr][nc];
                            ++count;
                        }
                    }
                ans[r][c] = sum / count;
            }
        }
        return ans;
    }
};
```


## 665. Non-decreasing Array

**Problem:** https://leetcode.com/problems/non-decreasing-array/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** A single pass counts adjacent inversions and checks constant-time neighboring values.

### Problem description

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element . 
 
 We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i ( 0-based ) such that ( 0 <= i <= n - 2 ). 

 Example 1: 
 
```
Input:
 nums = [4,2,3]

Output:
 true

Explanation:
 You could modify the first 4 to 1 to get a non-decreasing array.
```

 Example 2: 
 
```
Input:
 nums = [4,2,1]

Output:
 false

Explanation:
 You cannot get a non-decreasing array by modifying at most one element.
```

 Constraints: 

 n == nums.length 
 
 1 <= n <= 10 4 
 
 -10 5 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    bool checkPossibility(vector<int>& nums)
    {
        const int n = nums.size();
        int drop_count = 0;
        for (int i = 0; i < n - 1; i++) 
        {
            if (nums[i] > nums[i + 1]) 
            {
                drop_count++;
                if (drop_count > 1 or (i > 0 and i < n - 2 and nums[i - 1] > nums[i + 1] and nums[i] > nums[i + 2]))
                {
                    return false;
                }
            }
        }
        return true;
    }
};
```


## 674. Longest Continuous Increasing Subsequence

**Problem:** https://leetcode.com/problems/longest-continuous-increasing-subsequence/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** A single scan tracks the current strictly increasing run.

### Problem description

Given an unsorted array of integers nums , return the length of the longest continuous increasing subsequence (i.e. subarray) . The subsequence must be strictly increasing. 
 
 A continuous increasing subsequence is defined by two indices l and r ( l < r ) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r , nums[i] < nums[i + 1] . 

 Example 1: 
 
```
Input:
 nums = [1,3,5,4,7]

Output:
 3

Explanation:
 The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
```

 Example 2: 
 
```
Input:
 nums = [2,2,2,2,2]

Output:
 1

Explanation:
 The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
```

 Constraints: 

 1 <= nums.length <= 10 4 
 
 -10 9 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int maxLen = 1, currentLen = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i - 1]) currentLen++;
            else currentLen = 1;
            maxLen = max(maxLen, currentLen);
        }
        return maxLen;
    }
};
```


## 717. 1-bit and 2-bit Characters

**Problem:** https://leetcode.com/problems/1-bit-and-2-bit-characters/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** The index moves forward by one or two until the final bit.

### Problem description

We have two special characters: 

 The first character can be represented by one bit 0 . 
 
 The second character can be represented by two bits ( 10 or 11 ). 

 Given a binary array bits that ends with 0 , return true if the last character must be a one-bit character. 

 Example 1: 
 
```
Input:
 bits = [1,0,0]

Output:
 true

Explanation:
 The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
```

 Example 2: 
 
```
Input:
 bits = [1,1,1,0]

Output:
 false

Explanation:
 The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
```

 Constraints: 

 1 <= bits.length <= 1000 
 
 bits[i] is either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int i = 0;
        while (i < bits.size() - 1)
            i += bits[i] + 1;
        return i == bits.size() - 1;
    }
};
```


## 755. Pour Water

**Problem:** https://leetcode.com/problems/pour-water/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(volume × n)

**Space complexity:** O(n) for returned vector copy; O(1) auxiliary otherwise

**Complexity reasoning:** For each unit of water, the algorithm may scan left and right across n heights; returning heights by value copies n elements.

### Problem description

You are given an elevation map represents as an integer array heights where heights[i] representing the height of the terrain at index i . The width at each index is 1 . You are also given two integers volume and k . volume units of water will fall at index k . 
 
 Water first drops at the index k and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules: 

 If the droplet would eventually fall by moving left, then move left. 
 
 Otherwise, if the droplet would eventually fall by moving right, then move right. 
 
 Otherwise, rise to its current position. 

 Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, level means the height of the terrain plus any water in that column. 
 
 We can assume there is infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than one grid block, and each unit of water has to be in exactly one block. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/06/12/pour11-grid.jpg] 
 
```
Input:
 heights = [2,1,1,2,1,2,2], volume = 4, k = 3

Output:
 [2,2,2,3,2,2,2]

Explanation:

The first drop of water lands at index k = 3. When moving left or right, the water can only move to the same level or a lower level. (By level, we mean the total height of the terrain plus any water in that column.)
Since moving left will eventually make it fall, it moves left. (A droplet "made to fall" means go to a lower height than it was at previously.) Since moving left will not make it fall, it stays in place.

The next droplet falls at index k = 3. Since the new droplet moving left will eventually make it fall, it moves left. Notice that the droplet still preferred to move left, even though it could move right (and moving right makes it fall quicker.)

The third droplet falls at index k = 3. Since moving left would not eventually make it fall, it tries to move right. Since moving right would eventually make it fall, it moves right.

Finally, the fourth droplet falls at index k = 3. Since moving left would not eventually make it fall, it tries to move right. Since moving right would not eventually make it fall, it stays in place.
```

 Example 2: 
 
```
Input:
 heights = [1,2,3,4], volume = 2, k = 2

Output:
 [2,3,3,4]

Explanation:
 The last droplet settles at index 1, since moving further left would not cause it to eventually fall to a lower height.
```

 Example 3: 
 
```
Input:
 heights = [3,1,3], volume = 5, k = 1

Output:
 [4,4,4]
```

 Constraints: 

 1 <= heights.length <= 100 
 
 0 <= heights[i] <= 99 
 
 0 <= volume <= 2000 
 
 0 <= k < heights.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> pourWater(vector<int>& heights, int volume, int k) {
        int n = heights.size();
        while (volume-- > 0) {
            int best = k;
            for (int i = k - 1; i >= 0 && heights[i] <= heights[i + 1]; --i) {
                if (heights[i] < heights[best]) {
                    best = i;
                }
            }
            if (best == k) {
                for (int i = k + 1; i < n && heights[i] <= heights[i - 1]; ++i) {
                    if (heights[i] < heights[best]) {
                        best = i;
                    }
                }
            }
            ++heights[best];
        }
        return heights;
    }
};
```


## 766. Toeplitz Matrix

**Problem:** https://leetcode.com/problems/toeplitz-matrix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(1)

**Complexity reasoning:** The nested loops compare each non-first-row/non-first-column cell to its upper-left neighbor.

### Problem description

Given an m x n matrix , return  true  if the matrix is Toeplitz. Otherwise, return false . 
 
 A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/04/ex1.jpg] 
 
```
Input:
 matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

Output:
 true

Explanation:

In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/04/ex2.jpg] 
 
```
Input:
 matrix = [[1,2],[2,2]]

Output:
 false

Explanation:

The diagonal "[1, 2]" has different elements.
```

 Constraints: 

 m == matrix.length 
 
 n == matrix[i].length 
 
 1 <= m, n <= 20 
 
 0 <= matrix[i][j] <= 99 

 Follow up: 

 What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once? 
 
 What if the matrix is so large that you can only load up a partial row into the memory at once?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        for (int i = 1; i < matrix.size(); i++) {
            for (int j = 1; j < matrix[0].size(); j++) {
                if (matrix[i][j] != matrix[i - 1][j - 1])
                    return false;
            }
        }
        return true;
    }
};
```


## 794. Valid Tic-Tac-Toe State

**Problem:** https://leetcode.com/problems/valid-tic-tac-toe-state/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** The board is fixed at 3 by 3, and both winner checks examine a constant number of lines.

### Problem description

Given a Tic-Tac-Toe board as a string array board , return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game. 
 
 The board is a 3 x 3 array that consists of characters ' ' , 'X' , and 'O' . The ' ' character represents an empty square. 
 
 Here are the rules of Tic-Tac-Toe: 

 Players take turns placing characters into empty squares ' ' . 
 
 The first player always places 'X' characters, while the second player always places 'O' characters. 
 
 'X' and 'O' characters are always placed into empty squares, never filled ones. 
 
 The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal. 
 
 The game also ends if all squares are non-empty. 
 
 No more moves can be played if the game is over. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/05/15/tictactoe1-grid.jpg] 
 
```
Input:
 board = ["O "," "," "]

Output:
 false

Explanation:
 The first player always plays "X".
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/05/15/tictactoe2-grid.jpg] 
 
```
Input:
 board = ["XOX"," X "," "]

Output:
 false

Explanation:
 Players take turns making moves.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/05/15/tictactoe4-grid.jpg] 
 
```
Input:
 board = ["XOX","O O","XOX"]

Output:
 true
```

 Constraints: 

 board.length == 3 
 
 board[i].length == 3 
 
 board[i][j] is either 'X' , 'O' , or ' ' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool validTicTacToe(vector<string>& board) {
        int xCount = 0, oCount = 0;
        for (auto& row : board)
            for (char c : row) {
                if (c == 'X') xCount++;
                else if (c == 'O') oCount++;
            }

        if (oCount > xCount || xCount - oCount > 1)
            return false;
        bool xWin = win(board, 'X'), oWin = win(board, 'O');
        if (xWin && xCount != oCount + 1) return false;
        if (oWin && xCount != oCount) return false;
        if (xWin && oWin) return false;
        return true;
    }

    bool win(vector<string>& board, char p) {
        for (int i = 0; i < 3; ++i)
            if ((board[i][0] == p && board[i][1] == p && board[i][2] == p) ||
                (board[0][i] == p && board[1][i] == p && board[2][i] == p))
                return true;
        return (board[0][0] == p && board[1][1] == p && board[2][2] == p) ||
               (board[0][2] == p && board[1][1] == p && board[2][0] == p);
    }
};
```


## 835. Image Overlap

**Problem:** https://leetcode.com/problems/image-overlap/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Ordered map, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n⁴ log n)

**Space complexity:** O(n²)

**Complexity reasoning:** Up to O(n²) set pixels per image yield O(n⁴) pairs; ordered-map increments cost O(log n), while displacement keys have only O(n²) possible values.

### Problem description

You are given two images, img1 and img2 , represented as binary, square matrices of size n x n . A binary matrix has only 0 s and 1 s as values. 
 
 We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images. 
 
 Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased. 
 
 Return the largest possible overlap . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg] 
 
```
Input:
 img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]

Output:
 3

Explanation:
 We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).
```

 Example 2: 
 
```
Input:
 img1 = [[1]], img2 = [[1]]

Output:
 1
```

 Example 3: 
 
```
Input:
 img1 = [[0]], img2 = [[0]]

Output:
 0
```

 Constraints: 

 n == img1.length == img1[i].length 
 
 n == img2.length == img2[i].length 
 
 1 <= n <= 30 
 
 img1[i][j] is either 0 or 1 . 
 
 img2[i][j] is either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int n = img1.size();
        vector<pair<int,int>> a, b;
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) {
            if (img1[i][j]) a.push_back({i, j});
            if (img2[i][j]) b.push_back({i, j});
        }
        map<pair<int,int>, int> count;
        int best = 0;
        for (const auto& x : a) for (const auto& y : b)
            best = max(best, ++count[{x.first - y.first, x.second - y.second}]);
        return best;
    }
};
```


## 849. Maximize Distance to Closest Person

**Problem:** https://leetcode.com/problems/maximize-distance-to-closest-person/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One pass considers distances between occupied seats and both ends.

### Problem description

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the i th seat, and seats[i] = 0 represents that the i th seat is empty (0-indexed) . 
 
 There is at least one empty seat, and at least one person sitting. 
 
 Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.  
 
 Return that maximum distance to the closest person . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/10/distance.jpg] 
 
```
Input:
 seats = [1,0,0,0,1,0,1]

Output:
 2

Explanation: 

If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
```

 Example 2: 
 
```
Input:
 seats = [1,0,0,0]

Output:
 3

Explanation: 

If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
```

 Example 3: 
 
```
Input:
 seats = [0,1]

Output:
 1
```

 Constraints: 

 2 <= seats.length <= 2 * 10 4 
 
 seats[i]  is 0 or  1 . 
 
 At least one seat is empty . 
 
 At least one seat is occupied .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int maxDistToClosest(vector<int>& seats) 
    {
         int res = 0, n = seats.size(), last = -1;
         for (int i = 0; i < n; ++i) 
         {
            if (seats[i] == 1) 
            {
                res = last < 0 ? i : max(res, (i - last) / 2);
                last = i;
            }
        }
        res = max(res, n - last - 1);
        return res;
    }
};
```


## 867. Transpose Matrix

**Problem:** https://leetcode.com/problems/transpose-matrix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn) including output

**Complexity reasoning:** The transposed n-by-m matrix is allocated and each input cell copied once.

### Problem description

Given a 2D integer array matrix , return the transpose of matrix . 
 
 The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices. 
 
 [Figure: https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png] 

 Example 1: 
 
```
Input:
 matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output:
 [[1,4,7],[2,5,8],[3,6,9]]
```

 Example 2: 
 
```
Input:
 matrix = [[1,2,3],[4,5,6]]

Output:
 [[1,4],[2,5],[3,6]]
```

 Constraints: 

 m == matrix.length 
 
 n == matrix[i].length 
 
 1 <= m, n <= 1000 
 
 1 <= m * n <= 10 5 
 
 -10 9 <= matrix[i][j] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        int m = A.size(), n = A[0].size();
        vector<vector<int>> result(n, vector<int>(m));
        
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                result[j][i] = A[i][j];
        
        return result;
    }
};
```


## 885. Spiral Matrix III

**Problem:** https://leetcode.com/problems/spiral-matrix-iii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O((R+C)²)

**Space complexity:** O(RC) including output

**Complexity reasoning:** The expanding spiral traverses positions outside the grid too; reaching all R*C cells takes O((R+C)²) steps in the worst case.

### Problem description

You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column. 
 
 You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid. 
 
 Return an array of coordinates representing the positions of the grid in the order you visited them . 

 Example 1: 
 [Figure: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png] 
 
```
Input:
 rows = 1, cols = 4, rStart = 0, cStart = 0

Output:
 [[0,0],[0,1],[0,2],[0,3]]
```

 Example 2: 
 [Figure: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png] 
 
```
Input:
 rows = 5, cols = 6, rStart = 1, cStart = 4

Output:
 [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
```

 Constraints: 

 1 <= rows, cols <= 100 
 
 0 <= rStart < rows 
 
 0 <= cStart < cols

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int R, int C, int r0, int c0) {
        vector<vector<int>> res;
        int steps = 0, len = 1, dir = 0;
        vector<int> dr = {0, 1, 0, -1}, dc = {1, 0, -1, 0};

        while (res.size() < R * C) {
            if (dir == 0 || dir == 2) ++steps;
            for (int i = 0; i < steps; ++i) {
                if (r0 >= 0 && r0 < R && c0 >= 0 && c0 < C) {
                    res.push_back({r0, c0});
                }
                r0 += dr[dir];
                c0 += dc[dir];
            }
            dir = (dir + 1) % 4;
        }
        return res;
    }
};
```


## 896. Monotonic Array

**Problem:** https://leetcode.com/problems/monotonic-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One pass tracks whether increasing and decreasing order remain possible.

### Problem description

An array is monotonic if it is either monotone increasing or monotone decreasing. 
 
 An array nums is monotone increasing if for all i <= j , nums[i] <= nums[j] . An array nums is monotone decreasing if for all i <= j , nums[i] >= nums[j] . 
 
 Given an integer array nums , return true if the given array is monotonic, or false otherwise . 

 Example 1: 
 
```
Input:
 nums = [1,2,2,3]

Output:
 true
```

 Example 2: 
 
```
Input:
 nums = [6,5,4,4]

Output:
 true
```

 Example 3: 
 
```
Input:
 nums = [1,3,2]

Output:
 false
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 -10 5 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool increasing = true, decreasing = true;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i-1]) decreasing = false;
            if (nums[i] < nums[i-1]) increasing = false;
        }
        return increasing || decreasing;
    }
};
```


## 915. Partition Array into Disjoint Intervals

**Problem:** https://leetcode.com/problems/partition-array-into-disjoint-intervals/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Two length-n arrays store prefix maxima and suffix minima; three linear scans determine the split.

### Problem description

Given an integer array nums , partition it into two (contiguous) subarrays left and right so that: 

 Every element in left is less than or equal to every element in right . 
 
 left and right are non-empty. 
 
 left has the smallest possible size. 

 Return the length of left after such a partitioning . 
 
 Test cases are generated such that partitioning exists. 

 Example 1: 
 
```
Input:
 nums = [5,0,3,8,6]

Output:
 3

Explanation:
 left = [5,0,3], right = [8,6]
```

 Example 2: 
 
```
Input:
 nums = [1,1,1,0,6,12]

Output:
 4

Explanation:
 left = [1,1,1,0], right = [6,12]
```

 Constraints: 

 2 <= nums.length <= 10 5 
 
 0 <= nums[i] <= 10 6 
 
 There is at least one valid answer for the given input.

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int partitionDisjoint(vector<int>& A) {
        int n = A.size();
        vector<int> leftMax(n), rightMin(n);
        leftMax[0] = A[0];
        rightMin[n-1] = A[n-1];
        
        for (int i = 1; i < n; ++i) {
            leftMax[i] = max(leftMax[i-1], A[i]);
        }
        for (int i = n - 2; i >= 0; --i) {
            rightMin[i] = min(rightMin[i+1], A[i]);
        }
        
        for (int i = 0; i < n - 1; ++i) {
            if (leftMax[i] <= rightMin[i+1]) return i + 1;
        }
        
        return n;
    }
};
```


## 941. Valid Mountain Array

**Problem:** https://leetcode.com/problems/valid-mountain-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Two pointers independently scan uphill from the left and downhill from the right.

### Problem description

Given an array of integers arr , return true if and only if it is a valid mountain array . 
 
 Recall that arr is a mountain array if and only if: 

 arr.length >= 3 
 
 There exists some i with 0 < i < arr.length - 1 such that:

 arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
 
 arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 

 [Figure: https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png] 

 Example 1: 
 
```
Input:
 arr = [2,1]

Output:
 false
```
 
 Example 2: 
 
```
Input:
 arr = [3,5,5]

Output:
 false
```
 
 Example 3: 
 
```
Input:
 arr = [0,3,2,1]

Output:
 true
```

 Constraints: 

 1 <= arr.length <= 10 4 
 
 0 <= arr[i] <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int n = arr.size(), i = 0, j = n - 1;
        
        while (i + 1 < n && arr[i] < arr[i + 1]) i++;
        while (j > 0 && arr[j] < arr[j - 1]) j--;
        
        return i > 0 && i == j && j < n - 1;
    }
};
```


## 985. Sum of Even Numbers After Queries

**Problem:** https://leetcode.com/problems/sum-of-even-numbers-after-queries/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n+q)

**Space complexity:** O(q) including output; O(1) auxiliary

**Complexity reasoning:** The initial even sum scans n entries; each of q updates adjusts the sum in constant time.

### Problem description

You are given an integer array nums and an array queries where queries[i] = [val i , index i ] . 
 
 For each query i , first, apply nums[index i ] = nums[index i ] + val i , then print the sum of the even values of nums . 
 
 Return an integer array answer where answer[i] is the answer to the i th query . 

 Example 1: 
 
```
Input:
 nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]

Output:
 [8,6,2,4]

Explanation:
 At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
```

 Example 2: 
 
```
Input:
 nums = [1], queries = [[4,0]]

Output:
 [0]
```

 Constraints: 

 1 <= nums.length <= 10 4 
 
 -10 4 <= nums[i] <= 10 4 
 
 1 <= queries.length <= 10 4 
 
 -10 4 <= val i <= 10 4 
 
 0 <= index i < nums.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
        int sum = 0;
        for (int a : A)
            if (a % 2 == 0) sum += a;

        vector<int> res;
        for (auto& q : queries) {
            int val = q[0], i = q[1];
            if (A[i] % 2 == 0) sum -= A[i];
            A[i] += val;
            if (A[i] % 2 == 0) sum += A[i];
            res.push_back(sum);
        }
        return res;
    }
};
```


## 999. Available Captures for Rook

**Problem:** https://leetcode.com/problems/available-captures-for-rook/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** The chessboard is fixed at 8 by 8; the rook search and four directional scans have bounded length.

### Problem description

You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R' , some number of white bishops 'B' , and some number of black pawns 'p' . Empty squares are represented by '.' . 
 
 A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move. 
 
 Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path. 
 
 Return the number of pawns the white rook is attacking . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2019/02/20/1253_example_1_improved.PNG] 

 Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]] 
 
 Output: 3 
 
 Explanation: 
 
 In this example, the rook is attacking all the pawns. 

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2019/02/19/1253_example_2_improved.PNG] 

 Input: board = [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]] 
 
 Output: 0 
 
 Explanation: 
 
 The bishops are blocking the rook from attacking any of the pawns. 

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2019/02/20/1253_example_3_improved.PNG] 

 Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]] 
 
 Output: 3 
 
 Explanation: 
 
 The rook is attacking the pawns at positions b5, d6, and f5. 

 Constraints: 

 board.length == 8 
 
 board[i].length == 8 
 
 board[i][j] is either 'R' , '.' , 'B' , or 'p' 
 
 There is exactly one cell with board[i][j] == 'R'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        int x, y;
        for (int i = 0; i < 8; ++i)
            for (int j = 0; j < 8; ++j)
                if (board[i][j] == 'R') {
                    x = i; y = j;
                }
        int res = 0, dirs[5] = {0, 1, 0, -1, 0};
        for (int d = 0; d < 4; ++d) {
            int nx = x, ny = y;
            while (true) {
                nx += dirs[d]; ny += dirs[d + 1];
                if (nx < 0 || ny < 0 || nx >= 8 || ny >= 8 || board[nx][ny] == 'B') break;
                if (board[nx][ny] == 'p') {
                    res++;
                    break;
                }
            }
        }
        return res;
    }
};
```


## 1184. Distance Between Bus Stops

**Problem:** https://leetcode.com/problems/distance-between-bus-stops/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Two accumulate calls scan the full circular route and the selected segment.

### Problem description

A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number  i and (i + 1) % n . 
 
 The bus goes along both directions i.e. clockwise and counterclockwise. 
 
 Return the shortest distance between the given  start  and destination  stops. 

 Example 1: 
 
 [Figure: https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1.jpg] 
 
```
Input:
 distance = [1,2,3,4], start = 0, destination = 1

Output:
 1

Explanation:
 Distance between 0 and 1 is 1 or 9, minimum is 1.
```

 Example 2: 
 
 [Figure: https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1-1.jpg] 
 
```
Input:
 distance = [1,2,3,4], start = 0, destination = 2

Output:
 3

Explanation:
 Distance between 0 and 2 is 3 or 7, minimum is 3.
```

 Example 3: 
 
 [Figure: https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1-2.jpg] 
 
```
Input:
 distance = [1,2,3,4], start = 0, destination = 3

Output:
 4

Explanation:
 Distance between 0 and 3 is 6 or 4, minimum is 4.
```

 Constraints: 

 1 <= n <= 10^4 
 
 distance.length == n 
 
 0 <= start, destination < n 
 
 0 <= distance[i] <= 10^4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int distanceBetweenBusStops(vector<int>& dist, int start, int dest) {
        if (start > dest) swap(start, dest);
        int total = accumulate(dist.begin(), dist.end(), 0);
        int path = accumulate(dist.begin() + start, dist.begin() + dest, 0);
        return min(path, total - path);
    }
};
```


## 1222. Queens That Can Attack the King

**Problem:** https://leetcode.com/problems/queens-that-can-attack-the-king/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Hash set, Ordered set, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(q + 8B)

**Space complexity:** O(q + 8)

**Complexity reasoning:** Hashes q queen coordinates, then scans eight directions for at most B=8 board cells each; the hash set stores q positions (expected O(1) lookup).

### Problem description

On a 0-indexed 8 x 8 chessboard, there can be multiple black queens and one white king. 
 
 You are given a 2D integer array queens where queens[i] = [xQueen i , yQueen i ] represents the position of the i th black queen on the chessboard. You are also given an integer array king of length 2 where king = [xKing, yKing] represents the position of the white king. 
 
 Return the coordinates of the black queens that can directly attack the king . You may return the answer in any order . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/12/21/chess1.jpg] 
 
```
Input:
 queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]

Output:
 [[0,1],[1,0],[3,3]]

Explanation:
 The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/12/21/chess2.jpg] 
 
```
Input:
 queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]

Output:
 [[2,2],[3,4],[4,4]]

Explanation:
 The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).
```

 Constraints: 

 1 <= queens.length < 64 
 
 queens[i].length == king.length == 2 
 
 0 <= xQueen i , yQueen i , xKing, yKing < 8 
 
 All the given positions are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        unordered_set<string> board;
        for (auto& q : queens)
            board.insert(to_string(q[0]) + "," + to_string(q[1]));

        vector<vector<int>> res;
        vector<pair<int, int>> dirs = {{-1,0},{1,0},{0,-1},{0,1},{-1,-1},{-1,1},{1,-1},{1,1}};
        for (auto& d : dirs) {
            int x = king[0], y = king[1];
            while (true) {
                x += d.first;
                y += d.second;
                if (x < 0 || y < 0 || x >= 8 || y >= 8) break;
                if (board.count(to_string(x) + "," + to_string(y))) {
                    res.push_back({x, y});
                    break;
                }
            }
        }
        return res;
    }
};
```


## 1243. Array Transformation

**Problem:** https://leetcode.com/problems/array-transformation/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(nR)

**Space complexity:** O(n)

**Complexity reasoning:** Each round copies the n-element array and scans its interior; R is the number of rounds until no value changes, with one O(n) temporary copy per round.

### Problem description

Given an initial array arr , every day you produce a new array using the array of the previous day. 
 
 On the i -th day, you do the following operations on the array of day  i-1  to produce the array of day i : 

 If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented. 
 
 If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented. 
 
 The first and last elements never change. 

 After some days, the array does not change. Return that final array. 

 Example 1: 
 
```
Input:
 arr = [6,2,3,4]

Output:
 [6,3,3,4]

Explanation: 

On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
No more operations can be done to this array.
```

 Example 2: 
 
```
Input:
 arr = [1,6,3,4,3,5]

Output:
 [1,4,4,4,4,5]

Explanation: 

On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
No more operations can be done to this array.
```

 Constraints: 

 3 <= arr.length <= 100 
 
 1 <= arr[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> transformArray(vector<int>& arr) {
        int n = arr.size();
        while (true) {
            vector<int> next = arr;
            bool changed = false;
            for (int i = 1; i + 1 < n; ++i) {
                if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) {
                    ++next[i];
                    changed = true;
                } else if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
                    --next[i];
                    changed = true;
                }
            }
            if (!changed) {
                return arr;
            }
            arr.swap(next);
        }
    }
};
```


## 1260. Shift 2D Grid

**Problem:** https://leetcode.com/problems/shift-2d-grid/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn)

**Complexity reasoning:** Flattens all mn cells, rotates the flat vector in linear time, then rebuilds an m-by-n result; both containers use mn space.

### Problem description

Given a 2D grid of size m x n  and an integer k . You need to shift the grid   k times. 
 
 In one shift operation: 

 Element at grid[i][j] moves to grid[i][j + 1] . 
 
 Element at grid[i][n - 1] moves to grid[i + 1][0] . 
 
 Element at grid[m - 1][n - 1] moves to grid[0][0] . 

 Return the 2D grid after applying shift operation k times. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2019/11/05/e1.png] 
 
```
Input:
 
grid
 = [[1,2,3],[4,5,6],[7,8,9]], k = 1

Output:
 [[9,1,2],[3,4,5],[6,7,8]]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2019/11/05/e2.png] 
 
```
Input:
 
grid
 = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4

Output:
 [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
```

 Example 3: 
 
```
Input:
 
grid
 = [[1,2,3],[4,5,6],[7,8,9]], k = 9

Output:
 [[1,2,3],[4,5,6],[7,8,9]]
```

 Constraints: 

 m == grid.length 
 
 n == grid[i].length 
 
 1 <= m <= 50 
 
 1 <= n <= 50 
 
 -1000 <= grid[i][j] <= 1000 
 
 0 <= k <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        vector<int> flat;
        for (auto& row : grid)
            for (int val : row)
                flat.push_back(val);
        k = k % (m * n);
        rotate(flat.rbegin(), flat.rbegin() + k, flat.rend());
        vector<vector<int>> res(m, vector<int>(n));
        for (int i = 0; i < m * n; ++i)
            res[i / n][i % n] = flat[i];
        return res;
    }
};
```


## 1272. Remove Interval

**Problem:** https://leetcode.com/problems/remove-interval/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Examines each of n intervals once and emits at most two pieces per interval into the result.

### Problem description

A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b) . A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b ). 
 
 You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [a i , b i ] represents the interval [a i , b i ) . You are also given another interval toBeRemoved . 
 
 Return the set of real numbers with the interval toBeRemoved removed from intervals . In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved . Your answer should be a sorted list of disjoint intervals as described above. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/12/24/removeintervalex1.png] 
 
```
Input:
 intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]

Output:
 [[0,1],[6,7]]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/12/24/removeintervalex2.png] 
 
```
Input:
 intervals = [[0,5]], toBeRemoved = [2,3]

Output:
 [[0,2],[3,5]]
```

 Example 3: 
 
```
Input:
 intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]

Output:
 [[-5,-4],[-3,-2],[4,5],[8,9]]
```

 Constraints: 

 1 <= intervals.length <= 10 4 
 
 -10 9 <= a i < b i <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> removeInterval(vector<vector<int>>& intervals,
                                       vector<int>& toBeRemoved) {
        vector<vector<int>> answer;
        int low = toBeRemoved[0];
        int high = toBeRemoved[1];
        for (const auto& interval : intervals) {
            if (interval[0] < low) {
                int end = min(interval[1], low);
                if (interval[0] < end) {
                    answer.push_back({interval[0], end});
                }
            }
            if (interval[1] > high) {
                int start = max(interval[0], high);
                if (start < interval[1]) {
                    answer.push_back({start, interval[1]});
                }
            }
        }
        return answer;
    }
};
```


## 1287. Element Appearing More Than 25% In Sorted Array

**Problem:** https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(log n)

**Space complexity:** O(1)

**Complexity reasoning:** Tests only three candidate values and uses lower_bound and upper_bound on the sorted array for each.

### Problem description

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer. 

 Example 1: 
 
```
Input:
 arr = [1,2,2,6,6,6,6,7,10]

Output:
 6
```

 Example 2: 
 
```
Input:
 arr = [1,1]

Output:
 1
```

 Constraints: 

 1 <= arr.length <= 10 4 
 
 0 <= arr[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int n = arr.size();
        for (int i : {n / 4, n / 2, 3 * n / 4}) {
            int x = arr[i];
            auto lo = lower_bound(arr.begin(), arr.end(), x);
            auto hi = upper_bound(arr.begin(), arr.end(), x);
            if (hi - lo > n / 4) return x;
        }
        return arr[0];
    }
};
```


## 1299. Replace Elements with Greatest Element on Right Side

**Problem:** https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Traverses the input backward once, maintaining the greatest value seen; modifies the input in place.

### Problem description

Given an array arr , replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1 . 
 
 After doing so, return the array. 

 Example 1: 
 
```
Input:
 arr = [17,18,5,4,6,1]

Output:
 [18,6,6,6,1,-1]

Explanation:
 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
```

 Example 2: 
 
```
Input:
 arr = [400]

Output:
 [-1]

Explanation:
 There are no elements to the right of index 0.
```

 Constraints: 

 1 <= arr.length <= 10 4 
 
 1 <= arr[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();
        int maxRight = -1;
        for (int i = n - 1; i >= 0; --i) {
            int temp = arr[i];
            arr[i] = maxRight;
            maxRight = max(maxRight, temp);
        }
        return arr;
    }
};
```


## 1313. Decompress Run-Length Encoded List

**Problem:** https://leetcode.com/problems/decompress-run-length-encoded-list/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + L)

**Space complexity:** O(L)

**Complexity reasoning:** Processes n input entries in pairs and appends L=sum(nums[0],nums[2],...) decoded values to the output.

### Problem description

We are given a list nums of integers representing a list compressed with run-length encoding. 
 
 Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]]  (with i >= 0 ).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list. 
 
 Return the decompressed list. 

 Example 1: 
 
```
Input:
 nums = [1,2,3,4]

Output:
 [2,4,4,4]

Explanation:
 The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
```

 Example 2: 
 
```
Input:
 nums = [1,1,2,3]

Output:
 [1,3,3]
```

 Constraints: 

 2 <= nums.length <= 100 
 
 nums.length % 2 == 0 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> res;
        for (int i = 0; i < nums.size(); i += 2)
            res.insert(res.end(), nums[i], nums[i + 1]);
        return res;
    }
};
```


## 1375. Number of Times Binary String Is Prefix-Aligned

**Problem:** https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Scans flips once, tracking the largest flipped position and incrementing a counter when the prefix is complete.

### Problem description

You have a 1-indexed binary string of length n where all the bits are 0 initially. We will flip all the bits of this binary string (i.e., change them from 0 to 1 ) one by one. You are given a 1-indexed integer array flips where flips[i] indicates that the bit at index flips[i] will be flipped in the i th step. 
 
 A binary string is prefix-aligned if, after the i th step, all the bits in the inclusive range [1, i] are ones and all the other bits are zeros. 
 
 Return the number of times the binary string is prefix-aligned during the flipping process . 

 Example 1: 
 
```
Input:
 flips = [3,2,4,1,5]

Output:
 2

Explanation:
 The binary string is initially "00000".
After applying step 1: The string becomes "00100", which is not prefix-aligned.
After applying step 2: The string becomes "01100", which is not prefix-aligned.
After applying step 3: The string becomes "01110", which is not prefix-aligned.
After applying step 4: The string becomes "11110", which is prefix-aligned.
After applying step 5: The string becomes "11111", which is prefix-aligned.
We can see that the string was prefix-aligned 2 times, so we return 2.
```

 Example 2: 
 
```
Input:
 flips = [4,1,2,3]

Output:
 1

Explanation:
 The binary string is initially "0000".
After applying step 1: The string becomes "0001", which is not prefix-aligned.
After applying step 2: The string becomes "1001", which is not prefix-aligned.
After applying step 3: The string becomes "1101", which is not prefix-aligned.
After applying step 4: The string becomes "1111", which is prefix-aligned.
We can see that the string was prefix-aligned 1 time, so we return 1.
```

 Constraints: 

 n == flips.length 
 
 1 <= n <= 5 * 10 4 
 
 flips is a permutation of the integers in the range [1, n] .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int numTimesAllBlue(vector<int>& flips) {
        int res = 0, maxFlip = 0;
        for (int i = 0; i < flips.size(); ++i) {
            maxFlip = max(maxFlip, flips[i]);
            if (maxFlip == i + 1) res++;
        }
        return res;
    }
};
```


## 1380. Lucky Numbers in a Matrix

**Problem:** https://leetcode.com/problems/lucky-numbers-in-a-matrix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(m(n + m))

**Space complexity:** O(m) output

**Complexity reasoning:** For each of m rows, finds its minimum among n columns and checks that column across m rows; stores up to m lucky numbers.

### Problem description

Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order . 
 
 A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column. 

 Example 1: 
 
```
Input:
 matrix = [[3,7,8],[9,11,13],[15,16,17]]

Output:
 [15]

Explanation:
 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
```

 Example 2: 
 
```
Input:
 matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]

Output:
 [12]

Explanation:
 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
```

 Example 3: 
 
```
Input:
 matrix = [[7,8],[1,2]]

Output:
 [7]

Explanation:
 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
```

 Constraints: 

 m == mat.length 
 
 n == mat[i].length 
 
 1 <= n, m <= 50 
 
 1 <= matrix[i][j] <= 10 5 . 
 
 All elements in the matrix are distinct.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> res;
        for (int i = 0; i < matrix.size(); ++i) {
            int colIdx = 0;
            for (int j = 1; j < matrix[0].size(); ++j)
                if (matrix[i][j] < matrix[i][colIdx])
                    colIdx = j;

            bool isMax = true;
            for (int k = 0; k < matrix.size(); ++k)
                if (matrix[k][colIdx] > matrix[i][colIdx]) {
                    isMax = false;
                    break;
                }

            if (isMax) res.push_back(matrix[i][colIdx]);
        }
        return res;
    }
};
```


## 1389. Create Target Array in the Given Order

**Problem:** https://leetcode.com/problems/create-target-array-in-the-given-order/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n^2)

**Space complexity:** O(n)

**Complexity reasoning:** Inserts each new value at an arbitrary vector position; shifting existing elements can take O(i) on insertion i.

### Problem description

Given two arrays of integers  nums and index . Your task is to create target array under the following rules: 

 Initially target array is empty. 
 
 From left to right read nums[i] and index[i], insert at index index[i]  the value nums[i]  in  target array. 
 
 Repeat the previous step until there are no elements to read in nums and index. 

 Return the target array. 
 
 It is guaranteed that the insertion operations will be valid. 

 Example 1: 
 
```
Input:
 nums = [0,1,2,3,4], index = [0,1,2,2,1]

Output:
 [0,4,1,3,2]

Explanation:

nums index target
0 0 [0]
1 1 [0,1]
2 2 [0,1,2]
3 2 [0,1,3,2]
4 1 [0,4,1,3,2]
```

 Example 2: 
 
```
Input:
 nums = [1,2,3,4,0], index = [0,1,2,3,0]

Output:
 [0,1,2,3,4]

Explanation:

nums index target
1 0 [1]
2 1 [1,2]
3 2 [1,2,3]
4 3 [1,2,3,4]
0 0 [0,1,2,3,4]
```

 Example 3: 
 
```
Input:
 nums = [1], index = [0]

Output:
 [1]
```

 Constraints: 

 1 <= nums.length, index.length <= 100 
 
 nums.length == index.length 
 
 0 <= nums[i] <= 100 
 
 0 <= index[i] <= i

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int> res;
        for (int i = 0; i < nums.size(); ++i) {
            res.insert(res.begin() + index[i], nums[i]);
        }
        return res;
    }
};
```


## 1431. Kids With the Greatest Number of Candies

**Problem:** https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output

**Complexity reasoning:** Finds the maximum with one pass and creates one Boolean answer for each child with a second pass.

### Problem description

There are n kids with candies. You are given an integer array candies , where each candies[i] represents the number of candies the i th kid has, and an integer extraCandies , denoting the number of extra candies that you have. 
 
 Return a boolean array result of length n , where result[i] is true if, after giving the i th kid all the extraCandies , they will have the greatest number of candies among all the kids , or false otherwise . 
 
 Note that multiple kids can have the greatest number of candies. 

 Example 1: 
 
```
Input:
 candies = [2,3,5,1,3], extraCandies = 3

Output:
 [true,true,true,false,true] 

Explanation:
 If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
```

 Example 2: 
 
```
Input:
 candies = [4,2,1,1,2], extraCandies = 1

Output:
 [true,false,false,false,false] 

Explanation:
 There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
```

 Example 3: 
 
```
Input:
 candies = [12,1,12], extraCandies = 10

Output:
 [true,false,true]
```

 Constraints: 

 n == candies.length 
 
 2 <= n <= 100 
 
 1 <= candies[i] <= 100 
 
 1 <= extraCandies <= 50

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxCandies = *max_element(candies.begin(), candies.end());
        vector<bool> result;
        for (int candy : candies) {
            result.push_back(candy + extraCandies >= maxCandies);
        }
        return result;
    }
};
```


## 1437. Check If All 1's Are at Least Length K Places Away

**Problem:** https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Checks each position once and stores only the previous position containing a one.

### Problem description

Given an binary array nums and an integer k , return true if all 1 's are at least k places away from each other, otherwise return false . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png] 
 
```
Input:
 nums = [1,0,0,0,1,0,0,1], k = 2

Output:
 true

Explanation:
 Each of the 1s are at least 2 places away from each other.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png] 
 
```
Input:
 nums = [1,0,0,1,0,1], k = 2

Output:
 false

Explanation:
 The second 1 and third 1 are only one apart from each other.
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 0 <= k <= nums.length 
 
 nums[i] is 0 or 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int prev = -k - 1;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] == 1) {
                if (i - prev <= k) return false;
                prev = i;
            }
        }
        return true;
    }
};
```


## 1450. Number of Students Doing Homework at a Given Time

**Problem:** https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Checks the start and end times for each student with constant work per entry.

### Problem description

Given two integer arrays startTime and endTime and given an integer queryTime . 
 
 The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i] . 
 
 Return the number of students doing their homework at time queryTime . More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive. 

 Example 1: 
 
```
Input:
 startTime = [1,2,3], endTime = [3,2,7], queryTime = 4

Output:
 1

Explanation:
 We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.
```

 Example 2: 
 
```
Input:
 startTime = [4], endTime = [4], queryTime = 4

Output:
 1

Explanation:
 The only student was doing their homework at the queryTime.
```

 Constraints: 

 startTime.length == endTime.length 
 
 1 <= startTime.length <= 100 
 
 1 <= startTime[i] <= endTime[i] <= 1000 
 
 1 <= queryTime <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        int count = 0;
        for (int i = 0; i < startTime.size(); ++i) {
            if (startTime[i] <= queryTime && queryTime <= endTime[i])
                count++;
        }
        return count;
    }
};
```


## 1470. Shuffle the Array

**Problem:** https://leetcode.com/problems/shuffle-the-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output

**Complexity reasoning:** Appends two elements for each of n iterations; reserve avoids repeated vector growth.

### Problem description

Given the array nums consisting of 2n elements in the form [x 1 ,x 2 ,...,x n ,y 1 ,y 2 ,...,y n ] . 
 
 Return the array in the form [x 1 ,y 1 ,x 2 ,y 2 ,...,x n ,y n ] . 

 Example 1: 
 
```
Input:
 nums = [2,5,1,3,4,7], n = 3

Output:
 [2,3,5,4,1,7] 

Explanation:
 Since x
1
=2, x
2
=5, x
3
=1, y
1
=3, y
2
=4, y
3
=7 then the answer is [2,3,5,4,1,7].
```

 Example 2: 
 
```
Input:
 nums = [1,2,3,4,4,3,2,1], n = 4

Output:
 [1,4,2,3,3,2,4,1]
```

 Example 3: 
 
```
Input:
 nums = [1,1,2,2], n = 2

Output:
 [1,2,1,2]
```

 Constraints: 

 1 <= n <= 500 
 
 nums.length == 2n 
 
 1 <= nums[i] <= 10^3

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans;
        ans.reserve(2 * n);
        for (int i = 0; i < n; ++i) {
            ans.push_back(nums[i]);
            ans.push_back(nums[i + n]);
        }
        return ans;
    }
};
```


## 1503. Last Moment Before All Ants Fall Out of a Plank

**Problem:** https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Brainteaser, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(L + R)

**Space complexity:** O(1)

**Complexity reasoning:** Computes the maximum left-ant position and minimum right-ant position with two linear scans.

### Problem description

We have a wooden plank of the length n units . Some ants are walking on the plank, each ant moves with a speed of 1 unit per second . Some of the ants move to the left , the other move to the right . 
 
 When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time. 
 
 When an ant reaches one end of the plank at a time t , it falls out of the plank immediately. 
 
 Given an integer n and two integer arrays left and right , the positions of the ants moving to the left and the right, return the moment when the last ant(s) fall out of the plank . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/06/17/ants.jpg] 
 
```
Input:
 n = 4, left = [4,3], right = [0,1]

Output:
 4

Explanation:
 In the image above:
-The ant at index 0 is named A and going to the right.
-The ant at index 1 is named B and going to the right.
-The ant at index 3 is named C and going to the left.
-The ant at index 4 is named D and going to the left.
The last moment when an ant was on the plank is t = 4 seconds. After that, it falls immediately out of the plank. (i.e., We can say that at t = 4.0000000001, there are no ants on the plank).
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/06/17/ants2.jpg] 
 
```
Input:
 n = 7, left = [], right = [0,1,2,3,4,5,6,7]

Output:
 7

Explanation:
 All ants are going to the right, the ant at index 0 needs 7 seconds to fall.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2020/06/17/ants3.jpg] 
 
```
Input:
 n = 7, left = [0,1,2,3,4,5,6,7], right = []

Output:
 7

Explanation:
 All ants are going to the left, the ant at index 7 needs 7 seconds to fall.
```

 Constraints: 

 1 <= n <= 10 4 
 
 0 <= left.length <= n + 1 
 
 0 <= left[i] <= n 
 
 0 <= right.length <= n + 1 
 
 0 <= right[i] <= n 
 
 1 <= left.length + right.length <= n + 1 
 
 All values of left and right are unique, and each value can appear only in one of the two arrays.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int maxLeft = left.empty() ? 0 : *max_element(left.begin(), left.end());
        int maxRight = right.empty() ? 0 : n - *min_element(right.begin(), right.end());
        return max(maxLeft, maxRight);
    }
};
```


## 1534. Count Good Triplets

**Problem:** https://leetcode.com/problems/count-good-triplets/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n^3)

**Space complexity:** O(1)

**Complexity reasoning:** Enumerates all triples i<j<k using three nested loops and evaluates three constant-time comparisons.

### Problem description

Given an array of integers arr , and three integers  a ,  b  and  c . You need to find the number of good triplets. 
 
 A triplet (arr[i], arr[j], arr[k])  is good if the following conditions are true: 

 0 <= i < j < k < arr.length 
 
 |arr[i] - arr[j]| <= a 
 
 |arr[j] - arr[k]| <= b 
 
 |arr[i] - arr[k]| <= c 

 Where |x| denotes the absolute value of x . 
 
 Return the number of good triplets . 

 Example 1: 
 
```
Input:
 arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3

Output:
 4

Explanation:
 There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
```

 Example 2: 
 
```
Input:
 arr = [1,1,2,2,3], a = 0, b = 0, c = 1

Output:
 0

Explanation: 
No triplet satisfies all conditions.
```

 Constraints: 

 3 <= arr.length <= 100 
 
 0 <= arr[i] <= 1000 
 
 0 <= a, b, c <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int res = 0, n = arr.size();
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                for (int k = j + 1; k < n; ++k)
                    if (abs(arr[i] - arr[j]) <= a &&
                        abs(arr[j] - arr[k]) <= b &&
                        abs(arr[i] - arr[k]) <= c)
                        res++;
        return res;
    }
};
```


## 1535. Find the Winner of an Array Game

**Problem:** https://leetcode.com/problems/find-the-winner-of-an-array-game/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Maintains the current winner and consecutive win count in a single pass, possibly stopping early.

### Problem description

Given an integer array arr of distinct integers and an integer k . 
 
 A game will be played between the first two elements of the array (i.e. arr[0] and arr[1] ). In each round of the game, we compare arr[0] with arr[1] , the larger integer wins and remains at position 0 , and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds. 
 
 Return the integer which will win the game . 
 
 It is guaranteed that there will be a winner of the game. 

 Example 1: 
 
```
Input:
 arr = [2,1,3,5,4,6,7], k = 2

Output:
 5

Explanation:
 Let's see the rounds of the game:
Round | arr | winner | win_count
 1 | [2,1,3,5,4,6,7] | 2 | 1
 2 | [2,3,5,4,6,7,1] | 3 | 1
 3 | [3,5,4,6,7,1,2] | 5 | 1
 4 | [5,4,6,7,1,2,3] | 5 | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
```

 Example 2: 
 
```
Input:
 arr = [3,2,1], k = 10

Output:
 3

Explanation:
 3 will win the first 10 rounds consecutively.
```

 Constraints: 

 2 <= arr.length <= 10 5 
 
 1 <= arr[i] <= 10 6 
 
 arr contains distinct integers. 
 
 1 <= k <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        int win = arr[0], count = 0;
        for (int i = 1; i < arr.size(); ++i) {
            if (win > arr[i]) count++;
            else {
                win = arr[i];
                count = 1;
            }
            if (count == k) return win;
        }
        return win;
    }
};
```


## 1550. Three Consecutive Odds

**Problem:** https://leetcode.com/problems/three-consecutive-odds/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Scans values once, tracking the length of the current odd-number streak.

### Problem description

Given an integer array arr , return true  if there are three consecutive odd numbers in the array. Otherwise, return  false .

 Example 1: 
 
```
Input:
 arr = [2,6,4,1]

Output:
 false

Explanation:
 There are no three consecutive odds.
```

 Example 2: 
 
```
Input:
 arr = [1,2,34,3,4,5,7,23,12]

Output:
 true

Explanation:
 [5,7,23] are three consecutive odds.
```

 Constraints: 

 1 <= arr.length <= 1000 
 
 1 <= arr[i] <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int run = 0;
        for (int x : arr) {
            run = (x % 2 != 0) ? run + 1 : 0;
            if (run == 3) return true;
        }
        return false;
    }
};
```


## 1560. Most Visited Sector in  a Circular Track

**Problem:** https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output

**Complexity reasoning:** Emits the visited sectors between the initial and final sector, possibly wrapping once; no more than n sectors are emitted.

### Problem description

Given an integer n and an integer array rounds . We have a circular track which consists of n sectors labeled from 1 to n . A marathon will be held on this track, the marathon consists of m rounds. The i th round starts at sector rounds[i - 1] and ends at sector rounds[i] . For example, round 1 starts at sector rounds[0] and ends at sector rounds[1] 
 
 Return an array of the most visited sectors sorted in ascending order. 
 
 Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example). 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/08/14/tmp.jpg] 
 
```
Input:
 n = 4, rounds = [1,3,1,2]

Output:
 [1,2]

Explanation:
 The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are visited only once.
```

 Example 2: 
 
```
Input:
 n = 2, rounds = [2,1,2,1,2,1,2,1,2]

Output:
 [2]
```

 Example 3: 
 
```
Input:
 n = 7, rounds = [1,3,5,7]

Output:
 [1,2,3,4,5,6,7]
```

 Constraints: 

 2 <= n <= 100 
 
 1 <= m <= 100 
 
 rounds.length == m + 1 
 
 1 <= rounds[i] <= n 
 
 rounds[i] != rounds[i + 1] for 0 <= i < m

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> mostVisited(int n, vector<int>& rounds) {
        int first = rounds.front(), last = rounds.back();
        vector<int> ans;
        if (first <= last) {
            for (int x = first; x <= last; ++x) ans.push_back(x);
        } else {
            for (int x = 1; x <= last; ++x) ans.push_back(x);
            for (int x = first; x <= n; ++x) ans.push_back(x);
        }
        return ans;
    }
};
```


## 1566. Detect Pattern of Length M Repeated K or More Times

**Problem:** https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(nmk)

**Space complexity:** O(1)

**Complexity reasoning:** For each possible starting index (at most n), compares up to m*k elements against the repeated base pattern.

### Problem description

Given an array of positive integers arr , find a pattern of length m that is repeated k or more times. 
 
 A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions. 
 
 Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false . 

 Example 1: 
 
```
Input:
 arr = [1,2,4,4,4,4], m = 1, k = 3

Output:
 true

Explanation: 
The pattern 
(4)
 of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.
```

 Example 2: 
 
```
Input:
 arr = [1,2,1,2,1,1,1,3], m = 2, k = 2

Output:
 true

Explanation: 
The pattern 
(1,2)
 of length 2 is repeated 2 consecutive times. Another valid pattern 
(2,1) is
 also repeated 2 times.
```

 Example 3: 
 
```
Input:
 arr = [1,2,1,2,1,3], m = 2, k = 3

Output:
 false

Explanation: 
The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times.
```

 Constraints: 

 2 <= arr.length <= 100 
 
 1 <= arr[i] <= 100 
 
 1 <= m <= 100 
 
 2 <= k <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    bool containsPattern(vector<int>& arr, int m, int k) {
        int n = arr.size();
        for (int i = 0; i <= n - m * k; ++i) {
            bool match = true;
            for (int j = 0; j < m * k; ++j) {
                if (arr[i + j] != arr[i + j % m]) {
                    match = false;
                    break;
                }
            }
            if (match) return true;
        }
        return false;
    }
};
```


## 1572. Matrix Diagonal Sum

**Problem:** https://leetcode.com/problems/matrix-diagonal-sum/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Adds both diagonal cells for each row and subtracts the center once for odd n.

### Problem description

Given a square matrix  mat , return the sum of the matrix diagonals. 
 
 Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png] 
 
```
Input:
 mat = [[
1
,2,
3
],
  [4,
5
,6],
  [
7
,8,
9
]]

Output:
 25

Explanation: 
Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
```

 Example 2: 
 
```
Input:
 mat = [[
1
,1,1,
1
],
  [1,
1
,
1
,1],
  [1,
1
,
1
,1],
  [
1
,1,1,
1
]]

Output:
 8
```

 Example 3: 
 
```
Input:
 mat = [[
5
]]

Output:
 5
```

 Constraints: 

 n == mat.length == mat[i].length 
 
 1 <= n <= 100 
 
 1 <= mat[i][j] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int n = mat.size(), sum = 0;
        for (int i = 0; i < n; ++i) {
            sum += mat[i][i] + mat[i][n - i - 1];
        }
        if (n % 2) sum -= mat[n / 2][n / 2];
        return sum;
    }
};
```


## 1582. Special Positions in a Binary Matrix

**Problem:** https://leetcode.com/problems/special-positions-in-a-binary-matrix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(m + n)

**Complexity reasoning:** Scans the m-by-n matrix to compute row and column counts, then scans it again to count special cells.

### Problem description

Given an m x n binary matrix mat , return the number of special positions in mat . 
 
 A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed ). 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/12/23/special1.jpg] 
 
```
Input:
 mat = [[1,0,0],[0,0,1],[1,0,0]]

Output:
 1

Explanation:
 (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg] 
 
```
Input:
 mat = [[1,0,0],[0,1,0],[0,0,1]]

Output:
 3

Explanation:
 (0, 0), (1, 1) and (2, 2) are special positions.
```

 Constraints: 

 m == mat.length 
 
 n == mat[i].length 
 
 1 <= m, n <= 100 
 
 mat[i][j] is either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size(), res = 0;
        vector<int> row(m), col(n);
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                row[i] += mat[i][j], col[j] += mat[i][j];

        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (mat[i][j] == 1 && row[i] == 1 && col[j] == 1)
                    res++;
        return res;
    }
};
```


## 1583. Count Unhappy Friends

**Problem:** https://leetcode.com/problems/count-unhappy-friends/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n^2)

**Space complexity:** O(n^2)

**Complexity reasoning:** Builds an n-by-n preference-rank matrix, records partners, and checks at most n-1 preferred people for each of n friends.

### Problem description

You are given a list of  preferences  for  n  friends, where n is always even . 
 
 For each person i ,  preferences[i]  contains a list of friends  sorted in the order of preference . In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1 . 
 
 All the friends are divided into pairs. The pairings are given in a list  pairs , where pairs[i] = [x i , y i ] denotes x i  is paired with y i and y i is paired with x i . 
 
 However, this pairing may cause some of the friends to be unhappy. A friend x  is unhappy if x  is paired with y  and there exists a friend u  who is paired with v  but: 

 x  prefers u  over y , and 
 
 u  prefers x  over v . 

 Return the number of unhappy friends . 

 Example 1: 
 
```
Input:
 n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]

Output:
 2

Explanation:

Friend 1 is unhappy because:
- 1 is paired with 0 but prefers 3 over 0, and
- 3 prefers 1 over 2.
Friend 3 is unhappy because:
- 3 is paired with 2 but prefers 1 over 2, and
- 1 prefers 3 over 0.
Friends 0 and 2 are happy.
```

 Example 2: 
 
```
Input:
 n = 2, preferences = [[1], [0]], pairs = [[1, 0]]

Output:
 0

Explanation:
 Both friends 0 and 1 are happy.
```

 Example 3: 
 
```
Input:
 n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]

Output:
 4
```

 Constraints: 

 2 <= n <= 500 
 
 n  is even. 
 
 preferences.length == n 
 
 preferences[i].length == n - 1 
 
 0 <= preferences[i][j] <= n - 1 
 
 preferences[i]  does not contain i . 
 
 All values in  preferences[i]  are unique. 
 
 pairs.length == n/2 
 
 pairs[i].length == 2 
 
 x i != y i 
 
 0 <= x i , y i  <= n - 1 
 
 Each person is contained in exactly one pair.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int unhappyFriends(int n, vector<vector<int>>& preferences,
                       vector<vector<int>>& pairs) {
        vector<vector<int>> rank(n, vector<int>(n));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n - 1; ++j)
                rank[i][preferences[i][j]] = j;
        vector<int> partner(n);
        for (auto& p : pairs) { partner[p[0]] = p[1]; partner[p[1]] = p[0]; }
        int ans = 0;
        for (int x = 0; x < n; ++x) {
            for (int u : preferences[x]) {
                if (u == partner[x]) break;
                if (rank[u][x] < rank[u][partner[u]]) {
                    ++ans; break;
                }
            }
        }
        return ans;
    }
};
```


## 1599. Maximum Profit of Operating a Centennial Wheel

**Problem:** https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(c + W)

**Space complexity:** O(1)

**Complexity reasoning:** Processes c arriving customer groups and continues for W additional wheel turns to serve remaining customers (at most four per turn).

### Problem description

You are the operator of a Centennial Wheel that has four gondolas , and each gondola has room for up to four people . You have the ability to rotate the gondolas counterclockwise , which costs you runningCost dollars. 
 
 You are given an array customers of length n where customers[i] is the number of new customers arriving just before the i th rotation (0-indexed). This means you must rotate the wheel i times before the customers[i] customers arrive . You cannot make customers wait if there is room in the gondola . Each customer pays boardingCost dollars when they board on the gondola closest to the ground and will exit once that gondola reaches the ground again. 
 
 You can stop the wheel at any time, including before serving all customers . If you decide to stop serving customers, all subsequent rotations are free in order to get all the customers down safely. Note that if there are currently more than four customers waiting at the wheel, only four will board the gondola, and the rest will wait for the next rotation . 
 
 Return the minimum number of rotations you need to perform to maximize your profit. If there is no scenario where the profit is positive, return -1 . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/09/wheeldiagram12.png] 
 
```
Input:
 customers = [8,3], boardingCost = 5, runningCost = 6

Output:
 3

Explanation:
 The numbers written on the gondolas are the number of people currently there.
1. 8 customers arrive, 4 board and 4 wait for the next gondola, the wheel rotates. Current profit is 4 * $5 - 1 * $6 = $14.
2. 3 customers arrive, the 4 waiting board the wheel and the other 3 wait, the wheel rotates. Current profit is 8 * $5 - 2 * $6 = $28.
3. The final 3 customers board the gondola, the wheel rotates. Current profit is 11 * $5 - 3 * $6 = $37.
The highest profit was $37 after rotating the wheel 3 times.
```

 Example 2: 
 
```
Input:
 customers = [10,9,6], boardingCost = 6, runningCost = 4

Output:
 7

Explanation:

1. 10 customers arrive, 4 board and 6 wait for the next gondola, the wheel rotates. Current profit is 4 * $6 - 1 * $4 = $20.
2. 9 customers arrive, 4 board and 11 wait (2 originally waiting, 9 newly waiting), the wheel rotates. Current profit is 8 * $6 - 2 * $4 = $40.
3. The final 6 customers arrive, 4 board and 13 wait, the wheel rotates. Current profit is 12 * $6 - 3 * $4 = $60.
4. 4 board and 9 wait, the wheel rotates. Current profit is 16 * $6 - 4 * $4 = $80.
5. 4 board and 5 wait, the wheel rotates. Current profit is 20 * $6 - 5 * $4 = $100.
6. 4 board and 1 waits, the wheel rotates. Current profit is 24 * $6 - 6 * $4 = $120.
7. 1 boards, the wheel rotates. Current profit is 25 * $6 - 7 * $4 = $122.
The highest profit was $122 after rotating the wheel 7 times.
```

 Example 3: 
 
```
Input:
 customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92

Output:
 -1

Explanation:

1. 3 customers arrive, 3 board and 0 wait, the wheel rotates. Current profit is 3 * $1 - 1 * $92 = -$89.
2. 4 customers arrive, 4 board and 0 wait, the wheel rotates. Current profit is 7 * $1 - 2 * $92 = -$177.
3. 0 customers arrive, 0 board and 0 wait, the wheel rotates. Current profit is 7 * $1 - 3 * $92 = -$269.
4. 5 customers arrive, 4 board and 1 waits, the wheel rotates. Current profit is 11 * $1 - 4 * $92 = -$357.
5. 1 customer arrives, 2 board and 0 wait, the wheel rotates. Current profit is 13 * $1 - 5 * $92 = -$447.
The profit was never positive, so return -1.
```

 Constraints: 

 n == customers.length 
 
 1 <= n <= 10 5 
 
 0 <= customers[i] <= 50 
 
 1 <= boardingCost, runningCost <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperationsMaxProfit(vector<int>& customers, int boardingCost,
                               int runningCost) {
        int waiting = 0, profit = 0, best = 0, answer = -1;
        int i = 0, turns = 0;
        while (i < (int)customers.size() || waiting > 0) {
            if (i < (int)customers.size()) waiting += customers[i++];
            int boarded = min(4, waiting);
            waiting -= boarded;
            profit += boarded * boardingCost - runningCost;
            ++turns;
            if (profit > best) { best = profit; answer = turns; }
        }
        return answer;
    }
};
```


## 1620. Coordinate With Maximum Network Quality

**Problem:** https://leetcode.com/problems/coordinate-with-maximum-network-quality/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(51^2 * t)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Evaluates all 51-by-51 candidate coordinates and scans all t towers for each; only a few scalars and a two-element answer are stored.

### Problem description

You are given an array of network towers towers , where towers[i] = [x i , y i , q i ] denotes the i th network tower with location (x i , y i ) and quality factor q i . All the coordinates are integral coordinates on the X-Y plane, and the distance between the two coordinates is the Euclidean distance . 
 
 You are also given an integer radius where a tower is reachable if the distance is less than or equal to radius . Outside that distance, the signal becomes garbled, and the tower is not reachable . 
 
 The signal quality of the i th tower at a coordinate (x, y) is calculated with the formula ⌊q i / (1 + d)⌋ , where d is the distance between the tower and the coordinate. The network quality at a coordinate is the sum of the signal qualities from all the reachable towers. 
 
 Return the array [c x , c y ] representing the integral coordinate (c x , c y ) where the network quality is maximum. If there are multiple coordinates with the same network quality , return the lexicographically minimum non-negative coordinate. 
 
 Note: 

 A coordinate (x1, y1) is lexicographically smaller than (x2, y2) if either:

 x1 < x2 , or 
 
 x1 == x2 and y1 < y2 . 

 ⌊val⌋ is the greatest integer less than or equal to val (the floor function). 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/22/untitled-diagram.png] 
 
```
Input:
 towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2

Output:
 [2,1]

Explanation:
 At coordinate (2, 1) the total quality is 13.
- Quality of 7 from (2, 1) results in ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
- Quality of 5 from (1, 2) results in ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
- Quality of 9 from (3, 1) results in ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
No other coordinate has a higher network quality.
```

 Example 2: 
 
```
Input:
 towers = [[23,11,21]], radius = 9

Output:
 [23,11]

Explanation:
 Since there is only one tower, the network quality is highest right at the tower's location.
```

 Example 3: 
 
```
Input:
 towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2

Output:
 [1,2]

Explanation:
 Coordinate (1, 2) has the highest network quality.
```

 Constraints: 

 1 <= towers.length <= 50 
 
 towers[i].length == 3 
 
 0 <= x i , y i , q i <= 50 
 
 1 <= radius <= 50

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> bestCoordinate(vector<vector<int>>& towers, int radius) {
        int best = -1;
        vector<int> ans = {0, 0};
        for (int x = 0; x <= 50; ++x) for (int y = 0; y <= 50; ++y) {
            int quality = 0;
            for (auto& t : towers) {
                int dx = x - t[0], dy = y - t[1];
                if (dx * dx + dy * dy <= radius * radius)
                    quality += (int)floor(t[2] / (1.0 + sqrt(dx * dx + dy * dy)));
            }
            if (quality > best) { best = quality; ans = {x, y}; }
        }
        return ans;
    }
};
```


## 1646. Get Maximum in Generated Array

**Problem:** https://leetcode.com/problems/get-maximum-in-generated-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Builds n+1 dynamic-programming values and then scans the vector once to find its maximum.

### Problem description

You are given an integer n . A 0-indexed integer array nums of length n + 1 is generated in the following way: 

 nums[0] = 0 
 
 nums[1] = 1 
 
 nums[2 * i] = nums[i] when 2 <= 2 * i <= n 
 
 nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n 

 Return the maximum integer in the array nums ​​​. 

 Example 1: 
 
```
Input:
 n = 7

Output:
 3

Explanation:
 According to the given rules:
 nums[0] = 0
 nums[1] = 1
 nums[(1 * 2) = 2] = nums[1] = 1
 nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
 nums[(2 * 2) = 4] = nums[2] = 1
 nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
 nums[(3 * 2) = 6] = nums[3] = 2
 nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.
```

 Example 2: 
 
```
Input:
 n = 2

Output:
 1

Explanation:
 According to the given rules, nums = [0,1,1]. The maximum is max(0,1,1) = 1.
```

 Example 3: 
 
```
Input:
 n = 3

Output:
 2

Explanation:
 According to the given rules, nums = [0,1,1,2]. The maximum is max(0,1,1,2) = 2.
```

 Constraints: 

 0 <= n <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n == 0) return 0;
        vector<int> nums(n + 1);
        nums[0] = 0; nums[1] = 1;
        for (int i = 2; i <= n; ++i) {
            if (i % 2 == 0) nums[i] = nums[i / 2];
            else nums[i] = nums[i / 2] + nums[i / 2 + 1];
        }
        return *max_element(nums.begin(), nums.end());
    }
};
```


## 1672. Richest Customer Wealth

**Problem:** https://leetcode.com/problems/richest-customer-wealth/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(1)

**Complexity reasoning:** Sums n balances for each of m customer accounts; no auxiliary array is created.

### Problem description

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​ ​​​​​​th ​​​​ customer has in the j​​​​​ ​​​​​​th ​​​​ bank. Return the wealth that the richest customer has. 
 
 A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth . 

 Example 1: 
 
```
Input:
 accounts = [[1,2,3],[3,2,1]]

Output:
 6

Explanation
:

1st customer has wealth = 1 + 2 + 3 = 6

2nd customer has wealth = 3 + 2 + 1 = 6

Both customers are considered the richest with a wealth of 6 each, so return 6.
```

 Example 2: 
 
```
Input:
 accounts = [[1,5],[7,3],[3,5]]

Output:
 10

Explanation
: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
```

 Example 3: 
 
```
Input:
 accounts = [[2,8,7],[7,1,3],[1,9,5]]

Output:
 17
```

 Constraints: 

 m == accounts.length 
 
 n == accounts[i].length 
 
 1 <= m, n <= 50 
 
 1 <= accounts[i][j] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxWealth = 0;
        for (auto& account : accounts) {
            int sum = accumulate(account.begin(), account.end(), 0);
            maxWealth = max(maxWealth, sum);
        }
        return maxWealth;
    }
};
```


## 1701. Average Waiting Time

**Problem:** https://leetcode.com/problems/average-waiting-time/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Updates the finish time and accumulated waiting time for each customer exactly once.

### Problem description

There is a restaurant with a single chef. You are given an array customers , where customers[i] = [arrival i , time i ]: 

 arrival i is the arrival time of the i th customer. The arrival times are sorted in non-decreasing order. 
 
 time i is the time needed to prepare the order of the i th customer. 

 When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input . 
 
 Return the average waiting time of all customers . Solutions within 10 -5 from the actual answer are considered accepted. 

 Example 1: 
 
```
Input:
 customers = [[1,2],[2,5],[4,3]]

Output:
 5.00000

Explanation:

1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
So the average waiting time = (2 + 6 + 7) / 3 = 5.
```

 Example 2: 
 
```
Input:
 customers = [[5,2],[5,4],[10,3],[20,1]]

Output:
 3.25000

Explanation:

1) The first customer arrives at time 5, the chef takes his order and starts preparing it immediately at time 5, and finishes at time 7, so the waiting time of the first customer is 7 - 5 = 2.
2) The second customer arrives at time 5, the chef takes his order and starts preparing it at time 7, and finishes at time 11, so the waiting time of the second customer is 11 - 5 = 6.
3) The third customer arrives at time 10, the chef takes his order and starts preparing it at time 11, and finishes at time 14, so the waiting time of the third customer is 14 - 10 = 4.
4) The fourth customer arrives at time 20, the chef takes his order and starts preparing it immediately at time 20, and finishes at time 21, so the waiting time of the fourth customer is 21 - 20 = 1.
So the average waiting time = (2 + 6 + 4 + 1) / 4 = 3.25.
```

 Constraints: 

 1 <= customers.length <= 10 5 
 
 1 <= arrival i , time i <= 10 4 
 
 arrival i  <= arrival i+1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        long long time = 0, wait = 0;
        for (auto& c : customers) {
            time = max(time, (long long)c[0]) + c[1];
            wait += time - c[0];
        }
        return (double)wait / customers.size();
    }
};
```


## 1706. Where Will the Ball Fall

**Problem:** https://leetcode.com/problems/where-will-the-ball-fall/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(n) output

**Complexity reasoning:** Simulates n starting columns, following each ball through at most m rows, and stores one result per ball.

### Problem description

You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides. 
 
 Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left. 

 A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1 . 
 
 A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1 . 

 We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box. 
 
 Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the i th column at the top, or -1 if the ball gets stuck in the box . 

 Example 1: 
 
 [Figure: https://assets.leetcode.com/uploads/2019/09/26/ball.jpg] 
 
```
Input:
 grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]

Output:
 [1,-1,-1,-1,-1]

Explanation:
 This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
```

 Example 2: 
 
```
Input:
 grid = [[-1]]

Output:
 [-1]

Explanation:
 The ball gets stuck against the left wall.
```

 Example 3: 
 
```
Input:
 grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]

Output:
 [0,1,2,3,4,-1]
```

 Constraints: 

 m == grid.length 
 
 n == grid[i].length 
 
 1 <= m, n <= 100 
 
 grid[i][j] is 1 or -1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int> res(n);
        for (int j = 0; j < n; ++j) {
            int col = j;
            for (int i = 0; i < m; ++i) {
                int next = col + grid[i][col];
                if (next < 0 || next >= n || grid[i][col] != grid[i][next]) {
                    col = -1;
                    break;
                }
                col = next;
            }
            res[j] = col;
        }
        return res;
    }
};
```


## 1725. Number Of Rectangles That Can Form The Largest Square

**Problem:** https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Scans rectangles once, updating the largest possible square side and its frequency.

### Problem description

You are given an array rectangles where rectangles[i] = [l i , w i ] represents the i th rectangle of length l i and width w i . 
 
 You can cut the i th rectangle to form a square with a side length of k if both k <= l i and k <= w i . For example, if you have a rectangle [4,6] , you can cut it to get a square with a side length of at most 4 . 
 
 Let maxLen be the side length of the largest square you can obtain from any of the given rectangles. 
 
 Return the number of rectangles that can make a square with a side length of maxLen . 

 Example 1: 
 
```
Input:
 rectangles = [[5,8],[3,9],[5,12],[16,5]]

Output:
 3

Explanation:
 The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.
```

 Example 2: 
 
```
Input:
 rectangles = [[2,3],[3,7],[4,3],[3,7]]

Output:
 3
```

 Constraints: 

 1 <= rectangles.length <= 1000 
 
 rectangles[i].length == 2 
 
 1 <= l i , w i <= 10 9 
 
 l i != w i

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        int maxLen = 0, count = 0;
        for (auto& r : rectangles) {
            int side = min(r[0], r[1]);
            if (side > maxLen) {
                maxLen = side;
                count = 1;
            } else if (side == maxLen) {
                count++;
            }
        }
        return count;
    }
};
```


## 1752. Check if Array Is Sorted and Rotated

**Problem:** https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One circular pass counts adjacent decreases, including the last-to-first comparison.

### Problem description

Given an array nums , return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero) . Otherwise, return false . 
 
 There may be duplicates in the original array. 
 
 Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i . 

 Example 1: 
 
```
Input:
 nums = [3,4,5,1,2]

Output:
 true

Explanation:
 [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
```

 Example 2: 
 
```
Input:
 nums = [2,1,3,4]

Output:
 false

Explanation:
 There is no sorted array once rotated that can make nums.
```

 Example 3: 
 
```
Input:
 nums = [1,2,3]

Output:
 true

Explanation:
 [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
```

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    bool check(vector<int>& nums) {
        int count = 0, n = nums.size();
        for (int i = 0; i < n; ++i)
            if (nums[i] > nums[(i + 1) % n])
                count++;
        return count <= 1;
    }
};
```


## 1779. Find Nearest Point That Has the Same X or Y Coordinate

**Problem:** https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(p)

**Space complexity:** O(1)

**Complexity reasoning:** Scans all p points once, maintaining the best Manhattan distance and index.

### Problem description

You are given two integers, x and y , which represent your current location on a Cartesian grid: (x, y) . You are also given an array points where each points[i] = [a i , b i ] represents that a point exists at (a i , b i ) . A point is valid if it shares the same x-coordinate or the same y-coordinate as your location. 
 
 Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location . If there are multiple, return the valid point with the smallest index . If there are no valid points, return -1 . 
 
 The Manhattan distance between two points (x 1 , y 1 ) and (x 2 , y 2 ) is abs(x 1 - x 2 ) + abs(y 1 - y 2 ) . 

 Example 1: 
 
```
Input:
 x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]

Output:
 2

Explanation:
 Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.
```

 Example 2: 
 
```
Input:
 x = 3, y = 4, points = [[3,4]]

Output:
 0

Explanation:
 The answer is allowed to be on the same location as your current location.
```

 Example 3: 
 
```
Input:
 x = 3, y = 4, points = [[2,3]]

Output:
 -1

Explanation:
 There are no valid points.
```

 Constraints: 

 1 <= points.length <= 10 4 
 
 points[i].length == 2 
 
 1 <= x, y, a i , b i <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int res = -1, minDist = INT_MAX;
        for (int i = 0; i < points.size(); ++i) {
            if (points[i][0] == x || points[i][1] == y) {
                int dist = abs(x - points[i][0]) + abs(y - points[i][1]);
                if (dist < minDist) {
                    minDist = dist;
                    res = i;
                }
            }
        }
        return res;
    }
};
```


## 1800. Maximum Ascending Subarray Sum

**Problem:** https://leetcode.com/problems/maximum-ascending-subarray-sum/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One pass updates the running ascending-subarray sum and maximum.

### Problem description

Given an array of positive integers nums , return the maximum possible sum of an strictly increasing subarray in nums . 
 
 A subarray is defined as a contiguous sequence of numbers in an array. 

 Example 1: 
 
```
Input:
 nums = [10,20,30,5,10,50]

Output:
 65

Explanation: 
[5,10,50] is the ascending subarray with the maximum sum of 65.
```

 Example 2: 
 
```
Input:
 nums = [10,20,30,40,50]

Output:
 150

Explanation: 
[10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
```

 Example 3: 
 
```
Input:
 nums = [12,17,15,13,10,11,12]

Output:
 33

Explanation: 
[10,11,12] is the ascending subarray with the maximum sum of 33.
```

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 int maxAscendingSum(vector<int>& nums){
  int cur=0,best=0;
  for(int i=0;i<(int)nums.size();++i){cur=(i && nums[i]>nums[i-1])?cur+nums[i]:nums[i];best=max(best,cur);}
  return best;
 }
};
```


## 1848. Minimum Distance to the Target Element

**Problem:** https://leetcode.com/problems/minimum-distance-to-the-target-element/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Checks every array element and retains the smallest matching index distance.

### Problem description

Given an integer array nums (0-indexed) and two integers target and start , find an index i such that nums[i] == target and abs(i - start) is minimized . Note that  abs(x)  is the absolute value of x . 
 
 Return abs(i - start) . 
 
 It is guaranteed that target exists in nums . 

 Example 1: 
 
```
Input:
 nums = [1,2,3,4,5], target = 5, start = 3

Output:
 1

Explanation:
 nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
```

 Example 2: 
 
```
Input:
 nums = [1], target = 1, start = 0

Output:
 0

Explanation:
 nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.
```

 Example 3: 
 
```
Input:
 nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0

Output:
 0

Explanation:
 Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.
```

 Constraints: 

 1 <= nums.length <= 1000 
 
 1 <= nums[i] <= 10 4 
 
 0 <= start < nums.length 
 
 target is in nums .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int getMinDistance(vector<int>& nums,int target,int start){int ans=nums.size();for(int i=0;i<(int)nums.size();++i)if(nums[i]==target)ans=min(ans,abs(i-start));return ans;}};
```


## 1886. Determine Whether Matrix Can Be Obtained By Rotation

**Problem:** https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(1)

**Complexity reasoning:** At most four full matrix comparisons and four in-place layer rotations; each takes O(n²) time.

### Problem description

Given two n x n binary matrices mat and target , return true if it is possible to make mat equal to target by rotating mat in 90-degree increments , or false otherwise. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/05/20/grid3.png] 
 
```
Input:
 mat = [[0,1],[1,0]], target = [[1,0],[0,1]]

Output:
 true

Explanation: 
We can rotate mat 90 degrees clockwise to make mat equal target.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/05/20/grid4.png] 
 
```
Input:
 mat = [[0,1],[1,1]], target = [[1,0],[0,1]]

Output:
 false

Explanation:
 It is impossible to make mat equal to target by rotating mat.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/05/26/grid4.png] 
 
```
Input:
 mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]

Output:
 true

Explanation: 
We can rotate mat 90 degrees clockwise two times to make mat equal target.
```

 Constraints: 

 n == mat.length == target.length 
 
 n == mat[i].length == target[i].length 
 
 1 <= n <= 10 
 
 mat[i][j] and target[i][j] are either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        for (int k = 0; k < 4; ++k) {
            if (mat == target) return true;
            rotate(mat);
        }
        return false;
    }

    void rotate(vector<vector<int>>& mat) {
        int n = mat.size();
        for (int i = 0; i < n / 2; ++i)
            for (int j = i; j < n - i - 1; ++j) {
                int tmp = mat[i][j];
                mat[i][j] = mat[n - j - 1][i];
                mat[n - j - 1][i] = mat[n - i - 1][n - j - 1];
                mat[n - i - 1][n - j - 1] = mat[j][n - i - 1];
                mat[j][n - i - 1] = tmp;
            }
    }
};
```


## 1909. Remove One Element to Make the Array Strictly Increasing

**Problem:** https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Finds the first violation, then checks at most two candidate removals with linear scans.

### Problem description

Given a 0-indexed integer array nums , return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true . 
 
 The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length). 

 Example 1: 
 
```
Input:
 nums = [1,2,
10
,5,7]

Output:
 true

Explanation:
 By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.
```

 Example 2: 
 
```
Input:
 nums = [2,3,1,2]

Output:
 false

Explanation:

[3,1,2] is the result of removing the element at index 0.
[2,1,2] is the result of removing the element at index 1.
[2,3,2] is the result of removing the element at index 2.
[2,3,1] is the result of removing the element at index 3.
No resulting array is strictly increasing, so return false.
```

 Example 3: 
 
```
Input:
 nums = [1,1,1]

Output:
 false

Explanation:
 The result of removing any element is [1,1].
[1,1] is not strictly increasing, so return false.
```

 Constraints: 

 2 <= nums.length <= 1000 
 
 1 <= nums[i] <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool canBeIncreasing(vector<int>& nums){int n=nums.size(),bad=-1;for(int i=1;i<n;++i)if(nums[i]<=nums[i-1]){bad=i;break;}if(bad==-1)return true;for(int skip:{bad-1,bad}){int prev=INT_MIN;bool ok=true;for(int i=0;i<n;++i)if(i!=skip){if(nums[i]<=prev){ok=false;break;}prev=nums[i];}if(ok)return true;}return false;}};
```


## 1914. Cyclically Rotating a Grid

**Problem:** https://leetcode.com/problems/cyclically-rotating-a-grid/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(m+n) auxiliary; O(mn) returned grid

**Complexity reasoning:** Each ring is enumerated, copied, and rotated once; the largest ring uses O(m+n) temporary storage. Returning the grid by value may copy O(mn) elements.

### Problem description

You are given an m x n integer matrix grid ​​​, where m and n are both even integers, and an integer k . 
 
 The matrix is composed of several layers, which is shown in the below image, where each color is its own layer: 
 
 [Figure: https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png] 
 
 A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below: 
 [Figure: https://assets.leetcode.com/uploads/2021/06/22/explanation_grid.jpg] 
 
 Return the matrix after applying k cyclic rotations to it . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/06/19/rod2.png] 
 
```
Input:
 grid = [[40,10],[30,20]], k = 1

Output:
 [[10,20],[40,30]]

Explanation:
 The figures above represent the grid at every state.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/06/10/ringofgrid5.png] [Figure: https://assets.leetcode.com/uploads/2021/06/10/ringofgrid6.png] [Figure: https://assets.leetcode.com/uploads/2021/06/10/ringofgrid7.png] 
 
```
Input:
 grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2

Output:
 [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]

Explanation:
 The figures above represent the grid at every state.
```

 Constraints: 

 m == grid.length 
 
 n == grid[i].length 
 
 2 <= m, n <= 50 
 
 Both m and n are even integers. 
 
 1 <= grid[i][j] <= 5000 
 
 1 <= k <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<vector<int>> rotateGrid(vector<vector<int>>& grid,int k){int m=grid.size(),n=grid[0].size();for(int layer=0;layer<min(m,n)/2;++layer){int top=layer,left=layer,bottom=m-1-layer,right=n-1-layer;vector<pair<int,int>> cells;for(int c=left;c<=right;++c)cells.push_back({top,c});for(int r=top+1;r<=bottom;++r)cells.push_back({r,right});for(int c=right-1;c>=left;--c)cells.push_back({bottom,c});for(int r=bottom-1;r>top;--r)cells.push_back({r,left});vector<int> v;for(auto p:cells)v.push_back(grid[p.first][p.second]);int len=v.size();for(int i=0;i<len;++i)grid[cells[i].first][cells[i].second]=v[(i+k%len)%len];}return grid;}};
```


## 1920. Build Array from Permutation

**Problem:** https://leetcode.com/problems/build-array-from-permutation/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Allocates an n-element result and performs one indexed lookup per element.

### Problem description

Given a zero-based permutation nums ( 0-indexed ), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it. 
 
 A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 ( inclusive ). 

 Example 1: 
 
```
Input:
 nums = [0,2,1,5,3,4]

Output:
 [0,1,2,4,5,3]

Explanation:
 The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
 = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
 = [0,1,2,4,5,3]
```

 Example 2: 
 
```
Input:
 nums = [5,0,1,2,3,4]

Output:
 [4,5,0,1,2,3]

Explanation:
 The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
 = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
 = [4,5,0,1,2,3]
```

 Constraints: 

 1 <= nums.length <= 1000 
 
 0 <= nums[i] < nums.length 
 
 The elements in nums are distinct . 

 Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);
        for (int i = 0; i < n; ++i) {
            res[i] = nums[nums[i]];
        }
        return res;
    }
};
```


## 1929. Concatenation of Array

**Problem:** https://leetcode.com/problems/concatenation-of-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Copies the original n elements and appends another n elements to the result.

### Problem description

Given an integer array nums of length n , you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n ( 0-indexed ). 
 
 Specifically, ans is the concatenation of two nums arrays. 
 
 Return the array ans . 

 Example 1: 
 
```
Input:
 nums = [1,2,1]

Output:
 [1,2,1,1,2,1]

Explanation:
 The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
```

 Example 2: 
 
```
Input:
 nums = [1,3,2,1]

Output:
 [1,3,2,1,1,3,2,1]

Explanation:
 The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
```

 Constraints: 

 n == nums.length 
 
 1 <= n <= 1000 
 
 1 <= nums[i] <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> res = nums;
        res.insert(res.end(), nums.begin(), nums.end());
        return res;
    }
};
```


## 1958. Check if Move is Legal

**Problem:** https://leetcode.com/problems/check-if-move-is-legal/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Checks eight directions on a fixed 8×8 board, traversing at most seven cells per direction.

### Problem description

You are given a 0-indexed 8 x 8 grid board , where board[r][c] represents the cell (r, c) on a game board. On the board, free cells are represented by '.' , white cells are represented by 'W' , and black cells are represented by 'B' . 
 
 Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal). 
 
 A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color , and the remaining cells in the middle are the opposite color (no cells in the line are free). You can find examples for good lines in the figure below: 
 [Figure: https://assets.leetcode.com/uploads/2021/07/22/goodlines5.png] 
 
 Given two integers rMove and cMove and a character color representing the color you are playing as (white or black), return true if changing cell (rMove, cMove) to color color is a legal move, or false if it is not legal . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/07/10/grid11.png] 
 
```
Input:
 board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"

Output:
 true

Explanation:
 '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'.
The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/07/10/grid2.png] 
 
```
Input:
 board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"

Output:
 false

Explanation:
 While there are good lines with the chosen cell as a middle cell, there are no good lines with the chosen cell as an endpoint.
```

 Constraints: 

 board.length == board[r].length == 8 
 
 0 <= rMove, cMove < 8 
 
 board[rMove][cMove] == '.' 
 
 color is either 'B' or 'W' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool checkMove(vector<vector<char>>& board,int rMove,int cMove,char color){int dr[]={-1,-1,-1,0,0,1,1,1},dc[]={-1,0,1,-1,1,-1,0,1};for(int k=0;k<8;++k){int r=rMove+dr[k],c=cMove+dc[k],cnt=0;while(r>=0&&c>=0&&r<8&&c<8&&board[r][c]!='.'){if(board[r][c]==color){if(cnt>0)return true;break;}++cnt;r+=dr[k];c+=dc[k];}}return false;}};
```


## 2012. Sum of Beauty in the Array

**Problem:** https://leetcode.com/problems/sum-of-beauty-in-the-array/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Builds a suffix-minimum array in one pass and scans once with a running prefix maximum.

### Problem description

You are given a 0-indexed integer array nums . For each index i ( 1 <= i <= nums.length - 2 ) the beauty of nums[i] equals: 

 2 , if nums[j] < nums[i] < nums[k] , for all 0 <= j < i and for all i < k <= nums.length - 1 . 
 
 1 , if nums[i - 1] < nums[i] < nums[i + 1] , and the previous condition is not satisfied. 
 
 0 , if none of the previous conditions holds. 

 Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2 . 

 Example 1: 
 
```
Input:
 nums = [1,2,3]

Output:
 2

Explanation:
 For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.
```

 Example 2: 
 
```
Input:
 nums = [2,4,6,4]

Output:
 1

Explanation:
 For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.
```

 Example 3: 
 
```
Input:
 nums = [3,2,1]

Output:
 0

Explanation:
 For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.
```

 Constraints: 

 3 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int sumOfBeauties(vector<int>& nums) {
        int n = nums.size();
        vector<int> rightMin(n);
        rightMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i)
            rightMin[i] = min(nums[i], rightMin[i + 1]);

        int leftMax = nums[0], res = 0;
        for (int i = 1; i < n - 1; ++i) {
            if (leftMax < nums[i] && nums[i] < rightMin[i + 1])
                res += 2;
            else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1])
                res += 1;
            leftMax = max(leftMax, nums[i]);
        }
        return res;
    }
};
```


## 2016. Maximum Difference Between Increasing Elements

**Problem:** https://leetcode.com/problems/maximum-difference-between-increasing-elements/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One pass tracks the minimum previously seen value and best positive difference.

### Problem description

Given a 0-indexed integer array nums of size n , find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i] ), such that 0 <= i < j < n and nums[i] < nums[j] . 
 
 Return the maximum difference . If no such i and j exists, return -1 . 

 Example 1: 
 
```
Input:
 nums = [7,
1
,
5
,4]

Output:
 4

Explanation:

The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
```

 Example 2: 
 
```
Input:
 nums = [9,4,3,2]

Output:
 -1

Explanation:

There is no i and j such that i < j and nums[i] < nums[j].
```

 Example 3: 
 
```
Input:
 nums = [
1
,5,2,
10
]

Output:
 9

Explanation:

The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
```

 Constraints: 

 n == nums.length 
 
 2 <= n <= 1000 
 
 1 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int minVal = nums[0], res = -1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] > minVal)
                res = max(res, nums[i] - minVal);
            minVal = min(minVal, nums[i]);
        }
        return res;
    }
};
```


## 2018. Check if Word Can Be Placed In Crossword

**Problem:** https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(m) auxiliary plus O(L) word copy

**Complexity reasoning:** Scans row segments and builds each column into a temporary m-character vector; matching all segments examines at most O(mn) cells. The word parameter is copied by value (L characters).

### Problem description

You are given an m x n matrix board , representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells. 
 
 A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if: 

 It does not occupy a cell containing the character '#' . 
 
 The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board . 
 
 There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally . 
 
 There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically . 

 Given a string word , return true if word can be placed in board , or false otherwise . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/04/crossword-ex1-1.png] 
 
```
Input:
 board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"

Output:
 true

Explanation:
 The word "abc" can be placed as shown above (top to bottom).
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/04/crossword-ex2-1.png] 
 
```
Input:
 board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"

Output:
 false

Explanation:
 It is impossible to place the word because there will always be a space/letter above or below it.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/04/crossword-ex3-1.png] 
 
```
Input:
 board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"

Output:
 true

Explanation:
 The word "ca" can be placed as shown above (right to left).
```

 Constraints: 

 m == board.length 
 
 n == board[i].length 
 
 1 <= m * n <= 2 * 10 5 
 
 board[i][j] will be ' ' , '#' , or a lowercase English letter. 
 
 1 <= word.length <= max(m, n) 
 
 word will contain only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool placeWordInCrossword(vector<vector<char>>& board,string word){
        int m=board.size(),n=board[0].size(),L=word.size();
        auto fits=[&](const vector<char>&line,int start,int end){
            if(end-start!=L)return false;
            bool f=true,b=true;
            for(int i=0;i<L;++i){char c=line[start+i];
                if(c!=' '&&c!=word[i])f=false;
                if(c!=' '&&c!=word[L-1-i])b=false;
            }
            return f||b;
        };
        for(int r=0;r<m;++r){int st=0;
            for(int c=0;c<=n;++c)if(c==n||board[r][c]=='#'){
                if(fits(board[r],st,c))return true;st=c+1;
            }
        }
        for(int c=0;c<n;++c){vector<char>line;
            for(int r=0;r<m;++r)line.push_back(board[r][c]);
            int st=0;for(int r=0;r<=m;++r)if(r==m||line[r]=='#'){
                if(fits(line,st,r))return true;st=r+1;
            }
        }
        return false;
    }
};
```


## 2022. Convert 1D Array Into 2D Array

**Problem:** https://leetcode.com/problems/convert-1d-array-into-2d-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn)

**Complexity reasoning:** Allocates and fills an m-by-n output matrix when the input length matches.

### Problem description

You are given a 0-indexed 1-dimensional (1D) integer array original , and two integers, m and n . You are tasked with creating a 2-dimensional (2D) array with m rows and n columns using all the elements from original . 
 
 The elements from indices 0 to n - 1 ( inclusive ) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 ( inclusive ) should form the second row of the constructed 2D array, and so on. 
 
 Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/08/26/image-20210826114243-1.png] 
 
```
Input:
 original = [1,2,3,4], m = 2, n = 2

Output:
 [[1,2],[3,4]]

Explanation:
 The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
```

 Example 2: 
 
```
Input:
 original = [1,2,3], m = 1, n = 3

Output:
 [[1,2,3]]

Explanation:
 The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.
```

 Example 3: 
 
```
Input:
 original = [1,2], m = 1, n = 1

Output:
 []

Explanation:
 There are 2 elements in original.
It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.
```

 Constraints: 

 1 <= original.length <= 5 * 10 4 
 
 1 <= original[i] <= 10 5 
 
 1 <= m, n <= 4 * 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original,int m,int n){
        if(1LL*m*n!=(int)original.size())return {};
        vector<vector<int>>ans(m,vector<int>(n));
        for(int i=0;i<m*n;++i)ans[i/n][i%n]=original[i];return ans;
    }
};
```


## 2057. Smallest Index With Equal Value

**Problem:** https://leetcode.com/problems/smallest-index-with-equal-value/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Checks each index against its value modulo ten until a match is found.

### Problem description

Given a 0-indexed integer array nums , return the smallest index i of nums such that i mod 10 == nums[i] , or -1 if such index does not exist . 
 
 x mod y denotes the remainder when x is divided by y . 

 Example 1: 
 
```
Input:
 nums = [0,1,2]

Output:
 0

Explanation:
 
i=0: 0 mod 10 = 0 == nums[0].
i=1: 1 mod 10 = 1 == nums[1].
i=2: 2 mod 10 = 2 == nums[2].
All indices have i mod 10 == nums[i], so we return the smallest index 0.
```

 Example 2: 
 
```
Input:
 nums = [4,3,2,1]

Output:
 2

Explanation:
 
i=0: 0 mod 10 = 0 != nums[0].
i=1: 1 mod 10 = 1 != nums[1].
i=2: 2 mod 10 = 2 == nums[2].
i=3: 3 mod 10 = 3 != nums[3].
2 is the only index which has i mod 10 == nums[i].
```

 Example 3: 
 
```
Input:
 nums = [1,2,3,4,5,6,7,8,9,0]

Output:
 -1

Explanation:
 No index satisfies i mod 10 == nums[i].
```

 Constraints: 

 1 <= nums.length <= 100 
 
 0 <= nums[i] <= 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int smallestEqual(vector<int>& nums){
        for(int i=0;i<(int)nums.size();++i)if(i%10==nums[i])return i;
        return -1;
    }
};
```


## 2061. Number of Spaces Cleaning Robot Cleaned

**Problem:** https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn)

**Complexity reasoning:** Stores a four-direction visited-state mask per cell; each (cell, direction) state is processed at most once.

### Problem description

A room is represented by a 0-indexed 2D binary matrix room where a 0 represents an empty space and a 1 represents a space with an object . The top left corner of the room will be empty in all test cases. 
 
 A cleaning robot starts at the top left corner of the room and is facing right. The robot will continue heading straight until it reaches the edge of the room or it hits an object, after which it will turn 90 degrees clockwise and repeat this process. The starting space and all spaces that the robot visits are cleaned by it. 
 
 Return the number of clean spaces in the room if the robot runs indefinitely. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/11/01/image-20211101204703-1.png] 

 Input: room = [[0,0,0],[1,1,0],[0,0,0]] 
 
 Output: 7 
 
 Explanation: 

 ​​​​​​​The robot cleans the spaces at (0, 0), (0, 1), and (0, 2). 
 
 The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces down. 
 
 The robot cleans the spaces at (1, 2), and (2, 2). 
 
 The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces left. 
 
 The robot cleans the spaces at (2, 1), and (2, 0). 
 
 The robot has cleaned all 7 empty spaces, so return 7. 

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/11/01/image-20211101204736-2.png] 

 Input: room = [[0,1,0],[1,0,0],[0,0,0]] 
 
 Output: 1 
 
 Explanation: 

 The robot cleans the space at (0, 0). 
 
 The robot hits an object, so it turns 90 degrees clockwise and now faces down. 
 
 The robot hits an object, so it turns 90 degrees clockwise and now faces left. 
 
 The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces up. 
 
 The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces right. 
 
 The robot is back at its starting position. 
 
 The robot has cleaned 1 space, so return 1. 

 Example 3: 

 Input: room = [[0,0,0],[0,0,0],[0,0,0]] 
 
 Output: 8 ​​​​​​​ 

 Constraints: 

 m == room.length 
 
 n == room[r].length 
 
 1 <= m, n <= 300 
 
 room[r][c] is either 0 or 1 . 
 
 room[0][0] == 0

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int numberOfCleanRooms(vector<vector<int>>& room) {
        int m = room.size(), n = room[0].size();
        int dr[4] = {0, 1, 0, -1};
        int dc[4] = {1, 0, -1, 0};
        vector<vector<int>> seen(m, vector<int>(n, 0));
        int r = 0, c = 0, d = 0, answer = 0;
        while (!(seen[r][c] & (1 << d))) {
            if (seen[r][c] == 0) ++answer;
            seen[r][c] |= 1 << d;
            int nr = r + dr[d], nc = c + dc[d];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || room[nr][nc] == 1) {
                d = (d + 1) % 4;
            } else {
                r = nr;
                c = nc;
            }
        }
        return answer;
    }
};
```


## 2079. Watering Plants

**Problem:** https://leetcode.com/problems/watering-plants/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Processes each plant once, accounting arithmetically for any refill trip.

### Problem description

You want to water n plants in your garden with a watering can. The plants are arranged in a row and are labeled from 0 to n - 1 from left to right where the i th plant is located at x = i . There is a river at x = -1 that you can refill your watering can at. 
 
 Each plant needs a specific amount of water. You will water the plants in the following way: 

 Water the plants in order from left to right. 
 
 After watering the current plant, if you do not have enough water to completely water the next plant, return to the river to fully refill the watering can. 
 
 You cannot refill the watering can early. 

 You are initially at the river (i.e., x = -1 ). It takes one step to move one unit on the x-axis. 
 
 Given a 0-indexed integer array plants of n integers, where plants[i] is the amount of water the i th plant needs, and an integer capacity representing the watering can capacity, return the number of steps needed to water all the plants . 

 Example 1: 
 
```
Input:
 plants = [2,2,3,3], capacity = 5

Output:
 14

Explanation:
 Start at the river with a full watering can:
- Walk to plant 0 (1 step) and water it. Watering can has 3 units of water.
- Walk to plant 1 (1 step) and water it. Watering can has 1 unit of water.
- Since you cannot completely water plant 2, walk back to the river to refill (2 steps).
- Walk to plant 2 (3 steps) and water it. Watering can has 2 units of water.
- Since you cannot completely water plant 3, walk back to the river to refill (3 steps).
- Walk to plant 3 (4 steps) and water it.
Steps needed = 1 + 1 + 2 + 3 + 3 + 4 = 14.
```

 Example 2: 
 
```
Input:
 plants = [1,1,1,4,2,3], capacity = 4

Output:
 30

Explanation:
 Start at the river with a full watering can:
- Water plants 0, 1, and 2 (3 steps). Return to river (3 steps).
- Water plant 3 (4 steps). Return to river (4 steps).
- Water plant 4 (5 steps). Return to river (5 steps).
- Water plant 5 (6 steps).
Steps needed = 3 + 3 + 4 + 4 + 5 + 5 + 6 = 30.
```

 Example 3: 
 
```
Input:
 plants = [7,7,7,7,7,7,7], capacity = 8

Output:
 49

Explanation:
 You have to refill before watering each plant.
Steps needed = 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5 + 6 + 6 + 7 = 49.
```

 Constraints: 

 n == plants.length 
 
 1 <= n <= 1000 
 
 1 <= plants[i] <= 10 6 
 
 max(plants[i]) <= capacity <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int steps = 0, curr = capacity;
        for (int i = 0; i < plants.size(); ++i) {
            if (curr < plants[i]) {
                steps += 2 * i;
                curr = capacity;
            }
            curr -= plants[i];
            steps++;
        }
        return steps;
    }
};
```


## 2113. Elements in Array After Removing and Replacing Elements

**Problem:** https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(q)

**Space complexity:** O(q)

**Complexity reasoning:** Answers each of q queries in constant time using modular arithmetic and appends one result.

### Problem description

You are given a 0-indexed integer array nums . Initially on minute 0 , the array is unchanged. Every minute, the leftmost element in nums is removed until no elements remain. Then, every minute, one element is appended to the end of nums , in the order they were removed in, until the original array is restored. This process repeats indefinitely. 

 For example, the array [0,1,2] would change as follows: [0,1,2] → [1,2] → [2] → [] → [0] → [0,1] → [0,1,2] → [1,2] → [2] → [] → [0] → [0,1] → [0,1,2] → ... 

 You are also given a 2D integer array queries of size n where queries[j] = [time j , index j ] . The answer to the j th query is: 

 nums[index j ] if index j < nums.length at minute time j 
 
 -1 if index j >= nums.length at minute time j 

 Return an integer array ans of size n where ans[j] is the answer to the j th query . 

 Example 1: 
 
```
Input:
 nums = [0,1,2], queries = [[0,2],[2,0],[3,2],[5,0]]

Output:
 [2,2,-1,0]

Explanation:

Minute 0: [0,1,2] - All elements are in the nums.
Minute 1: [1,2] - The leftmost element, 0, is removed.
Minute 2: [2] - The leftmost element, 1, is removed.
Minute 3: [] - The leftmost element, 2, is removed.
Minute 4: [0] - 0 is added to the end of nums.
Minute 5: [0,1] - 1 is added to the end of nums.

At minute 0, nums[2] is 2.
At minute 2, nums[0] is 2.
At minute 3, nums[2] does not exist.
At minute 5, nums[0] is 0.
```

 Example 2: 
 
```
Input:
 nums = [2], queries = [[0,0],[1,0],[2,0],[3,0]]

Output:
 [2,-1,2,-1]
Minute 0: [2] - All elements are in the nums.
Minute 1: [] - The leftmost element, 2, is removed.
Minute 2: [2] - 2 is added to the end of nums.
Minute 3: [] - The leftmost element, 2, is removed.

At minute 0, nums[0] is 2.
At minute 1, nums[0] does not exist.
At minute 2, nums[0] is 2.
At minute 3, nums[0] does not exist.
```

 Constraints: 

 1 <= nums.length <= 100 
 
 0 <= nums[i] <= 100 
 
 n == queries.length 
 
 1 <= n <= 10 5 
 
 queries[j].length == 2 
 
 0 <= time j <= 10 5 
 
 0 <= index j < nums.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> elementInNums(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> answer;
        for (const auto& q : queries) {
            int time = q[0] % (2 * n);
            int length = time < n ? n - time : time - n;
            int offset = time < n ? time : 0;
            answer.push_back(q[1] < length ? nums[offset + q[1]] : -1);
        }
        return answer;
    }
};
```


## 2155. All Divisions With the Highest Score of a Binary Array

**Problem:** https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output; O(1) auxiliary

**Complexity reasoning:** Computes the initial score once and evaluates n+1 division points, recording all best indices.

### Problem description

You are given a 0-indexed binary array nums of length n . nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty) nums left and nums right : 

 nums left has all the elements of nums between index 0 and i - 1 (inclusive) , while nums right has all the elements of nums between index i and n - 1 (inclusive) . 
 
 If i == 0 , nums left is empty , while nums right has all the elements of nums . 
 
 If i == n , nums left has all the elements of nums, while nums right is empty . 

 The division score of an index i is the sum of the number of 0 's in nums left and the number of 1 's in nums right . 
 
 Return all distinct indices that have the highest possible division score . You may return the answer in any order . 

 Example 1: 
 
```
Input:
 nums = [0,0,1,0]

Output:
 [2,4]

Explanation:
 Division at index
- 0: nums
left
 is []. nums
right
 is [0,0,
1
,0]. The score is 0 + 1 = 1.
- 1: nums
left
 is [
0
]. nums
right
 is [0,
1
,0]. The score is 1 + 1 = 2.
- 2: nums
left
 is [
0
,
0
]. nums
right
 is [
1
,0]. The score is 2 + 1 = 3.
- 3: nums
left
 is [
0
,
0
,1]. nums
right
 is [0]. The score is 2 + 0 = 2.
- 4: nums
left
 is [
0
,
0
,1,
0
]. nums
right
 is []. The score is 3 + 0 = 3.
Indices 2 and 4 both have the highest possible division score 3.
Note the answer [4,2] would also be accepted.
```

 Example 2: 
 
```
Input:
 nums = [0,0,0]

Output:
 [3]

Explanation:
 Division at index
- 0: nums
left
 is []. nums
right
 is [0,0,0]. The score is 0 + 0 = 0.
- 1: nums
left
 is [
0
]. nums
right
 is [0,0]. The score is 1 + 0 = 1.
- 2: nums
left
 is [
0
,
0
]. nums
right
 is [0]. The score is 2 + 0 = 2.
- 3: nums
left
 is [
0
,
0
,
0
]. nums
right
 is []. The score is 3 + 0 = 3.
Only index 3 has the highest possible division score 3.
```

 Example 3: 
 
```
Input:
 nums = [1,1]

Output:
 [0]

Explanation:
 Division at index
- 0: nums
left
 is []. nums
right
 is [
1
,
1
]. The score is 0 + 2 = 2.
- 1: nums
left
 is [1]. nums
right
 is [
1
]. The score is 0 + 1 = 1.
- 2: nums
left
 is [1,1]. nums
right
 is []. The score is 0 + 0 = 0.
Only index 0 has the highest possible division score 2.
```

 Constraints: 

 n == nums.length 
 
 1 <= n <= 10 5 
 
 nums[i] is either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> maxScoreIndices(vector<int>& nums) {
        int score=accumulate(nums.begin(),nums.end(),0),best=-1;
        vector<int> ans;
        for(int i=0;i<=(int)nums.size();++i) {
            if(score>best) {best=score;ans.clear();}
            if(score==best) ans.push_back(i);
            if(i<(int)nums.size()) score+=(nums[i]==0?1:-1);
        }
        return ans;
    }
};
```


## 2176. Count Equal and Divisible Pairs in an Array

**Problem:** https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(1)

**Complexity reasoning:** Two nested loops test every distinct index pair.

### Problem description

Given a 0-indexed integer array nums of length n and an integer k , return the number of pairs (i, j) where 0 <= i < j < n , such that nums[i] == nums[j] and (i * j) is divisible by k .

 Example 1: 
 
```
Input:
 nums = [3,1,2,2,2,1,3], k = 2

Output:
 4

Explanation:

There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
```

 Example 2: 
 
```
Input:
 nums = [1,2,3,4], k = 1

Output:
 0

Explanation:
 Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.
```

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i], k <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        int ans=0;
        for(int i=0;i<(int)nums.size();++i)
            for(int j=i+1;j<(int)nums.size();++j)
                if(nums[i]==nums[j]&&(i*j)%k==0) ++ans;
        return ans;
    }
};
```


## 2210. Count Hills and Valleys in an Array

**Problem:** https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Compresses consecutive equal values into a vector and checks each interior value once.

### Problem description

You are given a 0-indexed integer array nums . An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i] . Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i] . Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j] . 
 
 Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index. 
 
 Return the number of hills and valleys in nums . 

 Example 1: 
 
```
Input:
 nums = [2,4,1,1,6,5]

Output:
 3

Explanation:

At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a valley.
At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a hill. 
At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a valley.
At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a valley, but note that it is part of the same valley as index 2.
At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a hill.
At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a valley. 
There are 3 hills and valleys so we return 3.
```

 Example 2: 
 
```
Input:
 nums = [6,6,5,5,4,1]

Output:
 0

Explanation:

At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill nor a valley.
At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill nor a valley.
At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 2 is neither a hill nor a valley.
At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 3 is neither a hill nor a valley.
At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index 4 is neither a hill nor a valley.
At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill nor a valley.
There are 0 hills and valleys so we return 0.
```

 Constraints: 

 3 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 int countHillValley(vector<int>& nums){vector<int>a;for(int x:nums)if(a.empty()||a.back()!=x)a.push_back(x);int ans=0;
  for(int i=1;i+1<(int)a.size();++i)if((a[i]>a[i-1]&&a[i]>a[i+1])||(a[i]<a[i-1]&&a[i]<a[i+1]))++ans;return ans;
 }
};
```


## 2239. Find Closest Number to Zero

**Problem:** https://leetcode.com/problems/find-closest-number-to-zero/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One scan tracks the value closest to zero, preferring positive values on ties.

### Problem description

Given an integer array nums of size n , return the number with the value closest to 0 in nums . If there are multiple answers, return the number with the largest value . 

 Example 1: 
 
```
Input:
 nums = [-4,-2,1,4,8]

Output:
 1

Explanation:

The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
```

 Example 2: 
 
```
Input:
 nums = [2,-1,1]

Output:
 1

Explanation:
 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
```

 Constraints: 

 1 <= n <= 1000 
 
 -10 5 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 int findClosestNumber(vector<int>& nums){int ans=nums[0];for(int x:nums)if(abs(x)<abs(ans)||(abs(x)==abs(ans)&&x>ans))ans=x;return ans;}
};
```


## 2257. Count Unguarded Cells in the Grid

**Problem:** https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn + g + w)

**Space complexity:** O(mn)

**Complexity reasoning:** Marks g guards and w walls, sweeps every row and column in both directions, and counts unguarded cells.

### Problem description

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [row i , col i ] and walls[j] = [row j , col j ] represent the positions of the i th guard and j th wall respectively. 
 
 A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it. 
 
 Return the number of unoccupied cells that are not guarded . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/03/10/example1drawio2.png] 
 
```
Input:
 m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]

Output:
 7

Explanation:
 The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/03/10/example2drawio.png] 
 
```
Input:
 m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]

Output:
 4

Explanation:
 The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
```

 Constraints: 

 1 <= m, n <= 10 5 
 
 2 <= m * n <= 10 5 
 
 1 <= guards.length, walls.length <= 5 * 10 4 
 
 2 <= guards.length + walls.length <= m * n 
 
 guards[i].length == walls[j].length == 2 
 
 0 <= row i , row j < m 
 
 0 <= col i , col j < n 
 
 All the positions in guards and walls are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {public:int countUnguarded(int m,int n,vector<vector<int>>& guards,vector<vector<int>>& walls){vector<vector<int>> a(m,vector<int>(n));for(auto &p:guards)a[p[0]][p[1]]=1;for(auto &p:walls)a[p[0]][p[1]]=2;vector<vector<bool>> seen(m,vector<bool>(n));for(int i=0;i<m;++i){bool on=false;for(int j=0;j<n;++j){if(a[i][j])on=a[i][j]==1;else if(on)seen[i][j]=true;}on=false;for(int j=n-1;j>=0;--j){if(a[i][j])on=a[i][j]==1;else if(on)seen[i][j]=true;}}for(int j=0;j<n;++j){bool on=false;for(int i=0;i<m;++i){if(a[i][j])on=a[i][j]==1;else if(on)seen[i][j]=true;}on=false;for(int i=m-1;i>=0;--i){if(a[i][j])on=a[i][j]==1;else if(on)seen[i][j]=true;}}int ans=0;for(int i=0;i<m;++i)for(int j=0;j<n;++j)if(!a[i][j]&&!seen[i][j])++ans;return ans;} };
```


## 2293. Min Max Game

**Problem:** https://leetcode.com/problems/min-max-game/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Repeated in-place rounds process n/2 + n/4 + ... elements, a geometric sum bounded by O(n).

### Problem description

You are given a 0-indexed integer array nums whose length is a power of 2 . 
 
 Apply the following algorithm on nums : 

 Let n be the length of nums . If n == 1 , end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2 . 
 
 For every even index i where 0 <= i < n / 2 , assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]) . 
 
 For every odd index i where 0 <= i < n / 2 , assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]) . 
 
 Replace the array nums with newNums . 
 
 Repeat the entire process starting from step 1. 

 Return the last number that remains in nums after applying the algorithm. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/04/13/example1drawio-1.png] 
 
```
Input:
 nums = [1,3,5,2,4,8,2,2]

Output:
 1

Explanation:
 The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.
```

 Example 2: 
 
```
Input:
 nums = [3]

Output:
 3

Explanation:
 3 is already the last remaining number, so we return 3.
```

 Constraints: 

 1 <= nums.length <= 1024 
 
 1 <= nums[i] <= 10 9 
 
 nums.length is a power of 2 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:int minMaxGame(vector<int>& nums){int n=nums.size();while(n>1){for(int i=0;i<n/2;++i)nums[i]=i%2?max(nums[2*i],nums[2*i+1]):min(nums[2*i],nums[2*i+1]);n/=2;}return nums[0];}};
```


## 2303. Calculate Amount Paid in Taxes

**Problem:** https://leetcode.com/problems/calculate-amount-paid-in-taxes/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(b)

**Space complexity:** O(1)

**Complexity reasoning:** Visits at most b tax brackets, calculating the taxable portion for each.

### Problem description

You are given a 0-indexed 2D integer array brackets where brackets[i] = [upper i , percent i ] means that the i th tax bracket has an upper bound of upper i and is taxed at a rate of percent i . The brackets are sorted by upper bound (i.e. upper i-1 < upper i for 0 < i < brackets.length ). 
 
 Tax is calculated as follows: 

 The first upper 0 dollars earned are taxed at a rate of percent 0 . 
 
 The next upper 1 - upper 0 dollars earned are taxed at a rate of percent 1 . 
 
 The next upper 2 - upper 1 dollars earned are taxed at a rate of percent 2 . 
 
 And so on. 

 You are given an integer income representing the amount of money you earned. Return the amount of money that you have to pay in taxes. Answers within 10 -5 of the actual answer will be accepted. 

 Example 1: 
 
```
Input:
 brackets = [[3,50],[7,10],[12,25]], income = 10

Output:
 2.65000

Explanation:

Based on your income, you have 3 dollars in the 1
st
 tax bracket, 4 dollars in the 2
nd
 tax bracket, and 3 dollars in the 3
rd
 tax bracket.
The tax rate for the three tax brackets is 50%, 10%, and 25%, respectively.
In total, you pay $3 * 50% + $4 * 10% + $3 * 25% = $2.65 in taxes.
```

 Example 2: 
 
```
Input:
 brackets = [[1,0],[4,25],[5,50]], income = 2

Output:
 0.25000

Explanation:

Based on your income, you have 1 dollar in the 1
st
 tax bracket and 1 dollar in the 2
nd
 tax bracket.
The tax rate for the two tax brackets is 0% and 25%, respectively.
In total, you pay $1 * 0% + $1 * 25% = $0.25 in taxes.
```

 Example 3: 
 
```
Input:
 brackets = [[2,50]], income = 0

Output:
 0.00000

Explanation:

You have no income to tax, so you have to pay a total of $0 in taxes.
```

 Constraints: 

 1 <= brackets.length <= 100 
 
 1 <= upper i <= 1000 
 
 0 <= percent i <= 100 
 
 0 <= income <= 1000 
 
 upper i is sorted in ascending order. 
 
 All the values of upper i are unique . 
 
 The upper bound of the last tax bracket is greater than or equal to income .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:double calculateTax(vector<vector<int>>& brackets,int income){int prev=0;double ans=0;for(auto& b:brackets){int take=max(0,min(income,b[0])-prev);ans+=take*b[1]/100.0;prev=b[0];if(income<=prev)break;}return ans;}};
```


## 2319. Check if Matrix Is X-Matrix

**Problem:** https://leetcode.com/problems/check-if-matrix-is-x-matrix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(1)

**Complexity reasoning:** Checks each cell against the main- or anti-diagonal requirement.

### Problem description

A square matrix is said to be an X-Matrix if both of the following conditions hold: 

 All the elements in the diagonals of the matrix are non-zero . 
 
 All other elements are 0. 

 Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix . Otherwise, return false . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/05/03/ex1.jpg] 
 
```
Input:
 grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]

Output:
 true

Explanation:
 Refer to the diagram above. 
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is an X-Matrix.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/05/03/ex2.jpg] 
 
```
Input:
 grid = [[5,7,0],[0,3,1],[0,5,0]]

Output:
 false

Explanation:
 Refer to the diagram above.
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is not an X-Matrix.
```

 Constraints: 

 n == grid.length == grid[i].length 
 
 3 <= n <= 100 
 
 0 <= grid[i][j] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:bool checkXMatrix(vector<vector<int>>& grid){int n=grid.size();for(int i=0;i<n;++i)for(int j=0;j<n;++j){bool diag=i==j||i+j==n-1;if(diag?(grid[i][j]==0):(grid[i][j]!=0))return false;}return true;}};
```


## 2373. Largest Local Values in a Matrix

**Problem:** https://leetcode.com/problems/largest-local-values-in-a-matrix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(n²)

**Complexity reasoning:** Evaluates every (n−2)×(n−2) window using nine constant-time comparisons and stores the result matrix.

### Problem description

You are given an n x n integer matrix grid . 
 
 Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that: 

 maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1 . 

 In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid . 
 
 Return the generated matrix . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/06/21/ex1.png] 
 
```
Input:
 grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]

Output:
 [[9,9],[8,6]]

Explanation:
 The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/07/02/ex2new2.png] 
 
```
Input:
 grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]

Output:
 [[2,2,2],[2,2,2],[2,2,2]]

Explanation:
 Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.
```

 Constraints: 

 n == grid.length == grid[i].length 
 
 3 <= n <= 100 
 
 1 <= grid[i][j] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n=grid.size();vector<vector<int>> ans(n-2,vector<int>(n-2));
        for(int i=0;i<n-2;++i)for(int j=0;j<n-2;++j){
            int mx=INT_MIN;for(int a=i;a<i+3;++a)for(int b=j;b<j+3;++b)mx=max(mx,grid[a][b]);
            ans[i][j]=mx;
        }
        return ans;
    }
};
```


## 2432. The Employee That Worked on the Longest Task

**Problem:** https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(l)

**Space complexity:** O(1)

**Complexity reasoning:** Scans l log entries, computing task durations and tie-breaking by employee ID.

### Problem description

There are n employees, each with a unique id from 0 to n - 1 . 
 
 You are given a 2D integer array logs where logs[i] = [id i , leaveTime i ] where: 

 id i is the id of the employee that worked on the i th task, and 
 
 leaveTime i is the time at which the employee finished the i th task. All the values leaveTime i are unique . 

 Note that the i th task starts the moment right after the (i - 1) th task ends, and the 0 th task starts at time 0 . 
 
 Return the id of the employee that worked the task with the longest time. If there is a tie between two or more employees, return the smallest id among them . 

 Example 1: 
 
```
Input:
 n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]

Output:
 1

Explanation:
 
Task 0 started at 0 and ended at 3 with 3 units of times.
Task 1 started at 3 and ended at 5 with 2 units of times.
Task 2 started at 5 and ended at 9 with 4 units of times.
Task 3 started at 9 and ended at 15 with 6 units of times.
The task with the longest time is task 3 and the employee with id 1 is the one that worked on it, so we return 1.
```

 Example 2: 
 
```
Input:
 n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]

Output:
 3

Explanation:
 
Task 0 started at 0 and ended at 1 with 1 unit of times.
Task 1 started at 1 and ended at 7 with 6 units of times.
Task 2 started at 7 and ended at 12 with 5 units of times.
Task 3 started at 12 and ended at 17 with 5 units of times.
The tasks with the longest time is task 1. The employee that worked on it is 3, so we return 3.
```

 Example 3: 
 
```
Input:
 n = 2, logs = [[0,10],[1,20]]

Output:
 0

Explanation:
 
Task 0 started at 0 and ended at 10 with 10 units of times.
Task 1 started at 10 and ended at 20 with 10 units of times.
The tasks with the longest time are tasks 0 and 1. The employees that worked on them are 0 and 1, so we return the smallest id 0.
```

 Constraints: 

 2 <= n <= 500 
 
 1 <= logs.length <= 500 
 
 logs[i].length == 2 
 
 0 <= id i <= n - 1 
 
 1 <= leaveTime i <= 500 
 
 id i != id i+1 
 
 leaveTime i are sorted in a strictly increasing order.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int hardestWorker(int n, vector<vector<int>>& logs) { int prev=0,best=-1,id=n; for(auto &x:logs){int d=x[1]-prev; if(d>best || (d==best && x[0]<id)){best=d;id=x[0];}prev=x[1];}return id;} };
```


## 2482. Difference Between Ones and Zeros in Row and Column

**Problem:** https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn)

**Complexity reasoning:** Counts ones in each row and column, then fills an m-by-n answer matrix.

### Problem description

You are given a 0-indexed m x n binary matrix grid . 
 
 A 0-indexed m x n difference matrix diff is created with the following procedure: 

 Let the number of ones in the i th row be onesRow i . 
 
 Let the number of ones in the j th column be onesCol j . 
 
 Let the number of zeros in the i th row be zerosRow i . 
 
 Let the number of zeros in the j th column be zerosCol j . 
 
 diff[i][j] = onesRow i + onesCol j - zerosRow i - zerosCol j 

 Return the difference matrix diff . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/11/06/image-20221106171729-5.png] 
 
```
Input:
 grid = [[0,1,1],[1,0,1],[0,0,1]]

Output:
 [[0,0,4],[0,0,4],[-2,-2,2]]

Explanation:

- diff[0][0] = 
onesRow
0
 + onesCol
0
 - zerosRow
0
 - zerosCol
0
 = 2 + 1 - 1 - 2 = 0 
- diff[0][1] = 
onesRow
0
 + onesCol
1
 - zerosRow
0
 - zerosCol
1
 = 2 + 1 - 1 - 2 = 0 
- diff[0][2] = 
onesRow
0
 + onesCol
2
 - zerosRow
0
 - zerosCol
2
 = 2 + 3 - 1 - 0 = 4 
- diff[1][0] = 
onesRow
1
 + onesCol
0
 - zerosRow
1
 - zerosCol
0
 = 2 + 1 - 1 - 2 = 0 
- diff[1][1] = 
onesRow
1
 + onesCol
1
 - zerosRow
1
 - zerosCol
1
 = 2 + 1 - 1 - 2 = 0 
- diff[1][2] = 
onesRow
1
 + onesCol
2
 - zerosRow
1
 - zerosCol
2
 = 2 + 3 - 1 - 0 = 4 
- diff[2][0] = 
onesRow
2
 + onesCol
0
 - zerosRow
2
 - zerosCol
0
 = 1 + 1 - 2 - 2 = -2
- diff[2][1] = 
onesRow
2
 + onesCol
1
 - zerosRow
2
 - zerosCol
1
 = 1 + 1 - 2 - 2 = -2
- diff[2][2] = 
onesRow
2
 + onesCol
2
 - zerosRow
2
 - zerosCol
2
 = 1 + 3 - 2 - 0 = 2
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/11/06/image-20221106171747-6.png] 
 
```
Input:
 grid = [[1,1,1],[1,1,1]]

Output:
 [[5,5,5],[5,5,5]]

Explanation:

- diff[0][0] = onesRow
0
 + onesCol
0
 - zerosRow
0
 - zerosCol
0
 = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow
0
 + onesCol
1
 - zerosRow
0
 - zerosCol
1
 = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow
0
 + onesCol
2
 - zerosRow
0
 - zerosCol
2
 = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow
1
 + onesCol
0
 - zerosRow
1
 - zerosCol
0
 = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow
1
 + onesCol
1
 - zerosRow
1
 - zerosCol
1
 = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow
1
 + onesCol
2
 - zerosRow
1
 - zerosCol
2
 = 3 + 2 - 0 - 0 = 5
```

 Constraints: 

 m == grid.length 
 
 n == grid[i].length 
 
 1 <= m, n <= 10 5 
 
 1 <= m * n <= 10 5 
 
 grid[i][j] is either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid){int m=grid.size(),n=grid[0].size();vector<int> r(m),c(n);for(int i=0;i<m;i++)for(int j=0;j<n;j++){r[i]+=grid[i][j];c[j]+=grid[i][j];}vector<vector<int>> ans(m,vector<int>(n));for(int i=0;i<m;i++)for(int j=0;j<n;j++)ans[i][j]=2*r[i]+2*c[j]-m-n;return ans;}};
```


## 2553. Separate the Digits in an Array

**Problem:** https://leetcode.com/problems/separate-the-digits-in-an-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(D)

**Space complexity:** O(D)

**Complexity reasoning:** Converts each integer to a decimal string and appends each digit once; D is the total number of digits.

### Problem description

Given an array of positive integers nums , return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums . 
 
 To separate the digits of an integer is to get all the digits it has in the same order. 

 For example, for the integer 10921 , the separation of its digits is [1,0,9,2,1] . 

 Example 1: 
 
```
Input:
 nums = [13,25,83,77]

Output:
 [1,3,2,5,8,3,7,7]

Explanation:
 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
```

 Example 2: 
 
```
Input:
 nums = [7,1,3,9]

Output:
 [7,1,3,9]

Explanation:
 The separation of each integer in nums is itself.
answer = [7,1,3,9].
```

 Constraints: 

 1 <= nums.length <= 1000 
 
 1 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 vector<int> separateDigits(vector<int>& nums){vector<int> ans;for(int x:nums){for(char c:to_string(x))ans.push_back(c-'0');}return ans;}
};
```


## 2639. Find the Width of Columns of a Grid

**Problem:** https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn · d)

**Space complexity:** O(n) output

**Complexity reasoning:** Each of the m×n entries is converted to a decimal string of up to d digits; the width array stores n results.

### Problem description

You are given a 0-indexed m x n integer matrix grid . The width of a column is the maximum length of its integers. 

 For example, if grid = [[-10], [3], [12]] , the width of the only column is 3 since -10 is of length 3 . 

 Return an integer array ans of size n where ans[i] is the width of the i th column . 
 
 The length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise. 

 Example 1: 
 
```
Input:
 grid = [[1],[22],[333]]

Output:
 [3]

Explanation:
 In the 0
th
 column, 333 is of length 3.
```

 Example 2: 
 
```
Input:
 grid = [[-15,1,3],[15,7,12],[5,6,-2]]

Output:
 [3,1,2]

Explanation:
 
In the 0
th
 column, only -15 is of length 3.
In the 1
st
 column, all integers are of length 1. 
In the 2
nd
 column, both 12 and -2 are of length 2.
```

 Constraints: 

 m == grid.length 
 
 n == grid[i].length 
 
 1 <= m, n <= 100 
 
 -10 9 <= grid[r][c] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 vector<int> findColumnWidth(vector<vector<int>>& grid){
  int m=grid.size(),n=grid[0].size();vector<int> ans(n,0);
  for(int i=0;i<m;++i)for(int j=0;j<n;++j)ans[j]=max(ans[j],(int)to_string(grid[i][j]).size());
  return ans;
 }
};
```


## 2643. Row With Maximum Ones

**Problem:** https://leetcode.com/problems/row-with-maximum-ones/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Accumulate each of the m rows of n entries; the returned two-element vector has constant size.

### Problem description

Given a m x n binary matrix mat , find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row. 
 
 In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected. 
 
 Return an array containing the index of the row, and the number of ones in it. 

 Example 1: 
 
```
Input:
 mat = [[0,1],[1,0]]

Output:
 [0,1]

Explanation:
 Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of ones (1
)
. So, the answer is [0,1].
```

 Example 2: 
 
```
Input:
 mat = [[0,0,0],[0,1,1]]

Output:
 [1,2]

Explanation:
 The row indexed 1 has the maximum count of ones 
(2)
. So we return its index, 
1
, and the count. So, the answer is [1,2].
```

 Example 3: 
 
```
Input:
 mat = [[0,0],[1,1],[0,0]]

Output:
 [1,2]

Explanation:
 The row indexed 1 has the maximum count of ones (2). So the answer is [1,2].
```

 Constraints: 

 m == mat.length   
 
 n == mat[i].length   
 
 1 <= m, n <= 100   
 
 mat[i][j] is either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 vector<int> rowAndMaximumOnes(vector<vector<int>>& mat){
  int row=0,best=-1;
  for(int i=0;i<(int)mat.size();++i){int c=accumulate(mat[i].begin(),mat[i].end(),0);if(c>best){best=c;row=i;}}
  return {row,best};
 }
};
```


## 2644. Find the Maximum Divisibility Score

**Problem:** https://leetcode.com/problems/find-the-maximum-divisibility-score/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(DN)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** For each of D divisors, test divisibility of all N numbers; only counters and the best divisor are retained.

### Problem description

You are given two integer arrays nums and divisors . 
 
 The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i] . 
 
 Return the integer divisors[i] with the maximum divisibility score. If multiple integers have the maximum score, return the smallest one. 

 Example 1: 

 Input: nums = [2,9,15,50], divisors = [5,3,7,2] 
 
 Output: 2 
 
 Explanation: 
 
 The divisibility score of divisors[0] is 2 since nums[2] and nums[3] are divisible by 5. 
 
 The divisibility score of divisors[1] is 2 since nums[1] and nums[2] are divisible by 3. 
 
 The divisibility score of divisors[2] is 0 since none of the numbers in nums is divisible by 7. 
 
 The divisibility score of divisors[3] is 2 since nums[0] and nums[3] are divisible by 2. 
 
 As divisors[0] ,  divisors[1] , and divisors[3] have the same divisibility score, we return the smaller one which is divisors[3] . 

 Example 2: 

 Input: nums = [4,7,9,3,9], divisors = [5,2,3] 
 
 Output: 3 
 
 Explanation: 
 
 The divisibility score of divisors[0] is 0 since none of numbers in nums is divisible by 5. 
 
 The divisibility score of divisors[1] is 1 since only nums[0] is divisible by 2. 
 
 The divisibility score of divisors[2] is 3 since nums[2] , nums[3] and nums[4] are divisible by 3. 

 Example 3: 

 Input: nums = [20,14,21,10], divisors = [10,16,20] 
 
 Output: 10 
 
 Explanation: 
 
 The divisibility score of divisors[0] is 2 since nums[0] and nums[3] are divisible by 10. 
 
 The divisibility score of divisors[1] is 0 since none of the numbers in nums is divisible by 16. 
 
 The divisibility score of divisors[2] is 1 since nums[0] is divisible by 20. 

 Constraints: 

 1 <= nums.length, divisors.length <= 1000 
 
 1 <= nums[i], divisors[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 int maxDivScore(vector<int>& nums,vector<int>& divisors){
  int best=-1,ans=INT_MAX;
  for(int d:divisors){int c=0;for(int x:nums)if(x%d==0)++c;if(c>best||(c==best&&d<ans)){best=c;ans=d;}}
  return ans;
 }
};
```


## 2660. Determine the Winner of a Bowling Game

**Problem:** https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Each player’s n rolls is scanned once; checking the previous two rolls takes constant time.

### Problem description

You are given two 0-indexed integer arrays player1 and player2 , representing the number of pins that player 1 and player 2 hit in a bowling game, respectively. 
 
 The bowling game consists of n turns, and the number of pins in each turn is exactly 10. 
 
 Assume a player hits x i pins in the i th turn. The value of the i th turn for the player is: 

 2x i if the player hits 10 pins in either (i - 1) th or (i - 2) th turn . 
 
 Otherwise, it is x i . 

 The score of the player is the sum of the values of their n turns. 
 
 Return 

 1 if the score of player 1 is more than the score of player 2, 
 
 2 if the score of player 2 is more than the score of player 1, and 
 
 0 in case of a draw. 

 Example 1: 

 Input: player1 = [5,10,3,2], player2 = [6,5,7,3] 
 
 Output: 1 
 
 Explanation: 
 
 The score of player 1 is 5 + 10 + 2*3 + 2*2 = 25. 
 
 The score of player 2 is 6 + 5 + 7 + 3 = 21. 

 Example 2: 

 Input: player1 = [3,5,7,6], player2 = [8,10,10,2] 
 
 Output: 2 
 
 Explanation: 
 
 The score of player 1 is 3 + 5 + 7 + 6 = 21. 
 
 The score of player 2 is 8 + 10 + 2*10 + 2*2 = 42. 

 Example 3: 

 Input: player1 = [2,3], player2 = [4,1] 
 
 Output: 0 
 
 Explanation: 
 
 The score of player1 is 2 + 3 = 5. 
 
 The score of player2 is 4 + 1 = 5. 

 Example 4: 

 Input: player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1] 
 
 Output: 2 
 
 Explanation: 
 
 The score of player1 is 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73. 
 
 The score of player2 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75. 

 Constraints: 

 n == player1.length == player2.length 
 
 1 <= n <= 1000 
 
 0 <= player1[i], player2[i] <= 10

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {int score(vector<int>&v){int s=0;for(int i=0;i<(int)v.size();i++)s+=v[i]*((i>0&&v[i-1]==10)||(i>1&&v[i-2]==10)?2:1);return s;}public:int isWinner(vector<int>&player1,vector<int>&player2){int a=score(player1),b=score(player2);return a==b?0:(a>b?1:2);}};
```


## 2672. Number of Adjacent Elements With the Same Color

**Problem:** https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + q)

**Space complexity:** O(n + q)

**Complexity reasoning:** Initialize an n-element color array, then update at most two adjacent pairs per query; store q answers.

### Problem description

You are given an integer n representing an array colors of length n where all elements are set to 0's meaning uncolored . You are also given a 2D integer array queries where queries[i] = [index i , color i ] . For the i th query : 

 Set colors[index i ] to color i . 
 
 Count the number of adjacent pairs in colors which have the same color (regardless of color i ). 

 Return an array answer of the same length as queries where answer[i] is the answer to the i th query. 

 Example 1: 

 Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]] 
 
 Output: [0,1,1,0,2] 
 
 Explanation: 

 Initially array colors = [0,0,0,0], where 0 denotes uncolored elements of the array. 
 
 After the 1 st query colors = [2,0,0,0]. The count of adjacent pairs with the same color is 0. 
 
 After the 2 nd query colors = [2,2,0,0]. The count of adjacent pairs with the same color is 1. 
 
 After the 3 rd query colors = [2,2,0,1]. The count of adjacent pairs with the same color is 1. 
 
 After the 4 th query colors = [2,1,0,1]. The count of adjacent pairs with the same color is 0. 
 
 After the 5 th query colors = [2,1,1,1]. The count of adjacent pairs with the same color is 2. 

 Example 2: 

 Input: n = 1, queries = [[0,100000]] 
 
 Output: [0] 
 
 Explanation: 
 
 After the 1 st query colors = [100000]. The count of adjacent pairs with the same color is 0. 

 Constraints: 

 1 <= n <= 10 5 
 
 1 <= queries.length <= 10 5 
 
 queries[i].length == 2 
 
 0 <= index i  <= n - 1 
 
 1 <=  color i  <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int> colorTheArray(int n,vector<vector<int>>&queries){vector<int>a(n),ans;int count=0;for(auto&q:queries){int i=q[0],v=q[1];if(a[i]){if(i&&a[i]==a[i-1])count--;if(i+1<n&&a[i]==a[i+1])count--;}a[i]=v;if(i&&a[i]==a[i-1])count++;if(i+1<n&&a[i]==a[i+1])count++;ans.push_back(count);}return ans;}};
```


## 2717. Semi-Ordered Permutation

**Problem:** https://leetcode.com/problems/semi-ordered-permutation/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** A single pass locates the positions of 1 and n, followed by constant-time arithmetic.

### Problem description

You are given a 0-indexed permutation of n integers nums . 
 
 A permutation is called semi-ordered if the first number equals 1 and the last number equals n . You can perform the below operation as many times as you want until you make nums a semi-ordered permutation: 

 Pick two adjacent elements in nums , then swap them. 

 Return the minimum number of operations to make nums a semi-ordered permutation . 
 
 A permutation is a sequence of integers from 1 to n of length n containing each number exactly once. 

 Example 1: 
 
```
Input:
 nums = [2,1,4,3]

Output:
 2

Explanation:
 We can make the permutation semi-ordered using these sequence of operations: 
1 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
2 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than two operations that make nums a semi-ordered permutation.
```

 Example 2: 
 
```
Input:
 nums = [2,4,1,3]

Output:
 3

Explanation:
 We can make the permutation semi-ordered using these sequence of operations:
1 - swap i = 1 and j = 2. The permutation becomes [2,1,4,3].
2 - swap i = 0 and j = 1. The permutation becomes [1,2,4,3].
3 - swap i = 2 and j = 3. The permutation becomes [1,2,3,4].
It can be proved that there is no sequence of less than three operations that make nums a semi-ordered permutation.
```

 Example 3: 
 
```
Input:
 nums = [1,3,4,2,5]

Output:
 0

Explanation:
 The permutation is already a semi-ordered permutation.
```

 Constraints: 

 2 <= nums.length == n <= 50 
 
 1 <= nums[i] <= 50 
 
 nums is a permutation.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int semiOrderedPermutation(vector<int>& nums){int n=nums.size(),a=0,b=0;for(int i=0;i<n;++i){if(nums[i]==1)a=i;if(nums[i]==n)b=i;}return a+n-1-b-(a>b);}};
```


## 2728. Count Houses in a Circular Street

**Problem:** https://leetcode.com/problems/count-houses-in-a-circular-street/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Interactive

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(k + h)

**Space complexity:** O(1)

**Complexity reasoning:** Close doors and advance k times, then traverse h houses until the opened door is reached (h ≤ k under the problem guarantee).

### Problem description

You are given an object street of class Street that represents a circular street and a positive integer k which represents a maximum bound for the number of houses in that street (in other words, the number of houses is less than or equal to k ). Houses' doors could be open or closed initially. 
 
 Initially, you are standing in front of a door to a house on this street. Your task is to count the number of houses in the street. 
 
 The class Street contains the following functions which may help you: 

 void openDoor() : Open the door of the house you are in front of. 
 
 void closeDoor() : Close the door of the house you are in front of. 
 
 boolean isDoorOpen() : Returns true if the door of the current house is open and false otherwise. 
 
 void moveRight() : Move to the right house. 
 
 void moveLeft() : Move to the left house. 

 Return ans which represents the number of houses on this street. 

 Example 1: 
 
```
Input:
 street = [0,0,0,0], k = 10

Output:
 4

Explanation:
 There are 4 houses, and all their doors are closed. 
The number of houses is less than k, which is 10.
```

 Example 2: 
 
```
Input:
 street = [1,0,1,1,0], k = 5

Output:
 5

Explanation:
 There are 5 houses, and the doors of the 1st, 3rd, and 4th house (moving in the right direction) are open, and the rest are closed.
The number of houses is equal to k, which is 5.
```

 Constraints: 

 n == number of houses 
 
 1 <= n <= k <= 10 3

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int houseCount(Street* street, int k) {
        for (int i = 0; i < k; ++i) {
            street->closeDoor();
            street->moveRight();
        }
        street->openDoor();
        street->moveRight();
        int count = 1;
        while (!street->isDoorOpen()) {
            ++count;
            street->moveRight();
        }
        return count;
    }
};
```


## 2735. Collecting Chocolates

**Problem:** https://leetcode.com/problems/collecting-chocolates/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(n)

**Complexity reasoning:** Try all n rotations; each rotation scans n positions while maintaining a length-n minimum-cost array.

### Problem description

You are given a 0-indexed integer array nums of size n representing the cost of collecting different chocolates. The cost of collecting the chocolate at the index i  is nums[i] . Each chocolate is of a different type, and initially, the chocolate at the index  i  is of i th type. 
 
 In one operation, you can do the following with an incurred cost of x : 

 Simultaneously change the chocolate of i th type to ((i + 1) mod n) th type for all chocolates. 

 Return the minimum cost to collect chocolates of all types, given that you can perform as many operations as you would like. 

 Example 1: 
 
```
Input:
 nums = [20,1,15], x = 5

Output:
 13

Explanation:
 Initially, the chocolate types are [0,1,2]. We will buy the 1
st
 type of chocolate at a cost of 1.
Now, we will perform the operation at a cost of 5, and the types of chocolates will become [1,2,0]. We will buy the 2
nd
 
type of chocolate at a cost of 1.
Now, we will again perform the operation at a cost of 5, and the chocolate types will become [2,0,1]. We will buy the 0
th 
type of chocolate at a cost of 1. 
Thus, the total cost will become (1 + 5 + 1 + 5 + 1) = 13. We can prove that this is optimal.
```

 Example 2: 
 
```
Input:
 nums = [1,2,3], x = 4

Output:
 6

Explanation:
 We will collect all three types of chocolates at their own price without performing any operations. Therefore, the total cost is 1 + 2 + 3 = 6.
```

 Constraints: 

 1 <= nums.length <= 1000 
 
 1 <= nums[i] <= 10 9 
 
 1 <= x <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:long long minCost(vector<int>& nums,int x){int n=nums.size();vector<int> best=nums;long long ans=LLONG_MAX;for(int t=0;t<n;++t){long long cost=1LL*t*x;for(int i=0;i<n;++i){best[i]=min(best[i],nums[(i+t)%n]);cost+=best[i];}ans=min(ans,cost);}return ans;}};
```


## 2765. Longest Alternating Subarray

**Problem:** https://leetcode.com/problems/longest-alternating-subarray/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(1)

**Complexity reasoning:** For every starting index, extend the alternating run until it breaks; the nested scans can examine Θ(n²) pairs.

### Problem description

You are given a 0-indexed integer array nums . A subarray s of length m is called alternating if: 

 m is greater than 1 . 
 
 s 1 = s 0 + 1 . 
 
 The 0-indexed subarray s looks like [s 0 , s 1 , s 0 , s 1 ,...,s (m-1) % 2 ] . In other words, s 1 - s 0 = 1 , s 2 - s 1 = -1 , s 3 - s 2 = 1 , s 4 - s 3 = -1 , and so on up to s[m - 1] - s[m - 2] = (-1) m . 

 Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists . 
 
 A subarray is a contiguous non-empty sequence of elements within an array. 

 Example 1: 

 Input: nums = [2,3,4,3,4] 
 
 Output: 4 
 
 Explanation: 
 
 The alternating subarrays are [2, 3] , [3,4] , [3,4,3] , and [3,4,3,4] . The longest of these is [3,4,3,4] , which is of length 4. 

 Example 2: 

 Input: nums = [4,5,6] 
 
 Output: 2 
 
 Explanation: 
 
 [4,5] and [5,6] are the only two alternating subarrays. They are both of length 2. 

 Constraints: 

 2 <= nums.length <= 100 
 
 1 <= nums[i] <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int alternatingSubarray(vector<int>& nums) {
        int n = nums.size(), answer = -1;
        for (int i = 0; i + 1 < n; ++i) {
            int expected = 1;
            for (int j = i + 1; j < n; ++j) {
                if (nums[j] - nums[j - 1] != expected) break;
                answer = max(answer, j - i + 1);
                expected = -expected;
            }
        }
        return answer;
    }
};
```


## 2778. Sum of Squares of Special Elements 

**Problem:** https://leetcode.com/problems/sum-of-squares-of-special-elements/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Check every 1-based index for divisibility into n and add the corresponding squared value.

### Problem description

You are given a 1-indexed integer array nums of length n . 
 
 An element nums[i] of nums is called special if i divides n , i.e. n % i == 0 . 
 
 Return the sum of the squares of all special elements of nums . 

 Example 1: 
 
```
Input:
 nums = [1,2,3,4]

Output:
 21

Explanation:
 There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.
```

 Example 2: 
 
```
Input:
 nums = [2,7,1,19,18,3]

Output:
 63

Explanation:
 There are exactly 4 special elements in nums: nums[1] since 1 divides 6, nums[2] since 2 divides 6, nums[3] since 3 divides 6, and nums[6] since 6 divides 6. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[3] * nums[3] + nums[6] * nums[6] = 2 * 2 + 7 * 7 + 1 * 1 + 3 * 3 = 63.
```

 Constraints: 

 1 <= nums.length == n <= 50 
 
 1 <= nums[i] <= 50

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int sumOfSquares(vector<int>& nums){int n=nums.size(),ans=0;for(int i=1;i<=n;++i)if(n%i==0)ans+=nums[i-1]*nums[i-1];return ans;}};
```


## 2798. Number of Employees Who Met the Target

**Problem:** https://leetcode.com/problems/number-of-employees-who-met-the-target/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Count qualifying employees in one pass through the hours array.

### Problem description

There are n employees in a company, numbered from 0 to n - 1 . Each employee i has worked for hours[i] hours in the company. 
 
 The company requires each employee to work for at least target hours. 
 
 You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target . 
 
 Return the integer denoting the number of employees who worked at least target hours . 

 Example 1: 
 
```
Input:
 hours = [0,1,2,3,4], target = 2

Output:
 3

Explanation:
 The company wants each employee to work for at least 2 hours.
- Employee 0 worked for 0 hours and didn't meet the target.
- Employee 1 worked for 1 hours and didn't meet the target.
- Employee 2 worked for 2 hours and met the target.
- Employee 3 worked for 3 hours and met the target.
- Employee 4 worked for 4 hours and met the target.
There are 3 employees who met the target.
```

 Example 2: 
 
```
Input:
 hours = [5,1,4,2,2], target = 6

Output:
 0

Explanation:
 The company wants each employee to work for at least 6 hours.
There are 0 employees who met the target.
```

 Constraints: 

 1 <= n == hours.length <= 50 
 
 0 <= hours[i], target <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int numberOfEmployeesWhoMetTarget(vector<int>& hours,int target){int ans=0;for(int x:hours)ans+=x>=target;return ans;}};
```


## 2855. Minimum Right Shifts to Sort the Array

**Problem:** https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Scan adjacent pairs to find the unique descending boundary, then validate and compute the required shift count.

### Problem description

You are given a 0-indexed array nums of length n containing distinct positive integers. Return the minimum number of right shifts required to sort nums and -1 if this is not possible. 
 
 A right shift is defined as shifting the element at index i to index (i + 1) % n , for all indices. 

 Example 1: 
 
```
Input:
 nums = [3,4,5,1,2]

Output:
 2

Explanation:
 
After the first right shift, nums = [2,3,4,5,1].
After the second right shift, nums = [1,2,3,4,5].
Now nums is sorted; therefore the answer is 2.
```

 Example 2: 
 
```
Input:
 nums = [1,3,5]

Output:
 0

Explanation:
 nums is already sorted therefore, the answer is 0.
```

 Example 3: 
 
```
Input:
 nums = [2,1,4]

Output:
 -1

Explanation:
 It's impossible to sort the array using right shifts.
```

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100 
 
 nums contains distinct integers.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:int minimumRightShifts(vector<int>& nums){int n=nums.size(),breaks=0,pos=0;for(int i=1;i<n;++i)if(nums[i]<nums[i-1]){++breaks;pos=i;}if(breaks==0)return 0;if(breaks>1||nums[n-1]>nums[0])return -1;return n-pos;}};
```


## 2899. Last Visited Integers

**Problem:** https://leetcode.com/problems/last-visited-integers/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each input item is processed once; the seen values and responses can each grow to linear size.

### Problem description

Given an integer array nums where nums[i] is either a positive integer or -1 . We need to find for each -1 the respective positive integer, which we call the last visited integer. 
 
 To achieve this goal, let's define two empty arrays: seen and ans . 
 
 Start iterating from the beginning of the array nums . 

 If a positive integer is encountered, prepend it to the front of seen . 
 
 If -1  is encountered, let k be the number of consecutive -1 s seen so far (including the current -1 ),

 If k is less than or equal to the length of seen , append the k -th element of seen to ans . 
 
 If k is strictly greater than the length of seen , append -1 to ans . 

 Return the array ans . 

 Example 1: 

 Input: nums = [1,2,-1,-1,-1] 
 
 Output: [2,1,-1] 
 
 Explanation: 
 
 Start with seen = [] and ans = [] . 

 Process nums[0] : The first element in nums is 1 . We prepend it to the front of seen . Now, seen == [1] . 
 
 Process nums[1] : The next element is 2 . We prepend it to the front of seen . Now, seen == [2, 1] . 
 
 Process nums[2] : The next element is -1 . This is the first occurrence of -1 , so k == 1 . We look for the first element in seen. We append 2 to ans . Now, ans == [2] . 
 
 Process nums[3] : Another -1 . This is the second consecutive -1 , so k == 2 . The second element in seen is 1 , so we append 1 to ans . Now, ans == [2, 1] . 
 
 Process nums[4] : Another -1 , the third in a row, making k = 3 . However, seen only has two elements ( [2, 1] ). Since k is greater than the number of elements in seen , we append -1 to ans . Finally, ans == [2, 1, -1] . 

 Example 2: 

 Input: nums = [1,-1,2,-1,-1] 
 
 Output: [1,2,1] 
 
 Explanation: 
 
 Start with seen = [] and ans = [] . 

 Process nums[0] : The first element in nums is 1 . We prepend it to the front of seen . Now, seen == [1] . 
 
 Process nums[1] : The next element is -1 . This is the first occurrence of -1 , so k == 1 . We look for the first element in seen , which is 1 . Append 1 to ans . Now, ans == [1] . 
 
 Process nums[2] : The next element is 2 . Prepend this to the front of seen . Now, seen == [2, 1] . 
 
 Process nums[3] : The next element is -1 . This -1 is not consecutive to the first -1 since 2 was in between. Thus, k resets to 1 . The first element in seen is 2 , so append 2 to ans . Now, ans == [1, 2] . 
 
 Process nums[4] : Another -1 . This is consecutive to the previous -1 , so k == 2 . The second element in seen is 1 , append 1 to ans . Finally, ans == [1, 2, 1] . 

 Constraints: 

 1 <= nums.length <= 100 
 
 nums[i] == -1 or 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> lastVisitedIntegers(vector<int>& nums) {
        vector<int> seen, answer;
        int consecutive = 0;
        for (int x : nums) {
            if (x != -1) {
                seen.push_back(x);
                consecutive = 0;
            } else {
                ++consecutive;
                int size = seen.size();
                answer.push_back(consecutive <= size ? seen[size - consecutive] : -1);
            }
        }
        return answer;
    }
};
```


## 2908. Minimum Sum of Mountain Triplets I

**Problem:** https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Build prefix and suffix minima in two linear passes, then evaluate each middle index once.

### Problem description

You are given a 0-indexed array nums of integers. 
 
 A triplet of indices (i, j, k) is a mountain if: 

 i < j < k 
 
 nums[i] < nums[j] and nums[k] < nums[j] 

 Return the minimum possible sum of a mountain triplet of nums . If no such triplet exists, return -1 . 

 Example 1: 
 
```
Input:
 nums = [8,6,1,5,3]

Output:
 9

Explanation:
 Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
- 2 < 3 < 4
- nums[2] < nums[3] and nums[4] < nums[3]
And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.
```

 Example 2: 
 
```
Input:
 nums = [5,4,8,7,10,2]

Output:
 13

Explanation:
 Triplet (1, 3, 5) is a mountain triplet of sum 13 since: 
- 1 < 3 < 5
- nums[1] < nums[3] and nums[5] < nums[3]
And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.
```

 Example 3: 
 
```
Input:
 nums = [6,5,4,3,4,5]

Output:
 -1

Explanation:
 It can be shown that there are no mountain triplets in nums.
```

 Constraints: 

 3 <= nums.length <= 50 
 
 1 <= nums[i] <= 50

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public:
 int minimumSum(vector<int>& nums){
  int n=nums.size();vector<int> left(n),right(n);int v=INT_MAX;
  for(int i=0;i<n;++i){left[i]=v;v=min(v,nums[i]);}
  v=INT_MAX;for(int i=n-1;i>=0;--i){right[i]=v;v=min(v,nums[i]);}
  int ans=INT_MAX;for(int j=1;j+1<n;++j)if(left[j]<nums[j]&&right[j]<nums[j])ans=min(ans,left[j]+nums[j]+right[j]);
  return ans==INT_MAX?-1:ans;
 }
};
```


## 2923. Find Champion I

**Problem:** https://leetcode.com/problems/find-champion-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(1)

**Complexity reasoning:** For each candidate champion, scan up to n opponents in the matrix; return immediately when a row wins against all others.

### Problem description

There are n teams numbered from 0 to n - 1 in a tournament. 
 
 Given a 0-indexed 2D boolean matrix grid of size n * n . For all i, j that 0 <= i, j <= n - 1 and i != j team i is stronger than team j if grid[i][j] == 1 , otherwise, team j is stronger than team i . 
 
 Team a will be the champion of the tournament if there is no team b that is stronger than team a . 
 
 Return the team that will be the champion of the tournament. 

 Example 1: 
 
```
Input:
 grid = [[0,1],[0,0]]

Output:
 0

Explanation:
 There are two teams in this tournament.
grid[0][1] == 1 means that team 0 is stronger than team 1. So team 0 will be the champion.
```

 Example 2: 
 
```
Input:
 grid = [[0,0,1],[1,0,1],[0,0,0]]

Output:
 1

Explanation:
 There are three teams in this tournament.
grid[1][0] == 1 means that team 1 is stronger than team 0.
grid[1][2] == 1 means that team 1 is stronger than team 2.
So team 1 will be the champion.
```

 Constraints: 

 n == grid.length 
 
 n == grid[i].length 
 
 2 <= n <= 100 
 
 grid[i][j] is either 0 or 1 . 
 
 For all i grid[i][i] is 0. 
 
 For all i, j that i != j , grid[i][j] != grid[j][i] . 
 
 The input is generated such that if team a is stronger than team b and team b is stronger than team c , then team a is stronger than team c .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution{public:int findChampion(vector<vector<int>>& grid){int n=grid.size();for(int i=0;i<n;i++){bool ok=true;for(int j=0;j<n;j++)if(i!=j&&!grid[i][j])ok=false;if(ok)return i;}return -1;}};
```


## 2934. Minimum Operations to Maximize Last Elements in Arrays

**Problem:** https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Evaluate both choices for the final pair; each choice scans the other n−1 positions with constant-time feasibility checks.

### Problem description

You are given two 0-indexed integer arrays, nums1 and nums2 , both having length n . 
 
 You are allowed to perform a series of operations ( possibly none ). 
 
 In an operation, you select an index i in the range [0, n - 1] and swap the values of nums1[i] and nums2[i] . 
 
 Your task is to find the minimum number of operations required to satisfy the following conditions: 

 nums1[n - 1] is equal to the maximum value among all elements of nums1 , i.e., nums1[n - 1] = max(nums1[0], nums1[1], ..., nums1[n - 1]) . 
 
 nums2[n - 1] is equal to the maximum value among all elements of nums2 , i.e., nums2[n - 1] = max(nums2[0], nums2[1], ..., nums2[n - 1]) . 

 Return an integer denoting the minimum number of operations needed to meet both conditions , or -1 if it is impossible to satisfy both conditions. 

 Example 1: 
 
```
Input:
 nums1 = [1,2,7], nums2 = [4,5,3]

Output:
 1

Explanation:
 In this example, an operation can be performed using index i = 2.
When nums1[2] and nums2[2] are swapped, nums1 becomes [1,2,3] and nums2 becomes [4,5,7].
Both conditions are now satisfied.
It can be shown that the minimum number of operations needed to be performed is 1.
So, the answer is 1.
```

 Example 2: 
 
```
Input:
 nums1 = [2,3,4,5,9], nums2 = [8,8,4,4,4]

Output:
 2

Explanation:
 In this example, the following operations can be performed:
First operation using index i = 4.
When nums1[4] and nums2[4] are swapped, nums1 becomes [2,3,4,5,4], and nums2 becomes [8,8,4,4,9].
Another operation using index i = 3.
When nums1[3] and nums2[3] are swapped, nums1 becomes [2,3,4,4,4], and nums2 becomes [8,8,4,5,9].
Both conditions are now satisfied.
It can be shown that the minimum number of operations needed to be performed is 2.
So, the answer is 2.
```

 Example 3: 
 
```
Input:
 nums1 = [1,5,4], nums2 = [2,5,3]

Output:
 -1

Explanation:
 In this example, it is not possible to satisfy both conditions. 
So, the answer is -1.
```

 Constraints: 

 1 <= n == nums1.length == nums2.length <= 1000 
 
 1 <= nums1[i] <= 10 9 
 
 1 <= nums2[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution{public:int minOperations(vector<int>& nums1,vector<int>& nums2){int n=nums1.size(),INF=1000000000;auto solve=[&](int a,int b){int cost=0;for(int i=0;i<n-1;i++){bool keep=nums1[i]<=a&&nums2[i]<=b,sw=nums2[i]<=a&&nums1[i]<=b;if(!keep&&!sw)return INF;if(!keep)cost++;}return cost;};int ans=min(solve(nums1.back(),nums2.back()),1+solve(nums2.back(),nums1.back()));return ans>=INF?-1:ans;}};
```


## 2951. Find the Peaks

**Problem:** https://leetcode.com/problems/find-the-peaks/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output

**Complexity reasoning:** Check each interior position against its two neighbors and append peak indices to the output vector.

### Problem description

You are given a 0-indexed array mountain . Your task is to find all the peaks in the mountain array. 
 
 Return an array that consists of indices of peaks in the given array in any order . 
 
 Notes: 

 A peak is defined as an element that is strictly greater than its neighboring elements. 
 
 The first and last elements of the array are not a peak. 

 Example 1: 
 
```
Input:
 mountain = [2,4,4]

Output:
 []

Explanation:
 mountain[0] and mountain[2] can not be a peak because they are first and last elements of the array.
mountain[1] also can not be a peak because it is not strictly greater than mountain[2].
So the answer is [].
```

 Example 2: 
 
```
Input:
 mountain = [1,4,3,8,5]

Output:
 [1,3]

Explanation:
 mountain[0] and mountain[4] can not be a peak because they are first and last elements of the array.
mountain[2] also can not be a peak because it is not strictly greater than mountain[3] and mountain[1].
But mountain [1] and mountain[3] are strictly greater than their neighboring elements.
So the answer is [1,3].
```

 Constraints: 

 3 <= mountain.length <= 100 
 
 1 <= mountain[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution{public:vector<int> findPeaks(vector<int>& mountain){vector<int> ans;for(int i=1;i+1<(int)mountain.size();i++)if(mountain[i]>mountain[i-1]&&mountain[i]>mountain[i+1])ans.push_back(i);return ans;}};
```


## 3000. Maximum Area of Longest Diagonal Rectangle

**Problem:** https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Inspect each rectangle once, comparing squared diagonal length and area with the current best.

### Problem description

You are given a 2D 0-indexed integer array dimensions . 
 
 For all indices i , 0 <= i < dimensions.length , dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i . 
 
 Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area. 

 Example 1: 
 
```
Input:
 dimensions = [[9,3],[8,6]]

Output:
 48

Explanation:
 
For index = 0, length = 9 and width = 3. Diagonal length = sqrt(9 * 9 + 3 * 3) = sqrt(90) ≈
 9.487.
For index = 1, length = 8 and width = 6. Diagonal length = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10.
So, the rectangle at index 1 has a greater diagonal length therefore we return area = 8 * 6 = 48.
```

 Example 2: 
 
```
Input:
 dimensions = [[3,4],[4,3]]

Output:
 12

Explanation:
 Length of diagonal is the same for both which is 5, so maximum area = 12.
```

 Constraints: 

 1 <= dimensions.length <= 100 
 
 dimensions[i].length == 2 
 
 1 <= dimensions[i][0], dimensions[i][1] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int areaOfMaxDiagonal(vector<vector<int>>& dimensions){int diag=-1,area=0;for(auto&v:dimensions){int d=v[0]*v[0]+v[1]*v[1],a=v[0]*v[1];if(d>diag||(d==diag&&a>area))diag=d,area=a;}return area;}};
```


## 3030. Find the Grid of Region Average

**Problem:** https://leetcode.com/problems/find-the-grid-of-region-average/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn)

**Complexity reasoning:** Every 3×3 candidate region is checked and, if valid, updated using constant-size loops; sum and count matrices each use mn cells.

### Problem description

You are given m x n grid image which represents a grayscale image, where image[i][j] represents a pixel with intensity in the range [0..255] . You are also given a non-negative integer threshold . 
 
 Two pixels are adjacent if they share an edge. 
 
 A region is a 3 x 3 subgrid where the absolute difference in intensity between any two adjacent pixels is less than or equal to threshold . 
 
 All pixels in a region belong to that region, note that a pixel can belong to multiple regions. 
 
 You need to calculate a m x n grid result , where result[i][j] is the average intensity of the regions to which image[i][j] belongs, rounded down to the nearest integer. If image[i][j] belongs to multiple regions, result[i][j] is the average of the rounded-down average intensities of these regions, rounded down to the nearest integer. If image[i][j] does not belong to any region, result[i][j] is equal to image[i][j] . 
 
 Return the grid result . 

 Example 1: 

 Input: image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3 
 
 Output: [[9,9,9,9],[9,9,9,9],[9,9,9,9]] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2023/12/21/example0corrected.png] 
 
 There are two regions as illustrated above. The average intensity of the first region is 9, while the average intensity of the second region is 9.67 which is rounded down to 9. The average intensity of both of the regions is (9 + 9) / 2 = 9. As all the pixels belong to either region 1, region 2, or both of them, the intensity of every pixel in the result is 9. 
 
 Please note that the rounded-down values are used when calculating the average of multiple regions, hence the calculation is done using 9 as the average intensity of region 2, not 9.67. 

 Example 2: 

 Input: image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12 
 
 Output: [[25,25,25],[27,27,27],[27,27,27],[30,30,30]] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2023/12/21/example1corrected.png] 
 
 There are two regions as illustrated above. The average intensity of the first region is 25, while the average intensity of the second region is 30. The average intensity of both of the regions is (25 + 30) / 2 = 27.5 which is rounded down to 27. 
 
 All the pixels in row 0 of the image belong to region 1, hence all the pixels in row 0 in the result are 25. Similarly, all the pixels in row 3 in the result are 30. The pixels in rows 1 and 2 of the image belong to region 1 and region 2, hence their assigned value is 27 in the result. 

 Example 3: 

 Input: image = [[5,6,7],[8,9,10],[11,12,13]], threshold = 1 
 
 Output: [[5,6,7],[8,9,10],[11,12,13]] 
 
 Explanation: 
 
 There is only one 3 x 3 subgrid, while it does not have the condition on difference of adjacent pixels, for example, the difference between image[0][0] and image[1][0] is |5 - 8| = 3 > threshold = 1 . None of them belong to any valid regions, so the result should be the same as image . 

 Constraints: 

 3 <= n, m <= 500 
 
 0 <= image[i][j] <= 255 
 
 0 <= threshold <= 255

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<vector<int>> resultGrid(vector<vector<int>>&a,int threshold){int m=a.size(),n=a[0].size();vector<vector<int>>sum(m,vector<int>(n)),cnt=sum;for(int i=0;i+2<m;i++)for(int j=0;j+2<n;j++){bool ok=true;int total=0;for(int r=i;r<i+3;r++)for(int c=j;c<j+3;c++){total+=a[r][c];if(r>i&&abs(a[r][c]-a[r-1][c])>threshold)ok=false;if(c>j&&abs(a[r][c]-a[r][c-1])>threshold)ok=false;}if(ok)for(int r=i;r<i+3;r++)for(int c=j;c<j+3;c++){sum[r][c]+=total/9;cnt[r][c]++;}}for(int i=0;i<m;i++)for(int j=0;j<n;j++)if(cnt[i][j])a[i][j]=sum[i][j]/cnt[i][j];return a;}};
```


## 3033. Modify the Matrix

**Problem:** https://leetcode.com/problems/modify-the-matrix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** For each column, scan its m entries to find the maximum and scan again to replace −1 values; the input matrix is modified in place.

### Problem description

Given a 0-indexed m x n integer matrix matrix , create a new 0-indexed matrix called answer . Make answer equal to matrix , then replace each element with the value -1 with the maximum element in its respective column. 
 
 Return the matrix answer . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2023/12/24/matrix1.png] 
 
```
Input:
 matrix = [[1,2,-1],[4,-1,6],[7,8,9]]

Output:
 [[1,2,9],[4,8,6],[7,8,9]]

Explanation:
 The diagram above shows the elements that are changed (in blue).
- We replace the value in the cell [1][1] with the maximum value in the column 1, that is 8.
- We replace the value in the cell [0][2] with the maximum value in the column 2, that is 9.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2023/12/24/matrix2.png] 
 
```
Input:
 matrix = [[3,-1],[5,2]]

Output:
 [[3,2],[5,2]]

Explanation:
 The diagram above shows the elements that are changed (in blue).
```

 Constraints: 

 m == matrix.length 
 
 n == matrix[i].length 
 
 2 <= m, n <= 50 
 
 -1 <= matrix[i][j] <= 100 
 
 The input is generated such that each column contains at least one non-negative integer.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<vector<int>> modifiedMatrix(vector<vector<int>>&a){int m=a.size(),n=a[0].size();for(int j=0;j<n;j++){int mx=0;for(int i=0;i<m;i++)mx=max(mx,a[i][j]);for(int i=0;i<m;i++)if(a[i][j]==-1)a[i][j]=mx;}return a;}};
```


## 3038. Maximum Number of Operations With the Same Score I

**Problem:** https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Process disjoint consecutive pairs until a pair sum differs from the first pair’s sum.

### Problem description

You are given an array of integers nums . Consider the following operation: 

 Delete the first two elements nums and define the score of the operation as the sum of these two elements. 

 You can perform this operation until nums contains fewer than two elements. Additionally, the same score must be achieved in all operations. 
 
 Return the maximum number of operations you can perform. 

 Example 1: 

 Input: nums = [3,2,1,4,5] 
 
 Output: 2 
 
 Explanation: 

 We can perform the first operation with the score 3 + 2 = 5 . After this operation, nums = [1,4,5] . 
 
 We can perform the second operation as its score is 4 + 1 = 5 , the same as the previous operation. After this operation, nums = [5] . 
 
 As there are fewer than two elements, we can't perform more operations. 

 Example 2: 

 Input: nums = [1,5,3,3,4,1,3,2,2,3] 
 
 Output: 2 
 
 Explanation: 

 We can perform the first operation with the score 1 + 5 = 6 . After this operation, nums = [3,3,4,1,3,2,2,3] . 
 
 We can perform the second operation as its score is 3 + 3 = 6 , the same as the previous operation. After this operation, nums = [4,1,3,2,2,3] . 
 
 We cannot perform the next operation as its score is 4 + 1 = 5 , which is different from the previous scores. 

 Example 3: 

 Input: nums = [5,3] 
 
 Output: 1 

 Constraints: 

 2 <= nums.length <= 100 
 
 1 <= nums[i] <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int maxOperations(vector<int>&a){int sum=a[0]+a[1],ans=0;for(int i=0;i+1<(int)a.size();i+=2){if(a[i]+a[i+1]!=sum)break;ans++;}return ans;}};
```


## 3065. Minimum Operations to Exceed Threshold Value I

**Problem:** https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Count elements below k with one linear pass and a single counter.

### Problem description

You are given a 0-indexed integer array nums , and an integer k . 
 
 In one operation, you can remove one occurrence of the smallest element of nums . 
 
 Return the minimum number of operations needed so that all elements of the array are greater than or equal to k . 

 Example 1: 
 
```
Input:
 nums = [2,11,10,1,3], k = 10

Output:
 3

Explanation:
 After one operation, nums becomes equal to [2, 11, 10, 3].
After two operations, nums becomes equal to [11, 10, 3].
After three operations, nums becomes equal to [11, 10].
At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
It can be shown that 3 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.
```

 Example 2: 
 
```
Input:
 nums = [1,1,2,4,9], k = 1

Output:
 0

Explanation:
 All elements of the array are greater than or equal to 1 so we do not need to apply any operations on nums.
```

 Example 3: 
 
```
Input:
 nums = [1,1,2,4,9], k = 9

Output:
 4

Explanation:
 only a single element of nums is greater than or equal to 9 so we need to apply the operations 4 times on nums.
```

 Constraints: 

 1 <= nums.length <= 50 
 
 1 <= nums[i] <= 10 9 
 
 1 <= k <= 10 9 
 
 The input is generated such that there is at least one index i such that nums[i] >= k .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int minOperations(vector<int>&nums,int k){int ans=0;for(int x:nums)ans+=x<k;return ans;}};
```


## 3073. Maximum Increasing Triplet Value

**Problem:** https://leetcode.com/problems/maximum-increasing-triplet-value/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Ordered Set

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Sort and deduplicate n values for coordinate compression; each element performs binary search and three Fenwick-tree operations, each O(log n).

### Problem description

Given an array nums , return the maximum value of a triplet (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k] . 
 
 The value of a triplet (i, j, k) is nums[i] - nums[j] + nums[k] . 

 Example 1: 

 Input: nums = [5,6,9] 
 
 Output: 8 
 
 Explanation: We only have one choice for an increasing triplet and that is choosing all three elements. The value of this triplet would be 5 - 6 + 9 = 8 . 

 Example 2: 

 Input: nums = [1,5,3,6] 
 
 Output: 4 
 
 Explanation: There are only two increasing triplets: 
 
 (0, 1, 3) : The value of this triplet is nums[0] - nums[1] + nums[3] = 1 - 5 + 6 = 2 . 
 
 (0, 2, 3) : The value of this triplet is nums[0] - nums[2] + nums[3] = 1 - 3 + 6 = 4 . 
 
 Thus the answer would be 4 . 

 Constraints: 

 3 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9 
 
 The input is generated such that at least one triplet meets the given condition.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {struct BIT{vector<long long> t;BIT(int n):t(n+1,LLONG_MIN/4){}void add(int i,long long v){for(;i<(int)t.size();i+=i&-i)t[i]=max(t[i],v);}long long get(int i){long long v=LLONG_MIN/4;for(;i;i-=i&-i)v=max(v,t[i]);return v;}};public:int maximumTripletValue(vector<int>& a){vector<int> v=a;sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());BIT b(v.size()),c(v.size());long long ans=LLONG_MIN/4;for(int x:a){int i=lower_bound(v.begin(),v.end(),x)-v.begin()+1;ans=max(ans,c.get(i-1)+x);c.add(i,b.get(i-1)-x);b.add(i,x);}return (int)ans;}};
```


## 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

**Problem:** https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Track increasing and decreasing streak lengths while scanning the array once.

### Problem description

You are given an array of integers nums . Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing . 

 Example 1: 

 Input: nums = [1,4,3,3,2] 
 
 Output: 2 
 
 Explanation: 
 
 The strictly increasing subarrays of nums are [1] , [2] , [3] , [3] , [4] , and [1,4] . 
 
 The strictly decreasing subarrays of nums are [1] , [2] , [3] , [3] , [4] , [3,2] , and [4,3] . 
 
 Hence, we return 2 . 

 Example 2: 

 Input: nums = [3,3,3,3] 
 
 Output: 1 
 
 Explanation: 
 
 The strictly increasing subarrays of nums are [3] , [3] , [3] , and [3] . 
 
 The strictly decreasing subarrays of nums are [3] , [3] , [3] , and [3] . 
 
 Hence, we return 1 . 

 Example 3: 

 Input: nums = [3,2,1] 
 
 Output: 3 
 
 Explanation: 
 
 The strictly increasing subarrays of nums are [3] , [2] , and [1] . 
 
 The strictly decreasing subarrays of nums are [3] , [2] , [1] , [3,2] , [2,1] , and [3,2,1] . 
 
 Hence, we return 3 . 

 Constraints: 

 1 <= nums.length <= 50 
 
 1 <= nums[i] <= 50

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int longestMonotonicSubarray(vector<int>& nums){int inc=1,dec=1,ans=1;for(int i=1;i<(int)nums.size();i++){inc=nums[i]>nums[i-1]?inc+1:1;dec=nums[i]<nums[i-1]?dec+1:1;ans=max(ans,max(inc,dec));}return ans;}};
```


## 3127. Make a Square with the Same Color

**Problem:** https://leetcode.com/problems/make-a-square-with-the-same-color/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Inspect the four 2×2 subgrids of the fixed 3×3 board, counting at most four cells in each.

### Problem description

You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W' . Character 'W' represents the white color , and character 'B' represents the black color . 
 
 Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where all cells are of the same color. 
 
 Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false . 

 Example 1: 

 Input: grid = [["B","W","B"],["B","W","W"],["B","W","B"]] 
 
 Output: true 
 
 Explanation: 
 
 It can be done by changing the color of the grid[0][2] . 

 Example 2: 

 Input: grid = [["B","W","B"],["W","B","W"],["B","W","B"]] 
 
 Output: false 
 
 Explanation: 
 
 It cannot be done by changing at most one cell. 

 Example 3: 

 Input: grid = [["B","W","B"],["B","W","W"],["B","W","W"]] 
 
 Output: true 
 
 Explanation: 
 
 The grid already contains a 2 x 2 square of the same color. 

 Constraints: 

 grid.length == 3 
 
 grid[i].length == 3 
 
 grid[i][j] is either 'W' or 'B' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: bool canMakeSquare(vector<vector<char>>& grid){for(int i=0;i<2;++i)for(int j=0;j<2;++j){int b=0;for(int x=i;x<i+2;++x)for(int y=j;y<j+2;++y)b+=grid[x][y]=='B';if(b!=2)return true;}return false;}};
```


## 3131. Find the Integer Added to Array I

**Problem:** https://leetcode.com/problems/find-the-integer-added-to-array-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Find the minimum in each of the two length-n arrays; their difference is the added integer.

### Problem description

You are given two arrays of equal length, nums1 and nums2 . 
 
 Each element in nums1 has been increased (or decreased in the case of negative) by an integer, represented by the variable x . 
 
 As a result, nums1 becomes equal to nums2 . Two arrays are considered equal when they contain the same integers with the same frequencies. 
 
 Return the integer x . 

 Example 1: 

 Input: nums1 = [2,6,4], nums2 = [9,7,5] 
 
 Output: 3 
 
 Explanation: 
 
 The integer added to each element of nums1 is 3. 

 Example 2: 

 Input: nums1 = [10], nums2 = [5] 
 
 Output: -5 
 
 Explanation: 
 
 The integer added to each element of nums1 is -5. 

 Example 3: 

 Input: nums1 = [1,1,1,1], nums2 = [1,1,1,1] 
 
 Output: 0 
 
 Explanation: 
 
 The integer added to each element of nums1 is 0. 

 Constraints: 

 1 <= nums1.length == nums2.length <= 100 
 
 0 <= nums1[i], nums2[i] <= 1000 
 
 The test cases are generated in a way that there is an integer x such that nums1 can become equal to nums2 by adding x to each element of nums1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int addedInteger(vector<int>& nums1,vector<int>& nums2){return *min_element(nums2.begin(),nums2.end())-*min_element(nums1.begin(),nums1.end());}};
```


## 3142. Check if Grid Satisfies Conditions

**Problem:** https://leetcode.com/problems/check-if-grid-satisfies-conditions/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(1)

**Complexity reasoning:** Check the vertical and horizontal conditions for each grid cell without allocating extra storage.

### Problem description

You are given a 2D matrix grid of size m x n . You need to check if each cell grid[i][j] is: 

 Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists). 
 
 Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists). 

 Return true if all the cells satisfy these conditions, otherwise, return false . 

 Example 1: 

 Input: grid = [[1,0,2],[1,0,2]] 
 
 Output: true 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/04/15/examplechanged.png] 
 
 All the cells in the grid satisfy the conditions. 

 Example 2: 

 Input: grid = [[1,1,1],[0,0,0]] 
 
 Output: false 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/03/27/example21.png] 
 
 All cells in the first row are equal. 

 Example 3: 

 Input: grid = [[1],[2],[3]] 
 
 Output: false 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/03/31/changed.png] 
 
 Cells in the first column have different values. 

 Constraints: 

 1 <= n, m <= 10 
 
 0 <= grid[i][j] <= 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool satisfiesConditions(vector<vector<int>>& grid){int m=grid.size(),n=grid[0].size();for(int i=0;i<m;++i)for(int j=0;j<n;++j){if(i&&grid[i][j]!=grid[i-1][j])return false;if(j&&grid[i][j]==grid[i][j-1])return false;}return true;}};
```


## 3151. Special Array I

**Problem:** https://leetcode.com/problems/special-array-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Compare parity of each adjacent pair, returning early if any pair matches.

### Problem description

An array is considered special if the parity of every pair of adjacent elements is different. In other words, one element in each pair must be even, and the other must be odd. 
 
 You are given an array of integers nums . Return true if nums is a special array, otherwise, return false . 

 Example 1: 

 Input: nums = [1] 
 
 Output: true 
 
 Explanation: 
 
 There is only one element. So the answer is true . 

 Example 2: 

 Input: nums = [2,1,4] 
 
 Output: true 
 
 Explanation: 
 
 There is only two pairs: (2,1) and (1,4) , and both of them contain numbers with different parity. So the answer is true . 

 Example 3: 

 Input: nums = [4,3,1,6] 
 
 Output: false 
 
 Explanation: 
 
 nums[1] and nums[2] are both odd. So the answer is false . 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool isArraySpecial(vector<int>& nums){for(int i=1;i<(int)nums.size();++i)if((nums[i]&1)==(nums[i-1]&1))return false;return true;}};
```


## 3175. Find The First Player to win K Games in a Row

**Problem:** https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Maintain the current champion and win streak while examining each remaining player at most once.

### Problem description

A competition consists of n players numbered from 0 to n - 1 . 
 
 You are given an integer array skills of size n and a positive integer k , where skills[i] is the skill level of player i . All integers in skills are unique . 
 
 All players are standing in a queue in order from player 0 to player n - 1 . 
 
 The competition process is as follows: 

 The first two players in the queue play a game, and the player with the higher skill level wins. 
 
 After the game, the winner stays at the beginning of the queue, and the loser goes to the end of it. 

 The winner of the competition is the first player who wins k games in a row . 
 
 Return the initial index of the winning player. 

 Example 1: 

 Input: skills = [4,2,6,3,9], k = 2 
 
 Output: 2 
 
 Explanation: 
 
 Initially, the queue of players is [0,1,2,3,4] . The following process happens: 

 Players 0 and 1 play a game, since the skill of player 0 is higher than that of player 1, player 0 wins. The resulting queue is [0,2,3,4,1] . 
 
 Players 0 and 2 play a game, since the skill of player 2 is higher than that of player 0, player 2 wins. The resulting queue is [2,3,4,1,0] . 
 
 Players 2 and 3 play a game, since the skill of player 2 is higher than that of player 3, player 2 wins. The resulting queue is [2,4,1,0,3] . 

 Player 2 won k = 2 games in a row, so the winner is player 2. 

 Example 2: 

 Input: skills = [2,5,4], k = 3 
 
 Output: 1 
 
 Explanation: 
 
 Initially, the queue of players is [0,1,2] . The following process happens: 

 Players 0 and 1 play a game, since the skill of player 1 is higher than that of player 0, player 1 wins. The resulting queue is [1,2,0] . 
 
 Players 1 and 2 play a game, since the skill of player 1 is higher than that of player 2, player 1 wins. The resulting queue is [1,0,2] . 
 
 Players 1 and 0 play a game, since the skill of player 1 is higher than that of player 0, player 1 wins. The resulting queue is [1,2,0] . 

 Player 1 won k = 3 games in a row, so the winner is player 1. 

 Constraints: 

 n == skills.length 
 
 2 <= n <= 10 5 
 
 1 <= k <= 10 9 
 
 1 <= skills[i] <= 10 6 
 
 All integers in skills are unique.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int findWinningPlayer(vector<int>& skills,int k){int win=0,champ=0;for(int i=1;i<(int)skills.size();++i){if(skills[champ]>skills[i])++win;else{champ=i;win=1;}if(win>=k)break;}return champ;}};
```


## 3195. Find the Minimum Area to Cover All Ones I

**Problem:** https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(1)

**Complexity reasoning:** Scan every grid cell and maintain minimum and maximum row/column indices containing a 1.

### Problem description

You are given a 2D binary array grid . Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle. 
 
 Return the minimum possible area of the rectangle. 

 Example 1: 

 Input: grid = [[0,1,0],[1,0,1]] 
 
 Output: 6 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png] 
 
 The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6 . 

 Example 2: 

 Input: grid = [[1,0],[0,0]] 
 
 Output: 1 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png] 
 
 The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1 . 

 Constraints: 

 1 <= grid.length, grid[i].length <= 1000 
 
 grid[i][j] is either 0 or 1. 
 
 The input is generated such that there is at least one 1 in grid .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int minimumArea(vector<vector<int>>& grid){int loR=INT_MAX,hiR=-1,loC=INT_MAX,hiC=-1;for(int i=0;i<(int)grid.size();++i)for(int j=0;j<(int)grid[0].size();++j)if(grid[i][j]){loR=min(loR,i);hiR=max(hiR,i);loC=min(loC,j);hiC=max(hiC,j);}return (hiR-loR+1)*(hiC-loC+1);}};
```


## 3197. Find the Minimum Area to Cover All Ones II

**Problem:** https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Matrix, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn(m+n)^2)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Enumerates horizontal, vertical, and mixed three-rectangle partitions; each candidate scans up to O(mn) cells to compute bounding areas.

### Problem description

You are given a 2D binary array grid . You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles. 
 
 Return the minimum possible sum of the area of these rectangles. 
 
 Note that the rectangles are allowed to touch. 

 Example 1: 

 Input: grid = [[1,0,1],[1,1,1]] 
 
 Output: 5 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/05/14/example0rect21.png] 

 The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2. 
 
 The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2. 
 
 The 1 at (1, 1) is covered by a rectangle of area 1. 

 Example 2: 

 Input: grid = [[1,0,1,0],[0,1,0,1]] 
 
 Output: 5 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/05/14/example1rect2.png] 

 The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3. 
 
 The 1 at (1, 1) is covered by a rectangle of area 1. 
 
 The 1 at (1, 3) is covered by a rectangle of area 1. 

 Constraints: 

 1 <= grid.length, grid[i].length <= 30 
 
 grid[i][j] is either 0 or 1. 
 
 The input is generated such that there are at least three 1's in grid .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int minimumSum(vector<vector<int>>& grid){int m=grid.size(),n=grid[0].size();auto area=[&](int r1,int r2,int c1,int c2){int a=m,b=-1,c=n,d=-1;for(int i=r1;i<r2;++i)for(int j=c1;j<c2;++j)if(grid[i][j]){a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j);}return b<0?1000000:(b-a+1)*(d-c+1);};int ans=INT_MAX;for(int i=1;i<m;++i)for(int j=i+1;j<m;++j)ans=min(ans,area(0,i,0,n)+area(i,j,0,n)+area(j,m,0,n));for(int i=1;i<n;++i)for(int j=i+1;j<n;++j)ans=min(ans,area(0,m,0,i)+area(0,m,i,j)+area(0,m,j,n));for(int i=1;i<m;++i)for(int j=1;j<n;++j){ans=min(ans,area(0,i,0,n)+area(i,m,0,j)+area(i,m,j,n));ans=min(ans,area(i,m,0,n)+area(0,i,0,j)+area(0,i,j,n));ans=min(ans,area(0,m,0,j)+area(0,i,j,n)+area(i,m,j,n));ans=min(ans,area(0,m,j,n)+area(0,i,0,j)+area(i,m,0,j));}return ans;}};
```


## 3200. Maximum Height of a Triangle

**Problem:** https://leetcode.com/problems/maximum-height-of-a-triangle/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(sqrt(red+blue))

**Space complexity:** O(1)

**Complexity reasoning:** Each trial consumes rows of increasing size until the available balls run out; two starting colors are tried.

### Problem description

You are given two integers red and blue representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1 st row will have 1 ball, the 2 nd row will have 2 balls, the 3 rd row will have 3 balls, and so on. 
 
 All the balls in a particular row should be the same color, and adjacent rows should have different colors. 
 
 Return the maximum height of the triangle that can be achieved. 

 Example 1: 

 Input: red = 2, blue = 4 
 
 Output: 3 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/06/16/brb.png] 
 
 The only possible arrangement is shown above. 

 Example 2: 

 Input: red = 2, blue = 1 
 
 Output: 2 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/06/16/br.png] 
The only possible arrangement is shown above. 

 Example 3: 

 Input: red = 1, blue = 1 
 
 Output: 1 

 Example 4: 

 Input: red = 10, blue = 1 
 
 Output: 2 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/06/16/br.png] 
The only possible arrangement is shown above. 

 Constraints: 

 1 <= red, blue <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int maxHeightOfTriangle(int red,int blue){auto run=[](int r,int b){int h=0;for(int row=1;;++row){int&v=(row%2?r:b);if(v<row)break;v-=row;++h;}return h;};return max(run(red,blue),run(blue,red));}};
```


## 3285. Find Indices of Stable Mountains

**Problem:** https://leetcode.com/problems/find-indices-of-stable-mountains/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output

**Complexity reasoning:** Checks the previous mountain height for each index and stores qualifying indices.

### Problem description

There are n mountains in a row, and each mountain has a height. You are given an integer array height where height[i] represents the height of mountain i , and an integer threshold . 
 
 A mountain is called stable if the mountain just before it ( if it exists ) has a height strictly greater than threshold . Note that mountain 0 is not stable. 
 
 Return an array containing the indices of all stable mountains in any order. 

 Example 1: 

 Input: height = [1,2,3,4,5], threshold = 2 
 
 Output: [3,4] 
 
 Explanation: 

 Mountain 3 is stable because height[2] == 3 is greater than threshold == 2 . 
 
 Mountain 4 is stable because height[3] == 4 is greater than threshold == 2 . 

 Example 2: 

 Input: height = [10,1,10,1,10], threshold = 3 
 
 Output: [1,3] 

 Example 3: 

 Input: height = [10,1,10,1,10], threshold = 10 
 
 Output: [] 

 Constraints: 

 2 <= n == height.length <= 100 
 
 1 <= height[i] <= 100 
 
 1 <= threshold <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: vector<int> stableMountains(vector<int>&height,int threshold){vector<int>a;for(int i=1;i<(int)height.size();++i)if(height[i-1]>threshold)a.push_back(i);return a;} };
```


## 3349. Adjacent Increasing Subarrays Detection I

**Problem:** https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(nk)

**Space complexity:** O(1)

**Complexity reasoning:** Tries every starting position and checks up to 2(k-1) adjacent pairs for its two length-k segments.

### Problem description

Given an array nums of n integers and an integer k , determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing . Specifically, check if there are two subarrays starting at indices a and b ( a < b ), where: 

 Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing . 
 
 The subarrays must be adjacent , meaning b = a + k . 

 Return true if it is possible to find two such subarrays, and false otherwise. 

 Example 1: 

 Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3 
 
 Output: true 
 
 Explanation: 

 The subarray starting at index 2 is [7, 8, 9] , which is strictly increasing. 
 
 The subarray starting at index 5 is [2, 3, 4] , which is also strictly increasing. 
 
 These two subarrays are adjacent, so the result is true . 

 Example 2: 

 Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5 
 
 Output: false 

 Constraints: 

 2 <= nums.length <= 100 
 
 1 < 2 * k <= nums.length 
 
 -1000 <= nums[i] <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool hasIncreasingSubarrays(vector<int>& nums,int k){int n=nums.size();for(int i=0;i+2*k<=n;i++){bool ok=true;for(int j=i+1;j<i+k;j++)if(nums[j]<=nums[j-1])ok=false;for(int j=i+k+1;j<i+2*k;j++)if(nums[j]<=nums[j-1])ok=false;if(ok)return true;}return false;}};
```


## 3353. Minimum Total Operations

**Problem:** https://leetcode.com/problems/minimum-total-operations/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Counts adjacent unequal pairs in a single pass.

### Problem description

Given an array of integers nums , you can perform any number of operations on this array. 
 
 In each operation , you can: 

 Choose a prefix of the array. 
 
 Choose an integer k (which can be negative) and add k to each element in the chosen prefix. 

 A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it. 
 
 Return the minimum number of operations required to make all elements in arr equal. 

 Example 1: 

 Input: nums = [1,4,2] 
 
 Output: 2 
 
 Explanation: 

 Operation 1 : Choose the prefix [1, 4] of length 2 and add -2 to each element of the prefix. The array becomes [-1, 2, 2] . 
 
 Operation 2 : Choose the prefix [-1] of length 1 and add 3 to it. The array becomes [2, 2, 2] . 
 
 Thus, the minimum number of required operations is 2. 

 Example 2: 

 Input: nums = [10,10,10] 
 
 Output: 0 
 
 Explanation: 

 All elements are already equal, so no operations are needed. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 -10 9 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int ans = 0;
        for (int i = 1; i < (int)nums.size(); ++i) {
            if (nums[i] != nums[i - 1]) ++ans;
        }
        return ans;
    }
};
```


## 3379. Transformed Array

**Problem:** https://leetcode.com/problems/transformed-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output

**Complexity reasoning:** Computes one modular destination index and writes one result for every element.

### Problem description

You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules: 
For each index i (where 0 <= i < nums.length ), perform the following independent actions:

 If nums[i] > 0 : Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value at the index where you land. 
 
 If nums[i] < 0 : Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value at the index where you land. 
 
 If nums[i] == 0 : Set result[i] to nums[i] . 

 Return the new array result . 
 
 Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end. 

 Example 1: 

 Input: nums = [3,-2,1,1] 
 
 Output: [1,1,1,3] 
 
 Explanation: 

 For nums[0] that is equal to 3, If we move 3 steps to right, we reach nums[3] . So result[0] should be 1. 
 
 For nums[1] that is equal to -2, If we move 2 steps to left, we reach nums[3] . So result[1] should be 1. 
 
 For nums[2] that is equal to 1, If we move 1 step to right, we reach nums[3] . So result[2] should be 1. 
 
 For nums[3] that is equal to 1, If we move 1 step to right, we reach nums[0] . So result[3] should be 3. 

 Example 2: 

 Input: nums = [-1,4,-1] 
 
 Output: [-1,-1,4] 
 
 Explanation: 

 For nums[0] that is equal to -1, If we move 1 step to left, we reach nums[2] . So result[0] should be -1. 
 
 For nums[1] that is equal to 4, If we move 4 steps to right, we reach nums[2] . So result[1] should be -1. 
 
 For nums[2] that is equal to -1, If we move 1 step to left, we reach nums[1] . So result[2] should be 4. 

 Constraints: 

 1 <= nums.length <= 100 
 
 -100 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int>constructTransformedArray(vector<int>&nums){int n=nums.size();vector<int>a(n);for(int i=0;i<n;i++)a[i]=nums[((i+nums[i])%n+n)%n];return a;}};
```


## 3386. Button with Longest Push Time

**Problem:** https://leetcode.com/problems/button-with-longest-push-time/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Scans each event once, tracking the previous timestamp and best duration.

### Problem description

You are given a 2D array events which represents a sequence of events where a child pushes a series of buttons on a keyboard. 
 
 Each events[i] = [index i , time i ] indicates that the button at index index i was pressed at time time i . 

 The array is sorted in increasing order of time . 
 
 The time taken to press a button is the difference in time between consecutive button presses. The time for the first button is simply the time at which it was pressed. 

 Return the index of the button that took the longest time to push. If multiple buttons have the same longest time, return the button with the smallest index . 

 Example 1: 

 Input: events = [[1,2],[2,5],[3,9],[1,15]] 
 
 Output: 1 
 
 Explanation: 

 Button with index 1 is pressed at time 2. 
 
 Button with index 2 is pressed at time 5, so it took 5 - 2 = 3 units of time. 
 
 Button with index 3 is pressed at time 9, so it took 9 - 5 = 4 units of time. 
 
 Button with index 1 is pressed again at time 15, so it took 15 - 9 = 6 units of time. 

 Example 2: 

 Input: events = [[10,5],[1,7]] 
 
 Output: 10 
 
 Explanation: 

 Button with index 10 is pressed at time 5. 
 
 Button with index 1 is pressed at time 7, so it took 7 - 5 = 2 units of time. 

 Constraints: 

 1 <= events.length <= 1000 
 
 events[i] == [index i , time i ] 
 
 1 <= index i , time i <= 10 5 
 
 The input is generated such that events is sorted in increasing order of time i .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int buttonWithLongestTime(vector<vector<int>>&events){int prev=0,best=-1,ans=INT_MAX;for(auto&e:events){int d=e[1]-prev;prev=e[1];if(d>best||(d==best&&e[0]<ans)){best=d;ans=e[0];}}return ans;}};
```


## 3392. Count Subarrays of Length Three With a Condition

**Problem:** https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Checks the fixed three-element condition at each possible ending index.

### Problem description

Given an integer array nums , return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number. 

 Example 1: 

 Input: nums = [1,2,1,4,1] 
 
 Output: 1 
 
 Explanation: 
 
 Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number. 

 Example 2: 

 Input: nums = [1,1,1] 
 
 Output: 0 
 
 Explanation: 
 
 [1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number. 

 Constraints: 

 3 <= nums.length <= 100 
 
 -100 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int countSubarrays(vector<int>&nums){int ans=0;for(int i=2;i<(int)nums.size();i++)ans+=(nums[i-2]+nums[i]==nums[i-1]/2&&nums[i-1]%2==0);return ans;}};
```


## 3417. Zigzag Grid Traversal With Skip

**Problem:** https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn) output

**Complexity reasoning:** Visits each grid cell once in alternating row directions, retaining every other value.

### Problem description

You are given an m x n 2D array grid of positive integers. 
 
 Your task is to traverse grid in a zigzag pattern while skipping every alternate cell. 
 
 Zigzag pattern traversal is defined as following the below actions: 

 Start at the top-left cell (0, 0) . 
 
 Move right within a row until the end of the row is reached. 
 
 Drop down to the next row, then traverse left until the beginning of the row is reached. 
 
 Continue alternating between right and left traversal until every row has been traversed. 

 Note that you must skip every alternate cell during the traversal. 
 
 Return an array of integers result containing, in order , the value of the cells visited during the zigzag traversal with skips. 

 Example 1: 

 Input: grid = [[1,2],[3,4]] 
 
 Output: [1,4] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/11/23/4012_example0.png] 

 Example 2: 

 Input: grid = [[2,1],[2,1],[2,1]] 
 
 Output: [2,1,2] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/11/23/4012_example1.png] 

 Example 3: 

 Input: grid = [[1,2,3],[4,5,6],[7,8,9]] 
 
 Output: [1,3,5,7,9] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/11/23/4012_example2.png] 

 Constraints: 

 2 <= n == grid.length <= 50 
 
 2 <= m == grid[i].length <= 50 
 
 1 <= grid[i][j] <= 2500

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int>zigzagTraversal(vector<vector<int>>&grid){vector<int>ans;int m=grid.size(),n=grid[0].size(),step=0;for(int i=0;i<m;i++)for(int t=0;t<n;t++){int j=i%2?n-1-t:t;if(step++%2==0)ans.push_back(grid[i][j]);}return ans;}};
```


## 3423. Maximum Difference Between Adjacent Elements in a Circular Array

**Problem:** https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Checks each circular neighboring pair once.

### Problem description

Given a circular array nums , find the maximum absolute difference between adjacent elements. 
 
 Note : In a circular array, the first and last elements are adjacent. 

 Example 1: 

 Input: nums = [1,2,4] 
 
 Output: 3 
 
 Explanation: 
 
 Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3 . 

 Example 2: 

 Input: nums = [-5,-10,-5] 
 
 Output: 5 
 
 Explanation: 
 
 The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5 . 

 Constraints: 

 2 <= nums.length <= 100 
 
 -100 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int maxAdjacentDistance(vector<int>& nums) {
 int ans=0,n=nums.size(); for(int i=0;i<n;++i) ans=max(ans,abs(nums[i]-nums[(i+1)%n])); return ans;
}};
```


## 3452. Sum of Good Numbers

**Problem:** https://leetcode.com/problems/sum-of-good-numbers/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Checks at most two positions k away for every array element.

### Problem description

Given an array of integers nums and an integer k , an element nums[i] is considered good if it is strictly greater than the elements at indices i - k and i + k (if those indices exist). If neither of these indices exists , nums[i] is still considered good . 
 
 Return the sum of all the good elements in the array. 

 Example 1: 

 Input: nums = [1,3,2,1,5,4], k = 2 
 
 Output: 12 
 
 Explanation: 
 
 The good numbers are nums[1] = 3 , nums[4] = 5 , and nums[5] = 4 because they are strictly greater than the numbers at indices i - k and i + k . 

 Example 2: 

 Input: nums = [2,1], k = 1 
 
 Output: 2 
 
 Explanation: 
 
 The only good number is nums[0] = 2 because it is strictly greater than nums[1] . 

 Constraints: 

 2 <= nums.length <= 100 
 
 1 <= nums[i] <= 1000 
 
 1 <= k <= floor(nums.length / 2)

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int sumOfGoodNumbers(vector<int>& nums,int k){int ans=0,n=nums.size();for(int i=0;i<n;++i)if((i<k||nums[i]>nums[i-k])&&(i+k>=n||nums[i]>nums[i+k]))ans+=nums[i];return ans;}};
```


## 3502. Minimum Cost to Reach Every Position

**Problem:** https://leetcode.com/problems/minimum-cost-to-reach-every-position/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output

**Complexity reasoning:** Maintains the running minimum and appends it once per input cost.

### Problem description

You are given an integer array cost of size n . You are currently at position n (at the end of the line) in a line of n + 1 people (numbered from 0 to n ). 
 
 You wish to move forward in the line, but each person in front of you charges a specific amount to swap places. The cost to swap with person i is given by cost[i] . 
 
 You are allowed to swap places with people as follows: 

 If they are in front of you, you must pay them cost[i] to swap with them. 
 
 If they are behind you, they can swap with you for free. 

 Return an array answer of size n , where answer[i] is the minimum total cost to reach each position i in the line . 

 Example 1: 

 Input: cost = [5,3,4,1,3,2] 
 
 Output: [5,3,3,1,1,1] 
 
 Explanation: 
 
 We can get to each position in the following way: 

 i = 0 . We can swap with person 0 for a cost of 5. 
 
 i = 1 . We can swap with person 1 for a cost of 3. 
 
 i = 2 . We can swap with person 1 for a cost of 3, then swap with person 2 for free. 
 
 i = 3 . We can swap with person 3 for a cost of 1. 
 
 i = 4 . We can swap with person 3 for a cost of 1, then swap with person 4 for free. 
 
 i = 5 . We can swap with person 3 for a cost of 1, then swap with person 5 for free. 

 Example 2: 

 Input: cost = [1,2,4,6,7] 
 
 Output: [1,1,1,1,1] 
 
 Explanation: 
 
 We can swap with person 0 for a cost of 1, then we will be able to reach any position i for free. 

 Constraints: 

 1 <= n == cost.length <= 100 
 
 1 <= cost[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int> minCosts(vector<int>&cost){vector<int>a;int best=INT_MAX;for(int x:cost){best=min(best,x);a.push_back(best);}return a;}};
```


## 3565. Sequential Grid Path Cover

**Problem:** https://leetcode.com/problems/sequential-grid-path-cover/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Recursion, Matrix

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(N·3^N) worst case, N=mn

**Space complexity:** O(N) auxiliary

**Complexity reasoning:** Starts DFS from up to N cells and backtracks over unvisited neighbors (at most three after the first step); recursion and the current path use O(N) memory.

### Problem description

You are given a 2D array grid of size m x n , and an integer k . There are k cells in grid containing the values from 1 to k exactly once , and the rest of the cells have a value 0. 
 
 You can start at any cell, and move from a cell to its neighbors (up, down, left, or right). You must find a path in grid which: 

 Visits each cell in grid exactly once . 
 
 Visits the cells with values from 1 to k in order . 

 Return a 2D array result of size (m * n) x 2 , where result[i] = [x i , y i ] represents the i th cell visited in the path. If there are multiple such paths, you may return any one. 
 
 If no such path exists, return an empty array. 

 Example 1: 

 Input: grid = [[0,0,0],[0,1,2]], k = 2 
 
 Output: [[0,0],[1,0],[1,1],[1,2],[0,2],[0,1]] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2025/05/16/ezgifcom-animated-gif-maker1.gif] 

 Example 2: 

 Input: grid = [[1,0,4],[3,0,2]], k = 4 
 
 Output: [] 
 
 Explanation: 
 
 There is no possible path that satisfies the conditions. 

 Constraints: 

 1 <= m == grid.length <= 5 
 
 1 <= n == grid[i].length <= 5 
 
 1 <= k <= m * n 
 
 0 <= grid[i][j] <= k 
 
 grid contains all integers between 1 and k exactly once.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    int m,n,k;
    vector<vector<int>> *g;
    vector<vector<int>> path;
    const int dx[4]={1,-1,0,0},dy[4]={0,0,1,-1};
    bool dfs(int x,int y,unsigned int mask,int next) {
        path.push_back({x,y});
        if((int)path.size()==m*n) return next==k+1;
        for(int d=0;d<4;++d) {
            int a=x+dx[d],b=y+dy[d];
            if(a<0||a>=m||b<0||b>=n) continue;
            int id=a*n+b;
            if(mask&(1u<<id)) continue;
            int val=(*g)[a][b];
            if(val && val!=next) continue;
            if(dfs(a,b,mask|(1u<<id),next+(val!=0))) return true;
        }
        path.pop_back();return false;
    }
public:
    vector<vector<int>> findPath(vector<vector<int>>& grid,int K) {
        g=&grid;m=grid.size();n=grid[0].size();k=K;
        for(int i=0;i<m;++i) for(int j=0;j<n;++j)
            if((grid[i][j]==0||grid[i][j]==1) && dfs(i,j,1u<<(i*n+j),grid[i][j]==1?2:1)) return path;
        return {};
    }
};
```


## 3616. Number of Student Replacements

**Problem:** https://leetcode.com/problems/number-of-student-replacements/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Maintains the smallest rank encountered during a single traversal.

### Problem description

You are given an integer array ranks where ranks[i] represents the rank of the i th student arriving in order . A lower number indicates a better rank. 
 
 Initially, the first student is selected by default. 
 
 A replacement occurs when a student with a strictly better rank arrives and replaces the current selection. 
 
 Return the total number of replacements made. 

 Example 1: 

 Input: ranks = [4,1,2] 
 
 Output: 1 
 
 Explanation: 

 The first student with ranks[0] = 4 is initially selected. 
 
 The second student with ranks[1] = 1 is better than the current selection, so a replacement occurs. 
 
 The third student has a worse rank, so no replacement occurs. 
 
 Thus, the number of replacements is 1. 

 Example 2: 

 Input: ranks = [2,2,3] 
 
 Output: 0 
 
 Explanation: 

 The first student with ranks[0] = 2 is initially selected. 
 
 Neither of ranks[1] = 2 or ranks[2] = 3 is better than the current selection. 
 
 Thus, the number of replacements is 0. 

 Constraints: 

 1 <= ranks.length <= 10 5 ​​​​​​​ 
 
 1 <= ranks[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int totalReplacements(vector<int>& ranks) {
        int best = ranks[0], ans = 0;
        for (int x : ranks) {
            if (x < best) {
                best = x;
                ++ans;
            }
        }
        return ans;
    }
};
```


## 3637. Trionic Array I

**Problem:** https://leetcode.com/problems/trionic-array-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Advances one index across three consecutive monotonic runs without revisiting elements.

### Problem description

You are given an integer array nums of length n . 
 
 An array is trionic if there exist indices 0 < p < q < n − 1 such that: 

 nums[0...p] is strictly increasing, 
 
 nums[p...q] is strictly decreasing, 
 
 nums[q...n − 1] is strictly increasing. 

 Return true if nums is trionic, otherwise return false . 

 Example 1: 

 Input: nums = [1,3,5,4,2,6] 
 
 Output: true 
 
 Explanation: 
 
 Pick p = 2 , q = 4 : 

 nums[0...2] = [1, 3, 5] is strictly increasing ( 1 < 3 < 5 ). 
 
 nums[2...4] = [5, 4, 2] is strictly decreasing ( 5 > 4 > 2 ). 
 
 nums[4...5] = [2, 6] is strictly increasing ( 2 < 6 ). 

 Example 2: 

 Input: nums = [2,1,3] 
 
 Output: false 
 
 Explanation: 
 
 There is no way to pick p and q to form the required three segments. 

 Constraints: 

 3 <= n <= 100 
 
 -1000 <= nums[i] <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 bool isTrionic(vector<int>& nums){int n=nums.size(),i=1;while(i<n&&nums[i]>nums[i-1])++i;if(i==1||i==n)return false;int p=i;while(i<n&&nums[i]<nums[i-1])++i;if(i==p||i==n)return false;p=i;while(i<n&&nums[i]>nums[i-1])++i;return i==n&&i>p;}
};
```


## 3683. Earliest Time to Finish One Task

**Problem:** https://leetcode.com/problems/earliest-time-to-finish-one-task/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Evaluates each task’s start plus duration once.

### Problem description

You are given a 2D integer array tasks where tasks[i] = [s i , t i ] . 
 
 Each [s i , t i ] in tasks represents a task with start time s i that takes t i units of time to finish. 
 
 Return the earliest time at which at least one task is finished. 

 Example 1: 

 Input: tasks = [[1,6],[2,3]] 
 
 Output: 5 
 
 Explanation: 
 
 The first task starts at time t = 1 and finishes at time 1 + 6 = 7 . The second task finishes at time 2 + 3 = 5 . You can finish one task at time 5. 

 Example 2: 

 Input: tasks = [[100,100],[100,100],[100,100]] 
 
 Output: 200 
 
 Explanation: 
 
 All three tasks finish at time 100 + 100 = 200 . 

 Constraints: 

 1 <= tasks.length <= 100 
 
 tasks[i] = [s i , t i ] 
 
 1 <= s i , t i <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int earliestTime(vector<vector<int>>& tasks){int ans=INT_MAX;for(auto&t:tasks)ans=min(ans,t[0]+t[1]);return ans;} };
```


## 3687. Library Late Fee Calculator

**Problem:** https://leetcode.com/problems/library-late-fee-calculator/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Adds the applicable constant-time fee for each day-late value.

### Problem description

You are given an integer array daysLate where daysLate[i] indicates how many days late the i th book was returned. 
 
 The penalty is calculated as follows: 

 If daysLate[i] == 1 , penalty is 1. 
 
 If 2 <= daysLate[i] <= 5 , penalty is 2 * daysLate[i] . 
 
 If daysLate[i] > 5 , penalty is 3 * daysLate[i] . 

 Return the total penalty for all books. 

 Example 1: 

 Input: daysLate = [5,1,7] 
 
 Output: 32 
 
 Explanation: 

 daysLate[0] = 5 : Penalty is 2 * daysLate[0] = 2 * 5 = 10 . 
 
 daysLate[1] = 1 : Penalty is 1 . 
 
 daysLate[2] = 7 : Penalty is 3 * daysLate[2] = 3 * 7 = 21 . 
 
 Thus, the total penalty is 10 + 1 + 21 = 32 . 

 Example 2: 

 Input: daysLate = [1,1] 
 
 Output: 2 
 
 Explanation: 

 daysLate[0] = 1 : Penalty is 1 . 
 
 daysLate[1] = 1 : Penalty is 1 . 
 
 Thus, the total penalty is 1 + 1 = 2 . 

 Constraints: 

 1 <= daysLate.length <= 100 
 
 1 <= daysLate[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int lateFee(vector<int>& daysLate) {
        int total = 0;
        for (int d : daysLate) total += d == 1 ? 1 : (d <= 5 ? 2 * d : 3 * d);
        return total;
    }
};
```


## 3701. Compute Alternating Sum

**Problem:** https://leetcode.com/problems/compute-alternating-sum/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Accumulates values with alternating signs in one loop.

### Problem description

You are given an integer array nums . 
 
 The alternating sum of nums is the value obtained by adding elements at even indices and subtracting elements at odd indices. That is, nums[0] - nums[1] + nums[2] - nums[3]... 
 
 Return an integer denoting the alternating sum of nums . 

 Example 1: 

 Input: nums = [1,3,5,7] 
 
 Output: -4 
 
 Explanation: 

 Elements at even indices are nums[0] = 1 and nums[2] = 5 because 0 and 2 are even numbers. 
 
 Elements at odd indices are nums[1] = 3 and nums[3] = 7 because 1 and 3 are odd numbers. 
 
 The alternating sum is nums[0] - nums[1] + nums[2] - nums[3] = 1 - 3 + 5 - 7 = -4 . 

 Example 2: 

 Input: nums = [100] 
 
 Output: 100 
 
 Explanation: 

 The only element at even indices is nums[0] = 100 because 0 is an even number. 
 
 There are no elements on odd indices. 
 
 The alternating sum is nums[0] = 100 . 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public: int alternatingSum(vector<int>& nums) {int s=0;for(int i=0;i<(int)nums.size();++i)s+=(i%2?-nums[i]:nums[i]);return s;}};
```


## 3708. Longest Fibonacci Subarray

**Problem:** https://leetcode.com/problems/longest-fibonacci-subarray/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Checks each consecutive triple once and updates the current Fibonacci-like run length.

### Problem description

You are given an array of positive integers nums . 
 
 A Fibonacci array is a contiguous sequence whose third and subsequent terms each equal the sum of the two preceding terms. 
 
 Return the length of the longest Fibonacci subarray in nums . 
 
 Note: Subarrays of length 1 or 2 are always Fibonacci . 

 Example 1: 

 Input: nums = [1,1,1,1,2,3,5,1] 
 
 Output: 5 
 
 Explanation: 
 
 The longest Fibonacci subarray is nums[2..6] = [1, 1, 2, 3, 5] . 
 
 [1, 1, 2, 3, 5] is Fibonacci because 1 + 1 = 2 , 1 + 2 = 3 , and 2 + 3 = 5 . 

 Example 2: 

 Input: nums = [5,2,7,9,16] 
 
 Output: 5 
 
 Explanation: 
 
 The longest Fibonacci subarray is nums[0..4] = [5, 2, 7, 9, 16] . 
 
 [5, 2, 7, 9, 16] is Fibonacci because 5 + 2 = 7 , 2 + 7 = 9 , and 7 + 9 = 16 . 

 Example 3: 

 Input: nums = [1000000000,1000000000,1000000000] 
 
 Output: 2 
 
 Explanation: 
 
 The longest Fibonacci subarray is nums[1..2] = [1000000000, 1000000000] . 
 
 [1000000000, 1000000000] is Fibonacci because its length is 2. 

 Constraints: 

 3 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size(), run = 2, best = min(n, 2);
        for (int i = 2; i < n; ++i) {
            if (1LL * nums[i - 2] + nums[i - 1] == nums[i]) ++run;
            else run = 2;
            best = max(best, run);
        }
        return best;
    }
};
```


## 3809. Best Reachable Tower

**Problem:** https://leetcode.com/problems/best-reachable-tower/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(t)

**Space complexity:** O(1)

**Complexity reasoning:** Checks Manhattan distance and quality for each tower; the position vectors have fixed length two.

### Problem description

You are given a 2D integer array towers , where towers[i] = [x i , y i , q i ] represents the coordinates (x i , y i ) and quality factor q i of the i th tower. 
 
 You are also given an integer array center = [cx, cy​​​​​​​] representing your location, and an integer radius . 
 
 A tower is reachable if its Manhattan distance from center is less than or equal to radius . 
 
 Among all reachable towers: 

 Return the coordinates of the tower with the maximum quality factor. 
 
 If there is a tie, return the tower with the lexicographically smallest coordinate. If no tower is reachable, return [-1, -1] . 
 
The Manhattan Distance between two cells (x i , y i ) and (x j , y j ) is |x i - x j | + |y i - y j | .

 A coordinate [x i , y i ] is lexicographically smaller than [x j , y j ] if x i < x j , or x i == x j and y i < y j . 
 
 |x| denotes the absolute value of x . 

 Example 1: 

 Input: towers = [[1,2,5], [2,1,7], [3,1,9]], center = [1,1], radius = 2 
 
 Output: [3,1] 
 
 Explanation: 

 Tower [1, 2, 5] : Manhattan distance = |1 - 1| + |2 - 1| = 1 , reachable. 
 
 Tower [2, 1, 7] : Manhattan distance = |2 - 1| + |1 - 1| = 1 , reachable. 
 
 Tower [3, 1, 9] : Manhattan distance = |3 - 1| + |1 - 1| = 2 , reachable. 

 All towers are reachable. The maximum quality factor is 9, which corresponds to tower [3, 1] . 

 Example 2: 

 Input: towers = [[1,3,4], [2,2,4], [4,4,7]], center = [0,0], radius = 5 
 
 Output: [1,3] 
 
 Explanation: 

 Tower [1, 3, 4] : Manhattan distance = |1 - 0| + |3 - 0| = 4 , reachable. 
 
 Tower [2, 2, 4] : Manhattan distance = |2 - 0| + |2 - 0| = 4 , reachable. 
 
 Tower [4, 4, 7] : Manhattan distance = |4 - 0| + |4 - 0| = 8 , not reachable. 

 Among the reachable towers, the maximum quality factor is 4. Both [1, 3] and [2, 2] have the same quality, so the lexicographically smaller coordinate is [1, 3] . 

 Example 3: 

 Input: towers = [[5,6,8], [0,3,5]], center = [1,2], radius = 1 
 
 Output: [-1,-1] 
 
 Explanation: 

 Tower [5, 6, 8] : Manhattan distance = |5 - 1| + |6 - 2| = 8 , not reachable. 
 
 Tower [0, 3, 5] : Manhattan distance = |0 - 1| + |3 - 2| = 2 , not reachable. 

 No tower is reachable within the given radius, so [-1, -1] is returned. 

 Constraints: 

 1 <= towers.length <= 10 5 
 
 towers[i] = [x i , y i , q i ] 
 
 center = [cx, cy] 
 
 0 <= x i , y i , q i , cx, cy <= 10 5 ​​​​​​​ 
 
 0 <= radius <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> bestTower(vector<vector<int>>& towers, vector<int>& center, int radius) {
        int bestQ = -1;
        vector<int> ans = {-1, -1};
        for (auto &t : towers) {
            int dist = abs(t[0] - center[0]) + abs(t[1] - center[1]);
            vector<int> pos = {t[0], t[1]};
            if (dist <= radius && (t[2] > bestQ || (t[2] == bestQ && pos < ans))) {
                bestQ = t[2]; ans = pos;
            }
        }
        return ans;
    }
};
```


## 3818. Minimum Prefix Removal to Make Array Strictly Increasing

**Problem:** https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Walks backward through the strictly increasing suffix until the first violation.

### Problem description

You are given an integer array nums . 
 
 You need to remove exactly one prefix (possibly empty) from nums. 
 
 Return an integer denoting the minimum length of the removed prefix such that the remaining array is strictly increasing . 

 Example 1: 

 Input: nums = [1,-1,2,3,3,4,5] 
 
 Output: 4 
 
 Explanation: 
 
 Removing the prefix = [1, -1, 2, 3] leaves the remaining array [3, 4, 5] which is strictly increasing. 

 Example 2: 

 Input: nums = [4,3,-2,-5] 
 
 Output: 3 
 
 Explanation: 
 
 Removing the prefix = [4, 3, -2] leaves the remaining array [-5] which is strictly increasing. 

 Example 3: 

 Input: nums = [1,2,3,4] 
 
 Output: 0 
 
 Explanation: 
 
 The array nums = [1, 2, 3, 4] is already strictly increasing so removing an empty prefix is sufficient. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 -10 9 <= nums[i] <= 10 9 ​​​​​​​

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int minimumPrefixLength(vector<int>& nums) {
        int i=(int)nums.size()-1;
        while(i>0&&nums[i-1]<nums[i]) --i;
        return i;
    }
};
```


## 3819. Rotate Non Negative Elements

**Problem:** https://leetcode.com/problems/rotate-non-negative-elements/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Collects nonnegative values, copies the input, then fills eligible positions with rotated values.

### Problem description

You are given an integer array nums and an integer k . 
 
 Rotate only the non-negative elements of the array to the left by k positions, in a cyclic manner. 
 
 All negative elements must stay in their original positions and must not move. 
 
 After rotation, place the non-negative elements back into the array in the new order, filling only the positions that originally contained non-negative values and skipping all negative positions. 
 
 Return the resulting array. 

 Example 1: 

 Input: nums = [1,-2,3,-4], k = 3 
 
 Output: [3,-2,1,-4] 
 
 Explanation: ​​​​​​​ 

 The non-negative elements, in order, are [1, 3] . 
 
 Left rotation with k = 3 results in:

 [1, 3] -> [3, 1] -> [1, 3] -> [3, 1] 

 Placing them back into the non-negative indices results in [3, -2, 1, -4] . 

 Example 2: 

 Input: nums = [-3,-2,7], k = 1 
 
 Output: [-3,-2,7] 
 
 Explanation: 

 The non-negative elements, in order, are [7] . 
 
 Left rotation with k = 1 results in [7] . 
 
 Placing them back into the non-negative indices results in [-3, -2, 7] . 

 Example 3: 

 Input: nums = [5,4,-9,6], k = 2 
 
 Output: [6,5,-9,4] 
 
 Explanation: 

 The non-negative elements, in order, are [5, 4, 6] . 
 
 Left rotation with k = 2 results in [6, 5, 4] . 
 
 Placing them back into the non-negative indices results in [6, 5, -9, 4] . 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 -10 5 <= nums[i] <= 10 5 
 
 0 <= k <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> rotateElements(vector<int>& nums, int k) {
        vector<int> vals;
        for (int x : nums) if (x >= 0) vals.push_back(x);
        int m = vals.size();
        if (m == 0) return nums;
        k %= m;
        vector<int> ans = nums;
        int j = 0;
        for (int i = 0; i < (int)nums.size(); ++i)
            if (nums[i] >= 0) ans[i] = vals[(j++ + k) % m];
        return ans;
    }
};
```


## 3833. Count Dominant Indices

**Problem:** https://leetcode.com/problems/count-dominant-indices/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Traverses backward while maintaining the suffix sum and count.

### Problem description

You are given an integer array nums of length n . 
 
 An element at index i is called dominant if: nums[i] > average(nums[i + 1], nums[i + 2], ..., nums[n - 1]) 
 
 Your task is to count the number of indices i that are dominant . 
 
 The average of a set of numbers is the value obtained by adding all the numbers together and dividing the sum by the total number of numbers. 
 
 Note : The rightmost element of any array is not dominant . 

 Example 1: 

 Input: nums = [5,4,3] 
 
 Output: 2 
 
 Explanation: 

 At index i = 0 , the value 5 is dominant as 5 > average(4, 3) = 3.5 . 
 
 At index i = 1 , the value 4 is dominant over the subarray [3] . 
 
 Index i = 2 is not dominant as there are no elements to its right. Thus, the answer is 2. 

 Example 2: 

 Input: nums = [4,1,2] 
 
 Output: 1 
 
 Explanation: 

 At index i = 0 , the value 4 is dominant over the subarray [1, 2] . 
 
 At index i = 1 , the value 1 is not dominant. 
 
 Index i = 2 is not dominant as there are no elements to its right. Thus, the answer is 1. 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100 ​​​​​​​

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int dominantIndices(vector<int>& nums) {
        long long suffix = 0;
        int ans = 0;
        for (int i = (int)nums.size() - 1; i >= 0; --i) {
            int count = (int)nums.size() - 1 - i;
            if (count && (long long)nums[i] * count > suffix) ++ans;
            suffix += nums[i];
        }
        return ans;
    }
};
```


## 3847. Find the Score Difference in a Game

**Problem:** https://leetcode.com/problems/find-the-score-difference-in-a-game/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Simulates each turn with constant-time parity toggles and score updates.

### Problem description

You are given an integer array nums , where nums[i] represents the points scored in the i th game. 
 
 There are exactly two players. Initially, the first player is active and the second player is inactive . 
 
 The following rules apply sequentially for each game i : 

 If nums[i] is odd, the active and inactive players swap roles. 
 
 In every 6th game (that is, game indices 5, 11, 17, ... ), the active and inactive players swap roles. 
 
 The active player plays the i th game and gains nums[i] points. 

 Return the score difference , defined as the first player's total score minus the second player's total score. 

 Example 1: 

 Input: nums = [1,2,3] 
 
 Output: 0 
 
 Explanation: ​​​​​​​ 

 Game 0: Since the points are odd, the second player becomes active and gains nums[0] = 1 point. 
 
 Game 1: No swap occurs. The second player gains nums[1] = 2 points. 
 
 Game 2: Since the points are odd, the first player becomes active and gains nums[2] = 3 points. 
 
 The score difference is 3 - 3 = 0 . 

 Example 2: 

 Input: nums = [2,4,2,1,2,1] 
 
 Output: 4 
 
 Explanation: 

 Games 0 to 2: The first player gains 2 + 4 + 2 = 8 points. 
 
 Game 3: Since the points are odd, the second player is now active and gains nums[3] = 1 point. 
 
 Game 4: The second player gains nums[4] = 2 points. 
 
 Game 5: Since the points are odd, the players swap roles. Then, because this is the 6th game, the players swap again. The second player gains nums[5] = 1 point. 
 
 The score difference is 8 - 4 = 4 . 

 Example 3: 

 Input: nums = [1] 
 
 Output: -1 
 
 Explanation: 

 Game 0: Since the points are odd, the second player is now active and gains nums[0] = 1 point. 
 
 The score difference is 0 - 1 = -1 . 

 Constraints: 

 1 <= nums.length <= 1000 
 
 1 <= nums[i] <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int scoreDifference(vector<int>& nums) {
        bool firstActive = true;
        int difference = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] % 2 != 0) firstActive = !firstActive;
            if ((i + 1) % 6 == 0) firstActive = !firstActive;
            difference += firstActive ? nums[i] : -nums[i];
        }
        return difference;
    }
};
```


## 3861. Minimum Capacity Box

**Problem:** https://leetcode.com/problems/minimum-capacity-box/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Scans capacities once and keeps the smallest eligible capacity’s index.

### Problem description

You are given an integer array capacity , where capacity[i] represents the capacity of the i th box, and an integer itemSize representing the size of an item. 
 
 The i th box can store the item if capacity[i] >= itemSize . 
 
 Return an integer denoting the index of the box with the minimum capacity that can store the item. If multiple such boxes exist, return the smallest index . 
 
 If no box can store the item, return -1. 

 Example 1: 

 Input: capacity = [1,5,3,7], itemSize = 3 
 
 Output: 2 
 
 Explanation: 
 
 The box at index 2 has a capacity of 3, which is the minimum capacity that can store the item. Thus, the answer is 2. 

 Example 2: 

 Input: capacity = [3,5,4,3], itemSize = 2 
 
 Output: 0 
 
 Explanation: 
 
 The minimum capacity that can store the item is 3, and it appears at indices 0 and 3. Thus, the answer is 0. 

 Example 3: 

 Input: capacity = [4], itemSize = 5 
 
 Output: -1 
 
 Explanation: 
 
 No box has enough capacity to store the item, so the answer is -1. 

 Constraints: 

 1 <= capacity.length <= 100 
 
 1 <= capacity[i] <= 100 
 
 1 <= itemSize <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int minimumIndex(vector<int>& capacity, int itemSize) {
        int ans = -1;
        for (int i = 0; i < (int)capacity.size(); ++i)
            if (capacity[i] >= itemSize && (ans == -1 || capacity[i] < capacity[ans])) ans = i;
        return ans;
    }
};
```


## 3872. Longest Arithmetic Sequence After Changing At Most One Element

**Problem:** https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Builds left and right arithmetic-run arrays and checks every possible modified position once.

### Problem description

You are given an integer array nums . 
 
 A subarray is arithmetic if the difference between consecutive elements in the subarray is constant. 
 
 You can replace at most one element in nums with any integer . Then, you select an arithmetic subarray from nums . 
 
 Return an integer denoting the maximum length of the arithmetic subarray you can select. 

 Example 1: 

 Input: nums = [9,7,5,10,1] 
 
 Output: 5 
 
 Explanation: 

 Replace nums[3] = 10 with 3. The array becomes [9, 7, 5, 3, 1] . 
 
 Select the subarray [ 9, 7, 5, 3, 1 ] , which is arithmetic because consecutive elements have a common difference of -2. 

 Example 2: 

 Input: nums = [1,2,6,7] 
 
 Output: 3 
 
 Explanation: 

 Replace nums[0] = 1 with -2. The array becomes [-2, 2, 6, 7] . 
 
 Select the subarray [ -2, 2, 6 , 7] , which is arithmetic because consecutive elements have a common difference of 4. 

 Constraints: 

 4 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int longestArithmetic(vector<int>& nums) {
        int n = nums.size();
        vector<int> left(n, 1), right(n, 1);
        for (int i = 1; i < n; ++i) {
            left[i] = 2;
            if (i >= 2 && (long long)nums[i] - nums[i-1] ==
                          (long long)nums[i-1] - nums[i-2])
                left[i] = left[i-1] + 1;
        }
        for (int i = n-2; i >= 0; --i) {
            right[i] = 2;
            if (i+2 < n && (long long)nums[i+1] - nums[i] ==
                           (long long)nums[i+2] - nums[i+1])
                right[i] = right[i+1] + 1;
        }
        int ans = 2;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, left[i]);
            if (i > 0) ans = max(ans, left[i-1] + 1);
            if (i+1 < n) ans = max(ans, right[i+1] + 1);
            if (i > 0 && i+1 < n) {
                long long gap = (long long)nums[i+1] - nums[i-1];
                if (gap % 2) continue;
                long long d = gap / 2;
                int l = 1, r = 1;
                if (i >= 2 && (long long)nums[i-1] - nums[i-2] == d)
                    l = left[i-1];
                if (i+2 < n && (long long)nums[i+2] - nums[i+1] == d)
                    r = right[i+1];
                ans = max(ans, l + 1 + r);
            }
        }
        return min(ans, n);
    }
};
```


## 3880. Minimum Absolute Difference Between Two Values

**Problem:** https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Tracks the latest indices containing 1 and 2 during one scan.

### Problem description

You are given an integer array nums consisting only of 0, 1, and 2. 
 
 A pair of indices (i, j) is called valid if nums[i] == 1 and nums[j] == 2 . 
 
 Return the minimum absolute difference between i and j among all valid pairs. If no valid pair exists, return -1. 
 
 The absolute difference between indices i and j is defined as abs(i - j) . 

 Example 1: 

 Input: nums = [1,0,0,2,0,1] 
 
 Output: 2 
 
 Explanation: 
 
 The valid pairs are: 

 (0, 3) which has absolute difference of abs(0 - 3) = 3 . 
 
 (5, 3) which has absolute difference of abs(5 - 3) = 2 . 

 Thus, the answer is 2. 

 Example 2: 

 Input: nums = [1,0,1,0] 
 
 Output: -1 
 
 Explanation: 
 
 There are no valid pairs in the array, thus the answer is -1. 

 Constraints: 

 1 <= nums.length <= 100 
 
 0 <= nums[i] <= 2

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int minAbsoluteDifference(vector<int>& nums) {
        int last1 = -1, last2 = -1, best = INT_MAX;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] == 1) { last1 = i; if (last2 != -1) best = min(best, i - last2); }
            if (nums[i] == 2) { last2 = i; if (last1 != -1) best = min(best, i - last1); }
        }
        return best == INT_MAX ? -1 : best;
    }
};
```


## 3909. Compare Sums of Bitonic Parts

**Problem:** https://leetcode.com/problems/compare-sums-of-bitonic-parts/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Finds the maximum element’s position, then sums the two portions in linear passes.

### Problem description

You are given a bitonic array nums of length n . 
 
 Split the array into two parts: 

 Ascending part : from index 0 to the peak element (inclusive). 
 
 Descending part : from the peak element to index n - 1 (inclusive). 

 The peak element belongs to both parts. 
 
 Return: 

 0 if the sum of the ascending part is greater. 
 
 1 if the sum of the descending part is greater. 
 
 -1 if both sums are equal . 

 Notes : 

 A bitonic array is an array that is strictly increasing up to a single peak element and then strictly decreasing . 
 
 An array is said to be strictly increasing if each element is strictly greater than its previous one (if exists). 
 
 An array is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists). 

 Example 1: 

 Input: nums = [1,3,2,1] 
 
 Output: 1 
 
 Explanation: 

 Peak element is nums[1] = 3 
 
 Ascending part = [1, 3] , sum is 1 + 3 = 4 
 
 Descending part = [3, 2, 1] , sum is 3 + 2 + 1 = 6 
 
 Since the descending part has a larger sum, return 1. 

 Example 2: 

 Input: nums = [2,4,5,2] 
 
 Output: 0 
 
 Explanation: 

 Peak element is nums[2] = 5 
 
 Ascending part = [2, 4, 5] , sum is 2 + 4 + 5 = 11 
 
 Descending part = [5, 2] , sum is 5 + 2 = 7 
 
 Since the ascending part has a larger sum, return 0. 

 Example 3: 

 Input: nums = [1,2,4,3] 
 
 Output: -1 
 
 Explanation: 

 Peak element is nums[2] = 4 
 
 Ascending part = [1, 2, 4] , sum is 1 + 2 + 4 = 7 
 
 Descending part = [4, 3] , sum is 4 + 3 = 7 
 
 Since both parts have equal sums, return -1. 

 Constraints: 

 3 <= n == nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9 
 
 nums is a bitonic array.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int compareBitonicSums(vector<int>& nums) {
        int n = nums.size(), peak = 0;
        for (int i=1; i<n; ++i)
            if (nums[i] > nums[peak]) peak = i;
        long long a=0, b=0;
        for (int i=0; i<=peak; ++i) a+=nums[i];
        for (int i=peak; i<n; ++i) b+=nums[i];
        return a==b ? -1 : (a>b ? 0 : 1);
    }
};
```


## 3912. Valid Elements in an Array

**Problem:** https://leetcode.com/problems/valid-elements-in-an-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Builds a suffix-maximum array and makes a second pass to collect valid elements.

### Problem description

You are given an integer array nums . 
 
 An element nums[i] is considered valid if it satisfies at least one of the following conditions: 

 It is strictly greater than every element to its left. 
 
 It is strictly greater than every element to its right. 

 The first and last elements are always valid. 
 
 Return an array of all valid elements in the same order as they appear in nums . 

 Example 1: 

 Input: nums = [1,2,4,2,3,2] 
 
 Output: [1,2,4,3,2] 
 
 Explanation: 

 nums[0] and nums[5] are always valid. 
 
 nums[1] and nums[2] are strictly greater than every element to their left. 
 
 nums[4] is strictly greater than every element to its right. 
 
 Thus, the answer is [1, 2, 4, 3, 2] . 

 Example 2: 

 Input: nums = [5,5,5,5] 
 
 Output: [5,5] 
 
 Explanation: 

 The first and last elements are always valid. 
 
 No other elements are strictly greater than all elements to their left or to their right. 
 
 Thus, the answer is [5, 5] . 

 Example 3: 

 Input: nums = [1] 
 
 Output: [1] 
 
 Explanation: 
 
 Since there is only one element, it is always valid. Thus, the answer is [1] . 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> findValidElements(vector<int>& nums) {
        int n = (int)nums.size();
        vector<int> rightMax(n);
        rightMax[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) rightMax[i] = max(nums[i], rightMax[i + 1]);
        vector<int> ans;
        int leftMax = INT_MIN;
        for (int i = 0; i < n; ++i) {
            if (i == 0 || i == n - 1 || nums[i] > leftMax || nums[i] > rightMax[i + 1]) ans.push_back(nums[i]);
            leftMax = max(leftMax, nums[i]);
        }
        return ans;
    }
};
```


## 3917. Count Indices With Opposite Parity

**Problem:** https://leetcode.com/problems/count-indices-with-opposite-parity/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output

**Complexity reasoning:** Counts even and odd elements, then appends the opposite-parity count for every position.

### Problem description

You are given an integer array nums of length n . 
 
 The score of an index i is defined as the number of indices j such that: 

 i < j < n , and 
 
 nums[i] and nums[j] have different parity (one is even and the other is odd). 

 Return an integer array answer of length n , where answer[i] is the score of index i . 

 Example 1: 

 Input: nums = [1,2,3,4] 
 
 Output: [2,1,1,0] 
 
 Explanation: 

 nums[0] = 1 , which is odd. Thus, the indices j = 1 and j = 3 satisfy the conditions, so the score of index 0 is 2. 
 
 nums[1] = 2 , which is even. Thus, the index j = 2 satisfies the conditions, so the score of index 1 is 1. 
 
 nums[2] = 3 , which is odd. Thus, the index j = 3 satisfies the conditions, so the score of index 2 is 1. 
 
 nums[3] = 4 , which is even. Thus, no index satisfies the conditions, so the score of index 3 is 0. 

 Thus, the answer = [2, 1, 1, 0] . 

 Example 2: 

 Input: nums = [1] 
 
 Output: [0] 
 
 Explanation: 
 
 There is only one element in nums . Thus, the score of index 0 is 0. 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> countOppositeParity(vector<int>& nums) {
        int even = 0, odd = 0;
        for (int x : nums) (x % 2 ? odd : even)++;
        vector<int> ans;
        for (int x : nums) {
            if (x % 2) { --odd; ans.push_back(even); }
            else { --even; ans.push_back(odd); }
        }
        return ans;
    }
};
```


## 3925. Concatenate Array With Reverse

**Problem:** https://leetcode.com/problems/concatenate-array-with-reverse/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Copies the n original elements and appends n elements in reverse order; the returned vector holds 2n elements.

### Problem description

You are given an integer array nums of length n . 
 
 Construct a new array ans of length 2 * n such that the first n elements are the same as nums , and the next n elements are the elements of nums in reverse order. 
 
 Formally, for 0 <= i <= n - 1 : 

 ans[i] = nums[i] 
 
 ans[i + n] = nums[n - i - 1] 

 Return an integer array ans . 

 Example 1: 

 Input: nums = [1,2,3] 
 
 Output: [1,2,3,3,2,1] 
 
 Explanation: 
 
 The first n elements of ans are the same as nums . 
 
 For the next n = 3 elements, each element is taken from nums in reverse order: 

 ans[3] = nums[2] = 3 
 
 ans[4] = nums[1] = 2 
 
 ans[5] = nums[0] = 1 

 Thus, ans = [1, 2, 3, 3, 2, 1] . 

 Example 2: 

 Input: nums = [1] 
 
 Output: [1,1] 
 
 Explanation: 
 
 The array remains the same when reversed. Thus, ans = [1, 1] . 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> concatWithReverse(vector<int>& nums) {
        vector<int> ans(nums.begin(), nums.end());
        ans.insert(ans.end(), nums.rbegin(), nums.rend());
        return ans;
    }
};
```


## 3937. Minimum Operations to Make Array Modulo Alternating I

**Problem:** https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(nk + k²)

**Space complexity:** O(k)

**Complexity reasoning:** For each of n elements, updates all k possible residue targets, then checks every pair of distinct even/odd targets. Two k-element cost arrays are stored.

### Problem description

You are given an integer array nums and an integer k . 
 
 In one operation, you can increase or decrease any element of nums by 1. 
 
 An array is called modulo alternating if there exist two distinct integers x and y ( 0 <= x, y < k ) such that: 

 For every even index i , nums[i] % k == x 
 
 For every odd index i , nums[i] % k == y 

 Return the minimum number of operations required to make nums modulo alternating . 

 Example 1: 

 Input: nums = [1,4,2,8], k = 3 
 
 Output: 2 
 
 Explanation: 

 Let's choose x = 1 for even indices and y = 2 for odd indices. 
 
 Perform the following operations:

 Increment nums[1] = 4 by 1, giving nums = [1, 5, 2, 8] . 
 
 Decrement nums[2] = 2 by 1, giving nums = [1, 5, 1, 8] . 

 Now, for even indices, nums[i] % k = 1 , and for odd indices, nums[i] % k = 2 . 
 
 Thus, the total number of operations required is 2. 

 Example 2: 

 Input: nums = [1,1,1], k = 3 
 
 Output: 1 
 
 Explanation: 

 Incrementing nums[1] by 1 gives nums = [1, 2, 1] , which satisfies the condition with x = 1 and y = 2 . 
 
 Thus, the total number of operations required is 1. 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 10 9 
 
 2 <= k <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums,int k){
        vector<int> even(k,0),odd(k,0);
        for(int i=0;i<(int)nums.size();++i){
            int r=nums[i]%k;
            vector<int>& costs=(i%2?odd:even);
            for(int t=0;t<k;++t){
                int d=abs(r-t);
                costs[t]+=min(d,k-d);
            }
        }
        int ans=INT_MAX;
        for(int x=0;x<k;++x) for(int y=0;y<k;++y)
            if(x!=y) ans=min(ans,even[x]+odd[y]);
        return ans;
    }
};
```


## 3942. Minimum Operations to Sort a Permutation

**Problem:** https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Queue, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Builds the reversed permutation and checks two candidate goal rotations in O(n). BFS visits at most 2n (orientation, shift) states, each with two constant-time transitions; distance, goal, and queue storage are O(n).

### Problem description

You are given an integer array nums of length n , where nums is a permutation of the integers from 0 to n - 1 . 
 
 You may perform only the following operations: 

 Reverse the entire array. 
 
 Rotate Left by One : Move the first element to the end of the array, and rest elements to left by one position. 

 Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1. 

 Example 1: 

 Input: nums = [0,2,1] 
 
 Output: 2 
 
 Explanation: 

 Rotate Left by one: [2, 1, 0] 
 
 Reverse the array: [0, 1, 2] 

 The array becomes sorted in 2 operations, which is minimal. 

 Example 2: 

 Input: nums = [1,0,2] 
 
 Output: 2 
 
 Explanation: 

 Reverse the array: [2, 0, 1] 
 
 Rotate Left by one: [0, 1, 2] 

 The array becomes sorted in 2 operations, which is minimal. 

 Example 3: 

 Input: nums = [2,0,1,3] 
 
 Output: -1 
 
 Explanation: 
 
 It is impossible to reach [0, 1, 2, 3] . Thus, the answer is -1. 

 Constraints: 

 1 <= n == nums.length <= 10 5 
 
 0 <= nums[i] <= n - 1 
 
 nums is a permutation of integers from 0 to n - 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n=nums.size();
        vector<int> rev(nums.rbegin(),nums.rend());
        vector<vector<int> > dist(2,vector<int>(n,-1));
        queue<pair<int,int> > q;q.push({0,0});dist[0][0]=0;
        vector<vector<bool> > goal(2,vector<bool>(n,false));
        for(int t=0;t<2;t++){
            const vector<int> &a=t?rev:nums;
            int z=find(a.begin(),a.end(),0)-a.begin();
            bool good=true;
            for(int i=0;i<n;i++)if(a[(i+z)%n]!=i){good=false;break;}
            if(good)goal[t][z]=true;
        }
        while(!q.empty()){
            auto p=q.front();q.pop();int t=p.first,s=p.second;
            if(goal[t][s])return dist[t][s];
            int ns=(s+1)%n;
            if(dist[t][ns]<0){dist[t][ns]=dist[t][s]+1;q.push({t,ns});}
            int nt=1-t;ns=(n-s)%n;
            if(dist[nt][ns]<0){dist[nt][ns]=dist[t][s]+1;q.push({nt,ns});}
        }
        return -1;
    }
};
```


## 3944. Minimum Operations to Make Array Modulo Alternating II

**Problem:** https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + k)

**Space complexity:** O(k)

**Complexity reasoning:** Each parity pass counts its elements, builds doubled residue frequencies and prefix sums, and evaluates k target residues in O(n + k) total. Choosing the two best odd-parity targets and combining costs takes O(k); temporary arrays are O(k).

### Problem description

You are given an integer array nums and an integer k . 
 
 In one operation, you can increase or decrease any element of nums by 1. 
 
 An array is called modulo alternating if there exist two distinct integers x and y ( 0 <= x, y < k ) such that: 

 For every even index i , nums[i] % k == x 
 
 For every odd index i , nums[i] % k == y 

 Return the minimum number of operations required to make nums modulo alternating . 

 Example 1: 

 Input: nums = [1,4,2,8], k = 3 
 
 Output: 2 
 
 Explanation: 

 Let's choose x = 1 for even indices and y = 2 for odd indices. 
 
 Perform the following operations:

 Increment nums[1] = 4 by 1, giving nums = [1, 5, 2, 8] . 
 
 Decrement nums[2] = 2 by 1, giving nums = [1, 5, 1, 8] . 

 Now, for even indices, nums[i] % k = 1 , and for odd indices, nums[i] % k = 2 . 
 
 Thus, the total number of operations required is 2. 

 Example 2: 

 Input: nums = [1,1,1], k = 3 
 
 Output: 1 
 
 Explanation: 

 Incrementing nums[1] by 1 gives nums = [1, 2, 1] , which satisfies the condition with x = 1 and y = 2 . 
 
 Thus, the total number of operations required is 1. 

 Example 3: 

 Input: nums = [6,7,8], k = 2 
 
 Output: 0 
 
 Explanation: 
 
 The array already satisfies the condition with x = 0 and y = 1 . Thus, no operations are required. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9 
 
 2 <= k <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
 vector<long long> costs(const vector<int>& nums,int k,int parity){
  vector<long long>freq(2*k),pc(2*k+1),ps(2*k+1),res(k);
  for(int i=parity;i<(int)nums.size();i+=2)++freq[nums[i]%k];
  for(int i=0;i<k;++i)freq[i+k]=freq[i];
  for(int i=0;i<2*k;++i){pc[i+1]=pc[i]+freq[i];ps[i+1]=ps[i]+freq[i]*i;}
  for(int x=0;x<k;++x){int mid=x+k/2, end=x+k;
   long long c1=ps[mid+1]-ps[x]-1LL*x*(pc[mid+1]-pc[x]);
   long long c2=1LL*(x+k)*(pc[end]-pc[mid+1])-(ps[end]-ps[mid+1]);
   res[x]=c1+c2;
  }
  return res;
 }
public:
 long long minOperations(vector<int>& nums,int k){
  auto a=costs(nums,k,0),b=costs(nums,k,1);
  int b1=-1,b2=-1;
  for(int i=0;i<k;++i)if(b1<0||b[i]<b[b1]){b2=b1;b1=i;}else if(b2<0||b[i]<b[b2])b2=i;
  long long ans=LLONG_MAX;
  for(int i=0;i<k;++i)ans=min(ans,a[i]+b[i==b1?b2:b1]);
  return ans;
 }
};
```


## 3979. Maximum Valid Pair Sum

**Problem:** https://leetcode.com/problems/maximum-valid-pair-sum/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Scans indices j from k through n-1 once, maintaining the maximum eligible earlier element and the best pair sum in scalar variables.

### Problem description

You are given an integer array nums of length n and an integer k . 
 
 A pair of indices (i, j) is called valid if: 

 0 <= i < j < n 
 
 j - i >= k 

 Return the maximum value of nums[i] + nums[j] among all valid pairs. 

 Example 1: 

 Input: nums = [1,3,5,2,8], k = 2 
 
 Output: 13 
 
 Explanation: 
 
 The valid pairs are: 

 (0, 2) : nums[0] + nums[2] = 6 
 
 (0, 3) : nums[0] + nums[3] = 3 
 
 (0, 4) : nums[0] + nums[4] = 9 
 
 (1, 3) : nums[1] + nums[3] = 5 
 
 (1, 4) : nums[1] + nums[4] = 11 
 
 (2, 4) : nums[2] + nums[4] = 13 

 Thus, the answer is 13.​​​​​​​ 

 Example 2: 

 Input: nums = [5,1,9], k = 1 
 
 Output: 14 
 
 Explanation: 

 Since k = 1 , every pair is valid. 
 
 The maximum value is obtained from a pair (0, 2) ​​​​​​​, which is nums[0] + nums[2] = 5 + 9 = 14 . 
 
 Thus, the answer is 14. 

 Constraints: 

 2 <= n == nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9 
 
 1 <= k <= n - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int maxValidPairSum(vector<int>& nums,int k){
        long long ans=LLONG_MIN;
        int best=INT_MIN;
        for(int j=k;j<(int)nums.size();++j){
            best=max(best,nums[j-k]);
            ans=max(ans,1LL*best+nums[j]);
        }
        return (int)ans;
    }
};
```


## 4020. Elevator Requests I

**Problem:** https://leetcode.com/problems/elevator-requests-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(r)

**Space complexity:** O(1)

**Complexity reasoning:** Processes each of the r elevator requests once, adding the distance from the previous floor; only two running scalars are kept.

### Problem description

You are given an integer n denoting the number of floors in a building, where the floors are numbered from 0 to n - 1 . 
 
 You are also given an integer array requests , where requests represents the sequence of floor requests. 
 
 An elevator starts at floor 0 and follows these rules: 

 The elevator moves one floor per second. 
 
 The elevator serves requests in the given order. 
 
 If the elevator is already on the requested floor, no movement is needed. 
 
 After serving a request, the elevator immediately starts moving toward the next request. 

 Return the total time in seconds required to serve all requests. 

 Example 1: 

 Input: n = 5, requests = [2,1,4,3] 
 
 Output: 7 
 
 Explanation: 

 requests[0] = 2 : Moving from floor 0 to floor 2 takes 2 seconds. 
 
 requests[1] = 1 : Moving from floor 2 to floor 1 takes 1 second. 
 
 requests[2] = 4 : Moving from floor 1 to floor 4 takes 3 seconds. 
 
 requests[3] = 3 : Moving from floor 4 to floor 3 takes 1 second. 

 The total time required is 2 + 1 + 3 + 1 = 7 seconds. 

 Example 2: 

 Input: n = 3, requests = [2,0,0] 
 
 Output: 4 
 
 Explanation: 

 requests[0] = 2 : Moving from floor 0 to floor 2 takes 2 seconds. 
 
 requests[1] = 0 : Moving from floor 2 to floor 0 takes 2 seconds. 
 
 requests[2] = 0 : No movement is needed. 

 The total time required is 2 + 2 + 0 = 4 seconds. 

 Constraints: 

 1 <= n <= 100 
 
 1 <= requests.length <= 100 
 
 0 <= requests[i] <= n - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int elevatorRequests(int n, vector<int>& requests) {
        int current = 0, total = 0;
        for (int floor : requests) { total += abs(floor - current); current = floor; }
        return total;
    }
};
```


## 4024. Nearest Available Drone

**Problem:** https://leetcode.com/problems/nearest-available-drone/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Enumeration

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(d)

**Space complexity:** O(1)

**Complexity reasoning:** Checks each of the d drones once using Manhattan distance and its range, tracking only the closest valid drone and its index.

### Problem description

You are given a 2D integer array drones , where drones[i] = [x i , y i , range i ] represents the x-coordinate, y-coordinate, and travel range of the i th drone. 
 
 You are also given an integer array target = [tx, ty] , representing the coordinates of the target. 
 
 A drone drones[i] can reach the target if the Manhattan distance between its coordinates and the target coordinates is less than or equal to its range i . 
 
 Return the index of the reachable drone with the minimum Manhattan distance to the target. If there is a tie, return the smallest index . If no drone can reach the target, return -1 . 

 Example 1: 

 Input: drones = [[0,0,8],[2,2,9]], target = [3,4] 
 
 Output: 1 
 
 Explanation: 

 The distance between drones[0] and target is |0 - 3| + |0 - 4| = 7 , which is within its range of 8. 
 
 The distance between drones[1] and target is |2 - 3| + |2 - 4| = 3 , which is within its range of 9. 
 
 Since drones[1] is the nearest drone, the answer is 1. 

 Example 2: 

 Input: drones = [[2,1,5],[4,4,5],[6,6,8]], target = [5,5] 
 
 Output: 1 
 
 Explanation: 

 The distance between drones[0] and target is |2 - 5| + |1 - 5| = 7 , which is greater than its range of 5. 
 
 The distance between drones[1] and target is |4 - 5| + |4 - 5| = 2 , which is within its range of 5. 
 
 The distance between drones[2] and target is |6 - 5| + |6 - 5| = 2 , which is within its range of 8. 
 
 Both drones[1] and drones[2] are the nearest drones. Since we should return the smallest index, the answer is 1. 

 Example 3: 

 Input: drones = [[4,4,5]], target = [8,6] 
 
 Output: -1 
 
 Explanation: 

 The distance between drones[0] and target is |4 - 8| + |4 - 6| = 6 , which is greater than its range of 5. 
 
 No drone can reach the target, so the answer is -1. 

 Constraints: 

 1 <= drones.length <= 100 
 
 drones[i] = [x i , y i , range i ] 
 
 target = [tx, ty] 
 
 -25 <= x i , y i , tx, ty <= 25 
 
 1 <= range i <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int nearestDrone(vector<vector<int>>& drones, vector<int>& target) {
        int best = INT_MAX, ans = -1;
        for (int i = 0; i < (int)drones.size(); ++i) {
            int dist = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1]);
            if (dist <= drones[i][2] && dist < best) { best = dist; ans = i; }
        }
        return ans;
    }
};
```


## 4052. Cyclically Shift Rows and Columns

**Problem:** https://leetcode.com/problems/cyclically-shift-rows-and-columns/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Matrix, Simulation

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(n²)

**Complexity reasoning:** Initializes two n-by-n matrices, then traverses all n² cells once to shift rows and once to shift columns; both temporary matrices require quadratic storage.

### Problem description

You are given an integer n , a 2D integer array grid of size n x n , and two integer arrays rowShift and colShift , each of length n , where: 

 rowShift[i] represents the number of positions to cyclically shift the i th row of grid to the left . 
 
 colShift[j] represents the number of positions to cyclically shift the j th column of grid upward . 

 First, cyclically shift each row according to rowShift , then cyclically shift each column of the resulting grid according to colShift . 
 
 Return the resulting grid after performing all the shifts. 
 
 A cyclic left shift of a row by k positions moves the element at column j to column (j - k + n) % n . All other rows remain unchanged. 
 
 A cyclic upward shift of a column by k positions moves the element at row i to row (i - k + n) % n . All other columns remain unchanged. 

 Example 1: 

 Input: n = 2, grid = [[1,2],[3,4]], rowShift = [1,0], colShift = [0,1] 
 
 Output: [[2,4],[3,1]] 
 
 Explanation: 
 
 The grid changes as follows: 
 
 [Figure: https://assets.leetcode.com/uploads/2026/08/18/4743-1.png] 

 Example 2: 

 Input: n = 3, grid = [[1,2,3],[4,5,6],[7,8,9]], rowShift = [1,2,0], colShift = [2,2,1] 
 
 Output: [[7,8,5],[2,3,9],[6,4,1]] 
 
 Explanation: 
 
 The grid changes as follows: 
 
 [Figure: https://assets.leetcode.com/uploads/2026/08/18/4743-2.png] 

 Constraints: 

 1 <= n == grid.length == grid[i].length <= 10 
 
 1 <= grid[i][j] <= 100 
 
 rowShift.length == colShift.length == n 
 
 0 <= rowShift[i], colShift[i] < n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    public: vector<vector<int>> cyclicShift(int n,vector<vector<int>>& grid,vector<int>& rowShift,vector<int>& colShift) {
        vector<vector<int>> a(n,vector<int>(n)),b=a;
        for(int i=0; i<n; i++)for(int j=0; j<n; j++)a[i][(j-rowShift[i]+n)%n]=grid[i][j];
        for(int i=0; i<n; i++)for(int j=0; j<n; j++)b[(i-colShift[j]+n)%n][j]=a[i][j];
        return b;
    }
}
;
```


## 4062. Transform Array Using Pair Operations

**Problem:** https://leetcode.com/problems/transform-array-using-pair-operations/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Brainteaser

**Primary pattern:** Simulation / Implementation

**Related patterns:** Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Directly model operations, states, and edge cases.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** After constant-time length and singleton checks, computes one sum over source and one over target; no auxiliary containers are allocated.

### Problem description

You are given two integer arrays source and target . 
 
 In one operation , you may choose two distinct indices i and j in source , along with any integer delta . Then update source as follows: 

 source[i] = source[i] + source[j] - delta 
 
 source[j] = delta 

 Return true if it is possible to make source equal to target after performing the operation any (including zero) number of times. Otherwise, return false . 

 Example 1: 

 Input: source = [1,2,3], target = [0,2,4] 
 
 Output: true 
 
 Explanation: 

 Choose indices i = 0 and j = 2 , and set delta = 4 . 
 
 Before operation, source[0] = 1 and source[2] = 3 . 
 
 After the operation,

 source[0] = 1 + 3 - 4 = 0 
 
 source[2] = 4 

 Hence, source becomes [0, 2, 4] , which is equal to target . 
 
 Therefore, the answer is true . 

 Example 2: 

 Input: source = [-5,-5], target = [-15,5] 
 
 Output: true 
 
 Explanation: 

 Choose indices i = 1 and j = 0 , and set delta = -15 . 
 
 Before operation, source[1] = -5 and source[0] = -5 . 
 
 After the operation,

 source[1] = -5 + (-5) - (-15) = 5 
 
 source[0] = -15 

 Hence, source becomes [-15, 5] , which is equal to target . 
 
 Therefore, the answer is true . 

 Example 3: 

 Input: source = [1,2,1], target = [0,2,5] 
 
 Output: false 
 
 Explanation: 
 
 It can be shown that no matter what operations are performed, source can never be made equal to target . Therefore, the answer is false . 

 Constraints: 

 2 <= source.length == target.length <= 10 5 
 
 -10 9 <= source[i], target[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool canTransform(vector<int>& source, vector<int>& target) {
        if (source.size() != target.size()) return false;
        if (source.size() == 1) return source[0] == target[0];
        long long a = 0, b = 0;
        for (int x : source) a += x;
        for (int x : target) b += x;
        return a == b;
    }
};
```

