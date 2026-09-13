# Population Outburst --- HackerEarth

## Problem

We start with a population represented conceptually as a tree.

-   The initial person has **ID `0`** and is at **level `0`**.
-   Every person has a reproduction capacity: the maximum number of
    children that person can have.
-   New people are given in birth order.
-   A younger person cannot start reproducing until all older people who
    can reproduce have exhausted their reproduction capacity.
-   For every new person, print:
    1.  the **parent ID**
    2.  the **level** of the new person
    3.  the new person's **age-wise rank among that parent's children**

A person whose reproduction capacity is `0` will never become a parent.

### Sample Input

``` text
9 2
1 2
2 1
5 2
4 1
10 0
15 0
21 0
23 1
42 100
```

### Sample Output

``` text
0 1 1
0 1 2
1 2 1
1 2 2
2 2 1
5 3 1
5 3 2
4 3 1
23 4 1
```

------------------------------------------------------------------------

## Understanding the Sample

Initially:

``` text
Person 0
Level = 0
Capacity = 2
```

Therefore the first two newborns belong to person `0`:

``` text
1 -> parent 0, level 1, rank 1
2 -> parent 0, level 1, rank 2
```

Person `0` has now exhausted its capacity.

Person `1` is the oldest person waiting to reproduce. Its capacity is
`2`:

``` text
5 -> parent 1, level 2, rank 1
4 -> parent 1, level 2, rank 2
```

Next comes person `2`, whose capacity is `1`:

``` text
10 -> parent 2, level 2, rank 1
```

Then person `5`:

``` text
15 -> parent 5, level 3, rank 1
21 -> parent 5, level 3, rank 2
```

The same process continues.

------------------------------------------------------------------------

## Key Observation

The statement:

> A younger member cannot reproduce until all older eligible members
> have exhausted their reproduction capacity.

implies **FIFO ordering**.

Therefore, this is naturally a **queue/deque simulation**.

The person at the front is always the current parent.

We continue assigning children to that person until their capacity
becomes zero. Only then do we remove them and move to the next waiting
person.

------------------------------------------------------------------------

## What Should Be Stored?

We do **not** need to construct the actual tree.

For each person who can reproduce in the future, we only need:

``` text
id
level
remaining reproduction capacity
next child rank
```

For example:

``` text
Person 42
capacity = 100
```

should be stored as **one record**:

``` text
{42, level, remaining = 100, nextRank = 1}
```

Do not create 100 queue entries.

Also, if:

``` text
capacity = 0
```

the person never needs to be inserted into the queue.

------------------------------------------------------------------------

## Algorithm

For every newborn `(id, capacity)`:

1.  The person at the front of the deque is the parent.
2.  The child's level is:

``` text
parent.level + 1
```

3.  Its sibling rank is the parent's current `nextRank`.
4.  Print:

``` text
parent.id childLevel siblingRank
```

5.  Decrease the parent's remaining capacity.
6.  Increment the parent's next child rank.
7.  If the parent's remaining capacity becomes zero, remove the parent
    from the front.
8.  If the newborn's capacity is greater than zero, insert the newborn
    at the back of the deque.

------------------------------------------------------------------------

## C++ Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

struct Person
{
    int id;
    int level;
    int remaining;
    int nextRank;
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, rootCapacity;
    cin >> n >> rootCapacity;

    deque<Person> q;

    // Initial person: ID 0, level 0
    if (rootCapacity > 0)
    {
        q.push_back({0, 0, rootCapacity, 1});
    }

    for (int i = 0; i < n; i++)
    {
        int id, capacity;
        cin >> id >> capacity;

        // The oldest eligible person is always the parent.
        Person &parent = q.front();

        int childLevel = parent.level + 1;
        int siblingRank = parent.nextRank;

        cout << parent.id << ' '
             << childLevel << ' '
             << siblingRank << '\n';

        // Parent has produced one child.
        parent.remaining--;
        parent.nextRank++;

        // If the parent is exhausted, remove it.
        if (parent.remaining == 0)
        {
            q.pop_front();
        }

        // Store the newborn only if it can reproduce later.
        if (capacity > 0)
        {
            q.push_back({
                id,
                childLevel,
                capacity,
                1
            });
        }
    }

    return 0;
}
```

------------------------------------------------------------------------

## Dry Run

For:

``` text
9 2
1 2
2 1
5 2
4 1
10 0
15 0
21 0
23 1
42 100
```

Initially:

``` text
Queue = [0(capacity=2)]
```

### Birth of 1

``` text
Parent = 0
Child level = 1
Rank = 1

Output: 0 1 1
```

Queue conceptually becomes:

``` text
0(remaining=1), 1(capacity=2)
```

### Birth of 2

``` text
Parent = 0
Child level = 1
Rank = 2

Output: 0 1 2
```

`0` is now exhausted:

``` text
Queue = [1, 2]
```

### Birth of 5

``` text
Parent = 1
Child level = 2
Rank = 1

Output: 1 2 1
```

### Birth of 4

``` text
Parent = 1
Child level = 2
Rank = 2

Output: 1 2 2
```

`1` is exhausted, so the next parent is `2`.

The same process continues until all births are processed.

------------------------------------------------------------------------

## Complexity

Let `N` be the number of newborns.

### Time

Each newborn is processed exactly once:

``` text
O(N)
```

Each reproducing person is inserted into and removed from the deque at
most once.

### Space

We store only people with non-zero reproduction capacity who are still
waiting or reproducing:

``` text
O(P)
```

where `P` is the number of currently active/waiting reproducing people.

We do **not** store the complete population tree.

------------------------------------------------------------------------

## Interview Takeaway

The important insight is not that this is a tree problem.

The important clue is:

``` text
Older eligible members reproduce before younger members.
```

That implies:

``` text
FIFO -> Queue
```

So the reasoning becomes:

``` text
Oldest eligible person
        |
        v
   Front of deque
        |
        v
Keep assigning children
until capacity is exhausted
        |
        v
Pop front
        |
        v
Next oldest eligible person
```

This lets us simulate the population directly without constructing a
tree.
