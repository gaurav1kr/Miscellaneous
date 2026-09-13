# Monk and Course Selection --- Priority Queue Solution

## Problem Summary

There are `C` courses and initially `N` students have already enrolled.

The `i`th existing student has IQ `Y[i]` and is enrolled in course `i`.

Monk and his `P-1` friends arrive one by one. Their IQ values are given
in array `X`.

For every arriving person, choose the course having the minimum value:

``` text
z = x * c
```

where:

-   `c` = number of students currently enrolled in that course.
-   `x` = sum of IQs of the last two students enrolled in that course.
-   If exactly one student is enrolled, `x` is that student's IQ.
-   If the course is empty, `x = 0`.

If multiple courses have the same `z`, choose the smallest course
number.

After a person selects a course, that course's state changes before the
next person chooses.

------------------------------------------------------------------------

## Key Observation

At any moment we only need to know which course has:

1.  the smallest `z`;
2.  and, on a tie, the smallest course number.

This is exactly what a **min-heap / priority queue** can maintain
efficiently.

After a person joins a course, only that one course changes.

Therefore:

``` text
take minimum course from heap
update that course
put it back into heap
```

------------------------------------------------------------------------

## Information Needed Per Course

For every course `i`, maintain:

``` text
count[i]
```

the number of enrolled students, and:

``` text
lastIQ[i]
```

the IQ of the most recently enrolled student.

We do not need to store the complete enrollment history.

Suppose a non-empty course currently has latest IQ:

``` text
lastIQ[i]
```

and a new student with IQ:

``` text
q
```

joins.

The last two students are now:

``` text
lastIQ[i] and q
```

so:

``` text
x = lastIQ[i] + q
```

After increasing the number of students:

``` text
z = count[i] * x
```

Finally:

``` text
lastIQ[i] = q
```

------------------------------------------------------------------------

## Initial State

The statement says that the `i`th existing student chooses the `i`th
course.

Therefore, for:

``` text
1 <= i <= N
```

course `i` initially contains exactly one student with IQ `Y[i]`.

Thus:

``` text
count[i] = 1
lastIQ[i] = Y[i]
x = Y[i]
z = Y[i]
```

For courses:

``` text
N+1 ... C
```

there are no students.

Therefore:

``` text
count[i] = 0
lastIQ[i] = 0
x = 0
z = 0
```

------------------------------------------------------------------------

## Priority Queue Ordering

Each heap entry contains:

``` text
(z, courseNumber)
```

The priority queue must return:

``` text
minimum z
```

and when two courses have equal `z`:

``` text
minimum course number
```

------------------------------------------------------------------------

## C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

struct Course
{
    long long z;
    int id;

    bool operator>(const Course& other) const
    {
        if (z != other.z)
            return z > other.z;

        return id > other.id;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int C, P, N;
    cin >> C >> P >> N;

    vector<long long> count(C + 1, 0);
    vector<long long> lastIQ(C + 1, 0);

    priority_queue<
        Course,
        vector<Course>,
        greater<Course>
    > pq;

    // Existing students.
    // Student i is already enrolled in course i.
    for (int i = 1; i <= N; ++i)
    {
        long long iq;
        cin >> iq;

        count[i] = 1;
        lastIQ[i] = iq;

        // One student:
        // x = iq
        // c = 1
        // z = iq
        pq.push({iq, i});
    }

    // Courses N+1 ... C are initially empty.
    for (int i = N + 1; i <= C; ++i)
    {
        // Empty course:
        // x = 0, c = 0, z = 0
        pq.push({0, i});
    }

    vector<long long> people(P);

    for (int i = 0; i < P; ++i)
        cin >> people[i];

    // Monk chooses first, followed by his friends.
    for (int i = 0; i < P; ++i)
    {
        long long newIQ = people[i];

        // Get the course with minimum z.
        // Ties automatically prefer the smaller ID.
        Course best = pq.top();
        pq.pop();

        int course = best.id;

        cout << course << ' ';

        long long newZ;

        if (count[course] == 0)
        {
            // This is the first student in the course.
            count[course] = 1;
            lastIQ[course] = newIQ;

            // For one student:
            // x = newIQ, c = 1
            newZ = newIQ;
        }
        else
        {
            // The previous latest student and the new
            // student are now the last two students.
            long long x = lastIQ[course] + newIQ;

            ++count[course];

            newZ = count[course] * x;

            // The new student becomes the latest student.
            lastIQ[course] = newIQ;
        }

        // Reinsert the updated course.
        pq.push({newZ, course});
    }

    cout << '\n';

    return 0;
}
```

------------------------------------------------------------------------

## Sample Walkthrough

Input:

``` text
5 4 4
2 8 5 1
9 10 5 1
```

Initially:

  Course     Initial Student IQ   Count   z
  -------- -------------------- ------- ---
  1                           2       1   2
  2                           8       1   8
  3                           5       1   5
  4                           1       1   1
  5                       Empty       0   0

The arriving IQ values are:

``` text
9 10 5 1
```

### Monk --- IQ 9

Minimum `z` is:

``` text
course 5 -> z = 0
```

So Monk chooses:

``` text
course 5
```

After joining:

``` text
count[5] = 1
lastIQ[5] = 9
z = 9
```

------------------------------------------------------------------------

### First Friend --- IQ 10

Current minimum is:

``` text
course 4 -> z = 1
```

The previous latest IQ is `1`.

So:

``` text
x = 1 + 10 = 11
count = 2
z = 2 * 11 = 22
```

Course selected:

``` text
4
```

------------------------------------------------------------------------

### Second Friend --- IQ 5

Current smallest course value is:

``` text
course 1 -> z = 2
```

Therefore the selected course is:

``` text
1
```

After enrollment:

``` text
x = 2 + 5 = 7
count = 2
z = 14
```

------------------------------------------------------------------------

### Third Friend --- IQ 1

The minimum remaining value is:

``` text
course 3 -> z = 5
```

Therefore:

``` text
course 3
```

The final output is:

``` text
5 4 1 3
```

------------------------------------------------------------------------

## Why Only the Latest IQ Is Needed

Suppose a course has previously received students with IQs:

``` text
q1, q2, q3, ..., qm
```

Before a new student `q` joins, the most recently enrolled student is:

``` text
qm
```

After `q` joins, the last two students are exactly:

``` text
qm and q
```

Thus:

``` text
x = qm + q
```

All earlier IQ values are irrelevant for calculating the new `z`.

Therefore keeping only:

``` text
lastIQ[i]
```

is sufficient.

------------------------------------------------------------------------

## Correctness Idea

Before each person chooses, the priority queue contains exactly one
entry for every course representing its current `z`.

Because the heap is ordered by:

``` text
(z, course number)
```

its top element is exactly the course required by the problem:

-   minimum `z`;
-   smallest course number when tied.

After the person joins, only that selected course changes.

The algorithm calculates its new:

``` text
count
lastIQ
z
```

and inserts the updated course back into the heap.

Thus the heap is correct again before the next person chooses.

Repeating this process produces exactly the sequence of course
selections required by the problem.

------------------------------------------------------------------------

## Why `long long` Is Important

The number of students in a course can grow significantly.

Also:

``` text
IQ <= 100000
```

The sum of the last two IQs can be:

``` text
200000
```

and `z` is:

``` text
count * x
```

which can exceed the range of a 32-bit signed integer.

Therefore use:

``` cpp
long long
```

for:

``` text
z
count
IQ arithmetic
```

------------------------------------------------------------------------

## Time Complexity

There are `C` courses in the priority queue.

Initialization takes at most:

``` text
O(C log C)
```

using individual heap insertions.

For each of the `P` arriving people we perform:

``` text
1 heap pop
1 heap push
```

Each costs:

``` text
O(log C)
```

Therefore:

``` text
Time = O(C log C + P log C)
```

or equivalently:

``` text
O((C + P) log C)
```

With:

``` text
C, P <= 100000
```

this is efficient.

------------------------------------------------------------------------

## Space Complexity

We store:

``` text
count[]      -> O(C)
lastIQ[]     -> O(C)
priority queue -> O(C)
people[]     -> O(P)
```

Therefore:

``` text
Space = O(C + P)
```

The `people` array can also be avoided by processing/storing input
differently, but it is easily within the memory limit.

------------------------------------------------------------------------

## Problem-Solving Pattern

``` text
Need minimum z before every enrollment
              |
              v
Tie by minimum course number
              |
              v
Priority queue ordered by (z, id)
              |
              v
Person chooses heap top
              |
              v
Only selected course changes
              |
              v
Update count and last IQ
              |
              v
new x = old lastIQ + new IQ
              |
              v
new z = new count * x
              |
              v
Push updated course back
              |
              v
Repeat for all P people
```

------------------------------------------------------------------------

## Key Takeaway

The problem looks like it requires tracking enrollment histories, but
only three pieces of state matter for each course:

``` text
current z
student count
latest student's IQ
```

A min-heap ordered by:

``` text
(z, course number)
```

then lets us simulate every selection efficiently.

Final complexity:

``` text
Time  : O((C + P) log C)
Space : O(C + P)
```
