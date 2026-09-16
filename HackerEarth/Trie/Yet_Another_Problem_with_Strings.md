# Yet Another Problem with Strings

## Problem Statement

You are given a 0-indexed array `S` containing `N` non-empty lowercase
English strings and `Q` queries.

Maintain an integer `LAST_YES`, initially `0`. `LAST_YES` is the index
of the most recent type-1 query whose answer was `"YES"`.

There are two types of queries.

### Type 1

``` text
1 t
```

Before processing the query, decipher every character of `t`:

``` cpp
c = (c + LAST_YES) % 26;
```

where characters are interpreted as values `0..25`.

After deciphering, determine whether **at least one current string
`S[i]` is a substring of `t`**.

Print:

``` text
YES
```

or:

``` text
NO
```

If the answer is `YES`, update:

``` text
LAST_YES = current query index
```

Queries are 0-indexed.

### Type 2

``` text
2 i alpha
```

Decipher the parameters:

``` cpp
i = (i + LAST_YES) % N;
alpha = (alpha + LAST_YES) % 26;
```

Then append character `alpha` to the end of `S[i]`.

### Constraints

-   `1 <= N, Q <= 200000`
-   Total length of the initial strings is at most `200000`.
-   Total length of strings appearing in type-1 queries is at most
    `200000`.
-   Strings contain only lowercase English letters.

------------------------------------------------------------------------

# Key Observations

A straightforward solution is difficult because:

1.  There can be up to `200000` strings.
2.  There can be up to `200000` queries.
3.  We must repeatedly determine whether **any current `S[i]` occurs
    inside a query string**.
4.  Type-2 operations dynamically modify strings.
5.  A string is modified only by **appending one character**.

The fifth property is the key.

Because strings only grow by appending characters, every version of
every `S[i]` can naturally be represented inside one global **prefix
trie**.

A type-2 update does not require rebuilding the data structure. It
simply moves the endpoint representing `S[i]` from its current trie node
to one child.

------------------------------------------------------------------------

# Approach

The solution combines:

-   Dynamic prefix trie
-   Double polynomial rolling hash
-   Hash table from a trie-path hash to its trie node
-   Lazy maintenance of active/dead trie paths
-   Iterative traversal to avoid stack overflow

------------------------------------------------------------------------

## 1. Global Prefix Trie

Insert every initial string into one trie.

Each trie node represents the string formed by the path:

``` text
root -> node
```

For every original string `S[i]`, maintain:

``` cpp
posStr[i]
```

which stores the trie node representing the current complete value of
`S[i]`.

For example, if:

``` text
S[i] = "abc"
```

then `posStr[i]` points to the node:

``` text
root -> a -> b -> c
```

------------------------------------------------------------------------

## 2. Handling Append Operations

Suppose:

``` text
S[i] = "abc"
```

and a type-2 query appends `'d'`.

Instead of rebuilding anything, move:

``` text
abc -> abcd
```

in the trie.

If the `'d'` child does not exist, create exactly one new trie node.

Therefore a type-2 operation requires only a constant amount of
structural trie work, apart from amortized lazy cleanup.

------------------------------------------------------------------------

# 3. Active Prefix Information

For a trie node `v`, we need to know whether at least one current string
`S[i]` is a prefix of the trie path represented by `v`.

Why?

Suppose the trie path represented by `v` is:

``` text
abcdef
```

and one current string is:

``` text
abc
```

Then if the query text contains `"abcdef"`, it certainly contains
`"abc"`.

So a trie path is useful whenever one of the current strings ends at
that node or at one of its ancestors.

The implementation maintains:

``` cpp
prefCnt[v]
addCnt[v]
deadNode[v]
```

`deadNode[v] == false` means that the represented trie path can still
prove that some current `S[i]` is present.

When strings grow, some old paths may stop having any active string as a
prefix. Those paths are marked dead lazily.

------------------------------------------------------------------------

# 4. Lazy Dead-Node Removal

When `S[i]` moves from node `v` to one of its children, the old endpoint
at `v` is no longer active.

This may make `v`, and possibly some descendants, useless.

The function:

``` cpp
removeDead(v)
```

propagates this change.

An important amortization property is:

> A trie node becomes dead at most once.

Therefore, even though `removeDead()` can traverse multiple nodes during
one update, the total cleanup work over all queries is bounded by the
total number of trie nodes.

------------------------------------------------------------------------

# 5. Why Iterative Traversal Is Important

The trie can be extremely deep.

For example, one string could contain hundreds of thousands of
characters, producing a trie shaped like:

``` text
root
 |
 a
 |
 b
 |
 c
 |
 ...
```

A recursive DFS on such a trie can overflow the C++ call stack and
produce a runtime error.

Therefore both initialization and lazy dead-node processing are
implemented **iteratively using explicit vectors as stacks**.

This avoids recursion-depth failures.

------------------------------------------------------------------------

# 6. Double Rolling Hash

For each trie node, store two polynomial hashes of the path from the
root:

``` cpp
treeHash1[v]
treeHash2[v]
```

Two hashes significantly reduce the probability of collisions compared
with using one hash.

A custom hash table maps:

``` text
(normalizedHash1, normalizedHash2)
            ->
        trie node
```

This lets us test whether a substring of a query string corresponds to
some path existing in the trie.

------------------------------------------------------------------------

# 7. Processing a Type-1 Query

First decipher the query string using `LAST_YES`.

Then calculate two prefix-hash arrays:

``` cpp
h1[]
h2[]
```

For every starting position `i` in the query string, we want to
determine how far the substring:

``` text
t[i...]
```

matches a path in the global trie.

Trie-prefix existence is monotonic:

``` text
if prefix of length L does not exist,
then no longer prefix can exist.
```

Therefore we binary-search for the longest matching trie path.

If its corresponding trie node is not dead:

``` cpp
!deadNode[v]
```

then some current `S[j]` is a prefix of that matched path.

Hence:

``` text
S[j] is a substring of t
```

and the answer is `YES`.

------------------------------------------------------------------------

# Correctness Intuition

Consider any current string `S[j]`.

Because strings only grow by appending characters, its complete value
always corresponds to some path in the global trie.

Now suppose `S[j]` occurs in query text `t` starting at position `i`.

The algorithm examines suffix:

``` text
t[i...]
```

and finds the longest prefix of that suffix that exists in the trie.

Since `S[j]` itself is such a trie path, the longest matched path has
length at least:

``` text
|S[j]|
```

Furthermore, the lazy active-prefix information ensures that the matched
node remains non-dead when some current `S[j]` is a prefix of that path.

Therefore the algorithm returns `YES`.

Conversely, if a matched node is non-dead, some current string is a
prefix of that matched trie path. Since the matched path occurs in `t`,
that current string also occurs in `t`.

Thus the algorithm reports `YES` exactly when at least one current
`S[i]` is a substring of the deciphered query text.

------------------------------------------------------------------------

# C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

static const int MAXV = 1000000 + 100;

static const int P1 = 53;
static const int P2 = 59;
static const int MIX = 14243;
static const int MOD = 1000000021;

static const int HASH_SIZE = 1 << 20;

static int nxt[MAXV][26];

static int addCnt[MAXV];
static int prefCnt[MAXV];

static int lenNode[MAXV];
static int posStr[MAXV];

static bool deadNode[MAXV];

static int nodes = 0;

static int pw1[MAXV];
static int pw2[MAXV];

static int treeHash1[MAXV];
static int treeHash2[MAXV];

static int h1[MAXV];
static int h2[MAXV];

vector<pair<pair<int,int>, int>> tableHash[HASH_SIZE];

inline int bucketId(int a, int b) {
    return (a + 1LL * b * MIX) & (HASH_SIZE - 1);
}

inline void insertHash(pair<int,int> h, int node) {

    int bucket = bucketId(h.first, h.second);

    for (const auto &x : tableHash[bucket]) {
        if (x.first == h)
            return;
    }

    tableHash[bucket].push_back({h, node});
}

inline int findHash(pair<int,int> h) {

    int bucket = bucketId(h.first, h.second);

    for (const auto &x : tableHash[bucket]) {
        if (x.first == h)
            return x.second;
    }

    return -1;
}

inline int normalize1(int h, int power) {

    return (int)(
        1LL * h *
        pw1[MAXV - 1 - power] % MOD
    );
}

inline int normalize2(int h, int power) {

    return (int)(
        1LL * h *
        pw2[MAXV - 1 - power] % MOD
    );
}

int addInitialString(const string &s) {

    int v = 0;

    for (char ch : s) {

        int c = ch - 'a';

        if (!nxt[v][c]) {

            if (nodes + 1 >= MAXV) {
                exit(0);
            }

            nxt[v][c] = ++nodes;
        }

        v = nxt[v][c];
    }

    ++addCnt[v];

    return v;
}

void buildInitial() {

    struct State {
        int v;
        int prefix;
    };

    vector<State> st;

    st.reserve(nodes + 1);

    st.push_back({0, 0});

    while (!st.empty()) {

        State cur = st.back();
        st.pop_back();

        int v = cur.v;

        int prefix =
            cur.prefix + addCnt[v];

        prefCnt[v] = prefix;

        addCnt[v] = 0;

        insertHash(
            {
                normalize1(treeHash1[v], 0),
                normalize2(treeHash2[v], 0)
            },
            v
        );

        for (int c = 0; c < 26; ++c) {

            int to = nxt[v][c];

            if (!to)
                continue;

            lenNode[to] =
                lenNode[v] + 1;

            treeHash1[to] =
                (
                    treeHash1[v] +
                    1LL * (c + 1) *
                    pw1[lenNode[v]]
                ) % MOD;

            treeHash2[to] =
                (
                    treeHash2[v] +
                    1LL * (c + 1) *
                    pw2[lenNode[v]]
                ) % MOD;

            st.push_back({
                to,
                prefix
            });
        }
    }
}

void removeDead(int start) {

    if (deadNode[start])
        return;

    if (addCnt[start] + prefCnt[start] > 0)
        return;

    vector<int> st;

    st.push_back(start);

    while (!st.empty()) {

        int v = st.back();
        st.pop_back();

        if (deadNode[v])
            continue;

        int active =
            addCnt[v] + prefCnt[v];

        if (active > 0)
            continue;

        deadNode[v] = true;

        int carry = addCnt[v];

        for (int c = 0; c < 26; ++c) {

            int to = nxt[v][c];

            if (!to)
                continue;

            addCnt[to] += carry;

            if (!deadNode[to] &&
                addCnt[to] + prefCnt[to] <= 0) {

                st.push_back(to);
            }
        }

        addCnt[v] = 0;
    }
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    pw1[0] = 1;
    pw2[0] = 1;

    for (int i = 1; i < MAXV; ++i) {

        pw1[i] =
            (int)(
                1LL * pw1[i - 1] *
                P1 % MOD
            );

        pw2[i] =
            (int)(
                1LL * pw2[i - 1] *
                P2 % MOD
            );
    }

    int N, Q;

    cin >> N >> Q;

    for (int i = 0; i < N; ++i) {

        string s;
        cin >> s;

        posStr[i] =
            addInitialString(s);
    }

    buildInitial();

    removeDead(0);

    int LAST_YES = 0;

    for (int queryIndex = 0;
         queryIndex < Q;
         ++queryIndex) {

        int type;
        cin >> type;

        if (type == 1) {

            string t;
            cin >> t;

            int m = (int)t.size();

            int shift = LAST_YES % 26;

            if (shift) {

                for (char &ch : t) {

                    ch = char(
                        'a' +
                        (ch - 'a' + shift) % 26
                    );
                }
            }

            h1[0] = t[0] - 'a' + 1;
            h2[0] = t[0] - 'a' + 1;

            for (int i = 1; i < m; ++i) {

                int c =
                    t[i] - 'a' + 1;

                h1[i] =
                    (
                        h1[i - 1] +
                        1LL * c * pw1[i]
                    ) % MOD;

                h2[i] =
                    (
                        h2[i - 1] +
                        1LL * c * pw2[i]
                    ) % MOD;
            }

            bool answer = false;

            for (int i = m - 1;
                 i >= 0 && !answer;
                 --i) {

                int low = i;
                int high = m;

                while (high - low > 1) {

                    int mid =
                        (low + high) >> 1;

                    int x1 =
                        (
                            h1[mid] -
                            (i ? h1[i - 1] : 0)
                            + MOD
                        ) % MOD;

                    int x2 =
                        (
                            h2[mid] -
                            (i ? h2[i - 1] : 0)
                            + MOD
                        ) % MOD;

                    x1 =
                        normalize1(x1, i);

                    x2 =
                        normalize2(x2, i);

                    if (findHash({x1, x2}) != -1)
                        low = mid;
                    else
                        high = mid;
                }

                int x1 =
                    (
                        h1[low] -
                        (i ? h1[i - 1] : 0)
                        + MOD
                    ) % MOD;

                int x2 =
                    (
                        h2[low] -
                        (i ? h2[i - 1] : 0)
                        + MOD
                    ) % MOD;

                x1 =
                    normalize1(x1, i);

                x2 =
                    normalize2(x2, i);

                int v =
                    findHash({x1, x2});

                if (v != -1 &&
                    !deadNode[v]) {

                    answer = true;
                }
            }

            if (answer) {

                cout << "YES\n";

                LAST_YES =
                    queryIndex;

            } else {

                cout << "NO\n";
            }
        }

        else {

            int id, alpha;

            cin >> id >> alpha;

            id =
                (id + LAST_YES) % N;

            alpha =
                (alpha + LAST_YES) % 26;

            int v =
                posStr[id];

            if (!nxt[v][alpha]) {

                if (nodes + 1 >= MAXV) {
                    return 0;
                }

                int to = ++nodes;

                nxt[v][alpha] = to;

                prefCnt[to] =
                    prefCnt[v];

                lenNode[to] =
                    lenNode[v] + 1;

                treeHash1[to] =
                    (
                        treeHash1[v] +
                        1LL * (alpha + 1) *
                        pw1[lenNode[v]]
                    ) % MOD;

                treeHash2[to] =
                    (
                        treeHash2[v] +
                        1LL * (alpha + 1) *
                        pw2[lenNode[v]]
                    ) % MOD;

                insertHash(
                    {
                        normalize1(
                            treeHash1[to],
                            0
                        ),

                        normalize2(
                            treeHash2[to],
                            0
                        )
                    },
                    to
                );
            }

            int to =
                nxt[v][alpha];

            --addCnt[v];
            ++addCnt[to];

            removeDead(v);

            posStr[id] = to;
        }
    }

    return 0;
}
```

------------------------------------------------------------------------

# Time Complexity

Let:

-   `L` = total length of all initial strings
-   `U` = number of appended characters over all type-2 queries
-   `T` = total length of all type-1 query strings

The trie contains at most:

``` text
O(L + U)
```

nodes.

## Initial Trie Construction

``` text
O(L)
```

expected/amortized work, plus hash-table operations.

## Type-2 Queries

Creating or following one trie edge is `O(1)`.

Dead-node cleanup is amortized because each trie node becomes dead at
most once.

Therefore total cleanup across all updates is:

``` text
O(L + U)
```

and the amortized update cost is very small.

## Type-1 Queries

For a query string of length `m`:

-   Compute hashes: `O(m)`
-   Examine each starting position.
-   Binary-search the longest matching trie path: `O(log m)` hash
    lookups.

Therefore:

``` text
O(m log m)
```

per type-1 query.

Across all type-1 queries:

``` text
O(T log T)
```

as a convenient upper bound.

## Overall

Approximately:

``` text
O(L + U + T log T)
```

with expected constant-time hash-table operations.

------------------------------------------------------------------------

# Space Complexity

The global trie contains:

``` text
O(L + U)
```

nodes.

Each node stores:

-   26 trie transitions
-   counters
-   path length
-   double hashes
-   active/dead state

The hash table also stores entries for trie paths.

Therefore:

``` text
O(L + U)
```

space.

The implementation uses a preallocated `MAXV` bound for predictable
performance.

------------------------------------------------------------------------

# Trade-offs

## Advantages

-   No rebuilding after updates.
-   Efficiently exploits the fact that strings only grow by appending.
-   Handles up to `200000` queries.
-   Total update cleanup is amortized over trie nodes.
-   Double hashing makes accidental hash collisions very unlikely.
-   Iterative traversal avoids stack overflow on extremely deep tries.
-   Much faster than rebuilding Aho-Corasick after batches of updates.

## Disadvantages

-   Significantly more complex than a standard trie or Aho-Corasick
    solution.
-   Uses substantial memory because every trie node has 26 transitions.
-   Rolling hashes are probabilistic; although double hashing makes
    collisions extremely unlikely, they are theoretically possible.
-   Requires careful maintenance of active/dead trie paths.
-   Hash normalization and substring indexing are easy sources of
    implementation errors.

------------------------------------------------------------------------

# Why Aho-Corasick Rebuilding Is Too Slow

A natural idea is to build an Aho-Corasick automaton from all current
strings.

The difficulty is that type-2 queries dynamically extend patterns.

Repeatedly rebuilding an automaton containing hundreds of thousands of
characters can become too expensive.

Even rebuilding once every fixed block of queries can lead to many
complete reconstructions.

The dynamic trie approach avoids this entirely:

``` text
append character
      |
      v
follow/create one trie child
      |
      v
move S[i] endpoint
```

This directly uses the special update structure of the problem.

------------------------------------------------------------------------

# Important Implementation Detail: Avoid Recursive DFS

An earlier version used recursive trie traversal.

That can fail when the trie contains a very deep chain, for example when
one string has hundreds of thousands of characters.

Such recursion may cause:

``` text
Runtime Error / Stack Overflow
```

even though the algorithm is otherwise correct.

The final solution therefore uses explicit stacks:

``` cpp
vector<State> st;
```

and:

``` cpp
vector<int> st;
```

for initialization and dead-node propagation respectively.

This makes the implementation safe for deep trie structures.
