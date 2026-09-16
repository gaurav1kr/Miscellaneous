# Maximum XOR Rectangular Submatrix

## Problem Summary

We are given an `N x M` matrix of Good Luck values.

The Good Luck value of a rectangular submatrix is defined as the XOR of
all elements inside that rectangle.

We need to find the **maximum possible XOR value among all rectangular
submatrices**.

### Constraints

``` text
1 <= N <= 10000
1 <= M <= 20
N >= M
1 <= Good Luck value <= 10^8
```

The important constraint is:

``` text
M <= 20
```

while:

``` text
N <= 10000
```

Therefore, any quadratic work should be performed over `M`, not `N`.

------------------------------------------------------------------------

# Key Idea

The 2-D problem can be reduced to a collection of 1-D problems.

The transformation is:

``` text
Maximum XOR Rectangle
        ↓
Fix two columns
        ↓
Compress each row using XOR
        ↓
Maximum XOR Contiguous Subarray
        ↓
Prefix XOR
        ↓
Maximum XOR Pair
        ↓
Binary Trie
```

------------------------------------------------------------------------

# Step 1: Fix Left and Right Columns

Suppose we fix two columns:

``` text
left ... right
```

For each row, compute the XOR of all elements between these columns.

For example:

``` text
1 2 3
4 5 6
7 8 9
```

Suppose:

``` text
left = 0
right = 1
```

For each row:

``` text
1 XOR 2 = 3
4 XOR 5 = 1
7 XOR 8 = 15
```

The matrix is compressed into:

``` text
3 1 15
```

Now choosing a contiguous range of rows in this array corresponds
exactly to choosing a rectangular submatrix between the fixed `left` and
`right` columns.

Therefore, for every pair of columns, the problem becomes:

> Find the maximum XOR of a contiguous subarray.

------------------------------------------------------------------------

# Step 2: Efficiently Build the Compressed Array

For every new `left` column, initialize:

``` cpp
rowXor[0 ... N-1] = 0;
```

Then gradually extend `right`:

``` cpp
for (int right = left; right < M; ++right) {
    for (int row = 0; row < N; ++row) {
        rowXor[row] ^= matrix[row][right];
    }
}
```

After this update:

``` text
rowXor[row]
```

contains the XOR of:

``` text
matrix[row][left ... right]
```

This avoids recomputing the row XOR from scratch for every pair of
columns.

------------------------------------------------------------------------

# Step 3: Maximum XOR Contiguous Subarray

Now consider a 1-D array:

``` text
a[0], a[1], ..., a[N-1]
```

Define prefix XOR:

``` text
prefix[i] = a[0] XOR a[1] XOR ... XOR a[i]
```

The XOR of a subarray `[L ... R]` can be calculated as:

``` text
prefix[R] XOR prefix[L - 1]
```

Therefore, for every current prefix XOR `P`, we need to find an earlier
prefix XOR `Q` that maximizes:

``` text
P XOR Q
```

This becomes a **maximum XOR pair** problem.

------------------------------------------------------------------------

# Step 4: Binary Trie

A binary trie stores integers bit by bit.

When querying a number `x`, for every bit we prefer the opposite bit.

Why?

Because:

``` text
0 XOR 1 = 1
1 XOR 0 = 1
```

A `1` in a higher bit position makes the XOR value larger.

Therefore:

``` text
if current bit of x is 0:
    prefer trie branch 1

if current bit of x is 1:
    prefer trie branch 0
```

If the preferred branch does not exist, use the same-bit branch.

------------------------------------------------------------------------

# Important: Insert Prefix XOR 0

Before processing the compressed array, insert:

``` text
0
```

into the trie.

This represents the empty prefix.

It allows us to correctly calculate subarrays starting at index `0`.

For example:

``` text
XOR(a[0 ... R]) = prefix[R] XOR 0
```

------------------------------------------------------------------------

# Example

Matrix:

``` text
1 2 3
4 5 6
7 8 9
```

Choose columns `0` through `1`.

Compressed array:

``` text
1 XOR 2 = 3
4 XOR 5 = 1
7 XOR 8 = 15
```

Therefore:

``` text
rowXor = [3, 1, 15]
```

Prefix XOR values are:

``` text
0
3
3 XOR 1 = 2
3 XOR 1 XOR 15 = 13
```

So the prefix values are:

``` text
0, 3, 2, 13
```

For every prefix value, query the binary trie for the previous prefix
that produces the maximum XOR.

Repeating this process for every pair of columns finds the maximum XOR
rectangle.

------------------------------------------------------------------------

# Complete C++ Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 10000;
const int MAXBITS = 27;

// At most N + 1 prefix XOR values are inserted.
// Each value may create at most MAXBITS + 1 trie nodes.
const int MAXNODE = (MAXN + 5) * 29;

int trie[MAXNODE][2];
int nodes;

void resetTrie() {
    nodes = 1;
    trie[0][0] = trie[0][1] = -1;
}

void newNode(int node) {
    trie[node][0] = trie[node][1] = -1;
}

void insertValue(int x) {
    int cur = 0;

    for (int bit = MAXBITS; bit >= 0; --bit) {
        int b = (x >> bit) & 1;

        if (trie[cur][b] == -1) {
            trie[cur][b] = nodes;
            newNode(nodes);
            ++nodes;
        }

        cur = trie[cur][b];
    }
}

int getMaximumXor(int x) {
    int cur = 0;
    int result = 0;

    for (int bit = MAXBITS; bit >= 0; --bit) {
        int b = (x >> bit) & 1;

        // To maximize XOR, prefer the opposite bit.
        int want = 1 - b;

        if (trie[cur][want] != -1) {
            result |= (1 << bit);
            cur = trie[cur][want];
        } else {
            cur = trie[cur][b];
        }
    }

    return result;
}

int maximumSubarrayXor(const vector<int>& a) {
    resetTrie();

    int prefix = 0;
    int best = 0;

    // Empty prefix.
    insertValue(0);

    for (int x : a) {
        prefix ^= x;

        // Find the previous prefix giving maximum XOR.
        best = max(best, getMaximumXor(prefix));

        // Make this prefix available for future subarrays.
        insertValue(prefix);
    }

    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<vector<int>> matrix(N, vector<int>(M));

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> matrix[i][j];
        }
    }

    int answer = 0;

    vector<int> rowXor(N);

    // Fix the left column.
    for (int left = 0; left < M; ++left) {

        fill(rowXor.begin(), rowXor.end(), 0);

        // Gradually extend the right column.
        for (int right = left; right < M; ++right) {

            // Compress matrix[left ... right] into a 1-D array.
            for (int row = 0; row < N; ++row) {
                rowXor[row] ^= matrix[row][right];
            }

            // Find the best contiguous range of rows.
            answer = max(
                answer,
                maximumSubarrayXor(rowXor)
            );
        }
    }

    cout << answer << '\n';

    return 0;
}
```

------------------------------------------------------------------------

# Complexity Analysis

There are:

``` text
M * (M + 1) / 2
```

possible pairs of columns.

For each column pair, we process `N` rows.

For every prefix XOR, the binary trie examines approximately `B` bits,
where:

``` text
B ≈ 28
```

because the input values are at most `10^8`.

Therefore:

``` text
Time Complexity = O(M^2 * N * B)
```

Given:

``` text
M <= 20
N <= 10000
B ≈ 28
```

the number of column pairs is at most:

``` text
20 * 21 / 2 = 210
```

The approximate number of bit operations is:

``` text
210 * 10000 * 28
≈ 59 million
```

which is feasible with an optimized C++ implementation.

The trie contains approximately:

``` text
O(N * B)
```

nodes.

Therefore:

``` text
Space Complexity = O(N * B + N * M)
```

including the matrix.

------------------------------------------------------------------------

# Why We Do Not Fix Rows

An alternative might be to fix two rows.

However:

``` text
N <= 10000
M <= 20
```

Fixing two rows would require approximately:

``` text
O(N^2)
```

row combinations.

In the worst case:

``` text
10000^2 = 100,000,000
```

pairs.

Instead, fixing columns requires only:

``` text
20^2
```

scale work.

This is why the condition:

``` text
N >= M
```

is an important hint in the problem.

------------------------------------------------------------------------

# Interview / Problem-Solving Takeaway

There are three important observations.

## Observation 1: Exploit the Small Dimension

Whenever a matrix problem has highly asymmetric dimensions such as:

``` text
N = 10000
M = 20
```

try to make the quadratic part depend on the smaller dimension.

Here:

``` text
O(M^2 * ...)
```

is practical, while:

``` text
O(N^2 * ...)
```

is not.

## Observation 2: Compress 2-D Into 1-D

Fixing two boundaries of a rectangle often allows the remaining
dimension to become a standard 1-D problem.

Here:

``` text
Fix left/right columns
        ↓
XOR each row between them
        ↓
1-D maximum XOR subarray
```

## Observation 3: Prefix XOR + Trie

For XOR subarray problems:

``` text
subarray XOR = prefix XOR previousPrefix
```

Therefore maximum subarray XOR becomes a maximum XOR-pair problem over
prefix values.

A binary trie finds the best XOR partner efficiently.

------------------------------------------------------------------------

# Final Pattern to Remember

``` text
2-D Maximum XOR Rectangle
          ↓
Exploit M <= 20
          ↓
Enumerate O(M^2) column pairs
          ↓
Compress rows using XOR
          ↓
1-D Maximum XOR Subarray
          ↓
Prefix XOR
          ↓
Binary Trie
          ↓
O(M^2 * N * B)
```

This combination of **dimension reduction + prefix XOR + binary trie**
is the central idea behind the solution.
