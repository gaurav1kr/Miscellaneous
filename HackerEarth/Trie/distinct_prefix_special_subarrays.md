# Distinct Prefixes and Special Subarrays --- Binary Trie

## Problem Summary

We are given multiple binary arrays represented as strings.

Sam writes down **all distinct prefixes** of all the given binary
arrays. If the same prefix occurs in multiple arrays, it is written only
once.

For every distinct prefix, Sam counts the number of **special
subarrays** contained in that prefix and adds all these counts together.

From the sample and explanation, a special subarray is of the form:

``` text
0 1 1 1 ... 1 0
```

That is:

-   its length is greater than `1`,
-   it starts with `0`,
-   it ends with `0`,
-   every element strictly between the two endpoints is `1`.

The final answer must be printed modulo the modulus specified in the
original problem statement.

> Note: The copied problem statement contains missing `svg` symbols,
> including the modulus. Replace `MOD` in the code with the exact
> modulus from the original HackerEarth statement if it differs.

------------------------------------------------------------------------

# Sample

Input:

``` text
3
00
10
001011
```

The distinct prefixes are:

``` text
0
1
10
00
001
0010
00101
001011
```

The number of special subarrays in each is:

``` text
0       -> 0
1       -> 0
10      -> 0
00      -> 1
001     -> 1
0010    -> 2
00101   -> 2
001011  -> 2
```

Therefore:

``` text
0 + 0 + 0 + 1 + 1 + 2 + 2 + 2 = 8
```

Answer:

``` text
8
```

------------------------------------------------------------------------

# Observation 1: Count Special Subarrays Using Zeros

Consider a binary prefix.

A special subarray has the structure:

``` text
0 1* 0
```

where `1*` means zero or more `1`s.

Suppose the zero positions are:

``` text
z1, z2, z3, ..., zk
```

Every pair of **consecutive zeros** forms exactly one special subarray.

Why?

Between two consecutive zeros there cannot be another zero. Since the
array is binary, everything between them must therefore be `1`.

For example:

``` text
001011
```

Zero positions are:

``` text
1, 2, 4
```

The consecutive-zero pairs are:

``` text
(1, 2)
(2, 4)
```

They produce:

``` text
00
010
```

So there are:

``` text
2
```

special subarrays.

------------------------------------------------------------------------

# Formula

If a prefix contains `Z` zeros:

``` text
specialSubarrays = max(0, Z - 1)
```

Examples:

``` text
Prefix     Number of zeros     Special subarrays

0                 1                    0
00                2                    1
001               2                    1
0010              3                    2
00101             3                    2
001011            3                    2
```

This matches the sample exactly.

------------------------------------------------------------------------

# Observation 2: We Need Distinct Prefixes

The input contains multiple binary strings.

Suppose we have:

``` text
001
001011
```

Their prefixes overlap:

``` text
001 prefixes:
0
00
001

001011 prefixes:
0
00
001
0010
00101
001011
```

But Sam writes each distinct prefix only once.

Therefore:

``` text
0
00
001
```

must not be counted twice.

This strongly suggests using a **Trie**.

------------------------------------------------------------------------

# Why a Trie Works

In a trie:

``` text
root
 |
 +-- 0
 |   |
 |   +-- 0
 |       |
 |       +-- 1
 |
 +-- 1
```

Every trie node corresponds to exactly one distinct prefix.

For example, a path:

``` text
root -> 0 -> 0 -> 1
```

represents:

``` text
001
```

Therefore:

> Number of unique prefixes = number of trie nodes excluding the root.

More importantly, when inserting a string:

-   if a child already exists, that prefix has already been seen,
-   if a child does not exist, creating it means we have discovered a
    new distinct prefix.

We should add to the answer **only when a new trie node is created**.

------------------------------------------------------------------------

# Information Stored in Each Trie Node

For each node, store:

``` text
zeros = number of zeros on the path from root to this node
```

If the parent represents a prefix containing `Z` zeros:

### Adding `1`

The new prefix still has:

``` text
Z
```

zeros.

### Adding `0`

The new prefix has:

``` text
Z + 1
```

zeros.

So:

``` cpp
newZeros = parentZeros + (bit == 0);
```

The contribution of the new prefix is:

``` cpp
max(0, newZeros - 1)
```

------------------------------------------------------------------------

# Complete Algorithm

Initialize a trie containing only the root.

Also initialize:

``` text
answer = 0
```

For every binary string:

1.  Start at the root.
2.  Process characters from left to right.
3.  For each bit:
    -   check whether the corresponding child exists,
    -   if it does not exist:
        -   create a new node,
        -   calculate its number of zeros,
        -   calculate its number of special subarrays,
        -   add this contribution to `answer`.
    -   move to that child.
4.  Continue with the next string.

Finally print:

``` text
answer % MOD
```

------------------------------------------------------------------------

# Sample Walkthrough

Input:

``` text
00
10
001011
```

## Insert `00`

Create prefix:

``` text
0
```

Zeros:

``` text
1
```

Contribution:

``` text
max(0, 1 - 1) = 0
```

Create prefix:

``` text
00
```

Zeros:

``` text
2
```

Contribution:

``` text
2 - 1 = 1
```

Running answer:

``` text
1
```

------------------------------------------------------------------------

## Insert `10`

Create:

``` text
1
```

Zeros:

``` text
0
```

Contribution:

``` text
0
```

Create:

``` text
10
```

Zeros:

``` text
1
```

Contribution:

``` text
0
```

Running answer:

``` text
1
```

------------------------------------------------------------------------

## Insert `001011`

Prefixes:

``` text
0
00
```

already exist, so they are not counted again.

Create:

``` text
001
```

Zeros:

``` text
2
```

Contribution:

``` text
1
```

Running answer:

``` text
2
```

Create:

``` text
0010
```

Zeros:

``` text
3
```

Contribution:

``` text
2
```

Running answer:

``` text
4
```

Create:

``` text
00101
```

Zeros:

``` text
3
```

Contribution:

``` text
2
```

Running answer:

``` text
6
```

Create:

``` text
001011
```

Zeros:

``` text
3
```

Contribution:

``` text
2
```

Running answer:

``` text
8
```

Final answer:

``` text
8
```

------------------------------------------------------------------------

# C++ Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

// IMPORTANT:
// Replace this with the modulus given in the original problem
// if the original value is different.
const ll MOD = 1000000007LL;

struct Node {
    int child[2];
    int zeros;

    Node() {
        child[0] = child[1] = -1;
        zeros = 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<Node> trie;

    // Root node.
    trie.emplace_back();

    ll answer = 0;

    for (int i = 0; i < N; ++i) {

        string s;
        cin >> s;

        int cur = 0;

        for (char ch : s) {

            int bit = ch - '0';

            // This child does not exist, so this is
            // a new distinct prefix.
            if (trie[cur].child[bit] == -1) {

                int newNode = (int)trie.size();

                trie[cur].child[bit] = newNode;

                trie.emplace_back();

                // Calculate the number of zeros
                // in this new prefix.
                trie[newNode].zeros =
                    trie[cur].zeros + (bit == 0);

                // Number of special subarrays in this prefix.
                ll special =
                    max(0, trie[newNode].zeros - 1);

                answer += special;
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
L = total length of all input binary strings
```

Every character is processed exactly once during trie insertion.

Trie operations take constant time because every node has only two
possible children:

``` text
0
1
```

Therefore:

``` text
Time Complexity = O(L)
```

At most one trie node is created for every input character.

Therefore:

``` text
Space Complexity = O(L)
```

------------------------------------------------------------------------

# Why We Do Not Generate Every Prefix Explicitly

A naive approach could generate every prefix as a separate string and
insert it into a set.

For example:

``` text
001011
```

would generate:

``` text
0
00
001
0010
00101
001011
```

Copying strings repeatedly can make the solution unnecessarily
expensive.

A trie naturally represents all prefixes without repeatedly copying
them.

For a binary alphabet, it is particularly efficient because every node
needs only:

``` text
child[0]
child[1]
```

------------------------------------------------------------------------

# Important Insight: Why Only Consecutive Zeros Matter

Suppose we have:

``` text
0 1 0 1 0
```

Zero positions are:

``` text
1, 3, 5
```

Valid special subarrays are:

``` text
positions 1..3 -> 010
positions 3..5 -> 010
```

But positions `1..5` give:

``` text
01010
```

which is not special because there is another `0` inside it.

Therefore only consecutive zeros can form a special subarray.

With `Z` zeros, the number of consecutive-zero pairs is:

``` text
Z - 1
```

Hence:

``` text
special = max(0, Z - 1)
```

------------------------------------------------------------------------

# Interview / Problem-Solving Takeaway

This problem combines two independent observations.

## 1. Simplify the Subarray Condition

Instead of enumerating subarrays, recognize:

``` text
special subarray = consecutive zero pair
```

Therefore:

``` text
special count = number of zeros - 1
```

for prefixes containing at least one zero.

## 2. Distinct Prefixes Suggest a Trie

When multiple strings share prefixes and each unique prefix must be
processed exactly once:

``` text
Trie
```

is a natural data structure.

Every newly created trie node represents exactly one previously unseen
prefix.

------------------------------------------------------------------------

# Final Pattern

``` text
Multiple Binary Strings
          ↓
Need Distinct Prefixes
          ↓
Binary Trie
          ↓
Each New Trie Node = New Prefix
          ↓
Track Number of Zeros Along Path
          ↓
Special Count = max(0, zeros - 1)
          ↓
Add Contribution Once
          ↓
O(Total Input Length)
```

This reduces what initially looks like a combination of prefix
enumeration and subarray counting into a single linear-time trie
traversal.
