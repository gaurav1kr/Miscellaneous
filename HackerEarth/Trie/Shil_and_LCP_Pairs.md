# Shil and LCP Pairs

## Problem Statement

Given `N` lowercase English strings `S1, S2, ..., SN`, find for every
`k` in `[0, L]` the number of unordered pairs `(i, j)` such that:

``` text
LCP(Si, Sj) = k
```

where `LCP` is the longest common prefix and:

``` text
L = max(len(Si))
```

### Input

-   First line: integer `N`.
-   Next `N` lines: the strings.

### Output

Print `L + 1` integers:

``` text
h0 h1 h2 ... hL
```

where `hk` is the number of unordered pairs having LCP length exactly
`k`.

### Constraints

-   `1 <= N <= 10^5`
-   Sum of lengths of all strings is at most `10^6`.
-   Strings contain only `'a'` to `'z'`.

### Sample

``` text
Input:
5
aaaa
ab
abcd
aaae
g

Output:
4 4 1 1 0
```

------------------------------------------------------------------------

## Approach: Trie + Pair Counting

A trie naturally groups strings by common prefixes.

For each trie node `v`, maintain:

-   `cnt[v]`: number of strings passing through `v`.
-   `depth[v]`: length of the prefix represented by `v`.

If `cnt[v] = x`, then:

\[ C(x,2) = `\frac{x(x-1)}{2}`{=tex} \]

pairs share **at least** `depth[v]` characters.

However, pairs that both continue through the same child have a longer
common prefix. Therefore:

\[ `\boxed{
exact(v)=C(cnt[v],2)-\sum_{u \in children(v)}C(cnt[u],2)
}`{=tex} \]

Then:

``` cpp
answer[depth[v]] += exact(v);
```

This also automatically handles strings ending at a node, duplicate
strings, and LCP equal to zero at the root.

------------------------------------------------------------------------

## Correctness

Consider a pair `(A, B)` whose exact LCP length is `k`.

Both strings pass through the same trie node `v` at depth `k`, so they
are included in `C(cnt[v], 2)`.

They do not both enter the same child of `v`; otherwise their common
prefix would have length at least `k + 1`. Therefore the pair is not
removed by the child subtraction and remains in `exact(v)`.

At every ancestor of `v`, both strings do enter the same child, so the
pair is subtracted there.

Hence each pair is counted exactly once, at the node representing its
exact longest common prefix.

------------------------------------------------------------------------

## C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using int64 = long long;

struct Node {
    int child[26];
    int cnt;
    int terminal;
    int depth;

    Node(int d = 0) {
        fill(child, child + 26, -1);
        cnt = 0;
        terminal = 0;
        depth = d;
    }
};

static inline int64 choose2(int64 x) {
    return x * (x - 1) / 2;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<Node> trie;
    trie.reserve(1000005);
    trie.emplace_back(0);

    int maxLen = 0;

    // Insert all strings.
    for (int i = 0; i < N; ++i) {
        string s;
        cin >> s;

        maxLen = max(maxLen, (int)s.size());

        int node = 0;
        trie[node].cnt++;

        for (char ch : s) {
            int c = ch - 'a';

            if (trie[node].child[c] == -1) {
                trie[node].child[c] = (int)trie.size();
                trie.emplace_back(trie[node].depth + 1);
            }

            node = trie[node].child[c];
            trie[node].cnt++;
        }

        trie[node].terminal++;
    }

    vector<int64> answer(maxLen + 1, 0);

    /*
        C(cnt[v], 2) = pairs whose LCP is at least depth[v].

        Pairs continuing through the same child have a longer
        common prefix, so subtract those child contributions.
    */
    for (int v = 0; v < (int)trie.size(); ++v) {
        int64 exact = choose2(trie[v].cnt);

        for (int c = 0; c < 26; ++c) {
            int to = trie[v].child[c];

            if (to != -1) {
                exact -= choose2(trie[to].cnt);
            }
        }

        answer[trie[v].depth] += exact;
    }

    for (int k = 0; k <= maxLen; ++k) {
        if (k)
            cout << ' ';

        cout << answer[k];
    }

    cout << '\n';

    return 0;
}
```

------------------------------------------------------------------------

## Time Complexity

Let `M` be the sum of lengths of all input strings.

Trie construction processes every character once:

\[ O(M) \]

The trie contains at most `M + 1` nodes. For each node we inspect 26
children:

\[ O(26M)=O(M) \]

because the alphabet size is constant.

Therefore:

\[ `\boxed{O(M)}`{=tex} \]

------------------------------------------------------------------------

## Space Complexity

The trie contains at most `M + 1` nodes, so:

\[ `\boxed{O(M)}`{=tex} \]

space is required.

The answer array requires `O(L)` additional space, where `L <= M`.

------------------------------------------------------------------------

## Trade-offs

### Advantages

-   Linear time for a fixed 26-character alphabet.
-   Avoids comparing all `O(N^2)` string pairs.
-   Handles duplicate strings correctly.
-   Handles one string being a prefix of another.
-   LCP `0` is handled naturally by the root.
-   No recursive DFS is required.

### Disadvantages

-   Each trie node stores 26 child indices, so memory usage can be
    relatively high.
-   A compressed/sparse trie could use less memory but would add lookup
    overhead and implementation complexity.

------------------------------------------------------------------------

## Key Formula

The complete solution is based on:

\[ `\boxed{
answer[depth(v)] +=
C(cnt[v],2)
-
\sum_{u \in children(v)}C(cnt[u],2)
}`{=tex} \]

Every unordered pair is counted exactly once at the trie node
representing its longest common prefix.
