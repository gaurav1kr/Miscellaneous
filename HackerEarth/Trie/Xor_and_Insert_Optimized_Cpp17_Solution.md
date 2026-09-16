# Xor and Insert --- Optimized C++17 Solution

## Problem Statement

Initially, you have a set:

``` text
S = {0}
```

There are three types of queries:

### Type 1 --- Insert

``` text
1 x
```

Add `x` to the set.

### Type 2 --- XOR All Elements

``` text
2 x
```

For every element `y` in the set, replace it with:

``` text
y = y XOR x
```

### Type 3 --- Find Minimum

``` text
3
```

Print the minimum element currently present in the set.

### Constraints

``` text
q <= 500000
x <= 10^9
```

The challenge is that a type-2 query affects **every element**. Updating
every element directly would be too slow.

------------------------------------------------------------------------

## Key Observation

Suppose we maintain a global value:

``` text
lazyXor
```

Instead of physically applying every XOR operation to every element, we
represent each logical value as:

``` text
logicalValue = storedValue XOR lazyXor
```

This allows a type-2 operation:

``` text
2 x
```

to be processed simply as:

``` cpp
lazyXor ^= x;
```

No element in the data structure needs to be changed.

The remaining questions are:

1.  How should a newly inserted value be stored?
2.  How can we efficiently find the minimum logical value?

A **Binary Trie** solves both.

------------------------------------------------------------------------

## Binary Trie

Since:

``` text
x <= 10^9
```

31 bits (`30 ... 0`) are sufficient.

Each trie node has two children:

``` text
child[0]
child[1]
```

corresponding to the next binary bit of a stored number.

------------------------------------------------------------------------

## Handling Type 1 --- Insert

Suppose the current global XOR is `L`.

The trie represents logical values as:

``` text
stored XOR L
```

If we want to insert a new logical value `x`, we need a stored value
such that:

``` text
stored XOR L = x
```

Therefore:

``` text
stored = x XOR L
```

So insertion becomes:

``` cpp
trie.insert(x ^ lazyXor);
```

This is an important detail. Inserting `x` directly would be incorrect
if previous type-2 operations have changed `lazyXor`.

------------------------------------------------------------------------

## Handling Type 2 --- XOR Every Element

Suppose the current logical value is:

``` text
stored XOR lazyXor
```

After XORing every element by `x`:

``` text
(stored XOR lazyXor) XOR x
```

Using associativity:

``` text
stored XOR (lazyXor XOR x)
```

Therefore, simply update:

``` cpp
lazyXor ^= x;
```

The trie itself remains unchanged.

This makes type-2 queries extremely efficient.

------------------------------------------------------------------------

## Handling Type 3 --- Find Minimum

We need to minimize:

``` text
storedValue XOR lazyXor
```

Consider one bit at a time, starting from the most significant bit.

If the current bit of `lazyXor` is `b`, we would prefer the stored value
to also have bit `b`.

Why?

``` text
b XOR b = 0
```

A `0` at a more significant bit always gives a smaller number than a
`1`, regardless of lower bits.

Therefore, while traversing the trie:

``` text
preferred stored bit = current lazyXor bit
```

If that child exists, choose it.

Otherwise, choose the opposite child and set that bit in the result to
`1`.

This greedy traversal produces the minimum possible value.

------------------------------------------------------------------------

## Example

Suppose the trie stores:

``` text
stored values = {2, 5, 7}
```

and:

``` text
lazyXor = 4
```

The actual logical values are:

``` text
2 XOR 4 = 6
5 XOR 4 = 1
7 XOR 4 = 3
```

Therefore the minimum is:

``` text
1
```

The trie finds this without explicitly transforming all stored values.

------------------------------------------------------------------------

## C++17 Implementation

``` cpp
#include <bits/stdc++.h>
using namespace std;

class BinaryTrie {
private:
    struct Node {
        int child[2];

        Node() {
            child[0] = child[1] = -1;
        }
    };

    vector<Node> trie;

public:
    BinaryTrie() {
        trie.reserve(16000000);
        trie.emplace_back();      // root
    }

    void insert(int x) {
        int node = 0;

        for (int bit = 30; bit >= 0; --bit) {
            int b = (x >> bit) & 1;

            if (trie[node].child[b] == -1) {
                trie[node].child[b] = (int)trie.size();
                trie.emplace_back();
            }

            node = trie[node].child[b];
        }
    }

    // Find minimum of:
    // storedValue XOR lazyXor
    int getMinimum(int lazyXor) const {
        int node = 0;
        int result = 0;

        for (int bit = 30; bit >= 0; --bit) {
            int lazyBit = (lazyXor >> bit) & 1;

            /*
                To minimize the resulting bit:

                    storedBit XOR lazyBit = 0

                Therefore prefer:

                    storedBit = lazyBit
            */
            int preferred = lazyBit;

            if (trie[node].child[preferred] != -1) {
                node = trie[node].child[preferred];
            }
            else {
                int other = preferred ^ 1;

                node = trie[node].child[other];

                // Forced result bit = 1
                result |= (1 << bit);
            }
        }

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    cin >> Q;

    BinaryTrie trie;

    // Initially S = {0}
    trie.insert(0);

    int lazyXor = 0;

    while (Q--) {
        int type;
        cin >> type;

        if (type == 1) {
            int x;
            cin >> x;

            /*
                logical value = stored XOR lazyXor

                Therefore, to insert logical x:

                    stored = x XOR lazyXor
            */
            trie.insert(x ^ lazyXor);
        }
        else if (type == 2) {
            int x;
            cin >> x;

            /*
                XOR all logical values with x.

                No trie modification is required.
            */
            lazyXor ^= x;
        }
        else {
            cout << trie.getMinimum(lazyXor) << '\n';
        }
    }

    return 0;
}
```

------------------------------------------------------------------------

## Correctness

We maintain the invariant:

``` text
logical value = stored value XOR lazyXor
```

### Insert Correctness

To insert logical value `x`, we store:

``` text
x XOR lazyXor
```

Its logical value is:

``` text
(x XOR lazyXor) XOR lazyXor
= x
```

because:

``` text
a XOR a = 0
x XOR 0 = x
```

Therefore insertion is correct.

### Global XOR Correctness

Before a type-2 query, an element is:

``` text
stored XOR lazyXor
```

After XORing it with `x`:

``` text
stored XOR lazyXor XOR x
```

which is equivalent to:

``` text
stored XOR (lazyXor XOR x)
```

Thus updating:

``` cpp
lazyXor ^= x;
```

correctly represents the transformation of every element without
modifying the trie.

### Minimum Query Correctness

The minimum query minimizes:

``` text
stored XOR lazyXor
```

Binary numbers are ordered by their most significant differing bit.

At every bit, we therefore prefer a resulting bit of `0`.

For:

``` text
storedBit XOR lazyBit = 0
```

we need:

``` text
storedBit = lazyBit
```

If such a trie child exists, taking it is always optimal. If it does not
exist, the resulting bit must be `1`, so we take the opposite child.

Applying this greedy choice from the most significant bit to the least
significant bit yields the smallest possible logical value.

------------------------------------------------------------------------

## Time Complexity

There are 31 relevant bits.

### Type 1 --- Insert

A value traverses 31 trie levels:

``` text
O(31) = O(log MAX_VALUE)
```

Effectively constant time.

### Type 2 --- XOR All Elements

Only one variable is updated:

``` text
lazyXor ^= x
```

Therefore:

``` text
O(1)
```

### Type 3 --- Minimum

The trie is traversed over 31 levels:

``` text
O(31) = O(log MAX_VALUE)
```

Effectively constant time.

### Overall

For `Q` queries:

``` text
O(Q * 31)
```

which is effectively:

``` text
O(Q)
```

for the fixed integer range.

------------------------------------------------------------------------

## Space Complexity

Every inserted value can create at most 31 new trie nodes.

For `M` insertions:

``` text
O(31 * M)
```

or more generally:

``` text
O(M log MAX_VALUE)
```

Since `Q <= 500000`, the worst-case number of nodes is approximately:

``` text
31 * 500000
```

although trie prefixes are shared, so the actual number can be lower.

------------------------------------------------------------------------

## Trade-offs

### Advantages

-   Type-2 XOR operations are `O(1)`.
-   Insertions are only 31 trie steps.
-   Minimum queries are only 31 trie steps.
-   No need to modify every element after a global XOR.
-   Works efficiently for up to hundreds of thousands of queries.
-   The approach directly exploits the bitwise nature of XOR.

### Disadvantages

-   A binary trie can consume significantly more memory than storing the
    integers directly.
-   Each trie node stores two child indices even when only one child is
    used.
-   The implementation assumes a fixed maximum bit width.
-   If the allowed values become larger (for example 64-bit integers),
    the trie depth must be increased.
-   This implementation does not delete elements. Supporting deletion
    would require node counts or frequencies.

------------------------------------------------------------------------

## Why a Normal Set Is Not Enough

A normal ordered set can easily handle:

``` text
insert(x)
minimum()
```

but a type-2 query requires:

``` text
for every y:
    y = y XOR x
```

XOR does not preserve numeric ordering.

For example:

``` text
1 < 2
```

but after XOR with `3`:

``` text
1 XOR 3 = 2
2 XOR 3 = 1
```

The order reverses.

Therefore, simply maintaining an ordered `std::set` does not allow a
global XOR to be lazily applied while preserving the ordering needed for
the minimum.

The binary trie works because it operates directly on the bits and can
incorporate `lazyXor` during traversal.

------------------------------------------------------------------------

## Summary

The solution combines two ideas:

``` text
1. Lazy global XOR
2. Binary Trie
```

Maintain:

``` text
logicalValue = storedValue XOR lazyXor
```

Then:

``` text
Insert x:
    insert(x XOR lazyXor)

XOR all by x:
    lazyXor ^= x

Find minimum:
    greedily traverse the trie using lazyXor bits
```

Complexities:

``` text
Type 1: O(31)
Type 2: O(1)
Type 3: O(31)

Space: O(number of insertions * 31)
```

This avoids ever iterating over the complete set for a global XOR
operation.
