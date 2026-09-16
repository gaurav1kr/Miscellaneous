# Minimize Trie Nodes

## Problem Statement

You are given `N` strings. Each string is represented by an array `cnt`
of size `26`, where:

``` text
cnt[i]
```

is the number of occurrences of the `i`-th lowercase English character
in that string.

You must select **exactly 4 distinct strings**.

Before inserting the selected strings into a trie, their characters may
be rearranged arbitrarily. The checker inserts the strings in an optimal
order so that the number of trie nodes is minimized.

The objective is to minimize:

``` text
Z = number of nodes in the resulting trie
```

The root node is included in the count.

### Important

This is an **approximate/optimization problem**. There is no single
exact output. Any four valid distinct indices form a valid answer, but
better selections receive a better score.

### Input Format

-   First line contains integer `N`.
-   The next `N` lines contain 26 integers describing the character
    counts of each string.

### Output Format

Print four distinct 1-based indices:

``` text
i1 i2 i3 i4
```

### Constraints

-   `N = 300`
-   `0 <= cnt[i][j] <= 10^5`
-   No input string is empty.

------------------------------------------------------------------------

# Key Observation

Because the characters of each selected string can be shuffled, the
original order of characters does not matter.

What matters is the amount of **multiset overlap** between selected
strings.

For two strings `A` and `B`, define:

\[ overlap(A,B) = `\sum`{=tex}\_{c=0}\^{25} `\min`{=tex}(A_c,B_c) \]

This measures how many character occurrences can potentially be shared
in a common trie prefix after rearrangement.

Selecting strings with large overlap generally allows more trie-prefix
sharing and therefore tends to reduce the number of trie nodes.

------------------------------------------------------------------------

# Heuristic Approach

Since this is an approximate problem, the solution uses a strong
heuristic rather than attempting an exact optimization over all:

\[ `\binom{300}{4}`{=tex} \]

quadruples.

The strategy has three stages:

1.  Compute pairwise multiset intersections.
2.  Build a promising candidate pool.
3.  Exhaustively test quadruples inside that pool and then apply local
    improvement using all `N` strings.

------------------------------------------------------------------------

## 1. Pairwise Intersection

For every pair `(i, j)`, calculate:

\[ I(i,j) = `\sum`{=tex}\_{c=0}\^{25}
`\min`{=tex}(cnt\[i\]\[c\],cnt\[j\]\[c\]) \]

There are only:

\[ `\binom{300}{2}`{=tex}=44850 \]

pairs, so this is inexpensive.

Pairs are sorted by decreasing intersection.

Strings appearing in the strongest pairs are likely to be good
candidates for the final answer.

------------------------------------------------------------------------

## 2. Candidate Pool

Take approximately 60 distinct strings occurring in the highest-overlap
pairs.

This reduces the search space from:

\[ `\binom{300}{4}`{=tex} `\approx 330`{=tex}`\text{ million}`{=tex} \]

to:

\[ `\binom{60}{4}`{=tex} =487635 \]

quadruples.

This is small enough to evaluate directly.

------------------------------------------------------------------------

# 3. Scoring Four Strings

For selected strings:

``` text
A, B, C, D
```

we consider three levels of commonality.

## Four-Way Commonality

For every character:

\[ `\min`{=tex}(A_c,B_c,C_c,D_c) \]

Summing over all characters gives the number of character occurrences
common to all four strings.

This is especially valuable because a prefix shared by all four strings
saves many trie nodes.

------------------------------------------------------------------------

## Triple Commonality

For each of the four possible triples, calculate the multiset
intersection.

For example:

\[ `\sum`{=tex}\_c `\min`{=tex}(A_c,B_c,C_c) \]

and similarly for the other triples.

------------------------------------------------------------------------

## Pairwise Commonality

Sum the intersections of all six pairs:

``` text
(A,B)
(A,C)
(A,D)
(B,C)
(B,D)
(C,D)
```

------------------------------------------------------------------------

# Heuristic Score

The implementation uses:

``` text
score =
    12 * common4
  +  4 * common3
  +      common2
```

Higher-order sharing receives more weight because sharing a trie prefix
among four strings is generally more valuable than sharing it among only
two.

A larger heuristic score is treated as a better candidate for minimizing
trie nodes.

These weights are heuristic rather than mathematically exact because the
problem itself is approximate.

------------------------------------------------------------------------

# 4. Exhaustive Search Inside Candidate Pool

After selecting the candidate pool, evaluate every quadruple:

``` text
i < j < k < l
```

and keep the quadruple with the highest heuristic score.

For 60 candidates there are only:

``` text
487635
```

quadruples.

Each score examines only 26 characters, so this is practical.

------------------------------------------------------------------------

# 5. Local Improvement

The candidate-pool search might miss a useful string outside the initial
top 60.

Therefore the solution performs a second optimization phase.

For each of the four selected positions:

1.  Try replacing it with every one of the `N` strings.
2.  Reject replacements that create duplicate indices.
3.  Recalculate the heuristic score.
4.  Keep an improving replacement.
5.  Repeat until no further single replacement improves the score.

This allows the final solution to escape some weaknesses of the initial
candidate selection.

------------------------------------------------------------------------

# C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

static const int ALPHA = 26;

struct Str {
    array<int, ALPHA> cnt{};
    ll len = 0;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<Str> a(N);

    for (int i = 0; i < N; ++i) {
        for (int c = 0; c < ALPHA; ++c) {
            cin >> a[i].cnt[c];
            a[i].len += a[i].cnt[c];
        }
    }

    // Pairwise intersection.
    vector<vector<ll>> inter(N, vector<ll>(N, 0));

    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {

            ll val = 0;

            for (int c = 0; c < ALPHA; ++c)
                val += min(a[i].cnt[c], a[j].cnt[c]);

            inter[i][j] = inter[j][i] = val;
        }
    }

    /*
        Larger score = more potential prefix sharing
                     = fewer expected trie nodes.
    */
    auto score = [&](int x, int y, int z, int w) -> ll {

        int ids[4] = {x, y, z, w};

        ll common4 = 0;

        for (int c = 0; c < ALPHA; ++c) {

            int mn = INT_MAX;

            for (int p = 0; p < 4; ++p)
                mn = min(mn, a[ids[p]].cnt[c]);

            common4 += mn;
        }

        ll common3 = 0;

        for (int skip = 0; skip < 4; ++skip) {

            for (int c = 0; c < ALPHA; ++c) {

                int mn = INT_MAX;

                for (int p = 0; p < 4; ++p) {

                    if (p == skip)
                        continue;

                    mn = min(mn, a[ids[p]].cnt[c]);
                }

                common3 += mn;
            }
        }

        ll common2 = 0;

        for (int p = 0; p < 4; ++p) {
            for (int q = p + 1; q < 4; ++q) {
                common2 += inter[ids[p]][ids[q]];
            }
        }

        return common4 * 12
             + common3 * 4
             + common2;
    };

    struct PairInfo {
        ll score;
        int x, y;

        bool operator<(const PairInfo& other) const {
            return score > other.score;
        }
    };

    vector<PairInfo> pairs;

    pairs.reserve(N * (N - 1) / 2);

    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {

            pairs.push_back({
                inter[i][j],
                i,
                j
            });
        }
    }

    sort(pairs.begin(), pairs.end());

    // Candidate pool.
    vector<int> candidates;
    vector<char> used(N, false);

    const int LIMIT = min(N, 60);

    for (const auto &p : pairs) {

        if (!used[p.x]) {
            used[p.x] = true;
            candidates.push_back(p.x);
        }

        if ((int)candidates.size() == LIMIT)
            break;

        if (!used[p.y]) {
            used[p.y] = true;
            candidates.push_back(p.y);
        }

        if ((int)candidates.size() == LIMIT)
            break;
    }

    // Safety: ensure at least four candidates.
    for (int i = 0;
         i < N && (int)candidates.size() < 4;
         ++i) {

        if (!used[i]) {
            used[i] = true;
            candidates.push_back(i);
        }
    }

    ll bestScore = LLONG_MIN;

    array<int, 4> best = {
        0, 1, 2, 3
    };

    int C = candidates.size();

    // Exhaustively evaluate quadruples in candidate pool.
    for (int ii = 0; ii < C; ++ii) {

        int i = candidates[ii];

        for (int jj = ii + 1; jj < C; ++jj) {

            int j = candidates[jj];

            for (int kk = jj + 1; kk < C; ++kk) {

                int k = candidates[kk];

                for (int llidx = kk + 1;
                     llidx < C;
                     ++llidx) {

                    int l = candidates[llidx];

                    ll cur = score(i, j, k, l);

                    if (cur > bestScore) {

                        bestScore = cur;

                        best = {
                            i, j, k, l
                        };
                    }
                }
            }
        }
    }

    // Local improvement against all N strings.
    bool improved = true;

    while (improved) {

        improved = false;

        for (int pos = 0; pos < 4; ++pos) {

            for (int candidate = 0;
                 candidate < N;
                 ++candidate) {

                bool duplicate = false;

                for (int p = 0; p < 4; ++p) {

                    if (p != pos &&
                        best[p] == candidate) {

                        duplicate = true;
                        break;
                    }
                }

                if (duplicate)
                    continue;

                auto temp = best;

                temp[pos] = candidate;

                ll cur = score(
                    temp[0],
                    temp[1],
                    temp[2],
                    temp[3]
                );

                if (cur > bestScore) {

                    bestScore = cur;
                    best = temp;

                    improved = true;
                }
            }
        }
    }

    // Output 1-based indices.
    sort(best.begin(), best.end());

    cout << best[0] + 1 << ' '
         << best[1] + 1 << ' '
         << best[2] + 1 << ' '
         << best[3] + 1 << '\n';

    return 0;
}
```

------------------------------------------------------------------------

# Complexity Analysis

Let:

``` text
N <= 300
A = 26
C = candidate pool size <= 60
```

## Pairwise Intersections

There are:

\[ O(N\^2) \]

pairs and each intersection processes 26 characters:

\[ O(26N\^2) \]

Since 26 is constant:

\[ `\boxed{O(N^2)}`{=tex} \]

------------------------------------------------------------------------

## Sorting Pairs

There are approximately:

\[ N(N-1)/2 \]

pairs.

Sorting requires:

\[ `\boxed{O(N^2 \log N)}`{=tex} \]

approximately.

------------------------------------------------------------------------

## Candidate Quadruple Search

There are:

\[ `\binom{C}{4}`{=tex} \]

quadruples.

Each score examines a constant number of combinations over 26
characters.

Therefore:

\[ `\boxed{O(C^4 \cdot 26)}`{=tex} \]

For `C = 60`:

``` text
C(60,4) = 487635
```

which is practical.

------------------------------------------------------------------------

## Local Search

Each pass tries at most:

``` text
4 * N
```

replacements.

Each replacement evaluates a score over 26 characters.

Therefore each local-search pass costs:

\[ O(4N `\cdot 26`{=tex})=O(N) \]

for fixed alphabet size.

------------------------------------------------------------------------

# Space Complexity

The input requires:

\[ O(26N) \]

space.

The pairwise intersection matrix requires:

\[ O(N\^2) \]

space.

The list of pairs also requires:

\[ O(N\^2) \]

space.

Therefore:

\[ `\boxed{O(N^2)}`{=tex} \]

overall auxiliary space.

------------------------------------------------------------------------

# Trade-offs

## Advantages

-   Much smaller search space than checking all `C(300,4)`
    possibilities.
-   Uses the ability to shuffle characters directly in its heuristic.
-   Rewards two-way, three-way, and four-way multiset overlap.
-   Exhaustively searches a strong candidate subset.
-   Local improvement can introduce strings outside the initial
    candidate pool.
-   Deterministic and easy to reproduce.

## Disadvantages

-   This is a heuristic; it does not guarantee the globally optimal four
    strings.
-   The weighted score is only a proxy for the checker's exact optimal
    trie-node count.
-   A good quadruple could theoretically contain strings that do not
    individually appear in the strongest pairwise overlaps.
-   Different weighting or randomized search may achieve better scores
    on some datasets.

------------------------------------------------------------------------

# Possible Improvements

Because this is an approximate challenge, further scoring improvements
can be attempted:

-   Increase the candidate pool if the time limit allows.
-   Run randomized restarts.
-   Use simulated annealing.
-   Try two-position replacements instead of only one-position
    replacements.
-   Tune the weights for four-way, triple, and pairwise intersections.
-   Develop a more exact estimator for the minimum trie size obtainable
    after character rearrangement.

------------------------------------------------------------------------

# Summary

The problem asks for four strings that can share as much trie structure
as possible after their characters are rearranged.

The heuristic therefore favors strings with high multiset overlap:

\[ overlap(A,B)=`\sum`{=tex}\_c`\min`{=tex}(A_c,B_c) \]

and extends this idea to triple and four-way intersections.

The solution combines:

``` text
pairwise preprocessing
        +
candidate reduction
        +
exhaustive quadruple search
        +
local improvement
```

to produce a strong valid solution within practical time limits.
