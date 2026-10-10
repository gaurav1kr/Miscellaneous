# Chapter 06 — Interval decomposition

> **Study goal:** Reconstruct the reasoning from the problem constraints. The example below is a teaching derivation; the linked original submission may use an equivalent optimized algorithm.

## 1. Start with a concrete question

**Worked example:** [312. Burst Balloons](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/312.md)

**State meaning:** D(l,r): maximum coins bursting balloons strictly between boundaries l and r.

## 2. Why this recurrence follows

Choosing the FIRST balloon leaves changing neighbors; choosing the LAST makes the interval boundaries fixed. This is the crucial mathematical trick.

**Mathematical recurrence:**

```text
D(l,r)=max over l<k<r of [D(l,k)+D(k,r)+a[l]*a[k]*a[r]]
```

Before using the equation, identify the empty or impossible states, and check whether alternatives should be **added**, **maximized**, **minimized**, or **OR-ed**.

## 3. Draw the decision and trace it

```mermaid
flowchart TD
 A["Interval (l,r)"] --> B["Choose k as LAST balloon"]
 B --> C["Solve left interval (l,k)"]
 B --> D["Solve right interval (k,r)"]
 C --> E["Add final gain a[l] × a[k] × a[r]"]
 D --> E
```

**Trace:** Padded [1,3,1,5,1]: choose a balloon k to burst LAST in an interval, after its interior neighbors have gone.

### How to reproduce the trace on paper

1. Write down the state definition, including exactly what the indices mean.
2. Mark the base cases before any recursive calls.
3. List the legal predecessor states or choices.
4. Compute small states first; annotate each arrow with its reason.
5. Compare the final result with a small manual enumeration.

## 4. Connect mathematics to your C++

Open [312. Burst Balloons](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/312.md) and find the line that performs the transition. If it is optimized, first imagine a full DP table, then explain why only a smaller number of previous states are required.

**Interview questions:** Why are the cases exhaustive? Why do they not double-count? What invariant does each variable maintain? Which changes in the problem would require another state dimension?

## 5. Related problems to compare

The following links group problems for study. **Do not assume they all use the same recurrence**: compare the constraints and the submitted algorithm before transferring a technique.

## Problems in this family (34)

- [131. Palindrome Partitioning](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/131.md) — Medium
- [132. Palindrome Partitioning II](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/132.md) — Hard
- [312. Burst Balloons](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/312.md) — Hard
- [375. Guess Number Higher or Lower II](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/375.md) — Medium
- [410. Split Array Largest Sum](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/410.md) — Hard
- [516. Longest Palindromic Subsequence](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/516.md) — Medium
- [546. Remove Boxes](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/546.md) — Hard
- [553. Optimal Division](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/553.md) — Medium
- [647. Palindromic Substrings](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/647.md) — Medium
- [664. Strange Printer](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/664.md) — Hard
- [730. Count Different Palindromic Subsequences](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/730.md) — Hard
- [813. Largest Sum of Averages](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/813.md) — Medium
- [877. Stone Game](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/877.md) — Medium
- [887. Super Egg Drop](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/887.md) — Hard
- [1000. Minimum Cost to Merge Stones](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1000.md) — Hard
- [1039. Minimum Score Triangulation of Polygon](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1039.md) — Medium
- [1105. Filling Bookcase Shelves](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1105.md) — Medium
- [1130. Minimum Cost Tree From Leaf Values](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1130.md) — Medium
- [1140. Stone Game II](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1140.md) — Medium
- [1147. Longest Chunked Palindrome Decomposition](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1147.md) — Hard
- [1278. Palindrome Partitioning III](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1278.md) — Hard
- [1312. Minimum Insertion Steps to Make a String Palindrome](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1312.md) — Hard
- [1335. Minimum Difficulty of a Job Schedule](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1335.md) — Hard
- [1388. Pizza With 3n Slices](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1388.md) — Hard
- [1406. Stone Game III](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1406.md) — Hard
- [1478. Allocate Mailboxes](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1478.md) — Hard
- [1510. Stone Game IV](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1510.md) — Hard
- [1547. Minimum Cost to Cut a Stick](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1547.md) — Hard
- [1690. Stone Game VII](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1690.md) — Medium
- [1745. Palindrome Partitioning IV](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1745.md) — Hard
- [1872. Stone Game VIII](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1872.md) — Hard
- [1884. Egg Drop With 2 Eggs and N Floors](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1884.md) — Medium
- [3414. Maximum Score of Non-overlapping Intervals](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/3414.md) — Hard
- [4009. Minimum Possible Maximum Waiting Time](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/4009.md) — Hard

