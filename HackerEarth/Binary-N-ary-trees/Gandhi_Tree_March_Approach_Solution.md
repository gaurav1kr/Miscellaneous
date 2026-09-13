# Gandhi Tree March --- Problem, Approach, and Solution

## 1. Problem in Simple Words

The problem gives us a **binary tree encoded as a string**.

We need to find all people/nodes that lie in a requested **vertical
column `C`** of the tree and print their IDs in sorted order.

Think of the root as being at column `0`.

-   Going to a **left child** decreases the column by `1`.
-   Going to a **right child** increases the column by `1`.

For example:

``` text
              A(0)
             /    \
         B(-1)    C(+1)
         /  \      /  \
     D(-2) E(0)  F(0) G(+2)
```

Therefore:

``` text
Column -2 -> D
Column -1 -> B
Column  0 -> A, E, F
Column +1 -> C
Column +2 -> G
```

If the requested column is `C = 0`, the relevant nodes are `A`, `E`, and
`F`.

The result must then be sorted according to the problem requirements.

------------------------------------------------------------------------

## 2. Understanding the Serialized Tree

The main confusing part of the problem is that the tree is not provided
using normal edges or `TreeNode` objects.

Instead, the complete tree is represented as a string.

Conceptually, the format is:

``` text
NODE(LEFT_SUBTREE RIGHT_SUBTREE)
```

A dot:

``` text
.
```

represents a `NULL` child.

### Example

``` text
B(..)
```

means:

``` text
      B
     / \
  NULL NULL
```

Similarly:

``` text
A(B(..)C(..))
```

represents:

``` text
       A
      / \
     B   C
```

A larger example:

``` text
A(B(..)C(D(..)E(..)))
```

represents:

``` text
       A
      / \
     B   C
        / \
       D   E
```

------------------------------------------------------------------------

## 3. Converting the Story into a Standard Problem

Ignore the story around Gandhi and people for a moment.

The underlying computer-science problem is:

> Given a serialized binary tree and a column `C`, find all nodes whose
> horizontal distance from the root equals `C`.

This is closely related to **vertical traversal of a binary tree**.

We define:

``` text
root column = 0
```

For any node at column `x`:

``` text
left child  = x - 1
right child = x + 1
```

For example:

``` text
       A(0)
      /    \
   B(-1)   C(+1)
           /   \
        D(0)   E(+2)
```

For `C = 0`, we collect:

``` text
A, D
```

------------------------------------------------------------------------

## 4. Initial / Straightforward Approach

A natural first approach is:

1.  Parse the serialized string.
2.  Construct the binary tree.
3.  Run DFS on the tree.
4.  Keep the current horizontal column during DFS.
5.  Collect nodes whose column equals `C`.
6.  Sort the collected IDs.

The DFS would conceptually be:

``` text
DFS(node, column):

    if node is NULL:
        return

    if column == C:
        add node to answer

    DFS(node.left,  column - 1)
    DFS(node.right, column + 1)
```

This approach works.

However, we can simplify it.

------------------------------------------------------------------------

## 5. Key Optimization

Ask:

> Do we actually need to construct the binary tree?

The answer is **no**.

Consider:

``` text
A(B(..)C(D(..)E(..)))
```

While parsing the string, we already know where every node is located.

Start with:

``` text
A -> column 0
```

When entering A's left subtree:

``` text
B -> column -1
```

When entering A's right subtree:

``` text
C -> column +1
```

When entering C's left subtree:

``` text
D -> 1 - 1 = 0
```

Therefore, while parsing the serialized tree, we can simultaneously
calculate the column.

This lets us combine:

``` text
Tree Parsing + DFS + Column Calculation
```

into one recursive function.

We do **not** need to allocate `TreeNode` objects.

------------------------------------------------------------------------

## 6. Recursive Parsing Idea

Maintain an index:

``` cpp
int idx;
```

which tells us our current position in the serialized string.

Define:

``` text
parse(column)
```

to mean:

> Parse the subtree beginning at the current string position, assuming
> its root is at `column`.

There are two cases.

### Case 1: NULL node

If the current character is:

``` text
.
```

there is no node.

So:

``` text
move idx forward
return
```

### Case 2: Real node

Read the current person's ID.

If:

``` text
column == targetColumn
```

add that person to the answer.

Then recursively parse:

``` text
left subtree  -> column - 1
right subtree -> column + 1
```

------------------------------------------------------------------------

## 7. Dry Run

Consider:

``` text
A(B(..)C(D(..)E(..)))
```

and:

``` text
target column = 0
```

### Root

``` text
A -> column 0
```

Target is `0`, therefore:

``` text
answer = [A]
```

### A's Left Child

``` text
B -> column -1
```

Not required.

### A's Right Child

``` text
C -> column +1
```

Not required.

### C's Left Child

``` text
D -> column 0
```

Required:

``` text
answer = [A, D]
```

### C's Right Child

``` text
E -> column +2
```

Not required.

Final result:

``` text
A, D
```

After sorting, print the required output.

------------------------------------------------------------------------

## 8. C++ Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

string s;
int idx;
int targetColumn;
string answer;

void parseTree(int column)
{
    // NULL node
    if (s[idx] == '.')
    {
        idx++;
        return;
    }

    // Read current person/node
    char person = s[idx++];

    // Check whether this node belongs to the requested column
    if (column == targetColumn)
    {
        answer.push_back(person);
    }

    // Skip '('
    idx++;

    // Parse left subtree
    parseTree(column - 1);

    // Parse right subtree
    parseTree(column + 1);

    // Skip ')'
    idx++;
}

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        cin >> targetColumn >> s;

        idx = 0;
        answer.clear();

        // Root starts at column 0
        parseTree(0);

        if (answer.empty())
        {
            cout << "Common Gandhijee!" << '\n';
        }
        else
        {
            sort(answer.begin(), answer.end());
            cout << answer << '\n';
        }
    }

    return 0;
}
```

> Note: Always verify the exact input order and required empty-result
> text against the current HackerEarth problem statement before
> submission.

------------------------------------------------------------------------

## 9. Complexity Analysis

Let:

-   `N` = size of the serialized tree / number of elements processed
-   `K` = number of people found in the requested column
-   `H` = height of the tree

### Parsing

Every part of the tree is visited once:

``` text
O(N)
```

### Sorting

We sort only the matching people:

``` text
O(K log K)
```

### Overall Time

``` text
O(N + K log K)
```

### Space

We do not construct a separate binary tree.

The main additional space is the recursion stack:

``` text
O(H)
```

plus the output collection.

------------------------------------------------------------------------

## 10. Interview Thought Process

A good way to explain the solution in an interview is:

1.  Recognize that the problem is asking about **vertical columns in a
    binary tree**.
2.  Assign horizontal distance `0` to the root.
3.  A left move changes the distance by `-1`.
4.  A right move changes the distance by `+1`.
5.  Notice that the input itself is recursively serialized.
6.  Use recursion to parse it.
7.  Carry the current horizontal distance as part of the recursive
    state.
8.  Collect a node whenever its horizontal distance equals `C`.
9.  Sort the collected IDs.
10. Avoid constructing the tree because the serialized input already
    provides the traversal structure.

------------------------------------------------------------------------

## 11. Main Insight to Remember

The most important observation is:

> **The serialized input already gives us a DFS traversal of the tree.
> Therefore, we can calculate each node's horizontal distance while
> parsing the string and avoid constructing the actual binary tree.**

This turns the problem into:

``` text
Recursive Parsing
        +
Horizontal Distance Tracking
        +
Collect Matching Nodes
        +
Sorting
```

That is the core approach to **Gandhi Tree March**.
