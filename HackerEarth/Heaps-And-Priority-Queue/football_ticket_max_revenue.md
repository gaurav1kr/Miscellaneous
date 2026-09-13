# Maximum Revenue from Football Ticket Sales

## Problem Summary

There are **M** seating rows in a stadium.

-   Row `i` initially has `X[i]` vacant seats.
-   If a row currently has `K` vacant seats, the ticket price for that
    row is **K pounds**.
-   After selling one ticket from that row, its vacant seats decrease
    from `K` to `K - 1`.
-   There are **N** fans who will buy one ticket each.
-   We need to find the **maximum possible total revenue**.

### Constraints

``` text
1 <= M <= 1,000,000
1 <= N <= 1,000,000
1 <= X[i] <= 1,000,000
sum(X[i]) > N
```

------------------------------------------------------------------------

## Key Observation

To maximize revenue, for every fan we should sell a ticket from the row
having the **maximum number of vacant seats at that moment**.

If a row currently has `K` vacant seats:

``` text
Revenue += K
K becomes K - 1
```

Then repeat the same process for the next fan.

------------------------------------------------------------------------

## Example

Input:

``` text
3 4
1 2 4
```

Initially:

``` text
Rows: 1 2 4
```

### Ticket 1

Maximum vacant seats = `4`.

``` text
Revenue = 4
Rows = 1 2 3
```

### Ticket 2

Maximum vacant seats = `3`.

``` text
Revenue = 4 + 3 = 7
Rows = 1 2 2
```

### Ticket 3

Maximum vacant seats = `2`.

``` text
Revenue = 7 + 2 = 9
Rows = 1 1 2
```

### Ticket 4

Maximum vacant seats = `2`.

``` text
Revenue = 9 + 2 = 11
```

Therefore:

``` text
Answer = 11
```

------------------------------------------------------------------------

# Approach 1: Max Heap

A natural solution is to use a **max heap**.

In C++:

``` cpp
priority_queue<int> pq;
```

Insert the vacant-seat count of every row into the heap.

For every fan:

1.  Get the largest value.
2.  Add it to the revenue.
3.  Decrease it by one.
4.  Insert it back into the heap if seats remain.

### Pseudocode

``` text
Insert all X[i] into maxHeap

revenue = 0

repeat N times:

    k = maxHeap.top()
    maxHeap.pop()

    revenue += k

    k--

    if k > 0:
        maxHeap.push(k)
```

### Complexity

Building the heap:

``` text
O(M)
```

Selling `N` tickets:

``` text
O(N log M)
```

Overall:

``` text
O(M + N log M)
```

This approach is simple, but with `M` and `N` up to `10^6` and a tight
time limit, we can do better.

------------------------------------------------------------------------

# Approach 2: Frequency Array / Bucket Approach

Since:

``` text
X[i] <= 1,000,000
```

we can maintain a frequency array.

Define:

``` text
freq[k] = number of rows currently having exactly k vacant seats
```

For example, for:

``` text
1 2 4
```

we have:

``` text
freq[1] = 1
freq[2] = 1
freq[4] = 1
```

Maintain another variable:

``` text
currentMax
```

which represents the maximum number of vacant seats currently available
in any row.

Initially:

``` text
currentMax = max(X[i])
```

------------------------------------------------------------------------

## Selling One Ticket

Suppose:

``` text
currentMax = K
```

Then sell one ticket from such a row.

Revenue becomes:

``` text
revenue += K
```

One row leaves bucket `K`:

``` cpp
freq[K]--;
```

That row now contains `K - 1` vacant seats:

``` cpp
freq[K - 1]++;
```

If there are no rows remaining with `K` vacant seats:

``` cpp
freq[K] == 0
```

move `currentMax` downward until we find a non-empty bucket:

``` cpp
while (currentMax > 0 && freq[currentMax] == 0)
    currentMax--;
```

------------------------------------------------------------------------

# C++ Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    cin >> M >> N;

    const int MAX_X = 1000000;

    vector<int> freq(MAX_X + 1, 0);

    int currentMax = 0;

    for (int i = 0; i < M; ++i) {
        int x;
        cin >> x;

        freq[x]++;
        currentMax = max(currentMax, x);
    }

    long long revenue = 0;

    for (int i = 0; i < N; ++i) {

        // Find the row with the maximum number
        // of currently vacant seats.
        while (currentMax > 0 && freq[currentMax] == 0) {
            currentMax--;
        }

        // Sell one ticket.
        revenue += currentMax;

        // Remove one row from the current bucket.
        freq[currentMax]--;

        // The same row now has one fewer vacant seat.
        if (currentMax > 1) {
            freq[currentMax - 1]++;
        }
    }

    cout << revenue << '\n';

    return 0;
}
```

------------------------------------------------------------------------

# Complexity Analysis

Reading the input and constructing the frequency array:

``` text
O(M)
```

Processing `N` fans:

``` text
O(N)
```

`currentMax` only moves downward and starts at a maximum value of
`1,000,000`.

Therefore, all executions of:

``` cpp
while (currentMax > 0 && freq[currentMax] == 0)
```

combined cost at most:

``` text
O(1,000,000)
```

Hence the total complexity is:

``` text
O(M + N + 1,000,000)
```

which is effectively linear for the given constraints.

Memory complexity:

``` text
O(1,000,000)
```

------------------------------------------------------------------------

# Why `long long` Is Required

The answer can be much larger than the maximum value of a 32-bit signed
integer.

Therefore, do not use:

``` cpp
int revenue;
```

Use:

``` cpp
long long revenue = 0;
```

------------------------------------------------------------------------

# Interview / Problem-Solving Takeaway

The first observation is:

> Always sell the next ticket from the row having the maximum number of
> vacant seats.

This immediately suggests a **max heap**.

However, the constraints provide another important clue:

``` text
X[i] <= 1,000,000
```

Since the possible values are bounded, we can replace the heap with a
**frequency array (bucket)** and maintain a pointer to the current
maximum.

So the progression is:

``` text
Greedy
  ↓
Max Heap
  ↓
Observe bounded X[i]
  ↓
Frequency Array / Buckets
  ↓
O(M + N + MAX_X)
```

For the given `1 second` time limit, the **frequency-array approach is
preferable**.
