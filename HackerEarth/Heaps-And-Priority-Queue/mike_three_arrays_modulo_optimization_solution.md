# Mike's Three Arrays --- Event Sweep / Modulo Optimization

## Problem

Mike has three arrays `A`, `B`, and `C`, each of length `N`, and an
integer `K`.

Find the minimum possible value, over all non-negative integers `t`, of:

``` text
max over all i of:

(A[i] + t) % K
+ (B[i] + t) % K
+ (C[i] + t) % K
```

In mathematical form:

\[ `\min`{=tex}*{t `\ge 0`{=tex}} `\max`{=tex}*{1 `\le `{=tex}i
`\le `{=tex}N} `\left`{=tex}( (A_i+t)`\bmod `{=tex}K +
(B_i+t)`\bmod `{=tex}K + (C_i+t)`\bmod `{=tex}K `\right`{=tex}) \]

------------------------------------------------------------------------

## Sample

``` text
N = 3
K = 6

1 4 2
3 5 0
3 3 5
```

For:

``` text
t = 4
```

the three row values are:

``` text
Row 1:
(1+4)%6 + (4+4)%6 + (2+4)%6
= 5 + 2 + 0
= 7

Row 2:
(3+4)%6 + (5+4)%6 + (0+4)%6
= 1 + 3 + 4
= 8

Row 3:
(3+4)%6 + (3+4)%6 + (5+4)%6
= 1 + 1 + 3
= 5
```

Therefore:

``` text
max(7,8,5) = 8
```

which is the minimum achievable answer.

------------------------------------------------------------------------

# Key Observation 1 --- Periodicity

Modulo `K` means:

``` text
f(t + K) = f(t)
```

Therefore we only need to consider:

``` text
0 <= t < K
```

------------------------------------------------------------------------

# Key Observation 2 --- What Happens Between Modulo Wraps?

For a particular row `i`, define:

``` text
f_i(t) =
(A[i]+t)%K
+ (B[i]+t)%K
+ (C[i]+t)%K
```

Initially:

``` text
f_i(0) = A[i] + B[i] + C[i]
```

As `t` increases by one, each of the three components normally increases
by one.

Therefore, while none of them wraps around modulo `K`:

``` text
f_i(t) = current[i] + 3*t
```

where initially:

``` text
current[i] = A[i] + B[i] + C[i]
```

------------------------------------------------------------------------

# Key Observation 3 --- Wrap Events

A value `x` wraps when:

``` text
x + t = K
```

so its wrap time is:

``` text
t = K - x
```

At that point:

``` text
(x+t) % K
```

drops by exactly `K`.

Therefore when one component of row `i` wraps, we can simply update:

``` cpp
current[i] -= K;
```

If two components wrap at the same time:

``` cpp
current[i] -= 2*K;
```

and similarly for three components.

------------------------------------------------------------------------

# Key Observation 4 --- Only Event Times Matter

Between two consecutive wrap events, every row has slope:

``` text
+3
```

because all three modulo terms increase by one.

Hence:

``` text
max_i f_i(t)
=
3*t + max_i current[i]
```

Between events, `current[i]` does not change, so this expression
strictly increases with `t`.

Therefore a minimum cannot occur somewhere in the middle between two
events.

We only need to check:

``` text
t = 0
```

and every modulo wrap event.

There are at most:

``` text
3*N
```

such events.

This converts a potentially huge search over `t` into an `O(N)` number
of candidate points.

------------------------------------------------------------------------

# Maintaining the Maximum Row

At every event we need:

``` text
max(current[i])
```

and some row values change by `-K`.

A `multiset<long long>` supports:

``` text
insert      O(log N)
erase       O(log N)
maximum     O(1) using rbegin()
```

So we keep every `current[i]` in a multiset.

When row `i` changes:

1.  erase its old value;
2.  subtract `K`;
3.  insert its new value.

Then:

``` cpp
*values.rbegin()
```

is the maximum adjusted row value.

The actual objective at time `t` is:

``` cpp
*values.rbegin() + 3LL * t
```

------------------------------------------------------------------------

# Important Detail --- Simultaneous Events

Multiple values may wrap at exactly the same `t`.

For example, a row may contain:

``` text
3 3 5
```

With:

``` text
K = 6
```

both `3`s wrap at:

``` text
t = 3
```

We must process **all events with the same `t` first**, and only then
calculate the candidate answer.

Otherwise we would evaluate an impossible intermediate state.

------------------------------------------------------------------------

# C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

struct Event
{
    int t;
    int row;

    bool operator<(const Event& other) const
    {
        return t < other.t;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;

    cin >> n >> k;

    vector<long long> cur(n);

    vector<Event> events;
    events.reserve(3LL * n);

    for (int i = 0; i < n; ++i)
    {
        long long a, b, c;
        cin >> a >> b >> c;

        cur[i] = a + b + c;

        // For x > 0, x wraps inside the interval
        // 1 <= t < k at t = k-x.
        //
        // x = 0 wraps at t = k, which is equivalent
        // to t = 0 because of modulo periodicity.

        if (a > 0)
            events.push_back({(int)(k - a), i});

        if (b > 0)
            events.push_back({(int)(k - b), i});

        if (c > 0)
            events.push_back({(int)(k - c), i});
    }

    // Sort all wrap events by time.
    sort(events.begin(), events.end());

    // Store the current adjusted value of every row.
    multiset<long long> values;

    for (long long x : cur)
        values.insert(x);

    // Candidate t = 0.
    long long answer = *values.rbegin();

    int m = (int)events.size();

    // Sweep through all wrap events.
    for (int p = 0; p < m; )
    {
        int q = p;
        int t = events[p].t;

        // Process ALL events occurring at the same t
        // before evaluating the objective.
        while (q < m && events[q].t == t)
        {
            int row = events[q].row;

            // Remove the old adjusted value.
            auto it = values.find(cur[row]);
            values.erase(it);

            // One component of this row wrapped.
            cur[row] -= k;

            // Insert the updated adjusted value.
            values.insert(cur[row]);

            ++q;
        }

        // Actual maximum at this t:
        //
        // max_i(current[i] + 3*t)
        // = max_i(current[i]) + 3*t

        long long current =
            *values.rbegin() + 3LL * t;

        answer = min(answer, current);

        p = q;
    }

    cout << answer << '\n';

    return 0;
}
```

------------------------------------------------------------------------

# Sample Walkthrough

Consider:

``` text
3 6

1 4 2
3 5 0
3 3 5
```

Initially:

``` text
current[0] = 1 + 4 + 2 = 7
current[1] = 3 + 5 + 0 = 8
current[2] = 3 + 3 + 5 = 11
```

At:

``` text
t = 0
```

the maximum is:

``` text
11
```

Now consider the wrap events.

For example:

``` text
value 5 -> wraps at t = 1
value 4 -> wraps at t = 2
value 3 -> wraps at t = 3
value 2 -> wraps at t = 4
value 1 -> wraps at t = 5
```

At every event, the corresponding row's adjusted value drops by `K = 6`.

After processing the events at:

``` text
t = 4
```

the actual row values become:

``` text
7, 8, 5
```

so:

``` text
maximum = 8
```

This is the minimum.

Output:

``` text
8
```

------------------------------------------------------------------------

# Correctness Reasoning

For each row, between modulo wrap points:

``` text
f_i(t) = current[i] + 3*t
```

All rows therefore have the same slope `+3`.

Consequently:

``` text
max_i f_i(t)
```

also increases between consecutive events.

Its value can decrease only when one or more modulo components wrap and
cause a `-K` jump.

Therefore a global minimum must occur either:

``` text
t = 0
```

or immediately at one of the wrap events.

The algorithm examines exactly these candidate times.

At each event time, it processes every simultaneous wrap and maintains
the exact maximum row value using the multiset.

Therefore the minimum recorded by the sweep is the globally minimal
achievable value.

------------------------------------------------------------------------

# Time Complexity

There are at most:

``` text
3N
```

events.

Creating the events:

``` text
O(N)
```

Sorting:

``` text
O(N log N)
```

Each event performs one multiset erase and one insertion:

``` text
O(log N)
```

Across all events:

``` text
O(N log N)
```

Therefore:

``` text
Time = O(N log N)
```

------------------------------------------------------------------------

# Space Complexity

We store:

``` text
N current row values
at most 3N events
N values in the multiset
```

Therefore:

``` text
Space = O(N)
```

------------------------------------------------------------------------

# Problem-Solving Thought Process

``` text
Modulo expression over arbitrary t
             |
             v
Modulo K makes function periodic
             |
             v
Only need 0 <= t < K
             |
             v
Between wraps every term increases linearly
             |
             v
Each row has slope +3
             |
             v
Wrap of one component causes -K jump
             |
             v
Minimum can occur only at wrap events
             |
             v
At most 3N candidate events
             |
             v
Sort events
             |
             v
Maintain max current[i]
             |
             v
multiset
             |
             v
Event sweep in O(N log N)
```

------------------------------------------------------------------------

# Key Takeaway

The crucial transformation is:

``` text
f_i(t) = current[i] + 3*t
```

where `current[i]` changes only when one of the row's three values wraps
modulo `K`.

Since all rows have the same slope between events, the maximum also
increases between events. Thus only the at-most `3N` wrap times need to
be evaluated.

Final complexity:

``` text
Time  : O(N log N)
Space : O(N)
```
