# 01 — Derive DP Instead of Memorizing It

## A repeatable seven-question method

1. **Objective:** Are we maximizing, minimizing, counting, or checking feasibility?
2. **Choice:** What is the first or last decision that splits possible answers?
3. **State:** Which parameters completely determine the remaining problem?
4. **Transition:** Write an equation for each choice, then combine with max/min/sum/OR.
5. **Base case:** What does an empty input, exhausted budget, or reached destination mean?
6. **Order:** Which states must be solved before this state?
7. **Optimization:** Can we reduce dimensions, use binary search, prefix sums, monotonic queues, or exploit bounded values?

```mermaid
flowchart LR
 A[Problem statement] --> B[Objective and constraints]
 B --> C[Choose state]
 C --> D[Enumerate legal decisions]
 D --> E[Recurrence and bases]
 E --> F[Correctness proof]
 F --> G[Memo or table]
 G --> H[Optimize]
```

## Worked derivation A: Count paths

For a grid allowing right/down moves, define `W(i,j)` as number of paths to `(i,j)`. The **last step** comes either from above or left. Those path sets do not overlap, so `W(i,j)=W(i-1,j)+W(i,j-1)`. At the origin, `W(0,0)=1`; blocked or out-of-bounds states have zero ways.

## Worked derivation B: Edit distance

Let `D(i,j)` be minimum operations to transform first `i` characters of A into first `j` of B. For unequal final characters: delete A's last, insert B's last, or substitute. Therefore `D(i,j)=1+min(D(i-1,j),D(i,j-1),D(i-1,j-1))`. Equal last characters give `D(i-1,j-1)`. Bases: `D(i,0)=i`, `D(0,j)=j`.

## Worked derivation C: Weighted interval scheduling

Sort intervals by start time. Define `F(i,k)` as best weight using intervals at/after `i` and at most `k` selections. Either skip interval `i`, or take it and jump to the first compatible interval `next(i)`. Thus `F(i,k)=max(F(i+1,k),w_i+F(next(i),k-1))`. The jump can be computed with binary search. Distinguish strict from non-strict endpoint compatibility.

## How to explain this in a FAANG interview

State the invariant *before* code; derive transitions from choices; justify why every solution falls into a case; compute a small example; discuss complexity and boundary cases; only then optimize memory. If a submitted solution uses greedy or another technique, explain the invariant or exchange argument rather than inventing a DP recurrence.
