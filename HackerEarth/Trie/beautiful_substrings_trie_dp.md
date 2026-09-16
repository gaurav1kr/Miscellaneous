# Beautiful Substrings --- Distinct Prefixes + Trie DP

## Problem Summary

We are given `N` strings consisting only of `'a'` and `'b'`.

A string is **beautiful** if it can be split completely into one or more
substrings such that every part:

-   starts with `'b'`,
-   ends with `'b'`,
-   contains only `'a'` characters in between.

So each block has the form:

``` text
b a* b
```

Examples of beautiful strings:

``` text
bab
bb
baab
baaabbabbbbaab
```

Examples that are not beautiful:

``` text
baa
bbb
b
baabab
```

Emil considers **all distinct prefixes** of all input strings. For every
distinct prefix, he counts all beautiful substrings contained in it and
sums those counts.

Return the answer modulo:

``` text
1,000,000,007
```

Constraints include:

``` text
1 <= N <= 10^5
1 <= |Si| <= 10^5
sum(|Si|) <= 2 * 10^6
```

------------------------------------------------------------------------

## Sample

``` text
3
bb
ab
bbabaa
```

Distinct prefixes:

``` text
b       -> 0
a       -> 0
ab      -> 0
bb      -> 1
bba     -> 1
bbab    -> 2
bbaba   -> 2
bbabaa  -> 2
```

Therefore:

``` text
answer = 8
```

------------------------------------------------------------------------

# Important Warning: Counting Only the Number of `b`s Is Wrong

A tempting formula is:

``` text
floor(B / 2) * ceil(B / 2)
```

where `B` is the number of `b`s in the prefix.

That is **not correct**.

The reason is that a beautiful substring must be splittable into
**contiguous valid blocks**:

``` text
b a* b | b a* b | ...
```

The blocks must touch each other. We cannot leave an `'a'` between two
blocks.

For example:

``` text
bababb
```

contains four `b`s, but the whole string is not beautiful.

So merely knowing the number of `b`s is insufficient.

We need some DP state describing how beautiful substrings can end near
the most recent `b`.

------------------------------------------------------------------------

# Observation 1: Distinct Prefixes Suggest a Trie

Across many input strings, the same prefix may occur several times.

For example:

``` text
bb
bbabaa
```

both contain:

``` text
b
bb
```

as prefixes.

They must be counted only once.

A trie handles this naturally:

> Every trie node corresponds to exactly one distinct prefix.

Therefore, while inserting all strings:

-   an existing node represents a prefix already counted,
-   a newly created node represents a new distinct prefix.

We calculate and add the contribution only when a new trie node is
created.

Because the alphabet contains only `'a'` and `'b'`, every node has at
most two children.

------------------------------------------------------------------------

# Observation 2: DP State for a Prefix

For every trie node / prefix, maintain four pieces of information.

## `total`

``` text
total = total number of beautiful substrings contained in this prefix
```

This is the value that contributes to Emil's final answer.

------------------------------------------------------------------------

## `ending`

``` text
ending = number of beautiful substrings ending exactly
         at the last character of this prefix
```

If the prefix ends in `'a'`:

``` text
ending = 0
```

because every beautiful string must end in `'b'`.

------------------------------------------------------------------------

## `beforeLastB`

Let the most recent `b` in the prefix be at position `p`.

Then:

``` text
beforeLastB =
    number of beautiful substrings ending exactly at position p - 1
```

This state becomes important when we encounter the next `b`.

------------------------------------------------------------------------

## `hasB`

``` text
hasB = whether this prefix contains at least one 'b'
```

This tells us whether a new `'b'` has a previous `'b'` available to form
a block.

------------------------------------------------------------------------

# Transition When Appending `'a'`

Suppose the current prefix is `P` and we create:

``` text
P + 'a'
```

A beautiful substring cannot end at this new character because every
beautiful string must end with `'b'`.

Therefore:

``` text
newEnding = 0
```

No new beautiful substring is created, so:

``` text
newTotal = oldTotal
```

The most recent `b` has not changed, therefore:

``` text
newBeforeLastB = oldBeforeLastB
newHasB        = oldHasB
```

So the transition is:

``` cpp
next.total       = cur.total;
next.ending      = 0;
next.beforeLastB = cur.beforeLastB;
next.hasB        = cur.hasB;
```

------------------------------------------------------------------------

# Transition When Appending `'b'`

This is the key part.

Suppose we append a new `'b'`.

If there is no previous `b`, no beautiful substring can end here:

``` text
newEnding = 0
```

Otherwise consider the **previous `b`**.

Because it is the previous occurrence of `b`, every character between it
and the current `b` must be `'a'`.

Therefore:

``` text
previous-b + a* + current-b
```

always forms one valid beautiful block.

That contributes:

``` text
1
```

new beautiful substring.

But we may also attach this new block to an already beautiful substring
ending **immediately before the previous `b`**.

The number of such strings is exactly:

``` text
beforeLastB
```

Therefore:

``` text
newEnding = 1 + beforeLastB
```

when a previous `b` exists.

So:

``` cpp
if (cur.hasB)
    newEnding = 1 + cur.beforeLastB;
else
    newEnding = 0;
```

Since these are exactly the newly created beautiful substrings:

``` text
newTotal = oldTotal + newEnding
```

------------------------------------------------------------------------

# Why `beforeLastB` Becomes `parent.ending`

After appending the new `'b'`, this new character becomes the most
recent `b`.

For future transitions, we need to remember how many beautiful
substrings ended immediately before this new `b`.

The character immediately before the new `b` is exactly the final
character of the parent prefix.

Therefore:

``` text
newBeforeLastB = parent.ending
```

This gives:

``` cpp
next.beforeLastB = cur.ending;
```

This small state transition is the central trick of the problem.

------------------------------------------------------------------------

# DP Transitions Summary

## Append `'a'`

``` text
total       = parent.total
ending      = 0
beforeLastB = parent.beforeLastB
hasB        = parent.hasB
```

## Append `'b'`

If there was a previous `b`:

``` text
ending = 1 + parent.beforeLastB
```

otherwise:

``` text
ending = 0
```

Then:

``` text
total       = parent.total + ending
beforeLastB = parent.ending
hasB        = true
```

All arithmetic involving counts is taken modulo `1e9+7`.

------------------------------------------------------------------------

# Sample Walkthrough: `bbabaa`

Start with the empty prefix.

## Prefix `b`

There is no previous `b`.

``` text
ending = 0
total  = 0
```

Contribution:

``` text
0
```

------------------------------------------------------------------------

## Prefix `bb`

There is a previous `b`.

The block:

``` text
bb
```

is beautiful.

``` text
ending = 1
total  = 1
```

Contribution:

``` text
1
```

------------------------------------------------------------------------

## Prefix `bba`

Appending `a` creates nothing new:

``` text
ending = 0
total  = 1
```

Contribution:

``` text
1
```

------------------------------------------------------------------------

## Prefix `bbab`

The previous `b` and current `b` form:

``` text
bab
```

So one new beautiful substring ends here.

Additionally, the earlier:

``` text
bb
```

is already present in the prefix.

Thus:

``` text
ending = 1
total  = 2
```

Contribution:

``` text
2
```

------------------------------------------------------------------------

## Prefix `bbaba`

Appending `a`:

``` text
ending = 0
total  = 2
```

Contribution:

``` text
2
```

------------------------------------------------------------------------

## Prefix `bbabaa`

Appending another `a`:

``` text
ending = 0
total  = 2
```

Contribution:

``` text
2
```

Hence for the sample's distinct prefixes:

``` text
b       -> 0
a       -> 0
ab      -> 0
bb      -> 1
bba     -> 1
bbab    -> 2
bbaba   -> 2
bbabaa  -> 2
```

Total:

``` text
8
```

------------------------------------------------------------------------

# Complete Accepted C++ Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll MOD = 1000000007LL;

struct Node {
    int child[2];

    // Total beautiful substrings in this prefix.
    ll total;

    // Beautiful substrings ending exactly
    // at the last character.
    ll ending;

    // Number of beautiful substrings ending
    // immediately before the most recent 'b'.
    ll beforeLastB;

    bool hasB;

    Node() {
        child[0] = child[1] = -1;
        total = 0;
        ending = 0;
        beforeLastB = 0;
        hasB = false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<Node> trie;

    // Total input length <= 2 * 10^6.
    trie.reserve(2000005);

    // Root represents the empty prefix.
    trie.emplace_back();

    ll answer = 0;

    for (int i = 0; i < N; ++i) {

        string s;
        cin >> s;

        int cur = 0;

        for (char ch : s) {

            int bit = (ch == 'b') ? 1 : 0;

            // New node => new distinct prefix.
            if (trie[cur].child[bit] == -1) {

                int nxt = (int)trie.size();

                trie[cur].child[bit] = nxt;
                trie.emplace_back();

                if (ch == 'a') {

                    // A beautiful substring cannot end with 'a'.
                    trie[nxt].total =
                        trie[cur].total;

                    trie[nxt].ending = 0;

                    // Most recent b remains unchanged.
                    trie[nxt].beforeLastB =
                        trie[cur].beforeLastB;

                    trie[nxt].hasB =
                        trie[cur].hasB;
                }
                else {

                    ll newEnding = 0;

                    if (trie[cur].hasB) {

                        // Previous b + a* + current b
                        // gives one valid block.
                        //
                        // It may also be appended to any
                        // beautiful substring ending immediately
                        // before the previous b.
                        newEnding =
                            1 + trie[cur].beforeLastB;

                        newEnding %= MOD;
                    }

                    trie[nxt].ending =
                        newEnding;

                    trie[nxt].total =
                        (trie[cur].total + newEnding) % MOD;

                    // The current character becomes the new
                    // most recent b. The character immediately
                    // before it is the parent's final character.
                    trie[nxt].beforeLastB =
                        trie[cur].ending;

                    trie[nxt].hasB = true;
                }

                // Every newly created trie node represents
                // exactly one new distinct prefix.
                answer += trie[nxt].total;

                if (answer >= MOD)
                    answer %= MOD;
            }

            cur = trie[cur].child[bit];
        }
    }

    cout << answer % MOD << '\n';

    return 0;
}
```

------------------------------------------------------------------------

# Complexity Analysis

Let:

``` text
L = sum of lengths of all input strings
```

From the constraints:

``` text
L <= 2 * 10^6
```

Every input character is processed once.

Every trie operation is `O(1)` because there are only two children:

``` text
'a'
'b'
```

Therefore:

``` text
Time Complexity: O(L)
```

At most one trie node is created for each input character:

``` text
Space Complexity: O(L)
```

This is suitable for the `1 second` / `256 MB` constraints with a
compact node representation and reserved trie capacity.

------------------------------------------------------------------------

# Why `trie.reserve(2000005)` Helps

The maximum total input length is:

``` text
2 * 10^6
```

So the trie can contain at most approximately:

``` text
2 * 10^6 + 1
```

nodes.

Using:

``` cpp
trie.reserve(2000005);
```

prevents repeated large reallocations and copying as the vector grows.

This is useful under the tight time limit.

------------------------------------------------------------------------

# Common Wrong Approach

A tempting but incorrect solution is to count only the number of `b`s:

``` cpp
(B / 2) * ((B + 1) / 2)
```

This assumes that every suitable pair/group of `b`s forms a beautiful
substring.

That ignores the requirement that the substring must be partitionable
into adjacent blocks:

``` text
b a* b | b a* b | ...
```

The DP state is necessary to enforce this structure.

------------------------------------------------------------------------

# Interview / Competitive Programming Takeaways

This problem combines two ideas.

## 1. Distinct prefixes across many strings

Think:

``` text
Trie
```

Every trie node represents one unique prefix.

------------------------------------------------------------------------

## 2. Count structured substrings incrementally

Instead of recomputing all substrings for every prefix, maintain DP
information while extending a prefix by one character.

The essential states are:

``` text
total
ending
beforeLastB
hasB
```

The most important transition is when adding `'b'`:

``` text
newEnding = 1 + beforeLastB
```

provided a previous `b` exists.

------------------------------------------------------------------------

# Final Pattern

``` text
Many strings
     ↓
Distinct prefixes
     ↓
Trie
     ↓
Each trie node = one unique prefix
     ↓
Maintain DP state along trie edges
     ↓
'a' → creates no new beautiful ending
'b' → 1 + beforeLastB new endings
     ↓
total += newEnding
     ↓
Add node.total once when node is created
     ↓
O(total input length)
```

The key lesson is that **the trie removes duplicate prefixes, while the
DP state counts valid beautiful substrings for each prefix without
enumerating substrings**.
