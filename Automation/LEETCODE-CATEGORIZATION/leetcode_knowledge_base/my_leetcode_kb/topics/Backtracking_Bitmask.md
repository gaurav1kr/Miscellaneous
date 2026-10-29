# Backtracking / Bitmask

**Problems:** 61

## Quick revision checklist

Enumerate choices while pruning; compress subsets as masks.

## Problem index

- [17. Letter Combinations of a Phone Number](#17-letter-combinations-of-a-phone-number) — Medium; code: yes
- [37. Sudoku Solver](#37-sudoku-solver) — Hard; code: yes
- [39. Combination Sum](#39-combination-sum) — Medium; code: yes
- [40. Combination Sum II](#40-combination-sum-ii) — Medium; code: yes
- [46. Permutations](#46-permutations) — Medium; code: yes
- [47. Permutations II](#47-permutations-ii) — Medium; code: yes
- [51. N-Queens](#51-n-queens) — Hard; code: yes
- [52. N-Queens II](#52-n-queens-ii) — Hard; code: yes
- [77. Combinations](#77-combinations) — Medium; code: yes
- [78. Subsets](#78-subsets) — Medium; code: yes
- [89. Gray Code](#89-gray-code) — Medium; code: yes
- [90. Subsets II](#90-subsets-ii) — Medium; code: yes
- [93. Restore IP Addresses](#93-restore-ip-addresses) — Medium; code: yes
- [216. Combination Sum III](#216-combination-sum-iii) — Medium; code: yes
- [254. Factor Combinations](#254-factor-combinations) — Medium; code: yes
- [267. Palindrome Permutation II](#267-palindrome-permutation-ii) — Medium; code: yes
- [282. Expression Add Operators](#282-expression-add-operators) — Hard; code: yes
- [291. Word Pattern II](#291-word-pattern-ii) — Medium; code: yes
- [306. Additive Number](#306-additive-number) — Medium; code: yes
- [320. Generalized Abbreviation](#320-generalized-abbreviation) — Medium; code: yes
- [401. Binary Watch](#401-binary-watch) — Easy; code: yes
- [411. Minimum Unique Word Abbreviation](#411-minimum-unique-word-abbreviation) — Hard; code: yes
- [489. Robot Room Cleaner](#489-robot-room-cleaner) — Hard; code: yes
- [491. Non-decreasing Subsequences](#491-non-decreasing-subsequences) — Medium; code: yes
- [679. 24 Game](#679-24-game) — Hard; code: yes
- [681. Next Closest Time](#681-next-closest-time) — Medium; code: yes
- [756. Pyramid Transition Matrix](#756-pyramid-transition-matrix) — Medium; code: yes
- [784. Letter Case Permutation](#784-letter-case-permutation) — Medium; code: yes
- [816. Ambiguous Coordinates](#816-ambiguous-coordinates) — Medium; code: yes
- [842. Split Array into Fibonacci Sequence](#842-split-array-into-fibonacci-sequence) — Medium; code: yes
- [949. Largest Time for Given Digits](#949-largest-time-for-given-digits) — Medium; code: yes
- [980. Unique Paths III](#980-unique-paths-iii) — Hard; code: yes
- [1079. Letter Tile Possibilities](#1079-letter-tile-possibilities) — Medium; code: yes
- [1088. Confusing Number II](#1088-confusing-number-ii) — Hard; code: yes
- [1219. Path with Maximum Gold](#1219-path-with-maximum-gold) — Medium; code: yes
- [1238. Circular Permutation in Binary Representation](#1238-circular-permutation-in-binary-representation) — Medium; code: yes
- [1239. Maximum Length of a Concatenated String with Unique Characters](#1239-maximum-length-of-a-concatenated-string-with-unique-characters) — Medium; code: yes
- [1240. Tiling a Rectangle with the Fewest Squares](#1240-tiling-a-rectangle-with-the-fewest-squares) — Hard; code: yes
- [1286. Iterator for Combination](#1286-iterator-for-combination) — Medium; code: yes
- [1307. Verbal Arithmetic Puzzle](#1307-verbal-arithmetic-puzzle) — Hard; code: yes
- [1415. The k-th Lexicographical String of All Happy Strings of Length n](#1415-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n) — Medium; code: yes
- [1593. Split a String Into the Max Number of Unique Substrings](#1593-split-a-string-into-the-max-number-of-unique-substrings) — Medium; code: yes
- [1601. Maximum Number of Achievable Transfer Requests](#1601-maximum-number-of-achievable-transfer-requests) — Hard; code: yes
- [1718. Construct the Lexicographically Largest Valid Sequence](#1718-construct-the-lexicographically-largest-valid-sequence) — Medium; code: yes
- [1849. Splitting a String Into Descending Consecutive Values](#1849-splitting-a-string-into-descending-consecutive-values) — Medium; code: yes
- [1863. Sum of All Subset XOR Totals](#1863-sum-of-all-subset-xor-totals) — Easy; code: yes
- [1980. Find Unique Binary String](#1980-find-unique-binary-string) — Medium; code: yes
- [2044. Count Number of Maximum Bitwise-OR Subsets](#2044-count-number-of-maximum-bitwise-or-subsets) — Medium; code: yes
- [2048. Next Greater Numerically Balanced Number](#2048-next-greater-numerically-balanced-number) — Medium; code: yes
- [2056. Number of Valid Move Combinations On Chessboard](#2056-number-of-valid-move-combinations-on-chessboard) — Hard; code: yes
- [2151. Maximum Good People Based on Statements](#2151-maximum-good-people-based-on-statements) — Hard; code: yes
- [2212. Maximum Points in an Archery Competition](#2212-maximum-points-in-an-archery-competition) — Medium; code: yes
- [2397. Maximum Rows Covered by Columns](#2397-maximum-rows-covered-by-columns) — Medium; code: yes
- [2664. The Knight’s Tour](#2664-the-knight-s-tour) — Medium; code: yes
- [2698. Find the Punishment Number of an Integer](#2698-find-the-punishment-number-of-an-integer) — Medium; code: yes
- [3211. Generate Binary Strings Without Adjacent Zeros](#3211-generate-binary-strings-without-adjacent-zeros) — Medium; code: yes
- [3437. Permutations III](#3437-permutations-iii) — Medium; code: yes
- [3646. Next Special Palindrome Number](#3646-next-special-palindrome-number) — Hard; code: yes
- [3669. Balanced K-Factor Decomposition](#3669-balanced-k-factor-decomposition) — Medium; code: yes
- [3799. Word Squares II](#3799-word-squares-ii) — Medium; code: yes
- [3955. Valid Binary Strings With Cost Limit](#3955-valid-binary-strings-with-cost-limit) — Medium; code: yes

---

## 17. Letter Combinations of a Phone Number

**Problem:** https://leetcode.com/problems/letter-combinations-of-a-phone-number/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, String Algorithms

**Data structures (inferred):** Hash map / hash set, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order . 
 
 A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters. 
 [Figure: https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png] 

 Example 1: 
 
```
Input:
 digits = "23"

Output:
 ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

 Example 2: 
 
```
Input:
 digits = "2"

Output:
 ["a","b","c"]
```

 Constraints: 

 1 <= digits.length <= 4 
 
 digits[i] is a digit in the range ['2', '9'] .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        vector<string> res;
        string cur;
        vector<string> map = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        
        function<void(int)> backtrack = [&](int i) {
            if (i == digits.size()) {
                res.push_back(cur);
                return;
            }
            for (char c : map[digits[i] - '0']) {
                cur.push_back(c);
                backtrack(i + 1);
                cur.pop_back();
            }
        };
        
        backtrack(0);
        return res;
    }
};
```


## 37. Sudoku Solver

**Problem:** https://leetcode.com/problems/sudoku-solver/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, Backtracking, Matrix, Algorithm X, Dancing Links

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Hash map / hash set, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Write a program to solve a Sudoku puzzle by filling the empty cells. 
 
 A sudoku solution must satisfy all of the following rules : 

 Each of the digits 1-9 must occur exactly once in each row. 
 
 Each of the digits 1-9 must occur exactly once in each column. 
 
 Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid. 

 The '.' character indicates empty cells. 

 Example 1: 
 [Figure: https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png] 
 
```
Input:
 board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

Output:
 [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

Explanation:
 The input board is shown above and the only valid solution is shown below:
```

 Constraints: 

 board.length == 9 
 
 board[i].length == 9 
 
 board[i][j] is a digit or '.' . 
 
 It is guaranteed that the input board has only one solution.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    void solveSudoku(vector<vector<char>>& board) 
    {
        solve(board);
    }

private:
    bool solve(vector<vector<char>>& board) 
    {
        for (int row = 0; row < 9; ++row) 
        {
            for (int col = 0; col < 9; ++col) 
            {
                if (board[row][col] == '.') 
                {
                    for (char num = '1'; num <= '9'; ++num) 
                    {
                        if (isValid(board, row, col, num)) 
                        {
                            board[row][col] = num;
                            if (solve(board)) return true;
                            board[row][col] = '.'; // backtrack
                        }
                    }
                    return false; // no valid number found
                }
            }
        }
        return true; // solved
    }

    bool isValid(vector<vector<char>>& board, int row, int col, char num) 
    {
        for (int i = 0; i < 9; ++i) 
        {
            if (board[row][i] == num || board[i][col] == num ||
                board[row / 3 * 3 + i / 3][col / 3 * 3 + i % 3] == num) 
                {
                return false;
                }
        }
        return true;
    }
};
```


## 39. Combination Sum

**Problem:** https://leetcode.com/problems/combination-sum/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array of distinct integers candidates and a target integer target , return a list of all unique combinations of candidates where the chosen numbers sum to target . You may return the combinations in any order . 
 
 The same number may be chosen from candidates an unlimited number of times . Two combinations are unique if the frequency of at least one of the chosen numbers is different. 
 
 The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input. 

 Example 1: 
 
```
Input:
 candidates = [2,3,6,7], target = 7

Output:
 [[2,2,3],[7]]

Explanation:

2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

 Example 2: 
 
```
Input:
 candidates = [2,3,5], target = 8

Output:
 [[2,2,2,2],[2,3,3],[3,5]]
```

 Example 3: 
 
```
Input:
 candidates = [2], target = 1

Output:
 []
```

 Constraints: 

 1 <= candidates.length <= 30 
 
 2 <= candidates[i] <= 40 
 
 All elements of candidates are distinct . 
 
 1 <= target <= 40

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    void dfs(int i, int target, vector<int>& c, vector<int>& path, vector<vector<int>>& res) {
        if (target == 0) { res.push_back(path); return; }
        if (i == c.size() || target < 0) return;
        
        path.push_back(c[i]);
        dfs(i, target - c[i], c, path, res);
        path.pop_back();
        
        dfs(i + 1, target, c, path, res);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        dfs(0, target, candidates, path, res);
        return res;
    }
};
```


## 40. Combination Sum II

**Problem:** https://leetcode.com/problems/combination-sum-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a collection of candidate numbers ( candidates ) and a target number ( target ), find all unique combinations in candidates  where the candidate numbers sum to target . 
 
 Each number in candidates  may only be used once in the combination. 
 
 Note:  The solution set must not contain duplicate combinations. 

 Example 1: 
 
```
Input:
 candidates = [10,1,2,7,6,1,5], target = 8

Output:
 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

 Example 2: 
 
```
Input:
 candidates = [2,5,2,1,2], target = 5

Output:
 
[
[1,2,2],
[5]
]
```

 Constraints: 

 1 <= candidates.length <= 100 
 
 1 <= candidates[i] <= 50 
 
 1 <= target <= 30

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    void backtrack(vector<int>& candidates, int target, int start, vector<int>& current, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(current);
            return;
        }
        for (int i = start; i < candidates.size(); ++i) {
            if (i > start && candidates[i] == candidates[i - 1]) continue; // Skip duplicates
            if (candidates[i] > target) break; // No need to proceed further
            current.push_back(candidates[i]);
            backtrack(candidates, target - candidates[i], i + 1, current, result);
            current.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> current;
        backtrack(candidates, target, 0, current, result);
        return result;
    }
};
```


## 46. Permutations

**Problem:** https://leetcode.com/problems/permutations/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array nums of distinct integers, return all the possible permutations . You can return the answer in any order . 

 Example 1: 
 
```
Input:
 nums = [1,2,3]

Output:
 [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```
 
 Example 2: 
 
```
Input:
 nums = [0,1]

Output:
 [[0,1],[1,0]]
```
 
 Example 3: 
 
```
Input:
 nums = [1]

Output:
 [[1]]
```

 Constraints: 

 1 <= nums.length <= 6 
 
 -10 <= nums[i] <= 10 
 
 All the integers of nums are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    vector<vector<int>> final_vec ;
public:
    void Get_permute(vector<int> a , int l , int r)
    {
        if(l==r)
        {
            final_vec.push_back(a) ;
        }
        else
        {
            // Permutations made  
            for (int i = l; i <= r; i++)  
            {  

                // Swapping done  
                swap(a[l], a[i]);    
                Get_permute(a, l+1, r);  
                swap(a[l], a[i]);  
            }  
        }  
    }
    vector<vector<int>> permute(vector<int>& nums) 
    {
        int lower = 0 ;
        int upper = nums.size() ;
        Get_permute(nums, lower, upper-1);
        return final_vec ;
    }
};
```


## 47. Permutations II

**Problem:** https://leetcode.com/problems/permutations-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking, Sorting

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a collection of numbers, nums , that might contain duplicates, return all possible unique permutations in any order . 

 Example 1: 
 
```
Input:
 nums = [1,1,2]

Output:

[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

 Example 2: 
 
```
Input:
 nums = [1,2,3]

Output:
 [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

 Constraints: 

 1 <= nums.length <= 8 
 
 -10 <= nums[i] <= 10

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> permuteUnique(std::vector<int>& nums) {
        std::vector<std::vector<int>> results;
        std::vector<int> current;
        std::vector<bool> used(nums.size(), false);
        std::sort(nums.begin(), nums.end()); // Sort to handle duplicates
        backtrack(nums, used, current, results);
        return results;
    }

private:
    void backtrack(const std::vector<int>& nums, std::vector<bool>& used,
                   std::vector<int>& current, std::vector<std::vector<int>>& results) {
        if (current.size() == nums.size()) {
            results.push_back(current);
            return;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) continue;
            used[i] = true;
            current.push_back(nums[i]);
            backtrack(nums, used, current, results);
            used[i] = false;
            current.pop_back();
        }
    }
};
```


## 51. N-Queens

**Problem:** https://leetcode.com/problems/n-queens/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Backtracking, Algorithm X

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. 
 
 Given an integer n , return all distinct solutions to the n-queens puzzle . You may return the answer in any order . 
 
 Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/13/queens.jpg] 
 
```
Input:
 n = 4

Output:
 [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Explanation:
 There exist two distinct solutions to the 4-queens puzzle as shown above
```

 Example 2: 
 
```
Input:
 n = 1

Output:
 [["Q"]]
```

 Constraints: 

 1 <= n <= 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> results;
        vector<string> board(n, string(n, '.'));
        vector<bool> columns(n, false), diag1(2 * n - 1, false), diag2(2 * n - 1, false);
        solve(0, n, board, results, columns, diag1, diag2);
        return results;
    }

private:
    void solve(int row, int n, vector<string>& board, vector<vector<string>>& results, 
               vector<bool>& columns, vector<bool>& diag1, vector<bool>& diag2) {
        if (row == n) {
            results.push_back(board);
            return;
        }

        for (int col = 0; col < n; ++col) {
            int d1 = row - col + n - 1;
            int d2 = row + col;
            if (columns[col] || diag1[d1] || diag2[d2]) continue;

            board[row][col] = 'Q';
            columns[col] = diag1[d1] = diag2[d2] = true;

            solve(row + 1, n, board, results, columns, diag1, diag2);

            board[row][col] = '.';
            columns[col] = diag1[d1] = diag2[d2] = false;
        }
    }
};
```


## 52. N-Queens II

**Problem:** https://leetcode.com/problems/n-queens-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Backtracking, Algorithm X

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask

**Data structures (inferred):** Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. 
 
 Given an integer n , return the number of distinct solutions to the  n-queens puzzle . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/13/queens.jpg] 
 
```
Input:
 n = 4

Output:
 2

Explanation:
 There are two distinct solutions to the 4-queens puzzle as shown.
```

 Example 2: 
 
```
Input:
 n = 1

Output:
 1
```

 Constraints: 

 1 <= n <= 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int totalNQueens(int n) {
        vector<int> cols(n, 0), diag1(2 * n, 0), diag2(2 * n, 0);
        return solve(0, n, cols, diag1, diag2);
    }

    int solve(int row, int n, vector<int>& cols, vector<int>& diag1, vector<int>& diag2) {
        if (row == n) return 1;
        int count = 0;
        for (int col = 0; col < n; col++) {
            if (cols[col] || diag1[row - col + n] || diag2[row + col]) continue;
            cols[col] = diag1[row - col + n] = diag2[row + col] = 1;
            count += solve(row + 1, n, cols, diag1, diag2);
            cols[col] = diag1[row - col + n] = diag2[row + col] = 0;
        }
        return count;
    }
};
```


## 77. Combinations

**Problem:** https://leetcode.com/problems/combinations/

**Difficulty:** Medium | **Premium:** No

**Tags:** Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask

**Data structures (inferred):** Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given two integers n and k , return all possible combinations of k numbers chosen from the range [1, n] . 
 
 You may return the answer in any order . 

 Example 1: 
 
```
Input:
 n = 4, k = 2

Output:
 [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Explanation:
 There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
```

 Example 2: 
 
```
Input:
 n = 1, k = 1

Output:
 [[1]]

Explanation:
 There is 1 choose 1 = 1 total combination.
```

 Constraints: 

 1 <= n <= 20 
 
 1 <= k <= n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    void solve(int ind,vector<int>&nums,vector<int>&ds,vector<vector<int>>&res,int k)
    {
        if(ind==nums.size())
        {
            if(ds.size()==k)
            {
                res.push_back(ds);
            }
            return;
        }
        ds.push_back(nums[ind]);
        solve(ind+1,nums,ds,res,k);
        ds.pop_back();
        solve(ind+1,nums,ds,res,k);
    }
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>>res;
        vector<int>ds;
        vector<int>nums;
        int i;
        for(i=1;i<=n;i++)
        {
            nums.push_back(i);
        }
        solve(0,nums,ds,res,k);
        return res;
        
    }
};
```


## 78. Subsets

**Problem:** https://leetcode.com/problems/subsets/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array nums of unique elements, return all possible subsets (the power set) . 
 
 The solution set must not contain duplicate subsets. Return the solution in any order . 

 Example 1: 
 
```
Input:
 nums = [1,2,3]

Output:
 [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

 Example 2: 
 
```
Input:
 nums = [0]

Output:
 [[],[0]]
```

 Constraints: 

 1 <= nums.length <= 10 
 
 -10 <= nums[i] <= 10 
 
 All the numbers of  nums are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    void backtrack(int start, std::vector<int>& nums, std::vector<int>& current, std::vector<std::vector<int>>& result) {
        result.push_back(current);  // Store current subset

        for (int i = start; i < nums.size(); ++i) {
            current.push_back(nums[i]);      // Include nums[i]
            backtrack(i + 1, nums, current, result);  // Recurse with next elements
            current.pop_back();              // Backtrack
        }
    }

    std::vector<std::vector<int>> subsets(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::vector<int> current;
        backtrack(0, nums, current, result);
        return result;
    }
};
```


## 89. Gray Code

**Problem:** https://leetcode.com/problems/gray-code/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Math / Number Theory, Bit Manipulation

**Data structures (inferred):** Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

An n-bit gray code sequence is a sequence of 2 n integers where: 

 Every integer is in the inclusive range [0, 2 n - 1] , 
 
 The first integer is 0 , 
 
 An integer appears no more than once in the sequence, 
 
 The binary representation of every pair of adjacent integers differs by exactly one bit , and 
 
 The binary representation of the first and last integers differs by exactly one bit . 

 Given an integer n , return any valid n-bit gray code sequence . 

 Example 1: 
 
```
Input:
 n = 2

Output:
 [0,1,3,2]

Explanation:

The binary representation of [0,1,3,2] is [00,01,11,10].
- 0
0
 and 0
1
 differ by one bit
- 
0
1 and 
1
1 differ by one bit
- 1
1
 and 1
0
 differ by one bit
- 
1
0 and 
0
0 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 
0
0 and 
1
0 differ by one bit
- 1
0
 and 1
1
 differ by one bit
- 
1
1 and 
0
1 differ by one bit
- 0
1
 and 0
0
 differ by one bit
```

 Example 2: 
 
```
Input:
 n = 1

Output:
 [0,1]
```

 Constraints: 

 1 <= n <= 16

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result(1 << n);
        for (int i = 0; i < (1 << n); i++) {
            result[i] = i ^ (i >> 1);
        }
        return result;
    }
};
```


## 90. Subsets II

**Problem:** https://leetcode.com/problems/subsets-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array nums that may contain duplicates, return all possible subsets (the power set) . 
 
 The solution set must not contain duplicate subsets. Return the solution in any order . 

 Example 1: 
 
```
Input:
 nums = [1,2,2]

Output:
 [[],[1],[1,2],[1,2,2],[2],[2,2]]
```
 
 Example 2: 
 
```
Input:
 nums = [0]

Output:
 [[],[0]]
```

 Constraints: 

 1 <= nums.length <= 10 
 
 -10 <= nums[i] <= 10

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    void backtrack(vector<int>& nums, int start, vector<int>& current, vector<vector<int>>& result) {
        result.push_back(current); // Add the current subset to the result
        
        for (int i = start; i < nums.size(); ++i) {
            // Skip duplicates
            if (i > start && nums[i] == nums[i - 1]) continue;

            // Include nums[i] in the current subset
            current.push_back(nums[i]);
            
            // Recurse for the next element
            backtrack(nums, i + 1, current, result);
            
            // Backtrack by removing the last element
            current.pop_back();
        }
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;

        // Sort the array to handle duplicates easily
        sort(nums.begin(), nums.end());
        
        // Start backtracking
        backtrack(nums, 0, current, result);
        
        return result;
    }
};
```


## 93. Restore IP Addresses

**Problem:** https://leetcode.com/problems/restore-ip-addresses/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 ( inclusive ) and cannot have leading zeros. 

 For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245" , "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

 Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s . You are not allowed to reorder or remove any digits in s . You may return the valid IP addresses in any order. 

 Example 1: 
 
```
Input:
 s = "25525511135"

Output:
 ["255.255.11.135","255.255.111.35"]
```

 Example 2: 
 
```
Input:
 s = "0000"

Output:
 ["0.0.0.0"]
```

 Example 3: 
 
```
Input:
 s = "101023"

Output:
 ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

 Constraints: 

 1 <= s.length <= 20 
 
 s consists of digits only.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    // Helper function to check if a given string is a valid IP address segment
    bool valid(string temp)
    {
        if(temp.size()>3 || temp.size()==0) return false; // segment length should be between 1 and 3
        if(temp.size()>1 && temp[0]=='0')   return false; // segment should not start with 0, unless it is a single digit
        if(temp.size() && stoi(temp)>255) return false; // segment should not be greater than 255
        return true;
    }

    // Backtracking function to generate all possible IP addresses
    void solve(vector<string>& ans, string output, int ind, string s, int dots)
    {
        if(dots == 3)
        { // if we have already added 3 dots, check if the remaining segment is valid
            if(valid(s.substr(ind)))
                ans.push_back(output+s.substr(ind));
            return;
        }
        int sz = s.size();
        for(int i=ind;i<min(ind+3, sz);i++)
        {
            if(valid(s.substr(ind, i-ind+1)))
            {
                output.push_back(s[i]);
                output.push_back('.');
                solve(ans, output, i+1, s, dots+1);
                output.pop_back(); //backtrack
            }
        }
    }

    vector<string> restoreIpAddresses(string s) 
    {
        vector<string> ans;
        string res;
        solve(ans, res, 0, s, 0);
        return ans;
    }
};
```


## 216. Combination Sum III

**Problem:** https://leetcode.com/problems/combination-sum-iii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Find all valid combinations of k numbers that sum up to n such that the following conditions are true: 

 Only numbers 1 through 9 are used. 
 
 Each number is used at most once . 

 Return a list of all possible valid combinations . The list must not contain the same combination twice, and the combinations may be returned in any order. 

 Example 1: 
 
```
Input:
 k = 3, n = 7

Output:
 [[1,2,4]]

Explanation:

1 + 2 + 4 = 7
There are no other valid combinations.
```

 Example 2: 
 
```
Input:
 k = 3, n = 9

Output:
 [[1,2,6],[1,3,5],[2,3,4]]

Explanation:

1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
```

 Example 3: 
 
```
Input:
 k = 4, n = 1

Output:
 []

Explanation:
 There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
```

 Constraints: 

 2 <= k <= 9 
 
 1 <= n <= 60

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    vector<vector<int>> ans;    
    void f(vector<int>& cur, int cnum, int k, int n) 
    {
        if(n < 0 || cur.size() > k) return;
        if(n == 0 && cur.size() == k) 
        {
            ans.push_back(cur);
            return;
        }
        
        for(int i=cnum; i<=9; ++i) 
        {
            cur.push_back(i);
            f(cur, i+1, k, n-i);
            cur.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum3(int k, int n) 
    {
        vector<int> cur;
        f(cur, 1, k, n);
        return ans;
    }
};
```


## 254. Factor Combinations

**Problem:** https://leetcode.com/problems/factor-combinations/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Backtracking, Prime Factorization

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask

**Data structures (inferred):** Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Numbers can be regarded as the product of their factors. 

 For example, 8 = 2 x 2 x 2 = 2 x 4 . 

 Given an integer n , return all possible combinations of its factors . You may return the answer in any order . 
 
 Note that the factors should be in the range [2, n - 1] . 

 Example 1: 
 
```
Input:
 n = 1

Output:
 []
```

 Example 2: 
 
```
Input:
 n = 12

Output:
 [[2,6],[3,4],[2,2,3]]
```

 Example 3: 
 
```
Input:
 n = 37

Output:
 []
```

 Constraints: 

 1 <= n <= 10 7

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
    vector< vector< int >>ans;
    vector< int>path;
    void dfs(int n, int start)
    {
        for (int f = start; (long long) f*f <= n;++f)
        {
            if (n % f)
            {
                continue;
            }
            path.push_back(f);
            auto x = path;
            x.push_back(n / f);
            ans.push_back(x);
            dfs(n / f, f);
            path.pop_back();
        }
    }
public:
    vector< vector< int >>getFactors(int n)
    {
        dfs(n, 2);
        return ans;
    }
};
```


## 267. Palindrome Permutation II

**Problem:** https://leetcode.com/problems/palindrome-permutation-ii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Hash Table, String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, String Algorithms

**Data structures (inferred):** Hash map / hash set, Ordered map, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a string s, return all the palindromic permutations (without duplicates) of it . 
 
 You may return the answer in any order . If s has no palindromic permutation, return an empty list. 

 Example 1: 
 
```
Input:
 s = "aabb"

Output:
 ["abba","baab"]
```
 
 Example 2: 
 
```
Input:
 s = "abc"

Output:
 []
```

 Constraints: 

 1 <= s.length <= 16 
 
 s consists of only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
public:
    vector< string>generatePalindromes(string s)
    {
        map< char, int>freq;
        for (char c : s)++freq[c];
        int odd = 0;
        string half, mid;
        for (auto&p : freq)
        {
            if (p.second % 2)
            {
                ++odd;
                mid = string(1, p.first);
            }
            half.append(p.second / 2, p.first);
        }
        if (odd >1) return { };
        vector< string>ans;
        do
        {
            string right = half;
            reverse(right.begin(), right.end());
            ans.push_back(half + mid + right);
        }
        while (next_permutation(half.begin(), half.end()));
        return ans;
    }
};
```


## 282. Expression Add Operators

**Problem:** https://leetcode.com/problems/expression-add-operators/

**Difficulty:** Hard | **Premium:** No

**Tags:** Math, String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Math / Number Theory

**Data structures (inferred):** String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a string num that contains only digits and an integer target , return all possibilities to insert the binary operators '+' , '-' , and/or '*' between the digits of num so that the resultant expression evaluates to the target value . 
 
 Note that operands in the returned expressions should not contain leading zeros. 
 
 Note that a number can contain multiple digits. 

 Example 1: 
 
```
Input:
 num = "123", target = 6

Output:
 ["1*2*3","1+2+3"]

Explanation:
 Both "1*2*3" and "1+2+3" evaluate to 6.
```

 Example 2: 
 
```
Input:
 num = "232", target = 8

Output:
 ["2*3+2","2+3*2"]

Explanation:
 Both "2*3+2" and "2+3*2" evaluate to 8.
```

 Example 3: 
 
```
Input:
 num = "3456237490", target = 9191

Output:
 []

Explanation:
 There are no expressions that can be created from "3456237490" to evaluate to 9191.
```

 Constraints: 

 1 <= num.length <= 10 
 
 num consists of only digits. 
 
 -2 31 <= target <= 2 31 - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<string> ans;
    
    vector<string> addOperators(string s, int target) 
    {
        helper(s,target, 0, "", 0, 0);
        return ans;
    }
    void helper(string s, int target,int i, const string& path, long eval, long residual) 
    {
        if(i==s.length()){
            if(eval==target){
                ans.push_back(path);
                return;
            }
        } 
        string currStr;
        long num=0;
        // backtracking loop
        for(int j=i;j<s.length();j++){
            // handle 0
            if(j>i && s[i]=='0') return;
            currStr+= s[j]; 
            num= num*10 + s[j]- '0';
            if(i==0){
                helper(s,target, j+1,path+ currStr,num, num);
            }
            else{
                helper(s,target,j+1,path + "+" + currStr, eval + num, num);
                helper(s,target,j+1,path + "-" + currStr, eval - num, -num);
                helper(s,target,j+1,path + "*" + currStr, eval -residual + residual*num , residual*num);


            }
        }
        
        
    }
};
```


## 291. Word Pattern II

**Problem:** https://leetcode.com/problems/word-pattern-ii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Hash Table, String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, String Algorithms

**Data structures (inferred):** Hash map, Hash map / hash set, Hash set, Ordered map, Ordered set, String

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a pattern and a string s , return true if s matches the pattern . 
 
 A string s matches a pattern if there is some bijective mapping of single characters to non-empty strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s . A bijective mapping means that no two characters map to the same string, and no character maps to two different strings. 

 Example 1: 
 
```
Input:
 pattern = "abab", s = "redblueredblue"

Output:
 true

Explanation:
 One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
```

 Example 2: 
 
```
Input:
 pattern = "aaaa", s = "asdasdasdasd"

Output:
 true

Explanation:
 One possible mapping is as follows:
'a' -> "asd"
```

 Example 3: 
 
```
Input:
 pattern = "aabb", s = "xyzabcxzyabc"

Output:
 false
```

 Constraints: 

 1 <= pattern.length, s.length <= 20 
 
 pattern and s consist of only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
    bool dfs(const string& p, int i, const string& s, int j,
             unordered_map<char, string>& mapping,
             unordered_set<string>& used)
             {
        if (i == (int)p.size() || j == (int)s.size())
        {
            return i == (int)p.size() && j == (int)s.size();
        }
        char c = p[i];
        if (mapping.count(c))
        {
            const string& word = mapping[c];
            if (s.compare(j, word.size(), word) != 0)
            {
                return false;
            }
            return dfs(p, i + 1, s, j + word.size(), mapping, used);
        }
        for (int end = j + 1; end <= (int)s.size(); ++end)
        {
            string word = s.substr(j, end - j);
            if (used.count(word))
            {
                continue;
            }
            mapping[c] = word;
            used.insert(word);
            if (dfs(p, i + 1, s, end, mapping, used))
            {
                return true;
            }
            used.erase(word);
            mapping.erase(c);
        }
        return false;
    }
public:
    bool wordPatternMatch(string pattern, string s)
    {
        unordered_map<char, string> mapping;
        unordered_set<string> used;
        return dfs(pattern, 0, s, 0, mapping, used);
    }
};
```


## 306. Additive Number

**Problem:** https://leetcode.com/problems/additive-number/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

An additive number is a string whose digits can form an additive sequence . 
 
 A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two. 
 
 Given a string containing only digits, return true if it is an additive number or false otherwise. 
 
 Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid. 

 Example 1: 
 
```
Input:
 "112358"

Output:
 true

Explanation:
 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```

 Example 2: 
 
```
Input:
 "199100199"

Output:
 true

Explanation:
 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199
```

 Constraints: 

 1 <= num.length <= 35 
 
 num consists only of digits. 

 Follow up: How would you handle overflow for very large input integers?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    bool isAdditiveNumber(string num) {
        int n = num.size();
        for (int i = 1; i <= n / 2; ++i) {
            for (int j = 1; max(i, j) <= n - i - j; ++j) {
                string a = num.substr(0, i);
                string b = num.substr(i, j);
                if ((a.size() > 1 && a[0] == '0') || (b.size() > 1 && b[0] == '0')) continue;

                string sum = a + b;
                while (sum.size() < num.size()) {
                    string c = addStrings(a, b);
                    sum += c;
                    a = b;
                    b = c;
                }
                if (sum == num) return true;
            }
        }
        return false;
    }

    string addStrings(string a, string b) {
        string res;
        int i = a.size() - 1, j = b.size() - 1, carry = 0;
        while (i >= 0 || j >= 0 || carry) {
            int x = i >= 0 ? a[i--] - '0' : 0;
            int y = j >= 0 ? b[j--] - '0' : 0;
            int sum = x + y + carry;
            res = char(sum % 10 + '0') + res;
            carry = sum / 10;
        }
        return res;
    }
};
```


## 320. Generalized Abbreviation

**Problem:** https://leetcode.com/problems/generalized-abbreviation/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** String, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Bit Manipulation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A word's generalized abbreviation can be constructed by taking any number of non-overlapping and non-adjacent substrings and replacing them with their respective lengths. 

 For example, "abcde" can be abbreviated into:

 "a3e" ( "bcd" turned into "3" ) 
 
 "1bcd1" ( "a" and "e" both turned into "1" ) 
 
 "5" ( "abcde" turned into "5" ) 
 
 "abcde" (no substrings replaced) 

 However, these abbreviations are invalid :

 "23" ( "ab" turned into "2" and "cde" turned into "3" ) is invalid as the substrings chosen are adjacent. 
 
 "22de" ( "ab" turned into "2" and "bc" turned into "2" ) is invalid as the substring chosen overlap. 

 Given a string word , return a list of all the possible generalized abbreviations of word . Return the answer in any order . 

 Example 1: 
 
```
Input:
 word = "word"

Output:
 ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]
```
 
 Example 2: 
 
```
Input:
 word = "a"

Output:
 ["1","a"]
```

 Constraints: 

 1 <= word.length <= 15 
 
 word consists of only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
    void dfs(const string& word, int index, int count, string current,
             vector<string>& result) {
        if (index == (int)word.size())
        {
            if (count) current += to_string(count);
            result.push_back(current);
            return;
        }
        dfs(word, index + 1, count + 1, current, result);
        if (count) current += to_string(count);
        current += word[index];
        dfs(word, index + 1, 0, current, result);
    }
public:
    vector<string> generateAbbreviations(string word) {
        vector<string> result;
        dfs(word, 0, 0, "", result);
        return result;
    }
};
```


## 401. Binary Watch

**Problem:** https://leetcode.com/problems/binary-watch/

**Difficulty:** Easy | **Premium:** No

**Tags:** Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Bit Manipulation

**Data structures (inferred):** Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right. 

 For example, the below binary watch reads "4:51" . 

 [Figure: https://assets.leetcode.com/uploads/2021/04/08/binarywatch.jpg] 
 
 Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent . You may return the answer in any order . 
 
 The hour must not contain a leading zero. 

 For example, "01:00" is not valid. It should be "1:00" . 

 The minute must consist of two digits and may contain a leading zero. 

 For example, "10:2" is not valid. It should be "10:02" . 

 Example 1: 
 
```
Input:
 turnedOn = 1

Output:
 ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
```
 
 Example 2: 
 
```
Input:
 turnedOn = 9

Output:
 []
```

 Constraints: 

 0 <= turnedOn <= 10

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> res;
        for (int h = 0; h < 12; ++h) {
            for (int m = 0; m < 60; ++m) {
                if (__builtin_popcount(h) + __builtin_popcount(m) == turnedOn) {
                    res.push_back(to_string(h) + ":" + (m < 10 ? "0" : "") + to_string(m));
                }
            }
        }
        return res;
    }
};
```


## 411. Minimum Unique Word Abbreviation

**Problem:** https://leetcode.com/problems/minimum-unique-word-abbreviation/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, String, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A string can be abbreviated by replacing any number of non-adjacent substrings with their lengths. For example, a string such as "substitution" could be abbreviated as (but not limited to): 

 "s10n" ( "s ubstitutio n" ) 
 
 "sub4u4" ( "sub stit u tion " ) 
 
 "12" ( " substitution " ) 
 
 "su3i1u2on" ( "su bst i t u ti on" ) 
 
 "substitution" (no substrings replaced) 

 Note that "s55n" ( "s ubsti tutio n" ) is not a valid abbreviation of "substitution" because the replaced substrings are adjacent. 
 
 The length of an abbreviation is the number of letters that were not replaced plus the number of substrings that were replaced. For example, the abbreviation "s10n" has a length of 3 ( 2 letters + 1 substring) and "su3i1u2on" has a length of 9 ( 6 letters + 3 substrings). 
 
 Given a target string target and an array of strings dictionary , return an abbreviation of target with the shortest possible length such that it is not an abbreviation of any string in dictionary . If there are multiple shortest abbreviations, return any of them . 

 Example 1: 
 
```
Input:
 target = "apple", dictionary = ["blade"]

Output:
 "a4"

Explanation:
 The shortest abbreviation of "apple" is "5", but this is also an abbreviation of "blade".
The next shortest abbreviations are "a4" and "4e". "4e" is an abbreviation of blade while "a4" is not.
Hence, return "a4".
```

 Example 2: 
 
```
Input:
 target = "apple", dictionary = ["blade","plain","amber"]

Output:
 "1p3"

Explanation:
 "5" is an abbreviation of both "apple" but also every word in the dictionary.
"a4" is an abbreviation of "apple" but also "amber".
"4e" is an abbreviation of "apple" but also "blade".
"1p3", "2p2", and "3l1" are the next shortest abbreviations of "apple".
Since none of them are abbreviations of words in the dictionary, returning any of them is correct.
```

 Constraints: 

 m == target.length 
 
 n == dictionary.length 
 
 1 <= m <= 21 
 
 0 <= n <= 1000 
 
 1 <= dictionary[i].length <= 100 
 
 log 2 (n) + m <= 21 if n > 0 
 
 target and dictionary[i] consist of lowercase English letters. 
 
 dictionary does not contain target .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
    int n;
    vector<int> differences;
    string target;
    int length(int mask)
    {
        int result = 0, skipped = 0;
        for (int i = 0; i < n; ++i)
        {
            if (mask & (1 << i))
            {
                if (skipped) ++result;
                skipped = 0;
                ++result;
            } else
            {
                ++skipped;
            }
        }
        if (skipped) ++result;
        return result;
    }
    string encode(int mask)
    {
        string result;
        int skipped = 0;
        for (int i = 0; i < n; ++i)
        {
            if (mask & (1 << i))
            {
                if (skipped) result += to_string(skipped);
                skipped = 0;
                result += target[i];
            } else
            {
                ++skipped;
            }
        }
        if (skipped) result += to_string(skipped);
        return result;
    }
public:
    string minAbbreviation(string target, vector<string>& dictionary)
    {
        this->target = target;
        n = target.size();
        differences.clear();
        for (const string& word : dictionary) {
            if ((int)word.size() != n) continue;
            int diff = 0;
            for (int i = 0; i < n; ++i)
            {
                if (word[i] != target[i]) diff |= 1 << i;
            }
            differences.push_back(diff);
        }
        if (differences.empty()) return to_string(n);
        int bestMask = (1 << n) - 1, bestLength = INT_MAX;
        for (int mask = 0; mask < (1 << n); ++mask)
        {
            int len = length(mask);
            if (len >= bestLength) continue;
            bool unique = true;
            for (int diff : differences) {
                if ((mask & diff) == 0)
                {
                    unique = false;
                    break;
                }
            }
            if (unique)
            {
                bestLength = len;
                bestMask = mask;
            }
        }
        return encode(bestMask);
    }
};
```


## 489. Robot Room Cleaner

**Problem:** https://leetcode.com/problems/robot-room-cleaner/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Backtracking, Interactive

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask

**Data structures (inferred):** Ordered set

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot. 
 
 The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot . 
 
 You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees. 
 
 When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell. 
 
 Design an algorithm to clean the entire room using the following APIs: 
 
```
interface Robot {
 // returns true if next cell is open and robot moves into the cell.
 // returns false if next cell is obstacle and robot stays on the current cell.
 boolean move();

 // Robot will stay on the same cell after calling turnLeft/turnRight.
 // Each turn will be 90 degrees.
 void turnLeft();
 void turnRight();

 // Clean the current cell.
 void clean();
}
```

 Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall. 

 Custom testing: 
 
 The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/07/17/lc-grid.jpg] 
 
```
Input:
 room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3

Output:
 Robot cleaned all rooms.

Explanation:
 All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
```

 Example 2: 
 
```
Input:
 room = [[1]], row = 0, col = 0

Output:
 Robot cleaned all rooms.
```

 Constraints: 

 m == room.length 
 
 n == room[i].length 
 
 1 <= m <= 100 
 
 1 <= n <= 200 
 
 room[i][j] is either 0 or 1 . 
 
 0 <= row < m 
 
 0 <= col < n 
 
 room[row][col] == 1 
 
 All the empty cells can be visited from the starting position.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    set<pair<int, int>> visited;
    const int dr[4] = {-1, 0, 1, 0};
    const int dc[4] = {0, 1, 0, -1};

    void goBack(Robot& robot) {
        robot.turnRight();
        robot.turnRight();
        robot.move();
        robot.turnRight();
        robot.turnRight();
    }

    void dfs(Robot& robot, int row, int col, int direction) {
        visited.insert({row, col});
        robot.clean();
        for (int step = 0; step < 4; ++step) {
            int nextDirection = (direction + step) % 4;
            int nr = row + dr[nextDirection];
            int nc = col + dc[nextDirection];
            if (!visited.count({nr, nc}) && robot.move()) {
                dfs(robot, nr, nc, nextDirection);
                goBack(robot);
            }
            robot.turnRight();
        }
    }

public:
    void cleanRoom(Robot& robot) {
        dfs(robot, 0, 0, 0);
    }
};
```


## 491. Non-decreasing Subsequences

**Problem:** https://leetcode.com/problems/non-decreasing-subsequences/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Hash set, Ordered set, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array nums , return all the different possible non-decreasing subsequences of the given array with at least two elements . You may return the answer in any order . 

 Example 1: 
 
```
Input:
 nums = [4,6,7,7]

Output:
 [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
```

 Example 2: 
 
```
Input:
 nums = [4,4,3,2,1]

Output:
 [[4,4]]
```

 Constraints: 

 1 <= nums.length <= 15 
 
 -100 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    void backtrack(vector<int>& nums, int index, vector<int>& current, vector<vector<int>>& result) {
        if (current.size() >= 2) {
            result.push_back(current);
        }
        unordered_set<int> used;

        for (int i = index; i < nums.size(); i++) {
            if ((current.empty() || nums[i] >= current.back()) && used.find(nums[i]) == used.end()) {
                used.insert(nums[i]);
                current.push_back(nums[i]);
                backtrack(nums, i + 1, current, result);
                current.pop_back();
            }
        }
    }

    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(nums, 0, current, result);
        return result;
    }
};
```


## 679. 24 Game

**Problem:** https://leetcode.com/problems/24-game/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Math, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array cards of length 4 . You have four cards, each containing a number in the range [1, 9] . You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24. 
 
 You are restricted with the following rules: 

 The division operator '/' represents real division, not integer division.

 For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12 . 

 Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.

 For example, if cards = [1, 1, 1, 1] , the expression "-1 - 1 - 1 - 1" is not allowed . 

 You cannot concatenate numbers together

 For example, if cards = [1, 2, 1, 2] , the expression "12 + 12" is not valid. 

 Return true if you can get such expression that evaluates to 24 , and false otherwise. 

 Example 1: 
 
```
Input:
 cards = [4,1,8,7]

Output:
 true

Explanation:
 (8-4) * (7-1) = 24
```

 Example 2: 
 
```
Input:
 cards = [1,2,1,2]

Output:
 false
```

 Constraints: 

 cards.length == 4 
 
 1 <= cards[i] <= 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    bool judgePoint24(vector<int>& cards) {
        vector<double> nums(cards.begin(), cards.end());
        return solve(nums);
    }

    bool solve(vector<double>& nums) {
        if (nums.size() == 1) return abs(nums[0] - 24.0) < 1e-6;
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = 0; j < nums.size(); ++j) {
                if (i == j) continue;
                vector<double> next;
                for (int k = 0; k < nums.size(); ++k) {
                    if (k != i && k != j) next.push_back(nums[k]);
                }
                for (double d : {nums[i] + nums[j], nums[i] - nums[j], nums[j] - nums[i],
                                  nums[i] * nums[j], nums[i] / nums[j], nums[j] / nums[i]}) {
                    if (isfinite(d)) {
                        next.push_back(d);
                        if (solve(next)) return true;
                        next.pop_back();
                    }
                }
            }
        }
        return false;
    }
};
```


## 681. Next Closest Time

**Problem:** https://leetcode.com/problems/next-closest-time/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Hash Table, String, Backtracking, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, String Algorithms

**Data structures (inferred):** Hash map / hash set, String

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a time represented in the format "HH:MM" , form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused. 
 
 You may assume the given input string is always valid. For example, "01:34" , "12:09" are all valid. "1:34" , "12:9" are all invalid. 

 Example 1: 
 
```
Input:
 time = "19:34"

Output:
 "19:39"

Explanation:
 The next closest time choosing from digits 
1
, 
9
, 
3
, 
4
, is 
19:39
, which occurs 5 minutes later.
It is not 
19:33
, because this occurs 23 hours and 59 minutes later.
```

 Example 2: 
 
```
Input:
 time = "23:59"

Output:
 "22:22"

Explanation:
 The next closest time choosing from digits 
2
, 
3
, 
5
, 
9
, is 
22:22
.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
```

 Constraints: 

 time.length == 5 
 
 time is a valid time in the form "HH:MM" . 
 
 0 <= HH < 24 
 
 0 <= MM < 60

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string nextClosestTime(string time) {
        bool allowed[10] = {};
        for (char c : time) {
            if (c != ':') {
                allowed[c - '0'] = true;
            }
        }
        int start = stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3, 2));
        for (int delta = 1; delta <= 1440; ++delta) {
            int minute = (start + delta) % 1440;
            int hour = minute / 60;
            int rem = minute % 60;
            string result = string(2 - to_string(hour).size(), '0')
                          + to_string(hour) + ":"
                          + string(2 - to_string(rem).size(), '0')
                          + to_string(rem);
            bool valid = true;
            for (char c : result) {
                if (c != ':' && !allowed[c - '0']) {
                    valid = false;
                }
            }
            if (valid) {
                return result;
            }
        }
        return time;
    }
};
```


## 756. Pyramid Transition Matrix

**Problem:** https://leetcode.com/problems/pyramid-transition-matrix/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, String, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, String Algorithms, Bit Manipulation

**Data structures (inferred):** Hash map, Hash map / hash set, Ordered map, Queue, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top. 
 
 To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks . The patterns are given as a list of three-letter strings allowed , where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block. 

 For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom. 

 You start with a bottom row of blocks bottom , given as a single string, that you must use as the base of the pyramid. 
 
 Given bottom and allowed , return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed , or false otherwise . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/08/26/pyramid1-grid.jpg] 
 
```
Input:
 bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]

Output:
 true

Explanation:
 The allowed triangular patterns are shown on the right.
Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/08/26/pyramid2-grid.jpg] 
 
```
Input:
 bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]

Output:
 false

Explanation:
 The allowed triangular patterns are shown on the right.
Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.
```

 Constraints: 

 2 <= bottom.length <= 6 
 
 0 <= allowed.length <= 216 
 
 allowed[i].length == 3 
 
 The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'} . 
 
 All the values of allowed are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    map<string, vector<string>> vec;
    unordered_map<string, bool> memo;

    bool un_fun(string s) {
        if (s.length() == 1) return true;

        if (memo.find(s) != memo.end()) {
            return memo[s];
        }

        bool ans = false;

        queue<pair<string, int>> q;
        vector<string> p;

        string pfx = s.substr(0, 2);

        for (int i = 0; i < vec[pfx].size(); i++) {
            q.push({ vec[pfx][i], 0 });
        }

        while (!q.empty()) {
            pair<string, int> top = q.front();
            q.pop();

            if (top.second == s.length() - 2) {
                p.push_back(top.first);
            }

            int st_idx = top.second + 1;
            string prev = top.first;

            pfx = s.substr(st_idx, 2);

            for (int i = 0; i < vec[pfx].size(); i++) {
                q.push({ prev + vec[pfx][i], st_idx });
            }
        }

        for (int i = 0; i < p.size(); i++) {
            ans = ans || un_fun(p[i]);
        }

        memo[s] = ans;
        return ans;
    }

    bool pyramidTransition(string bottom, vector<string> &allowed) {
        for (int i = 0; i < allowed.size(); i++) {
            string p = "";
            p += allowed[i][2];
            vec[allowed[i].substr(0, 2)].push_back(p);
        }

        return un_fun(bottom);
    }
};
```


## 784. Letter Case Permutation

**Problem:** https://leetcode.com/problems/letter-case-permutation/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Bit Manipulation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a string s , you can transform every letter individually to be lowercase or uppercase to create another string. 
 
 Return a list of all possible strings we could create . Return the output in any order . 

 Example 1: 
 
```
Input:
 s = "a1b2"

Output:
 ["a1b2","a1B2","A1b2","A1B2"]
```

 Example 2: 
 
```
Input:
 s = "3z4"

Output:
 ["3z4","3Z4"]
```

 Constraints: 

 1 <= s.length <= 12 
 
 s consists of lowercase English letters, uppercase English letters, and digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    void permute(string s,vector<string> &res,int i){
        if(i==s.length()){
            res.push_back(s);
            return;
        }
        if(isalpha(s[i])){
            s[i]=toupper(s[i]);
            permute(s,res,i+1);
            s[i]=tolower(s[i]);
            permute(s,res,i+1);
        }else{
            permute(s,res,i+1);
        }
    }
    vector<string> letterCasePermutation(string s) {
        vector<string> res;
        permute(s,res,0);
        return res;
        
    }
};
```


## 816. Ambiguous Coordinates

**Problem:** https://leetcode.com/problems/ambiguous-coordinates/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Backtracking, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)" . Then, we removed all commas, decimal points, and spaces and ended up with the string s. 

 For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)" . 

 Return a list of strings representing all possibilities for what our original coordinates could have been . 
 
 Our original representation never had extraneous zeroes, so we never started with numbers like "00" , "0.0" , "0.00" , "1.0" , "001" , "00.01" , or any other number that can be represented with fewer digits. Also, a decimal point within a number never occurs without at least one digit occurring before it, so we never started with numbers like ".1" . 
 
 The final answer list can be returned in any order. All coordinates in the final answer have exactly one space between them (occurring after the comma.) 

 Example 1: 
 
```
Input:
 s = "(123)"

Output:
 ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
```

 Example 2: 
 
```
Input:
 s = "(0123)"

Output:
 ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]

Explanation:
 0.0, 00, 0001 or 00.01 are not allowed.
```

 Example 3: 
 
```
Input:
 s = "(00011)"

Output:
 ["(0, 0.011)","(0.001, 1)"]
```

 Constraints: 

 4 <= s.length <= 12 
 
 s[0] == '(' and s[s.length - 1] == ')' . 
 
 The rest of s are digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> ambiguousCoordinates(string s) {
        vector<string> res;
        s = s.substr(1, s.size() - 2);

        for (int i = 1; i < s.size(); ++i) {
            vector<string> left = split(s.substr(0, i));
            vector<string> right = split(s.substr(i));
            for (string& l : left)
                for (string& r : right)
                    res.push_back("(" + l + ", " + r + ")");
        }
        return res;
    }

    vector<string> split(string s) {
        vector<string> res;
        if (s.front() == '0' && s.back() == '0' && s.size() > 1) return res;
        if (s.size() > 1 && s.front() == '0') res.push_back("0." + s.substr(1));
        else {
            res.push_back(s);
            for (int i = 1; i < s.size(); ++i)
                if (s.back() != '0')
                    res.push_back(s.substr(0, i) + "." + s.substr(i));
        }
        return res;
    }
};
```


## 842. Split Array into Fibonacci Sequence

**Problem:** https://leetcode.com/problems/split-array-into-fibonacci-sequence/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string of digits num , such as "123456579" . We can split it into a Fibonacci-like sequence [123, 456, 579] . 
 
 Formally, a Fibonacci-like sequence is a list f of non-negative integers such that: 

 0 <= f[i] < 2 31 , (that is, each integer fits in a 32-bit signed integer type), 
 
 f.length >= 3 , and 
 
 f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2 . 

 Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself. 
 
 Return any Fibonacci-like sequence split from num , or return [] if it cannot be done. 

 Example 1: 
 
```
Input:
 num = "1101111"

Output:
 [11,0,11,11]

Explanation:
 The output [110, 1, 111] would also be accepted.
```

 Example 2: 
 
```
Input:
 num = "112358130"

Output:
 []

Explanation:
 The task is impossible.
```

 Example 3: 
 
```
Input:
 num = "0123"

Output:
 []

Explanation:
 Leading zeroes are not allowed, so "01", "2", "3" is not valid.
```

 Constraints: 

 1 <= num.length <= 200 
 
 num contains only digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool dfs(int idx, string& s, vector<int>& seq) {
        if (idx == s.size()) return seq.size() >= 3;

        long num = 0;
        for (int i = idx; i < s.size(); ++i) {
            if (i > idx && s[idx] == '0') break;
            num = num * 10 + (s[i] - '0');
            if (num > INT_MAX) break;

            if (seq.size() >= 2 && num != (long)seq[seq.size() - 1] + seq[seq.size() - 2])
                continue;

            seq.push_back(num);
            if (dfs(i + 1, s, seq)) return true;
            seq.pop_back();
        }
        return false;
    }

    vector<int> splitIntoFibonacci(string num) {
        vector<int> seq;
        dfs(0, num, seq);
        return seq;
    }
};
```


## 949. Largest Time for Given Digits

**Problem:** https://leetcode.com/problems/largest-time-for-given-digits/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String, Backtracking, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once . 
 
 24-hour times are formatted as "HH:MM" , where HH is between 00 and 23 , and MM is between 00 and 59 . The earliest 24-hour time is 00:00 , and the latest is 23:59 . 
 
 Return the latest 24-hour time in "HH:MM" format . If no valid time can be made, return an empty string. 

 Example 1: 
 
```
Input:
 arr = [1,2,3,4]

Output:
 "23:41"

Explanation:
 The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
```

 Example 2: 
 
```
Input:
 arr = [5,5,5,5]

Output:
 ""

Explanation:
 There are no valid 24-hour times as "55:55" is not valid.
```

 Constraints: 

 arr.length == 4 
 
 0 <= arr[i] <= 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string largestTimeFromDigits(vector<int>& arr) {
        string res = "";
        sort(arr.begin(), arr.end());
        do {
            int h = arr[0] * 10 + arr[1], m = arr[2] * 10 + arr[3];
            if (h < 24 && m < 60) {
                char buf[6];
                sprintf(buf, "%02d:%02d", h, m);
                res = max(res, string(buf));
            }
        } while (next_permutation(arr.begin(), arr.end()));
        return res;
    }
};
```


## 980. Unique Paths III

**Problem:** https://leetcode.com/problems/unique-paths-iii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Backtracking, Bit Manipulation, Matrix, Hamiltonian Path

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an m x n integer array grid where grid[i][j] could be: 

 1 representing the starting square. There is exactly one starting square. 
 
 2 representing the ending square. There is exactly one ending square. 
 
 0 representing empty squares we can walk over. 
 
 -1 representing obstacles that we cannot walk over. 

 Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/08/02/lc-unique1.jpg] 
 
```
Input:
 grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]

Output:
 2

Explanation:
 We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/08/02/lc-unique2.jpg] 
 
```
Input:
 grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]

Output:
 4

Explanation:
 We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/08/02/lc-unique3-.jpg] 
 
```
Input:
 grid = [[0,1],[2,0]]

Output:
 0

Explanation:
 There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
```

 Constraints: 

 m == grid.length 
 
 n == grid[i].length 
 
 1 <= m, n <= 20 
 
 1 <= m * n <= 20 
 
 -1 <= grid[i][j] <= 2 
 
 There is exactly one starting cell and one ending cell.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
    // Dimensions 
    int m, n;

    // Direction Vectors
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};

public:
    // function to check for the validity of CELLij
    bool isvalid(int i, int j)
    {
        return i >= 0 and j >= 0 and i < m and j < n;
    }

    int dfs(int i, int j, int left, pair<int, int> dest, vector<vector<int>> &grid)
    {
        // Base case
        if (left == -1 and pair<int, int>(i, j) == dest)
            return 1;

        // Mark visited
        grid[i][j] = -1;

        int ans = 0;
        for (int k = 0; k < 4; k++)
        {
            int x = i + dx[k];
            int y = j + dy[k];

            // Add up all possibilities to answer
            if (isvalid(x, y) and grid[x][y] != -1)
                ans += dfs(x, y, left - 1, dest, grid);
        }

        // Backtrack
        grid[i][j] = 0;

        return ans;
    }

    int uniquePathsIII(vector<vector<int>> &grid)
    {
        m = grid.size(), n = grid[0].size();

        pair<int, int> src, dest;
        int empty = 0;

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 0)
                    empty++;
                if (grid[i][j] == 1)
                    src = {i, j};
                if (grid[i][j] == 2)
                    dest = {i, j};
            }
        }

        return dfs(src.first, src.second, empty, dest, grid);
    }
};
```


## 1079. Letter Tile Possibilities

**Problem:** https://leetcode.com/problems/letter-tile-possibilities/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, String, Backtracking, Counting

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, String Algorithms

**Data structures (inferred):** Hash map / hash set, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You have n    tiles , where each tile has one letter tiles[i] printed on it. 
 
 Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles . 

 Example 1: 
 
```
Input:
 tiles = "AAB"

Output:
 8

Explanation: 
The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
```

 Example 2: 
 
```
Input:
 tiles = "AAABBC"

Output:
 188
```

 Example 3: 
 
```
Input:
 tiles = "V"

Output:
 1
```

 Constraints: 

 1 <= tiles.length <= 7 
 
 tiles consists of uppercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int numTilePossibilities(string tiles) {
        vector<int> freq(26, 0);
        for (char c : tiles) freq[c - 'A']++;
        return backtrack(freq);
    }

    int backtrack(vector<int>& freq) {
        int sum = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                sum++;
                freq[i]--;
                sum += backtrack(freq);
                freq[i]++;
            }
        }
        return sum;
    }
};
```


## 1088. Confusing Number II

**Problem:** https://leetcode.com/problems/confusing-number-ii/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Math, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Math / Number Theory

**Data structures (inferred):** Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid . 
 
 We can rotate digits of a number by 180 degrees to form new digits. 

 When 0 , 1 , 6 , 8 , and 9 are rotated 180 degrees, they become 0 , 1 , 9 , 8 , and 6 respectively. 
 
 When 2 , 3 , 4 , 5 , and 7 are rotated 180 degrees, they become invalid . 

 Note that after rotating a number, we can ignore leading zeros. 

 For example, after rotating 8000 , we have 0008 which is considered as just 8 . 

 Given an integer n , return the number of confusing numbers in the inclusive range [1, n] . 

 Example 1: 
 
```
Input:
 n = 20

Output:
 6

Explanation:
 The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
```

 Example 2: 
 
```
Input:
 n = 100

Output:
 19

Explanation:
 The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
```

 Constraints: 

 1 <= n <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    int limit;
    int count = 0;
    const vector<int> digits = {0, 1, 6, 8, 9};
    const vector<int> rotated = {0, 1, 9, 8, 6};

    void dfs(long long value, long long rotation, long long place) {
        if (value > limit) {
            return;
        }
        if (value != 0 && value != rotation) {
            ++count;
        }
        for (int i = 0; i < 5; ++i) {
            if (value == 0 && digits[i] == 0) {
                continue;
            }
            long long next = value * 10 + digits[i];
            if (next <= limit) {
                dfs(next, rotated[i] * place + rotation, place * 10);
            }
        }
    }

public:
    int confusingNumberII(int n) {
        limit = n;
        count = 0;
        dfs(0, 0, 1);
        return count;
    }
};
```


## 1219. Path with Maximum Gold

**Problem:** https://leetcode.com/problems/path-with-maximum-gold/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking, Matrix

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

In a gold mine grid of size m x n , each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty. 
 
 Return the maximum amount of gold you can collect under the conditions: 

 Every time you are located in a cell you will collect all the gold in that cell. 
 
 From your position, you can walk one step to the left, right, up, or down. 
 
 You can't visit the same cell more than once. 
 
 Never visit a cell with 0 gold. 
 
 You can start and stop collecting gold from any position in the grid that has some gold. 

 Example 1: 
 
```
Input:
 grid = [[0,6,0],[5,8,7],[0,9,0]]

Output:
 24

Explanation:

[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
```

 Example 2: 
 
```
Input:
 grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]

Output:
 28

Explanation:

[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
```

 Constraints: 

 m == grid.length 
 
 n == grid[i].length 
 
 1 <= m, n <= 15 
 
 0 <= grid[i][j] <= 100 
 
 There are at most 25 cells containing gold.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#define AXIS 4
int max_gold = 0;
class Solution
{
    int x_axis[AXIS];
    int y_axis[AXIS];
public:
    Solution() : x_axis{ 0,-1,0,1 }, y_axis{ 1,0,-1,0 }
    {
    }
    bool check_equal_elem(vector<vector<int>> grid , int row_grid , int col_grid)
    {
        int source = grid[0][0];
        for(int i=0;i<row_grid;i++)
        for (int j = 1; j < col_grid; j++)
        {
            if (grid[i][j] != source) return false;
        }
        return true;
    }
    void check_max(int i, int j, vector<vector<int>> grid, int row_grid, int col_grid, int  sum)
    {
        sum += grid[i][j];
        grid[i][j] = -grid[i][j];
        if (sum > max_gold)
        {
            max_gold = sum;
        }

        for (int k = 0; k < AXIS; k++)
        {
            int new_x = i + x_axis[k];
            int new_y = j + y_axis[k];
            if (new_x >= 0 && new_y >= 0 && new_x < row_grid && new_y < col_grid && grid[new_x][new_y] > 0)
                check_max(new_x, new_y, grid, row_grid, col_grid, sum);
        }
        grid[i][j] = -grid[i][j];
    }
    int getMaximumGold(vector<vector<int>>& grid)
    {
        int row_grid = grid.size();
        int col_grid = grid[0].size();
        max_gold = 0;

        bool equal_elem = check_equal_elem(grid, row_grid, col_grid);
        if (equal_elem)
        {
            return row_grid * col_grid * grid[0][0];
        }

        for (int i = 0; i < row_grid; i++)
        {
            for (int j = 0; j < col_grid; j++)
            {
                if (grid[i][j])
                {
                    int sum = 0;
                    check_max(i, j, grid, row_grid, col_grid, sum);
                }
            }
        }
        return max_gold;
    }
};
```


## 1238. Circular Permutation in Binary Representation

**Problem:** https://leetcode.com/problems/circular-permutation-in-binary-representation/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Math / Number Theory, Bit Manipulation

**Data structures (inferred):** Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given 2 integers n and start . Your task is return any permutation p  of (0,1,2.....,2^n -1) such that : 

 p[0] = start 
 
 p[i] and p[i+1]  differ by only one bit in their binary representation. 
 
 p[0] and p[2^n -1]  must also differ by only one bit in their binary representation. 

 Example 1: 
 
```
Input:
 n = 2, start = 3

Output:
 [3,2,0,1]

Explanation:
 The binary representation of the permutation is (11,10,00,01). 
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]
```

 Example 2: 
 
```
Input:
 n = 3, start = 2

Output:
 [2,6,7,5,4,0,1,3]

Explanation:
 The binary representation of the permutation is (010,110,111,101,100,000,001,011).
```

 Constraints: 

 1 <= n <= 16 
 
 0 <= start < 2 ^ n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> circularPermutation(int n, int start) {
        vector<int> res;
        for (int i = 0; i < (1 << n); ++i)
            res.push_back(start ^ (i ^ (i >> 1)));
        return res;
    }
};
```


## 1239. Maximum Length of a Concatenated String with Unique Characters

**Problem:** https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash set, Ordered set, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array of strings arr . A string s is formed by the concatenation of a subsequence of arr that has unique characters . 
 
 Return the maximum possible length of s . 
 
 A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements. 

 Example 1: 
 
```
Input:
 arr = ["un","iq","ue"]

Output:
 4

Explanation:
 All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
```

 Example 2: 
 
```
Input:
 arr = ["cha","r","act","ers"]

Output:
 6

Explanation:
 Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
```

 Example 3: 
 
```
Input:
 arr = ["abcdefghijklmnopqrstuvwxyz"]

Output:
 26

Explanation:
 The only string in arr has all 26 characters.
```

 Constraints: 

 1 <= arr.length <= 16 
 
 1 <= arr[i].length <= 26 
 
 arr[i] contains only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int maxLength(vector<string>& arr) {
        return backtrack(arr, "", 0);
    }

    int backtrack(vector<string>& arr, string current, int index) {
        unordered_set<char> charSet(current.begin(), current.end());
        if (charSet.size() != current.size()) return 0;
        
        int maxLen = current.size();
        for (int i = index; i < arr.size(); i++) {
            maxLen = max(maxLen, backtrack(arr, current + arr[i], i + 1));
        }
        return maxLen;
    }
};
```


## 1240. Tiling a Rectangle with the Fewest Squares

**Problem:** https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

**Difficulty:** Hard | **Premium:** No

**Tags:** Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask

**Data structures (inferred):** Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a rectangle of size n x m , return the minimum number of integer-sided squares that tile the rectangle . 

 Example 1: 
 
 [Figure: https://assets.leetcode.com/uploads/2019/10/17/sample_11_1592.png] 
 
```
Input:
 n = 2, m = 3

Output:
 3

Explanation:
 
3
 squares are necessary to cover the rectangle.

2
 (squares of 
1x1
)

1
 (square of 
2x2
)
```

 Example 2: 
 
 [Figure: https://assets.leetcode.com/uploads/2019/10/17/sample_22_1592.png] 
 
```
Input:
 n = 5, m = 8

Output:
 5
```

 Example 3: 
 
 [Figure: https://assets.leetcode.com/uploads/2019/10/17/sample_33_1592.png] 
 
```
Input:
 n = 11, m = 13

Output:
 6
```

 Constraints: 

 1 <= n, m <= 13

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int res = INT_MAX;

    void dfs(int n, int m, vector<int>& height, int cur) {
        if (cur >= res) return;
        int minH = INT_MAX, idx = -1;
        for (int i = 0; i < m; ++i) {
            if (height[i] < minH) {
                minH = height[i];
                idx = i;
            }
        }
        if (minH == n) {
            res = min(res, cur);
            return;
        }

        int j = idx;
        while (j < m && height[j] == minH && j - idx + 1 + minH <= n) ++j;
        --j;

        for (int len = j - idx + 1; len >= 1; --len) {
            for (int k = 0; k < len; ++k) height[idx + k] += len;
            dfs(n, m, height, cur + 1);
            for (int k = 0; k < len; ++k) height[idx + k] -= len;
        }
    }

    int tilingRectangle(int n, int m) {
        if (n < m) swap(n, m);
        vector<int> height(m, 0);
        dfs(n, m, height, 0);
        return res;
    }
};
```


## 1286. Iterator for Combination

**Problem:** https://leetcode.com/problems/iterator-for-combination/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Backtracking, Design, Iterator

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Stack / Queue

**Data structures (inferred):** String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Design the CombinationIterator class: 

 CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments. 
 
 next() Returns the next combination of length combinationLength in lexicographical order . 
 
 hasNext() Returns true if and only if there exists a next combination. 

 Example 1: 
 
```
Input

["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]

Output

[null, "ab", true, "ac", true, "bc", false]

Explanation

CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next(); // return "ab"
itr.hasNext(); // return True
itr.next(); // return "ac"
itr.hasNext(); // return True
itr.next(); // return "bc"
itr.hasNext(); // return False
```

 Constraints: 

 1 <= combinationLength <= characters.length <= 15 
 
 All the characters of characters are unique . 
 
 At most 10 4 calls will be made to next and hasNext . 
 
 It is guaranteed that all calls of the function next are valid.

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <vector>
using namespace std;

class CombinationIterator {
public:
    vector<string> combinations;
    int idx = 0;

    CombinationIterator(string characters, int combinationLength) {
        generateCombinations(characters, combinationLength, 0, "");
    }

    void generateCombinations(string& chars, int length, int start, string comb) {
        if (comb.size() == length) {
            combinations.push_back(comb);
            return;
        }
        for (int i = start; i < chars.size(); ++i) {
            generateCombinations(chars, length, i + 1, comb + chars[i]);
        }
    }

    string next() {
        return combinations[idx++];
    }

    bool hasNext() {
        return idx < combinations.size();
    }
};
```


## 1307. Verbal Arithmetic Puzzle

**Problem:** https://leetcode.com/problems/verbal-arithmetic-puzzle/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Math, String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an equation, represented by words on the left side and the result on the right side. 
 
 You need to check if the equation is solvable under the following rules: 

 Each character is decoded as one digit (0 - 9). 
 
 No two characters can map to the same digit. 
 
 Each words[i] and result are decoded as one number without leading zeros. 
 
 Sum of numbers on the left side ( words ) will equal to the number on the right side ( result ). 

 Return true if the equation is solvable, otherwise return false . 

 Example 1: 
 
```
Input:
 words = ["SEND","MORE"], result = "MONEY"

Output:
 true

Explanation:
 Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" , 9567 + 1085 = 10652
```

 Example 2: 
 
```
Input:
 words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"

Output:
 true

Explanation:
 Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" , 650 + 68782 + 68782 = 138214
```

 Example 3: 
 
```
Input:
 words = ["LEET","CODE"], result = "POINT"

Output:
 false

Explanation:
 There is no possible mapping to satisfy the equation, so we return false.
Note that two different characters cannot map to the same digit.
```

 Constraints: 

 2 <= words.length <= 5 
 
 1 <= words[i].length, result.length <= 7 
 
 words[i], result contain only uppercase English letters. 
 
 The number of different characters used in the expression is at most 10 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    int map[256];
    int visited[10];
public:
    bool isSolvable(vector<string>& words, string result) {
        for(int i=0; i<256; i++)
            map[i] = -1;
        reverse(result.begin(), result.end());
        for(auto& word: words) {
            if(word.size()>result.size())
                return false;
            reverse(word.begin(), word.end());
        }
        return dfs(words, result, 0, 0, 0);
    }
    bool dfs(vector<string>& words, string result, int j, int i, int sum) {
        if( j == result.size() ) {
            if( sum != 0 )
                return false;
            if(result.size()>1 && map[result.back()]==0) //result has leading zero.
                return false;
            return true;
        };
        if( i == words.size() ) { //result row
            if(map[ result[j] ] != -1) {//already mapped.
                if(map[ result[j] ] != sum%10)
                    return false;
                else
                    return dfs(words, result, j+1, 0, sum/10);
            } else {
                if(visited[sum%10] == 1)
                    return false;
                map[result[j]] = sum%10;
                visited[sum%10] = 1;
                if(dfs(words, result, j+1, 0, sum/10))
                    return true;
                map[result[j]] = -1;
                visited[sum%10] = 0;
                return false;
            }
        };

        if( j >= words[i].length() )
            return dfs(words, result, j, i+1, sum);
        char ch = words[i][j];
        if(map[ch]!=-1) {
            if(words[i].size()>1 && j==words.size()-1 && map[ch]==0) //leading zero
                return false;
            return dfs(words, result, j, i+1, sum+map[ch]);
        } else {
            for(int d=0; d<=9; d++) {
                if(visited[d])
                    continue;
                if(d==0 && words[i].size()>1 && j==words[i].size()-1)
                    continue;
                map[ch] = d;
                visited[d] = 1;
                if(dfs(words, result, j, i+1, sum+d))
                    return true;
                map[ch] = -1;
                visited[d] = 0;
            }
            return false;
        }
        return true;
    }
};
```


## 1415. The k-th Lexicographical String of All Happy Strings of Length n

**Problem:** https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A happy string is a string that: 

 consists only of letters of the set ['a', 'b', 'c'] . 
 
 s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed). 

 For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings. 
 
 Given two integers n and k , consider a list of all happy strings of length n sorted in lexicographical order. 
 
 Return the kth string of this list or return an empty string if there are less than k happy strings of length n . 

 Example 1: 
 
```
Input:
 n = 1, k = 3

Output:
 "c"

Explanation:
 The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
```

 Example 2: 
 
```
Input:
 n = 1, k = 4

Output:
 ""

Explanation:
 There are only 3 happy strings of length 1.
```

 Example 3: 
 
```
Input:
 n = 3, k = 9

Output:
 "cab"

Explanation:
 There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9
th
 string = "cab"
```

 Constraints: 

 1 <= n <= 10 
 
 1 <= k <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    void dfs(int n, int k, string& cur, int& count, string& answer) {
        if (!answer.empty()) return;
        if ((int)cur.size() == n) {
            if (++count == k) answer = cur;
            return;
        }
        for (char c = 'a'; c <= 'c'; ++c) {
            if (!cur.empty() && cur.back() == c) continue;
            cur.push_back(c);
            dfs(n, k, cur, count, answer);
            cur.pop_back();
            if (!answer.empty()) return;
        }
    }
public:
    string getHappyString(int n, int k) {
        string cur, ans;
        int count = 0;
        dfs(n, k, cur, count, ans);
        return ans;
    }
};
```


## 1593. Split a String Into the Max Number of Unique Substrings

**Problem:** https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, String Algorithms

**Data structures (inferred):** Hash map / hash set, Hash set, Ordered set, String

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a string  s ,  return the maximum number of unique substrings that the given string can be split into . 
 
 You can split string  s into any list of  non-empty substrings , where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique . 
 
 A substring is a contiguous sequence of characters within a string. 

 Example 1: 
 
```
Input:
 s = "ababccc"

Output:
 5

Explanation
: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
```

 Example 2: 
 
```
Input:
 s = "aba"

Output:
 2

Explanation
: One way to split maximally is ['a', 'ba'].
```

 Example 3: 
 
```
Input:
 s = "aa"

Output:
 1

Explanation
: It is impossible to split the string any further.
```

 Constraints: 

 1 <= s.length <= 16 

 s contains only lower case English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int maxUniqueSplit(string s) {
        unordered_set<string> seen;
        return dfs(s, 0, seen);
    }

    int dfs(const string& s, int start, unordered_set<string>& seen) {
        if (start == s.size()) return 0;
        int res = 0;
        for (int end = start + 1; end <= s.size(); ++end) {
            string substr = s.substr(start, end - start);
            if (!seen.count(substr)) {
                seen.insert(substr);
                res = max(res, 1 + dfs(s, end, seen));
                seen.erase(substr);
            }
        }
        return res;
    }
};
```


## 1601. Maximum Number of Achievable Transfer Requests

**Problem:** https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Backtracking, Bit Manipulation, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

We have n buildings numbered from 0 to n - 1 . Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in. 
 
 You are given an array requests where requests[i] = [from i , to i ] represents an employee's request to transfer from building from i to building to i . 
 
 All buildings are full , so a list of requests is achievable only if for each building, the net change in employee transfers is zero . This means the number of employees leaving is equal to the number of employees moving in . For example if n = 3 and two employees are leaving building 0 , one is leaving building 1 , and one is leaving building 2 , there should be two employees moving to building 0 , one employee moving to building 1 , and one employee moving to building 2 . 
 
 Return the maximum number of achievable requests . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/10/move1.jpg] 
 
```
Input:
 n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]

Output:
 5

Explantion:
 Let's see the requests:
From building 0 we have employees x and y and both want to move to building 1.
From building 1 we have employees a and b and they want to move to buildings 2 and 0 respectively.
From building 2 we have employee z and they want to move to building 0.
From building 3 we have employee c and they want to move to building 4.
From building 4 we don't have any requests.
We can achieve the requests of users x and b by swapping their places.
We can achieve the requests of users y, a and z by swapping the places in the 3 buildings.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/10/move2.jpg] 
 
```
Input:
 n = 3, requests = [[0,0],[1,2],[2,1]]

Output:
 3

Explantion:
 Let's see the requests:
From building 0 we have employee x and they want to stay in the same building 0.
From building 1 we have employee y and they want to move to building 2.
From building 2 we have employee z and they want to move to building 1.
We can achieve all the requests.
```

 Example 3: 
 
```
Input:
 n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]

Output:
 4
```

 Constraints: 

 1 <= n <= 20 
 
 1 <= requests.length <= 16 
 
 requests[i].length == 2 
 
 0 <= from i , to i < n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
    int maxReq = 0;

    void backtrack(int i, int count, vector<int>& indegree, vector<vector<int>>& requests) {
        if (i == requests.size()) {
            for (int bal : indegree)
                if (bal != 0) return;
            maxReq = max(maxReq, count);
            return;
        }

        // Accept request
        indegree[requests[i][0]]--;
        indegree[requests[i][1]]++;
        backtrack(i + 1, count + 1, indegree, requests);
        indegree[requests[i][0]]++;
        indegree[requests[i][1]]--;

        // Reject request
        backtrack(i + 1, count, indegree, requests);
    }

public:
    int maximumRequests(int n, vector<vector<int>>& requests) {
        vector<int> indegree(n, 0);
        backtrack(0, 0, indegree, requests);
        return maxReq;
    }
};
```


## 1718. Construct the Lexicographically Largest Valid Sequence

**Problem:** https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer n , find a sequence with elements in the range [1, n] that satisfies all of the following: 

 The integer 1 occurs once in the sequence. 
 
 Each integer between 2 and n occurs twice in the sequence. 
 
 For every integer i between 2 and n , the distance between the two occurrences of i is exactly i . 

 The distance between two numbers on the sequence, a[i] and a[j] , is the absolute difference of their indices, |j - i| . 
 
 Return the lexicographically largest sequence . It is guaranteed that under the given constraints, there is always a solution. 
 
 A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b . For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5 . 

 Example 1: 
 
```
Input:
 n = 3

Output:
 [3,1,2,3,2]

Explanation:
 [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
```

 Example 2: 
 
```
Input:
 n = 5

Output:
 [5,3,1,4,3,5,2,4,2]
```

 Constraints: 

 1 <= n <= 20

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
 bool dfs(int pos,int n,vector<int>& a,vector<int>& used){
  while(pos<(int)a.size() && a[pos])++pos;
  if(pos==(int)a.size())return true;
  for(int x=n;x>=1;--x){
   if(used[x])continue;
   if(x>1 && (pos+x>=(int)a.size() || a[pos+x]))continue;
   used[x]=1;a[pos]=x;if(x>1)a[pos+x]=x;
   if(dfs(pos+1,n,a,used))return true;
   a[pos]=0;if(x>1)a[pos+x]=0;used[x]=0;
  }
  return false;
 }
public:
 vector<int> constructDistancedSequence(int n){
  vector<int> a(2*n-1),used(n+1);dfs(0,n,a,used);return a;
 }
};
```


## 1849. Splitting a String Into Descending Consecutive Values

**Problem:** https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Backtracking, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string s that consists of only digits. 
 
 Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1 . 

 For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89] . The values are in descending order and adjacent values differ by 1 , so this way is valid. 
 
 Another example, the string s = "001" can be split into ["0", "01"] , ["00", "1"] , or ["0", "0", "1"] . However all the ways are invalid because they have numerical values [0,1] , [0,1] , and [0,0,1] respectively, all of which are not in descending order. 

 Return true if it is possible to split s ​​​​​​ as described above , or false otherwise. 
 
 A substring is a contiguous sequence of characters in a string. 

 Example 1: 
 
```
Input:
 s = "1234"

Output:
 false

Explanation:
 There is no valid way to split s.
```

 Example 2: 
 
```
Input:
 s = "050043"

Output:
 true

Explanation:
 s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.
```

 Example 3: 
 
```
Input:
 s = "9080701"

Output:
 false

Explanation:
 There is no valid way to split s.
```

 Constraints: 

 1 <= s.length <= 20 
 
 s only consists of digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    long long int mx=9999999999; // as max of s.size()==20 so if any number exceeds mx it will not be valid as we will not be able to make two partitions then, according to the situation given. 
    bool helper(string& s,int i,int j,long long int prev,int n)
    {
       // if we are at the last index then, we have to just check if the (prev-pres)==1.
       // if that condition is true, then it means we got a correct match
        if(j==n-1)
        {
            string str=s.substr(i,j-i+1);
            long long int pres=stoll(str);
            if(prev-pres==1)
                return true;
            return false;
        }
           bool m=false;
           string str=s.substr(i,j-i+1);
           long long int pres=stoll(str); 
           if(pres>mx)
               return false;
            if(prev==-1 || prev-pres==1)
                m=m || helper(s,j+1,j+1,pres,n); // in this step we are calling the function  keeping in mind that we have found the integer till this index and freshly calculating the integer from the next index, that's why passed (j+1,j+1) inside the function. 
            
        m=m || helper(s,i,j+1,prev,n);  // in this step we are calling the function keeping in mind that we will extend the integer to the next index and passing the prev val as it is. 
        
        return m; 
    }
    bool splitString(string s) {
        int n=s.size();
        long long int prev=-1;
        return helper(s,0,0,prev,n);
    }
};
```


## 1863. Sum of All Subset XOR Totals

**Problem:** https://leetcode.com/problems/sum-of-all-subset-xor-totals/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Math / Number Theory, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

The XOR total of an array is defined as the bitwise XOR of all its elements , or 0 if the array is empty . 

 For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1 . 

 Given an array nums , return the sum of all XOR totals for every subset of nums .  
 
 Note: Subsets with the same elements should be counted multiple times. 
 
 An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b . 

 Example 1: 
 
```
Input:
 nums = [1,3]

Output:
 6

Explanation: 
The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6
```

 Example 2: 
 
```
Input:
 nums = [5,1,6]

Output:
 28

Explanation: 
The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
```

 Example 3: 
 
```
Input:
 nums = [3,4,5,6,7,8]

Output:
 480

Explanation:
 The sum of all XOR totals for every subset is 480.
```

 Constraints: 

 1 <= nums.length <= 12 
 
 1 <= nums[i] <= 20

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int subsetXORSum(vector<int>& nums){int x=0;for(int v:nums)x|=v;return x*(1<<((int)nums.size()-1));}};
```


## 1980. Find Unique Binary String

**Problem:** https://leetcode.com/problems/find-unique-binary-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, String, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array of strings nums containing n unique binary strings each of length n , return a binary string of length n that does not appear in nums . If there are multiple answers, you may return any of them . 

 Example 1: 
 
```
Input:
 nums = ["01","10"]

Output:
 "11"

Explanation:
 "11" does not appear in nums. "00" would also be correct.
```

 Example 2: 
 
```
Input:
 nums = ["00","01"]

Output:
 "11"

Explanation:
 "11" does not appear in nums. "10" would also be correct.
```

 Example 3: 
 
```
Input:
 nums = ["111","011","001"]

Output:
 "101"

Explanation:
 "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
```

 Constraints: 

 n == nums.length 
 
 1 <= n <= 16 
 
 nums[i].length == n 
 
 nums[i] is either '0' or '1' . 
 
 All the strings of nums are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        string res;
        for (int i = 0; i < nums.size(); ++i)
            res += nums[i][i] == '0' ? '1' : '0';
        return res;
    }
};
```


## 2044. Count Number of Maximum Bitwise-OR Subsets

**Problem:** https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking, Bit Manipulation, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array nums , find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR . 
 
 An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b . Two subsets are considered different if the indices of the elements chosen are different. 
 
 The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] ( 0-indexed ). 

 Example 1: 
 
```
Input:
 nums = [3,1]

Output:
 2

Explanation:
 The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
```

 Example 2: 
 
```
Input:
 nums = [2,2,2]

Output:
 7

Explanation:
 All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 2
3
 - 1 = 7 total subsets.
```

 Example 3: 
 
```
Input:
 nums = [3,2,1,5]

Output:
 6

Explanation:
 The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
```

 Constraints: 

 1 <= nums.length <= 16 
 
 1 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums){int n=nums.size(),target=0,ans=0;
        for(int x:nums)target|=x;
        for(int mask=1;mask<(1<<n);++mask){int v=0;
            for(int i=0;i<n;++i)if(mask>>i&1)v|=nums[i];
            if(v==target)++ans;
        }
        return ans;
    }
};
```


## 2048. Next Greater Numerically Balanced Number

**Problem:** https://leetcode.com/problems/next-greater-numerically-balanced-number/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, Math, Backtracking, Counting, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Hashing / Frequency Counting, Math / Number Theory

**Data structures (inferred):** Hash map / hash set

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

An integer x is numerically balanced if for every digit d in the number x , there are exactly d occurrences of that digit in x . 
 
 Given an integer n , return the smallest numerically balanced number strictly greater than n . 

 Example 1: 
 
```
Input:
 n = 1

Output:
 22

Explanation:
 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
```

 Example 2: 
 
```
Input:
 n = 1000

Output:
 1333

Explanation:
 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
```

 Example 3: 
 
```
Input:
 n = 3000

Output:
 3133

Explanation:
 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
```

 Constraints: 

 0 <= n <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int nextBeautifulNumber(int n){int best=INT_MAX;
        for(int mask=1;mask<(1<<7);++mask){string s;
            for(int d=1;d<=7;++d)if(mask>>(d-1)&1)s.append(d,char('0'+d));
            if(s.size()>7)continue;
            sort(s.begin(),s.end());
            do{int x=stoi(s);if(x>n)best=min(best,x);}
            while(next_permutation(s.begin(),s.end()));
        }
        return best;
    }
};
```


## 2056. Number of Valid Move Combinations On Chessboard

**Problem:** https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, String, Backtracking, Simulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There is an 8 x 8 chessboard containing n pieces (rooks, queens, or bishops). You are given a string array pieces of length n , where pieces[i] describes the type (rook, queen, or bishop) of the i th piece. In addition, you are given a 2D integer array positions also of length n , where positions[i] = [r i , c i ] indicates that the i th piece is currently at the 1-based coordinate (r i , c i ) on the chessboard. 
 
 When making a move for a piece, you choose a destination square that the piece will travel toward and stop on. 

 A rook can only travel horizontally or vertically from (r, c) to the direction of (r+1, c) , (r-1, c) , (r, c+1) , or (r, c-1) . 
 
 A queen can only travel horizontally, vertically, or diagonally from (r, c) to the direction of (r+1, c) , (r-1, c) , (r, c+1) , (r, c-1) , (r+1, c+1) , (r+1, c-1) , (r-1, c+1) , (r-1, c-1) . 
 
 A bishop can only travel diagonally from (r, c) to the direction of (r+1, c+1) , (r+1, c-1) , (r-1, c+1) , (r-1, c-1) . 

 You must make a move for every piece on the board simultaneously. A move combination consists of all the moves performed on all the given pieces. Every second, each piece will instantaneously travel one square towards their destination if they are not already at it. All pieces start traveling at the 0 th second. A move combination is invalid if, at a given time, two or more pieces occupy the same square. 
 
 Return the number of valid move combinations ​​​​​. 
 
 Notes: 

 No two pieces will start in the same square. 
 
 You may choose the square a piece is already on as its destination . 
 
 If two pieces are directly adjacent to each other, it is valid for them to move past each other and swap positions in one second. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/09/23/a1.png] 
 
```
Input:
 pieces = ["rook"], positions = [[1,1]]

Output:
 15

Explanation:
 The image above shows the possible squares the piece can move to.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/09/23/a2.png] 
 
```
Input:
 pieces = ["queen"], positions = [[1,1]]

Output:
 22

Explanation:
 The image above shows the possible squares the piece can move to.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/09/23/a3.png] 
 
```
Input:
 pieces = ["bishop"], positions = [[4,3]]

Output:
 12

Explanation:
 The image above shows the possible squares the piece can move to.
```

 Constraints: 

 n == pieces.length 
 
 n == positions.length 
 
 1 <= n <= 4 
 
 pieces only contains the strings "rook" , "queen" , and "bishop" . 
 
 There will be at most one queen on the chessboard. 
 
 1 <= r i , c i <= 8 
 
 Each positions[i] is distinct.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    struct Move{int dx,dy,steps;};
    vector<vector<Move>>options;
    vector<Move>chosen;
    vector<vector<int>>pos;
    int ans=0;
    bool compatible(int a,int b){
        for(int t=0;t<=7;++t){
            int ax=pos[a][0]+chosen[a].dx*min(t,chosen[a].steps);
            int ay=pos[a][1]+chosen[a].dy*min(t,chosen[a].steps);
            int bx=pos[b][0]+chosen[b].dx*min(t,chosen[b].steps);
            int by=pos[b][1]+chosen[b].dy*min(t,chosen[b].steps);
            if(ax==bx&&ay==by)return false;
        }
        return true;
    }
    void dfs(int i){if(i==(int)pos.size()){++ans;return;}
        for(auto mv:options[i]){chosen[i]=mv;bool ok=true;
            for(int j=0;j<i;++j)if(!compatible(i,j)){ok=false;break;}
            if(ok)dfs(i+1);
        }
    }
public:
    int countCombinations(vector<string>& pieces,vector<vector<int>>& positions){
        pos=positions;int n=pieces.size();options.assign(n,{});chosen.resize(n);ans=0;
        for(int i=0;i<n;++i){options[i].push_back({0,0,0});
            for(int dx=-1;dx<=1;++dx)for(int dy=-1;dy<=1;++dy){
                if(dx==0&&dy==0)continue;
                bool diagonal=dx!=0&&dy!=0;
                if(pieces[i]=="rook"&&diagonal)continue;
                if(pieces[i]=="bishop"&&!diagonal)continue;
                for(int t=1;t<=7;++t){int x=pos[i][0]+t*dx,y=pos[i][1]+t*dy;
                    if(x<1||x>8||y<1||y>8)break;
                    options[i].push_back({dx,dy,t});
                }
            }
        }
        dfs(0);return ans;
    }
};
```


## 2151. Maximum Good People Based on Statements

**Problem:** https://leetcode.com/problems/maximum-good-people-based-on-statements/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Backtracking, Bit Manipulation, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There are two types of persons: 

 The good person : The person who always tells the truth. 
 
 The bad person : The person who might tell the truth and might lie. 

 You are given a 0-indexed 2D integer array statements of size n x n that represents the statements made by n people about each other. More specifically, statements[i][j] could be one of the following: 

 0 which represents a statement made by person i that person j is a bad person. 
 
 1 which represents a statement made by person i that person j is a good person. 
 
 2 represents that no statement is made by person i about person j . 

 Additionally, no person ever makes a statement about themselves. Formally, we have that statements[i][i] = 2 for all 0 <= i < n . 
 
 Return the maximum number of people who can be good based on the statements made by the n people . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/01/15/logic1.jpg] 
 
```
Input:
 statements = [[2,1,2],[1,2,2],[2,0,2]]

Output:
 2

Explanation:
 Each person makes a single statement.
- Person 0 states that person 1 is good.
- Person 1 states that person 0 is good.
- Person 2 states that person 1 is bad.
Let's take person 2 as the key.
- Assuming that person 2 is a good person:
 - Based on the statement made by person 2, person 1 is a bad person.
 - Now we know for sure that person 1 is bad and person 2 is good.
 - Based on the statement made by person 1, and since person 1 is bad, they could be:
 - telling the truth. There will be a contradiction in this case and this assumption is invalid.
 - lying. In this case, person 0 is also a bad person and lied in their statement.
 - 
Following that person 2 is a good person, there will be only one good person in the group
.
- Assuming that person 2 is a bad person:
 - Based on the statement made by person 2, and since person 2 is bad, they could be:
 - telling the truth. Following this scenario, person 0 and 1 are both bad as explained before.
 - 
Following that person 2 is bad but told the truth, there will be no good persons in the group
.
 - lying. In this case person 1 is a good person.
 - Since person 1 is a good person, person 0 is also a good person.
 - 
Following that person 2 is bad and lied, there will be two good persons in the group
.
We can see that at most 2 persons are good in the best case, so we return 2.
Note that there is more than one way to arrive at this conclusion.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/01/15/logic2.jpg] 
 
```
Input:
 statements = [[2,0],[0,2]]

Output:
 1

Explanation:
 Each person makes a single statement.
- Person 0 states that person 1 is bad.
- Person 1 states that person 0 is bad.
Let's take person 0 as the key.
- Assuming that person 0 is a good person:
 - Based on the statement made by person 0, person 1 is a bad person and was lying.
 - 
Following that person 0 is a good person, there will be only one good person in the group
.
- Assuming that person 0 is a bad person:
 - Based on the statement made by person 0, and since person 0 is bad, they could be:
 - telling the truth. Following this scenario, person 0 and 1 are both bad.
 - 
Following that person 0 is bad but told the truth, there will be no good persons in the group
.
 - lying. In this case person 1 is a good person.
 - 
Following that person 0 is bad and lied, there will be only one good person in the group
.
We can see that at most, one person is good in the best case, so we return 1.
Note that there is more than one way to arrive at this conclusion.
```

 Constraints: 

 n == statements.length == statements[i].length 
 
 2 <= n <= 15 
 
 statements[i][j] is either 0 , 1 , or 2 . 
 
 statements[i][i] == 2

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int maximumGood(vector<vector<int>>& statements) {
        int n=statements.size(),ans=0;
        for(int mask=0;mask<(1<<n);++mask) {
            bool ok=true;
            for(int i=0;i<n&&ok;++i) if(mask>>i&1)
                for(int j=0;j<n;++j) if(statements[i][j]!=2 && statements[i][j]!=((mask>>j)&1)) {ok=false;break;}
            if(ok) ans=max(ans,__builtin_popcount((unsigned)mask));
        }
        return ans;
    }
};
```


## 2212. Maximum Points in an Archery Competition

**Problem:** https://leetcode.com/problems/maximum-points-in-an-archery-competition/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking, Bit Manipulation, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Alice and Bob are opponents in an archery competition. The competition has set the following rules: 

 Alice first shoots numArrows arrows and then Bob shoots numArrows arrows. 
 
 The points are then calculated as follows:

 The target has integer scoring sections ranging from 0 to 11 inclusive . 
 
 For each section of the target with score k (in between 0 to 11 ), say Alice and Bob have shot a k and b k arrows on that section respectively. If a k >= b k , then Alice takes k points. If a k < b k , then Bob takes k points. 
 
 However, if a k == b k == 0 , then nobody takes k points. 

 For example, if Alice and Bob both shot 2 arrows on the section with score 11 , then Alice takes 11 points. On the other hand, if Alice shot 0 arrows on the section with score 11 and Bob shot 2 arrows on that same section, then Bob takes 11 points. 

 You are given the integer numArrows and an integer array aliceArrows of size 12 , which represents the number of arrows Alice shot on each scoring section from 0 to 11 . Now, Bob wants to maximize the total number of points he can obtain. 
 
 Return the array bobArrows which represents the number of arrows Bob shot on each scoring section from 0 to 11 . The sum of the values in bobArrows should equal numArrows . 
 
 If there are multiple ways for Bob to earn the maximum total points, return any one of them. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/24/ex1.jpg] 
 
```
Input:
 numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]

Output:
 [0,0,0,0,1,1,0,0,1,2,3,1]

Explanation:
 The table above shows how the competition is scored. 
Bob earns a total point of 4 + 5 + 8 + 9 + 10 + 11 = 47.
It can be shown that Bob cannot obtain a score higher than 47 points.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/24/ex2new.jpg] 
 
```
Input:
 numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]

Output:
 [0,0,0,0,0,0,0,0,1,1,1,0]

Explanation:
 The table above shows how the competition is scored.
Bob earns a total point of 8 + 9 + 10 = 27.
It can be shown that Bob cannot obtain a score higher than 27 points.
```

 Constraints: 

 1 <= numArrows <= 10 5 
 
 aliceArrows.length == bobArrows.length == 12 
 
 0 <= aliceArrows[i], bobArrows[i] <= numArrows 
 
 sum(aliceArrows[i]) == numArrows

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 vector<int> maximumBobPoints(int numArrows,vector<int>& aliceArrows){vector<int> best(12),cur(12);int score=-1;
  for(int mask=0;mask<(1<<12);++mask){fill(cur.begin(),cur.end(),0);int used=0,pts=0;
   for(int i=1;i<12;++i)if(mask&(1<<i)){cur[i]=aliceArrows[i]+1;used+=cur[i];pts+=i;}
   if(used<=numArrows&&pts>score){cur[0]=numArrows-used;best=cur;score=pts;}
  }return best;
 }
};
```


## 2397. Maximum Rows Covered by Columns

**Problem:** https://leetcode.com/problems/maximum-rows-covered-by-columns/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Backtracking, Bit Manipulation, Matrix, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an m x n binary matrix matrix and an integer numSelect . 
 
 Your goal is to select exactly numSelect distinct columns from matrix such that you cover as many rows as possible. 
 
 A row is considered covered if all the 1 's in that row are also part of a column that you have selected. If a row does not have any 1 s, it is also considered covered. 
 
 More formally, let us consider selected = {c 1 , c 2 , ...., c numSelect } as the set of columns selected by you. A row i is covered by selected if: 

 For each cell where matrix[i][j] == 1 , the column j is in selected . 
 
 Or, no cell in row i has a value of 1 . 

 Return the maximum number of rows that can be covered by a set of numSelect columns. 

 Example 1: 
 
 [Figure: https://assets.leetcode.com/uploads/2022/07/14/rowscovered.png] 

 Input: matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], numSelect = 2 
 
 Output: 3 
 
 Explanation: 
 
 One possible way to cover 3 rows is shown in the diagram above. 
We choose s = {0, 2}. 
- Row 0 is covered because it has no occurrences of 1. 
- Row 1 is covered because the columns with value 1, i.e. 0 and 2 are present in s. 
- Row 2 is not covered because matrix[2][1] == 1 but 1 is not present in s. 
- Row 3 is covered because matrix[2][2] == 1 and 2 is present in s. 
Thus, we can cover three rows. 
Note that s = {1, 2} will also cover 3 rows, but it can be shown that no more than three rows can be covered. 

 Example 2: 
 
 [Figure: https://assets.leetcode.com/uploads/2022/07/14/rowscovered2.png] 

 Input: matrix = [[1],[0]], numSelect = 1 
 
 Output: 2 
 
 Explanation: 
 
 Selecting the only column will result in both rows being covered since the entire matrix is selected. 

 Constraints: 

 m == matrix.length 
 
 n == matrix[i].length 
 
 1 <= m, n <= 12 
 
 matrix[i][j] is either 0 or 1 . 
 
 1 <= numSelect <= n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int maximumRows(vector<vector<int>>& matrix,int numSelect){int m=matrix.size(),n=matrix[0].size();vector<int>mask(m);for(int i=0;i<m;i++)for(int j=0;j<n;j++)if(matrix[i][j])mask[i]|=1<<j;int best=0;for(int s=0;s<(1<<n);s++)if(__builtin_popcount((unsigned)s)==numSelect){int cnt=0;for(int x:mask)if((x&s)==x)cnt++;best=max(best,cnt);}return best;}};
```


## 2664. The Knight’s Tour

**Problem:** https://leetcode.com/problems/the-knights-tour/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Backtracking, Matrix

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given two positive integers m and n which are the height and width of a 0-indexed 2D-array board , a pair of positive integers (r, c) which is the starting position of the knight on the board. 
 
 Your task is to find an order of movements for the knight, in a manner that every cell of the  board gets visited exactly once (the starting cell is considered visited and you shouldn't visit it again). 
 
 Return the array board in which the cells' values show the order of visiting the cell starting from 0 (the initial place of the knight). 
 
 Note that a knight can move from cell (r1, c1) to cell (r2, c2) if 0 <= r2 <= m - 1 and 0 <= c2 <= n - 1 and min(abs(r1 - r2), abs(c1 - c2)) = 1 and max(abs(r1 - r2), abs(c1 - c2)) = 2 . 

 Example 1: 
 
```
Input:
 m = 1, n = 1, r = 0, c = 0

Output:
 [[0]]

Explanation:
 There is only 1 cell and the knight is initially on it so there is only a 0 inside the 1x1 grid.
```

 Example 2: 
 
```
Input:
 m = 3, n = 4, r = 0, c = 0

Output:
 [[0,3,6,9],[11,8,1,4],[2,5,10,7]]

Explanation:
 By the following order of movements we can visit the entire board.
(0,0)->(1,2)->(2,0)->(0,1)->(1,3)->(2,1)->(0,2)->(2,3)->(1,1)->(0,3)->(2,2)->(1,0)
```

 Constraints: 

 1 <= m, n <= 5 
 
 0 <= r <= m - 1 
 
 0 <= c <= n - 1 
 
 The inputs will be generated such that there exists at least one possible order of movements with the given condition

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    int dr[8] = {1, 1, -1, -1, 2, 2, -2, -2};
    int dc[8] = {2, -2, 2, -2, 1, -1, 1, -1};
public:
    vector<vector<int>> tourOfKnight(int m, int n, int r, int c) {
        vector<vector<int>> board(m, vector<int>(n, -1));
        auto degree = [&](int x, int y) {
            int count = 0;
            for (int d = 0; d < 8; ++d) {
                int nx = x + dr[d], ny = y + dc[d];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && board[nx][ny] == -1) ++count;
            }
            return count;
        };
        function<bool(int,int,int)> dfs = [&](int x, int y, int step) {
            board[x][y] = step;
            if (step == m * n - 1) return true;
            vector<array<int,3>> moves;
            for (int d = 0; d < 8; ++d) {
                int nx = x + dr[d], ny = y + dc[d];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && board[nx][ny] == -1)
                    moves.push_back({degree(nx, ny), nx, ny});
            }
            sort(moves.begin(), moves.end());
            for (const auto& next : moves)
                if (dfs(next[1], next[2], step + 1)) return true;
            board[x][y] = -1;
            return false;
        };
        dfs(r, c, 0);
        return board;
    }
};
```


## 2698. Find the Punishment Number of an Integer

**Problem:** https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Math / Number Theory

**Data structures (inferred):** Not inferred

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a positive integer n , return the punishment number of n . 
 
 The punishment number of n is defined as the sum of the squares of all integers i such that: 

 1 <= i <= n 
 
 The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i . 

 Example 1: 
 
```
Input:
 n = 10

Output:
 182

Explanation:
 There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182
```

 Example 2: 
 
```
Input:
 n = 37

Output:
 1478

Explanation:
 There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478
```

 Constraints: 

 1 <= n <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {bool check(const string&s,int pos,int target){if(pos==(int)s.size())return target==0;int x=0;for(int i=pos;i<(int)s.size();i++){x=x*10+s[i]-'0';if(x>target)break;if(check(s,i+1,target-x))return true;}return false;}public:int punishmentNumber(int n){int ans=0;for(int i=1;i<=n;i++)if(check(to_string(i*i),0,i))ans+=i*i;return ans;}};
```


## 3211. Generate Binary Strings Without Adjacent Zeros

**Problem:** https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Bit Manipulation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a positive integer n . 
 
 A binary string x is valid if all substrings of x of length 2 contain at least one "1" . 
 
 Return all valid strings with length n , in any order. 

 Example 1: 

 Input: n = 3 
 
 Output: ["010","011","101","110","111"] 
 
 Explanation: 
 
 The valid strings of length 3 are: "010" , "011" , "101" , "110" , and "111" . 

 Example 2: 

 Input: n = 1 
 
 Output: ["0","1"] 
 
 Explanation: 
 
 The valid strings of length 1 are: "0" and "1" . 

 Constraints: 

 1 <= n <= 18

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {void dfs(int n,string&s,vector<string>&out){if((int)s.size()==n){out.push_back(s);return;}s+='1';dfs(n,s,out);s.pop_back();if(s.empty()||s.back()=='1'){s+='0';dfs(n,s,out);s.pop_back();}}public:vector<string> validStrings(int n){vector<string>r;string s;dfs(n,s,r);return r;}};
```


## 3437. Permutations III

**Problem:** https://leetcode.com/problems/permutations-iii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Backtracking

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer n , an alternating permutation is a permutation of the first n positive integers such that no two adjacent elements are both odd or both even. 
 
 Return all such alternating permutations sorted in lexicographical order. 

 Example 1: 

 Input: n = 4 
 
 Output: [[1,2,3,4],[1,4,3,2],[2,1,4,3],[2,3,4,1],[3,2,1,4],[3,4,1,2],[4,1,2,3],[4,3,2,1]] 

 Example 2: 

 Input: n = 2 
 
 Output: [[1,2],[2,1]] 

 Example 3: 

 Input: n = 3 
 
 Output: [[1,2,3],[3,2,1]] 

 Constraints: 

 1 <= n <= 10

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    void dfs(int n, vector<int>& path, vector<int>& used,
             vector<vector<int>>& result) {
        if (static_cast<int>(path.size()) == n) {
            result.push_back(path);
            return;
        }
        for (int x = 1; x <= n; ++x) {
            if (used[x]) continue;
            if (!path.empty() && (path.back() & 1) == (x & 1)) continue;
            used[x] = 1;
            path.push_back(x);
            dfs(n, path, used, result);
            path.pop_back();
            used[x] = 0;
        }
    }
public:
    vector<vector<int>> permute(int n) {
        vector<vector<int>> result;
        vector<int> path, used(n + 1, 0);
        dfs(n, path, used, result);
        return result;
    }
};
```


## 3646. Next Special Palindrome Number

**Problem:** https://leetcode.com/problems/next-special-palindrome-number/

**Difficulty:** Hard | **Premium:** No

**Tags:** Backtracking, Bit Manipulation

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Bit Manipulation

**Data structures (inferred):** Not inferred

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer n . 
 
 A number is called special if: 

 It is a palindrome . 
 
 Every digit k in the number appears exactly k times. 

 Return the smallest special number strictly greater than n . 

 Example 1: 

 Input: n = 2 
 
 Output: 22 
 
 Explanation: 
 
 22 is the smallest special number greater than 2, as it is a palindrome and the digit 2 appears exactly 2 times. 

 Example 2: 

 Input: n = 33 
 
 Output: 212 
 
 Explanation: 
 
 212 is the smallest special number greater than 33, as it is a palindrome and the digits 1 and 2 appear exactly 1 and 2 times respectively. 

 Constraints: 

 0 <= n <= 10 15

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 long long specialPalindrome(long long n){long long ans=LLONG_MAX;string bound=to_string(n);
  for(int mask=1;mask<(1<<9);++mask){int odd=0,len=0;string half,mid;
   for(int d=1;d<=9;++d)if(mask>>(d-1)&1){len+=d;if(d&1){++odd;mid=string(1,char('0'+d));}half+=string(d/2,char('0'+d));}
   if(odd>1||len>16||len<(int)bound.size())continue;
   sort(half.begin(),half.end());do{string s=half+mid;string rev=half;reverse(rev.begin(),rev.end());s+=rev;
    if(s.size()>bound.size()||s>bound){long long v=stoll(s);ans=min(ans,v);break;}}
   while(next_permutation(half.begin(),half.end()));
  }return ans==LLONG_MAX?-1:ans;
 }
};
```


## 3669. Balanced K-Factor Decomposition

**Problem:** https://leetcode.com/problems/balanced-k-factor-decomposition/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, Backtracking, Number Theory

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, Math / Number Theory

**Data structures (inferred):** Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two integers n and k . 
 
 Split the number n into exactly k positive integers such that the product of these integers is equal to n . 
 
 Return any one split in which the maximum difference between any two numbers is minimized . You may return the result in any order. 

 Example 1: 

 Input: n = 100, k = 2 
 
 Output: [10,10] 
 
 Explanation: 
 
 The split [10, 10] yields 10 * 10 = 100 and a max-min difference of 0, which is minimal. 

 Example 2: 

 Input: n = 44, k = 3 
 
 Output: [2,2,11] 
 
 Explanation: 

 Split [1, 1, 44] yields a difference of 43 
 
 Split [1, 2, 22] yields a difference of 21 
 
 Split [1, 4, 11] yields a difference of 10 
 
 Split [2, 2, 11] yields a difference of 9 

 Therefore, [2, 2, 11] is the optimal split with the smallest difference 9. 

 Constraints: 

 4 <= n <= 10 5 
 
 2 <= k <= 5 
 
 k is strictly less than the total number of positive divisors of n .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { vector<int> best,cur;int spread=INT_MAX;void dfs(int n,int k,int lo){if(k==1){if(n<lo)return;cur.push_back(n);if(cur.back()-cur.front()<spread){spread=cur.back()-cur.front();best=cur;}cur.pop_back();return;}for(int d=lo;1LL*d*d<=n;++d)if(n%d==0){cur.push_back(d);dfs(n/d,k-1,d);cur.pop_back();}}public:vector<int> minDifference(int n,int k){best.clear();cur.clear();spread=INT_MAX;dfs(n,k,1);return best;} };
```


## 3799. Word Squares II

**Problem:** https://leetcode.com/problems/word-squares-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String, Backtracking, Sorting, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string array words , consisting of distinct 4-letter strings, each containing lowercase English letters. 
 
 A word square consists of 4 distinct words: top , left , right and bottom , arranged as follows: 

 top forms the top row . 
 
 bottom forms the bottom row . 
 
 left forms the left column (top to bottom). 
 
 right forms the right column (top to bottom). 

 It must satisfy: 

 top[0] == left[0] , top[3] == right[0] 
 
 bottom[0] == left[3] , bottom[3] == right[3] 

 Return all valid distinct word squares, sorted in ascending lexicographic order by the 4-tuple (top, left, right, bottom)​​​​​​​ . 

 Example 1: 

 Input: words = ["able","area","echo","also"] 
 
 Output: [["able","area","echo","also"],["area","able","also","echo"]] 
 
 Explanation: 
 
 There are exactly two valid 4-word squares that satisfy all corner constraints: 

 "able" (top), "area" (left), "echo" (right), "also" (bottom)

 top[0] == left[0] == 'a' 
 
 top[3] == right[0] == 'e' 
 
 bottom[0] == left[3] == 'a' 
 
 bottom[3] == right[3] == 'o' 

 "area" (top), "able" (left), "also" (right), "echo" (bottom)

 All corner constraints are satisfied. 

 Thus, the answer is [["able","area","echo","also"],["area","able","also","echo"]] . 

 Example 2: 

 Input: words = ["code","cafe","eden","edge"] 
 
 Output: [] 
 
 Explanation: 
 
 No combination of four words satisfies all four corner constraints. Thus, the answer is empty array [] . 

 Constraints: 

 4 <= words.length <= 15 
 
 words[i].length == 4 
 
 words[i] consists of only lowercase English letters. 
 
 All words[i] are distinct .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        int n = words.size();
        vector<vector<string>> ans;
        for (int a = 0; a < n; ++a)
            for (int b = 0; b < n; ++b) if (b != a && words[a][0] == words[b][0])
                for (int c = 0; c < n; ++c) if (c != a && c != b && words[a][3] == words[c][0])
                    for (int d = 0; d < n; ++d) if (d != a && d != b && d != c &&
                        words[d][0] == words[b][3] && words[d][3] == words[c][3])
                        ans.push_back({words[a], words[b], words[c], words[d]});
        sort(ans.begin(), ans.end());
        return ans;
    }
};
```


## 3955. Valid Binary Strings With Cost Limit

**Problem:** https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Backtracking, Bit Manipulation, Enumeration

**Primary pattern:** Backtracking / Bitmask

**Related patterns:** Backtracking / Bitmask, String Algorithms, Bit Manipulation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Enumerate choices while pruning; compress subsets as masks.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two integers n and k . 
 
 The cost of a binary string s is defined as the sum of all indices i (0-based) such that s[i] == '1' . 
 
 A binary string is considered valid if: 

 It does not contain two consecutive '1' characters. 
 
 Its cost is less than or equal to k . 

 Return a list of all valid binary strings of length n in any order. 

 Example 1: 

 Input: n = 3, k = 1 
 
 Output: ["000","010","100"] 
 
 Explanation: 
 
 The binary strings of length 3 without consecutive '1' characters are: 

 "000" : cost = 0 
 
 " 100" : cost = 0 
 
 "010" : cost = 1 
 
 "001" : cost = 2 
 
 "101" : cost = 0 + 2 = 2 

 Among these, the strings with cost less than or equal to k = 1 are "000" , "010" and "100" . 
 
 Thus, the valid strings are ["000", "010", "100"] . 

 Example 2: 

 Input: n = 1, k = 0 
 
 Output: ["0","1"] 
 
 Explanation: 
 
 The valid binary strings of length 1 are "0" and "1" . 
 
 Thus the answer is ["0", "1"] . 

 Constraints: 

 1 <= n <= 12 
 
 0 <= k <= n * (n - 1) / 2

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    void dfs(int i,int n,int budget,string& s,vector<string>& ans){
        if(i==n){ans.push_back(s);return;}
        s.push_back('0');
        dfs(i+1,n,budget,s,ans);
        s.pop_back();
        if(budget>=i && (i==0||s.back()!='1')){
            s.push_back('1');
            dfs(i+1,n,budget-i,s,ans);
            s.pop_back();
        }
    }
public:
    vector<string> generateValidStrings(int n,int k){
        vector<string> ans;string s;
        dfs(0,n,k,s,ans);
        return ans;
    }
};
```

