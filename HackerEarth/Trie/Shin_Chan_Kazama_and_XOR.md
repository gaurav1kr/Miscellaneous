# Shin-Chan Kazama and XOR

## Problem Statement

Given an array `A[1..N]`, answer `Q` queries.

Each query contains:

``` text
l r X
```

For every query, find a value `Z` occurring in the subarray:

``` text
A[l], A[l+1], ..., A[r]
```

such that:

``` text
Z XOR X
```

is minimum among all values in that range.

Also output the number of times the selected value `Z` occurs in
`[l, r]`.

### Input Format

-   First line: integer `N`
-   Second line: `N` integers representing array `A`
-   Third line: integer `Q`
-   Next `Q` lines: three integers `l`, `r`, and `X`

### Output Format

For each query, print:

``` text
Z frequency
```

where:

-   `Z` minimizes `Z XOR X` in `A[l..r]`
-   `frequency` is the number of occurrences of `Z` in `A[l..r]`

### Constraints

-   `1 <= N <= 10^6`
-   `1 <= A[i], X <= 10^9`
-   `1 <= l <= r <= N`
-   `1 <= Q <= 50000`

### Sample Input

``` text
7
1 3 2 3 4 5 5
5
1 1 1
1 2 2
1 4 3
1 5 4
1 7 5
```

### Sample Output

``` text
1 1
3 1
3 2
4 1
5 2
```

------------------------------------------------------------------------

# Key Observation

To minimize:

``` text
Z XOR X
```

we want the bits of `Z` to match the bits of `X` as much as possible,
starting from the most significant bit.

At a particular bit:

``` text
X bit = 0  -> prefer Z bit = 0
X bit = 1  -> prefer Z bit = 1
```

because:

``` text
0 XOR 0 = 0
1 XOR 1 = 0
```

If the preferred bit does not occur among the candidate values, we are
forced to choose the opposite bit.

This greedy choice is correct because a difference at a more significant
bit dominates all less-significant bits.

The challenge is efficiently determining whether the preferred bit
exists **inside an arbitrary subarray `[l,r]`**.

------------------------------------------------------------------------

# Why a Persistent Binary Trie Can Exceed Memory

A natural solution is a persistent binary trie, with one version for
every array prefix.

For `A[i] <= 10^9`, approximately 30 bits are needed.

With:

``` text
N = 10^6
```

a persistent trie can create roughly:

``` text
30 * 10^6
```

nodes.

If each node stores multiple 32-bit integers, memory can exceed the
`256 MB` limit.

Similarly, storing a `vector<int>` of positions at every static trie
node introduces substantial per-vector overhead.

Therefore we need a more memory-efficient range data structure.

------------------------------------------------------------------------

# Approach: Wavelet Matrix

A **Wavelet Matrix** is well suited for this problem.

It organizes the array level by level according to the bits of its
values.

Since:

``` text
A[i], X <= 10^9
```

we need 30 bit levels:

``` text
bit 29, bit 28, ..., bit 0
```

At each level:

1.  Record whether each current value has bit `0` or `1`.
2.  Stable-partition the values:
    -   all zero-bit values first
    -   all one-bit values second
3.  Store how many zeros exist at that level.

A query range can then be mapped from one level to the next while
greedily selecting the bit that minimizes XOR.

------------------------------------------------------------------------

# Packed BitVector

Storing one integer per element per level would still consume too much
memory.

Instead, each level stores its bits packed into:

``` cpp
uint64_t
```

One `uint64_t` stores 64 elements.

For each packed bitvector we also store prefix popcounts over the 64-bit
blocks.

This supports:

``` cpp
rank1(pos)
```

which returns the number of `1` bits in:

``` text
[0, pos)
```

Then:

``` cpp
rank0(pos) = pos - rank1(pos)
```

Using rank operations, we can determine how many zeros and ones occur
inside any current range `[l,r)`.

------------------------------------------------------------------------

# Query Algorithm

The input query uses a 1-based inclusive range:

``` text
[l, r]
```

Convert it to a zero-based half-open range:

``` cpp
--l;
```

so the Wavelet Matrix operates on:

``` text
[l, r)
```

At every level, calculate:

``` cpp
onesL  = rank1(l);
onesR  = rank1(r);

zerosL = l - onesL;
zerosR = r - onesR;
```

Therefore:

``` cpp
countZero = zerosR - zerosL;
countOne  = onesR - onesL;
```

------------------------------------------------------------------------

## Case 1: Current Bit of X is 0

Prefer a `0` bit for `Z`.

If:

``` text
countZero > 0
```

choose zero and map the interval into the zero partition:

``` cpp
l = zerosL;
r = zerosR;
```

Otherwise choose one:

``` cpp
l = zeroCount[level] + onesL;
r = zeroCount[level] + onesR;
```

------------------------------------------------------------------------

## Case 2: Current Bit of X is 1

Prefer a `1` bit for `Z`.

If:

``` text
countOne > 0
```

choose one:

``` cpp
l = zeroCount[level] + onesL;
r = zeroCount[level] + onesR;
```

Otherwise choose zero:

``` cpp
l = zerosL;
r = zerosR;
```

------------------------------------------------------------------------

# Getting the Frequency

After processing all 30 bits, all elements remaining in the Wavelet
Matrix interval `[l,r)` are equal to the selected value `Z`.

Therefore:

``` cpp
frequency = r - l;
```

No additional frequency map or position list is required.

This is one of the main advantages of the Wavelet Matrix solution.

------------------------------------------------------------------------

# Correctness

At each bit from most significant to least significant, the algorithm
tries to choose the same bit as `X`.

If such a value exists in the current candidate range, choosing the same
bit makes the current XOR bit equal to `0`.

Choosing the opposite bit would make that XOR bit equal to `1`,
producing a larger XOR value regardless of all remaining lower bits.

Therefore the greedy choice is optimal.

If the preferred bit is unavailable, every candidate has the opposite
bit, so choosing it is mandatory.

After processing all bits, the selected sequence of bits uniquely
defines the minimum-XOR value `Z`.

The Wavelet Matrix range transformation preserves exactly those original
range elements consistent with all chosen bits. Hence the final interval
contains precisely the occurrences of `Z` in the original query range.

Thus:

``` cpp
r - l
```

is exactly the required frequency.

------------------------------------------------------------------------

# C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

class BitVector {
private:
    int n;

    // Packed bits: 64 elements per uint64_t.
    vector<uint64_t> bits;

    /*
        prefix[i] = number of 1s in complete
        64-bit blocks [0, i).
    */
    vector<int> prefix;

public:
    BitVector() : n(0) {}

    explicit BitVector(int size) {
        init(size);
    }

    void init(int size) {
        n = size;

        int blocks = (n + 63) >> 6;

        bits.assign(blocks, 0);
        prefix.assign(blocks + 1, 0);
    }

    void setBit(int pos) {
        bits[pos >> 6] |=
            (1ULL << (pos & 63));
    }

    void build() {
        int blocks = (int)bits.size();

        for (int i = 0; i < blocks; ++i) {
            prefix[i + 1] =
                prefix[i] +
                __builtin_popcountll(bits[i]);
        }
    }

    // Number of 1 bits in [0, pos).
    inline int rank1(int pos) const {

        int block = pos >> 6;
        int offset = pos & 63;

        int result = prefix[block];

        if (offset != 0 &&
            block < (int)bits.size()) {

            uint64_t mask =
                (1ULL << offset) - 1;

            result +=
                __builtin_popcountll(
                    bits[block] & mask
                );
        }

        return result;
    }

    // Number of 0 bits in [0, pos).
    inline int rank0(int pos) const {
        return pos - rank1(pos);
    }
};


class WaveletMatrix {
private:
    static const int MAX_BIT = 29;
    static const int LEVELS = 30;

    int n;

    BitVector bv[LEVELS];

    /*
        Number of zero-bit elements at each level.
        Ones begin from position zeroCount[level].
    */
    int zeroCount[LEVELS];

public:
    WaveletMatrix(const vector<int>& input) {

        n = (int)input.size();

        vector<int> cur = input;
        vector<int> next(n);

        for (int level = 0;
             level < LEVELS;
             ++level) {

            int bit =
                MAX_BIT - level;

            bv[level].init(n);

            int zeros = 0;

            for (int i = 0; i < n; ++i) {

                if ((cur[i] >> bit) & 1) {
                    bv[level].setBit(i);
                } else {
                    ++zeros;
                }
            }

            zeroCount[level] = zeros;

            bv[level].build();

            /*
                Stable partition:
                zeros first, ones second.
            */
            int zeroPos = 0;
            int onePos = zeros;

            for (int i = 0; i < n; ++i) {

                if ((cur[i] >> bit) & 1) {
                    next[onePos++] = cur[i];
                } else {
                    next[zeroPos++] = cur[i];
                }
            }

            cur.swap(next);
        }
    }

    /*
        Query range is [l, r), zero-indexed.

        Returns:
            {Z, frequency}

        where Z minimizes Z XOR X.
    */
    pair<int, int> minXor(
        int l,
        int r,
        int X
    ) const {

        int Z = 0;

        for (int level = 0;
             level < LEVELS;
             ++level) {

            int bit =
                MAX_BIT - level;

            int xb =
                (X >> bit) & 1;

            int onesL =
                bv[level].rank1(l);

            int onesR =
                bv[level].rank1(r);

            int zerosL =
                l - onesL;

            int zerosR =
                r - onesR;

            int countZero =
                zerosR - zerosL;

            int countOne =
                onesR - onesL;

            int chosenBit;

            if (xb == 0) {

                if (countZero > 0) {

                    chosenBit = 0;

                    l = zerosL;
                    r = zerosR;

                } else {

                    chosenBit = 1;

                    l =
                        zeroCount[level] +
                        onesL;

                    r =
                        zeroCount[level] +
                        onesR;
                }

            } else {

                if (countOne > 0) {

                    chosenBit = 1;

                    l =
                        zeroCount[level] +
                        onesL;

                    r =
                        zeroCount[level] +
                        onesR;

                } else {

                    chosenBit = 0;

                    l = zerosL;
                    r = zerosR;
                }
            }

            if (chosenBit) {
                Z |= (1 << bit);
            }
        }

        /*
            After all levels, every value in [l,r)
            is exactly Z.
        */
        int frequency = r - l;

        return {Z, frequency};
    }
};


int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> A(N);

    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    WaveletMatrix wm(A);

    int Q;
    cin >> Q;

    while (Q--) {

        int l, r, X;

        cin >> l >> r >> X;

        /*
            Input: 1-based inclusive [l,r]
            Wavelet Matrix: 0-based half-open [l-1,r)
        */
        --l;

        auto [Z, frequency] =
            wm.minXor(l, r, X);

        cout << Z
             << ' '
             << frequency
             << '\n';
    }

    return 0;
}
```

------------------------------------------------------------------------

# Time Complexity

Let:

``` text
B = 30
```

because values are at most `10^9`.

## Construction

At every one of the 30 levels, all `N` elements are scanned and
stable-partitioned.

Therefore:

\[ `\boxed{O(NB)}`{=tex} \]

Since `B = 30`:

\[ `\boxed{O(30N)}`{=tex} \]

which is effectively linear in `N`.

## Query

Each query visits exactly 30 Wavelet Matrix levels.

Every level performs a constant number of rank operations.

Therefore:

\[ `\boxed{O(B)}`{=tex} \]

or:

\[ `\boxed{O(30)}`{=tex} \]

per query.

For `Q` queries:

\[ `\boxed{O(30Q)}`{=tex} \]

## Overall

\[ `\boxed{O(30N + 30Q)}`{=tex} \]

or more generally:

\[ `\boxed{O((N+Q)\log V)}`{=tex} \]

where `V` is the maximum value.

------------------------------------------------------------------------

# Space Complexity

Each of the 30 levels stores `N` bits.

Raw bit storage is:

\[ 30N `\text{ bits}`{=tex} \]

For:

``` text
N = 10^6
```

this is approximately:

``` text
30,000,000 bits
≈ 3.75 MB
```

Each level also stores prefix popcounts for groups of 64 bits.

There are approximately:

``` text
N / 64
```

prefix entries per level.

These consume only a few additional megabytes.

During construction, two arrays of `N` integers are used for stable
partitioning:

``` cpp
cur
next
```

which require roughly:

``` text
8 MB
```

for `N = 10^6`.

Therefore the Wavelet Matrix stays comfortably below the `256 MB` memory
limit.

------------------------------------------------------------------------

# Trade-offs

## Advantages

-   Very memory efficient compared with a persistent trie.
-   Query time is only 30 levels.
-   No dynamic allocation of millions of trie nodes.
-   No per-node `vector` overhead.
-   Directly supports arbitrary subarray queries.
-   Frequency of the selected value is obtained for free from the final
    interval size.
-   Construction and query complexities are deterministic.
-   Particularly suitable for large `N` and static arrays.

## Disadvantages

-   More complex to understand and implement than a standard binary
    trie.
-   Primarily suited to static arrays; supporting arbitrary array
    updates would require a different or more sophisticated structure.
-   Correct interval mapping between Wavelet Matrix levels must be
    implemented carefully.
-   Rank operations and bit packing require careful indexing.

------------------------------------------------------------------------

# Comparison with Other Approaches

## Persistent Binary Trie

A persistent trie provides excellent query time:

``` text
O(log V)
```

but can require approximately:

``` text
N * log V
```

nodes.

For `N = 10^6` and 30 bits, this can approach 30 million nodes and
exceed a `256 MB` memory limit.

## Static Trie with Position Vectors

A static trie can store occurrence positions at each node and use binary
search for range existence.

However, storing a `vector<int>` at millions of nodes creates
substantial object and allocation overhead.

## Wavelet Matrix

The Wavelet Matrix retains the same bit-by-bit greedy logic while
representing each level compactly using packed bits.

It therefore provides:

``` text
Query: O(log V)
Memory: O(N log V) bits + compact rank metadata
```

rather than `O(N log V)` full trie nodes.

------------------------------------------------------------------------

# Summary

The key greedy rule is:

``` text
At each bit:
    prefer Z_bit = X_bit
```

because this makes the corresponding XOR bit zero.

The Wavelet Matrix efficiently determines whether the preferred bit
exists inside the current subarray and maps the range into the chosen
partition.

After all 30 bits:

``` cpp
frequency = r - l;
```

because the final interval contains exactly the occurrences of the
optimal value `Z`.

This gives an efficient solution for the full constraints while staying
comfortably within the memory limit.
