# Operation Dilemma --- HackerEarth

## Problem Summary

You are given two integer arrays `A` and `B` of size `N`.

For every index `i`, you may choose either:

``` text
A[i] + B[i]
```

or:

``` text
A[i] - B[i]
```

You are allowed to choose the **addition operation at most `K` times**.

Among all subarrays of length `L`, find the **largest possible sum**
after making the optimal choices.

------------------------------------------------------------------------

## Key Observation

Consider a fixed window of length `L`.

Start by choosing subtraction at every position:

``` text
A[i] - B[i]
```

Therefore the base value of the window is:

``` text
baseSum = Σ(A[i] - B[i])
```

Now suppose we change index `i` from subtraction to addition.

The improvement is:

``` text
(A[i] + B[i]) - (A[i] - B[i])
= 2 * B[i]
```

So choosing the add operation at index `i` changes the sum by:

``` text
2 * B[i]
```

Because we can use at most `K` add operations, the optimal strategy is
to select the **K largest positive values of `B[i]` in the current
window**.

We never select a non-positive `B[i]`, because it would not improve the
answer.

Thus:

``` text
Window Answer
=
Σ(A[i] - B[i])
+
2 * sum(K largest positive B[i])
```

This is the central observation of the problem.

------------------------------------------------------------------------

## Sliding Window

There are `N-L+1` possible windows of length `L`.

Recomputing the K largest values independently for every window would be
too expensive.

Instead, slide the window one position at a time.

When moving from one window to the next:

1.  Remove the old leftmost element.
2.  Add the new rightmost element.
3.  Update the base sum.
4.  Update the K largest positive `B` values.
5.  Calculate the current answer.

------------------------------------------------------------------------

## Maintaining the K Largest Values

Use two multisets:

``` text
high = K largest positive B values in the window
low  = all remaining positive B values
```

Also maintain:

``` text
sumHigh = sum of all elements in high
```

Then:

``` text
currentAnswer = baseSum + 2 * sumHigh
```

### Invariants

We maintain:

``` text
high.size() <= K
```

and whenever enough positive elements exist:

``` text
high.size() == K
```

Also:

``` text
every element in high >= every element in low
```

Therefore `high` always contains exactly the K largest useful values.

------------------------------------------------------------------------

## C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

class TopK
{
private:
    // high contains the K largest positive values.
    multiset<long long> high;

    // low contains all remaining positive values.
    multiset<long long> low;

    long long sumHigh = 0;
    int K;

    void rebalance()
    {
        // high must contain at most K elements.
        while ((int)high.size() > K)
        {
            auto it = high.begin();

            long long x = *it;

            sumHigh -= x;
            high.erase(it);

            low.insert(x);
        }

        // If high contains fewer than K values,
        // move the largest values from low.
        while ((int)high.size() < K && !low.empty())
        {
            auto it = prev(low.end());

            long long x = *it;

            low.erase(it);

            high.insert(x);
            sumHigh += x;
        }

        // Ensure every element in high is at least
        // as large as every element in low.
        while (!high.empty() && !low.empty())
        {
            auto smallestHigh = high.begin();
            auto largestLow = prev(low.end());

            if (*smallestHigh >= *largestLow)
                break;

            long long a = *smallestHigh;
            long long b = *largestLow;

            sumHigh -= a;
            sumHigh += b;

            high.erase(smallestHigh);
            low.erase(largestLow);

            high.insert(b);
            low.insert(a);
        }
    }

public:
    TopK(int k) : K(k) {}

    void add(long long x)
    {
        // Non-positive B does not improve the result.
        if (x <= 0)
            return;

        if ((int)high.size() < K)
        {
            high.insert(x);
            sumHigh += x;
        }
        else if (K > 0 && x > *high.begin())
        {
            auto it = high.begin();

            long long smallest = *it;

            high.erase(it);
            sumHigh -= smallest;

            low.insert(smallest);

            high.insert(x);
            sumHigh += x;
        }
        else
        {
            low.insert(x);
        }

        rebalance();
    }

    void remove(long long x)
    {
        if (x <= 0)
            return;

        auto it = high.find(x);

        if (it != high.end())
        {
            sumHigh -= x;
            high.erase(it);
        }
        else
        {
            it = low.find(x);

            if (it != low.end())
                low.erase(it);
        }

        rebalance();
    }

    long long getSum() const
    {
        return sumHigh;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--)
    {
        int N, L, K;
        cin >> N >> L >> K;

        vector<long long> A(N);
        vector<long long> B(N);

        for (auto &x : A)
            cin >> x;

        for (auto &x : B)
            cin >> x;

        TopK topK(K);

        long long baseSum = 0;

        // Build the first window.
        for (int i = 0; i < L; ++i)
        {
            baseSum += A[i] - B[i];
            topK.add(B[i]);
        }

        long long answer =
            baseSum + 2LL * topK.getSum();

        // Slide the window.
        for (int r = L; r < N; ++r)
        {
            int removeIndex = r - L;

            // Remove the old leftmost element.
            baseSum -= A[removeIndex] - B[removeIndex];
            topK.remove(B[removeIndex]);

            // Add the new rightmost element.
            baseSum += A[r] - B[r];
            topK.add(B[r]);

            long long current =
                baseSum + 2LL * topK.getSum();

            answer = max(answer, current);
        }

        cout << answer << '\n';
    }

    return 0;
}
```

------------------------------------------------------------------------

## Example

Input:

``` text
1
5 5 2
1 2 3 4 5
-1 2 3 4 5
```

There is only one window because:

``` text
N = 5
L = 5
```

### Step 1: Subtract B everywhere

``` text
A[i] - B[i]
```

gives:

``` text
1 - (-1) = 2
2 - 2    = 0
3 - 3    = 0
4 - 4    = 0
5 - 5    = 0
```

Therefore:

``` text
baseSum = 2
```

### Step 2: Choose at most K = 2 additions

The positive `B` values are:

``` text
2, 3, 4, 5
```

The two largest are:

``` text
5 and 4
```

Switching these positions from subtraction to addition improves the
answer by:

``` text
2 * (5 + 4)
= 18
```

Therefore:

``` text
answer = 2 + 18
       = 20
```

Output:

``` text
20
```

------------------------------------------------------------------------

## Why Negative B Values Are Ignored

Suppose:

``` text
B[i] = -5
```

The improvement from switching to addition would be:

``` text
2 * B[i]
= -10
```

So the result would become smaller.

Since the problem says **at most K** additions rather than exactly K
additions, there is no reason to choose such an operation.

Therefore only:

``` text
B[i] > 0
```

needs to be stored in the Top-K data structure.

------------------------------------------------------------------------

## Time Complexity

For every element, we perform a constant number of multiset operations.

Each multiset insertion/deletion costs:

``` text
O(log L)
```

Each element enters the sliding window once and leaves it once.

Therefore, for one test case:

``` text
O(N log L)
```

For all test cases:

``` text
O(sum(N) * log L)
```

More generally:

``` text
O(N log N)
```

is also a valid upper bound.

------------------------------------------------------------------------

## Space Complexity

The two multisets together contain at most the positive `B` values of
the current window:

``` text
O(L)
```

The implementation also stores arrays `A` and `B`:

``` text
O(N)
```

Therefore total auxiliary/program data is:

``` text
O(N + L) = O(N)
```

If the arrays were streamed/stored differently, the sliding-window data
structure itself requires only:

``` text
O(L)
```

------------------------------------------------------------------------

## Interview / Problem-Solving Thought Process

``` text
For every i choose:
A[i] + B[i]
or
A[i] - B[i]

        |
        v

Assume subtraction everywhere

        |
        v

Base = Σ(A[i] - B[i])

        |
        v

Changing one index to addition gains:

(A[i] + B[i]) - (A[i] - B[i])

        |
        v

Gain = 2 * B[i]

        |
        v

At most K operations

        |
        v

Choose K largest positive B[i]

        |
        v

Need this for every length-L window

        |
        v

Sliding Window + Dynamic Top-K

        |
        v

Two multisets:
high = top K
low  = remaining

        |
        v

Answer =
baseSum + 2 * sumHigh
```

------------------------------------------------------------------------

## Core Formula

The most important formula to remember is:

``` text
Window Answer
=
sum(A[i] - B[i])
+
2 * sum(K largest positive B[i])
```

Once this transformation is recognized, the original operation problem
becomes a standard **sliding-window Top-K maintenance problem**.
