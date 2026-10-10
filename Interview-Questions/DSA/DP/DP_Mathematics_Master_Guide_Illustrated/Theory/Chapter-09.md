# Chapter 09 — Subset-state DP

> **Study goal:** Reconstruct the reasoning from the problem constraints. The example below is a teaching derivation; the linked original submission may use an equivalent optimized algorithm.

## 1. Start with a concrete question

**Worked example:** [464. Can I Win](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/464.md)

**State meaning:** Win(mask): whether current player can force a win from used-number set mask.

## 2. Why this recurrence follows

The state is the set of already chosen numbers. A winning move either finishes immediately or leaves the opponent in a losing state.

**Mathematical recurrence:**

```text
Win(mask)=OR over legal x of [x>=remaining OR NOT Win(mask with x used)]
```

Before using the equation, identify the empty or impossible states, and check whether alternatives should be **added**, **maximized**, **minimized**, or **OR-ed**.

## 3. Draw the decision and trace it

```mermaid
flowchart TD
 A["Current used-number mask"] --> B["Try each unused number x"]
 B --> C{"Reach target now?"}
 C -->|Yes| D["Winning state"]
 C -->|No| E["Evaluate opponent on next mask"]
 E --> F{"Opponent loses?"}
 F -->|Yes| D
 F -->|No| G["Try another number"]
```

**Trace:** Numbers 1..3, target 4: first player chooses 1,2,or 3; examine each reply and whether it lets the opponent force a win.

### How to reproduce the trace on paper

1. Write down the state definition, including exactly what the indices mean.
2. Mark the base cases before any recursive calls.
3. List the legal predecessor states or choices.
4. Compute small states first; annotate each arrow with its reason.
5. Compare the final result with a small manual enumeration.

## 4. Connect mathematics to your C++

Open [464. Can I Win](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/464.md) and find the line that performs the transition. If it is optimized, first imagine a full DP table, then explain why only a smaller number of previous states are required.

**Interview questions:** Why are the cases exhaustive? Why do they not double-count? What invariant does each variable maintain? Which changes in the problem would require another state dimension?

## 5. Related problems to compare

The following links group problems for study. **Do not assume they all use the same recurrence**: compare the constraints and the submitted algorithm before transferring a technique.

## Problems in this family (19)

- [464. Can I Win](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/464.md) — Medium
- [473. Matchsticks to Square](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/473.md) — Medium
- [526. Beautiful Arrangement](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/526.md) — Medium
- [698. Partition to K Equal Sum Subsets](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/698.md) — Medium
- [773. Sliding Puzzle](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/773.md) — Hard
- [847. Shortest Path Visiting All Nodes](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/847.md) — Hard
- [943. Find the Shortest Superstring](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/943.md) — Hard
- [996. Number of Squareful Arrays](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/996.md) — Hard
- [1125. Smallest Sufficient Team](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1125.md) — Hard
- [1349. Maximum Students Taking Exam](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1349.md) — Hard
- [1494. Parallel Courses II](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1494.md) — Hard
- [1595. Minimum Cost to Connect Two Groups of Points](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1595.md) — Hard
- [1723. Find Minimum Time to Finish All Jobs](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1723.md) — Hard
- [1755. Closest Subsequence Sum](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1755.md) — Hard
- [1815. Maximum Number of Groups Getting Fresh Donuts](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1815.md) — Hard
- [1947. Maximum Compatibility Score Sum](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1947.md) — Medium
- [1986. Minimum Number of Work Sessions to Finish the Tasks](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1986.md) — Medium
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/2035.md) — Hard
- [2050. Parallel Courses III](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/2050.md) — Hard

