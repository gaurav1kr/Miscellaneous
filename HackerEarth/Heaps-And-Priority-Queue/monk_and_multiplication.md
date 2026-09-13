# Monk and Multiplication --- Top 3 Product in Every Prefix

## Problem Summary

Given an integer array `A` of size `N`, for every index `i` we need to
find the product of:

-   the largest element,
-   the second largest element, and
-   the third largest element

in the prefix:

``` text
A[1 ... i]
```

If fewer than 3 elements are available, print:

``` text
-1
```

Two elements may have the same value, as long as they are from different
indices.

### Constraints

``` text
1 <= N <= 100000
0 <= A[i] <= 1000000
```

------------------------------------------------------------------------

## Key Observation

For every prefix, we only need the **three largest values seen so far**.

Therefore, instead of sorting every prefix or maintaining all elements,
keep three variables:

``` text
first  = largest
second = second largest
third  = third largest
```

Whenever a new element `x` arrives, update these three values.

------------------------------------------------------------------------

## Updating the Top Three

For every `x`:

``` cpp
if (x >= first) {
    third = second;
    second = first;
    first = x;
}
else if (x >= second) {
    third = second;
    second = x;
}
else if (x > third) {
    third = x;
}
```

The use of `>=` is important because duplicate values are allowed at
different indices.

For example:

``` text
5 5 4
```

has valid top-three values:

``` text
5, 5, 4
```

------------------------------------------------------------------------

## Example

Input:

``` text
5
1 2 3 4 5
```

### Index 1

Elements:

``` text
1
```

There are fewer than 3 elements.

``` text
Output = -1
```

### Index 2

Elements:

``` text
1 2
```

Again, fewer than 3 elements.

``` text
Output = -1
```

### Index 3

Elements:

``` text
1 2 3
```

Top three:

``` text
3, 2, 1
```

Product:

``` text
3 * 2 * 1 = 6
```

### Index 4

Elements:

``` text
1 2 3 4
```

Top three:

``` text
4, 3, 2
```

Product:

``` text
4 * 3 * 2 = 24
```

### Index 5

Elements:

``` text
1 2 3 4 5
```

Top three:

``` text
5, 4, 3
```

Product:

``` text
5 * 4 * 3 = 60
```

Final output:

``` text
-1
-1
6
24
60
```

------------------------------------------------------------------------

# C++ Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    long long first = -1;
    long long second = -1;
    long long third = -1;

    for (int i = 0; i < N; ++i) {

        long long x;
        cin >> x;

        if (x >= first) {
            third = second;
            second = first;
            first = x;
        }
        else if (x >= second) {
            third = second;
            second = x;
        }
        else if (x > third) {
            third = x;
        }

        if (i < 2) {
            cout << -1 << '\n';
        }
        else {
            cout << first * second * third << '\n';
        }
    }

    return 0;
}
```

------------------------------------------------------------------------

# Why `long long` Is Required

The maximum value of an element is:

``` text
10^6
```

The maximum possible product is:

``` text
10^6 * 10^6 * 10^6
= 10^18
```

A 32-bit `int` cannot hold this value.

Therefore use:

``` cpp
long long
```

for `first`, `second`, `third`, and the resulting product.

------------------------------------------------------------------------

# Complexity

For every element we perform only a constant number of comparisons and
assignments.

Therefore:

``` text
Time Complexity  : O(N)
Space Complexity : O(1)
```

This is optimal because every input element must be examined at least
once.

------------------------------------------------------------------------

# Alternative: Priority Queue

Since the problem is related to priority queues, another possible
approach is to maintain a priority queue.

However, we only need the largest three values, so maintaining three
variables is simpler and faster.

A priority-queue-based approach generally introduces logarithmic
operations, whereas the direct top-three approach requires only constant
work per element.

Therefore the preferred solution is:

``` text
Maintain Top 3
      ↓
Process each element once
      ↓
O(N) time
      ↓
O(1) extra space
```

------------------------------------------------------------------------

# Interview / Problem-Solving Takeaway

The important observation is that we do **not** need to recompute the
three largest elements for every prefix.

When processing:

``` text
A[1], A[2], ..., A[i]
```

suppose we already know the top three values for:

``` text
A[1 ... i-1]
```

When `A[i]` arrives, only this new value can change the existing top
three.

Therefore, maintain the answer incrementally.

This is a common pattern in streaming/prefix problems:

> If only the top `K` elements are required and `K` is very small,
> maintaining those `K` elements directly can be better than maintaining
> the entire data set in a heap or sorted structure.
