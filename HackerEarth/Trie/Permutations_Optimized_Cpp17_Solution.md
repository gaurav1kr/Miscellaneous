# Permutations --- Optimized C++17 Solution

## Problem Statement

You are given a permutation:

`A = {a1, a2, ..., aN}`

of `N` integers from `0` to `N - 1`.

You must process `Q` online queries of two types:

1.  **Swap**
    -   `1 X Y`
    -   Swap `A[X]` and `A[Y]`.
2.  **K-th MEX**
    -   `2 L R K`
    -   Print `MexK(A[L], ..., A[R])`, where `MexK` is the **K-th
        smallest non-negative integer that does not occur** in the
        subarray `A[L...R]`.

The queries are encoded using the answer to the previous type-2 query:

-   `X = X' XOR LastAns`
-   `Y = Y' XOR LastAns`
-   `L = L' XOR LastAns`
-   `R = R' XOR LastAns`
-   `K = K' XOR LastAns`

Initially, `LastAns = 0`.

### Constraints

-   `1 <= N <= 10^5`
-   `1 <= Q <= 2 * 10^5`
-   `1 <= X, Y <= N`
-   `1 <= L <= R <= N`
-   `1 <= K <= 10^5`
-   `0 <= ai < N`
-   `A` is a permutation.

------------------------------------------------------------------------

## Key Observation

Because `A` is a permutation, every value from `0` to `N - 1` occurs
**exactly once**.

Maintain:

``` text
pos[value] = current array position of value
```

For a query `[L, R]`, a value `x` is present in the subarray exactly
when:

``` text
L <= pos[x] <= R
```

Therefore, the problem can be viewed over the **value domain** rather
than the array-position domain.

For any group of consecutive values:

``` text
number of missing values
    = number of values in the group
      - number whose positions are inside [L, R]
```

This allows us to skip entire groups of values while searching for the
K-th missing number.

------------------------------------------------------------------------

## Approach --- Square Root Decomposition

Divide the value range `[0, N - 1]` into blocks of approximately
`sqrt(N)` values.

For each value block, maintain a sorted vector containing the **current
array positions** of all values belonging to that block.

For example, if a block represents values:

``` text
0, 1, 2, ..., 319
```

then its vector contains:

``` text
pos[0], pos[1], pos[2], ..., pos[319]
```

sorted by position.

### Counting Present Values in a Block

For a query `[L, R]`, the number of values from a block that occur
inside the subarray can be calculated with two binary searches:

``` cpp
upper_bound(block.begin(), block.end(), R)
-
lower_bound(block.begin(), block.end(), L)
```

If a block contains `B` values and `P` of them are present in `[L, R]`,
then:

``` text
missing = B - P
```

### Finding the K-th Missing Value

Process blocks from smallest values to largest values.

For each block:

1.  Count how many values from the block are present in `[L, R]`.
2.  Calculate how many are missing.
3.  If `K > missing`, skip the entire block and set:

``` text
K -= missing
```

4.  Otherwise, the answer lies inside this block.
5.  Scan the individual values in that block and test:

``` cpp
pos[value] < L || pos[value] > R
```

Each such value is missing. The value that reduces `K` to zero is the
answer.

### Values Greater Than or Equal to N

The permutation contains only values `0 ... N-1`.

Therefore every value:

``` text
N, N+1, N+2, ...
```

is automatically missing.

If all blocks are processed and `K` is still positive:

``` text
answer = N + K - 1
```

------------------------------------------------------------------------

## Handling Swap Queries

Suppose positions `X` and `Y` contain values:

``` text
vx = A[X]
vy = A[Y]
```

After the swap:

``` text
pos[vx] = Y
pos[vy] = X
```

If `vx` and `vy` belong to **different value blocks**, update their
corresponding sorted position vectors:

``` text
block(vx): X -> Y
block(vy): Y -> X
```

Only one element changes in each block, so sorted order can be restored
by moving that element left or right.

### Important Optimization

If both values belong to the **same value block**, the block's set of
positions does not change.

Before:

``` text
..., X, ..., Y, ...
```

After swapping the two values, that same block still owns positions:

``` text
..., X, ..., Y, ...
```

So the block vector requires **no update**. Only `A[]` and `pos[]` are
changed.

------------------------------------------------------------------------

## C++17 Implementation

``` cpp
#include <bits/stdc++.h>
using namespace std;

class Solver {
private:
    int n;
    int BLOCK;
    int numBlocks;

    vector<int> a;
    vector<int> pos;

    // Sorted positions for values belonging to each value block
    vector<vector<int>> blockPos;

    int getBlock(int value) const {
        return value / BLOCK;
    }

    // Number of values from block b whose positions lie in [L, R]
    int countPresent(int b, int L, int R) const {
        const auto &v = blockPos[b];

        return upper_bound(v.begin(), v.end(), R)
             - lower_bound(v.begin(), v.end(), L);
    }

    // Replace one position in a block and restore sorted order
    void replacePosition(int b, int oldPos, int newPos) {
        auto &v = blockPos[b];

        auto it = lower_bound(v.begin(), v.end(), oldPos);

        // oldPos must exist because it belongs to this value block
        *it = newPos;

        int idx = int(it - v.begin());

        while (idx > 0 && v[idx] < v[idx - 1]) {
            swap(v[idx], v[idx - 1]);
            --idx;
        }

        while (idx + 1 < (int)v.size() &&
               v[idx] > v[idx + 1]) {
            swap(v[idx], v[idx + 1]);
            ++idx;
        }
    }

public:
    explicit Solver(int N) : n(N) {
        BLOCK = 320;
        numBlocks = (n + BLOCK - 1) / BLOCK;

        a.resize(n + 1);
        pos.resize(n);
        blockPos.resize(numBlocks);
    }

    void readPermutation() {
        for (int i = 1; i <= n; ++i) {
            cin >> a[i];
            pos[a[i]] = i;
        }

        // Blocks are built over VALUES, not array positions
        for (int value = 0; value < n; ++value) {
            int b = getBlock(value);
            blockPos[b].push_back(pos[value]);
        }

        for (auto &v : blockPos) {
            sort(v.begin(), v.end());
        }
    }

    void swapPositions(int x, int y) {
        if (x == y)
            return;

        int vx = a[x];
        int vy = a[y];

        int bx = getBlock(vx);
        int by = getBlock(vy);

        if (bx == by) {
            // Same value block: its set of positions is unchanged
            swap(a[x], a[y]);

            pos[vx] = y;
            pos[vy] = x;

            return;
        }

        // vx moves from x to y
        replacePosition(bx, x, y);

        // vy moves from y to x
        replacePosition(by, y, x);

        swap(a[x], a[y]);

        pos[vx] = y;
        pos[vy] = x;
    }

    long long kthMissing(int L, int R, long long K) const {
        for (int b = 0; b < numBlocks; ++b) {

            int startValue = b * BLOCK;
            int endValue = min(n - 1, startValue + BLOCK - 1);

            int blockSize = endValue - startValue + 1;

            int present = countPresent(b, L, R);

            long long missing =
                (long long)blockSize - present;

            if (K > missing) {
                K -= missing;
                continue;
            }

            // Answer is inside this value block
            for (int value = startValue;
                 value <= endValue;
                 ++value) {

                if (pos[value] < L || pos[value] > R) {
                    --K;

                    if (K == 0)
                        return value;
                }
            }
        }

        // Every value >= n is absent from the permutation
        return (long long)n + K - 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    Solver solver(N);
    solver.readPermutation();

    int Q;
    cin >> Q;

    long long lastAns = 0;

    while (Q--) {
        int type;
        cin >> type;

        if (type == 1) {
            long long Xp, Yp;
            cin >> Xp >> Yp;

            int X = (int)(Xp ^ lastAns);
            int Y = (int)(Yp ^ lastAns);

            solver.swapPositions(X, Y);
        }
        else {
            long long Lp, Rp, Kp;
            cin >> Lp >> Rp >> Kp;

            int L = (int)(Lp ^ lastAns);
            int R = (int)(Rp ^ lastAns);
            long long K = Kp ^ lastAns;

            long long ans = solver.kthMissing(L, R, K);

            cout << ans << '\n';

            lastAns = ans;
        }
    }

    return 0;
}
```

------------------------------------------------------------------------

## Correctness

For every value `x` in `[0, N-1]`, `pos[x]` is its unique current
position because the array is always a permutation.

Thus, for a query `[L,R]`:

``` text
x is present <=> L <= pos[x] <= R
```

Each value block contains a consecutive range of candidate values. Its
sorted position vector lets us count exactly how many of those
candidates are present in `[L,R]`. Subtracting this count from the block
size gives exactly the number of missing values in that value range.

When the algorithm skips a block, it subtracts exactly the number of
missing values skipped. Consequently, the first block for which
`K <= missing` must contain the required K-th missing value. Scanning
that block in increasing value order then returns precisely that value.

If the answer is not in `[0,N-1]`, all remaining non-negative integers
starting at `N` are absent, so the remaining K-th missing value is
`N + K - 1`.

------------------------------------------------------------------------

## Time Complexity

Let the block size be `B`, with approximately `N/B` blocks.

### Build

Constructing and sorting all blocks:

``` text
O(N log B)
```

### Type 1 --- Swap

For values in different blocks:

-   Find the old position using `lower_bound`: `O(log B)`
-   Restore sorted order after replacement: worst-case `O(B)`
-   Two blocks may be updated.

Therefore:

``` text
O(B)
```

worst case per swap.

If both values belong to the same block, the block vectors do not
change, so the update is:

``` text
O(1)
```

apart from simple array assignments/swaps.

### Type 2 --- K-th Missing Query

There are approximately:

``` text
N / B
```

blocks.

For every visited block, two binary searches cost:

``` text
O(log B)
```

Once the target block is found, at most `B` values are scanned.

Therefore:

``` text
O((N / B) * log B + B)
```

With `B ≈ sqrt(N)`:

``` text
O(sqrt(N) * log N)
```

approximately.

For `N = 100000` and `B = 320`, there are only about `313` value blocks.

------------------------------------------------------------------------

## Space Complexity

The main structures are:

-   `A`: `O(N)`
-   `pos`: `O(N)`
-   All block position vectors combined: exactly `N` positions.

Therefore:

``` text
O(N)
```

space.

This is substantially more memory-efficient than storing every value in
multiple tree nodes.

------------------------------------------------------------------------

## Trade-offs

### Advantages

-   **Low memory usage:** `O(N)` instead of an `O(N log N)` structure.
-   **Simple permutation invariant:** `pos[value]` makes presence
    testing very cheap.
-   **Fast range counting:** sorted block positions allow binary-search
    counting.
-   **Efficient swaps:** only the blocks containing the two swapped
    values may change.
-   **Same-block swaps are especially cheap:** no block-vector
    modification is required.
-   Avoids the large memory overhead of GNU PBDS trees.

### Disadvantages

-   Query complexity is approximately `O(sqrt(N) log N)`, rather than
    the theoretical `O(log^2 N)` achievable with more sophisticated
    structures.
-   Updating a block can take `O(B)` because changing one position may
    require shifting it across the sorted vector.
-   Performance depends on the chosen block size. `320` works well for
    `N <= 10^5`, but the optimal constant can vary by judge and
    workload.
-   This solution relies heavily on the fact that the array is a
    **permutation**. If duplicate values were allowed, the simple
    `pos[value]` representation would no longer be sufficient.

------------------------------------------------------------------------

## Why Not Segment Tree + PBDS?

A natural alternative is a segment tree over the value domain where each
node stores an ordered set of positions.

That gives approximately:

``` text
O(log^2 N)
```

for both updates and queries.

However, each value appears in `O(log N)` segment-tree nodes. With
`N = 10^5`, this results in roughly millions of PBDS nodes, plus
hundreds of thousands of tree objects.

PBDS nodes have significant per-node memory overhead, so this approach
can exceed strict memory limits or produce runtime failures such as
`SIGSEGV`.

The square-root decomposition solution trades some query speed for much
lower memory consumption:

``` text
Segment Tree + PBDS:
Time  : O(log^2 N)
Space : O(N log N), with high constants

Square Root Decomposition:
Query : O(sqrt(N) log N)
Update: O(sqrt(N)) worst case
Space : O(N)
```

For the given constraints and judge environment, the square-root
decomposition approach is a practical and robust choice.
