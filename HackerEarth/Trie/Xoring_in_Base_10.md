# Xoring in Base 10

## Problem Statement

Given two numbers

\[ A = (A_nA\_{n-1}`\ldots `{=tex}A_1) \]

and

\[ B = (B_nB\_{n-1}`\ldots `{=tex}B_1) \]

in base 10, define their **XOR in base 10** as:

\[ A `\oplus `{=tex}B = (X_nX\_{n-1}`\ldots `{=tex}X_1) \]

where:

\[ X_i = (A_i + B_i) `\bmod 10`{=tex} \]

In other words, corresponding decimal digits are added independently
modulo `10`, with **no carry** between positions.

Given an array `S` containing `n` integers, find the **maximum number
obtainable by XORing exactly `k` integers**.

### Input Format

-   The first line contains two integers `n` and `k`:
    -   `n` = number of elements in the sequence.
    -   `k` = exact number of elements that must be selected.
-   The second line contains `n` integers.

### Output Format

Output a single integer representing the maximum possible base-10 XOR
value.

### Constraints

-   `1 <= n <= 40`
-   `1 <= k <= n`
-   `0 <= S[i] <= 10^9`

### Example

``` text
Input:
3 2
4 1 5

Output:
9
```

### Explanation

Selecting `4` and `5` gives:

``` text
(4 + 5) % 10 = 9
```

Therefore, the maximum possible answer is `9`.

------------------------------------------------------------------------

## Approach

Since `n <= 40`, enumerating all subsets directly would require up to:

\[ 2\^{40} \]

subsets, which is too large.

We use **Meet-in-the-Middle (MITM)**.

### 1. Split the Array

Divide the input into two halves:

-   Left half: at most 20 elements
-   Right half: at most 20 elements

Each half therefore has at most:

\[ 2\^{20} `\approx 10`{=tex}\^6 \]

subsets, which is manageable.

------------------------------------------------------------------------

## 2. Generate All Subsets

For every subset of each half, calculate:

-   Number of selected elements.
-   Base-10 XOR value of those elements.

Instead of recomputing a subset from scratch, use:

``` cpp
prev = mask & (mask - 1);
bit  = __builtin_ctz(mask);
```

`prev` removes the least-significant set bit from `mask`.

Therefore:

``` text
xor[mask] = xor[prev] XOR element[bit]
```

and:

``` text
count[mask] = count[prev] + 1
```

This efficiently generates all subset states.

------------------------------------------------------------------------

## 3. Group Right-Half Subsets by Count

Suppose a subset from the left half contains `c` elements.

Since exactly `k` elements must be selected, the right half must
contribute:

``` text
k - c
```

elements.

We therefore create a separate **decimal trie** for every possible
subset size.

For example:

``` text
trie[0] -> XOR values using exactly 0 right elements
trie[1] -> XOR values using exactly 1 right element
trie[2] -> XOR values using exactly 2 right elements
...
```

This ensures that only combinations containing exactly `k` elements are
considered.

------------------------------------------------------------------------

## 4. Decimal Trie

A normal XOR problem uses a binary trie because XOR operates on bits.

Here the operation works independently on **decimal digits**, so each
trie node has 10 possible children:

``` text
0, 1, 2, ..., 9
```

Numbers are inserted from the **most significant decimal digit to the
least significant digit**.

Because:

``` text
S[i] <= 10^9
```

we can safely process 10 decimal positions, including leading zeroes.

------------------------------------------------------------------------

## 5. Greedily Find the Maximum Result

Suppose the current digit from the left subset XOR is `a`, and the
corresponding digit from a right subset is `b`.

The resulting digit is:

\[ r = (a + b) `\bmod 10`{=tex} \]

To maximize the final number, we want the most significant digit to be
as large as possible.

At each trie level, try:

``` text
r = 9, 8, 7, ..., 0
```

For a desired result digit `r`, the required right-side digit is:

\[ b = (r-a+10)`\bmod 10`{=tex} \]

If that child exists in the trie, choose it immediately.

This greedy decision is correct because a larger digit at a more
significant position always dominates every possible choice of the
remaining less-significant digits.

------------------------------------------------------------------------

## C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;

static const int DIGITS = 10;

/*
    Digit-wise XOR in base 10:
    result_digit = (a_digit + b_digit) % 10
*/
ull xorBase10(ull a, ull b) {
    ull result = 0;
    ull place = 1;

    for (int i = 0; i < DIGITS; ++i) {
        int da = a % 10;
        int db = b % 10;

        int d = (da + db) % 10;

        result += (ull)d * place;

        a /= 10;
        b /= 10;
        place *= 10;
    }

    return result;
}

class DecimalTrie {
private:
    struct Node {
        int child[10];

        Node() {
            fill(child, child + 10, -1);
        }
    };

    vector<Node> trie;

public:
    DecimalTrie() {
        trie.emplace_back();
    }

    void reserve(size_t n) {
        trie.reserve(n);
    }

    void insert(ull x) {
        int digits[DIGITS];

        for (int i = DIGITS - 1; i >= 0; --i) {
            digits[i] = x % 10;
            x /= 10;
        }

        int node = 0;

        for (int i = 0; i < DIGITS; ++i) {
            int d = digits[i];

            if (trie[node].child[d] == -1) {
                trie[node].child[d] = (int)trie.size();
                trie.emplace_back();
            }

            node = trie[node].child[d];
        }
    }

    ull getMaximum(ull x) const {
        int digits[DIGITS];

        for (int i = DIGITS - 1; i >= 0; --i) {
            digits[i] = x % 10;
            x /= 10;
        }

        int node = 0;
        ull answer = 0;

        for (int i = 0; i < DIGITS; ++i) {
            int a = digits[i];

            for (int resultDigit = 9; resultDigit >= 0; --resultDigit) {

                int b = (resultDigit - a + 10) % 10;

                if (trie[node].child[b] != -1) {
                    answer = answer * 10 + resultDigit;
                    node = trie[node].child[b];
                    break;
                }
            }
        }

        return answer;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<ull> S(n);

    for (auto &x : S)
        cin >> x;

    int n1 = n / 2;
    int n2 = n - n1;

    vector<ull> left(S.begin(), S.begin() + n1);
    vector<ull> right(S.begin() + n1, S.end());

    int leftSize = 1 << n1;
    int rightSize = 1 << n2;

    vector<ull> leftXor(leftSize, 0);
    vector<unsigned char> leftCount(leftSize, 0);

    vector<ull> rightXor(rightSize, 0);
    vector<unsigned char> rightCount(rightSize, 0);

    // Generate all left-half subsets.
    for (int mask = 1; mask < leftSize; ++mask) {
        int bit = __builtin_ctz(mask);
        int prev = mask & (mask - 1);

        leftXor[mask] = xorBase10(leftXor[prev], left[bit]);
        leftCount[mask] = leftCount[prev] + 1;
    }

    // Generate all right-half subsets.
    for (int mask = 1; mask < rightSize; ++mask) {
        int bit = __builtin_ctz(mask);
        int prev = mask & (mask - 1);

        rightXor[mask] = xorBase10(rightXor[prev], right[bit]);
        rightCount[mask] = rightCount[prev] + 1;
    }

    /*
        trie[c] stores right-half XOR values obtained
        by selecting exactly c elements.
    */
    vector<unique_ptr<DecimalTrie>> tries(n2 + 1);

    for (int c = 0; c <= n2; ++c)
        tries[c] = make_unique<DecimalTrie>();

    for (int mask = 0; mask < rightSize; ++mask) {
        int cnt = rightCount[mask];

        if (cnt <= k)
            tries[cnt]->insert(rightXor[mask]);
    }

    ull answer = 0;

    for (int mask = 0; mask < leftSize; ++mask) {

        int leftSelected = leftCount[mask];
        int rightNeeded = k - leftSelected;

        if (rightNeeded < 0 || rightNeeded > n2)
            continue;

        ull best = tries[rightNeeded]->getMaximum(leftXor[mask]);

        answer = max(answer, best);
    }

    cout << answer << '\n';

    return 0;
}
```

------------------------------------------------------------------------

## Correctness

For every left-half subset containing `c` elements, the algorithm
queries only the trie containing right-half subsets with exactly `k-c`
elements.

Therefore every considered pair contains exactly:

\[ c + (k-c) = k \]

elements.

For a fixed left XOR value, the decimal trie examines the result from
the most significant digit toward the least significant digit.

At each position it selects the largest achievable result digit. Since a
larger digit at the first differing decimal position produces a larger
overall integer regardless of subsequent digits, this greedy trie
traversal returns the maximum possible result for that left subset.

Since every valid left-half subset is queried, every possible selection
of exactly `k` original elements is represented by one left/right subset
pair.

Hence, taking the maximum over all queries produces the required answer.

------------------------------------------------------------------------

## Time Complexity

Let:

``` text
L = floor(n / 2)
R = n - L
D = number of decimal digits = 10
```

There are:

\[ 2\^L \]

left subsets and:

\[ 2\^R \]

right subsets.

Generating the subset XOR values requires:

\[ O(D(2\^L + 2\^R)) \]

Building the tries requires:

\[ O(D `\cdot 2`{=tex}\^R) \]

For every left subset, a trie query processes `D` positions and may
inspect at most 10 possible result digits at each position. Since both
are constants, each query is effectively `O(D)`.

Overall:

\[ `\boxed{O(D(2^{n/2}))}`{=tex} \]

More precisely:

\[ `\boxed{O(D(2^L + 2^R))}`{=tex} \]

Since `D = 10`, this is commonly written as:

\[ `\boxed{O(2^{n/2})}`{=tex} \]

for this problem.

------------------------------------------------------------------------

## Space Complexity

The subset arrays require:

\[ O(2\^L + 2\^R) \]

space.

In the worst case, each right-half XOR value can add up to `D` trie
nodes:

\[ O(D `\cdot 2`{=tex}\^R) \]

Therefore the total space complexity is:

\[ `\boxed{O(D \cdot 2^{n/2})}`{=tex} \]

Since `D = 10` is constant:

\[ `\boxed{O(2^{n/2})}`{=tex} \]

------------------------------------------------------------------------

## Trade-offs

### Advantages

-   Reduces an infeasible `2^40` subset search to approximately two
    `2^20` searches.
-   Correctly enforces the requirement of selecting **exactly `k`
    elements**.
-   Decimal trie allows efficient maximization of the unusual digit-wise
    modulo-10 XOR operation.
-   Greedy trie lookup avoids comparing every left subset against every
    right subset.

### Disadvantages

-   Uses considerably more memory than simple subset enumeration because
    trie nodes contain 10 child pointers.
-   Implementation is more complex than standard Meet-in-the-Middle.
-   The technique relies on the operation being independent across
    decimal positions.
-   A naive trie representation can consume significant memory in the
    worst case.

### Why Not Brute Force?

Checking all subsets of `n = 40` elements would require approximately:

\[ 2\^{40} `\approx 1.1`{=tex} `\times 10`{=tex}\^{12} \]

subsets, which is infeasible.

Meet-in-the-Middle reduces this to roughly:

\[ 2 `\times 2`{=tex}\^{20} `\approx 2.1`{=tex} `\times 10`{=tex}\^6 \]

subset states, making the problem practical.
