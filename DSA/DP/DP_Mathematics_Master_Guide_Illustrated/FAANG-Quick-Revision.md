# FAANG Dynamic Programming — Quick Revision

## The 60-second interview checklist

**Objective → State → Decisions → Recurrence → Bases → Order → Proof → Complexity → Optimization.**

| Goal | Combine candidate states with | Impossible state |
|---|---|---|
| Maximum reward | `max` | `-INF` |
| Minimum cost | `min` | `+INF` |
| Number of ways | `sum` | `0` |
| Feasibility | `OR` | `false` |
| Probability | weighted sum | `0` |

## Concept formula flashcards

### [A recurrence expresses a large answer using smaller answers.](Chapter-01.md)

`F(n)=\sum_{c\in Choices(n)}F(next(n,c))`

For counting, add disjoint cases. For optimization, replace sum with min or max. Base cases must express empty structures correctly.

### [Each item creates a decision: select or reject.](Chapter-02.md)

`F(i,c)=\max(F(i-1,c),v_i+F(i-1,c-w_i))`

Only use the take branch when the remaining capacity is feasible. Counting versions use addition; feasibility versions use logical OR.

### [A cell or position is a state; transitions come from legal predecessor positions.](Chapter-03.md)

`F(i,j)=F(i-1,j)+F(i,j-1)`

For minimum cost paths, replace + of paths with min of predecessor costs, then add the current cell cost. Obstacles contribute zero ways.

### [Match prefixes by considering their final symbols.](Chapter-04.md)

`D(i,j)=\min(D(i-1,j)+1,D(i,j-1)+1,D(i-1,j-1)+[a_i\ne b_j])`

The three alternatives correspond to delete, insert and substitute. In matching/counting variants, the aggregation changes.

### [A subsequence is built by choosing a compatible predecessor.](Chapter-05.md)

`L(i)=1+\max_{j<i,\;a_j<a_i}L(j)`

When there is no predecessor, length is one. More advanced variants add dimensions such as last difference or number of chosen elements.

### [Split an interval at a chosen boundary, root, or last operation.](Chapter-06.md)

`F(l,r)=\min_{l\le k<r}(F(l,k)+F(k+1,r)+cost(l,k,r))`

Some interval problems maximize rather than minimize. Choosing the last operation can make otherwise interacting subproblems independent.

### [Sort events and jump to the next compatible event.](Chapter-07.md)

`F(i,k)=\max(F(i+1,k),w_i+F(next(i),k-1))`

For inclusive intervals, compatibility requires next.start > current.end. Binary search can find next(i).

### [The state represents a legal mode or finite history.](Chapter-08.md)

`F(i,s)=\operatorname{opt}_{p\to s}(F(i-1,p)+cost(p,s,i))`

Examples include holding stock versus not holding, cooldown, and bounded operation counts. Draw a state-transition graph before coding.

### [Represent a chosen subset as bits of an integer.](Chapter-09.md)

`F(mask)=\operatorname{opt}_{i\notin mask}(cost(mask,i)+F(mask\cup\{i\}))`

There are 2^n subsets. Each transition adds or removes one element, subject to feasibility.

### [Count or optimize subject to a bound, random transition, or digit restriction.](Chapter-10.md)

`F(state)=\sum_{choice}P(choice)F(next(state,choice))`

For probability, multiply by transition probabilities. For digit DP, track position, tightness and relevant history.

### [Use algebraic invariants, prefix summaries, or monotonic structures instead of a full DP table.](Chapter-11.md)

`bestEnding(i)=\max(a_i,a_i+bestEnding(i-1))`

This is Kadane’s recurrence; other problems in this group may use greedy, stacks, two pointers, prefix sums, or a specialized optimization—not necessarily DP.

## Five traps

1. Counting ordered sequences vs unordered combinations (loop order matters).
2. Inclusive interval endpoints vs strict compatibility.
3. In-place 0/1 knapsack requires descending capacity updates.
4. An impossible max state must not silently become zero.
5. LeetCode DP tag does not mean your best solution must use DP; greedy and other techniques can be stronger.

## Revision sequence

First learn [foundations](00-Mathematical-Foundations.md), then derive one representative problem per chapter, then use the [master index](Problem-Master-Index.md) to review your actual code.
