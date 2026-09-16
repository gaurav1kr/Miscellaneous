# Magic Pairs --- Count XOR Values in a Range Using a Binary Trie

## Problem Summary

We are given an array `A` of `N` positive integers and two integers `L`
and `R`.

A pair of indices `(i, j)` is a **magic pair** if:

``` text
i < j
```

and:

``` text
L <= (A[i] XOR A[j]) <= R
```

where `XOR` denotes the bitwise XOR operation.

We need to count the total number of such pairs.

> Note: The copied problem statement contains missing `svg` symbols. The
> condition above is inferred from the sample and explanation.

------------------------------------------------------------------------

# Sample

Input:

``` text
2
5 5 14
9 8 4 2 1
1 1 2
1
```

Output:

``` text
8
0
```

For the first test case:

``` text
A = [9, 8, 4, 2, 1]
L = 5
R = 14
```

The pair XOR values are:

``` text
9 XOR 8 = 1     -> invalid
9 XOR 4 = 13    -> valid
9 XOR 2 = 11    -> valid
9 XOR 1 = 8     -> valid

8 XOR 4 = 12    -> valid
8 XOR 2 = 10    -> valid
8 XOR 1 = 9     -> valid

4 XOR 2 = 6     -> valid
4 XOR 1 = 5     -> valid

2 XOR 1 = 3     -> invalid
```

Therefore:

``` text
answer = 8
```

------------------------------------------------------------------------

# Naive Approach

We could examine every pair:

``` cpp
for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
        int value = A[i] ^ A[j];

        if (L <= value && value <= R)
            answer++;
    }
}
```

But this requires:

``` text
O(N^2)
```

time.

For large `N`, this is too slow.

We need to use the bit structure of XOR.

------------------------------------------------------------------------

# Key Reduction

We want:

``` text
L <= (x XOR y) <= R
```

Instead of directly counting XOR values inside an interval, convert the
range into two prefix-count queries:

``` text
count(L <= XOR <= R)
=
count(XOR < R + 1)
-
count(XOR < L)
```

So the main problem becomes:

> Given `x` and a value `K`, how many previously seen values `y`
> satisfy:

``` text
x XOR y < K
```

This can be answered efficiently using a **binary trie**.

------------------------------------------------------------------------

# Process the Array from Left to Right

We process:

``` text
A[0], A[1], ..., A[N-1]
```

When processing `A[i]`, the trie contains only:

``` text
A[0 ... i-1]
```

Therefore every value returned by the trie corresponds to a pair:

``` text
(j, i)
```

where:

``` text
j < i
```

This means every valid pair is counted exactly once.

For each `x = A[i]`:

``` text
valid =
    countLessThan(x, R + 1)
    -
    countLessThan(x, L)
```

Then insert `x` into the trie.

------------------------------------------------------------------------

# Binary Trie

A binary trie stores numbers bit by bit.

For example, suppose we use four bits:

``` text
5 = 0101
6 = 0110
9 = 1001
```

Conceptually:

``` text
              root
             /    \
            0      1
           /        \
          1          0
         / \          \
        0   1          0
        |   |          |
        1   0          1
```

Every node stores:

``` text
count = number of inserted values passing through this node
```

This allows us to count entire groups of numbers without visiting each
number individually.

------------------------------------------------------------------------

# How to Count `x XOR y < K`

This is the most important part of the solution.

We inspect bits from the most significant bit to the least significant
bit.

Let:

``` text
xb = current bit of x
kb = current bit of K
yb = current bit of y
```

The XOR bit is:

``` text
xb XOR yb
```

------------------------------------------------------------------------

# Case 1: Current Bit of K Is 0

Suppose:

``` text
kb = 0
```

For the XOR value to remain smaller than `K`, the XOR bit cannot become
`1` at this position while all higher bits are equal.

Therefore the XOR bit must be:

``` text
0
```

That means:

``` text
yb = xb
```

So we can only continue through:

``` cpp
child[xb]
```

No values can be added to the answer immediately.

------------------------------------------------------------------------

# Case 2: Current Bit of K Is 1

Suppose:

``` text
kb = 1
```

There are two possibilities.

## XOR Bit = 0

If:

``` text
xb XOR yb = 0
```

then the XOR value becomes strictly smaller than `K` at this bit.

Once it is smaller at a more significant bit, all remaining lower bits
can be anything.

Therefore **every value in this branch is valid**.

XOR bit `0` requires:

``` text
yb = xb
```

So we add:

``` cpp
count(child[xb])
```

to the answer.

## XOR Bit = 1

If:

``` text
xb XOR yb = 1
```

then the XOR prefix is still equal to `K` at this bit.

Therefore we must continue checking lower bits.

XOR bit `1` requires:

``` text
yb = xb ^ 1
```

So continue through:

``` cpp
child[xb ^ 1]
```

------------------------------------------------------------------------

# Query Logic

The resulting logic is:

``` cpp
if (kb == 1) {

    // XOR bit = 0:
    // result becomes smaller than K.
    answer += count(child[xb]);

    // XOR bit = 1:
    // result is still equal to K so far.
    cur = child[xb ^ 1];
}
else {

    // XOR bit must remain 0.
    cur = child[xb];
}
```

This is the central binary-trie technique for XOR range counting.

------------------------------------------------------------------------

# Complete Algorithm

For every test case:

1.  Create an empty binary trie.
2.  Set:

``` text
answer = 0
```

3.  Process every array element `x` from left to right.
4.  Calculate:

``` text
upper = countLessThan(x, R + 1)
lower = countLessThan(x, L)
```

5.  Add:

``` text
upper - lower
```

to the answer. 6. Insert `x` into the trie. 7. Print the final answer.

------------------------------------------------------------------------

# C++ Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct Node {
    int child[2];
    int count;

    Node() {
        child[0] = child[1] = -1;
        count = 0;
    }
};

class BinaryTrie {
private:
    vector<Node> trie;

    // Suitable for non-negative signed 32-bit integer values.
    // Increase if the original constraints allow larger values.
    static const int MAX_BIT = 30;

public:
    BinaryTrie() {
        trie.emplace_back();
    }

    void insert(int x) {

        int cur = 0;

        trie[cur].count++;

        for (int bit = MAX_BIT; bit >= 0; --bit) {

            int b = (x >> bit) & 1;

            if (trie[cur].child[b] == -1) {

                trie[cur].child[b] =
                    (int)trie.size();

                trie.emplace_back();
            }

            cur = trie[cur].child[b];

            trie[cur].count++;
        }
    }

    // Count previously inserted values y such that:
    //
    //      (x XOR y) < k
    //
    ll countLessThan(int x, ll k) {

        if (k <= 0)
            return 0;

        int cur = 0;

        ll answer = 0;

        for (int bit = MAX_BIT;
             bit >= 0 && cur != -1;
             --bit) {

            int xb = (x >> bit) & 1;

            int kb = (k >> bit) & 1;

            if (kb == 1) {

                // If XOR bit is 0, the result becomes
                // smaller than k at this position.
                //
                // XOR bit 0 means:
                //
                // y_bit = x_bit

                int same =
                    trie[cur].child[xb];

                if (same != -1) {
                    answer += trie[same].count;
                }

                // To remain equal to k so far,
                // XOR bit must be 1.
                //
                // Therefore:
                //
                // y_bit = x_bit XOR 1

                cur =
                    trie[cur].child[xb ^ 1];
            }
            else {

                // k has bit 0.
                //
                // XOR bit must also be 0.
                //
                // Therefore:
                //
                // y_bit = x_bit

                cur =
                    trie[cur].child[xb];
            }
        }

        return answer;
    }
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {

        int N;
        int L, R;

        cin >> N >> L >> R;

        vector<int> A(N);

        for (int &x : A) {
            cin >> x;
        }

        BinaryTrie trie;

        ll answer = 0;

        for (int x : A) {

            // Count:
            //
            // L <= (x XOR y) <= R
            //
            // using:
            //
            // count(XOR < R + 1)
            // -
            // count(XOR < L)

            ll upper =
                trie.countLessThan(
                    x,
                    (ll)R + 1
                );

            ll lower =
                trie.countLessThan(
                    x,
                    (ll)L
                );

            answer += upper - lower;

            // Insert only after querying.
            //
            // This guarantees that x is paired only
            // with earlier indices.
            trie.insert(x);
        }

        cout << answer << '\n';
    }

    return 0;
}
```

------------------------------------------------------------------------

# Why Query Before Insert?

Suppose we process:

``` text
A[i]
```

If we inserted `A[i]` before querying, the trie would contain the
current element itself.

That could incorrectly create a pair:

``` text
(i, i)
```

because:

``` text
A[i] XOR A[i] = 0
```

Instead, always do:

``` text
query(A[i])
insert(A[i])
```

Then the trie contains only indices:

``` text
0 ... i-1
```

and every counted pair satisfies:

``` text
j < i
```

------------------------------------------------------------------------

# Why `long long` for the Answer?

The number of pairs can be as large as:

``` text
N * (N - 1) / 2
```

For sufficiently large `N`, this can exceed a 32-bit signed integer.

Therefore use:

``` cpp
long long answer;
```

The query counts should also use:

``` cpp
long long
```

------------------------------------------------------------------------

# Complexity Analysis

Let:

``` text
B = number of bits
```

For 32-bit integers:

``` text
B ≈ 31
```

For every array element we perform:

``` text
2 trie queries
1 trie insertion
```

Each operation examines at most `B` bits.

Therefore:

``` text
Time Complexity = O(N * B)
```

Since `B` is a small constant:

``` text
O(N * 31)
```

is effectively linear.

The trie may contain at most:

``` text
O(N * B)
```

nodes.

Therefore:

``` text
Space Complexity = O(N * B)
```

------------------------------------------------------------------------

# Why a Normal Set or Map Is Not Enough

The condition is based on:

``` text
A[i] XOR A[j]
```

XOR does not preserve normal numeric ordering.

For example, knowing that:

``` text
x < y
```

does not tell us whether:

``` text
(a XOR x) < (a XOR y)
```

Therefore a normal ordered set cannot directly answer the required range
query efficiently.

A binary trie works because XOR is determined independently at each bit
position.

------------------------------------------------------------------------

# Important Pattern to Remember

Whenever you see:

``` text
L <= (A[i] XOR A[j]) <= R
```

think:

``` text
count(XOR <= R)
-
count(XOR < L)
```

or equivalently:

``` text
count(XOR < R + 1)
-
count(XOR < L)
```

Then solve:

``` text
count(x XOR y < K)
```

using a binary trie.

------------------------------------------------------------------------

# Interview / Problem-Solving Takeaway

The solution is built from three observations.

## Observation 1: Convert a Range Into Prefix Counts

Instead of solving:

``` text
L <= XOR <= R
```

directly, transform it into:

``` text
count(XOR < R + 1)
-
count(XOR < L)
```

This is a very common technique:

``` text
count values in [L, R]
=
count values < R + 1
-
count values < L
```

## Observation 2: Process Left to Right

Insert only previously seen values.

This automatically handles:

``` text
i < j
```

and prevents duplicate pair counting.

## Observation 3: XOR Comparisons Are Bitwise

To determine whether:

``` text
x XOR y < K
```

compare the numbers from the most significant bit downward.

A binary trie lets us count entire branches at once.

------------------------------------------------------------------------

# Final Pattern

``` text
Magic Pair
    ↓
L <= A[i] XOR A[j] <= R
    ↓
Range Counting
    ↓
count(XOR < R + 1)
-
count(XOR < L)
    ↓
Process Array Left to Right
    ↓
Binary Trie of Previous Values
    ↓
O(N * B)
```

This **XOR range + binary trie** pattern is useful in many
competitive-programming and interview problems involving pair counts,
maximum XOR, and bounded XOR queries.
