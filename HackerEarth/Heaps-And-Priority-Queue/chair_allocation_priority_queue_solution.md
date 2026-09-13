# Chair Allocation --- Priority Queue Approach

## Core Idea

Represent every maximal continuous empty block as an interval `[L,R]`.
The next person chooses: 1. the interval with maximum length; 2. on a
tie, the interval with the smallest `L`.

A priority queue maintains exactly this ordering.

For an interval of length `len = R-L+1`: - odd `len`:
`seat = L + len/2`; - even `len`: left middle is `L + len/2 - 1`; choose
it for preference `L`, otherwise choose the next chair.

After choosing `seat`, split the interval into `[L,seat-1]` and
`[seat+1,R]` when non-empty.

## Important Memory Optimization

Do **not** allocate `vector<int>(N+1)` because `N` may be huge. Only `M`
chairs can be occupied, so store:

``` cpp
unordered_map<long long,int> occupied;
```

Use `long long` for chair positions and interval endpoints.

## C++17 Solution

``` cpp
#include <bits/stdc++.h>
using namespace std;

struct Interval {
    long long l, r;
};

struct Compare {
    bool operator()(const Interval& a, const Interval& b) const {
        long long lenA = a.r - a.l + 1;
        long long lenB = b.r - b.l + 1;

        if (lenA != lenB)
            return lenA < lenB;   // larger interval first

        return a.l > b.l;         // leftmost interval first
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N;
    int M;
    cin >> N >> M;

    string preference;
    cin >> preference;

    priority_queue<Interval, vector<Interval>, Compare> pq;

    unordered_map<long long, int> occupied;
    occupied.reserve(2 * M + 10);
    occupied.max_load_factor(0.7);

    if (N > 0)
        pq.push({1, N});

    for (int person = 1; person <= M; ++person) {
        if (pq.empty())
            break;

        Interval cur = pq.top();
        pq.pop();

        long long l = cur.l;
        long long r = cur.r;
        long long len = r - l + 1;
        long long seat;

        if (len & 1LL) {
            seat = l + len / 2;
        } else {
            long long leftMiddle = l + len / 2 - 1;

            if (preference[person - 1] == 'L')
                seat = leftMiddle;
            else
                seat = leftMiddle + 1;
        }

        occupied[seat] = person;

        if (l <= seat - 1)
            pq.push({l, seat - 1});

        if (seat + 1 <= r)
            pq.push({seat + 1, r});
    }

    int Q;
    cin >> Q;

    while (Q--) {
        long long position;
        cin >> position;

        auto it = occupied.find(position);

        if (it == occupied.end())
            cout << -1 << '\n';
        else
            cout << it->second << '\n';
    }

    return 0;
}
```

## Example

For:

``` text
N = 5
M = 3
preferences = RLR
```

Person 1 selects seat `3` from `[1,5]`.

The remaining intervals are `[1,2]` and `[4,5]`.

They have equal length, so Person 2 gets the leftmost interval `[1,2]`.
Preference `L` gives seat `1`.

Person 3 then selects `[4,5]`. Preference `R` gives seat `5`.

Final occupancy:

``` text
Chair:   1   2   3   4   5
Person:  2  -1   1  -1   3
```

## Correctness

The heap always selects the longest empty interval, breaking ties by the
leftmost endpoint. The middle-seat formula implements the required `L/R`
preference. Splitting the selected interval around the occupied chair
preserves exactly the maximal empty intervals for the next person.

## Time Complexity

Each person performs one heap pop and at most two heap pushes:

``` text
O(log M)
```

For all people:

``` text
O(M log M)
```

Each query is an expected `O(1)` hash lookup, so:

``` text
Expected total = O(M log M + Q)
```

## Space Complexity

The heap contains `O(M)` intervals and the hash map contains at most `M`
occupied chairs:

``` text
O(M)
```

This is the critical improvement over an `O(N)` chair array when `N` is
very large.

## Key Takeaway

> Maintain maximal empty intervals in a priority queue, and store only
> occupied chair positions. This gives `O(M log M + Q)` expected time
> and `O(M)` space.
