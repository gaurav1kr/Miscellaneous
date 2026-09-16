# Ma5termind and XOR Minimization

## Problem Statement

Given a sequence of `N` positive integers, consider all **non-empty
subsequences** of the sequence.

For each subsequence:

1.  Compute the sum of its selected elements.
2.  For each query value `A`, calculate:

``` text
subsequence_sum XOR A
```

For every query, find the achievable subsequence sum that gives the
**minimum XOR value with `A`**.

For that optimal sum, output:

1.  The subsequence sum.
2.  The number of non-empty subsequences producing that sum, modulo
    `10^9 + 7`.

### Input Format

-   First line: integer `N`.
-   Second line: `N` space-separated integers.
-   Third line: integer `Q`, the number of queries.
-   Next `Q` lines: one integer `A` per query.

### Output Format

For every query, print:

``` text
best_sum number_of_subsequences
```

where `best_sum` minimizes:

``` text
best_sum XOR A
```

among all sums obtainable from non-empty subsequences.

### Constraints

-   `1 <= N <= 100`
-   `1 <= sequence[i] <= 1000`
-   `Q <= 5 * 10^5`
-   `1 <= A <= 10^9`

Since:

``` text
N <= 100
sequence[i] <= 1000
```

the maximum possible subsequence sum is:

``` text
100000
```

------------------------------------------------------------------------

## Sample

``` text
Input:
3
1 2 3
3
3
5
7
```

The non-empty subsequence sums are:

``` text
1 -> 1 way
2 -> 1 way
3 -> 2 ways
4 -> 1 way
5 -> 1 way
6 -> 1 way
```

For `A = 3`:

``` text
3 XOR 3 = 0
```

which is optimal, and sum `3` can be formed in two ways:

``` text
{3}
{1, 2}
```

For `A = 5`, sum `5` is optimal.

For `A = 7`, sum `6` gives:

``` text
6 XOR 7 = 1
```

which is the minimum possible value among achievable sums.

Therefore:

``` text
Output:
3 2
5 1
6 1
```

------------------------------------------------------------------------

# Approach

The solution has two main parts:

1.  **0/1 Subset-Sum DP** to determine every achievable non-empty
    subsequence sum and count how many subsequences produce it.
2.  **Binary Trie** containing all achievable non-empty sums, allowing
    each query to find the sum minimizing XOR with `A`.

------------------------------------------------------------------------

# 1. Subset-Sum DP

Let:

``` cpp
ways[s]
```

be the number of subsequences whose sum is exactly `s`, modulo:

``` text
MOD = 1,000,000,007
```

We use the standard 0/1 subset-sum transition.

Initially:

``` cpp
ways[0] = 1;
```

This represents the empty subset **only as an internal DP state**, so
that selecting the first element can be generated naturally.

For every array element `x`, iterate sums in descending order:

``` cpp
for (int s = currentSum; s >= 0; --s)
```

and update:

``` cpp
ways[s + x] += ways[s];
```

Descending iteration is essential because each input element can be
selected at most once.

------------------------------------------------------------------------

# 2. Why Reachability Must Be Stored Separately

A subtle but important issue is that `ways[s]` is stored modulo:

``` text
10^9 + 7
```

Suppose the true number of subsequences producing sum `s` is a multiple
of `10^9 + 7`.

Then:

``` cpp
ways[s] == 0
```

even though the sum is actually achievable.

Therefore this is incorrect:

``` cpp
if (ways[s] != 0)
    // sum is reachable
```

Instead, maintain:

``` cpp
vector<char> reachable;
```

where:

``` cpp
reachable[s] = true
```

means at least one subsequence produces sum `s`, independently of its
modulo count.

The DP therefore maintains both:

``` text
ways[s]       -> count modulo MOD
reachable[s]  -> actual existence
```

------------------------------------------------------------------------

# 3. Empty Subsequence Must Not Be an Answer

The DP starts with:

``` cpp
ways[0] = 1;
reachable[0] = true;
```

but this is only an internal state.

The problem requires non-empty subsequences.

Since all sequence values are positive:

``` text
sequence[i] >= 1
```

every non-empty subsequence has a positive sum.

Therefore when building the binary trie, we insert only:

``` text
sum >= 1
```

and deliberately exclude `0`.

------------------------------------------------------------------------

# 4. Binary Trie for Minimum XOR

After DP, insert every reachable non-empty sum into a binary trie.

Each trie node has two children:

``` text
child[0]
child[1]
```

representing a binary bit.

Because query values can be as large as `10^9`, we process bits from
`30` down to `0`.

------------------------------------------------------------------------

# 5. Greedy Minimum-XOR Query

Suppose the current bit of query `A` is `b`.

To minimize XOR, we prefer a stored sum having the **same bit**:

``` text
b XOR b = 0
```

If such a trie child exists, choose it.

Otherwise we are forced to choose:

``` text
b XOR 1 = 1
```

at that position.

Because bits are processed from most significant to least significant,
greedily minimizing the current bit always gives the globally minimum
XOR value.

At the end of the traversal, reconstruct the chosen sum.

Then output:

``` cpp
bestSum
ways[bestSum]
```

------------------------------------------------------------------------

# Correctness

## Lemma 1: DP finds every achievable subsequence sum

For every element `x`, the descending DP transition considers two
possibilities:

-   Do not select `x`.
-   Select `x`, converting a previous sum `s` into `s + x`.

Because sums are processed in descending order, the current element
cannot be reused during the same iteration.

Thus after processing all elements, every subset/subsequence sum is
represented.

------------------------------------------------------------------------

## Lemma 2: `ways[s]` contains the correct count modulo MOD

Whenever an existing subsequence of sum `s` selects the current element
`x`, it creates exactly one subsequence of sum:

``` text
s + x
```

Therefore:

``` cpp
ways[s + x] += ways[s];
```

counts all possible subsequences.

Taking every update modulo `10^9 + 7` produces the required answer
count.

------------------------------------------------------------------------

## Lemma 3: The trie contains exactly the achievable non-empty sums

`reachable[s]` records whether a sum can actually be formed.

The trie inserts every `s >= 1` for which:

``` cpp
reachable[s] == true
```

Since all input elements are positive, `sum = 0` corresponds only to the
empty subsequence and is excluded.

Therefore the trie contains exactly the sums of valid non-empty
subsequences.

------------------------------------------------------------------------

## Lemma 4: Trie traversal finds the achievable sum minimizing XOR with A

At each bit, the algorithm prefers the child having the same bit as `A`.

This makes the XOR bit `0`.

If the same-bit child does not exist, every achievable candidate in the
current trie subtree must produce XOR bit `1`, so taking the opposite
child is forced.

Since higher bits dominate all lower bits numerically, minimizing each
bit greedily from most significant to least significant gives the
minimum possible XOR value.

Therefore the returned sum minimizes:

``` text
sum XOR A
```

over all achievable non-empty subsequence sums.

------------------------------------------------------------------------

# C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

static const int MOD = 1000000007;
static const int MAX_BIT = 30;

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
        trie.emplace_back();
    }

    void insert(int x) {
        int node = 0;

        for (int bit = MAX_BIT; bit >= 0; --bit) {

            int b = (x >> bit) & 1;

            if (trie[node].child[b] == -1) {
                trie[node].child[b] =
                    (int)trie.size();

                trie.emplace_back();
            }

            node = trie[node].child[b];
        }
    }

    /*
        Return the stored value x minimizing:

            x XOR value
    */
    int minimumXorValue(int value) const {

        int node = 0;
        int result = 0;

        for (int bit = MAX_BIT; bit >= 0; --bit) {

            int b = (value >> bit) & 1;

            // Prefer the same bit because b XOR b = 0.
            if (trie[node].child[b] != -1) {

                node = trie[node].child[b];

                if (b)
                    result |= (1 << bit);
            }
            else {

                int other = b ^ 1;

                node = trie[node].child[other];

                if (other)
                    result |= (1 << bit);
            }
        }

        return result;
    }
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> a(N);

    int totalSum = 0;

    for (int &x : a) {
        cin >> x;
        totalSum += x;
    }

    /*
        ways[s]:
            number of subsequences with sum s modulo MOD.

        reachable[s]:
            whether at least one subsequence has sum s.

        Sum 0 represents the empty subset only as an
        internal DP state.
    */
    vector<int> ways(totalSum + 1, 0);
    vector<char> reachable(totalSum + 1, false);

    ways[0] = 1;
    reachable[0] = true;

    int currentSum = 0;

    for (int x : a) {

        // Descending order -> each element used at most once.
        for (int s = currentSum; s >= 0; --s) {

            if (!reachable[s])
                continue;

            reachable[s + x] = true;

            ways[s + x] += ways[s];

            if (ways[s + x] >= MOD)
                ways[s + x] -= MOD;
        }

        currentSum += x;
    }

    /*
        Insert ONLY non-empty subsequence sums.

        Because all input values are positive, all non-empty
        subsequence sums are >= 1.
    */
    BinaryTrie trie;

    for (int sum = 1; sum <= totalSum; ++sum) {

        if (reachable[sum]) {
            trie.insert(sum);
        }
    }

    int Q;
    cin >> Q;

    while (Q--) {

        int A;
        cin >> A;

        int bestSum =
            trie.minimumXorValue(A);

        cout << bestSum
             << ' '
             << ways[bestSum]
             << '\n';
    }

    return 0;
}
```

------------------------------------------------------------------------

# Time Complexity

Let:

``` text
S = sum of all sequence elements
```

Since:

``` text
N <= 100
a[i] <= 1000
```

we have:

``` text
S <= 100000
```

## Subset-Sum DP

For each of `N` elements, we process at most `S` sums:

\[ `\boxed{O(N \cdot S)}`{=tex} \]

In the worst case:

``` text
100 * 100000 = 10^7
```

operations.

------------------------------------------------------------------------

## Trie Construction

There are at most `S` achievable sums.

Each sum uses 31 trie levels:

\[ `\boxed{O(S \cdot 31)}`{=tex} \]

which is effectively:

\[ `\boxed{O(S \log A)}`{=tex} \]

------------------------------------------------------------------------

## Queries

Each query traverses exactly 31 trie levels:

\[ O(31) \]

For `Q` queries:

\[ `\boxed{O(Q \cdot 31)}`{=tex} \]

or:

\[ `\boxed{O(Q \log A)}`{=tex} \]

------------------------------------------------------------------------

## Overall Time Complexity

\[ `\boxed{
O(N \cdot S + S\log A + Q\log A)
}`{=tex} \]

Since the trie depth is fixed at 31, this is very efficient for up to:

``` text
Q = 500000
```

------------------------------------------------------------------------

# Space Complexity

The DP arrays require:

\[ O(S) \]

space.

The binary trie stores at most 31 nodes per achievable sum in the
theoretical worst case:

\[ O(S`\log `{=tex}A) \]

although prefixes are heavily shared in practice.

Therefore:

\[ `\boxed{O(S\log A)}`{=tex} \]

is the overall worst-case space complexity.

------------------------------------------------------------------------

# Trade-offs

## Advantages

-   Expensive subsequence computation is performed only once.
-   Handles up to `500000` queries efficiently.
-   Each query requires only about 31 trie steps.
-   Correctly counts subsequences modulo `10^9 + 7`.
-   Separating reachability from modulo counts avoids a subtle
    correctness bug.
-   Excluding sum `0` correctly removes the empty subsequence.
-   Binary trie provides deterministic minimum-XOR lookup.

## Disadvantages

-   Subset-sum DP depends on the relatively small maximum total sum
    (`<= 100000`).
-   A binary trie uses more memory than simply storing achievable sums.
-   The solution relies on all sequence values being positive to
    identify `0` exclusively with the empty subsequence.

------------------------------------------------------------------------

# Important Pitfalls

### 1. Do not include the empty subsequence

Although DP needs:

``` cpp
ways[0] = 1;
```

do **not** insert sum `0` into the trie.

Otherwise queries can incorrectly choose the empty subsequence.

### 2. Do not use ways\[s\] to determine reachability

This is incorrect:

``` cpp
if (ways[s] != 0)
```

because counts are modulo `10^9 + 7`.

Instead use:

``` cpp
reachable[s]
```

separately.

### 3. Iterate subset-sum DP backwards

This is required:

``` cpp
for (int s = currentSum; s >= 0; --s)
```

Forward iteration could reuse the same element multiple times, turning
the solution into an unbounded knapsack.

------------------------------------------------------------------------

# Summary

The solution first reduces the exponential number of subsequences to at
most `100000` possible sums using 0/1 subset-sum DP.

It then inserts every reachable **non-empty** sum into a binary trie.

For every query `A`, the trie greedily chooses matching bits from most
significant to least significant, returning the achievable sum
minimizing:

``` text
sum XOR A
```

The corresponding DP count gives the required number of subsequences
modulo `10^9 + 7`.
