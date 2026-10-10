# Chapter 07 — Scheduling and Weighted Intervals

## Core mathematical idea

Sort events and jump to the next compatible event .

## A representative mathematical model

`F(i,k)=\max(F(i+1,k),w_i+F(next(i),k-1))`

For inclusive intervals, compatibility requires next.start > current.end. Binary search can find next(i).

**Important:** This formula is a pattern template. The precise recurrence for a listed problem must be derived from that problem’s constraints and code.

## State-transition picture

```mermaid
flowchart TD
 A["Events sorted by finish or start"] --> B{"Take current event?"}
 B -->|No| C["Next event"]
 B -->|Yes| D["Profit plus next compatible"]
 C --> E["Maximum total profit"]
 D --> E
```

## How to study the linked problems

For each problem: read the mathematical template, articulate its state and decision, inspect the submitted implementation, then justify why its transitions are correct. Compare with the previous problem: which constraint forced a new state dimension?

## Problems in this family (12)

- [121. Best Time to Buy and Sell Stock](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/121.md) — Easy
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/689.md) — Hard
- [983. Minimum Cost For Tickets](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/983.md) — Medium
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1031.md) — Medium
- [1235. Maximum Profit in Job Scheduling](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1235.md) — Hard
- [1687. Delivering Boxes from Storage to Ports](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1687.md) — Hard
- [1751. Maximum Number of Events That Can Be Attended II](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/1751.md) — Hard
- [2008. Maximum Earnings From Taxi](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/2008.md) — Medium
- [2054. Two Best Non-Overlapping Events](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/2054.md) — Medium
- [4023. Elevator Requests II](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/4023.md) — Hard
- [4027. Elevator Requests III](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/4027.md) — Hard
- [4068. Maximize Meeting Earnings with Idle Gaps](https://github.com/gaurav1kr/Miscellaneous/blob/main/DSA/DP/DP_Mathematics_Master_Guide_Illustrated/Problems/4068.md) — Hard
