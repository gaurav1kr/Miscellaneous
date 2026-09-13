# Monk Loves Candy — Maximum Candies Using a Priority Queue

## Problem Summary

There are `N` bags of candies.

- Bag `i` initially contains `A[i]` candies.
- In one minute, Monk chooses one bag and eats all candies from it.
- If the bag contained `X` candies before eating, it immediately refills with:

```text
floor(X / 2)
```

candies.

- Monk has exactly `K` minutes.
- We need to find the **maximum total number of candies Monk can consume**.

### Constraints

```text
1 <= T <= 10
1 <= N <= 100000
0 <= K <= 100000
0 <= A[i] <= 10^10
```

---

# Key Observation

To maximize the total number of candies consumed, Monk should always choose the bag with the **maximum number of candies currently available**.

Why?

If two bags contain:

```text
X >= Y
```

then choosing `X` gives at least as many candies immediately as choosing `Y`.

Since after eating, the chosen bag becomes:

```text
floor(X / 2)
```

we again need to know the largest bag for the next minute.

This is exactly what a **max heap / priority queue** is designed for.

---

# Data Structure

In C++:

```cpp
priority_queue<long long> pq;
```

A `priority_queue` returns the largest element in:

```text
O(1)
```

for `top()`, while insertion and removal take:

```text
O(log N)
```

---

# Algorithm

For every test case:

1. Insert all `N` bag values into a max heap.
2. Initialize:

```text
answer = 0
```

3. Repeat `K` times:
   - Take the maximum value `X`.
   - Add `X` to the answer.
   - Remove `X` from the heap.
   - Insert `X / 2` back into the heap.
4. Print the answer.

---

# Example

Input:

```text
1
5 3
2 1 7 4 2
```

Initial bags:

```text
2 1 7 4 2
```

The max heap gives:

```text
7
```

## Minute 1

Take:

```text
7
```

Monk eats:

```text
7
```

Total:

```text
answer = 7
```

The bag refills with:

```text
7 / 2 = 3
```

New state conceptually:

```text
2 1 3 4 2
```

---

## Minute 2

Maximum:

```text
4
```

Monk eats:

```text
4
```

Total:

```text
answer = 7 + 4 = 11
```

Bag refills with:

```text
4 / 2 = 2
```

State:

```text
2 1 3 2 2
```

---

## Minute 3

Maximum:

```text
3
```

Monk eats:

```text
3
```

Total:

```text
answer = 11 + 3 = 14
```

Bag refills with:

```text
3 / 2 = 1
```

Final answer:

```text
14
```

---

# C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {

        int N, K;
        cin >> N >> K;

        priority_queue<long long> pq;

        for (int i = 0; i < N; ++i) {
            long long x;
            cin >> x;

            pq.push(x);
        }

        long long candies = 0;

        for (int i = 0; i < K; ++i) {

            long long x = pq.top();
            pq.pop();

            // Monk eats all candies from the largest bag.
            candies += x;

            // The bag magically refills with floor(x / 2).
            pq.push(x / 2);
        }

        cout << candies << '\n';
    }

    return 0;
}
```

---

# Why `long long` Is Required

The constraints allow:

```text
A[i] <= 10^10
```

which is already larger than the maximum value supported by a signed 32-bit `int`.

Also, Monk may consume large values repeatedly.

Therefore use:

```cpp
long long
```

for:

```text
A[i]
heap values
answer
```

---

# Complexity Analysis

Building the heap requires:

```text
O(N log N)
```

For each of the `K` minutes:

- one `pop`
- one `push`

Each costs:

```text
O(log N)
```

Therefore:

```text
Time Complexity = O((N + K) log N)
```

Memory:

```text
O(N)
```

---

# Why Greedy Works

At every minute, Monk wants to maximize the number of candies consumed immediately.

Suppose the maximum bag contains:

```text
X
```

and another bag contains:

```text
Y
```

where:

```text
X >= Y
```

Choosing `X` gives at least as much immediate gain as choosing `Y`.

After the choice, the selected bag becomes half its previous size, and the same decision problem repeats.

Therefore the optimal strategy is:

> Always consume the bag with the maximum number of candies currently available.

---

# Interview / Problem-Solving Takeaway

A priority queue is especially useful when:

- you repeatedly need the current maximum or minimum,
- after selecting it, the value changes,
- and the updated value must participate in future selections.

This problem has exactly that pattern:

```text
Get maximum
    ↓
Consume it
    ↓
Update value to X / 2
    ↓
Insert it back
    ↓
Repeat
```

So the natural solution is:

```text
Greedy + Max Heap
```

with:

```text
O((N + K) log N)
```

time complexity.
