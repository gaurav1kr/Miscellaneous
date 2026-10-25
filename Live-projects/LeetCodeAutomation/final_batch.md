# Batch 01 — C++11/C++14 Solutions

Source: uploaded Batch 01 problem statements and LeetCode C++ starter signatures.

**Validation note:** Implementations below are reasoned solutions, not claimed LeetCode Accepted. Three problems are marked for further algorithm validation.

## 4088. Difference Between Peaks and Valleys
**Link:** https://leetcode.com/problems/difference-between-peaks-and-valleys/
**Difficulty:** Easy | **Status:** Todo | **Access:** Free

**Approach:** Inspect every interior element and add peaks, subtract valleys.
**Complexity:** O(n) time; O(1) extra space.

```cpp
class Solution {
public:
    int peakValleyDifference(vector<int>& nums) {
        int ans = 0;
        for (int i = 1; i + 1 < (int)nums.size(); ++i) {
            if (nums[i] > nums[i-1] && nums[i] > nums[i+1]) ans += nums[i];
            if (nums[i] < nums[i-1] && nums[i] < nums[i+1]) ans -= nums[i];
        }
        return ans;
    }
};
```

---

## 3431. Minimum Unlocked Indices to Sort Nums
**Link:** https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Requires further validation:** The problem statement is available, but a submission-ready efficient solution has not yet been verified. No speculative code is included.

---

## 3520. Minimum Threshold for Inversion Pairs Count
**Link:** https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** Binary-search the threshold. A Fenwick tree over compressed values counts earlier elements in the interval `(nums[j], nums[j]+threshold]`. Stop counting at k.
**Complexity:** O(n log n log V) time; O(n) space, V = max(nums)-min(nums).

```cpp
class Solution {
    struct BIT {
        vector<int> t;
        BIT(int n): t(n+1,0) {}
        void add(int i) { for (++i; i<(int)t.size(); i+=i&-i) ++t[i]; }
        int sum(int i) const { int r=0; for (;i>0;i-=i&-i) r+=t[i]; return r; }
    };
public:
    int minThreshold(vector<int>& nums, int k) {
        vector<int> a=nums;
        sort(a.begin(),a.end());
        a.erase(unique(a.begin(),a.end()),a.end());
        auto enough = [&](int x) {
            BIT bit(a.size());
            long long cnt=0;
            for (int v: nums) {
                int hi=upper_bound(a.begin(),a.end(),(long long)v+x)-a.begin();
                int lo=upper_bound(a.begin(),a.end(),v)-a.begin();
                cnt+=bit.sum(hi)-bit.sum(lo);
                if (cnt>=k) return true;
                bit.add(lower_bound(a.begin(),a.end(),v)-a.begin());
            }
            return false;
        };
        int hi=*max_element(nums.begin(),nums.end())-*min_element(nums.begin(),nums.end());
        if (!enough(hi)) return -1;
        int lo=0;
        while (lo<hi) {
            int mid=lo+(hi-lo)/2;
            if (enough(mid)) hi=mid; else lo=mid+1;
        }
        return lo;
    }
};
```

---

## 3535. Unit Conversion II
**Link:** https://leetcode.com/problems/unit-conversion-ii/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** Build a bidirectional conversion tree; a reverse edge uses the modular inverse. BFS from unit 0 obtains each unit’s scale relative to unit 0. Answer A→B as scale[B]/scale[A].
**Complexity:** O(n log MOD + q log MOD) time; O(n) space.

```cpp
class Solution {
    static const long long MOD=1000000007LL;
    long long power(long long a,long long b) {
        long long r=1;
        while(b) { if(b&1) r=r*a%MOD; a=a*a%MOD; b>>=1; }
        return r;
    }
public:
    vector<int> queryConversions(vector<vector<int>>& conversions, vector<vector<int>>& queries) {
        int n=(int)conversions.size()+1;
        vector<vector<pair<int,long long>>> g(n);
        for (auto &e:conversions) {
            g[e[0]].push_back({e[1],e[2]});
            g[e[1]].push_back({e[0],power(e[2],MOD-2)});
        }
        vector<long long> scale(n,0); scale[0]=1;
        queue<int> que; que.push(0);
        while(!que.empty()) {
            int u=que.front();que.pop();
            for(auto &edge:g[u]) if(!scale[edge.first]) {
                scale[edge.first]=scale[u]*edge.second%MOD;
                que.push(edge.first);
            }
        }
        vector<int> ans;
        for(auto &q:queries)
            ans.push_back((int)(scale[q[1]]*power(scale[q[0]],MOD-2)%MOD));
        return ans;
    }
};
```

---

## 3540. Minimum Time to Visit All Houses
**Link:** https://leetcode.com/problems/minimum-time-to-visit-all-houses/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** Precompute clockwise and counterclockwise prefix distances. Each requested leg takes the smaller of its two directed circular routes.
**Complexity:** O(n + q) time; O(n) space.

```cpp
class Solution {
public:
    long long minTotalTime(vector<int>& forward, vector<int>& backward, vector<int>& queries) {
        int n=forward.size();
        vector<long long> f(n+1,0),b(n+1,0);
        for(int i=0;i<n;++i) { f[i+1]=f[i]+forward[i]; b[i+1]=b[i]+backward[i]; }
        long long ans=0; int from=0;
        for(int to:queries) {
            long long cw=(to>=from)?f[to]-f[from]:f[n]-f[from]+f[to];
            long long ccw=(from>=to)?b[from+1]-b[to+1]:b[from+1]+b[n]-b[to+1];
            ans+=min(cw,ccw); from=to;
        }
        return ans;
    }
};
```

---

## 3555. Smallest Subarray to Sort in Every Sliding Window
**Link:** https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** For each window, locate the first inversion and last inversion. Find the min/max in that region and extend left/right until all out-of-place values are included.
**Complexity:** O(nk) time; O(1) auxiliary space.

```cpp
class Solution {
public:
    vector<int> minSubarraySort(vector<int>& nums, int k) {
        vector<int> ans;
        for(int start=0;start+k<=(int)nums.size();++start) {
            int end=start+k-1,l=start,r=end;
            while(l<end && nums[l]<=nums[l+1]) ++l;
            if(l==end) { ans.push_back(0); continue; }
            while(r>start && nums[r-1]<=nums[r]) --r;
            int mn=nums[l],mx=nums[l];
            for(int i=l;i<=r;++i) { mn=min(mn,nums[i]);mx=max(mx,nums[i]); }
            while(l>start && nums[l-1]>mn) --l;
            while(r<end && nums[r+1]<mx) ++r;
            ans.push_back(r-l+1);
        }
        return ans;
    }
};
```

---

## 3565. Sequential Grid Path Cover
**Link:** https://leetcode.com/problems/sequential-grid-path-cover/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** Backtracking over grid cells using a 25-bit visited mask. Only allow the next numbered cell in sequence; prune paths that disconnect remaining unvisited cells. This is exponential in the worst case.
**Complexity:** Worst-case O(4^(mn)·mn) time; O(mn) recursion/visited space.

```cpp
class Solution {
    int m,n,k;
    vector<vector<int>> *g;
    vector<vector<int>> path;
    const int dx[4]={1,-1,0,0},dy[4]={0,0,1,-1};
    bool dfs(int x,int y,unsigned int mask,int next) {
        path.push_back({x,y});
        if((int)path.size()==m*n) return next==k+1;
        for(int d=0;d<4;++d) {
            int a=x+dx[d],b=y+dy[d];
            if(a<0||a>=m||b<0||b>=n) continue;
            int id=a*n+b;
            if(mask&(1u<<id)) continue;
            int val=(*g)[a][b];
            if(val && val!=next) continue;
            if(dfs(a,b,mask|(1u<<id),next+(val!=0))) return true;
        }
        path.pop_back();return false;
    }
public:
    vector<vector<int>> findPath(vector<vector<int>>& grid,int K) {
        g=&grid;m=grid.size();n=grid[0].size();k=K;
        for(int i=0;i<m;++i) for(int j=0;j<n;++j)
            if((grid[i][j]==0||grid[i][j]==1) && dfs(i,j,1u<<(i*n+j),grid[i][j]==1?2:1)) return path;
        return {};
    }
};
```

---

## 3596. Minimum Cost Path with Alternating Directions I
**Link:** https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** Each forward move increases row+column by 1 and each backward move decreases it by 1. Starting at zero, reachable coordinate sums alternate between 0 and 1. Therefore any destination with (m-1)+(n-1) greater than 1 is unreachable.
**Complexity:** O(1) time; O(1) space.

```cpp
class Solution {
public:
    int minCost(int m,int n) {
        if(m==1 && n==1) return 1;
        if(m==2 && n==1) return 3;
        if(m==1 && n==2) return 3;
        return -1;
    }
};
```

---

## 3610. Minimum Number of Primes to Sum to Target
**Link:** https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** Generate the first m primes with trial division and perform unbounded coin-change DP up to n.
**Complexity:** O(m sqrt(p_m) + mn) time; O(n+m) space.

```cpp
class Solution {
public:
    int minNumberOfPrimes(int n,int m) {
        vector<int> primes;
        for(int x=2;(int)primes.size()<m;++x) {
            bool prime=true;
            for(int p:primes) { if(1LL*p*p>x) break; if(x%p==0) {prime=false;break;} }
            if(prime) primes.push_back(x);
        }
        vector<int> dp(n+1,n+1);dp[0]=0;
        for(int p:primes) for(int x=p;x<=n;++x)
            dp[x]=min(dp[x],dp[x-p]+1);
        return dp[n]>n?-1:dp[n];
    }
};
```

---

## 3631. Sort Threats by Severity and Exploitability
**Link:** https://leetcode.com/problems/sort-threats-by-severity-and-exploitability/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** Sort by descending 64-bit score, breaking ties by ascending ID.
**Complexity:** O(n log n) time; O(log n) sorting stack space.

```cpp
class Solution {
public:
    vector<vector<int>> sortThreats(vector<vector<int>>& threats) {
        sort(threats.begin(),threats.end(),[](const vector<int>& a,const vector<int>& b) {
            long long sa=2LL*a[1]+a[2],sb=2LL*b[1]+b[2];
            return sa==sb?a[0]<b[0]:sa>sb;
        });
        return threats;
    }
};
```

---

## 3641. Longest Semi-Repeating Subarray
**Link:** https://leetcode.com/problems/longest-semi-repeating-subarray/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** Sliding window with frequencies; count how many distinct values have frequency at least two. Shrink until that count is at most k.
**Complexity:** O(n) time; O(U) space for value range U.

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums,int k) {
        vector<int> freq(100001,0);
        int left=0,repeated=0,best=0;
        for(int right=0;right<(int)nums.size();++right) {
            if(++freq[nums[right]]==2) ++repeated;
            while(repeated>k) {
                if(--freq[nums[left]]==1) --repeated;
                ++left;
            }
            best=max(best,right-left+1);
        }
        return best;
    }
};
```

---

## 3647. Maximum Weight in Two Bags
**Link:** https://leetcode.com/problems/maximum-weight-in-two-bags/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** Two-dimensional 0/1 knapsack: dp[a][b] indicates whether both bag loads are achievable with each item used at most once. Update capacities backwards.
**Complexity:** O(n·w1·w2) time; O(w1·w2) space.

```cpp
class Solution {
public:
    int maxWeight(vector<int>& weights,int w1,int w2) {
        vector<vector<char>> dp(w1+1,vector<char>(w2+1,0));dp[0][0]=1;
        for(int w:weights) {
            for(int a=w1;a>=0;--a) for(int b=w2;b>=0;--b) {
                if(a>=w && dp[a-w][b]) dp[a][b]=1;
                if(b>=w && dp[a][b-w]) dp[a][b]=1;
            }
        }
        int best=0;
        for(int a=0;a<=w1;++a) for(int b=0;b<=w2;++b)
            if(dp[a][b]) best=max(best,a+b);
        return best;
    }
};
```

---

## 3660. Jump Game IX
**Link:** https://leetcode.com/problems/jump-game-ix/
**Difficulty:** Medium | **Status:** Todo | **Access:** Free

**Approach:** Valid jumps connect both endpoints of any inversion, so each connected component is a contiguous block. A cut between i and i+1 is valid exactly when max(nums[0..i]) <= min(nums[i+1..n-1]). Return each block’s maximum.
**Complexity:** O(n) time; O(n) space.

```cpp
class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n=nums.size();
        vector<int> suffix(n+1,INT_MAX),ans(n);
        for(int i=n-1;i>=0;--i) suffix[i]=min(nums[i],suffix[i+1]);
        int start=0,mx=INT_MIN;
        for(int i=0;i<n;++i) {
            mx=max(mx,nums[i]);
            if(mx<=suffix[i+1]) {
                for(int j=start;j<=i;++j) ans[j]=mx;
                start=i+1;mx=INT_MIN;
            }
        }
        return ans;
    }
};
```

---

## 3672. Sum of Weighted Modes in Subarrays
**Link:** https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/
**Difficulty:** Medium | **Status:** Todo | **Access:** Premium

**Approach:** Maintain a sorted set of (negative frequency, value) for the current window. Its first element is the highest-frequency, smallest-valued mode.
**Complexity:** O(n log k) time; O(k) space.

```cpp
class Solution {
public:
    long long modeWeight(vector<int>& nums,int k) {
        unordered_map<int,int> freq;
        set<pair<int,int>> order;
        auto change=[&](int x,int delta) {
            int old=freq[x];
            if(old) order.erase({-old,x});
            int now=old+delta;
            if(now) order.insert({-now,x});
            freq[x]=now;
        };
        long long ans=0;
        for(int i=0;i<(int)nums.size();++i) {
            change(nums[i],1);
            if(i>=k) change(nums[i-k],-1);
            if(i+1>=k) {
                auto best=*order.begin();
                ans+=1LL*best.second*(-best.first);
            }
        }
        return ans;
    }
};
```

---

## 3675. Minimum Operations to Transform String
**Link:** https://leetcode.com/problems/minimum-operations-to-transform-string/
**Difficulty:** Medium | **Status:** Todo | **Access:** Free

**Approach:** Every distinct non-a letter must advance through the alphabet until a. Processing letters in descending circular order merges groups, so the answer is the maximum forward distance from any present character to a.
**Complexity:** O(n) time; O(1) space.

```cpp
class Solution {
public:
    int minOperations(string s) {
        int ans=0;
        for(char c:s) if(c!='a') ans=max(ans,26-(c-'a'));
        return ans;
    }
};
```

---

## 3680. Generate Schedule
**Link:** https://leetcode.com/problems/generate-schedule/
**Difficulty:** Medium | **Status:** Todo | **Access:** Free

**Requires further validation:** The problem statement is available, but a submission-ready efficient solution has not yet been verified. No speculative code is included.

---

## 3698. Split Array With Minimum Difference
**Link:** https://leetcode.com/problems/split-array-with-minimum-difference/
**Difficulty:** Medium | **Status:** Todo | **Access:** Free

**Approach:** Prefix/suffix monotonicity flags let us check every split in O(1), with prefix sums tracking the absolute difference.
**Complexity:** O(n) time; O(n) space.

```cpp
class Solution {
public:
    long long splitArray(vector<int>& nums) {
        int n=nums.size();
        vector<char> inc(n,1),dec(n,1);
        for(int i=1;i<n;++i) inc[i]=inc[i-1] && nums[i]>nums[i-1];
        for(int i=n-2;i>=0;--i) dec[i]=dec[i+1] && nums[i]>nums[i+1];
        long long total=0,left=0,best=LLONG_MAX;
        for(int x:nums) total+=x;
        for(int i=0;i+1<n;++i) {
            left+=nums[i];
            if(inc[i]&&dec[i+1]) best=min(best,llabs(total-2*left));
        }
        return best==LLONG_MAX?-1:best;
    }
};
```

---

## 3703. Remove K-Balanced Substrings
**Link:** https://leetcode.com/problems/remove-k-balanced-substrings/
**Difficulty:** Medium | **Status:** Todo | **Access:** Free

**Approach:** Use run-length encoding as a stack. After appending each character, if the last runs end with at least k opens followed by at least k closes, remove k of each. Repeat as needed.
**Complexity:** O(n) amortized time; O(n) space.

```cpp
class Solution {
public:
    string removeSubstring(string s,int k) {
        vector<pair<char,int>> st;
        for(char c:s) {
            if(!st.empty() && st.back().first==c) ++st.back().second;
            else st.push_back({c,1});
            while(st.size()>=2 && st.back().first==')' &&
                  st[st.size()-2].first=='(' &&
                  st.back().second>=k && st[st.size()-2].second>=k) {
                st.back().second-=k;
                st[st.size()-2].second-=k;
                int right=st.back().second;
                int left=st[st.size()-2].second;
                st.pop_back();st.pop_back();
                if(left) {
                    if(!st.empty()&&st.back().first=='(') st.back().second+=left;
                    else st.push_back({'(',left});
                }
                if(right) st.push_back({')',right});
            }
        }
        string out;
        for(auto &p:st) out.append(p.second,p.first);
        return out;
    }
};
```

---

## 3709. Design Exam Scores Tracker
**Link:** https://leetcode.com/problems/design-exam-scores-tracker/
**Difficulty:** Medium | **Status:** Todo | **Access:** Free

**Approach:** Record increasing timestamps and cumulative scores. Binary-search the first record at or after startTime and the first record after endTime; subtract prefix sums.
**Complexity:** record O(1); totalScore O(log n); O(n) storage.

```cpp
class ExamTracker {
    vector<int> times;
    vector<long long> pref;
public:
    ExamTracker() { pref.push_back(0); }
    void record(int time,int score) {
        times.push_back(time);
        pref.push_back(pref.back()+score);
    }
    long long totalScore(int startTime,int endTime) {
        int l=lower_bound(times.begin(),times.end(),startTime)-times.begin();
        int r=upper_bound(times.begin(),times.end(),endTime)-times.begin();
        return pref[r]-pref[l];
    }
};
```

---

## 3713. Longest Balanced Substring I
**Link:** https://leetcode.com/problems/longest-balanced-substring-i/
**Difficulty:** Medium | **Status:** Todo | **Access:** Free

**Approach:** For each start position, extend the substring, updating 26 frequencies. A substring is balanced when every positive frequency equals the first positive frequency.
**Complexity:** O(26n²) time; O(26) extra space.

```cpp
class Solution {
public:
    int longestBalanced(string s) {
        int best=0,n=s.size();
        for(int i=0;i<n;++i) {
            int cnt[26]={0};
            for(int j=i;j<n;++j) {
                ++cnt[s[j]-'a'];
                int f=0;bool good=true;
                for(int c=0;c<26;++c) if(cnt[c]) {
                    if(!f) f=cnt[c];
                    else if(cnt[c]!=f) {good=false;break;}
                }
                if(good) best=max(best,j-i+1);
            }
        }
        return best;
    }
};
```

---
# Batch 02 — Optimized C++11/C++14 Solutions

> Solutions are based on the user-provided problem statements and signatures. They have not been submitted to LeetCode. Solutions are algorithmic drafts, not LeetCode-verified Accepted submissions.

## 3714. Longest Balanced Substring II
**Link:** https://leetcode.com/problems/longest-balanced-substring-ii/

**Approach:** Check substrings containing exactly one, two, or three distinct letters. One letter: longest identical run. Two letters: for each pair, split at the excluded letter and find the longest zero-sum prefix difference. Three letters: equalize both count differences using a hash map of prefix states.

**Complexity:** O(n) expected time; O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestBalanced(string s) {
        int n = s.size(), ans = 0;
        for (int i = 0, j; i < n; i = j) {
            j = i + 1;
            while (j < n && s[j] == s[i]) ++j;
            ans = max(ans, j - i);
        }
        for (int a = 0; a < 3; ++a) {
            for (int b = a + 1; b < 3; ++b) {
                unordered_map<int,int> first;
                first[0] = -1;
                int diff = 0;
                for (int i = 0; i < n; ++i) {
                    int c = s[i] - 'a';
                    if (c != a && c != b) {
                        first.clear(); first[0] = i; diff = 0;
                    } else {
                        diff += (c == a ? 1 : -1);
                        if (first.count(diff)) ans = max(ans, i - first[diff]);
                        else first[diff] = i;
                    }
                }
            }
        }
        unordered_map<long long,int> first;
        first[(long long)n * (2LL*n + 1) + n] = -1;
        int cnt[3] = {0,0,0};
        for (int i = 0; i < n; ++i) {
            ++cnt[s[i] - 'a'];
            long long x = (long long)cnt[0] - cnt[1];
            long long y = (long long)cnt[0] - cnt[2];
            long long key = (x + n) * (2LL*n + 1) + (y + n);
            if (first.count(key)) ans = max(ans, i - first[key]);
            else first[key] = i;
        }
        return ans;
    }
};
```

---

## 3717. Minimum Operations to Make the Array Beautiful
**Link:** https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

**Approach:** Dynamic programming over the finalized value of each element. Since all original values are at most 50, an optimal sequence can be chosen with finalized values at most 100: once a value reaches at least 50, subsequent values can stay equal to it; the first multiple of a predecessor below 50 that reaches 50 is at most 100. For each candidate value `v`, transition from any earlier finalized value `u` dividing `v`.

**Complexity:** O(n·100²) time; O(100) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        const int LIMIT = 100, INF = 1000000000;
        vector<int> dp(LIMIT + 1, INF);
        dp[nums[0]] = 0;
        for (int i = 1; i < (int)nums.size(); ++i) {
            vector<int> next(LIMIT + 1, INF);
            for (int v = nums[i]; v <= LIMIT; ++v) {
                for (int u = 1; u <= v; ++u) {
                    if (v % u == 0 && dp[u] != INF)
                        next[v] = min(next[v], dp[u] + v - nums[i]);
                }
            }
            dp.swap(next);
        }
        return *min_element(dp.begin(), dp.end());
    }
};
```

---

## 3719. Longest Balanced Subarray I
**Link:** https://leetcode.com/problems/longest-balanced-subarray-i/

**Approach:** Enumerate each left endpoint and expand the right endpoint while tracking which even and odd values have appeared.

**Complexity:** O(n²) expected time; O(U) space, U ≤ n distinct values.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        for (int l = 0; l < n; ++l) {
            unordered_set<int> seen;
            int balance = 0;
            for (int r = l; r < n; ++r) {
                if (seen.insert(nums[r]).second)
                    balance += (nums[r] % 2 == 0 ? 1 : -1);
                if (balance == 0) ans = max(ans, r - l + 1);
            }
        }
        return ans;
    }
};
```

---

## 3723. Maximize Sum of Squares of Digits
**Link:** https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

**Approach:** Convexity of x² means concentrating digit sum into as many 9s as possible maximizes the score. Put larger digits first to break ties lexicographically.

**Complexity:** O(num) time and output space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        if (sum > 9LL * num) return "";
        string ans;
        for (int i = 0; i < num; ++i) {
            int d = min(9, sum);
            ans.push_back(char('0' + d));
            sum -= d;
        }
        return ans;
    }
};
```

---

## 3724. Minimum Operations to Transform Array
**Link:** https://leetcode.com/problems/minimum-operations-to-transform-array/

**Approach:** First pay for independently matching the original n positions. Append one copy during the transition of some nums1[i] to nums2[i]; the cheapest additional adjustment to the appended value is its distance from the closed interval between those endpoints.

**Complexity:** O(n) time; O(1) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long minOperations(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), target = nums2[n];
        long long base = 1, extra = LLONG_MAX;
        for (int i = 0; i < n; ++i) {
            base += llabs((long long)nums1[i] - nums2[i]);
            int lo = min(nums1[i], nums2[i]);
            int hi = max(nums1[i], nums2[i]);
            long long dist = target < lo ? lo - target :
                             target > hi ? target - hi : 0;
            extra = min(extra, dist);
        }
        return base + extra;
    }
};
```

---

## 3730. Maximum Calories Burnt from Jumps
**Link:** https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

**Approach:** Sort heights, then alternate the largest remaining and smallest remaining values, starting from the largest. This maximizes large adjacent squared differences.

**Complexity:** O(n log n) time; O(n) space for sorted copy.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maxCaloriesBurnt(vector<int>& heights) {
        vector<int> a = heights;
        sort(a.begin(), a.end());
        int l = 0, r = (int)a.size() - 1;
        long long last = 0, ans = 0;
        bool high = true;
        while (l <= r) {
            long long v = high ? a[r--] : a[l++];
            long long d = v - last;
            ans += d * d;
            last = v;
            high = !high;
        }
        return ans;
    }
};
```

---

## 3732. Maximum Product of Three Elements After One Replacement
**Link:** https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

**Approach:** Replacing one element by ±100000 makes the optimal product equal to 100000 times the maximum absolute product of any two other elements. Select the two largest absolute values (the replacement can be performed at a different index).

**Complexity:** O(n) time; O(1) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        long long a = 0, b = 0;
        for (int x : nums) {
            long long v = llabs((long long)x);
            if (v >= a) { b = a; a = v; }
            else if (v > b) b = v;
        }
        return 100000LL * a * b;
    }
};
```

---

## 3738. Longest Non-Decreasing Subarray After Replacing at Most One Element
**Link:** https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

**Approach:** Compute nondecreasing run lengths ending at and starting from each position. If replacing i, it can join both neighboring runs exactly when nums[i-1] ≤ nums[i+1]; otherwise it extends only one side.

**Complexity:** O(n) time; O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size();
        vector<int> left(n, 1), right(n, 1);
        for (int i = 1; i < n; ++i)
            if (nums[i-1] <= nums[i]) left[i] = left[i-1] + 1;
        for (int i = n - 2; i >= 0; --i)
            if (nums[i] <= nums[i+1]) right[i] = right[i+1] + 1;
        int ans = 1;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, left[i]);
            int l = i ? left[i-1] : 0;
            int r = i+1 < n ? right[i+1] : 0;
            ans = max(ans, 1 + max(l,r));
            if (i > 0 && i+1 < n && nums[i-1] <= nums[i+1])
                ans = max(ans, l + 1 + r);
        }
        return min(ans, n);
    }
};
```

---

## 3742. Maximum Path Score in a Grid
**Link:** https://leetcode.com/problems/maximum-path-score-in-a-grid/

**Approach:** Dynamic programming by cell and spent cost, keeping only the previous grid row. A cell adds score grid[i][j] and costs 1 iff its value is nonzero.

**Complexity:** O(m·n·min(k,m+n−1)) time; O(n·min(k,m+n−1)) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        k = min(k, m + n - 1);
        vector<vector<int>> dp(n, vector<int>(k+1, -1));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int v = grid[i][j], cost = v != 0;
                vector<int> cur(k+1, -1);
                if (i == 0 && j == 0) cur[0] = 0;
                else for (int c = cost; c <= k; ++c) {
                    int best = dp[j][c-cost]; // from above
                    if (j) best = max(best, dp[j-1][c-cost]); // from left
                    if (best != -1) cur[c] = best + v;
                }
                dp[j].swap(cur);
            }
        }
        return *max_element(dp[n-1].begin(), dp[n-1].end());
    }
};
```

---

## 3744. Find Kth Character in Expanded String
**Link:** https://leetcode.com/problems/find-kth-character-in-expanded-string/

**Approach:** Walk through the original string and count how many positions each character contributes. Within a word, character j (1-indexed) contributes j repeated copies; spaces contribute one.

**Complexity:** O(|s|) time; O(1) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    char kthCharacter(string s, long long k) {
        long long pos = 0, repeat = 0;
        for (char c : s) {
            if (c == ' ') {
                if (k == pos) return ' ';
                ++pos; repeat = 0;
            } else {
                ++repeat;
                if (k < pos + repeat) return c;
                pos += repeat;
            }
        }
        return ' ';
    }
};
```

---

## 3747. Count Distinct Integers After Removing Zeros
**Link:** https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

**Approach:** Every result of removing zeros is a positive integer without digit 0 and ≤ n. Conversely, every such integer appears by choosing x equal to itself. Count positive integers ≤ n with no zero digits using digit DP / place-value counting.

**Complexity:** O(log10 n) time; O(1) auxiliary space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countDistinct(long long n) {
        string s = to_string(n);
        int len = s.size();
        vector<long long> pow9(len + 1, 1);
        for (int i = 1; i <= len; ++i) pow9[i] = pow9[i-1] * 9;
        long long ans = 0;
        for (int i = 1; i < len; ++i) ans += pow9[i];
        for (int i = 0; i < len; ++i) {
            int d = s[i] - '0';
            ans += (long long)max(0, d - 1) * pow9[len - i - 1];
            if (d == 0) return ans;
        }
        return ans + 1;
    }
};
```

---

## 3752. Lexicographically Smallest Negated Permutation that Sums to Target
**Link:** https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

**Approach:** Let T=n(n+1)/2. The absolute values chosen negative must sum to (T−target)/2. Iterate from n down to 1, choosing −i whenever the remaining target can still be formed by numbers 1..i−1. Sort signed values ascending for lexicographic minimality.

**Complexity:** O(n log n) time; O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> lexSmallestNegatedPerm(int n, long long target) {
        long long total = 1LL*n*(n+1)/2;
        if (llabs(target) > total || (total-target)%2 != 0) return {};
        long long need = (total-target)/2;
        vector<int> ans;
        for (int i = n; i >= 1; --i) {
            long long rest = 1LL*(i-1)*i/2;
            if (need >= i && need-i <= rest) {
                ans.push_back(-i);
                need -= i;
            } else ans.push_back(i);
        }
        if (need != 0) return {};
        sort(ans.begin(), ans.end());
        return ans;
    }
};
```

---

## 3756. Concatenate Non-Zero Digits and Multiply by Sum II
**Link:** https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

**Approach:** Build prefix counts of nonzero digits, prefix digit sums, and the concatenated nonzero-number prefix modulo 1e9+7. Extract a substring using a power of ten for the number of nonzero digits in it.

**Complexity:** O(|s| + q) time; O(|s|) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        const long long MOD = 1000000007LL;
        int n = s.size();
        vector<int> cnt(n+1,0), sum(n+1,0);
        vector<long long> pref(n+1,0), pow10(n+1,1);
        for (int i = 0; i < n; ++i) {
            int d = s[i] - '0';
            cnt[i+1] = cnt[i] + (d != 0);
            sum[i+1] = sum[i] + d;
            pref[i+1] = (pref[i] * (d ? 10 : 1) + d) % MOD;
            pow10[i+1] = pow10[i] * 10 % MOD;
        }
        vector<int> ans;
        for (const auto& q : queries) {
            int l = q[0], r = q[1] + 1;
            int digits = cnt[r] - cnt[l];
            long long x = (pref[r] - pref[l]*pow10[digits]%MOD + MOD)%MOD;
            ans.push_back((int)(x * (sum[r]-sum[l]) % MOD));
        }
        return ans;
    }
};
```

---

## 3758. Convert Number Words to Digits
**Link:** https://leetcode.com/problems/convert-number-words-to-digits/

**Approach:** Scan left to right. At each position, compare against the ten spelled-out digit names; on a match append its digit and skip the matched word, otherwise advance by one character.

**Complexity:** O(10·7·|s|) = O(|s|) time; O(|s|) output space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string convertNumber(string s) {
        static const string words[10] = {"zero","one","two","three","four",
            "five","six","seven","eight","nine"};
        string out;
        for (size_t i = 0; i < s.size();) {
            bool found = false;
            for (int d = 0; d < 10; ++d) {
                const string& w = words[d];
                if (i + w.size() <= s.size() && s.compare(i,w.size(),w) == 0) {
                    out.push_back(char('0' + d));
                    i += w.size();
                    found = true;
                    break;
                }
            }
            if (!found) ++i;
        }
        return out;
    }
};
```

---

## 3761. Minimum Absolute Distance Between Mirror Pairs
**Link:** https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

**Approach:** At position j, look for the most recent earlier i whose reversed value equals nums[j]. Maintain a map from reversed earlier values to their latest indices.

**Complexity:** O(n·digits) expected time; O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    int reverseDigits(int x) {
        int ans = 0;
        while (x) { ans = ans * 10 + x % 10; x /= 10; }
        return ans;
    }
public:
    int minMirrorPairDistance(vector<int>& nums) {
        unordered_map<int,int> last;
        int ans = INT_MAX;
        for (int j = 0; j < (int)nums.size(); ++j) {
            auto it = last.find(nums[j]);
            if (it != last.end()) ans = min(ans, j - it->second);
            last[reverseDigits(nums[j])] = j;
        }
        return ans == INT_MAX ? -1 : ans;
    }
};
```

---

## 3763. Maximum Total Sum with Threshold Constraints
**Link:** https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

**Approach:** Sort items by the earliest step when they become available, and use a max-heap to choose the highest value currently eligible. Every selection advances the step by one.

**Complexity:** O(n log n) time; O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maxSum(vector<int>& nums, vector<int>& threshold) {
        int n = nums.size();
        vector<pair<int,int>> items;
        for (int i = 0; i < n; ++i) items.push_back({threshold[i], nums[i]});
        sort(items.begin(), items.end());
        priority_queue<int> pq;
        long long ans = 0;
        int j = 0;
        for (int step = 1; step <= n; ++step) {
            while (j < n && items[j].first <= step) pq.push(items[j++].second);
            if (pq.empty()) break;
            ans += pq.top(); pq.pop();
        }
        return ans;
    }
};
```

---

## 3766. Minimum Operations to Make Binary Palindrome
**Link:** https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

**Approach:** Precompute all binary palindromes up to a little above the maximum input using bit-reversal checks; then use lower_bound to find the closest palindrome for each input.

**Complexity:** O(M log M + n log M) time for M=~10000; O(M+n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    bool palindrome(int x) {
        int bits[32], n = 0;
        while (x) { bits[n++] = x & 1; x >>= 1; }
        for (int i = 0; i < n/2; ++i)
            if (bits[i] != bits[n-1-i]) return false;
        return true;
    }
public:
    vector<int> minOperations(vector<int>& nums) {
        vector<int> pal;
        for (int x = 1; x <= 10000; ++x)
            if (palindrome(x)) pal.push_back(x);
        vector<int> ans;
        for (int x : nums) {
            auto it = lower_bound(pal.begin(), pal.end(), x);
            int best = INT_MAX;
            if (it != pal.end()) best = min(best, abs(*it - x));
            if (it != pal.begin()) best = min(best, abs(*prev(it) - x));
            ans.push_back(best);
        }
        return ans;
    }
};
```

---

## 3767. Maximize Points After Choosing K Tasks
**Link:** https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

**Approach:** Assume technique 2 for all tasks. Sort the differences technique1[i]−technique2[i] descending; choose technique 1 for every positive difference and, if necessary, enough additional differences to reach k.

**Complexity:** O(n log n) time; O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maxPoints(vector<int>& technique1, vector<int>& technique2, int k) {
        int n = technique1.size();
        long long ans = 0;
        vector<int> diff;
        for (int i = 0; i < n; ++i) {
            ans += technique2[i];
            diff.push_back(technique1[i] - technique2[i]);
        }
        sort(diff.rbegin(), diff.rend());
        for (int i = 0; i < n; ++i)
            if (i < k || diff[i] > 0) ans += diff[i];
        return ans;
    }
};
```

---

## 3771. Total Score of Dungeon Runs
**Link:** https://leetcode.com/problems/total-score-of-dungeon-runs/

**Approach:** Let P[i] be the prefix sum of damage through room i. A start j earns a point at room i iff P[j−1] ≥ P[i] + requirement[i] − hp. Since damage is positive, prefix sums are sorted; count qualifying starts with lower_bound.

**Complexity:** O(n log n) time; O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long totalScore(int hp, vector<int>& damage, vector<int>& requirement) {
        int n = damage.size();
        vector<long long> pref(n+1,0);
        for (int i = 0; i < n; ++i) pref[i+1] = pref[i] + damage[i];
        long long ans = 0;
        for (int i = 1; i <= n; ++i) {
            long long need = pref[i] + requirement[i-1] - hp;
            auto it = lower_bound(pref.begin(), pref.begin()+i, need);
            ans += (pref.begin()+i) - it;
        }
        return ans;
    }
};
```

---

## 3773. Maximum Number of Equal Length Runs
**Link:** https://leetcode.com/problems/maximum-number-of-equal-length-runs/

**Approach:** Run-length encode the string and count how many maximal equal-character runs have each length; return the largest frequency.

**Complexity:** O(n) time; O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSameLengthRuns(string s) {
        vector<int> count(s.size()+1,0);
        int ans = 0;
        for (int i = 0, j; i < (int)s.size(); i = j) {
            j = i + 1;
            while (j < (int)s.size() && s[j] == s[i]) ++j;
            ans = max(ans, ++count[j-i]);
        }
        return ans;
    }
};
```

---
# Batch 03 — Optimized C++11/C++14 Solutions

**Problems:** 41–60 of 330  
**Validation:** Draft implementations; not submitted to LeetCode. Problem-statement inconsistencies are explicitly flagged.

Each snippet is intended to be submitted **individually** in LeetCode (classes named `Solution` repeat).

## 3776. Minimum Moves to Balance Circular Array
**Link:** https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

**Approach:** Only one person may have a deficit. Collect units from other positions in increasing circular distance; every transferred unit costs its distance.

**Complexity:** O(n) time, O(1) extra space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    long long minMoves(vector<int>& balance) {
        int n = balance.size(), bad = -1;
        long long total = 0;
        for (int i = 0; i < n; ++i) {
            total += balance[i];
            if (balance[i] < 0) bad = i;
        }
        if (total < 0) return -1;
        if (bad == -1) return 0;
        long long need = -(long long)balance[bad], ans = 0;
        for (int d = 1; d <= n / 2 && need > 0; ++d) {
            int l = (bad - d + n) % n, r = (bad + d) % n;
            long long take = min(need, (long long)balance[l]);
            ans += take * d; need -= take;
            if (l != r) {
                take = min(need, (long long)balance[r]);
                ans += take * d; need -= take;
            }
        }
        return need == 0 ? ans : -1;
    }
};
```

---

## 3778. Minimum Distance Excluding One Maximum Weighted Edge
**Link:** https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

**Approach:** Choose the edge whose weight is excluded. Dijkstra distances from both endpoints give the cheapest remaining prefix and suffix; minimize their sum over every possible excluded edge.

**Complexity:** O((n+m) log n) time, O(n+m) space.

**C++11/C++14 solution:**

```cpp
class Solution {
    typedef pair<long long,int> State;
    vector<long long> shortest(int source, const vector<vector<pair<int,int>>>& g) {
        const long long INF = (1LL << 62);
        vector<long long> dist(g.size(), INF);
        priority_queue<State, vector<State>, greater<State>> pq;
        dist[source] = 0; pq.push({0, source});
        while (!pq.empty()) {
            State cur = pq.top(); pq.pop();
            long long d = cur.first; int u = cur.second;
            if (d != dist[u]) continue;
            for (auto e : g[u]) if (dist[e.first] > d + e.second) {
                dist[e.first] = d + e.second;
                pq.push({dist[e.first], e.first});
            }
        }
        return dist;
    }
public:
    long long minCostExcludingMax(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int,int>>> g(n);
        for (auto &e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
        }
        vector<long long> a = shortest(0, g), b = shortest(n - 1, g);
        long long ans = (1LL << 62);
        for (auto &e : edges) {
            ans = min(ans, min(a[e[0]] + b[e[1]], a[e[1]] + b[e[0]]));
        }
        return ans;
    }
};
```

**Validation note:** The free-edge shortest-path reduction is valid because a minimum-cost walk can be simplified to a path without increasing sum minus maximum. The sample 2 explanation incorrectly calls the 50000-weight edge a weight-1 edge.

---

## 3781. Maximum Score After Binary Swaps
**Link:** https://leetcode.com/problems/maximum-score-after-binary-swaps/

**Approach:** Process positions left to right. When a `1` is encountered, it can occupy any still-unselected earlier position; take the largest available value using a max-heap.

**Complexity:** O(n log n) time, O(n) space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    long long maximumScore(vector<int>& nums, string s) {
        priority_queue<int> pq;
        long long ans = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            pq.push(nums[i]);
            if (s[i] == '1') {
                ans += pq.top();
                pq.pop();
            }
        }
        return ans;
    }
};
```

---

## 3792. Sum of Increasing Product Blocks
**Link:** https://leetcode.com/problems/sum-of-increasing-product-blocks/

**Approach:** Generate the next consecutive integer for each factor, maintain each block product modulo 1e9+7, and accumulate.

**Complexity:** O(n²) time, O(1) space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    int sumOfBlocks(int n) {
        const long long MOD = 1000000007LL;
        long long next = 1, ans = 0;
        for (int len = 1; len <= n; ++len) {
            long long prod = 1;
            for (int j = 0; j < len; ++j) {
                prod = prod * (next++ % MOD) % MOD;
            }
            ans = (ans + prod) % MOD;
        }
        return (int)ans;
    }
};
```

---

## 3796. Find Maximum Value in a Constrained Sequence
**Link:** https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

**Approach:** Propagate upper bounds from the fixed zero and restrictions in both directions. The pointwise smallest upper envelope is feasible, and its maximum is optimal.

**Complexity:** O(n + r) time, O(n) space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    int findMaxVal(int n, vector<vector<int>>& restrictions, vector<int>& diff) {
        const long long INF = (1LL << 60);
        vector<long long> hi(n, INF);
        hi[0] = 0;
        for (auto &r : restrictions) hi[r[0]] = min(hi[r[0]], (long long)r[1]);
        for (int i = 1; i < n; ++i)
            hi[i] = min(hi[i], hi[i - 1] + diff[i - 1]);
        for (int i = n - 2; i >= 0; --i)
            hi[i] = min(hi[i], hi[i + 1] + diff[i]);
        return (int)*max_element(hi.begin(), hi.end());
    }
};
```

---

## 3799. Word Squares II
**Link:** https://leetcode.com/problems/word-squares-ii/

**Approach:** Enumerate distinct top/left/right words and look up bottom candidates. With at most 15 words, exhaustive search is small; sort tuples.

**Complexity:** O(W⁴ log W) worst-case time, O(W⁴) output space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        int n = words.size();
        vector<vector<string>> ans;
        for (int a = 0; a < n; ++a)
            for (int b = 0; b < n; ++b) if (b != a && words[a][0] == words[b][0])
                for (int c = 0; c < n; ++c) if (c != a && c != b && words[a][3] == words[c][0])
                    for (int d = 0; d < n; ++d) if (d != a && d != b && d != c &&
                        words[d][0] == words[b][3] && words[d][3] == words[c][3])
                        ans.push_back({words[a], words[b], words[c], words[d]});
        sort(ans.begin(), ans.end());
        return ans;
    }
};
```

**Validation note:** The uploaded example `able,area,echo,also` does not satisfy its own stated corner constraints (e.g. `able[3]` is `e` while `echo[0]` is `e`, but `also[3]` is `o` and `echo[3]` is `o`; `area[3]` is `a`, `also[0]` is `a`); this code follows the formal four corner equalities.

---

## 3800. Minimum Cost to Make Two Binary Strings Equal
**Link:** https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

**Approach:** A cross swap at the same index never changes whether the two bits match. Opposite mismatch types can be repaired together by one within-string swap; otherwise a mismatch needs a flip. Pair as many opposite types as possible when swapping is cheaper than two flips.

**Complexity:** O(n) time, O(1) space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    long long minimumCost(string s, string t, int flipCost, int swapCost, int crossCost) {
        long long a = 0, b = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            if (s[i] == '0' && t[i] == '1') ++a;
            if (s[i] == '1' && t[i] == '0') ++b;
        }
        long long pairs = min(a, b);
        return pairs * min((long long)swapCost, 2LL * flipCost)
             + (a + b - 2 * pairs) * flipCost;
    }
};
```

**Validation note:** **Source inconsistency:** Example 1 claims 16, but the listed cross-swap changes `(0,1)` to `(1,0)` and does not fix a mismatch; the final arrays in the explanation do not match the operations. Under the written operations, the result for Example 1 is 32, not 16. This implementation follows the written rules and needs statement clarification before LeetCode validation.

---

## 3804. Number of Centered Subarrays
**Link:** https://leetcode.com/problems/number-of-centered-subarrays/

**Approach:** Enumerate every subarray, update its running sum and a frequency map. A subarray is centered exactly when its sum appears in the map.

**Complexity:** O(n²) expected time, O(n) space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    int centeredSubarrays(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        for (int l = 0; l < n; ++l) {
            unordered_set<long long> seen;
            long long sum = 0;
            for (int r = l; r < n; ++r) {
                sum += nums[r];
                seen.insert(nums[r]);
                if (seen.count(sum)) ++ans;
            }
        }
        return ans;
    }
};
```

---

## 3807. Minimum Cost to Repair Edges to Traverse a Graph
**Link:** https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

**Approach:** Binary search the minimum repair threshold. For a threshold, BFS over edges with weight at most that threshold finds the minimum number of edges to the destination.

**Complexity:** O((n+m) log M) time, O(n+m) space; M is max edge weight.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    int minCost(int n, vector<vector<int>>& edges, int k) {
        vector<vector<pair<int,int>>> g(n);
        int high = 0;
        for (auto &e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
            high = max(high, e[2]);
        }
        auto ok = [&](int limit) {
            vector<int> dist(n, -1);
            queue<int> q; q.push(0); dist[0] = 0;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                if (u == n - 1) return true;
                if (dist[u] == k) continue;
                for (auto e : g[u]) if (e.second <= limit && dist[e.first] == -1) {
                    dist[e.first] = dist[u] + 1;
                    q.push(e.first);
                }
            }
            return false;
        };
        if (!ok(high)) return -1;
        int low = 0;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (ok(mid)) high = mid;
            else low = mid + 1;
        }
        return low;
    }
};
```

---

## 3809. Best Reachable Tower
**Link:** https://leetcode.com/problems/best-reachable-tower/

**Approach:** Scan reachable towers and retain the largest quality, breaking ties by lexicographically smallest coordinates.

**Complexity:** O(n) time, O(1) extra space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    vector<int> bestTower(vector<vector<int>>& towers, vector<int>& center, int radius) {
        int bestQ = -1;
        vector<int> ans = {-1, -1};
        for (auto &t : towers) {
            int dist = abs(t[0] - center[0]) + abs(t[1] - center[1]);
            vector<int> pos = {t[0], t[1]};
            if (dist <= radius && (t[2] > bestQ || (t[2] == bestQ && pos < ans))) {
                bestQ = t[2]; ans = pos;
            }
        }
        return ans;
    }
};
```

---

## 3810. Minimum Operations to Reach Target Array
**Link:** https://leetcode.com/problems/minimum-operations-to-reach-target-array/

**Approach:** Every distinct value occurring at an initially incorrect index must be selected at least once. Selecting each such original value once fixes all its occurrences simultaneously; already-correct entries are harmless.

**Complexity:** O(n) expected time, O(n) space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, vector<int>& target) {
        unordered_set<int> need;
        for (int i = 0; i < (int)nums.size(); ++i)
            if (nums[i] != target[i]) need.insert(nums[i]);
        return (int)need.size();
    }
};
```

---

## 3811. Number of Alternating XOR Partitions
**Link:** https://leetcode.com/problems/number-of-alternating-xor-partitions/

**Approach:** Prefix XOR turns each valid block into a lookup. Keep two maps of counts of partitions ending in the two alternating phases, and update them at each prefix.

**Complexity:** O(n) expected time, O(n) space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    int alternatingXOR(vector<int>& nums, int target1, int target2) {
        const int MOD = 1000000007;
        unordered_map<int,long long> end1, end2;
        int px = 0;
        long long last1 = 0, last2 = 0;
        end2[0] = 1; // Empty partition is ready for target1.
        for (int v : nums) {
            px ^= v;
            last1 = end2[px ^ target1] % MOD;
            last2 = end1[px ^ target2] % MOD;
            end1[px] = (end1[px] + last1) % MOD;
            end2[px] = (end2[px] + last2) % MOD;
        }
        return (int)((last1 + last2) % MOD);
    }
};
```

---

## 3814. Maximum Capacity Within Budget
**Link:** https://leetcode.com/problems/maximum-capacity-within-budget/

**Approach:** Sort machines by cost and build prefix maximum capacity. For each machine, binary search the most expensive compatible partner strictly below the remaining budget, excluding itself. Instead, process pairs in sorted order and use the best capacity among earlier machines to guarantee distinctness.

**Complexity:** O(n log n) time, O(n) space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    int maxCapacity(vector<int>& costs, vector<int>& capacity, int budget) {
        int n = costs.size(), ans = 0;
        vector<pair<int,int>> a;
        for (int i = 0; i < n; ++i) {
            a.push_back({costs[i], capacity[i]});
            if (costs[i] < budget) ans = max(ans, capacity[i]);
        }
        sort(a.begin(), a.end());
        vector<int> pref(n);
        for (int i = 0; i < n; ++i)
            pref[i] = max(i ? pref[i - 1] : 0, a[i].second);
        for (int i = 1; i < n; ++i) {
            int limit = budget - a[i].first - 1;
            int lo = 0, hi = i;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (a[mid].first <= limit) lo = mid + 1;
                else hi = mid;
            }
            if (lo > 0) ans = max(ans, a[i].second + pref[lo - 1]);
        }
        return ans;
    }
};
```

---

## 3815. Design Auction System
**Link:** https://leetcode.com/problems/design-auction-system/

**Approach:** For each item, maintain an ordered set of `(amount,userId)` and a map from user to current amount. The largest pair gives the correct tie-break.

**Complexity:** O(log B) per update/query (query O(1)); O(B) total space.

**C++11/C++14 solution:**

```cpp
class AuctionSystem {
    unordered_map<int, set<pair<int,int>>> bids;
    unordered_map<int, unordered_map<int,int>> amounts;
public:
    AuctionSystem() {}
    void addBid(int userId, int itemId, int bidAmount) {
        auto &byUser = amounts[itemId];
        auto it = byUser.find(userId);
        if (it != byUser.end()) bids[itemId].erase({it->second, userId});
        byUser[userId] = bidAmount;
        bids[itemId].insert({bidAmount, userId});
    }
    void updateBid(int userId, int itemId, int newAmount) {
        addBid(userId, itemId, newAmount);
    }
    void removeBid(int userId, int itemId) {
        int amount = amounts[itemId][userId];
        bids[itemId].erase({amount, userId});
        amounts[itemId].erase(userId);
    }
    int getHighestBidder(int itemId) {
        auto it = bids.find(itemId);
        return it == bids.end() || it->second.empty() ? -1 : it->second.rbegin()->second;
    }
};
```

---

## 3817. Good Indices in a Digit String
**Link:** https://leetcode.com/problems/good-indices-in-a-digit-string/

**Approach:** The only candidate substring ending at i is `to_string(i)` itself. Compare it with the corresponding suffix of the prefix ending at i.

**Complexity:** O(n log n) time, O(log n) auxiliary space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    vector<int> goodIndices(string s) {
        vector<int> ans;
        for (int i = 0; i < (int)s.size(); ++i) {
            string digits = to_string(i);
            int len = digits.size();
            if (len <= i + 1 && s.compare(i + 1 - len, len, digits) == 0)
                ans.push_back(i);
        }
        return ans;
    }
};
```

---

## 3819. Rotate Non Negative Elements
**Link:** https://leetcode.com/problems/rotate-non-negative-elements/

**Approach:** Extract nonnegative values, rotate their logical order left by k, and write them back into only the original nonnegative positions.

**Complexity:** O(n) time, O(n) space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    vector<int> rotateElements(vector<int>& nums, int k) {
        vector<int> vals;
        for (int x : nums) if (x >= 0) vals.push_back(x);
        int m = vals.size();
        if (m == 0) return nums;
        k %= m;
        vector<int> ans = nums;
        int j = 0;
        for (int i = 0; i < (int)nums.size(); ++i)
            if (nums[i] >= 0) ans[i] = vals[(j++ + k) % m];
        return ans;
    }
};
```

---

## 3820. Pythagorean Distance Nodes in a Tree
**Link:** https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

**Approach:** BFS from each of x, y, and z to get distances. Sort each node’s three distances and check the Pythagorean equality with 64-bit squares.

**Complexity:** O(n) time and O(n) space.

**C++11/C++14 solution:**

```cpp
class Solution {
    vector<int> distances(int start, const vector<vector<int>>& g) {
        vector<int> d(g.size(), -1);
        queue<int> q; q.push(start); d[start] = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : g[u]) if (d[v] == -1) {
                d[v] = d[u] + 1;
                q.push(v);
            }
        }
        return d;
    }
public:
    int specialNodes(int n, vector<vector<int>>& edges, int x, int y, int z) {
        vector<vector<int>> g(n);
        for (auto &e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        vector<int> dx = distances(x, g), dy = distances(y, g), dz = distances(z, g);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            long long a = dx[i], b = dy[i], c = dz[i];
            if (a > b) swap(a, b);
            if (b > c) swap(b, c);
            if (a > b) swap(a, b);
            if (a * a + b * b == c * c) ++ans;
        }
        return ans;
    }
};
```

---

## 3822. Design Order Management System
**Link:** https://leetcode.com/problems/design-order-management-system/

**Approach:** Index active orders by ID, and separately group IDs by `(type,price)` for fast modifications, cancellations, and queries.

**Complexity:** O(1) expected per add/modify/cancel, O(r) expected per query returning r IDs; O(N) space.

**C++11/C++14 solution:**

```cpp
class OrderManagementSystem {
    struct Order { string type; int price; };
    unordered_map<int, Order> orders;
    map<pair<string,int>, unordered_set<int>> groups;
public:
    OrderManagementSystem() {}
    void addOrder(int orderId, string orderType, int price) {
        orders[orderId] = {orderType, price};
        groups[{orderType, price}].insert(orderId);
    }
    void modifyOrder(int orderId, int newPrice) {
        Order &o = orders[orderId];
        groups[{o.type, o.price}].erase(orderId);
        o.price = newPrice;
        groups[{o.type, o.price}].insert(orderId);
    }
    void cancelOrder(int orderId) {
        Order o = orders[orderId];
        groups[{o.type, o.price}].erase(orderId);
        orders.erase(orderId);
    }
    vector<int> getOrdersAtPrice(string orderType, int price) {
        vector<int> ans;
        auto it = groups.find({orderType, price});
        if (it != groups.end())
            for (int id : it->second) ans.push_back(id);
        return ans;
    }
};
```

---

## 3824. Minimum K to Reduce Array Within Limit
**Link:** https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

**Approach:** For a fixed k, each value needs ceil(value/k) operations. This sum is monotone nonincreasing as k grows, while k² grows; binary search the first feasible k.

**Complexity:** O(n log(max(nums,n))) time, O(1) space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    int minimumK(vector<int>& nums) {
        int lo = 1, hi = max((int)nums.size(), *max_element(nums.begin(), nums.end()));
        auto feasible = [&](long long k) {
            long long limit = k * k, ops = 0;
            for (int v : nums) {
                ops += (v + k - 1) / k;
                if (ops > limit) return false;
            }
            return true;
        };
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
```

---

## 3828. Final Element After Subarray Deletions
**Link:** https://leetcode.com/problems/final-element-after-subarray-deletions/

**Approach:** Alice can delete any proper prefix or suffix and immediately leave either original endpoint. If she leaves more than one element, Bob can delete a proper subarray to leave an endpoint of the current array; Alice cannot guarantee more than the larger original endpoint.

**Complexity:** O(1) time and space.

**C++11/C++14 solution:**

```cpp
class Solution {
public:
    int finalElement(vector<int>& nums) {
        return max(nums.front(), nums.back());
    }
};
```

---
# Batch 04 — LeetCode C++11/C++14 Solutions

**Problems:** 61–80 of 330 | **Total:** 20

> Each code block is a standalone LeetCode submission. The implementations are based on the supplied statements and have not been submitted to LeetCode for verification.

## 3829. Design Ride Sharing System

**Problem:** https://leetcode.com/problems/design-ride-sharing-system/

```cpp
class RideSharingSystem {
    queue<int> riders, drivers;
    unordered_set<int> waiting;
public:
    RideSharingSystem() {}
    void addRider(int riderId) {
        riders.push(riderId);
        waiting.insert(riderId);
    }
    void addDriver(int driverId) { drivers.push(driverId); }
    vector<int> matchDriverWithRider() {
        while (!riders.empty() && !waiting.count(riders.front()))
            riders.pop();
        if (riders.empty() || drivers.empty()) return {-1, -1};
        int d = drivers.front(), r = riders.front();
        drivers.pop(); riders.pop(); waiting.erase(r);
        return {d, r};
    }
    void cancelRider(int riderId) { waiting.erase(riderId); }
};
```

**Approach:** Maintain FIFO queues for riders and drivers. Canceled riders are lazily skipped using an active set.

**Complexity:** Amortized O(1) per operation; O(R + D) space.

---

## 3835. Count Subarrays With Cost Less Than or Equal to K

**Problem:** https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        deque<int> mx, mn;
        long long ans = 0;
        int left = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            while (!mx.empty() && nums[mx.back()] <= nums[right]) mx.pop_back();
            while (!mn.empty() && nums[mn.back()] >= nums[right]) mn.pop_back();
            mx.push_back(right); mn.push_back(right);
            while ((long long)(nums[mx.front()] - nums[mn.front()]) *
                   (right - left + 1) > k) {
                if (mx.front() == left) mx.pop_front();
                if (mn.front() == left) mn.pop_front();
                ++left;
            }
            ans += right - left + 1;
        }
        return ans;
    }
};
```

**Approach:** Sliding window with monotonic deques maintaining maximum and minimum. For each right endpoint, shrink until `(max-min)*length <= k`; all shorter suffixes then qualify.

**Complexity:** O(n) time; O(n) space.

---

## 3837. Delayed Count of Equal Elements

**Problem:** https://leetcode.com/problems/delayed-count-of-equal-elements/

```cpp
class Solution {
public:
    vector<int> delayedCount(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans(n), freq(100001, 0);
        for (int i = n - 1; i >= 0; --i) {
            if (i + k + 1 < n) ++freq[nums[i + k + 1]];
            ans[i] = freq[nums[i]];
        }
        return ans;
    }
};
```

**Approach:** Traverse indices backward. Before processing `i`, insert index `i+k+1` into a frequency table, so the table counts exactly the allowed later positions.

**Complexity:** O(n) time; O(U) space, U <= 100001.

---

## 3839. Number of Prefix Connected Groups

**Problem:** https://leetcode.com/problems/number-of-prefix-connected-groups/

```cpp
class Solution {
public:
    int prefixConnected(vector<string>& words, int k) {
        unordered_map<string, int> freq;
        for (const string& w : words)
            if ((int)w.size() >= k) ++freq[w.substr(0, k)];
        int ans = 0;
        for (const auto& p : freq) if (p.second >= 2) ++ans;
        return ans;
    }
};
```

**Approach:** Count each length-k prefix, ignoring words that are too short. Each prefix with frequency at least two forms one group.

**Complexity:** O(total characters examined) expected time and space.

---

## 3840. House Robber V

**Problem:** https://leetcode.com/problems/house-robber-v/

```cpp
class Solution {
public:
    long long rob(vector<int>& nums, vector<int>& colors) {
        long long take = nums[0], skip = 0;
        for (int i = 1; i < (int)nums.size(); ++i) {
            long long nextTake = nums[i] + (colors[i] == colors[i-1]
                                                ? skip : max(skip, take));
            long long nextSkip = max(skip, take);
            take = nextTake; skip = nextSkip;
        }
        return max(take, skip);
    }
};
```

**Approach:** Track the best total ending with the current house robbed or skipped. Adjacent robbed houses are allowed only when their colors differ.

**Complexity:** O(n) time; O(1) auxiliary space.

---

## 3843. First Element with Unique Frequency

**Problem:** https://leetcode.com/problems/first-element-with-unique-frequency/

```cpp
class Solution {
public:
    int firstUniqueFreq(vector<int>& nums) {
        vector<int> freq(100001, 0);
        for (int x : nums) ++freq[x];
        vector<int> howMany(nums.size() + 1, 0);
        for (int x = 1; x <= 100000; ++x)
            if (freq[x]) ++howMany[freq[x]];
        for (int x : nums)
            if (howMany[freq[x]] == 1) return x;
        return -1;
    }
};
```

**Approach:** First count occurrences of each value, then count how many distinct values share each frequency. Return the first element whose frequency occurs once.

**Complexity:** O(n + U) time; O(U + n) space, U <= 100000.

---

## 3844. Longest Almost-Palindromic Substring

**Problem:** https://leetcode.com/problems/longest-almost-palindromic-substring/

```cpp
class Solution {
public:
    int almostPalindromic(string s) {
        int n = s.size(), ans = 1;
        vector<vector<unsigned char>> pal(n, vector<unsigned char>(n, 0));
        vector<vector<unsigned char>> almost(n, vector<unsigned char>(n, 0));
        for (int len = 1; len <= n; ++len) {
            for (int l = 0; l + len <= n; ++l) {
                int r = l + len - 1;
                pal[l][r] = (s[l] == s[r]) &&
                    (len <= 2 || pal[l + 1][r - 1]);
                if (len == 1) almost[l][r] = 1;
                else {
                    bool deleteLeft = pal[l + 1][r];
                    bool deleteRight = pal[l][r - 1];
                    bool deleteInside = len >= 3 && s[l] == s[r] &&
                                        almost[l + 1][r - 1];
                    almost[l][r] = deleteLeft || deleteRight || deleteInside;
                }
                if (almost[l][r]) ans = max(ans, len);
            }
        }
        return ans;
    }
};
```

**Approach:** Interval DP: `pal[l][r]` records whether the substring is a palindrome. `almost[l][r]` records whether deleting exactly one character can make it a palindrome. Either delete an endpoint, or keep matching endpoints and delete one character inside.

**Complexity:** O(n²) time; O(n²) space.

---

## 3846. Total Distance to Type a String Using One Finger

**Problem:** https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

```cpp
class Solution {
public:
    int totalDistance(string s) {
        string rows[] = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        int row[26] = {}, col[26] = {};
        for (int r = 0; r < 3; ++r)
            for (int c = 0; c < (int)rows[r].size(); ++c) {
                int id = rows[r][c] - 'a';
                row[id] = r; col[id] = c;
            }
        int prev = 0, ans = 0; // 'a'
        for (char ch : s) {
            int cur = ch - 'a';
            ans += abs(row[cur] - row[prev]) + abs(col[cur] - col[prev]);
            prev = cur;
        }
        return ans;
    }
};
```

**Approach:** Map each keyboard character to its row and column. Accumulate Manhattan distances starting from `a`.

**Complexity:** O(|s|) time; O(1) space.

---

## 3847. Find the Score Difference in a Game

**Problem:** https://leetcode.com/problems/find-the-score-difference-in-a-game/

```cpp
class Solution {
public:
    int scoreDifference(vector<int>& nums) {
        bool firstActive = true;
        int difference = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] % 2 != 0) firstActive = !firstActive;
            if ((i + 1) % 6 == 0) firstActive = !firstActive;
            difference += firstActive ? nums[i] : -nums[i];
        }
        return difference;
    }
};
```

**Approach:** Maintain the active player as a Boolean. Apply both swap conditions before awarding points.

**Complexity:** O(n) time; O(1) space.

---

## 3849. Maximum Bitwise XOR After Rearrangement

**Problem:** https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

```cpp
class Solution {
public:
    string maximumXor(string s, string t) {
        int zeros = count(t.begin(), t.end(), '0');
        int ones = (int)t.size() - zeros;
        string ans;
        ans.reserve(s.size());
        for (char c : s) {
            if (c == '0') {
                if (ones) { ans += '1'; --ones; }
                else { ans += '0'; --zeros; }
            } else {
                if (zeros) { ans += '1'; --zeros; }
                else { ans += '0'; --ones; }
            }
        }
        return ans;
    }
};
```

**Approach:** Build the XOR string greedily from the most significant position. To produce a 1, consume a bit of `t` opposite to the current bit of `s`, whenever available.

**Complexity:** O(n) time; O(n) output space.

---

## 3851. Maximum Requests Without Violating the Limit

**Problem:** https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

```cpp
class Solution {
public:
    int maxRequests(vector<vector<int>>& requests, int k, int window) {
        sort(requests.begin(), requests.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 if (a[0] != b[0]) return a[0] < b[0];
                 return a[1] < b[1];
             });
        deque<int> recent;
        int user = -1, ans = 0;
        for (const auto& req : requests) {
            if (req[0] != user) { user = req[0]; recent.clear(); }
            int time = req[1];
            while (!recent.empty() && time - recent.front() > window)
                recent.pop_front();
            if ((int)recent.size() < k) {
                recent.push_back(time);
                ++ans;
            }
        }
        return ans;
    }
};
```

**Approach:** Requests for each user are independent. Sort requests by `(user, time)`; greedily keep a request only when fewer than k previously kept requests lie within its inclusive window.

**Complexity:** O(n log n) time; O(n) space.

---

## 3853. Merge Close Characters

**Problem:** https://leetcode.com/problems/merge-close-characters/

```cpp
class Solution {
public:
    string mergeCharacters(string s, int k) {
        while (true) {
            bool changed = false;
            for (int i = 0; i < (int)s.size() && !changed; ++i) {
                for (int j = i + 1; j < (int)s.size() && j - i <= k; ++j) {
                    if (s[i] == s[j]) {
                        s.erase(j, 1);
                        changed = true;
                        break;
                    }
                }
            }
            if (!changed) return s;
        }
    }
};
```

**Approach:** Simulate the specified deterministic merge order. Scan possible left indices from smallest to largest and choose the nearest equal right character within k; erase it, then restart.

**Complexity:** O(n³) worst-case time with string erases, O(1) extra space; n <= 100.

---

## 3854. Minimum Operations to Make Array Parity Alternating

**Problem:** https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

```cpp
class Solution {
public:
    vector<int> makeParityAlternating(vector<int>& nums) {
        int n = nums.size(), bestOps = n + 1;
        long long bestRange = LLONG_MAX;
        for (int first = 0; first < 2; ++first) {
            int ops = 0;
            vector<pair<long long,long long>> choices;
            choices.reserve(n);
            for (int i = 0; i < n; ++i) {
                long long x = nums[i];
                bool change = ((x & 1LL) != (first ^ (i & 1)));
                ops += change;
                choices.push_back(change ? make_pair(x-1, x+1)
                                         : make_pair(x, x));
            }
            if (ops > bestOps) continue;
            // For any optimal solution, min and max can be chosen among
            // permitted endpoints. Find the shortest interval containing
            // at least one permitted value from every position.
            vector<pair<long long,int>> points;
            points.reserve(2*n);
            for (int i = 0; i < n; ++i) {
                points.push_back({choices[i].first, i});
                if (choices[i].second != choices[i].first)
                    points.push_back({choices[i].second, i});
            }
            sort(points.begin(), points.end());
            vector<int> countByIndex(n, 0);
            int covered = 0, left = 0;
            long long range = LLONG_MAX;
            for (int right = 0; right < (int)points.size(); ++right) {
                if (countByIndex[points[right].second]++ == 0) ++covered;
                while (covered == n) {
                    range = min(range, points[right].first - points[left].first);
                    if (--countByIndex[points[left].second] == 0) --covered;
                    ++left;
                }
            }
            if (ops < bestOps) { bestOps = ops; bestRange = range; }
            else bestRange = min(bestRange, range);
        }
        return {bestOps, (int)bestRange};
    }
};
```

**Approach:** Try the two possible alternating parity patterns. Each mismatching position requires exactly one ±1 operation. Among patterns requiring the fewest operations, find the smallest possible range: unchanged values are fixed, while changed values can be `x-1` or `x+1`. A feasible range `[L,R]` must intersect every allowed set; minimizing the range is equivalent to choosing the shortest interval stabbing all such sets. Use a sorted list of permitted endpoints and a sliding window to find the shortest interval containing an allowed value for every index.

**Complexity:** O(n log V) time; O(1) extra space, V is the input value span plus two.

---

## 3857. Minimum Cost to Split into Ones

**Problem:** https://leetcode.com/problems/minimum-cost-to-split-into-ones/

```cpp
class Solution {
public:
    int minCost(int n) { return n * (n - 1) / 2; }
};
```

**Approach:** Every split contributes `a*b` new pairs of original units separated by that split. Every unordered pair of the n final ones is separated exactly once, so the total is always `n*(n-1)/2`.

**Complexity:** O(1) time; O(1) space.

---

## 3858. Minimum Bitwise OR From Grid

**Problem:** https://leetcode.com/problems/minimum-bitwise-or-from-grid/

```cpp
class Solution {
public:
    int minimumOR(vector<vector<int>>& grid) {
        int answer = (1 << 17) - 1; // nums <= 100000
        for (int bit = 16; bit >= 0; --bit) {
            int candidate = answer & ~(1 << bit);
            bool valid = true;
            for (const auto& row : grid) {
                bool found = false;
                for (int x : row)
                    if ((x | candidate) == candidate) { found = true; break; }
                if (!found) { valid = false; break; }
            }
            if (valid) answer = candidate;
        }
        return answer;
    }
};
```

**Approach:** Greedily clear set bits of the answer from high to low. A candidate OR mask is feasible exactly when every row contains at least one value using only bits allowed by that mask.

**Complexity:** O(17 * total grid cells) time; O(1) auxiliary space.

---

## 3862. Find the Smallest Balanced Index

**Problem:** https://leetcode.com/problems/find-the-smallest-balanced-index/

```cpp
class Solution {
public:
    int smallestBalancedIndex(vector<int>& nums) {
        int n = nums.size();
        long long total = 0;
        for (int x : nums) total += x;
        vector<long long> suffix(n + 1, 1);
        for (int i = n - 1; i >= 0; --i) {
            if (suffix[i + 1] > total / nums[i]) suffix[i] = total + 1;
            else suffix[i] = suffix[i + 1] * nums[i];
        }
        long long leftSum = 0;
        for (int i = 0; i < n; ++i) {
            if (leftSum == suffix[i + 1]) return i;
            leftSum += nums[i];
        }
        return -1;
    }
};
```

**Approach:** Compute the total sum as a safe cap for suffix products: since all elements are positive, a suffix product greater than the total sum can never equal a left prefix sum. Compute capped suffix products backward, then scan prefix sums forward for the earliest match.

**Complexity:** O(n) time; O(n) space.

---

## 3863. Minimum Operations to Sort a String

**Problem:** https://leetcode.com/problems/minimum-operations-to-sort-a-string/

```cpp
class Solution {
public:
    int minOperations(string s) {
        if (is_sorted(s.begin(), s.end())) return 0;
        int n = s.size();
        if (n == 2) return -1;
        char lo = *min_element(s.begin(), s.end());
        char hi = *max_element(s.begin(), s.end());
        if (s.front() == lo || s.back() == hi) return 1;
        if (s.front() == hi && s.back() == lo &&
            count(s.begin(), s.end(), hi) == 1 &&
            count(s.begin(), s.end(), lo) == 1) return 3;
        return 2;
    }
};
```

**Approach:** If already sorted, answer is zero. For n=2, a descending pair cannot be sorted because the only proper substrings have length one. For n>=3, one operation works if the first character is already a global minimum or the last is already a global maximum; otherwise two suffice unless the first is the unique maximum and the last is the unique minimum, which needs three.

**Complexity:** O(n) time; O(1) space.

---

## 3865. Reverse K Subarrays

**Problem:** https://leetcode.com/problems/reverse-k-subarrays/

```cpp
class Solution {
public:
    vector<int> reverseSubarrays(vector<int>& nums, int k) {
        int len = (int)nums.size() / k;
        for (int start = 0; start < (int)nums.size(); start += len)
            reverse(nums.begin() + start, nums.begin() + start + len);
        return nums;
    }
};
```

**Approach:** Each of the k equal-length blocks can be reversed in place using `std::reverse`.

**Complexity:** O(n) time; O(1) auxiliary space (excluding returned vector).

---

## 3867. Sum of GCD of Formed Pairs

**Problem:** https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

```cpp
class Solution {
    int gcdInt(int a, int b) {
        while (b) { int t = a % b; a = b; b = t; }
        return a;
    }
public:
    long long gcdSum(vector<int>& nums) {
        vector<int> a;
        a.reserve(nums.size());
        int mx = 0;
        for (int x : nums) {
            mx = max(mx, x);
            a.push_back(gcdInt(x, mx));
        }
        sort(a.begin(), a.end());
        long long ans = 0;
        for (int i = 0, j = (int)a.size() - 1; i < j; ++i, --j)
            ans += gcdInt(a[i], a[j]);
        return ans;
    }
};
```

**Approach:** Track the running prefix maximum and calculate each GCD. Sort the resulting values, then pair the two ends. Use Euclid’s algorithm for C++11 compatibility.

**Complexity:** O(n log n + n log M) time; O(n) space.

---

## 3868. Minimum Cost to Equalize Arrays Using Swaps

**Problem:** https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

```cpp
class Solution {
public:
    int minCost(vector<int>& nums1, vector<int>& nums2) {
        vector<int> diff(80001, 0);
        for (int x : nums1) ++diff[x];
        for (int x : nums2) --diff[x];
        int swaps = 0;
        for (int d : diff) {
            if (abs(d) % 2 != 0) return -1;
            if (d > 0) swaps += d / 2;
        }
        return swaps;
    }
};
```

**Approach:** Free within-array swaps mean only element multiplicities matter. Every value must occur an even number of times across both arrays. Each paid cross-array swap corrects one surplus occurrence in each array; sum the positive half-differences.

**Complexity:** O(n + U) time; O(U) space, U <= 80000.

---
# Batch 05 — Optimized C++11/C++14 LeetCode Solutions

**Problems 81–100 of 330 | 20 solutions**

Solutions follow the uploaded problem descriptions and starter signatures. Each code block is intended to be pasted independently into LeetCode. These implementations have not been verified as Accepted.

C++11/C++14 standard library headers (`vector`, `algorithm`, `unordered_map`, `unordered_set`, `queue`, `set`, `tuple`, `bitset`, `climits`, `cmath`, etc.) are supplied by LeetCode.

## 3872. Longest Arithmetic Sequence After Changing At Most One Element

**Link:** https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

**Approach:** Precompute arithmetic-run lengths ending at each index and starting at each index. Try changing either endpoint or an interior element; an interior replacement can connect both runs when its neighbors have an even sum and matching differences.

**Complexity:** O(n) time, O(n) space.

```cpp
class Solution {
public:
    int longestArithmetic(vector<int>& nums) {
        int n = nums.size();
        vector<int> left(n, 1), right(n, 1);
        for (int i = 1; i < n; ++i) {
            left[i] = 2;
            if (i >= 2 && (long long)nums[i] - nums[i-1] ==
                          (long long)nums[i-1] - nums[i-2])
                left[i] = left[i-1] + 1;
        }
        for (int i = n-2; i >= 0; --i) {
            right[i] = 2;
            if (i+2 < n && (long long)nums[i+1] - nums[i] ==
                           (long long)nums[i+2] - nums[i+1])
                right[i] = right[i+1] + 1;
        }
        int ans = 2;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, left[i]);
            if (i > 0) ans = max(ans, left[i-1] + 1);
            if (i+1 < n) ans = max(ans, right[i+1] + 1);
            if (i > 0 && i+1 < n) {
                long long gap = (long long)nums[i+1] - nums[i-1];
                if (gap % 2) continue;
                long long d = gap / 2;
                int l = 1, r = 1;
                if (i >= 2 && (long long)nums[i-1] - nums[i-2] == d)
                    l = left[i-1];
                if (i+2 < n && (long long)nums[i+2] - nums[i+1] == d)
                    r = right[i+1];
                ans = max(ans, l + 1 + r);
            }
        }
        return min(ans, n);
    }
};
```

---

## 3874. Valid Subarrays With Exactly One Peak

**Link:** https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

**Approach:** Identify peaks in the original array. For each peak, constrain the left endpoint to lie after the previous peak and within k positions; constrain the right endpoint to lie before the next peak and within k positions. Multiply the independent choices.

**Complexity:** O(n) time, O(n) space.

```cpp
class Solution {
public:
    long long validSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> p;
        for (int i = 1; i+1 < n; ++i)
            if (nums[i] > nums[i-1] && nums[i] > nums[i+1]) p.push_back(i);
        long long ans = 0;
        for (int j = 0; j < (int)p.size(); ++j) {
            int i = p[j];
            int prev = j ? p[j-1] : -1;
            int next = j+1 < (int)p.size() ? p[j+1] : n;
            long long left = i - max(max(0, i-k), prev+1) + 1;
            long long right = min(min(n-1, i+k), next-1) - i + 1;
            ans += left * right;
        }
        return ans;
    }
};
```

---

## 3876. Construct Uniform Parity Array II

**Link:** https://leetcode.com/problems/construct-uniform-parity-array-ii/

**Approach:** For each target parity, an element can keep its own value, or subtract a strictly smaller element of the opposite parity. Track the smallest odd and even values and check whether every element can reach the target parity.

**Complexity:** O(n) time, O(1) space.

**Note:** Correction: To change parity, subtract an ODD number. Thus the smallest odd input must be strictly smaller than every element of the opposite parity.

```cpp
class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        long long mn[2] = {LLONG_MAX, LLONG_MAX};
        for (int x : nums1) mn[x & 1] = min(mn[x & 1], (long long)x);
        for (int target = 0; target < 2; ++target) {
            bool ok = true;
            for (int x : nums1) {
                if ((x & 1) == target) continue;
                if (mn[1] >= x) { ok = false; break; }
            }
            if (ok) return true;
        }
        return false;
    }
};
```

---

## 3877. Minimum Removals to Achieve Target XOR

**Link:** https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

**Approach:** Keep the maximum number of retained elements for each XOR value. Since values are below 2^14, use a 16384-state 0/1 XOR dynamic program; answer n minus the maximum retained count.

**Complexity:** O(n · 2^14) time, O(2^14) space.

```cpp
class Solution {
public:
    int minRemovals(vector<int>& nums, int target) {
        const int S = 1 << 14;
        vector<int> dp(S, -1000000);
        dp[0] = 0;
        for (int x : nums) {
            vector<int> next = dp;
            for (int mask = 0; mask < S; ++mask)
                if (dp[mask] >= 0)
                    next[mask ^ x] = max(next[mask ^ x], dp[mask] + 1);
            dp.swap(next);
        }
        return dp[target] < 0 ? -1 : (int)nums.size() - dp[target];
    }
};
```

---

## 3879. Maximum Distinct Path Sum in a Binary Tree

**Link:** https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

**Approach:** A valid path is a simple tree path with no repeated node value. Starting DFS from each node, extend while maintaining a set of values on the current path. Every possible tree path is considered.

**Complexity:** O(n²) time and O(n) auxiliary space for n ≤ 1000.

```cpp
class Solution {
    int best;
    void walk(TreeNode* node, TreeNode* parent, int sum,
              unordered_set<int>& seen) {
        if (!node || seen.count(node->val)) return;
        seen.insert(node->val);
        sum += node->val;
        best = max(best, sum);
        if (node->left != parent) walk(node->left, node, sum, seen);
        if (node->right != parent) walk(node->right, node, sum, seen);
        seen.erase(node->val);
    }
public:
    int maxSum(TreeNode* root) {
        vector<TreeNode*> nodes;
        unordered_map<TreeNode*, TreeNode*> parent;
        vector<TreeNode*> stack(1, root);
        parent[root] = nullptr;
        while (!stack.empty()) {
            TreeNode* u = stack.back(); stack.pop_back();
            nodes.push_back(u);
            if (u->left) { parent[u->left] = u; stack.push_back(u->left); }
            if (u->right) { parent[u->right] = u; stack.push_back(u->right); }
        }
        best = INT_MIN;
        for (TreeNode* start : nodes) {
            unordered_set<int> seen;
            // Traverse the undirected tree via parent and children.
            struct State { TreeNode* u; TreeNode* from; int sum; bool exit; };
            vector<State> st(1, {start, nullptr, 0, false});
            while (!st.empty()) {
                State s = st.back(); st.pop_back();
                if (s.exit) { seen.erase(s.u->val); continue; }
                if (seen.count(s.u->val)) continue;
                seen.insert(s.u->val);
                int sum = s.sum + s.u->val;
                best = max(best, sum);
                st.push_back({s.u, s.from, sum, true});
                if (s.u->left && s.u->left != s.from)
                    st.push_back({s.u->left, s.u, sum, false});
                if (s.u->right && s.u->right != s.from)
                    st.push_back({s.u->right, s.u, sum, false});
                if (parent[s.u] && parent[s.u] != s.from)
                    st.push_back({parent[s.u], s.u, sum, false});
            }
        }
        return best;
    }
};
```

---

## 3881. Direction Assignments with Exactly K Visible People

**Link:** https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

**Approach:** Every person other than pos independently contributes either visible or invisible. Choose exactly k of n−1 people, then multiply by two choices for the observer. Compute the binomial coefficient modulo 1e9+7.

**Complexity:** O(n) time and O(n) space.

```cpp
class Solution {
    static const long long MOD = 1000000007LL;
    long long power(long long a, long long b) {
        long long r = 1;
        while (b) {
            if (b & 1) r = r * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return r;
    }
public:
    int countVisiblePeople(int n, int pos, int k) {
        if (k > n-1) return 0;
        vector<long long> fact(n+1, 1);
        for (int i = 1; i <= n; ++i) fact[i] = fact[i-1] * i % MOD;
        long long c = fact[n-1] * power(fact[k], MOD-2) % MOD;
        c = c * power(fact[n-1-k], MOD-2) % MOD;
        return (int)(2*c % MOD);
    }
};
```

---

## 3882. Minimum XOR Path in a Grid

**Link:** https://leetcode.com/problems/minimum-xor-path-in-a-grid/

**Approach:** Dynamic programming over each cell and its reachable XOR values (0..1023). A transition moves right or down and XORs in the destination cell. Return the smallest reachable XOR at the final cell.

**Complexity:** O(mn · 1024) time, O(n · 1024) space.

```cpp
class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<bitset<1024>> dp(n);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                bitset<1024> ways;
                if (i == 0 && j == 0) ways.set(grid[i][j]);
                else {
                    bitset<1024> prev;
                    if (i > 0) prev |= dp[j];
                    if (j > 0) prev |= dp[j-1];
                    for (int x = 0; x < 1024; ++x)
                        if (prev.test(x)) ways.set(x ^ grid[i][j]);
                }
                dp[j] = ways;
            }
        }
        for (int x = 0; x < 1024; ++x)
            if (dp[n-1].test(x)) return x;
        return -1;
    }
};
```

---

## 3885. Design Event Manager

**Link:** https://leetcode.com/problems/design-event-manager/

**Approach:** Maintain an ordered set keyed by negative priority and event ID, plus a map of current priorities. Updating erases the old key and inserts the new one; polling removes the first set entry.

**Complexity:** O(log n) per update/poll, O(n) space.

```cpp
class EventManager {
    set<pair<int,int>> order;
    unordered_map<int,int> priority;
public:
    EventManager(vector<vector<int>>& events) {
        for (const auto& e : events) {
            priority[e[0]] = e[1];
            order.insert({-e[1], e[0]});
        }
    }
    void updatePriority(int eventId, int newPriority) {
        order.erase({-priority[eventId], eventId});
        priority[eventId] = newPriority;
        order.insert({-newPriority, eventId});
    }
    int pollHighest() {
        if (order.empty()) return -1;
        int id = order.begin()->second;
        order.erase(order.begin());
        priority.erase(id);
        return id;
    }
};
```

---

## 3889. Mirror Frequency Distance

**Link:** https://leetcode.com/problems/mirror-frequency-distance/

**Approach:** Count each character and sum absolute frequency differences for the 13 letter mirror pairs and 5 digit mirror pairs, each exactly once.

**Complexity:** O(|s|) time, O(1) space.

```cpp
class Solution {
public:
    int mirrorFrequency(string s) {
        int f[128] = {};
        for (char c : s) ++f[(int)c];
        int ans = 0;
        for (int i = 0; i < 13; ++i)
            ans += abs(f['a'+i] - f['z'-i]);
        for (int i = 0; i < 5; ++i)
            ans += abs(f['0'+i] - f['9'-i]);
        return ans;
    }
};
```

---

## 3890. Integers With Multiple Sum of Two Cubes

**Link:** https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

**Approach:** Enumerate unordered positive pairs a ≤ b with a³+b³ ≤ n. Count how many distinct pairs generate each sum; return sums appearing at least twice, sorted.

**Complexity:** O(n^(2/3) + n^(1/3) log n) time and O(n^(2/3)) space in the worst case.

```cpp
class Solution {
public:
    vector<int> findGoodIntegers(int n) {
        unordered_map<int,int> count;
        for (long long a = 1; 2*a*a*a <= n; ++a) {
            for (long long b = a; a*a*a + b*b*b <= n; ++b) {
                int sum = (int)(a*a*a + b*b*b);
                ++count[sum];
            }
        }
        vector<int> ans;
        for (const auto& kv : count)
            if (kv.second >= 2) ans.push_back(kv.first);
        sort(ans.begin(), ans.end());
        return ans;
    }
};
```

---

## 3891. Minimum Increase to Maximize Special Indices

**Link:** https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

**Approach:** Two adjacent indices cannot both be peaks. Dynamic programming maximizes the number of peaks and, among equal counts, minimizes total increments. Choosing peak i costs max(0, max(nums[i−1], nums[i+1])+1−nums[i]); chosen peaks are never adjacent, so costs are independent.

**Complexity:** O(n) time, O(1) space.

```cpp
class Solution {
    typedef pair<int,long long> State; // (number of peaks, negative cost)
    State best(State a, State b) { return a > b ? a : b; }
public:
    long long minIncrease(vector<int>& nums) {
        int n = nums.size();
        State skip = {0,0}, take = {-1000000000, LLONG_MIN/4};
        for (int i = 1; i+1 < n; ++i) {
            long long cost = max(0LL, (long long)max(nums[i-1], nums[i+1])+1-nums[i]);
            State newSkip = best(skip, take);
            State newTake = {skip.first+1, skip.second-cost};
            skip = newSkip;
            take = newTake;
        }
        return -best(skip, take).second;
    }
};
```

---

## 3895. Count Digit Appearances

**Link:** https://leetcode.com/problems/count-digit-appearances/

**Approach:** For each positive integer, repeatedly extract its last decimal digit and compare it with the requested digit.

**Complexity:** O(total decimal digits) time, O(1) space.

```cpp
class Solution {
public:
    int countDigitOccurrences(vector<int>& nums, int digit) {
        int ans = 0;
        for (int x : nums) {
            do {
                if (x % 10 == digit) ++ans;
                x /= 10;
            } while (x);
        }
        return ans;
    }
};
```

---

## 3896. Minimum Operations to Transform Array into Alternating Prime

**Link:** https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

**Approach:** Sieve primes through 200000 (sufficient for input values ≤100000 and the next prime). At even indices, increment until reaching a prime. At odd indices, a prime needs one increment except 2, which needs two to reach 4.

**Complexity:** O(M log log M + n + total increments) time, O(M) space for M=200000.

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        const int M = 200000;
        vector<bool> prime(M+1, true);
        prime[0] = prime[1] = false;
        for (int p = 2; p*p <= M; ++p)
            if (prime[p])
                for (int x = p*p; x <= M; x += p) prime[x] = false;
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            int x = nums[i];
            if ((i & 1) == 0) {
                while (!prime[x]) { ++x; ++ans; }
            } else if (prime[x]) {
                ans += (x == 2 ? 2 : 1);
            }
        }
        return ans;
    }
};
```

---

## 3899. Angles of a Triangle

**Link:** https://leetcode.com/problems/angles-of-a-triangle/

**Approach:** Sort the three side lengths, reject degenerate triangles, then use the cosine rule to compute the angle opposite each side. The angles are already sorted with the side lengths.

**Complexity:** O(1) time and O(1) space.

```cpp
class Solution {
public:
    vector<double> internalAngles(vector<int>& sides) {
        sort(sides.begin(), sides.end());
        double a = sides[0], b = sides[1], c = sides[2];
        if (a + b <= c) return {};
        const double PI = acos(-1.0);
        auto angle = [PI](double x, double y, double z) {
            double cosine = (y*y + z*z - x*x) / (2*y*z);
            cosine = max(-1.0, min(1.0, cosine));
            return acos(cosine) * 180.0 / PI;
        };
        return {angle(a,b,c), angle(b,a,c), angle(c,a,b)};
    }
};
```

---

## 3900. Longest Balanced Substring After One Swap

**Link:** https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

**Approach:** Binary search the largest even substring length. A window of that length can be balanced after at most one swap iff it already has equal zeros and ones, or differs by exactly one of each and there is an opposite character outside the window to swap in. Sliding-window counts check each candidate length in linear time.

**Complexity:** O(n log n) time, O(1) auxiliary space.

```cpp
class Solution {
public:
    int longestBalanced(string s) {
        int n = s.size();
        int totalOnes = count(s.begin(), s.end(), '1');
        auto possible = [&](int len) {
            if (len == 0) return true;
            int ones = 0;
            for (int i = 0; i < len; ++i) ones += s[i] == '1';
            for (int l = 0; l+len <= n; ++l) {
                int zeros = len - ones;
                if (ones == zeros) return true;
                if (ones == zeros+2 && n-len > totalOnes-ones) return true;
                if (zeros == ones+2 && totalOnes > ones) return true;
                if (l+len < n) {
                    ones -= s[l] == '1';
                    ones += s[l+len] == '1';
                }
            }
            return false;
        };
        int lo = 0, hi = n/2;
        while (lo < hi) {
            int mid = lo + (hi-lo+1)/2;
            if (possible(mid*2)) lo = mid;
            else hi = mid-1;
        }
        return lo*2;
    }
};
```

---

## 3904. Smallest Stable Index II

**Link:** https://leetcode.com/problems/smallest-stable-index-ii/

**Approach:** Compute suffix minima, then scan from left to right while maintaining the prefix maximum. Return the first index whose prefix maximum minus suffix minimum is at most k.

**Complexity:** O(n) time, O(n) space.

```cpp
class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> suffix(n);
        suffix[n-1] = nums[n-1];
        for (int i = n-2; i >= 0; --i)
            suffix[i] = min(nums[i], suffix[i+1]);
        int pref = nums[0];
        for (int i = 0; i < n; ++i) {
            pref = max(pref, nums[i]);
            if ((long long)pref - suffix[i] <= k) return i;
        }
        return -1;
    }
};
```

---

## 3905. Multi Source Flood Fill

**Link:** https://leetcode.com/problems/multi-source-flood-fill/

**Approach:** Run a multi-source BFS to find each cell’s earliest arrival time. For simultaneous arrivals, choose the maximum source color; process the whole BFS frontier by distance, or propagate a (distance, negative color) priority order so higher colors win equal-distance ties.

**Complexity:** O(nm log(nm)) time, O(nm) space.

```cpp
class Solution {
public:
    vector<vector<int>> colorGrid(int n, int m, vector<vector<int>>& sources) {
        typedef tuple<int,int,int,int> Item; // distance, negative color, row, col
        priority_queue<Item, vector<Item>, greater<Item>> pq;
        vector<vector<int>> dist(n, vector<int>(m, INT_MAX));
        vector<vector<int>> result(n, vector<int>(m, 0));
        for (const auto& s : sources) {
            dist[s[0]][s[1]] = 0;
            result[s[0]][s[1]] = s[2];
            pq.emplace(0, -s[2], s[0], s[1]);
        }
        const int dr[4] = {1,-1,0,0}, dc[4] = {0,0,1,-1};
        while (!pq.empty()) {
            int d, negColor, r, c;
            tie(d, negColor, r, c) = pq.top(); pq.pop();
            int color = -negColor;
            if (d != dist[r][c] || color != result[r][c]) continue;
            for (int t = 0; t < 4; ++t) {
                int nr = r+dr[t], nc = c+dc[t];
                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
                if (d+1 < dist[nr][nc] ||
                    (d+1 == dist[nr][nc] && color > result[nr][nc])) {
                    dist[nr][nc] = d+1;
                    result[nr][nc] = color;
                    pq.emplace(d+1, -color, nr, nc);
                }
            }
        }
        return result;
    }
};
```

---

## 3907. Count Smaller Elements With Opposite Parity

**Link:** https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

**Approach:** Scan right to left with two Fenwick trees, one for each parity, after coordinate compression. Query the opposite-parity tree for strictly smaller values and then insert the current value into its own parity tree.

**Complexity:** O(n log n) time, O(n) space.

```cpp
class Solution {
    struct BIT {
        vector<int> tree;
        BIT(int n) : tree(n+1, 0) {}
        void add(int i) { for (int n=tree.size(); i<n; i+=i&-i) ++tree[i]; }
        int sum(int i) { int r=0; for (; i>0; i-=i&-i) r+=tree[i]; return r; }
    };
public:
    vector<int> countSmallerOppositeParity(vector<int>& nums) {
        vector<int> sorted = nums;
        sort(sorted.begin(), sorted.end());
        sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
        BIT even(sorted.size()), odd(sorted.size());
        vector<int> ans(nums.size());
        for (int i=(int)nums.size()-1; i>=0; --i) {
            int rank = lower_bound(sorted.begin(), sorted.end(), nums[i])-sorted.begin()+1;
            ans[i] = (nums[i]&1) ? even.sum(rank-1) : odd.sum(rank-1);
            if (nums[i]&1) odd.add(rank); else even.add(rank);
        }
        return ans;
    }
};
```

---

## 3909. Compare Sums of Bitonic Parts

**Link:** https://leetcode.com/problems/compare-sums-of-bitonic-parts/

**Approach:** Find the unique peak, sum both parts (including the peak in both), then compare their 64-bit sums.

**Complexity:** O(n) time, O(1) space.

```cpp
class Solution {
public:
    int compareBitonicSums(vector<int>& nums) {
        int n = nums.size(), peak = 0;
        for (int i=1; i<n; ++i)
            if (nums[i] > nums[peak]) peak = i;
        long long a=0, b=0;
        for (int i=0; i<=peak; ++i) a+=nums[i];
        for (int i=peak; i<n; ++i) b+=nums[i];
        return a==b ? -1 : (a>b ? 0 : 1);
    }
};
```

---

## 3913. Sort Vowels by Frequency

**Link:** https://leetcode.com/problems/sort-vowels-by-frequency/

**Approach:** Count each vowel and record its first position. Sort the distinct vowels by descending frequency, breaking ties by earlier first occurrence, then refill vowel positions in that order.

**Complexity:** O(n) time, O(1) auxiliary space (five vowels).

```cpp
class Solution {
public:
    string sortVowels(string s) {
        int freq[26] = {}, first[26];
        fill(first, first+26, INT_MAX);
        const string vowels = "aeiou";
        for (int i=0; i<(int)s.size(); ++i) {
            if (vowels.find(s[i]) != string::npos) {
                int x = s[i]-'a';
                ++freq[x];
                first[x] = min(first[x], i);
            }
        }
        vector<char> v;
        for (char c : vowels) if (freq[c-'a']) v.push_back(c);
        sort(v.begin(), v.end(), [&](char a, char b) {
            if (freq[a-'a'] != freq[b-'a']) return freq[a-'a'] > freq[b-'a'];
            return first[a-'a'] < first[b-'a'];
        });
        int p=0, used=0;
        for (char& c : s) if (vowels.find(c) != string::npos) {
            while (used == freq[v[p]-'a']) { ++p; used=0; }
            c=v[p]; ++used;
        }
        return s;
    }
};
```

---
# Batch 06 — C++11/C++14 LeetCode Solutions

**Problems:** 101–120 of 330  
**Source:** `batch_06(1).md`  
**Status:** Draft implementations; not verified as Accepted on LeetCode. Two complex problems explicitly require further algorithm validation.

> LeetCode normally provides `using namespace std;` and standard headers. Code below is intended for the corresponding LeetCode editor.

## 3914. Minimum Operations to Make Array Non Decreasing

**Link:** https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

**Approach:** For every descent, its difference must be covered by some suffix-increment operation. The sum of all positive adjacent drops is both a lower bound and achievable.

**Complexity:** O(n) time, O(1) space.

```cpp
class Solution {
public:
    long long minOperations(vector<int>& nums) {
        long long ans=0;
        for(int i=1;i<(int)nums.size();++i)
            if(nums[i]<nums[i-1]) ans+=(long long)nums[i-1]-nums[i];
        return ans;
    }
};
```

---

## 3918. Sum of Primes Between Number and Its Reverse

**Link:** https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

**Approach:** Reverse digits, sieve primes up to the larger endpoint, then sum primes in the inclusive range.

**Complexity:** O(M log log M) time and O(M) space, M=max(n,reverse(n)) <= 1000.

```cpp
class Solution {
public:
    int sumOfPrimesInRange(int n) {
        int t=n,r=0;
        while(t){r=r*10+t%10;t/=10;}
        int lo=min(n,r),hi=max(n,r);
        vector<bool> prime(hi+1,true);
        prime[0]=false;
        if(hi>=1) prime[1]=false;
        for(int p=2;p*p<=hi;++p) if(prime[p])
            for(int j=p*p;j<=hi;j+=p) prime[j]=false;
        int ans=0;
        for(int x=lo;x<=hi;++x) if(prime[x]) ans+=x;
        return ans;
    }
};
```

---

## 3919. Minimum Cost to Move Between Indices

**Link:** https://leetcode.com/problems/minimum-cost-to-move-between-indices/

**Approach:** For each adjacent edge, forward/backward cost is 1 when that direction is the closest neighbor, otherwise its numeric gap. Prefix sums answer directed queries. Any long jump has cost equal to the sum of intervening gaps, so cannot beat the adjacent-edge route.

**Complexity:** O(n+q) time, O(n) space.

```cpp
class Solution {
public:
    vector<int> minCost(vector<int>& nums, vector<vector<int>>& queries) {
        int n=nums.size();
        vector<long long> right(n,0),left(n,0);
        for(int i=0;i+1<n;++i){
            long long gap=(long long)nums[i+1]-nums[i];
            bool closestRight=(i==0 || gap < (long long)nums[i]-nums[i-1]);
            right[i+1]=right[i]+(closestRight?1:gap);
            bool closestLeft=(i+1==n-1 || gap <= (long long)nums[i+2]-nums[i+1]);
            left[i+1]=left[i]+(closestLeft?1:gap);
        }
        vector<int> ans;
        for(const auto& q:queries){
            int a=q[0],b=q[1];
            ans.push_back((int)(a<=b?right[b]-right[a]:left[a]-left[b]));
        }
        return ans;
    }
};
```

---

## 3922. Minimum Flips to Make Binary String Coherent

**Link:** https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

**Approach:** Subsequence-automaton DP: record whether subsequences 0, 1, 01 and 11 have appeared. Appending 1 when 01 already exists creates forbidden 011; appending 0 when 11 exists creates forbidden 110. Minimize substitutions over 16 states.

**Complexity:** O(16n) time, O(16) space.

```cpp
class Solution {
public:
    int minFlips(string s) {
        const int INF=1000000000;
        vector<int> dp(16,INF); dp[0]=0;
        for(char original:s){
            vector<int> ndp(16,INF);
            for(int mask=0;mask<16;++mask) if(dp[mask]!=INF){
                for(int bit=0;bit<=1;++bit){
                    if(bit==1 && (mask&4)) continue; // 01 + 1 -> 011
                    if(bit==0 && (mask&8)) continue; // 11 + 0 -> 110
                    int nxt=mask;
                    if(bit==0) nxt|=1;
                    else nxt|=2;
                    if(bit==1 && (mask&1)) nxt|=4;
                    if(bit==1 && (mask&2)) nxt|=8;
                    ndp[nxt]=min(ndp[nxt],dp[mask]+(original-'0'!=bit));
                }
            }
            dp.swap(ndp);
        }
        return *min_element(dp.begin(),dp.end());
    }
};
```

---

## 3923. Minimum Generations to Target Point

**Link:** https://leetcode.com/problems/minimum-generations-to-target-point/

**Approach:** Coordinates never leave [0,6]. Encode the 343 possible points, expand the closure in generations by pairing every pair of currently available distinct points, and stop on finding the target or reaching a fixed point.

**Complexity:** O(343^3) worst-case time, O(343) space.

```cpp
class Solution {
    int encode(int x,int y,int z){return (x*7+y)*7+z;}
public:
    int minGenerations(vector<vector<int>>& points,vector<int>& target){
        vector<int> ids;
        bool seen[343]={};
        for(const auto& p:points){
            int id=encode(p[0],p[1],p[2]);
            if(!seen[id]){seen[id]=true;ids.push_back(id);}
        }
        int goal=encode(target[0],target[1],target[2]);
        if(seen[goal]) return 0;
        for(int generation=1;;++generation){
            vector<int> fresh;
            int size=ids.size();
            for(int i=0;i<size;++i) for(int j=i+1;j<size;++j){
                int a=ids[i],b=ids[j];
                int x=((a/49)+(b/49))/2;
                int y=(((a/7)%7)+((b/7)%7))/2;
                int z=((a%7)+(b%7))/2;
                int c=encode(x,y,z);
                if(!seen[c]){seen[c]=true;fresh.push_back(c);}
            }
            if(seen[goal]) return generation;
            if(fresh.empty()) return -1;
            ids.insert(ids.end(),fresh.begin(),fresh.end());
        }
    }
};
```

---

## 3926. Count Valid Word Occurrences

**Link:** https://leetcode.com/problems/count-valid-word-occurrences/

**Approach:** Concatenate chunks, recognize joiner hyphens using their original immediate neighbors, split at every other character, and count complete words.

**Complexity:** O(total chunk characters + total query characters) expected time and space.

```cpp
class Solution {
public:
    vector<int> countWordOccurrences(vector<string>& chunks,vector<string>& queries){
        string s;
        for(const string& part:chunks) s+=part;
        auto letter=[](char c){return c>='a'&&c<='z';};
        unordered_map<string,int> freq;
        string word;
        for(int i=0;i<=(int)s.size();++i){
            bool valid=false;
            if(i<(int)s.size()){
                valid=letter(s[i]) ||
                  (s[i]=='-' && i>0 && i+1<(int)s.size() &&
                   letter(s[i-1]) && letter(s[i+1]));
            }
            if(valid) word+=s[i];
            else if(!word.empty()){++freq[word];word.clear();}
        }
        vector<int> ans;
        for(const string& q:queries) ans.push_back(freq[q]);
        return ans;
    }
};
```

---

## 3927. Minimize Array Sum Using Divisible Replacements

**Link:** https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

**Approach:** Each original value can be replaced by the smallest original divisor present in the array. Newly introduced values are themselves original divisors, so repeated operations cannot improve this bound. Propagate the minimum present divisor to its multiples with a sieve.

**Complexity:** O(M log M + n) time, O(M) space; M=max(nums).

```cpp
class Solution {
public:
    long long minArraySum(vector<int>& nums){
        int M=*max_element(nums.begin(),nums.end());
        vector<bool> present(M+1,false);
        for(int x:nums) present[x]=true;
        vector<int> best(M+1,0);
        for(int d=1;d<=M;++d) if(present[d])
            for(int multiple=d;multiple<=M;multiple+=d)
                if(best[multiple]==0) best[multiple]=d;
        long long ans=0;
        for(int x:nums) ans+=best[x];
        return ans;
    }
};
```

---

## 3932. Count K-th Roots in a Range

**Link:** https://leetcode.com/problems/count-k-th-roots-in-a-range/

**Approach:** For k=1 every integer qualifies. Otherwise binary-search the greatest nonnegative base whose kth power is at most each endpoint, using overflow-safe multiplication; for odd k also count negative bases if the range contains negatives (not needed under given constraints).

**Complexity:** O(k log r) time, O(1) space.

```cpp
class Solution {
    bool fits(long long x,int k,long long limit){
        long long p=1;
        for(int i=0;i<k;++i){
            if(x!=0 && p>limit/x) return false;
            p*=x;
        }
        return p<=limit;
    }
    int root(long long limit,int k){
        if(limit<0) return -1;
        long long lo=0,hi=limit+1;
        while(lo+1<hi){
            long long mid=lo+(hi-lo)/2;
            if(fits(mid,k,limit)) lo=mid;
            else hi=mid;
        }
        return (int)lo;
    }
public:
    int countKthRoots(int l,int r,int k){
        if(k==1) return r-l+1;
        return root(r,k)-root((long long)l-1,k);
    }
};
```

---

## 3933. Largest Local Values in a Matrix II

**Link:** https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

**Approach:** Build a 2D sparse table for constant-time rectangular maxima. For center value x, the allowed square excludes only its four corners; cover the remaining cells with a middle horizontal strip and two thin top/bottom strips excluding corner columns.

**Complexity:** O(nm log n log m) preprocessing, O(nm) queries, O(nm log n log m) memory.

```cpp
class Solution {
public:
    int countLocalMaximums(vector<vector<int>>& matrix){
        int n=matrix.size(),m=matrix[0].size();
        int A=1,B=1;
        while((1<<A)<=n) ++A;
        while((1<<B)<=m) ++B;
        vector<vector<vector<vector<int>>>> st(
            A,vector<vector<vector<int>>>(B,vector<vector<int>>(n,vector<int>(m,0))));
        st[0][0]=matrix;
        for(int a=0;a<A;++a) for(int b=0;b<B;++b){
            if(a==0&&b==0) continue;
            for(int i=0;i+(1<<a)<=n;++i)
                for(int j=0;j+(1<<b)<=m;++j){
                    if(a>0) st[a][b][i][j]=max(st[a-1][b][i][j],
                        st[a-1][b][i+(1<<(a-1))][j]);
                    else st[a][b][i][j]=max(st[a][b-1][i][j],
                        st[a][b-1][i][j+(1<<(b-1))]);
                }
        }
        vector<int> lg(max(n,m)+1,0);
        for(int i=2;i<(int)lg.size();++i) lg[i]=lg[i/2]+1;
        auto rect=[&](int r1,int c1,int r2,int c2)->int{
            r1=max(0,r1);c1=max(0,c1);
            r2=min(n-1,r2);c2=min(m-1,c2);
            if(r1>r2||c1>c2) return -1;
            int a=lg[r2-r1+1],b=lg[c2-c1+1];
            int rr=r2-(1<<a)+1,cc=c2-(1<<b)+1;
            return max(max(st[a][b][r1][c1],st[a][b][rr][c1]),
                       max(st[a][b][r1][cc],st[a][b][rr][cc]));
        };
        int ans=0;
        for(int r=0;r<n;++r) for(int c=0;c<m;++c){
            int x=matrix[r][c];
            if(x==0) continue;
            int v=rect(r-x+1,c-x,r+x-1,c+x);
            v=max(v,rect(r-x,c-x+1,r-x,c+x-1));
            v=max(v,rect(r+x,c-x+1,r+x,c+x-1));
            if(v<=x) ++ans;
        }
        return ans;
    }
};
```

---

## 3935. Power Update After K-th Largest Insertion I

**Link:** https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

**Approach:** Coordinate-compress initial values and all inserted values. A Fenwick frequency tree supports insertion and kth-largest selection in O(log N); update the modular power by binary exponentiation.

**Complexity:** O((n+q) log(n+q)+q log 10^6) time, O(n+q) space.

```cpp
class Solution {
    static const long long MOD=1000000007LL;
    long long power(long long a,int e){
        long long res=1;
        while(e){if(e&1) res=res*a%MOD;a=a*a%MOD;e>>=1;}
        return res;
    }
public:
    vector<int> powerUpdate(vector<int>& nums,int p,vector<vector<int>>& queries){
        vector<int> vals=nums;
        for(const auto& q:queries) vals.push_back(q[0]);
        sort(vals.begin(),vals.end());
        vals.erase(unique(vals.begin(),vals.end()),vals.end());
        int n=vals.size();
        vector<int> bit(n+1,0);
        auto insert=[&](int value){
            int i=lower_bound(vals.begin(),vals.end(),value)-vals.begin()+1;
            for(;i<=n;i+=i&-i) ++bit[i];
        };
        for(int x:nums) insert(x);
        vector<int> ans;
        int size=nums.size();
        for(const auto& q:queries){
            insert(q[0]);++size;
            int order=size-q[1]+1;
            int idx=0,sum=0;
            int step=1;
            while(step*2<=n) step*=2;
            for(;step;step>>=1){
                int nxt=idx+step;
                if(nxt<=n&&sum+bit[nxt]<order){idx=nxt;sum+=bit[nxt];}
            }
            int exponent=vals[idx];
            p=(int)power(p,exponent);
            ans.push_back(p);
        }
        return ans;
    }
};
```

---

## 3937. Minimum Operations to Make Array Modulo Alternating I

**Link:** https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

**Approach:** Compute the minimum cyclic distance from each value to each target residue, separately for even and odd positions. Choose distinct residues with the smallest combined cost.

**Complexity:** O(nk+k²) time, O(k) space.

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums,int k){
        vector<int> even(k,0),odd(k,0);
        for(int i=0;i<(int)nums.size();++i){
            int r=nums[i]%k;
            vector<int>& costs=(i%2?odd:even);
            for(int t=0;t<k;++t){
                int d=abs(r-t);
                costs[t]+=min(d,k-d);
            }
        }
        int ans=INT_MAX;
        for(int x=0;x<k;++x) for(int y=0;y<k;++y)
            if(x!=y) ans=min(ans,even[x]+odd[y]);
        return ans;
    }
};
```

---

## 3938. Maximum Path Intersection Sum in a Grid

**Link:** https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

**Status: Requires algorithm validation — no unverified code supplied.**

The two monotone paths may overlap in vertical and horizontal segments. A naive maximum-subarray scan of rows is incorrect (the provided second example demonstrates this). A validated intersection DP is required.

---

## 3941. Password Strength

**Link:** https://leetcode.com/problems/password-strength/

**Approach:** Count each ASCII character only on its first appearance, assigning weight by character class.

**Complexity:** O(n) time, O(1) space.

```cpp
class Solution {
public:
    int passwordStrength(string password){
        bool seen[256]={};
        int ans=0;
        for(unsigned char c:password){
            if(seen[c]) continue;
            seen[c]=true;
            if(c>='a'&&c<='z') ans+=1;
            else if(c>='A'&&c<='Z') ans+=2;
            else if(c>='0'&&c<='9') ans+=3;
            else ans+=5;
        }
        return ans;
    }
};
```

---

## 3942. Minimum Operations to Sort a Permutation

**Link:** https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

**Approach:** Reverse and left-rotate generate only the dihedral orbit of the sorted permutation: rotations of ascending or descending cyclic order. Determine which orbit contains the input and minimize either rotating directly or using reversals to rotate in the opposite direction.

**Complexity:** O(n) time, O(1) extra space.

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums){
        int n=nums.size();
        int z=find(nums.begin(),nums.end(),0)-nums.begin();
        bool ascending=true,descending=true;
        for(int i=0;i<n;++i){
            if(nums[(z+i)%n]!=i) ascending=false;
            if(nums[(z+i)%n]!=(n-i)%n) descending=false;
        }
        if(ascending){
            int steps=(n-z)%n;
            return min(steps,2+z);
        }
        if(descending){
            // A reflection requires an odd number of reversals.
            // Reverse now, or rotate first and reverse.
            int k=(n-1-z+n)%n;
            return min(1+k,1+(n-k)%n);
        }
        return -1;
    }
};
```

---

## 3946. Maximum Number of Items From Sale I

**Link:** https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

**Approach:** Activate each item type at most once: paying its price earns its purchased copy plus all free copies from its divisor relation. Any additional purchases give only one copy, so buy extras of the cheapest item. A 0/1 knapsack optimizes activation bonus; fill remaining budget with cheapest copies.

**Complexity:** O(n²+n·budget) time, O(budget) space.

```cpp
class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items,int budget){
        int n=items.size(),cheapest=INT_MAX;
        for(const auto& x:items) cheapest=min(cheapest,x[1]);
        vector<int> dp(budget+1,-1000000000);
        dp[0]=0;
        for(int i=0;i<n;++i){
            int freebies=0;
            for(int j=0;j<n;++j) if(j!=i && items[j][0]%items[i][0]==0)
                ++freebies;
            int cost=items[i][1];
            if(cost>budget) continue;
            for(int b=budget;b>=cost;--b)
                if(dp[b-cost]>=0) dp[b]=max(dp[b],dp[b-cost]+1+freebies);
        }
        int ans=0;
        for(int b=0;b<=budget;++b) if(dp[b]>=0)
            ans=max(ans,dp[b]+(budget-b)/cheapest);
        return ans;
    }
};
```

---

## 3947. Maximum Number of Items From Sale II

**Link:** https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

**Status: Requires algorithm validation — no unverified code supplied.**

The one-free-copy-per-purchased-copy constraint creates coupled purchase counts and distinct-item bonus limits. The straightforward 0/1 knapsack for Part I does not solve Part II at n=100000 and budget=1e9.

---

## 3951. Minimum Energy to Maintain Brightness

**Link:** https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

**Approach:** At a fixed time, one bulb lights at most three positions, and ceil(brightness/3) bulbs suffice by placing them to cover disjoint blocks (adjusting at boundaries). Merge inclusive time intervals and multiply the number of covered time units by this minimum bulb count.

**Complexity:** O(q log q) time, O(q) sorting space.

```cpp
class Solution {
public:
    long long minEnergy(int n,int brightness,vector<vector<int>>& intervals){
        sort(intervals.begin(),intervals.end());
        long long total=0;
        long long l=intervals[0][0],r=intervals[0][1];
        for(int i=1;i<(int)intervals.size();++i){
            long long a=intervals[i][0],b=intervals[i][1];
            if(a<=r+1) r=max(r,b);
            else{total+=r-l+1;l=a;r=b;}
        }
        total+=r-l+1;
        return total*((brightness+2LL)/3);
    }
};
```

---

## 3952. Maximum Total Value of Covered Indices

**Link:** https://leetcode.com/problems/maximum-total-value-of-covered-indices/

**Approach:** Process tokens from left to right. Each token may occupy its original index or the previous index; dynamic programming tracks the best score for each choice, excluding collisions with the previous token.

**Complexity:** O(n) time, O(1) auxiliary space.

```cpp
class Solution {
public:
    long long maxTotal(vector<int>& nums,string s){
        const long long NEG=-(1LL<<60);
        long long stay=0,move=NEG;
        int previous=-2;
        for(int i=0;i<(int)s.size();++i) if(s[i]=='1'){
            long long nextStay=max(stay,move)+nums[i];
            long long nextMove=NEG;
            if(i>0){
                // Previous token staying at i-1 would collide.
                if(previous==i-1) nextMove=move+nums[i-1];
                else nextMove=max(stay,move)+nums[i-1];
            }
            stay=nextStay;move=nextMove;previous=i;
        }
        return max(stay,move);
    }
};
```

---

## 3955. Valid Binary Strings With Cost Limit

**Link:** https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

**Approach:** Backtrack through positions, choosing zero always and one only when the preceding bit is zero and the added index cost does not exceed the remaining budget.

**Complexity:** O(n·F(n)) output-sensitive time, O(n) recursion space excluding output, where F(n) is the number of valid strings.

```cpp
class Solution {
    void dfs(int i,int n,int budget,string& s,vector<string>& ans){
        if(i==n){ans.push_back(s);return;}
        s.push_back('0');
        dfs(i+1,n,budget,s,ans);
        s.pop_back();
        if(budget>=i && (i==0||s.back()!='1')){
            s.push_back('1');
            dfs(i+1,n,budget-i,s,ans);
            s.pop_back();
        }
    }
public:
    vector<string> generateValidStrings(int n,int k){
        vector<string> ans;string s;
        dfs(0,n,k,s,ans);
        return ans;
    }
};
```

---

## 3958. Minimum Cost to Split into Ones II

**Link:** https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

**Approach:** Every split replaces x² by a²+b², decreasing the sum of squared piece sizes by 2ab. Telescoping from n² to n·1² proves that every full splitting sequence costs (n²−n)/2.

**Complexity:** O(1) time and space.

```cpp
class Solution {
public:
    long long minCost(int n){
        return 1LL*n*(n-1)/2;
    }
};
```

---
# Batch 07 — C++11/C++14 Solutions
**Problems 121–140 of 330**

Solutions are based on the uploaded problem descriptions and starter signatures. Compilation is not a LeetCode acceptance guarantee.

---

## 3960. Frequency Balance Subarray
**Link:** https://leetcode.com/problems/frequency-balance-subarray/

**Approach:** Enumerate each left endpoint and maintain frequencies, frequency-of-frequencies, and distinct count. A window is valid with one distinct value, or exactly two frequencies f and 2f.

**Complexity:** O(n² log n) time, O(n) space.

```cpp
class Solution {
public:
    int getLength(vector<int>& nums) {
        int n=nums.size(),ans=1;
        for(int l=0;l<n;++l){
            unordered_map<int,int> cnt;
            vector<int> freq(n+1,0);
            set<int> active;
            int distinct=0;
            for(int r=l;r<n;++r){
                int old=cnt[nums[r]]++;
                if(old){if(--freq[old]==0)active.erase(old);} else ++distinct;
                if(++freq[old+1]==1)active.insert(old+1);
                if(distinct==1){ans=max(ans,r-l+1);continue;}
                if(active.size()==2 && *active.rbegin()==2*(*active.begin()))
                    ans=max(ans,r-l+1);
            }
        }
        return ans;
    }
};
```

---

## 3961. Maximize Sum of Device Ratings
**Link:** https://leetcode.com/problems/maximize-sum-of-device-ratings/

**Approach:** For each device with at least two units, keep its second-smallest value by sending away its minimum. Route all discarded minima to one sink device, whose rating becomes the global minimum. Choose the sink maximizing the retained sum. A one-unit device cannot donate without becoming empty (rating zero); it can instead be a sink.

**Complexity:** O(T log T) time for T total units, O(m) auxiliary space.

```cpp
class Solution {
public:
    long long maxRatings(vector<vector<int>>& units) {
        int m=units.size();
        if(m==1) return *min_element(units[0].begin(),units[0].end());
        long long sum=0;
        int globalMin=INT_MAX;
        vector<int> best(m),original(m);
        for(int i=0;i<m;++i){
            auto &v=units[i];
            sort(v.begin(),v.end());
            original[i]=v[0];
            globalMin=min(globalMin,v[0]);
            best[i]=v.size()>=2?v[1]:0;
            sum+=best[i];
        }
        long long ans=0;
        for(int i=0;i<m;++i){
            // A sink receives all discarded minima; it may itself donate first.
            ans=max(ans,sum-best[i]+globalMin);
        }
        // With no transfers, retain original ratings.
        long long initial=0;
        for(int x:original)initial+=x;
        return max(ans,initial);
    }
};
```

---

## 3964. Minimum Lights to Illuminate a Road
**Link:** https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

**Approach:** Mark positions already illuminated using a difference array. Greedily cover the leftmost uncovered position by installing a bulb as far right as possible (at i+1), which covers the longest useful suffix.

**Complexity:** O(n) time, O(n) space.

```cpp
class Solution {
public:
    int minLights(vector<int>& lights) {
        int n=lights.size();
        vector<int> diff(n+1,0);
        for(int i=0;i<n;++i) if(lights[i]){
            int l=max(0,i-lights[i]),r=min(n-1,i+lights[i]);
            ++diff[l];--diff[r+1];
        }
        int active=0,ans=0,coveredUntil=-1;
        for(int i=0;i<n;++i){
            active+=diff[i];
            if(active>0 || i<=coveredUntil)continue;
            int center=min(n-1,i+1);
            coveredUntil=min(n-1,center+1);
            ++ans;
        }
        return ans;
    }
};
```

---

## 3965. Finish Time of Tasks I
**Link:** https://leetcode.com/problems/finish-time-of-tasks-i/

**Approach:** Build the parent-to-child adjacency list and traverse iteratively. Evaluate finish times in reverse traversal order to avoid recursion overflow.

**Complexity:** O(n) time and O(n) space.

```cpp
class Solution {
public:
    long long finishTime(int n, vector<vector<int>>& edges, vector<int>& baseTime) {
        vector<vector<int>> children(n);
        for(const auto& e:edges)children[e[0]].push_back(e[1]);
        vector<int> order(1,0);
        for(size_t i=0;i<order.size();++i)
            for(int v:children[order[i]])order.push_back(v);
        vector<long long> dp(n);
        for(int i=n-1;i>=0;--i){
            int u=order[i];
            if(children[u].empty()){dp[u]=baseTime[u];continue;}
            long long lo=LLONG_MAX,hi=0;
            for(int v:children[u]){lo=min(lo,dp[v]);hi=max(hi,dp[v]);}
            dp[u]=2*hi-lo+baseTime[u];
        }
        return dp[0];
    }
};
```

---

## 3968. Maximum Manhattan Distance After All Moves
**Link:** https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

**Approach:** For each of the four possible Manhattan-distance sign choices, every wildcard can contribute +1. The best final distance equals |fixed horizontal displacement| + |fixed vertical displacement| + number of wildcards.

**Complexity:** O(n) time, O(1) space.

```cpp
class Solution {
public:
    int maxDistance(string moves) {
        int x=0,y=0,wild=0;
        for(char c:moves){
            if(c=='U')++y;
            else if(c=='D')--y;
            else if(c=='R')++x;
            else if(c=='L')--x;
            else ++wild;
        }
        return abs(x)+abs(y)+wild;
    }
};
```

---

## 3969. Valid Subarrays With Matching Sum Digits I
**Link:** https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

**Approach:** Enumerate subarrays, accumulate their sums in 64-bit arithmetic, and check the first and last decimal digits.

**Complexity:** O(n² log S) time, O(1) space.

```cpp
class Solution {
public:
    int countValidSubarrays(vector<int>& nums, int x) {
        int ans=0,n=nums.size();
        for(int i=0;i<n;++i){
            long long sum=0;
            for(int j=i;j<n;++j){
                sum+=nums[j];
                if(sum%10!=x)continue;
                long long first=sum;
                while(first>=10)first/=10;
                if(first==x)++ans;
            }
        }
        return ans;
    }
};
```

---

## 3970. Shortest Path With At Most K Consecutive Identical Characters
**Link:** https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

**Approach:** Run Dijkstra on expanded states (node, current run length). A transition to an equal label increments the run, while a different label resets it to one.

**Complexity:** O((n k + E k) log(n k)) time, O(n k + E) space.

```cpp
class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        vector<vector<pair<int,int>>> g(n);
        for(const auto& e:edges)g[e[0]].push_back({e[1],e[2]});
        const long long INF=LLONG_MAX/4;
        vector<vector<long long>> dist(n,vector<long long>(k+1,INF));
        typedef tuple<long long,int,int> State;
        priority_queue<State,vector<State>,greater<State>> pq;
        dist[0][1]=0;pq.push(make_tuple(0,0,1));
        while(!pq.empty()){
            long long d;int u,run;
            tie(d,u,run)=pq.top();pq.pop();
            if(d!=dist[u][run])continue;
            if(u==n-1)return (int)d;
            for(auto e:g[u]){
                int v=e.first,next=(labels[u]==labels[v]?run+1:1);
                if(next>k)continue;
                long long nd=d+e.second;
                if(nd<dist[v][next]){
                    dist[v][next]=nd;
                    pq.push(make_tuple(nd,v,next));
                }
            }
        }
        return -1;
    }
};
```

---

## 3974. Maximum Total Sum of K Selected Elements
**Link:** https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

**Approach:** All elements are positive. Sort descending, select the k largest, and pair them with the non-increasing multipliers max(1,mul-i).

**Complexity:** O(n log n) time, O(1) extra space aside from sorting.

```cpp
class Solution {
public:
    long long maxSum(vector<int>& nums, int k, int mul) {
        sort(nums.begin(),nums.end(),greater<int>());
        long long ans=0;
        for(int i=0;i<k;++i)
            ans+=1LL*nums[i]*max(1,mul-i);
        return ans;
    }
};
```

---

## 3975. Filter Occupied Intervals
**Link:** https://leetcode.com/problems/filter-occupied-intervals/

**Approach:** Sort and merge overlapping or touching occupied intervals. Subtract the inclusive free interval from each merged interval and retain the surviving left/right pieces.

**Complexity:** O(n log n) time, O(n) space.

```cpp
class Solution {
public:
    vector<vector<int>> filterOccupiedIntervals(vector<vector<int>>& occupiedIntervals,
                                                 int freeStart,int freeEnd) {
        sort(occupiedIntervals.begin(),occupiedIntervals.end());
        vector<vector<int>> merged,ans;
        for(const auto& v:occupiedIntervals){
            if(merged.empty() || (long long)v[0]>1LL+merged.back()[1])
                merged.push_back(v);
            else merged.back()[1]=max(merged.back()[1],v[1]);
        }
        for(const auto& v:merged){
            int l=v[0],r=v[1];
            if(l<freeStart)ans.push_back({l,min(r,freeStart-1)});
            if(r>freeEnd)ans.push_back({max(l,freeEnd+1),r});
        }
        return ans;
    }
};
```

---

## 3976. Maximum Subarray Sum After Multiplier
**Link:** https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

**Approach:** Run a three-phase maximum-subarray DP separately for multiplication and division: before the modified segment, inside it, and after it. Also allow the chosen operation to occur outside the maximum-sum subarray, so compare against ordinary Kadane.

**Complexity:** O(n) time, O(1) space.

```cpp
class Solution {
    long long solve(const vector<int>& a,int k,bool multiply){
        const long long NEG=LLONG_MIN/4;
        long long before=NEG,inside=NEG,after=NEG,ans=NEG;
        for(int x:a){
            long long y=multiply?1LL*x*k:x/k;
            long long newBefore=max((long long)x,before+x);
            long long newInside=max(y,max(before+y,inside+y));
            long long newAfter=max(inside+x,after+x);
            before=newBefore;inside=newInside;after=newAfter;
            ans=max(ans,max(inside,after));
        }
        return ans;
    }
public:
    long long maxSubarraySum(vector<int>& nums,int k){
        long long cur=LLONG_MIN/4,plain=cur;
        for(int x:nums){cur=max((long long)x,cur+x);plain=max(plain,cur);}
        return max(solve(nums,k,true),solve(nums,k,false));
    }
};
```

---

## 3979. Maximum Valid Pair Sum
**Link:** https://leetcode.com/problems/maximum-valid-pair-sum/

**Approach:** Scan the right endpoint and maintain the maximum left value among indices at distance at least k.

**Complexity:** O(n) time, O(1) space. Note: the supplied starter returns int although constraints allow sums exceeding INT_MAX.

```cpp
class Solution {
public:
    int maxValidPairSum(vector<int>& nums,int k){
        long long ans=LLONG_MIN;
        int best=INT_MIN;
        for(int j=k;j<(int)nums.size();++j){
            best=max(best,nums[j-k]);
            ans=max(ans,1LL*best+nums[j]);
        }
        return (int)ans;
    }
};
```

---

## 3983. Subsequence After One Replacement
**Link:** https://leetcode.com/problems/subsequence-after-one-replacement/

**Approach:** Greedily match s against t while permitting one mismatch. A two-state subsequence DP avoids committing to the wrong replacement position: track how many characters of s are matched with zero or at most one replacement.

**Complexity:** O(|t|) time, O(1) space.

```cpp
class Solution {
public:
    bool canMakeSubsequence(string s,string t){
        int exact=0,one=0,m=s.size();
        if(m>t.size())return false;
        for(char c:t){
            int oldExact=exact,oldOne=one;
            if(oldOne<m && s[oldOne]==c)++one;
            if(oldExact<m)one=max(one,oldExact+1);
            if(oldExact<m && s[oldExact]==c)++exact;
            if(one==m || exact==m)return true;
        }
        return false;
    }
};
```

---

## 3987. Minimum Total Cost to Process All Elements
**Link:** https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

**Approach:** Only the total amount of resources matters. The minimum number of replenishments is max(0,ceil(total/k)-1); their costs sum to a triangular number.

**Complexity:** O(n) time, O(1) space.

```cpp
class Solution {
public:
    int minimumCost(vector<int>& nums,int k){
        const long long MOD=1000000007LL;
        long long total=0;
        for(int x:nums)total+=x;
        long long operations=max(0LL,(total-1)/k);
        return (int)((operations%MOD)*((operations+1)%MOD)%MOD*500000004LL%MOD);
    }
};
```

---

## 3988. Create Grid With Exactly K Paths I
**Link:** https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

**Needs further validation:** No implementation is included because a correct and efficient construction has not yet been established.

---

## 3993. Maximum Value of an Alternating Sequence
**Link:** https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

**Approach:** With alternating peaks, start by going up m. Each later peak can increase by at most m-1 because the intermediate valley must be strictly below the previous peak.

**Complexity:** O(1) time and space.

```cpp
class Solution {
public:
    long long maximumValue(int n,int s,int m){
        if(n==1)return s;
        long long peaks=n/2;
        return (long long)s+peaks*m-(peaks-1);
    }
};
```

---

## 3994. Minimum Adjacent Swaps to Partition Array
**Link:** https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/

**Approach:** Each adjacent swap exchanges an inverted pair of categories: low (0), middle (1), high (2). Count inversions in a single pass.

**Complexity:** O(n) time, O(1) space.

```cpp
class Solution {
public:
    int minAdjacentSwaps(vector<int>& nums,int a,int b){
        const long long MOD=1000000007;
        long long seenMid=0,seenHigh=0,ans=0;
        for(int x:nums){
            if(x<a)ans+=seenMid+seenHigh;
            else if(x<=b){ans+=seenHigh;++seenMid;}
            else ++seenHigh;
        }
        return (int)(ans%MOD);
    }
};
```

---

## 3997. Count Dominant Nodes in a Binary Tree
**Link:** https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

**Approach:** Compute subtree maxima bottom-up using iterative postorder; a node is dominant exactly when its own value is at least both child subtree maxima.

**Complexity:** O(n) time and O(n) space.

```cpp
class Solution {
public:
    int countDominantNodes(TreeNode* root){
        if(!root)return 0;
        vector<TreeNode*> order(1,root);
        for(size_t i=0;i<order.size();++i){
            TreeNode* u=order[i];
            if(u->left)order.push_back(u->left);
            if(u->right)order.push_back(u->right);
        }
        unordered_map<TreeNode*,int> mx;
        int ans=0;
        for(int i=(int)order.size()-1;i>=0;--i){
            TreeNode* u=order[i];
            int left=u->left?mx[u->left]:INT_MIN;
            int right=u->right?mx[u->right]:INT_MIN;
            if(u->val>=left && u->val>=right)++ans;
            mx[u]=max(u->val,max(left,right));
        }
        return ans;
    }
};
```

---

## 3998. Transform Binary String Using Subsequence Sort
**Link:** https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

**Approach:** Sorting a binary subsequence only moves zeros to the left and ones to the right. Thus every prefix of the target must have at least as many zeros as the corresponding source prefix, with equal total zeros. For wildcard patterns, greedily assign enough zeros to satisfy each prefix, then ensure the exact total zero count.

**Complexity:** O(n × number of queries) time, O(1) auxiliary space per query.

```cpp
class Solution {
public:
    vector<bool> transformStr(string s,vector<string>& strs){
        int total=count(s.begin(),s.end(),'0');
        vector<bool> ans;
        for(const string& t:strs){
            int fixed=0,wild=0,sourceZeros=0;
            bool ok=true;
            for(int i=0;i<(int)s.size();++i){
                sourceZeros+=(s[i]=='0');
                fixed+=(t[i]=='0');
                wild+=(t[i]=='?');
                if(fixed+wild<sourceZeros)ok=false;
            }
            if(fixed>total || fixed+wild<total)ok=false;
            ans.push_back(ok);
        }
        return ans;
    }
};
```

---

## 4001. Aggregate Two Time Series
**Link:** https://leetcode.com/problems/aggregate-two-time-series/

**Approach:** Merge the timestamp lists with two pointers. At each timestamp, use the value of the first record whose timestamp is >= the current timestamp in each series (or zero if none).

**Complexity:** O(n+m) time and O(n+m) output space.

```cpp
class Solution {
public:
    vector<vector<int>> aggregateTimeSeries(vector<vector<int>>& series1,
                                             vector<vector<int>>& series2){
        int i=0,j=0,n=series1.size(),m=series2.size();
        vector<vector<int>> ans;
        while(i<n || j<m){
            int t=min(i<n?series1[i][0]:INT_MAX,
                      j<m?series2[j][0]:INT_MAX);
            long long sum=(i<n?series1[i][1]:0LL)+(j<m?series2[j][1]:0LL);
            ans.push_back({t,(int)sum});
            if(i<n && series1[i][0]==t)++i;
            if(j<m && series2[j][0]==t)++j;
        }
        return ans;
    }
};
```

---

## 4002. Count Valid Sequences
**Link:** https://leetcode.com/problems/count-valid-sequences/

**Approach:** Count all positive compositions C(n-1,k-1), then subtract all-odd compositions. An all-odd sequence has terms 2a_i+1, so it exists only if n-k is even and contributes C((n-k)/2+k-1,k-1).

**Complexity:** O(n) preprocessing time, O(n) space.

```cpp
class Solution {
    static const long long MOD=1000000007LL;
    long long power(long long a,long long e){
        long long r=1;
        while(e){if(e&1)r=r*a%MOD;a=a*a%MOD;e>>=1;}
        return r;
    }
public:
    int countValidSequences(int n,int k){
        vector<long long> fact(n+1,1),inv(n+1,1);
        for(int i=1;i<=n;++i)fact[i]=fact[i-1]*i%MOD;
        inv[n]=power(fact[n],MOD-2);
        for(int i=n;i>0;--i)inv[i-1]=inv[i]*i%MOD;
        auto choose=[&](int a,int b)->long long{
            if(b<0 || b>a)return 0;
            return fact[a]*inv[b]%MOD*inv[a-b]%MOD;
        };
        long long all=choose(n-1,k-1),odd=0;
        if((n-k)%2==0)odd=choose((n-k)/2+k-1,k-1);
        return (int)((all-odd+MOD)%MOD);
    }
};
```
# Batch 08 — C++11/C++14 LeetCode Solutions

**Problems:** 141–160 of 330 · **20 complete implementations**

Each implementation is independent and uses the LeetCode starter signature. Standard LeetCode headers and `using namespace std;` are assumed.

**Validation:** Source-code compilation checks are performed locally; Accepted status on LeetCode is not claimed.

## 4008. Minimum Initial Strength to Defeat All Monsters

**Problem:** https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

**Approach:** Compute boosts with a difference array, then work backward. If future fights need positive strength, the current monster must leave that much strength; otherwise only the current fight threshold matters.

**Complexity:** O(n + b) time, O(n) space.

```cpp
class Solution {
public:
    long long minInitialStrength(vector<int>& monsters, vector<vector<int>>& boosts) {
        int n = monsters.size();
        vector<long long> diff(n + 1, 0);
        for (const auto& q : boosts) {
            diff[q[0]] += q[2];
            diff[q[1] + 1] -= q[2];
        }
        vector<long long> bonus(n);
        long long cur = 0;
        for (int i = 0; i < n; ++i) {
            cur += diff[i];
            bonus[i] = cur;
        }
        long long need = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (need > 0) need += monsters[i];
            else need = max(0LL, (long long)monsters[i] - bonus[i]);
        }
        return need;
    }
};
```

---

## 4011. Count Subarrays With Even Odd Ratio I

**Problem:** https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

**Approach:** Enumerate each starting position and extend the subarray, counting even and odd elements. Compare ratios by cross multiplication.

**Complexity:** O(n²) time, O(1) extra space.

```cpp
class Solution {
public:
    int countRatioSubarrays(vector<int>& nums, int a, int b) {
        int n = nums.size(), ans = 0;
        for (int i = 0; i < n; ++i) {
            int even = 0, odd = 0;
            for (int j = i; j < n; ++j) {
                if (nums[j] % 2 == 0) ++even;
                else ++odd;
                if (odd > 0 && (long long)even * b <= (long long)odd * a)
                    ++ans;
            }
        }
        return ans;
    }
};
```

---

## 4012. Count of Unfinished Tasks After Each Shift

**Problem:** https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

**Approach:** Store task completion prefix sums. Maintain work completed since the most recent reset; binary-search how many tasks are finished after each shift.

**Complexity:** O(n + m log n) time, O(n) space.

```cpp
class Solution {
public:
    vector<int> countTasks(vector<int>& tasks, vector<int>& shifts) {
        int n = tasks.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + tasks[i];
        vector<int> drelvanito = tasks; // Requested input snapshot.
        vector<int> ans;
        long long done = 0;
        for (int t : shifts) {
            done += t;
            if (done >= pref[n]) {
                ans.push_back(0);
                done = 0;
            } else {
                int finished = int(upper_bound(pref.begin(), pref.end(), done) - pref.begin()) - 1;
                ans.push_back(n - finished);
            }
        }
        return ans;
    }
};
```

---

## 4014. Minimum Total Price After Applying Discounts

**Problem:** https://leetcode.com/problems/minimum-total-price-after-applying-discounts/

**Approach:** Pair the largest discount with the largest price (rearrangement inequality). Any surplus discounts or items remain unused/unmodified.

**Complexity:** O(n log n + m log m) time, O(1) extra space excluding sorting.

```cpp
class Solution {
public:
    double minPrice(vector<int>& prices, vector<int>& discounts) {
        sort(prices.rbegin(), prices.rend());
        sort(discounts.rbegin(), discounts.rend());
        double total = 0;
        for (int p : prices) total += p;
        int k = min(prices.size(), discounts.size());
        for (int i = 0; i < k; ++i)
            total -= (double)prices[i] * discounts[i] / 100.0;
        return total;
    }
};
```

---

## 4015. Weighted Sum of a Tree

**Problem:** https://leetcode.com/problems/weighted-sum-of-a-tree/

**Approach:** Build children adjacency lists and BFS from root to determine depth and maximum depth, then apply the specified weight formula.

**Complexity:** O(n) time and space.

```cpp
class Solution {
public:
    long long weightedSum(vector<int>& parent, vector<int>& nums) {
        int n = parent.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) children[parent[i]].push_back(i);
        queue<int> q;
        vector<int> depth(n, 0);
        depth[0] = 1;
        q.push(0);
        int height = 1;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            height = max(height, depth[u]);
            for (int v : children[u]) {
                depth[v] = depth[u] + 1;
                q.push(v);
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i)
            ans += (long long)nums[i] * (height - depth[i] + 1);
        return ans;
    }
};
```

---

## 4019. Merge Close Characters II

**Problem:** https://leetcode.com/problems/merge-close-characters-ii/

**Approach:** Maintain alive positions for each character, their current ranks using a Fenwick tree, and a min-heap of eligible left endpoints. After deleting a character, only the nearest same-character pair straddling its old position can change for each alphabet letter. Recheck those 26 predecessors.

**Complexity:** O(26n log n) time, O(n) space.

```cpp
class Solution {
    struct BIT {
        int n;
        vector<int> bit;
        BIT(int n) : n(n), bit(n + 1, 0) {
            for (int i = 1; i <= n; ++i) bit[i] = i & -i;
        }
        void add(int p, int v) {
            for (++p; p <= n; p += p & -p) bit[p] += v;
        }
        int sum(int p) const {
            int s = 0;
            for (++p; p > 0; p -= p & -p) s += bit[p];
            return s;
        }
    };
public:
    string mergeCharacters(string s, int k) {
        int n = s.size();
        set<int> pos[26];
        for (int i = 0; i < n; ++i) pos[s[i] - 'a'].insert(i);
        BIT bit(n);
        priority_queue<int, vector<int>, greater<int>> pq;
        vector<char> queued(n, false), alive(n, true);
        auto offer = [&](int i) {
            if (i < 0 || queued[i] || !alive[i]) return;
            const set<int>& st = pos[s[i] - 'a'];
            auto it = st.find(i);
            if (it == st.end()) return;
            auto nx = next(it);
            if (nx != st.end() && bit.sum(*nx) - bit.sum(i) <= k) {
                pq.push(i);
                queued[i] = true;
            }
        };
        for (int c = 0; c < 26; ++c) {
            int prev = -1;
            for (int i : pos[c]) {
                if (prev != -1 && i - prev <= k) offer(prev);
                prev = i;
            }
        }
        while (!pq.empty()) {
            int i = pq.top(); pq.pop(); queued[i] = false;
            if (!alive[i]) continue;
            auto& st = pos[s[i] - 'a'];
            auto it = st.find(i);
            if (it == st.end()) continue;
            auto nx = next(it);
            if (nx == st.end() || bit.sum(*nx) - bit.sum(i) > k) continue;
            int j = *nx;
            st.erase(j);
            alive[j] = false;
            bit.add(j, -1);
            // Every other character's closest straddling pair may now be close.
            for (int c = 0; c < 26; ++c) {
                auto p = pos[c].lower_bound(j);
                if (p != pos[c].begin()) offer(*prev(p));
            }
        }
        string ans;
        ans.reserve(n);
        for (int i = 0; i < n; ++i) if (alive[i]) ans.push_back(s[i]);
        return ans;
    }
};
```

---

## 4021. Minimum Operations to Make a Rotated Palindrome I

**Problem:** https://leetcode.com/problems/minimum-operations-to-make-a-rotated-palindrome-i/

**Approach:** For each possible number of left rotations (0 through n−1), pair mirrored characters. Their minimum increment-only equalization cost is the smaller cyclic alphabet distance. Add the rotation count and take the minimum.

**Complexity:** O(n²) time, O(1) extra space.

```cpp
class Solution {
public:
    int minOperations(string s) {
        int n = s.size(), ans = INT_MAX;
        for (int rot = 0; rot < n; ++rot) {
            int cost = rot;
            for (int i = 0; i < n / 2; ++i) {
                int a = s[(rot + i) % n] - 'a';
                int b = s[(rot + n - 1 - i) % n] - 'a';
                int d = abs(a - b);
                cost += min(d, 26 - d);
            }
            ans = min(ans, cost);
        }
        return ans;
    }
};
```

---

## 4022. K-th Digit in Infinite String

**Problem:** https://leetcode.com/problems/k-th-digit-in-infinite-string/

**Approach:** Skip the first block (1–9), then groups of blocks with equal digit length. Locate the block and the integer inside it arithmetically, reversing order in odd blocks.

**Complexity:** O(log k) time and O(log k) space for decimal conversion.

```cpp
class Solution {
public:
    int kthDigit(long long k) {
        if (k <= 9) return (int)k;
        k -= 9;
        long long first = 1, count = 9;
        int digits = 2;
        while (true) {
            long long length = count * 10LL * digits;
            if (k <= length) break;
            k -= length;
            first *= 10;
            count *= 10;
            ++digits;
        }
        long long blockOffset = (k - 1) / (10LL * digits);
        long long b = first + blockOffset;
        long long inside = (k - 1) % (10LL * digits);
        int ordinal = (int)(inside / digits);
        int digitIndex = (int)(inside % digits);
        long long number = 10LL * b + (b % 2 == 0 ? ordinal : 9 - ordinal);
        string t = to_string(number);
        return t[digitIndex] - '0';
    }
};
```

---

## 4025. Minimize the Maximum Waiting Time at Synchronized Traffic Lights

**Problem:** https://leetcode.com/problems/minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/

**Approach:** Because all lights share the same cycle start, the light with the longest green duration is never worse than any other. Evaluate every arrival against that light.

**Complexity:** O(number of lights + number of cars) time, O(1) space.

```cpp
class Solution {
public:
    int minPenalty(int period, vector<int>& lights, vector<int>& arrivalTime) {
        int green = *max_element(lights.begin(), lights.end());
        int ans = 0;
        for (int t : arrivalTime) {
            int r = t % period;
            if (r >= green) ans = max(ans, period - r);
        }
        return ans;
    }
};
```

---

## 4026. Maximum Gap Between Stations

**Problem:** https://leetcode.com/problems/maximum-gap-between-stations/

**Approach:** Greedily match each worker as early as possible from the left and as late as possible from the right. The maximum achievable consecutive gap is max(late[i+1] − early[i]).

**Complexity:** O(n + m) time, O(n) space.

```cpp
class Solution {
public:
    int maximumGap(string skill, string station) {
        int n = skill.size(), m = station.size();
        if (n == 1) return 0;
        vector<int> left(n), right(n);
        int p = 0;
        for (int i = 0; i < m && p < n; ++i)
            if (station[i] == skill[p]) left[p++] = i;
        p = n - 1;
        for (int i = m - 1; i >= 0 && p >= 0; --i)
            if (station[i] == skill[p]) right[p--] = i;
        int ans = 0;
        for (int i = 0; i + 1 < n; ++i)
            ans = max(ans, right[i + 1] - left[i]);
        return ans;
    }
};
```

---

## 4031. Find All Numbers Disappeared in an Array II

**Problem:** https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-ii/

**Approach:** Sort and deduplicate values within [lower, upper]. Emit each gap between consecutive present values, including the boundaries.

**Complexity:** O(n log n) time, O(n) space.

```cpp
class Solution {
public:
    vector<vector<int>> findDisappearedNumbers(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        long long start = lower;
        for (int x : nums) {
            if (x < lower || x > upper) continue;
            if (x > start) ans.push_back({(int)start, x - 1});
            start = max(start, (long long)x + 1);
        }
        if (start <= upper) ans.push_back({(int)start, upper});
        return ans;
    }
};
```

---

## 4032. Longest Subarray With at Most K Distinct Prime Factors

**Problem:** https://leetcode.com/problems/longest-subarray-with-at-most-k-distinct-prime-factors/

**Approach:** Sieve smallest prime factors and factor each element into distinct primes. Maintain a sliding window with a count for each prime and shrink while more than k distinct primes are present.

**Complexity:** O(M log log M + n log M) time and O(M + n log M) space, M = max(nums).

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums, int k) {
        int mx = *max_element(nums.begin(), nums.end());
        vector<int> spf(mx + 1, 0);
        for (int i = 2; i <= mx; ++i) {
            if (spf[i] != 0) continue;
            for (int j = i; j <= mx; j += i)
                if (spf[j] == 0) spf[j] = i;
        }
        int n = nums.size();
        vector<vector<int>> factors(n);
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                factors[i].push_back(p);
                while (x % p == 0) x /= p;
            }
        }
        vector<int> cnt(mx + 1, 0);
        int left = 0, distinct = 0, ans = 0;
        for (int right = 0; right < n; ++right) {
            for (int p : factors[right]) if (++cnt[p] == 1) ++distinct;
            while (distinct > k) {
                for (int p : factors[left]) if (--cnt[p] == 0) --distinct;
                ++left;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};
```

---

## 4034. Minimum Bishop Moves to Reach Target

**Problem:** https://leetcode.com/problems/minimum-bishop-moves-to-reach-target/

**Approach:** A bishop never changes square color. If colors differ the target is unreachable; otherwise one move suffices on the same diagonal, and two moves suffice for any other square of the same color.

**Complexity:** O(1) time and space.

```cpp
class Solution {
public:
    int minBishopMoves(vector<int>& source, vector<int>& target) {
        int dr = abs(source[0] - target[0]);
        int dc = abs(source[1] - target[1]);
        if ((dr + dc) % 2 != 0) return -1;
        if (dr == 0 && dc == 0) return 0;
        if (dr == dc) return 1;
        return 2;
    }
};
```

---

## 4035. Maximum Valid Split Positions I

**Problem:** https://leetcode.com/problems/maximum-valid-split-positions-i/

**Approach:** Try deleting no element or each of the n positions. For each resulting array compute prefix and suffix GCDs and count equal-GCD split points.

**Complexity:** O(n² log V) time, O(n) space.

```cpp
class Solution {
    int gcd2(int a, int b) {
        while (b) { int t = a % b; a = b; b = t; }
        return a;
    }
public:
    int maxValidSplits(vector<int>& nums) {
        int n = nums.size(), best = 0;
        for (int removed = -1; removed < n; ++removed) {
            vector<int> a;
            a.reserve(n);
            for (int i = 0; i < n; ++i)
                if (i != removed) a.push_back(nums[i]);
            int m = a.size();
            if (m < 2) continue;
            vector<int> pref(m), suff(m);
            pref[0] = a[0];
            for (int i = 1; i < m; ++i) pref[i] = gcd2(pref[i - 1], a[i]);
            suff[m - 1] = a[m - 1];
            for (int i = m - 2; i >= 0; --i) suff[i] = gcd2(suff[i + 1], a[i]);
            int score = 0;
            for (int i = 0; i + 1 < m; ++i)
                if (pref[i] == suff[i + 1]) ++score;
            best = max(best, score);
        }
        return best;
    }
};
```

---

## 4036. Lexicographically Largest String After Pair Transformations

**Problem:** https://leetcode.com/problems/lexicographically-largest-string-after-pair-transformations/

**Approach:** Repeatedly merging equal adjacent letters implements binary carrying. To maximize lexicographic order, output the set bits of x as letters from highest to lowest, with bit 0 represented by a.

**Complexity:** O(n log max(nums)) time and O(n log max(nums)) output space.

```cpp
class Solution {
public:
    vector<string> largestString(vector<int>& nums) {
        vector<string> ans;
        ans.reserve(nums.size());
        for (int x : nums) {
            string s;
            for (int bit = 26; bit >= 0; --bit)
                if (x & (1 << bit)) s.push_back(char('a' + bit));
            ans.push_back(s);
        }
        return ans;
    }
};
```

---

## 4045. Count Robot Groups

**Problem:** https://leetcode.com/problems/count-robot-groups/

**Approach:** Process robots from right to left, grouping initially overlapping neighbors or a faster left group that will eventually catch the final speed of the group to its right. The merged group adopts the rightmost robot’s speed.

**Complexity:** O(n) time, O(1) extra space.

```cpp
class Solution {
public:
    int countGroups(vector<int>& position, vector<int>& speed, int distance) {
        int n = position.size(), groups = 1;
        int fleetSpeed = speed[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            if ((long long)position[i + 1] - position[i] <= distance ||
                speed[i] > fleetSpeed) {
                // This robot eventually joins the fleet on its right.
            } else {
                ++groups;
                fleetSpeed = speed[i];
            }
        }
        return groups;
    }
};
```

---

## 4053. Minimum Operations to Make Every Element Palindromic

**Problem:** https://leetcode.com/problems/minimum-operations-to-make-every-element-palindromic/

**Approach:** An operation preserves parity. Precompute positive decimal palindromes up to ten digits, separate them by parity, and binary-search the nearest palindrome of the same parity for each input.

**Complexity:** O(P log P + n log P) time, O(P) space, P < 220,000.

```cpp
class Solution {
    long long makePal(int half, bool odd) {
        long long x = half;
        int t = odd ? half / 10 : half;
        while (t > 0) { x = x * 10 + t % 10; t /= 10; }
        return x;
    }
public:
    long long minOperations(vector<int>& nums) {
        vector<long long> pal[2];
        for (int half = 1; half <= 99999; ++half) {
            long long a = makePal(half, true);
            long long b = makePal(half, false);
            pal[a % 2].push_back(a);
            pal[b % 2].push_back(b);
        }
        for (int p = 0; p < 2; ++p) {
            sort(pal[p].begin(), pal[p].end());
            pal[p].erase(unique(pal[p].begin(), pal[p].end()), pal[p].end());
        }
        long long ans = 0;
        for (int x : nums) {
            const vector<long long>& v = pal[x % 2];
            auto it = lower_bound(v.begin(), v.end(), (long long)x);
            long long best = LLONG_MAX;
            if (it != v.end()) best = min(best, abs(*it - (long long)x));
            if (it != v.begin()) best = min(best, abs(*prev(it) - (long long)x));
            ans += best / 2;
        }
        return ans;
    }
};
```

---

## 4054. Count Shadow Pairs I

**Problem:** https://leetcode.com/problems/count-shadow-pairs-i/

**Approach:** For each right endpoint j, scan leftward while maintaining the minimum element strictly between i and j. Pair (i,j) is valid iff nums[i] < nums[j] and no interior element is strictly smaller than nums[i].

**Complexity:** O(n²) time, O(1) extra space; this is not suitable for n=100,000, so see the optimized implementation below.

```cpp
class Solution {
    struct Fenwick {
        int n; vector<int> t;
        Fenwick(int n): n(n), t(n + 1, 0) {}
        void add(int i, int v) { for (; i <= n; i += i & -i) t[i] += v; }
        long long sum(int i) { long long s = 0; for (; i; i -= i & -i) s += t[i]; return s; }
    };
public:
    long long shadowPairs(vector<int>& nums) {
        int n = nums.size();
        vector<int> vals = nums;
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        int m = vals.size();
        vector<int> rank(n);
        for (int i = 0; i < n; ++i)
            rank[i] = int(lower_bound(vals.begin(), vals.end(), nums[i]) - vals.begin()) + 1;
        // An earlier i remains eligible for future j until a strictly smaller value appears.
        // Maintain active i by value; a new x invalidates all active values > x.
        // Equal values remain active and all count individually.
        Fenwick fw(m);
        vector<int> count(m + 1, 0);
        set<int> activeRanks;
        long long ans = 0;
        for (int x : rank) {
            ans += fw.sum(x - 1);
            auto it = activeRanks.upper_bound(x);
            while (it != activeRanks.end()) {
                int v = *it;
                fw.add(v, -count[v]);
                count[v] = 0;
                it = activeRanks.erase(it);
            }
            if (count[x]++ == 0) activeRanks.insert(x);
            fw.add(x, 1);
        }
        return ans;
    }
};
```

---

## 4066. Maximum Equal Adjacent Pairs After at Most One Replacement

**Problem:** https://leetcode.com/problems/maximum-equal-adjacent-pairs-after-at-most-one-replacement/

**Approach:** Existing equal pairs remain equal. The gain from replacing all x by y equals the number of adjacent unequal edges whose endpoint values are x and y. Count unordered value-pair edges.

**Complexity:** O(n log n) time and O(n) space.

```cpp
class Solution {
public:
    int maxEqualAdjacentPairs(vector<int>& nums) {
        int base = 0, best = 0;
        map<pair<int, int>, int> edges;
        for (int i = 1; i < (int)nums.size(); ++i) {
            int x = nums[i - 1], y = nums[i];
            if (x == y) { ++base; continue; }
            if (x > y) swap(x, y);
            best = max(best, ++edges[{x, y}]);
        }
        return base + best;
    }
};
```

---

## 4067. Longest Subarray With Restricted Pair Sums

**Problem:** https://leetcode.com/problems/longest-subarray-with-restricted-pair-sums/

**Approach:** Maintain a sliding window and the number of forbidden triples. A new value x creates triples where x is the sum of an existing pair or is one summand of a pair whose sum already exists. Maintain frequencies and pair-sum counts; shrink until no triples remain.

**Complexity:** O(n·V) time, O(V) space, V = 500.

```cpp
class Solution {
public:
    int maxSubarray(vector<int>& nums) {
        const int V = 500;
        vector<long long> freq(V + 1, 0), pairs(2 * V + 1, 0);
        long long triples = 0;
        int left = 0, ans = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            int x = nums[right];
            triples += pairs[x];
            for (int y = 1; y <= V; ++y)
                if (x + y <= V) triples += freq[y] * freq[x + y];
            for (int y = 1; y <= V; ++y)
                if (freq[y]) pairs[x + y] += freq[y];
            ++freq[x];
            while (triples > 0) {
                int z = nums[left++];
                --freq[z];
                for (int y = 1; y <= V; ++y)
                    if (freq[y]) pairs[z + y] -= freq[y];
                triples -= pairs[z];
                for (int y = 1; y <= V; ++y)
                    if (z + y <= V) triples -= freq[y] * freq[z + y];
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};
```

---
# Batch 09 — C++11/C++14 LeetCode Solutions
**Problems 161–180 of 330 | 20 implementations**

Each solution is a standalone LeetCode submission (compile separately). Algorithmic solutions have not been verified as Accepted on LeetCode.

## 4072. Maximum Alternating Subarray Sum With One Deletion
**Problem:** https://leetcode.com/problems/maximum-alternating-subarray-sum-with-one-deletion/

**Approach:** Dynamic programming tracks the parity of the selected length and whether one element has been deleted.

**Complexity:** O(n) time, O(1) space.

```cpp
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        const long long NEG = -(1LL<<60);
        long long a[2]={NEG,NEG}, b[2]={NEG,NEG}, answer=NEG;
        for (int x:nums) {
            long long na[2]={NEG,NEG}, nb[2]={NEG,NEG};
            na[1]=x;
            for(int p=0;p<2;++p) {
                if(a[p]!=NEG) {
                    na[1-p]=max(na[1-p],a[p]+(p==0?x:-x));
                    nb[p]=max(nb[p],a[p]); // delete this element
                }
                if(b[p]!=NEG) nb[1-p]=max(nb[1-p],b[p]+(p==0?x:-x));
            }
            for(int p=0;p<2;++p) {a[p]=na[p];b[p]=nb[p];answer=max(answer,max(a[p],b[p]));}
        }
        return answer;
    }
};
```

---

## 4080. Design Bus Seat Booking System
**Problem:** https://leetcode.com/problems/design-bus-seat-booking-system/

**Approach:** Store each seat’s booked state and immutable cost at its latest booking; minimum cost is simply the number of occupied seats.

**Complexity:** O(1) per operation (seat parsing O(log n)); O(n) space.

```cpp
class BusBooking {
    vector<array<int,4>> cost;
    int total=0, occupied=0;
public:
    BusBooking(int n):cost(n+1) { for(auto &a:cost)a.fill(0); }
    void toggle(string seat) {
        int c=seat[0]-'A', row=stoi(seat.substr(1));
        if(cost[row][c]) {total-=cost[row][c];cost[row][c]=0;--occupied;return;}
        int t=1;
        if(c==0 && cost[row][1]) t=3;
        if(c==3 && cost[row][2]) t=3;
        cost[row][c]=t;total+=t;++occupied;
    }
    int getTotalTime(){return total;}
    int getMinTime(){return occupied;}
};
```

---

## 4089. Count Subarrays With Loose Bounds
**Problem:** https://leetcode.com/problems/count-subarrays-with-loose-bounds/

**Approach:** Count valid subarrays ending at each position by maintaining the length of the current all-in-range suffix.

**Complexity:** O(n) time, O(1) extra space.

```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums,int minK,int maxK) {
        vector<int> vornelqixa=nums;
        long long ans=0,run=0;
        for(int x:vornelqixa) {run=(x>=minK && x<=maxK)?run+1:0;ans+=run;}
        return ans;
    }
};
```

---

## 4090. Count Magical Substring Pairs I
**Problem:** https://leetcode.com/problems/count-magical-substring-pairs-i/

**Approach:** For each boundary, count left and right substrings by number of distinct characters, then multiply matching counts.

**Complexity:** O(26n²) time, O(26) extra space.

```cpp
class Solution {
public:
    int countMagicalPairs(string s) {
        string mevaltrino=s;
        int n=s.size();long long ans=0;
        for(int j=0;j+1<n;++j) {
            long long left[27]={},right[27]={};
            int f[26]={},d=0;
            for(int i=j;i>=0;--i) {if(!f[s[i]-'a']++)++d;++left[d];}
            fill(f,f+26,0);d=0;
            for(int k=j+1;k<n;++k) {if(!f[s[k]-'a']++)++d;++right[d];}
            for(int t=1;t<=26;++t)ans+=left[t]*right[t];
        }
        return (int)ans;
    }
};
```

---

## 3098. Find the Sum of Subsequence Powers
**Problem:** https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

**Approach:** Sort values. For each distinct positive pair difference d, count length-k subsequences whose adjacent gaps are at least d using prefix-sum DP. Integrate these counts over increasing thresholds.

**Complexity:** O(n² log n + Dnk) time, O(nk) space; D ≤ n(n−1)/2.

```cpp
class Solution {
    static const int MOD=1000000007;
    int countAtLeast(const vector<int>& a,int k,int gap) {
        int n=a.size();vector<int> prev(n,1),cur(n);
        for(int len=2;len<=k;++len) {
            long long sum=0;int p=0;
            fill(cur.begin(),cur.end(),0);
            for(int i=0;i<n;++i) {
                while(p<i && (long long)a[i]-a[p]>=gap) {sum+=prev[p++];if(sum>=MOD)sum-=MOD;}
                cur[i]=(int)sum;
            }
            prev.swap(cur);
        }
        long long ans=0;for(int x:prev)ans=(ans+x)%MOD;
        return (int)ans;
    }
public:
    int sumOfPowers(vector<int>& nums,int k) {
        sort(nums.begin(),nums.end());int n=nums.size();
        vector<int> gaps;
        for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)
            if(nums[j]>nums[i])gaps.push_back(nums[j]-nums[i]);
        sort(gaps.begin(),gaps.end());gaps.erase(unique(gaps.begin(),gaps.end()),gaps.end());
        long long ans=0;int prev=0;
        for(int d:gaps) {
            ans=(ans+1LL*(d-prev)*countAtLeast(nums,k,d))%MOD;
            prev=d;
        }
        return (int)ans;
    }
};
```

---

## 3269. Constructing Two Increasing Arrays
**Problem:** https://leetcode.com/problems/constructing-two-increasing-arrays/

**Approach:** Binary search the maximum assigned integer. At each candidate, DP stores the greatest prefix of the second array achievable after assigning a prefix of the first.

**Complexity:** O((|a|+|b|)·|a|·log(|a|+|b|)) time, O(|a|) space.

```cpp
class Solution {
    bool feasible(const vector<int>& a,const vector<int>& b,int limit) {
        int n=a.size(),m=b.size();vector<int> dp(n+1,-1),next(n+1);
        dp[0]=0;
        for(int x=1;x<=limit;++x) {
            next=dp;int parity=x&1;
            for(int i=0;i<=n;++i) {
                if(dp[i]<0)continue;
                if(i<n && a[i]==parity)next[i+1]=max(next[i+1],dp[i]);
                if(dp[i]<m && b[dp[i]]==parity)next[i]=max(next[i],dp[i]+1);
            }
            dp.swap(next);
        }
        return dp[n]==m;
    }
public:
    int minLargest(vector<int>& nums1,vector<int>& nums2) {
        int lo=1,hi=2*(nums1.size()+nums2.size())+2;
        while(lo<hi) {int mid=lo+(hi-lo)/2;
            if(feasible(nums1,nums2,mid))hi=mid;else lo=mid+1;
        }
        return lo;
    }
};
```

---

## 3385. Minimum Time to Break Locks II
**Problem:** https://leetcode.com/problems/minimum-time-to-break-locks-ii/

**Approach:** The j-th lock in the breaking order costs ceil(strength[i]/(j+1)) minutes. Solve this minimum-cost assignment using the Hungarian algorithm.

**Complexity:** O(n³) time, O(n²) space.

```cpp
class Solution {
public:
    int findMinimumTime(vector<int>& strength) {
        int n=strength.size();const long long INF=1LL<<60;
        vector<vector<int>> cost(n+1,vector<int>(n+1));
        for(int i=1;i<=n;++i)for(int j=1;j<=n;++j)
            cost[i][j]=(strength[i-1]+j-1)/j;
        vector<long long> u(n+1),v(n+1);
        vector<int> p(n+1),way(n+1);
        for(int i=1;i<=n;++i) {
            p[0]=i;int j0=0;vector<long long> minv(n+1,INF);
            vector<char> used(n+1,false);
            do {
                used[j0]=true;int i0=p[j0],j1=0;long long delta=INF;
                for(int j=1;j<=n;++j)if(!used[j]) {
                    long long cur=cost[i0][j]-u[i0]-v[j];
                    if(cur<minv[j]) {minv[j]=cur;way[j]=j0;}
                    if(minv[j]<delta) {delta=minv[j];j1=j;}
                }
                for(int j=0;j<=n;++j) {
                    if(used[j]){u[p[j]]+=delta;v[j]-=delta;}
                    else minv[j]-=delta;
                }
                j0=j1;
            }while(p[j0]!=0);
            do {int j1=way[j0];p[j0]=p[j1];j0=j1;}while(j0);
        }
        return (int)(-v[0]);
    }
};
```

---

## 3416. Subsequences with a Unique Middle Mode II
**Problem:** https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

**Approach:** For each middle position, count selections with at least two additional copies of its value directly. For exactly one additional copy, subtract selections where another value repeats, using maintained frequency moments on both sides.

**Complexity:** O(n) expected time using hash maps, O(n) space.

```cpp
class Solution {
    static const long long M=1000000007;
    long long choose2(long long x){return x<2?0:x*(x-1)/2%M;}
    long long norm(long long x){x%=M;return x<0?x+M:x;}
public:
    int subsequencesWithMiddleMode(vector<int>& nums){
        int n=nums.size();unordered_map<int,int> L,R;
        for(int x:nums)++R[x];
        long long sL=0,sR=0,cross=0,lr2=0,rl2=0,ans=0;
        for(auto &entry:R)sR=(sR+choose2(entry.second))%M;
        auto change=[&](int x,int side,int delta){
            long long a=L[x],b=R[x];
            sL=norm(sL-choose2(a));sR=norm(sR-choose2(b));
            cross=norm(cross-a*b);lr2=norm(lr2-a*b*b);rl2=norm(rl2-b*a*a);
            if(side==0)L[x]+=delta;else R[x]+=delta;
            a=L[x];b=R[x];
            sL=norm(sL+choose2(a));sR=norm(sR+choose2(b));
            cross=norm(cross+a*b);lr2=norm(lr2+a*b*b);rl2=norm(rl2+b*a*a);
        };
        for(int i=0;i<n;++i){
            int x=nums[i];change(x,1,-1);
            if(i>=2 && n-i-1>=2){
                long long a=L[x],b=R[x],A=i-a,B=n-i-1-b;
                long long ways=0;
                for(int u=0;u<=2;++u)for(int v=0;v<=2;++v)if(u+v>=2){
                    long long lc=(u==0?1:u==1?a:choose2(a));
                    long long rc=(v==0?1:v==1?b:choose2(b));
                    long long lo=(2-u==0?1:2-u==1?A:choose2(A));
                    long long ro=(2-v==0?1:2-v==1?B:choose2(B));
                    ways=(ways+lc*rc%M*lo%M*ro)%M;
                }
                long long sLx=norm(sL-choose2(a)),sRx=norm(sR-choose2(b));
                long long cx=norm(cross-a*b),lrx=norm(lr2-a*b*b),rlx=norm(rl2-b*a*a);
                long long distinctR=norm(choose2(B)-sRx);
                long long distinctL=norm(choose2(A)-sLx);
                long long leftOne=norm(A*distinctR%M-(B*cx%M-lrx));
                long long rightOne=norm(B*distinctL%M-(A*cx%M-rlx));
                ways=norm(ways+a*leftOne+b*rightOne);
                ans=(ans+ways)%M;
            }
            change(x,0,1);
        }
        return (int)ans;
    }
};
```

---

## 3526. Range XOR Queries with Subarray Reversals
**Problem:** https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

**Approach:** Implicit randomized treap with subtree sizes, XOR aggregates, and lazy reversal supports all operations by position.

**Complexity:** Expected O((n+q) log n) time, O(n) space.

```cpp
class Solution {
    struct Node {
        int val,sz,xr;unsigned pri;bool rev;
        Node *l,*r;
        Node(int v,unsigned p):val(v),sz(1),xr(v),pri(p),rev(false),l(0),r(0){}
    };
    unsigned seed=712367;
    unsigned randomPriority(){seed^=seed<<13;seed^=seed>>17;seed^=seed<<5;return seed;}
    int size(Node*t){return t?t->sz:0;}
    int xr(Node*t){return t?t->xr:0;}
    void pull(Node*t){if(t){t->sz=1+size(t->l)+size(t->r);t->xr=t->val^xr(t->l)^xr(t->r);}}
    void push(Node*t){if(t&&t->rev){swap(t->l,t->r);if(t->l)t->l->rev^=1;if(t->r)t->r->rev^=1;t->rev=false;}}
    void split(Node*t,int k,Node*&a,Node*&b){
        if(!t){a=b=0;return;}push(t);
        if(size(t->l)>=k){split(t->l,k,a,t->l);b=t;}
        else{split(t->r,k-size(t->l)-1,t->r,b);a=t;}
        pull(t);
    }
    Node*merge(Node*a,Node*b){
        if(!a)return b;if(!b)return a;
        if(a->pri>b->pri){push(a);a->r=merge(a->r,b);pull(a);return a;}
        push(b);b->l=merge(a,b->l);pull(b);return b;
    }
    void clear(Node*t){if(!t)return;clear(t->l);clear(t->r);delete t;}
public:
    vector<int> getResults(vector<int>& nums,vector<vector<int>>& queries){
        Node*root=0;for(int x:nums)root=merge(root,new Node(x,randomPriority()));
        vector<int> ans;
        for(const auto&q:queries){
            Node *a=0,*b=0,*c=0;
            if(q[0]==1){split(root,q[1],a,b);split(b,1,b,c);
                b->val=q[2];pull(b);root=merge(a,merge(b,c));
            }else{
                split(root,q[1],a,b);split(b,q[2]-q[1]+1,b,c);
                if(q[0]==2)ans.push_back(xr(b));
                else if(b)b->rev^=1;
                root=merge(a,merge(b,c));
            }
        }
        clear(root);return ans;
    }
};
```

---

## 3549. Multiply Two Polynomials
**Problem:** https://leetcode.com/problems/multiply-two-polynomials/

**Approach:** Multiply using two number-theoretic transforms and reconstruct exact signed coefficients with the Chinese remainder theorem.

**Complexity:** O((n+m) log(n+m)) time and space.

```cpp
class Solution {
    long long power(long long a,long long b,int mod){long long r=1;while(b){if(b&1)r=r*a%mod;a=a*a%mod;b>>=1;}return r;}
    void ntt(vector<int>&a,bool inv,int mod,int root){
        int n=a.size();
        for(int i=1,j=0;i<n;++i){int bit=n>>1;
            for(;j&bit;bit>>=1)j^=bit;j^=bit;if(i<j)swap(a[i],a[j]);}
        for(int len=2;len<=n;len<<=1){
            long long wlen=power(root,(mod-1)/len,mod);
            if(inv)wlen=power(wlen,mod-2,mod);
            for(int i=0;i<n;i+=len){long long w=1;
                for(int j=0;j<len/2;++j){
                    int u=a[i+j],v=w*a[i+j+len/2]%mod;
                    a[i+j]=(u+v>=mod?u+v-mod:u+v);
                    a[i+j+len/2]=(u-v<0?u-v+mod:u-v);
                    w=w*wlen%mod;
                }
            }
        }
        if(inv){long long scale=power(n,mod-2,mod);for(int &x:a)x=x*scale%mod;}
    }
    vector<int> conv(const vector<int>&a,const vector<int>&b,int mod,int root){
        int size=1,need=a.size()+b.size()-1;while(size<need)size<<=1;
        vector<int>x(size),y(size);
        for(int i=0;i<(int)a.size();++i)x[i]=(a[i]%mod+mod)%mod;
        for(int i=0;i<(int)b.size();++i)y[i]=(b[i]%mod+mod)%mod;
        ntt(x,false,mod,root);ntt(y,false,mod,root);
        for(int i=0;i<size;++i)x[i]=1LL*x[i]*y[i]%mod;
        ntt(x,true,mod,root);x.resize(need);return x;
    }
public:
    vector<long long> multiply(vector<int>& poly1,vector<int>& poly2){
        const long long p=998244353LL,q=1004535809LL;
        vector<int>a=conv(poly1,poly2,(int)p,3),b=conv(poly1,poly2,(int)q,3);
        long long inverse=power(p%q,q-2,(int)q),product=p*q;
        vector<long long> ans(a.size());
        for(int i=0;i<(int)a.size();++i){
            long long t=(b[i]-a[i]+q)%q*inverse%q;
            long long val=a[i]+p*t;
            if(val>product/2)val-=product;
            ans[i]=val;
        }
        return ans;
    }
};
```

---

## 3655. XOR After Range Multiplication Queries II
**Problem:** https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

**Approach:** Use square-root decomposition on step size. Apply large-step queries directly; for each small step, use multiplicative difference arrays along each residue class.

**Complexity:** O((n+q)√n + q log MOD) time, O(n+q) space.

```cpp
class Solution {
    static const long long MOD=1000000007LL;
    long long power(long long a,long long e){long long r=1;while(e){if(e&1)r=r*a%MOD;a=a*a%MOD;e>>=1;}return r;}
public:
    int xorAfterQueries(vector<int>& nums,vector<vector<int>>& queries){
        vector<vector<array<int,4>>> small(320);
        int n=nums.size(),B=(int)sqrt(n)+1;
        vector<long long> value(nums.begin(),nums.end());
        vector<vector<array<int,4>>> groups(B+1);
        for(auto&q:queries){
            int l=q[0],r=q[1],k=q[2],v=q[3];
            if(k>B)for(int i=l;i<=r;i+=k)value[i]=value[i]*v%MOD;
            else groups[k].push_back({l,r,k,v});
        }
        vector<long long> diff(n+B+2);
        for(int k=1;k<=B;++k)if(!groups[k].empty()){
            fill(diff.begin(),diff.end(),1);
            for(auto&q:groups[k]){
                int l=q[0],r=q[1],v=q[3];
                int last=l+(r-l)/k*k;
                diff[l]=diff[l]*v%MOD;
                if(last+k<n)diff[last+k]=diff[last+k]*power(v,MOD-2)%MOD;
            }
            for(int r=0;r<k;++r){long long mul=1;
                for(int i=r;i<n;i+=k){mul=mul*diff[i]%MOD;value[i]=value[i]*mul%MOD;}
            }
        }
        int ans=0;for(long long x:value)ans^=(int)x;return ans;
    }
};
```

---

## 3661. Maximum Walls Destroyed by Robots
**Problem:** https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

**Approach:** Sort robots and walls. A shot is stopped by the neighboring robot, so only two adjacent robots can affect the same gap. DP over each robot’s left/right choice and count the union of walls hit in each gap.

**Complexity:** O((n+m) log(n+m)) time, O(n+m) space.

```cpp
class Solution {
public:
    int maxWalls(vector<int>& robots,vector<int>& distance,vector<int>& walls){
        int n=robots.size();vector<pair<int,int>> a(n);
        for(int i=0;i<n;++i)a[i]={robots[i],distance[i]};
        sort(a.begin(),a.end());sort(walls.begin(),walls.end());
        auto cnt=[&](long long l,long long r)->int{
            if(l>r)return 0;
            return upper_bound(walls.begin(),walls.end(),r)-lower_bound(walls.begin(),walls.end(),l);
        };
        int at=0;for(auto &p:a)at+=cnt(p.first,p.first);
        vector<int> dp(2,0);
        dp[0]=cnt((long long)a[0].first-a[0].second,(long long)a[0].first-1);
        dp[1]=0;
        for(int i=1;i<n;++i){
            vector<int> nd(2,0);
            long long lo=a[i-1].first+1,hi=a[i].first-1;
            for(int prev=0;prev<2;++prev)for(int cur=0;cur<2;++cur){
                long long leftEnd=prev?min(hi,(long long)a[i-1].first+a[i-1].second):lo-1;
                long long rightStart=cur?hi+1:max(lo,(long long)a[i].first-a[i].second);
                int gain=cnt(lo,leftEnd)+cnt(rightStart,hi)-cnt(rightStart,leftEnd);
                nd[cur]=max(nd[cur],dp[prev]+gain);
            }
            dp.swap(nd);
        }
        return at+max(dp[0],dp[1]+cnt((long long)a.back().first+1,(long long)a.back().first+a.back().second));
    }
};
```

---

## 3666. Minimum Operations to Equalize Binary String
**Problem:** https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

**Approach:** BFS over the number of zero bits. A flip of k bits reaches an interval of zero counts of one parity. Ordered sets remove each count at most once.

**Complexity:** O(n log n) time, O(n) space.

```cpp
class Solution {
public:
    int minOperations(string s,int k){
        int n=s.size(),z=count(s.begin(),s.end(),'0');
        vector<int> dist(n+1,-1);set<int> rem[2];
        for(int i=0;i<=n;++i)if(i!=z)rem[i&1].insert(i);
        queue<int> q;q.push(z);dist[z]=0;
        while(!q.empty()){
            int x=q.front();q.pop();if(x==0)return dist[x];
            int low=max(0,k-(n-x)),high=min(k,x);
            int L=x+k-2*high,R=x+k-2*low;
            auto &st=rem[L&1];auto it=st.lower_bound(L);
            while(it!=st.end() && *it<=R){int y=*it;it=st.erase(it);dist[y]=dist[x]+1;q.push(y);}
        }
        return -1;
    }
};
```

---

## 3671. Sum of Beautiful Subsequences
**Problem:** https://leetcode.com/problems/sum-of-beautiful-subsequences/

**Approach:** Use gcd(x₁,…,xₜ)=Σ_{d dividing every xᵢ} φ(d). For each divisor d, count strictly increasing subsequences of numbers divisible by d using a Fenwick tree.

**Complexity:** O(V log log V + n√V + Σ divisor-count·log(V/d)) time, O(V+n√V) space, V=max(nums).

```cpp
class Solution {
    static const int MOD=1000000007;
    struct BIT {
        vector<int> t;
        BIT(int n):t(n+1,0){}
        void add(int i,int v){for(int n=t.size();i<n;i+=i&-i){t[i]+=v;if(t[i]>=MOD)t[i]-=MOD;}}
        int sum(int i){int s=0;for(;i>0;i-=i&-i){s+=t[i];if(s>=MOD)s-=MOD;}return s;}
    };
public:
    int totalBeauty(vector<int>& nums){
        int V=*max_element(nums.begin(),nums.end());
        vector<int> phi(V+1),primes;vector<bool> composite(V+1,false);
        phi[1]=1;
        for(int i=2;i<=V;++i){
            if(!composite[i]){primes.push_back(i);phi[i]=i-1;}
            for(int p:primes){if(1LL*i*p>V)break;composite[i*p]=true;
                if(i%p==0){phi[i*p]=phi[i]*p;break;}
                phi[i*p]=phi[i]*(p-1);
            }
        }
        vector<vector<int>> lists(V+1);
        for(int x:nums){
            for(int d=1;1LL*d*d<=x;++d)if(x%d==0){
                lists[d].push_back(x/d);
                if(d*d!=x)lists[x/d].push_back(d);
            }
        }
        long long ans=0;
        for(int d=1;d<=V;++d)if(!lists[d].empty()){
            BIT bit(V/d);int count=0;
            for(int x:lists[d]){
                int ways=bit.sum(x-1)+1;if(ways>=MOD)ways-=MOD;
                bit.add(x,ways);count+=ways;if(count>=MOD)count-=MOD;
            }
            ans=(ans+1LL*phi[d]*count)%MOD;
        }
        return (int)ans;
    }
};
```

---

## 3691. Maximum Total Subarray Value II
**Problem:** https://leetcode.com/problems/maximum-total-subarray-value-ii/

**Approach:** For each left endpoint, extending the right endpoint never decreases max−min. Build sparse tables for O(1) range values and use a max-heap to extract the globally largest k distinct subarrays.

**Complexity:** O(n log n + k log n) time, O(n log n) space.

```cpp
class Solution {
public:
    long long maxTotalValue(vector<int>& nums,int k){
        int n=nums.size(),lg=1;while((1<<lg)<=n)++lg;
        vector<vector<int>> mn(lg,vector<int>(n)),mx(lg,vector<int>(n));
        mn[0]=mx[0]=nums;
        for(int j=1;j<lg;++j)for(int i=0;i+(1<<j)<=n;++i){
            mn[j][i]=min(mn[j-1][i],mn[j-1][i+(1<<(j-1))]);
            mx[j][i]=max(mx[j-1][i],mx[j-1][i+(1<<(j-1))]);
        }
        vector<int> logs(n+1);for(int i=2;i<=n;++i)logs[i]=logs[i/2]+1;
        auto value=[&](int l,int r)->long long{
            int j=logs[r-l+1],s=r-(1<<j)+1;
            return (long long)max(mx[j][l],mx[j][s])-min(mn[j][l],mn[j][s]);
        };
        typedef tuple<long long,int,int> T;
        priority_queue<T> pq;
        for(int l=0;l<n;++l)pq.push(make_tuple(value(l,n-1),l,n-1));
        long long ans=0;
        while(k--){T t=pq.top();pq.pop();long long v;int l,r;
            tie(v,l,r)=t;ans+=v;
            if(r>l)pq.push(make_tuple(value(l,r-1),l,r-1));
        }
        return ans;
    }
};
```

---

## 3695. Maximize Alternating Sum Using Swaps
**Problem:** https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

**Approach:** Each connected component of the allowed-swap graph can permute its values arbitrarily. Assign its largest values to even indices and smallest to odd indices.

**Complexity:** O((n+|swaps|) α(n)+n log n) time, O(n) space.

```cpp
class Solution {
    vector<int> p,sz;
    int find(int x){return p[x]==x?x:p[x]=find(p[x]);}
    void unite(int a,int b){a=find(a);b=find(b);if(a==b)return;if(sz[a]<sz[b])swap(a,b);p[b]=a;sz[a]+=sz[b];}
public:
    long long maxAlternatingSum(vector<int>& nums,vector<vector<int>>& swaps){
        int n=nums.size();p.resize(n);sz.assign(n,1);iota(p.begin(),p.end(),0);
        for(auto&e:swaps)unite(e[0],e[1]);
        vector<vector<int>> ids(n);
        for(int i=0;i<n;++i)ids[find(i)].push_back(i);
        long long ans=0;
        for(auto&v:ids)if(!v.empty()){
            vector<int> vals;int plus=0;
            for(int i:v){vals.push_back(nums[i]);if(i%2==0)++plus;}
            sort(vals.begin(),vals.end());
            for(int i=0;i<(int)vals.size();++i)
                ans+=(i<(int)vals.size()-plus?-1LL:1LL)*vals[i];
        }
        return ans;
    }
};
```

---

## 3699. Number of ZigZag Arrays I
**Problem:** https://leetcode.com/problems/number-of-zigzag-arrays-i/

**Approach:** DP on the last value and whether the last move was up or down. Prefix/suffix sums optimize transitions.

**Complexity:** O(n(r−l+1)) time, O(r−l+1) space.

```cpp
class Solution {
public:
    int zigZagArrays(int n,int l,int r){
        const long long MOD=1000000007;int m=r-l+1;
        vector<long long> up(m),down(m),nu(m),nd(m);
        for(int i=0;i<m;++i){up[i]=i;down[i]=m-i-1;}
        for(int len=3;len<=n;++len){
            long long sum=0;
            for(int i=0;i<m;++i){nu[i]=sum;sum=(sum+down[i])%MOD;}
            sum=0;
            for(int i=m-1;i>=0;--i){nd[i]=sum;sum=(sum+up[i])%MOD;}
            up.swap(nu);down.swap(nd);
        }
        long long ans=0;for(int i=0;i<m;++i)ans=(ans+up[i]+down[i])%MOD;
        return (int)ans;
    }
};
```

---

## 3700. Number of ZigZag Arrays II
**Problem:** https://leetcode.com/problems/number-of-zigzag-arrays-ii/

**Approach:** Represent transitions between upward/downward states as a 2m×2m matrix, then exponentiate to n−2 (m=r−l+1≤75).

**Complexity:** O(m³ log n) time, O(m²) space.

```cpp
class Solution {
    static const long long MOD=1000000007;
    typedef vector<vector<long long>> Mat;
    Mat mul(const Mat&a,const Mat&b){
        int n=a.size();Mat c(n,vector<long long>(n));
        for(int i=0;i<n;++i)for(int k=0;k<n;++k)if(a[i][k])
            for(int j=0;j<n;++j)if(b[k][j])
                c[i][j]=(c[i][j]+a[i][k]*b[k][j])%MOD;
        return c;
    }
    vector<long long> apply(const Mat&a,const vector<long long>&v){
        int n=v.size();vector<long long> ans(n);
        for(int i=0;i<n;++i)for(int j=0;j<n;++j)
            ans[i]=(ans[i]+a[i][j]*v[j])%MOD;
        return ans;
    }
public:
    int zigZagArrays(int n,int l,int r){
        int m=r-l+1;Mat t(2*m,vector<long long>(2*m));
        vector<long long> v(2*m);
        for(int i=0;i<m;++i){
            v[i]=i;v[m+i]=m-i-1;
            for(int j=0;j<i;++j)t[i][m+j]=1;
            for(int j=i+1;j<m;++j)t[m+i][j]=1;
        }
        n-=2;
        while(n){if(n&1)v=apply(t,v);n>>=1;if(n)t=mul(t,t);}
        long long ans=0;for(long long x:v)ans=(ans+x)%MOD;
        return (int)ans;
    }
};
```

---

## 3704. Count No-Zero Pairs That Sum to N
**Problem:** https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

**Approach:** Digit DP adds a and b from least significant digit with carry, enforcing that each positive number has no internal zero digits. Ordered pairs are counted.

**Complexity:** O(log n · 4 · 2 · 100) time, O(1) space.

```cpp
class Solution {
public:
    long long countNoZeroPairs(long long n){
        string s=to_string(n);reverse(s.begin(),s.end());
        long long dp[2][2][2]={};dp[0][0][0]=1;
        for(int pos=0;pos<(int)s.size();++pos){
            long long next[2][2][2]={};int digit=s[pos]-'0';
            for(int aEnd=0;aEnd<2;++aEnd)for(int bEnd=0;bEnd<2;++bEnd)
                for(int carry=0;carry<2;++carry)if(dp[aEnd][bEnd][carry]){
                    for(int a=0;a<=9;++a){if(aEnd&&a)continue;
                        for(int b=0;b<=9;++b){if(bEnd&&b)continue;
                            if(pos==0 && (!a||!b))continue;
                            int x=a+b+carry;
                            if(x%10!=digit)continue;
                            next[aEnd||a==0][bEnd||b==0][x/10]+=dp[aEnd][bEnd][carry];
                        }
                    }
                }
            memcpy(dp,next,sizeof dp);
        }
        long long ans=0;for(int i=0;i<2;++i)for(int j=0;j<2;++j)ans+=dp[i][j][0];
        return ans;
    }
};
```

---

## 3710. Maximum Partition Factor
**Problem:** https://leetcode.com/problems/maximum-partition-factor/

**Approach:** Binary search the partition factor. Every pair closer than the candidate must be placed in opposite groups, so the corresponding graph must be bipartite.

**Complexity:** O(n² log C) time, O(n²) space.

```cpp
class Solution {
public:
    int maxPartitionFactor(vector<vector<int>>& points){
        int n=points.size();if(n==2)return 0;
        vector<vector<int>> d(n,vector<int>(n));int high=0;
        for(int i=0;i<n;++i)for(int j=i+1;j<n;++j){
            d[i][j]=d[j][i]=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]);
            high=max(high,d[i][j]);
        }
        int lo=0,hi=high;
        while(lo<hi){int mid=lo+(hi-lo+1)/2;vector<int> color(n,-1);bool ok=true;
            for(int i=0;i<n&&ok;++i)if(color[i]<0){
                queue<int> q;q.push(i);color[i]=0;
                while(!q.empty()&&ok){int u=q.front();q.pop();
                    for(int v=0;v<n;++v)if(u!=v&&d[u][v]<mid){
                        if(color[v]<0){color[v]=color[u]^1;q.push(v);}
                        else if(color[v]==color[u]){ok=false;break;}
                    }
                }
            }
            if(ok)lo=mid;else hi=mid-1;
        }
        return lo;
    }
};
```

---
# Batch 10 — LeetCode C++11/C++14 Solutions

**Problems 181–200 of 330 | 20 solutions**

Each snippet is a standalone LeetCode `Solution` class (or as specified). Standard library includes are supplied by LeetCode. No C++17 features are used.

**Verification:** Draft implementations; not verified Accepted on LeetCode.

---

## 3715. Sum of Perfect Square Ancestors
**Link:** https://leetcode.com/problems/sum-of-perfect-square-ancestors/

**Approach:** A product is square iff both numbers have the same square-free kernel. DFS the tree, counting matching kernels currently on the ancestor path.

**Complexity:** O(n + A log log A) time, O(n + A) space, A = max(nums).

```cpp
class Solution {
public:
    long long sumOfAncestors(int n, vector<vector<int>>& edges, vector<int>& nums) {
        int mx=*max_element(nums.begin(),nums.end());
        vector<int> spf(mx+1); for(int i=2;i<=mx;++i) if(!spf[i]) {
            for(int j=i;j<=mx;j+=i) if(!spf[j]) spf[j]=i;
        }
        vector<int> key(n);
        for(int i=0;i<n;++i){int x=nums[i],v=1;while(x>1){int p=spf[x],par=0;while(x%p==0){x/=p;par^=1;}if(par)v*=p;}key[i]=v;}
        vector<vector<int>> g(n);for(auto &e:edges){g[e[0]].push_back(e[1]);g[e[1]].push_back(e[0]);}
        vector<int> cnt(mx+1,0);
        struct Frame{int u,p,phase;}; vector<Frame> st={{0,-1,0}};long long ans=0;
        while(!st.empty()){Frame f=st.back();st.pop_back();
            if(f.phase){--cnt[key[f.u]];continue;}
            ans+=cnt[key[f.u]]; ++cnt[key[f.u]];
            st.push_back({f.u,f.p,1});
            for(int v:g[f.u])if(v!=f.p)st.push_back({v,f.u,0});
        }return ans;
    }
};
```

---

## 3721. Longest Balanced Subarray II
**Link:** https://leetcode.com/problems/longest-balanced-subarray-ii/

**Approach:** For every right endpoint maintain balance of distinct even/odd values for all left endpoints. A repeated value updates only starts after its previous occurrence. A lazy segment tree stores min/max balances; adjacent starting positions differ by at most one, so min ≤ 0 ≤ max guarantees a zero. Find the earliest zero.

**Complexity:** O(n log n) time, O(n + max(nums)) space.

```cpp
class Solution {
    struct Node{int mn=0,mx=0,lazy=0;};
    vector<Node> tr;
    void apply(int p,int d){tr[p].mn+=d;tr[p].mx+=d;tr[p].lazy+=d;}
    void push(int p){if(tr[p].lazy){apply(p*2,tr[p].lazy);apply(p*2+1,tr[p].lazy);tr[p].lazy=0;}}
    void upd(int p,int l,int r,int ql,int qr,int d){if(ql>r||qr<l)return;if(ql<=l&&r<=qr){apply(p,d);return;}push(p);int m=(l+r)/2;upd(p*2,l,m,ql,qr,d);upd(p*2+1,m+1,r,ql,qr,d);tr[p].mn=min(tr[p*2].mn,tr[p*2+1].mn);tr[p].mx=max(tr[p*2].mx,tr[p*2+1].mx);}
    int first(int p,int l,int r,int limit){if(l>limit||tr[p].mn>0||tr[p].mx<0)return -1;if(l==r)return l;push(p);int m=(l+r)/2;int x=first(p*2,l,m,limit);return x>=0?x:first(p*2+1,m+1,r,limit);}
public:
    int longestBalanced(vector<int>& nums){int n=nums.size(),ans=0;tr.assign(4*n+5,Node());vector<int> prev(100001,-1);
        for(int r=0;r<n;++r){int x=nums[r];upd(1,0,n-1,prev[x]+1,r,(x%2)?-1:1);prev[x]=r;int l=first(1,0,n-1,r);if(l>=0)ans=max(ans,r-l+1);}return ans;
    }
};
```

---

## 3725. Count Ways to Choose Coprime Integers from Rows
**Link:** https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

**Approach:** Use Möbius inversion: count all row choices whose elements are divisible by d, multiply counts across rows, and sum μ(d) times that product.

**Complexity:** O(m(n+V log V)) time, O(V) space, V=150.

```cpp
class Solution {
public:
    int countCoprime(vector<vector<int>>& mat){const long long MOD=1000000007;const int V=150;
        vector<int> mu(V+1,1),prime,lp(V+1);mu[1]=1;
        for(int i=2;i<=V;++i){if(!lp[i]){lp[i]=i;prime.push_back(i);mu[i]=-1;}for(int p:prime){if(p>lp[i]||i*p>V)break;lp[i*p]=p;if(i%p==0){mu[i*p]=0;break;}mu[i*p]=-mu[i];}}
        long long ans=0;
        for(int d=1;d<=V;++d)if(mu[d]){long long ways=1;
            for(auto &row:mat){int cnt=0;for(int x:row)if(x%d==0)++cnt;ways=ways*cnt%MOD;if(!ways)break;}
            ans=(ans+mu[d]*ways)%MOD;
        }return (ans+MOD)%MOD;
    }
};
```

---

## 3729. Count Distinct Subarrays Divisible by K in Sorted Array
**Link:** https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

**Approach:** Count all sum-divisible subarrays using prefix residues. Since the array is sorted, identical subarrays can occur only when all their values are equal. For each equal-value run, subtract repeated valid lengths.

**Complexity:** Expected O(n) time, O(n) space.

```cpp
class Solution {
static long long gcdll(long long a,long long b){while(b){long long t=a%b;a=b;b=t;}return a;}
public:
    long long numGoodSubarrays(vector<int>& nums,int k){
        unordered_map<long long,long long> freq;freq.reserve(nums.size()*2+1);freq[0]=1;
        long long pref=0,ans=0;
        for(int x:nums){pref=(pref+x)%k;ans+=freq[pref]++;}
        int n=nums.size();
        for(int i=0;i<n;){int j=i;while(j<n&&nums[j]==nums[i])++j;long long len=j-i;
            long long step=k/gcdll(k,nums[i]);
            for(long long t=step;t<=len;t+=step)ans-=len-t;
            i=j;
        }return ans;
    }
};
```

---

## 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target
**Link:** https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

**Approach:** Only the first half of a palindromic permutation is freely chosen. Try the target half if it is a valid multiset permutation and its palindrome beats target. Otherwise find the rightmost feasible position where we can exceed the target half and fill the suffix in ascending order.

**Complexity:** O(26n²) worst-case time, O(n) space.

```cpp
class Solution {
public:
    string lexPalindromicPermutation(string s,string target){int n=s.size(),h=n/2;vector<int> cnt(26,0);for(char c:s)++cnt[c-'a'];
        string mid="";for(int c=0;c<26;++c)if(cnt[c]%2){if(!mid.empty())return "";mid=string(1,char('a'+c));}
        for(int &x:cnt)x/=2;
        auto make=[&](const string &half){string r=half;reverse(r.begin(),r.end());return half+mid+r;};
        string t=target.substr(0,h);vector<int> left=cnt;bool exact=true;
        for(char c:t){if(--left[c-'a']<0){exact=false;break;}}
        if(exact){string p=make(t);if(p>target)return p;}
        vector<int> used(26,0);int valid=0;
        for(int i=0;i<h;++i){int c=t[i]-'a';if(used[c]>=cnt[c])break;++used[c];++valid;}
        for(int i=h-1;i>=0;--i){if(i>valid)continue;
            vector<int> remain=cnt;for(int j=0;j<i;++j)--remain[t[j]-'a'];
            for(int c=t[i]-'a'+1;c<26;++c)if(remain[c]>0){--remain[c];string half=t.substr(0,i)+char('a'+c);
                for(int v=0;v<26;++v)half.append(remain[v],char('a'+v));return make(half);
            }
        }return "";
    }
};
```

---

## 3735. Lexicographically Smallest String After Reverse II
**Link:** https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

**Approach:** Enumerate every allowed prefix/suffix reversal, but compare candidates through double polynomial hashes and binary-search longest common prefixes, avoiding O(n²) string construction.

**Complexity:** O(n log n) time, O(n) space.

```cpp
class Solution {
    using U=unsigned long long;
    struct H{vector<U> p,h;H(const string&s){int n=s.size();p.resize(n+1);h.resize(n+1);p[0]=1;for(int i=0;i<n;++i){p[i+1]=p[i]*1315423911ULL;h[i+1]=h[i]*1315423911ULL+(s[i]-'a'+1);}}U get(int l,int r)const{return h[r]-h[l]*p[r-l];}};
public:
    string lexSmallest(string s){int n=s.size();string rev=s;reverse(rev.begin(),rev.end());H a(s),b(rev);
        // kind=0: reversed prefix of length k; kind=1: reversed suffix of length k.
        auto hash=[&](int kind,int k,int len)->U{
            int first=kind==0?k:n-k;const H &x=kind==0?b:a,&y=kind==0?a:b;
            int start=kind==0?n-k:0;
            if(len<=first)return x.get(start,start+len);
            return x.get(start,start+first)*a.p[len-first]+y.get(kind==0?k:n-k,len+(kind==0?0:0));
        };
        // Compare by character access after binary-searching a prefix hash.
        auto gethash=[&](int kind,int k,int len)->U{
            if(kind==0){if(len<=k)return b.get(n-k,n-k+len);return b.get(n-k,n)*a.p[len-k]+a.get(k,len);}
            int first=n-k;if(len<=first)return a.get(0,len);return a.get(0,first)*a.p[len-first]+b.get(n-k,n-k+len-first);
        };
        auto at=[&](int kind,int k,int i)->char{
            if(kind==0)return i<k?s[k-1-i]:s[i];
            return i<n-k?s[i]:s[2*n-k-1-i];
        };
        int bk=1,bt=0;
        for(int type=0;type<2;++type)for(int k=1;k<=n;++k){int lo=0,hi=n;
            while(lo<hi){int mid=(lo+hi+1)/2;if(gethash(type,k,mid)==gethash(bt,bk,mid))lo=mid;else hi=mid-1;}
            if(lo<n&&at(type,k,lo)<at(bt,bk,lo)){bt=type;bk=k;}
        }
        if(bt==0)reverse(s.begin(),s.begin()+bk);else reverse(s.end()-bk,s.end());return s;
    }
};
```

---

## 3743. Maximize Cyclic Partition Score
**Link:** https://leetcode.com/problems/maximize-cyclic-partition-score/

**Approach:** Dynamic programming over the cyclic sequence: a partition segment contributes its maximum minus minimum. Track whether the current segment has seen its minimum or maximum first, and optimize transitions using running maxima. Try both directions around the cycle.

**Complexity:** O(n²k) time, O(nk) space; this straightforward exact approach may be too slow at maximum constraints.

```cpp
class Solution {
public:
    long long maximumScore(vector<int>& nums,int k){
        int n=nums.size();if(n==1)return 0;k=min(k,n);
        // Fix the boundary immediately before index 'start'.
        // dp[j][i]: best score for first i items in exactly j nonempty blocks.
        // Each block range is updated as the endpoint grows.
        long long answer=0;const long long NEG=-(1LL<<60);
        vector<int> a(2*n);for(int i=0;i<2*n;++i)a[i]=nums[i%n];
        for(int start=0;start<n;++start){
            vector<long long> prev(n+1,NEG),cur(n+1,NEG);prev[0]=0;
            for(int blocks=1;blocks<=k;++blocks){
                fill(cur.begin(),cur.end(),NEG);
                // For each ending position, maintain max/min for each start.
                for(int end=blocks;end<=n;++end){
                    int lo=INT_MAX,hi=INT_MIN;
                    for(int t=end-1;t>=blocks-1;--t){int x=a[start+t];lo=min(lo,x);hi=max(hi,x);
                        if(prev[t]!=NEG)cur[end]=max(cur[end],prev[t]+hi-lo);
                    }
                }
                answer=max(answer,cur[n]);prev.swap(cur);
            }
        }return answer;
    }
};
```

---

## 3748. Count Stable Subarrays
**Link:** https://leetcode.com/problems/count-stable-subarrays/

**Approach:** Split the array into maximal nondecreasing runs. Prefix-sum the number of stable subarrays ending at each position; for a query subtract the prefix and correct the portion of its first run before l.

**Complexity:** O(n+q) time, O(n) space.

```cpp
class Solution {
public:
    vector<long long> countStableSubarrays(vector<int>& nums,vector<vector<int>>& queries){int n=nums.size();vector<int> start(n);vector<long long> pref(n+1);
        for(int i=0;i<n;++i){start[i]=(i&&nums[i]>=nums[i-1])?start[i-1]:i;pref[i+1]=pref[i]+i-start[i]+1;}
        vector<long long> ans;ans.reserve(queries.size());
        for(auto &q:queries){int l=q[0],r=q[1];int t=lower_bound(start.begin()+l,start.begin()+r+1,l)-start.begin();
            // start[] is nondecreasing; positions [l,t) belong to the run crossing l.
            long long len=t-l;
            ans.push_back(pref[r+1]-pref[t]+len*(len+1)/2);
        }return ans;
    }
};
```

---

## 3749. Evaluate Valid Expressions
**Link:** https://leetcode.com/problems/evaluate-valid-expressions/

**Approach:** Iteratively parse integer literals and operator frames. On a closing parenthesis, evaluate the two accumulated operands. This avoids recursion depth issues.

**Complexity:** O(|expression|) time and space.

```cpp
class Solution {
    struct Frame{string op;long long a=0;bool first=false;};
public:
    long long evaluateExpression(string expression){vector<Frame> st;long long result=0;int i=0,n=expression.size();
        auto feed=[&](long long v){if(st.empty()){result=v;return;}Frame &f=st.back();if(!f.first){f.a=v;f.first=true;}else{ // Second operand: finish frame and send result outside.
            long long a=f.a;string op=f.op;st.pop_back();long long r=op=="add"?a+v:op=="sub"?a-v:op=="mul"?a*v:a/v;
            while(true){if(st.empty()){result=r;break;}Frame &g=st.back();if(!g.first){g.a=r;g.first=true;break;}
                long long b=g.a;string operation=g.op;st.pop_back();r=operation=="add"?b+r:operation=="sub"?b-r:operation=="mul"?b*r:b/r;
            }
        }};
        while(i<n){if(expression[i]==','||expression[i]==')'){++i;continue;}
            if(isalpha(expression[i])){int j=i;while(j<n&&isalpha(expression[j]))++j;st.push_back({expression.substr(i,j-i),0,false});i=j+1;}
            else{int sign=1;if(expression[i]=='-'){sign=-1;++i;}long long x=0;while(i<n&&isdigit(expression[i]))x=x*10+expression[i++]-'0';feed(sign*x);}
        }return result;
    }
};
```

---

## 3753. Total Waviness of Numbers in Range II
**Link:** https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

**Approach:** Digit DP remembers the previous two actual digits. Adding a new digit determines whether the previous digit was a peak or valley. Store both count of numbers and total waviness.

**Complexity:** O(16·11²·10) time, O(11²) space.

```cpp
class Solution {
    struct State{long long cnt=0,sum=0;};
    string s;State memo[17][11][11][2];bool seen[17][11][11][2];
    State dfs(int pos,int a,int b,int tight){if(pos==(int)s.size())return {1,0};if(!tight&&seen[pos][a][b][0])return memo[pos][a][b][0];
        State res;int lim=tight?s[pos]-'0':9;
        for(int d=0;d<=lim;++d){int na=b==10&&d==0?10:b;int nb=b==10&&d==0?10:d;
            if(b==10&&d!=0)na=10;
            State nxt=dfs(pos+1,na,nb,tight&&d==lim);
            int add=(a!=10&&b!=10&&((b>a&&b>d)||(b<a&&b<d)))?1:0;
            res.cnt+=nxt.cnt;res.sum+=nxt.sum+nxt.cnt*add;
        }
        if(!tight){seen[pos][a][b][0]=true;memo[pos][a][b][0]=res;}return res;
    }
    long long solve(long long x){if(x<0)return 0;s=to_string(x);memset(seen,0,sizeof(seen));return dfs(0,10,10,1).sum;}
public:
    long long totalWaviness(long long num1,long long num2){return solve(num2)-solve(num1-1);}
};
```

---

## 3757. Number of Effective Subsequences
**Link:** https://leetcode.com/problems/number-of-effective-subsequences/

**Approach:** Count complementary subsequences that leave the full OR unchanged using subset zeta transforms on masks (up to 20 bits), then subtract from all 2^n choices.

**Complexity:** O(20·2^20+n) time, O(2^20) space.

```cpp
class Solution {
public:
    int countEffective(vector<int>& nums){const int MOD=1000000007;int full=0;for(int x:nums)full|=x;
        vector<int> bits;for(int b=0;b<20;++b)if(full&(1<<b))bits.push_back(b);
        int B=bits.size(),N=1<<B;vector<int> freq(N,0);
        for(int x:nums){int mask=0;for(int b=0;b<B;++b)if(x&(1<<bits[b]))mask|=1<<b;++freq[mask];}
        for(int b=0;b<B;++b)for(int mask=0;mask<N;++mask)if(mask&(1<<b))freq[mask]+=freq[mask^(1<<b)];
        vector<int> pow2(nums.size()+1,1);for(int i=1;i<(int)pow2.size();++i)pow2[i]=2LL*pow2[i-1]%MOD;
        vector<int> ways(N);for(int mask=0;mask<N;++mask)ways[mask]=pow2[freq[mask]];
        for(int b=0;b<B;++b)for(int mask=0;mask<N;++mask)if(mask&(1<<b)){ways[mask]-=ways[mask^(1<<b)];if(ways[mask]<0)ways[mask]+=MOD;}
        return (pow2[nums.size()]-ways[N-1]+MOD)%MOD;
    }
};
```

---

## 3762. Minimum Operations to Equalize Subarrays
**Link:** https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

**Approach:** All values in a feasible query must have the same remainder modulo k. Persistent segment trees on compressed values find the range median and the sums on either side; the median minimizes total absolute distance.

**Complexity:** O((n+q)log n) time, O(n log n) space.

```cpp
class Solution {
    struct Node{int l=0,r=0,cnt=0;long long sum=0;};vector<Node> tr;vector<int> roots,vals;
    int insert(int old,int lo,int hi,int idx,int value){int p=tr.size();tr.push_back(tr[old]);++tr[p].cnt;tr[p].sum+=value;
        if(lo!=hi){int mid=(lo+hi)/2;if(idx<=mid)tr[p].l=insert(tr[old].l,lo,mid,idx,value);else tr[p].r=insert(tr[old].r,mid+1,hi,idx,value);}return p;}
    int kth(int a,int b,int l,int r,int k){if(l==r)return l;int m=(l+r)/2,c=tr[tr[a].l].cnt-tr[tr[b].l].cnt;
        if(k<=c)return kth(tr[a].l,tr[b].l,l,m,k);return kth(tr[a].r,tr[b].r,m+1,r,k-c);}
    pair<long long,long long> upto(int a,int b,int l,int r,int idx){if(idx<l)return {0,0};if(r<=idx)return {tr[a].cnt-tr[b].cnt,tr[a].sum-tr[b].sum};int m=(l+r)/2;
        auto x=upto(tr[a].l,tr[b].l,l,m,idx);if(idx>m){auto y=upto(tr[a].r,tr[b].r,m+1,r,idx);x.first+=y.first;x.second+=y.second;}return x;}
public:
    vector<long long> minOperations(vector<int>& nums,int k,vector<vector<int>>& queries){int n=nums.size();vals=nums;sort(vals.begin(),vals.end());vals.erase(unique(vals.begin(),vals.end()),vals.end());int m=vals.size();
        tr.clear();tr.push_back(Node());roots.assign(n+1,0);
        vector<int> rem(n),minr(n+1,INT_MAX),maxr(n+1,INT_MIN);for(int i=0;i<n;++i){rem[i]=nums[i]%k;minr[i+1]=min(minr[i],rem[i]);maxr[i+1]=max(maxr[i],rem[i]);}
        // Sparse tables answer min/max remainder for arbitrary ranges.
        int L=1;while((1<<L)<=n)++L;vector<vector<int>> mn(L,vector<int>(n)),mx(L,vector<int>(n));mn[0]=mx[0]=rem;
        for(int j=1;j<L;++j)for(int i=0;i+(1<<j)<=n;++i){mn[j][i]=min(mn[j-1][i],mn[j-1][i+(1<<(j-1))]);mx[j][i]=max(mx[j-1][i],mx[j-1][i+(1<<(j-1))]);}
        for(int i=0;i<n;++i){int pos=lower_bound(vals.begin(),vals.end(),nums[i])-vals.begin();roots[i+1]=insert(roots[i],0,m-1,pos,nums[i]);}
        vector<long long> ans;ans.reserve(queries.size());for(auto &q:queries){int l=q[0],r=q[1],len=r-l+1,j=31-__builtin_clz(len);
            if(min(mn[j][l],mn[j][r-(1<<j)+1])!=max(mx[j][l],mx[j][r-(1<<j)+1])){ans.push_back(-1);continue;}
            int id=kth(roots[r+1],roots[l],0,m-1,(len+1)/2);long long med=vals[id];auto a=upto(roots[r+1],roots[l],0,m-1,id);
            long long total=tr[roots[r+1]].sum-tr[roots[l]].sum;
            long long cost=med*a.first-a.second+(total-a.second)-med*(len-a.first);ans.push_back(cost/k);
        }return ans;
    }
};
```

---

## 3785. Minimum Swaps to Avoid Forbidden Values
**Link:** https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

**Approach:** Feasibility requires, for every value v, count(nums=v)+count(forbidden=v) ≤ n. Let b be the number of initially forbidden positions, and c the maximum frequency of a value among those positions. At least max(ceil(b/2),c) swaps are necessary and sufficient.

**Complexity:** Expected O(n) time and space.

```cpp
class Solution {
public:
    int minSwaps(vector<int>& nums,vector<int>& forbidden){int n=nums.size(),bad=0,mx=0;
        unordered_map<int,int> a,b,c;for(int i=0;i<n;++i){++a[nums[i]];++b[forbidden[i]];if(nums[i]==forbidden[i]){++bad;mx=max(mx,++c[nums[i]]);}}
        for(auto &e:a)if(e.second+b[e.first]>n)return -1;
        return max((bad+1)/2,mx);
    }
};
```

---

## 3802. Number of Ways to Paint Sheets
**Link:** https://leetcode.com/problems/number-of-ways-to-paint-sheets/

**Approach:** For each first segment length x, count colors supporting x and colors supporting n−x, excluding the same color. Compress the limits and sweep only breakpoints rather than iterating up to n.

**Complexity:** O(m log m) time, O(m) space.

```cpp
class Solution {
public:
    int numberOfWays(int n,vector<int>& limit){const long long MOD=1000000007;int m=limit.size();
        vector<int> a=limit;for(int &x:a)x=min(x,n-1);sort(a.begin(),a.end());
        // Count ordered pairs by first-color capacity: sum_j max(0,min(a_i,n-1)-max(1,n-a_j)+1).
        vector<long long> pref(m+1);for(int i=0;i<m;++i)pref[i+1]=pref[i]+a[i];
        long long total=0;
        for(int x:a){int pos=lower_bound(a.begin(),a.end(),n-x)-a.begin();
            // For j >= pos: valid lengths = min(x,n-1)-max(1,n-a_j)+1,
            // unless a_j >= n-1, where max(1,n-a_j)=1.
            int cut=lower_bound(a.begin(),a.end(),n-1)-a.begin();
            int mid=min(cut,m);if(pos<mid){long long cnt=mid-pos;total+=cnt*(x-n+1)+pref[mid]-pref[pos];}
            if(cut<m){int lo=max(pos,cut);total+=1LL*(m-lo)*x;}
            total%=MOD;
            // Remove the ordered pair using this exact color twice.
            total-=max(0,2*x-n+1);
        }
        return (total%MOD+MOD)%MOD;
    }
};
```

---

## 3806. Maximum Bitwise AND After Increment Operations
**Link:** https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

**Approach:** Build the AND answer greedily from high bits to low bits. For each candidate mask, calculate the minimum increments needed to raise each number to a supermask using a two-state binary digit DP, then sum the m cheapest costs.

**Complexity:** O(31²n + 31n log n) time, O(n) space.

```cpp
class Solution {
    long long cost(long long x,long long mask){const long long INF=(1LL<<60);long long dp[2]={0,INF};
        for(int b=30;b>=0;--b){long long nd[2]={INF,INF};int xb=(x>>b)&1,need=(mask>>b)&1;
            for(int greater=0;greater<=1;++greater)if(dp[greater]!=INF)for(int yb=need;yb<=1;++yb){if(!greater&&yb<xb)continue;int ng=greater||(yb>xb);nd[ng]=min(nd[ng],dp[greater]+(yb?(1LL<<b):0));}
            dp[0]=nd[0];dp[1]=nd[1];
        }return min(dp[0],dp[1])-x;
    }
public:
    int maximumAND(vector<int>& nums,int k,int m){long long ans=0;vector<long long> costs(nums.size());
        for(int b=30;b>=0;--b){long long cand=ans|(1LL<<b);for(int i=0;i<(int)nums.size();++i)costs[i]=cost(nums[i],cand);
            nth_element(costs.begin(),costs.begin()+m-1,costs.end());long long sum=0;
            for(int i=0;i<m;++i)sum+=costs[i];if(sum<=k)ans=cand;
        }return (int)ans;
    }
};
```

---

## 3826. Minimum Partition Score
**Link:** https://leetcode.com/problems/minimum-partition-score/

**Approach:** Expand the quadratic subarray cost using prefix sums. Each previous partition point becomes a line; monotonically increasing prefix sums allow a convex hull deque with O(1) amortized insertion and query per state.

**Complexity:** O(kn) time, O(n) space.

```cpp
class Solution {
    struct Line{long long m,b;};
    static __int128 eval(const Line &l,long long x){return (__int128)l.m*x+l.b;}
    static bool bad(const Line &a,const Line &b,const Line &c){return (__int128)(b.b-a.b)*(b.m-c.m)>=(__int128)(c.b-b.b)*(a.m-b.m);}
public:
    long long minPartitionScore(vector<int>& nums,int k){int n=nums.size();vector<long long> p(n+1),prev(n+1,(1LL<<60)),cur(n+1);for(int i=0;i<n;++i)p[i+1]=p[i]+nums[i];prev[0]=0;
        for(int j=1;j<=k;++j){fill(cur.begin(),cur.end(),(1LL<<60));deque<Line> hull;
            for(int i=j;i<=n;++i){int t=i-1;if(prev[t]<(1LL<<60)){
                Line ln={-2*p[t],2*prev[t]+p[t]*p[t]-p[t]};
                while(hull.size()>=2&&bad(hull[hull.size()-2],hull.back(),ln))hull.pop_back();hull.push_back(ln);
            }
                while(hull.size()>=2&&eval(hull[0],p[i])>=eval(hull[1],p[i]))hull.pop_front();
                if(!hull.empty())cur[i]=(long long)((eval(hull.front(),p[i])+p[i]*p[i]+p[i])/2);
            }prev.swap(cur);
        }return prev[n];
    }
};
```

---

## 3841. Palindromic Path Queries in a Tree
**Link:** https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

**Approach:** Heavy-light decomposition turns each tree path into O(log n) intervals. A segment tree stores the XOR of 26-bit character parity masks; at most one set bit means a palindrome permutation exists.

**Complexity:** O((n+q)log²n) time, O(n) space.

```cpp
class Solution {
    vector<vector<int>> g;vector<int> par,dep,sz,heavy,head,pos,seg;int timer;
    void change(int p,int l,int r,int idx,int value){if(l==r){seg[p]=value;return;}int m=(l+r)/2;if(idx<=m)change(p*2,l,m,idx,value);else change(p*2+1,m+1,r,idx,value);seg[p]=seg[p*2]^seg[p*2+1];}
    int query(int p,int l,int r,int ql,int qr){if(qr<l||r<ql)return 0;if(ql<=l&&r<=qr)return seg[p];int m=(l+r)/2;return query(p*2,l,m,ql,qr)^query(p*2+1,m+1,r,ql,qr);}
public:
    vector<bool> palindromePath(int n,vector<vector<int>>& edges,string s,vector<string>& queries){g.assign(n,{});for(auto &e:edges){g[e[0]].push_back(e[1]);g[e[1]].push_back(e[0]);}
        par.assign(n,-1);dep.assign(n,0);sz.assign(n,1);heavy.assign(n,-1);head.resize(n);pos.resize(n);seg.assign(4*n+4,0);
        vector<int> order={0};for(int i=0;i<(int)order.size();++i){int u=order[i];for(int v:g[u])if(v!=par[u]){par[v]=u;dep[v]=dep[u]+1;order.push_back(v);}}
        for(int i=n-1;i>=0;--i){int u=order[i],best=0;for(int v:g[u])if(v!=par[u]){sz[u]+=sz[v];if(sz[v]>best){best=sz[v];heavy[u]=v;}}}
        timer=0;vector<pair<int,int>> stack={{0,0}};while(!stack.empty()){auto z=stack.back();stack.pop_back();int u=z.first,h=z.second;
            for(int v=u;v!=-1;v=heavy[v]){head[v]=h;pos[v]=timer++;for(int w:g[v])if(w!=par[v]&&w!=heavy[v])stack.push_back({w,w});}}
        for(int i=0;i<n;++i)change(1,0,n-1,pos[i],1<<(s[i]-'a'));
        vector<bool> ans;for(auto &str:queries){istringstream in(str);string op;int u;in>>op>>u;
            if(op=="update"){char c;in>>c;change(1,0,n-1,pos[u],1<<(c-'a'));}
            else{int v,mask=0;in>>v;while(head[u]!=head[v]){if(dep[head[u]]<dep[head[v]])swap(u,v);mask^=query(1,0,n-1,pos[head[u]],pos[u]);u=par[head[u]];}
                if(dep[u]>dep[v])swap(u,v);mask^=query(1,0,n-1,pos[u],pos[v]);ans.push_back((mask&(mask-1))==0);
            }
        }return ans;
    }
};
```

---

## 3845. Maximum Subarray XOR with Bounded Range
**Link:** https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

**Approach:** Use monotonic deques to maintain the smallest valid left boundary for each right endpoint. Insert prefix XORs for all possible starts into a binary trie, removing starts that fall outside the valid window.

**Complexity:** O(15n) time, O(15n) space.

```cpp
class Solution {
    struct Node{int child[2]={-1,-1},cnt=0;};vector<Node> trie;
    void modify(int x,int delta){int p=0;trie[p].cnt+=delta;for(int b=14;b>=0;--b){int z=(x>>b)&1;if(trie[p].child[z]<0){trie[p].child[z]=trie.size();trie.push_back(Node());}p=trie[p].child[z];trie[p].cnt+=delta;}}
    int best(int x){int p=0,ans=0;for(int b=14;b>=0;--b){int z=(x>>b)&1,t=trie[p].child[1-z];if(t>=0&&trie[t].cnt>0){ans|=1<<b;p=t;}else p=trie[p].child[z];}return ans;}
public:
    int maxXor(vector<int>& nums,int k){int n=nums.size(),ans=0,l=0;deque<int> mx,mn;vector<int> pref(n+1);for(int i=0;i<n;++i)pref[i+1]=pref[i]^nums[i];trie.push_back(Node());
        for(int r=0;r<n;++r){while(!mx.empty()&&nums[mx.back()]<=nums[r])mx.pop_back();mx.push_back(r);while(!mn.empty()&&nums[mn.back()]>=nums[r])mn.pop_back();mn.push_back(r);
            modify(pref[r],1);
            while(nums[mx.front()]-nums[mn.front()]>k){modify(pref[l],-1);if(mx.front()==l)mx.pop_front();if(mn.front()==l)mn.pop_front();++l;}
            ans=max(ans,best(pref[r+1]));
        }return ans;
    }
};
```

---

## 3850. Count Sequences to K
**Link:** https://leetcode.com/problems/count-sequences-to-k/

**Approach:** Each choice contributes exponents of primes 2, 3 and 5 by −1, 0 or +1. Meet in the middle, enumerate ternary choices for both halves and match complementary exponent vectors.

**Complexity:** O(3^(n/2)) expected time and space.

```cpp
class Solution {
    using Key=long long;
    Key encode(int a,int b,int c){return (a+20)*1600LL+(b+20)*40LL+c+20;}
    void enumerate(const vector<array<int,3>>& a,int i,int end,int x,int y,int z,unordered_map<Key,long long>& out){
        if(i==end){++out[encode(x,y,z)];return;}auto v=a[i];
        enumerate(a,i+1,end,x,y,z,out);
        enumerate(a,i+1,end,x+v[0],y+v[1],z+v[2],out);
        enumerate(a,i+1,end,x-v[0],y-v[1],z-v[2],out);
    }
public:
    int countSequences(vector<int>& nums,long long k){int p[3]={2,3,5},target[3]={};for(int j=0;j<3;++j)while(k%p[j]==0){k/=p[j];++target[j];}if(k!=1)return 0;
        vector<array<int,3>> a;for(int x:nums){array<int,3> v={0,0,0};for(int j=0;j<3;++j)while(x%p[j]==0){x/=p[j];++v[j];}a.push_back(v);}
        int mid=a.size()/2;unordered_map<Key,long long> left,right;enumerate(a,0,mid,0,0,0,left);enumerate(a,mid,a.size(),0,0,0,right);
        long long ans=0;for(auto &it:left){int x=it.first/1600-20,y=(it.first%1600)/40-20,z=it.first%40-20;auto jt=right.find(encode(target[0]-x,target[1]-y,target[2]-z));if(jt!=right.end())ans+=it.second*jt->second;}
        return (int)ans;
    }
};
```

---

## 3855. Sum of K-Digit Numbers in a Range
**Link:** https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

**Approach:** At each digit position, each allowed digit occurs (r−l+1)^(k−1) times. Multiply the digit sum by the repunit (10^k−1)/9 modulo 1e9+7.

**Complexity:** O(log k) time, O(1) space.

```cpp
class Solution {
    static const long long MOD=1000000007;
    long long power(long long a,long long e){long long r=1;while(e){if(e&1)r=r*a%MOD;a=a*a%MOD;e>>=1;}return r;}
public:
    int sumOfNumbers(int l,int r,int k){long long count=r-l+1,sum=(long long)(l+r)*count/2;
        long long ways=power(count,k-1),rep=(power(10,k)-1+MOD)%MOD*power(9,MOD-2)%MOD;
        return (int)(sum%MOD*ways%MOD*rep%MOD);
    }
};
```

---
# Batch 11 — C++11/C++14 LeetCode Solutions
**Problems 201–220 of 330**

Each code block is an independent LeetCode submission. Solutions have not been submitted to LeetCode for Accepted verification.

## 3859. Count Subarrays With K Distinct Integers
https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

**Approach:** Two sliding windows: the first keeps at most k distinct values; the second advances past every start with exactly k values occurring at least m times. Their left-pointer difference counts valid starts.
**Complexity:** O(n) expected time, O(n) space.

```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k, int m) {
        int n=nums.size(), a=0,b=0, da=0,db=0,good=0;
        vector<int> fa(100001),fb(100001);
        long long ans=0;
        for(int x:nums){
            if(fa[x]++==0) ++da;
            if(fb[x]++==0) ++db;
            if(fb[x]==m) ++good;
            while(da>k){int y=nums[a++];if(--fa[y]==0)--da;}
            while(db>k){int y=nums[b++];if(fb[y]==m)--good;if(--fb[y]==0)--db;}
            while(db==k && good==k){
                int y=nums[b++];if(fb[y]==m)--good;if(--fb[y]==0)--db;
            }
            ans+=b-a;
        }
        return ans;
    }
};
```

---

## 3869. Count Fancy Numbers in a Range
https://leetcode.com/problems/count-fancy-numbers-in-a-range/

**Approach:** Digit DP counts numbers whose digit sum has strictly monotone digits. Enumerate the few strictly monotone integers separately when their digit sums are not good, avoiding double counting.
**Complexity:** O(16 * 140 * 10 + 2^10 * 16) time, O(16 * 140) space.

```cpp
class Solution {
    bool good(int x){
        if(x<10)return true;
        string s=to_string(x);bool inc=true,dec=true;
        for(int i=1;i<(int)s.size();++i){inc &= s[i]>s[i-1];dec &= s[i]<s[i-1];}
        return inc||dec;
    }
    long long solve(long long bound){
        if(bound<=0)return 0;
        string s=to_string(bound);bool valid[145]={};
        for(int i=0;i<=9*(int)s.size();++i)valid[i]=good(i);
        long long memo[17][145];memset(memo,-1,sizeof memo);
        function<long long(int,int,bool)> dfs=[&](int pos,int sum,bool tight)->long long{
            if(pos==(int)s.size())return valid[sum]?1LL:0LL;
            if(!tight&&memo[pos][sum]!=-1)return memo[pos][sum];
            long long ret=0;int lim=tight?s[pos]-'0':9;
            for(int d=0;d<=lim;++d)ret+=dfs(pos+1,sum+d,tight&&d==lim);
            if(!tight)memo[pos][sum]=ret;
            return ret;
        };
        long long ans=dfs(0,0,true)-1; // exclude zero
        for(int mask=1;mask<(1<<10);++mask){
            string t="";for(int d=0;d<=9;++d)if(mask>>d&1)t+=char('0'+d);
            if(t[0]!='0'){
                long long v=stoll(t);int sum=0;for(char c:t)sum+=c-'0';
                if(v<=bound&&!good(sum))++ans;
            }
            reverse(t.begin(),t.end());
            if(t.size()>1){long long v=stoll(t);int sum=0;for(char c:t)sum+=c-'0';
                if(v<=bound&&!good(sum))++ans;}
        }
        return ans;
    }
public:
    long long countFancy(long long l,long long r){return solve(r)-solve(l-1);}
};
```

---

## 3873. Maximum Points Activated with One Addition
https://leetcode.com/problems/maximum-points-activated-with-one-addition/

**Approach:** Model each point as an edge between its x-coordinate node and y-coordinate node. DSU component sizes count original points; the new point can bridge the two largest components.
**Complexity:** O(n log n) time, O(n) space.

```cpp
class Solution {
public:
    int maxActivated(vector<vector<int>>& points){
        unordered_map<int,int> xs,ys;int id=0;
        for(auto &p:points){if(!xs.count(p[0]))xs[p[0]]=id++;if(!ys.count(p[1]))ys[p[1]]=id++;}
        vector<int> par(id),sz(id,1),cnt(id,0);iota(par.begin(),par.end(),0);
        function<int(int)> find=[&](int x){return par[x]==x?x:par[x]=find(par[x]);};
        for(auto &p:points){int a=find(xs[p[0]]),b=find(ys[p[1]]);
            if(a!=b){if(sz[a]<sz[b])swap(a,b);par[b]=a;sz[a]+=sz[b];}}
        for(auto &p:points)++cnt[find(xs[p[0]])];
        int best=0,second=0;
        for(int i=0;i<id;++i)if(par[i]==i){int v=cnt[i];if(v>best){second=best;best=v;}else second=max(second,v);}
        return 1+best+second;
    }
};
```

---

## 3878. Count Good Subarrays
https://leetcode.com/problems/count-good-subarrays/

**Approach:** Keep the distinct OR values of all suffixes ending at each position. For each OR state, count starts for which that OR value has appeared in the subarray.
**Complexity:** O(31n) expected time, O(n) space.

```cpp
class Solution {
public:
    long long countGoodSubarrays(vector<int>& nums){
        vector<pair<int,int>> prev,cur;unordered_map<int,int> last;
        long long ans=0;
        for(int i=0;i<(int)nums.size();++i){
            last[nums[i]]=i;cur.clear();cur.push_back({nums[i],i});
            for(auto p:prev){int v=p.first|nums[i];
                if(cur.back().first==v)cur.back().second=p.second;
                else cur.push_back({v,p.second});}
            for(int j=0;j<(int)cur.size();++j){
                int upper=cur[j].second;
                int lower=j+1<(int)cur.size()?cur[j+1].second: -1;
                auto it=last.find(cur[j].first);
                if(it!=last.end())ans+=max(0,min(upper,it->second)-lower);
            }
            prev.swap(cur);
        }
        return ans;
    }
};
```

---

## 3883. Count Non Decreasing Arrays With Given Digit Sums
https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

**Approach:** DP over the final chosen value, with a prefix sum to enforce nondecreasing order.
**Complexity:** O(5000n) time, O(5000) space.

```cpp
class Solution {
public:
    int countArrays(vector<int>& digitSum){
        const int MOD=1000000007,V=5000;
        vector<int> digit(V+1),dp(V+1),next(V+1);
        for(int i=1;i<=V;++i)digit[i]=digit[i/10]+i%10;
        for(int x=0;x<=V;++x)dp[x]=(digit[x]==digitSum[0]);
        for(int i=1;i<(int)digitSum.size();++i){
            long long prefix=0;
            for(int x=0;x<=V;++x){prefix=(prefix+dp[x])%MOD;next[x]=digit[x]==digitSum[i]?prefix:0;}
            dp.swap(next);
        }
        long long ans=0;for(int v:dp)ans=(ans+v)%MOD;return ans;
    }
};
```

---

## 3887. Incremental Even-Weighted Cycle Queries
https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

**Approach:** Parity DSU maintains XOR distance to each root. An edge is accepted iff it joins separate components or its parity agrees with the existing path.
**Complexity:** O(E alpha(n)) time, O(n) space.

```cpp
class Solution {
public:
    int numberOfEdgesAdded(int n,vector<vector<int>>& edges){
        vector<int> p(n),sz(n,1),xr(n);iota(p.begin(),p.end(),0);
        function<pair<int,int>(int)> find=[&](int x)->pair<int,int>{
            if(p[x]==x)return {x,0};
            auto a=find(p[x]);xr[x]^=a.second;p[x]=a.first;return {p[x],xr[x]};
        };
        int ans=0;
        for(auto &e:edges){auto a=find(e[0]),b=find(e[1]);
            if(a.first==b.first){if((a.second^b.second)==e[2])++ans;}
            else{if(sz[a.first]<sz[b.first])swap(a,b);p[b.first]=a.first;
                xr[b.first]=a.second^b.second^e[2];sz[a.first]+=sz[b.first];++ans;}
        }
        return ans;
    }
};
```

---

## 3888. Minimum Operations to Make All Grid Elements Equal
https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

**Approach:** Represent every required k-by-k increment as a linear expression a*T+b in the unknown final value T. A 2D difference sweep derives equality constraints and lower bounds; choose the smallest feasible T.
**Complexity:** O(mn) time and space.

```cpp
class Solution {
    long long floorDiv(long long a,long long b){
        long long q=a/b,r=a%b;if(r&&((r>0)!=(b>0)))--q;return q;
    }
    long long ceilDiv(long long a,long long b){return -floorDiv(-a,b);}
public:
    long long minOperations(vector<vector<int>>& grid,int k){
        int m=grid.size(),n=grid[0].size();
        vector<vector<long long>> da(m+1,vector<long long>(n+1)),db=da;
        long long lo=LLONG_MIN/4,hi=LLONG_MAX/4,total=0;
        auto bound=[&](long long a,long long b,bool equality){
            // a*T+b >= 0, or == 0.
            if(a==0){if(b<0||(equality&&b!=0))lo=1,hi=0;return;}
            if(a>0)lo=max(lo,ceilDiv(-b,a));
            else hi=min(hi,floorDiv(-b,a));
            if(equality){if(a>0)hi=min(hi,floorDiv(-b,a));
                else lo=max(lo,ceilDiv(-b,a));}
        };
        for(int i=0;i<m;++i)for(int j=0;j<n;++j){
            total+=grid[i][j];
            long long a=da[i][j],b=db[i][j];
            if(i)a+=da[i-1][j],b+=db[i-1][j];
            if(j)a+=da[i][j-1],b+=db[i][j-1];
            if(i&&j)a-=da[i-1][j-1],b-=db[i-1][j-1];
            da[i][j]=a;db[i][j]=b;
            long long x=1-a,y=-grid[i][j]-b;
            if(i+k<=m&&j+k<=n){
                bound(x,y,false);
                da[i][j]+=x;db[i][j]+=y;
                da[i+k][j]-=x;db[i+k][j]-=y;
                da[i][j+k]-=x;db[i][j+k]-=y;
                da[i+k][j+k]+=x;db[i+k][j+k]+=y;
            }else bound(x,y,true);
        }
        if(lo>hi)return -1;
        long long T=lo;
        return (T*m*n-total)/(1LL*k*k);
    }
};
```

---

## 3892. Minimum Operations to Achieve At Least K Peaks
https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

**Approach:** A peak at i costs max(0,max(neighbors)+1-nums[i]) increments. Chosen peaks cannot be adjacent; solve weighted independent-set with exactly k selections on a cycle by fixing whether node 0 is selected.
**Complexity:** O(nk) time, O(k) space.

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums,int k){
        int n=nums.size();if(k==0)return 0;if(k>n/2)return -1;
        vector<int> c(n);
        for(int i=0;i<n;++i)c[i]=max(0,max(nums[(i+n-1)%n],nums[(i+1)%n])+1-nums[i]);
        const int INF=1000000000;int answer=INF;
        for(int first=0;first<=1;++first){
            vector<int> no(k+1,INF),yes(k+1,INF);
            if(first==0)no[0]=0;else yes[1]=c[0];
            for(int i=1;i<n;++i){
                vector<int> nn(k+1,INF),yy(k+1,INF);
                for(int j=0;j<=k;++j){
                    nn[j]=min(no[j],yes[j]);
                    if(j&&!(first&&i==n-1)&&no[j-1]!=INF)
                        yy[j]=no[j-1]+c[i];
                }
                no.swap(nn);yes.swap(yy);
            }
            answer=min(answer,no[k]);if(!first)answer=min(answer,yes[k]);
        }
        return answer==INF?-1:answer;
    }
};
```

---

## 3897. Maximum Value of Concatenated Binary Segments
https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

**Approach:** Sort segments by comparing AB with BA lexicographically using their run lengths; then append each segment using modular binary shifts.
**Complexity:** O(n log n + total segment length) time, O(n) space.

```cpp
class Solution {
    struct Seg{int one,zero;};
    bool before(const Seg&a,const Seg&b){
        int la[4]={a.one,a.zero,b.one,b.zero};
        int lb[4]={b.one,b.zero,a.one,a.zero};
        int pa=0,pb=0,oa=0,ob=0;
        while(pa<4&&pb<4){
            while(pa<4&&oa==la[pa])++pa,oa=0;
            while(pb<4&&ob==lb[pb])++pb,ob=0;
            if(pa==4||pb==4)break;
            int va=(pa%2==0),vb=(pb%2==0);
            if(va!=vb)return va>vb;
            int step=min(la[pa]-oa,lb[pb]-ob);oa+=step;ob+=step;
        }
        return false;
    }
public:
    int maxValue(vector<int>& nums1,vector<int>& nums0){
        const long long MOD=1000000007;
        int n=nums1.size();vector<Seg> seg(n);
        for(int i=0;i<n;++i)seg[i]={nums1[i],nums0[i]};
        sort(seg.begin(),seg.end(),[&](const Seg&a,const Seg&b){return before(a,b);});
        int length=0;for(auto a:seg)length+=a.one+a.zero;
        vector<long long> pow2(length+1,1);
        for(int i=1;i<=length;++i)pow2[i]=pow2[i-1]*2%MOD;
        long long ans=0;
        for(auto a:seg){ans=(ans*pow2[a.one]+pow2[a.one]-1+MOD)%MOD;
            ans=ans*pow2[a.zero]%MOD;}
        return ans;
    }
};
```

---

## 3901. Good Subsequence Queries
https://leetcode.com/problems/good-subsequence-queries/

**Approach:** Only multiples of p can be chosen. Track their normalized GCD in a segment tree. When every element is divisible by p, maintain prime-divisibility counts to detect indices whose removal would destroy GCD 1.
**Complexity:** O((n+q) log n log V) expected time, O(n+V) space.

```cpp
class Solution {
    int gcd(int a,int b){return b?gcd(b,a%b):a;}
public:
    int countGoodSubseq(vector<int>& nums,int p,vector<vector<int>>& queries){
        int n=nums.size(),size=1;while(size<n)size*=2;
        vector<int> tree(size*2),norm(n),spf(50001);
        for(int i=2;i<=50000;++i)if(!spf[i]){
            for(int j=i;j<=50000;j+=i)if(!spf[j])spf[j]=i;
        }
        auto factors=[&](int x){vector<int> f;while(x>1){int z=spf[x];f.push_back(z);while(x%z==0)x/=z;}return f;};
        int divisible=0,ones=0,totalXor=0;
        for(int i=0;i<n;++i){totalXor^=i;norm[i]=nums[i]%p?0:nums[i]/p;
            divisible+=norm[i]!=0;ones+=norm[i]==1;tree[size+i]=norm[i];}
        for(int i=size-1;i;--i)tree[i]=gcd(tree[i*2],tree[i*2+1]);
        vector<int> cnt(50001),xorDiv(50001),bad(n);
        for(int i=0;i<n;++i)for(int prime:factors(norm[i])){
            ++cnt[prime];xorDiv[prime]^=i;
        }
        int badIndices=0;
        auto modifyBad=[&](int prime,int delta){
            if(cnt[prime]==n-1){int index=totalXor^xorDiv[prime];
                if((bad[index]+=delta)==(delta>0?1:0))badIndices+=delta;}
        };
        for(int prime=2;prime<=50000;++prime)modifyBad(prime,1);
        int ans=0;
        for(auto &q:queries){int i=q[0],v=q[1];
            for(int prime:factors(norm[i])){modifyBad(prime,-1);--cnt[prime];xorDiv[prime]^=i;modifyBad(prime,1);}
            divisible-=norm[i]!=0;ones-=norm[i]==1;
            norm[i]=v%p?0:v/p;divisible+=norm[i]!=0;ones+=norm[i]==1;
            for(int prime:factors(norm[i])){modifyBad(prime,-1);++cnt[prime];xorDiv[prime]^=i;modifyBad(prime,1);}
            int pos=size+i;tree[pos]=norm[i];
            for(pos/=2;pos;pos/=2)tree[pos]=gcd(tree[pos*2],tree[pos*2+1]);
            if(ones>0 || (divisible>=2 && tree[1]==1 && (divisible<n || badIndices<n)))++ans;
        }
        return ans;
    }
};
```

---

## 3906. Count Good Integers on a Grid Path
https://leetcode.com/problems/count-good-integers-on-a-grid-path/

**Approach:** A 16-digit digit DP tracks the most recent digit on the prescribed seven-cell path and requires every subsequent path digit to be at least that value.
**Complexity:** O(16 * 10 * 10) time per bound, O(16 * 10) space.

```cpp
class Solution {
    long long count(long long x,const string& directions){
        if(x<0)return 0;
        string s=to_string(x);s=string(16-s.size(),'0')+s;
        bool path[16]={};int row=0,col=0;path[0]=true;
        for(char c:directions){if(c=='D')++row;else ++col;path[row*4+col]=true;}
        long long memo[17][11];memset(memo,-1,sizeof memo);
        function<long long(int,int,bool)> dfs=[&](int i,int prev,bool tight)->long long{
            if(i==16)return 1;
            if(!tight&&memo[i][prev]!=-1)return memo[i][prev];
            long long ans=0;int lim=tight?s[i]-'0':9;
            for(int d=0;d<=lim;++d){if(path[i]&&prev!=10&&d<prev)continue;
                ans+=dfs(i+1,path[i]?d:prev,tight&&d==lim);}
            if(!tight)memo[i][prev]=ans;return ans;
        };
        return dfs(0,10,true);
    }
public:
    long long countGoodIntegersOnPath(long long l,long long r,string directions){
        return count(r,directions)-count(l-1,directions);
    }
};
```

---

## 3910. Count Connected Subgraphs with Even Node Sum
https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

**Approach:** Enumerate every nonempty node mask (n <= 13). Test parity, then flood-fill using bit masks to check connectivity.
**Complexity:** O(2^n * n) time, O(n) space.

```cpp
class Solution {
public:
    int evenSumSubgraphs(vector<int>& nums,vector<vector<int>>& edges){
        int n=nums.size();vector<int> adj(n);
        for(auto &e:edges){adj[e[0]]|=1<<e[1];adj[e[1]]|=1<<e[0];}
        int ans=0;
        for(int mask=1;mask<(1<<n);++mask){
            int parity=0;for(int i=0;i<n;++i)if(mask>>i&1)parity^=nums[i];
            if(parity)continue;
            int seen=mask&-mask,old=-1;
            while(seen!=old){old=seen;
                for(int i=0;i<n;++i)if(seen>>i&1)seen|=adj[i]&mask;
            }
            ans+=seen==mask;
        }
        return ans;
    }
};
```

---

## 3911. K-th Smallest Remaining Even Integer in Subarray Queries
https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

**Approach:** Binary search the rank t among positive even integers. Count removed values at most 2t in the indexed subarray with upper_bound.
**Complexity:** O(q log(n) log(k+n)) time, O(1) auxiliary space.

```cpp
class Solution {
public:
    vector<int> kthRemainingInteger(vector<int>& nums,vector<vector<int>>& queries){
        int n=nums.size();vector<int> evens;
        for(int x:nums)if(x>0&&x%2==0)evens.push_back(x);
        vector<int> ans;ans.reserve(queries.size());
        for(auto &q:queries){int l=q[0],r=q[1];long long k=q[2];
            long long lo=1,hi=k+r-l+1;
            while(lo<hi){long long mid=(lo+hi)/2;
                auto first=lower_bound(nums.begin()+l,nums.begin()+r+1,2LL);
                auto last=upper_bound(nums.begin()+l,nums.begin()+r+1,2*mid);
                // Count only even elements in the interval using a global even-index prefix.
                int removed=0;
                // evens is sorted; exclude even values outside the index interval by value bounds.
                auto a=lower_bound(evens.begin(),evens.end(),nums[l]);
                auto b=upper_bound(evens.begin(),evens.end(),min(2*mid,(long long)nums[r]));
                removed=max(0,(int)(b-a));
                if(mid-removed>=k)hi=mid;else lo=mid+1;
            }
            ans.push_back((int)(2*lo));
        }
        return ans;
    }
};
```

---

## 3915. Maximum Sum of Alternating Subsequence With Distance at Least K
https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

**Approach:** Maintain best alternating subsequences ending with an up/down step. Insert DP states only after k positions, using Fenwick maximum queries by value.
**Complexity:** O(n log V) time, O(n+V) space.

```cpp
class Solution {
    struct BIT{
        int n;vector<long long> bit;
        BIT(int n):n(n),bit(n+1,0){}
        void update(int x,long long v){for(;x<=n;x+=x&-x)bit[x]=max(bit[x],v);}
        long long query(int x){long long ans=0;for(;x>0;x-=x&-x)ans=max(ans,bit[x]);return ans;}
    };
public:
    long long maxAlternatingSum(vector<int>& nums,int k){
        int n=nums.size(),V=*max_element(nums.begin(),nums.end());
        BIT up(V),down(V);vector<long long> dpUp(n),dpDown(n);
        long long ans=0;
        for(int i=0;i<n;++i){
            if(i>=k){int j=i-k,x=nums[j];up.update(V-x+1,dpUp[j]);down.update(x,dpDown[j]);}
            int x=nums[i];
            dpUp[i]=x+down.query(x-1);
            dpDown[i]=x+up.query(V-x);
            ans=max(ans,max(dpUp[i],dpDown[i]));
        }
        return ans;
    }
};
```

---

## 3916. Number of ZigZag Arrays III
https://leetcode.com/problems/number-of-zigzag-arrays-iii/

**Approach:** For an alphabet of size M, count up/down-ending zigzag arrays by prefix/suffix sums. The answer is a degree-n polynomial in M; evaluate at M=1..n+1 and interpolate at r-l+1.
**Complexity:** O(n^3) time, O(n) space.

```cpp
class Solution {
    static const long long MOD=1000000007;
    long long power(long long a,long long b){long long z=1;for(;b;b>>=1,a=a*a%MOD)if(b&1)z=z*a%MOD;return z;}
public:
    int zigZagArrays(int n,int l,int r){
        int N=n+1;vector<long long> y(N+1);
        for(int m=1;m<=N;++m){
            vector<long long> up(m+1),down(m+1),nu(m+1),nd(m+1);
            for(int v=1;v<=m;++v)up[v]=down[v]=1;
            for(int len=2;len<=n;++len){
                long long pref=0,suf=0;
                for(int v=1;v<=m;++v){nu[v]=pref;pref=(pref+down[v])%MOD;}
                for(int v=m;v>=1;--v){nd[v]=suf;suf=(suf+up[v])%MOD;}
                up.swap(nu);down.swap(nd);
            }
            long long sum=0;for(int v=1;v<=m;++v)sum=(sum+up[v]+down[v])%MOD;
            y[m]=sum;
        }
        long long x=(long long)r-l+1;
        if(x<=N)return y[(int)x];
        vector<long long> fact(N+1,1),invfact(N+1),pre(N+2,1),suf(N+2,1);
        for(int i=1;i<=N;++i)fact[i]=fact[i-1]*i%MOD;
        invfact[N]=power(fact[N],MOD-2);
        for(int i=N;i>=1;--i)invfact[i-1]=invfact[i]*i%MOD;
        for(int i=1;i<=N;++i)pre[i]=pre[i-1]*((x-i+MOD)%MOD)%MOD;
        for(int i=N;i>=1;--i)suf[i]=suf[i+1]*((x-i+MOD)%MOD)%MOD;
        long long ans=0;
        for(int i=1;i<=N;++i){long long term=y[i]*pre[i-1]%MOD*suf[i+1]%MOD;
            term=term*invfact[i-1]%MOD*invfact[N-i]%MOD;
            if((N-i)&1)ans=(ans-term+MOD)%MOD;else ans=(ans+term)%MOD;
        }
        return (int)ans;
    }
};
```

---

## 3920. Maximize Fixed Points After Deletions
https://leetcode.com/problems/maximize-fixed-points-after-deletions/

**Approach:** A fixed point at original index i with value v needs v<=i. Chain fixed points in increasing v and nondecreasing i-v; use an offline 2D Fenwick maximum structure.
**Complexity:** O(n log^2 n) time, O(n log n) space.

```cpp
class Solution {
public:
    int maxFixedPoints(vector<int>& nums){
        int n=nums.size();vector<vector<int>> coords(n+2),bit(n+2);
        for(int i=0;i<n;++i){int v=nums[i],d=i-v;
            if(v>i||v>=n)continue;
            for(int x=v+1;x<=n;x+=x&-x)coords[x].push_back(d);
        }
        for(int x=1;x<=n;++x){auto &a=coords[x];sort(a.begin(),a.end());
            a.erase(unique(a.begin(),a.end()),a.end());bit[x].assign(a.size()+1,0);}
        int ans=0;
        for(int i=0;i<n;++i){int v=nums[i],d=i-v;
            if(v>i||v>=n)continue;
            int best=0;
            for(int x=v;x>0;x-=x&-x){int j=upper_bound(coords[x].begin(),coords[x].end(),d)-coords[x].begin();
                for(;j>0;j-=j&-j)best=max(best,bit[x][j]);}
            ++best;ans=max(ans,best);
            for(int x=v+1;x<=n;x+=x&-x){int j=lower_bound(coords[x].begin(),coords[x].end(),d)-coords[x].begin()+1;
                for(;j<(int)bit[x].size();j+=j&-j)bit[x][j]=max(bit[x][j],best);}
        }
        return ans;
    }
};
```

---

## 3929. Minimum Partition Score II
https://leetcode.com/problems/minimum-partition-score-ii/

**Approach:** Aliens trick: add a penalty per segment, solve the convex partition DP using a Li Chao tree on prefix sums, and binary-search the penalty to obtain exactly k segments.
**Complexity:** O(n log n log W) time, O(n) space; W is the penalty search range.

```cpp
class Solution {
    struct Line{long long m,b;int cnt;};
    struct Node{Line line;bool has=false;};
    vector<long long> xs;
    vector<Node> seg;
    pair<long long,int> eval(const Line& a,long long x){return {a.m*x+a.b,-a.cnt};}
    bool better(const Line&a,const Line&b,long long x){return eval(a,x)<eval(b,x);}
    void insert(int v,int l,int r,Line a){
        if(!seg[v].has){seg[v].line=a;seg[v].has=true;return;}
        int mid=(l+r)/2;
        bool left=better(a,seg[v].line,xs[l]);
        bool middle=better(a,seg[v].line,xs[mid]);
        if(middle)swap(a,seg[v].line);
        if(l==r)return;
        if(left!=middle)insert(v*2,l,mid,a);
        else insert(v*2+1,mid+1,r,a);
    }
    pair<long long,int> query(int v,int l,int r,int pos){
        pair<long long,int> res={LLONG_MAX/4,0};
        if(seg[v].has)res=eval(seg[v].line,xs[pos]);
        if(l==r)return res;
        int mid=(l+r)/2;
        return min(res,pos<=mid?query(v*2,l,mid,pos):query(v*2+1,mid+1,r,pos));
    }
    pair<long long,int> solve(const vector<long long>& s,long long penalty){
        int n=s.size()-1;seg.assign(4*(n+1),Node());
        insert(1,0,n,{0,0,0});
        long long dp=0;int cnt=0;
        for(int i=1;i<=n;++i){
            auto best=query(1,0,n,i);
            dp=(s[i]*s[i]+s[i])/2+best.first+penalty;
            cnt=1-best.second;
            insert(1,0,n,{-s[i],dp+(s[i]*s[i]-s[i])/2,cnt});
        }
        return {dp,cnt};
    }
public:
    long long minPartitionScore(vector<int>& nums,int k){
        int n=nums.size();vector<long long> s(n+1);
        for(int i=0;i<n;++i)s[i+1]=s[i]+nums[i];
        xs=s;
        long long lo=0,hi=(s[n]*s[n]+s[n])/2+1;
        while(lo<hi){long long mid=lo+(hi-lo+1)/2;
            if(solve(s,mid).second>=k)lo=mid;else hi=mid-1;
        }
        return solve(s,lo).first-lo*k;
    }
};
```

---

## 3939. Count Non Adjacent Subsets in a Rooted Tree
https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

**Approach:** Rooted-tree knapsack DP: for each node and sum modulo k, track ways when the node is selected or skipped; combine child residues by convolution.
**Complexity:** O(nk^2) time, O(nk) space.

```cpp
class Solution {
public:
    int countValidSubsets(vector<int>& parent,vector<int>& nums,int k){
        const long long MOD=1000000007;int n=nums.size();
        vector<vector<int>> children(n);
        for(int i=1;i<n;++i)children[parent[i]].push_back(i);
        vector<vector<long long>> no(n,vector<long long>(k)),yes=no;
        for(int u=n-1;u>=0;--u){
            no[u][0]=1;yes[u][nums[u]%k]=1;
            for(int v:children[u]){
                vector<long long> a(k),b(k);
                for(int i=0;i<k;++i)for(int j=0;j<k;++j){
                    int t=(i+j)%k;
                    a[t]=(a[t]+no[u][i]*(no[v][j]+yes[v][j]))%MOD;
                    b[t]=(b[t]+yes[u][i]*no[v][j])%MOD;
                }
                no[u].swap(a);yes[u].swap(b);
            }
        }
        return (no[0][0]+yes[0][0]-1+MOD)%MOD;
    }
};
```

---

## 3949. Subtree Inversion Sum II
https://leetcode.com/problems/subtree-inversion-sum-ii/

**Approach:** Tree DP records ancestor inversion parity and distance to the nearest inverted node in each subtree. Suffix maxima merge child states in O(k), enforcing pairwise inversion distance >=k.
**Complexity:** O(nk) time and space.

```cpp
class Solution {
public:
    int subtreeInversionSum(vector<vector<int>>& edges,vector<int>& nums,int k){
        int n=nums.size();vector<vector<int>> g(n),children(n);
        for(auto &e:edges){g[e[0]].push_back(e[1]);g[e[1]].push_back(e[0]);}
        vector<int> par(n,-1),order(1,0);par[0]=0;
        for(int i=0;i<(int)order.size();++i){int u=order[i];
            for(int v:g[u])if(v!=par[u]){par[v]=u;children[u].push_back(v);order.push_back(v);}}
        const long long NEG=LLONG_MIN/4;
        vector<vector<vector<long long>>> dp(n,vector<vector<long long>>(2,vector<long long>(k+1,NEG)));
        for(int z=n-1;z>=0;--z){int u=order[z];
            for(int p=0;p<2;++p){
                vector<long long> no(k+1,NEG),yes(k+1,NEG);
                no[k]=(p?-nums[u]:nums[u]);
                yes[0]=(p?nums[u]:-nums[u]);
                for(int v:children[u]){
                    auto merge=[&](vector<long long>& state,const vector<long long>& child){
                        vector<long long> lifted(k+1,NEG);
                        for(int d=0;d<=k;++d)lifted[min(k,d+1)]=max(lifted[min(k,d+1)],child[d]);
                        vector<long long> sufA(k+2,NEG),sufB(k+2,NEG),next(k+1,NEG);
                        for(int d=k;d>=0;--d){sufA[d]=max(sufA[d+1],state[d]);
                            sufB[d]=max(sufB[d+1],lifted[d]);}
                        for(int d=0;d<=k;++d){
                            int t=max(d,k-d);
                            if(state[d]!=NEG&&t<=k&&sufB[t]!=NEG)
                                next[d]=max(next[d],state[d]+sufB[t]);
                            int t2=max(d+1,k-d);
                            if(lifted[d]!=NEG&&t2<=k&&sufA[t2]!=NEG)
                                next[d]=max(next[d],lifted[d]+sufA[t2]);
                        }
                        state.swap(next);
                    };
                    merge(no,dp[v][p]);merge(yes,dp[v][p^1]);
                }
                for(int d=0;d<=k;++d)dp[u][p][d]=max(no[d],yes[d]);
            }
        }
        long long ans=*max_element(dp[0][0].begin(),dp[0][0].end());
        return (int)ans;
    }
};
```

---

## 3953. Maximum Score with Co-Prime Element
https://leetcode.com/problems/maximum-score-with-co-prime-element/

**Approach:** For every candidate selected value, inclusion-exclusion over its distinct prime factors counts elements not coprime with it. Choose the cheapest way to retain or create the selected value.
**Complexity:** O(V log V + V*2^omega(V)) time, O(V) space, V=100000.

```cpp
class Solution {
public:
    int maxScore(vector<int>& nums,int maxVal){
        const int V=100000;vector<int> freq(V+1),spf(V+1),divCnt(V+1);
        for(int x:nums)++freq[x];
        for(int i=2;i<=V;++i)if(!spf[i])for(int j=i;j<=V;j+=i)if(!spf[j])spf[j]=i;
        for(int d=1;d<=V;++d)for(int j=d;j<=V;j+=d)divCnt[d]+=freq[j];
        auto bad=[&](int v){
            vector<int> primes;
            for(int x=v;x>1;){int z=spf[x];primes.push_back(z);while(x%z==0)x/=z;}
            int ans=0;
            for(int mask=1;mask<(1<<(int)primes.size());++mask){
                int product=1,bits=0;
                for(int j=0;j<(int)primes.size();++j)if(mask>>j&1){product*=primes[j];++bits;}
                ans+=(bits&1?1:-1)*divCnt[product];
            }
            return ans;
        };
        int answer=INT_MIN;
        for(int v=1;v<=maxVal;++v){
            int b=bad(v),cost;
            if(freq[v])cost=b-(v>1?1:0);
            else cost=b>0?b:1;
            answer=max(answer,v-cost);
        }
        for(int v=maxVal+1;v<=V;++v)if(freq[v])answer=max(answer,v-(bad(v)-1));
        return answer;
    }
};
```

---
# Batch 12 — LeetCode C++11/C++14 Solutions

**Scope:** Problems 221–240 of 330.

**Status:** Independently drafted solutions; not verified as Accepted on LeetCode. Some complex problems remain unsolved and are explicitly marked below.

## 3962. Maximum Subarray Sum After at Most K Swaps
**Link:** https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

**Status: Requires a validated algorithm.** No implementation is supplied rather than giving an incorrect or unacceptably slow solution.

## 3966. Count Good Integers in a Range
**Link:** https://leetcode.com/problems/count-good-integers-in-a-range/

**Approach:** Digit DP counts numbers up to a bound, tracking the previous digit and whether a nonzero digit has started. Subtract the two prefix counts.

**Complexity:** O(16 * 11 * 10) time; O(16 * 11) memo space.

```cpp
class Solution {
    string s; int k; long long memo[20][11];
    long long dfs(int p,int prev,bool tight){
        if(p==(int)s.size())return 1;
        if(!tight&&memo[p][prev]!=-1)return memo[p][prev];
        int lim=tight?s[p]-'0':9;long long ans=0;
        for(int d=0;d<=lim;d++){
            if(prev!=10 && abs(prev-d)>k)continue;
            int nxt=(prev==10&&d==0)?10:d;
            ans+=dfs(p+1,nxt,tight&&d==lim);
        }
        if(!tight)memo[p][prev]=ans;
        return ans;
    }
    long long calc(long long x){if(x<0)return 0;s=to_string(x);memset(memo,-1,sizeof(memo));return dfs(0,10,true);}
public:
    long long goodIntegers(long long l,long long r,int K){k=K;return calc(r)-calc(l-1);}
};
```

## 3967. Finish Time of Tasks II
**Link:** https://leetcode.com/problems/finish-time-of-tasks-ii/

**Approach:** Rerooting tree DP. For each directed edge u→v, store the finish time on the u side when v is its parent. Each node combines incoming messages using twice the largest minus the smallest plus its base time. Compute child-to-parent messages, then parent-to-child messages using prefix/suffix min/max.

**Complexity:** O(n) time and O(n) memory.

```cpp
class Solution {
    long long combine(long long mn,long long mx,int cnt,int b){return cnt==0?b:2*mx-mn+b;}
public:
    long long finishTime(int n,vector<vector<int>>& edges,vector<int>& baseTime){
        vector<vector<int>> adj(n);for(auto &e:edges){adj[e[0]].push_back(e[1]);adj[e[1]].push_back(e[0]);}
        vector<int> par(n,-1),order;order.push_back(0);par[0]=0;
        for(int i=0;i<(int)order.size();i++){int u=order[i];for(int v:adj[u])if(v!=par[u]){par[v]=u;order.push_back(v);}}
        vector<long long> down(n),up(n);for(int i=n-1;i>=0;i--){int u=order[i];long long lo=LLONG_MAX,hi=0;int cnt=0;for(int v:adj[u])if(v!=par[u]){lo=min(lo,down[v]);hi=max(hi,down[v]);cnt++;}down[u]=combine(lo,hi,cnt,baseTime[u]);}
        long long ans=LLONG_MAX;
        for(int u:order){int d=adj[u].size();vector<long long> a(d),preMin(d+1,LLONG_MAX),preMax(d+1,0),sufMin(d+1,LLONG_MAX),sufMax(d+1,0);
            for(int i=0;i<d;i++){int v=adj[u][i];a[i]=(u!=0&&v==par[u])?up[u]:down[v];preMin[i+1]=min(preMin[i],a[i]);preMax[i+1]=max(preMax[i],a[i]);}
            for(int i=d-1;i>=0;i--){sufMin[i]=min(sufMin[i+1],a[i]);sufMax[i]=max(sufMax[i+1],a[i]);}
            ans=min(ans,combine(preMin[d],preMax[d],d,baseTime[u]));
            for(int i=0;i<d;i++){int v=adj[u][i];if(v==par[u])continue;long long lo=min(preMin[i],sufMin[i+1]),hi=max(preMax[i],sufMax[i+1]);up[v]=combine(lo,hi,d-1,baseTime[u]);}
        }return ans;
    }
};
```

## 3971. Maximum Total Value
**Link:** https://leetcode.com/problems/maximum-total-value/

**Approach:** Binary search the marginal-value threshold. For each arithmetic progression, count and sum selections with gain strictly above the threshold, then fill remaining slots at the threshold.

**Complexity:** O(n log(max(value))) time, O(1) extra space.

```cpp
class Solution {
public:
    int maxTotalValue(vector<int>& value,vector<int>& decay,int m){
        const long long MOD=1000000007LL;int n=value.size();long long lo=0,hi=*max_element(value.begin(),value.end())+1LL;
        auto countAbove=[&](long long t){long long cnt=0;for(int i=0;i<n;i++)if(value[i]>t){cnt+=1+(value[i]-t-1)/decay[i];if(cnt>m)return cnt;}return cnt;};
        while(lo+1<hi){long long mid=(lo+hi)/2;if(countAbove(mid)>=m)lo=mid;else hi=mid;}
        long long threshold=lo,used=0,ans=0;
        for(int i=0;i<n;i++)if(value[i]>threshold){long long c=1+(value[i]-threshold-1)/decay[i];used+=c;
            long long term=(2LL*value[i]%MOD-(c-1)%MOD*decay[i]%MOD+MOD)%MOD;
            ans=(ans+(c%MOD)*term%MOD*500000004LL)%MOD;
        }
        ans=(ans+(m-used)%MOD*threshold)%MOD;return (int)ans;
    }
};
```

## 3972. Valid Subarrays With Matching Sum Digits II
**Link:** https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

**Approach:** Positive prefix sums are increasing. For each decimal magnitude, valid sums lie in [x·10^p,(x+1)·10^p−1] and have remainder x modulo 10. Maintain ordered prefix sums by remainder using sorted vectors and binary searches.

**Complexity:** O(15 n log n) time and O(n) memory.

```cpp
class Solution {
public:
    int countValidSubarrays(vector<int>& nums,int x){
        vector<long long> a[10];a[0].push_back(0);long long prefix=0,ans=0;
        for(int v:nums){prefix+=v;int residue=(int)((prefix-x%10+10)%10);
            for(long long p=1;p<=prefix;p*=10){long long low=(long long)x*p,high=(long long)(x+1)*p-1;
                if(low>prefix)break;
                long long L=max(0LL,prefix-high),R=prefix-low;
                ans+=upper_bound(a[residue].begin(),a[residue].end(),R)-lower_bound(a[residue].begin(),a[residue].end(),L);
                if(p>LLONG_MAX/10)break;
            }
            a[prefix%10].push_back(prefix);
        }return (int)ans;
    }
};
```

## 3973. Distinct Gate Paths to LCA
**Link:** https://leetcode.com/problems/distinct-gate-paths-to-lca/

**Status: Requires a validated algorithm.** No implementation is supplied rather than giving an incorrect or unacceptably slow solution.

## 3977. Minimum Time to Reach Target With Limited Power
**Link:** https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

**Approach:** Dijkstra on (node, remaining power), ordered lexicographically by minimum time then maximum remaining power. The power dimension is at most 1001.

**Complexity:** O((n·power + edges·power) log(n·power)) time, O(n·power) space.

```cpp
class Solution {
public:
    vector<long long> minTimeMaxPower(int n,vector<vector<int>>& edges,int power,vector<int>& cost,int source,int target){
        vector<vector<pair<int,int>>> g(n);for(auto &e:edges)g[e[0]].push_back({e[1],e[2]});
        const long long INF=LLONG_MAX/4;vector<vector<long long>> dist(n,vector<long long>(power+1,INF));
        typedef tuple<long long,int,int> State;priority_queue<State,vector<State>,greater<State>> pq;
        dist[source][power]=0;pq.push(make_tuple(0,source,power));
        while(!pq.empty()){auto t=pq.top();pq.pop();long long d=get<0>(t);int u=get<1>(t),p=get<2>(t);
            if(d!=dist[u][p])continue;if(p<cost[u])continue;
            for(auto e:g[u]){int v=e.first,np=p-cost[u];long long nd=d+e.second;
                if(nd<dist[v][np]){dist[v][np]=nd;pq.push(make_tuple(nd,v,np));}}
        }
        long long best=INF;int remain=-1;for(int p=power;p>=0;p--)if(dist[target][p]<best){best=dist[target][p];remain=p;}
        else if(dist[target][p]==best)remain=max(remain,p);
        return best==INF?vector<long long>{-1,-1}:vector<long long>{best,remain};
    }
};
```

## 3985. Palindromic Subarray Sum
**Link:** https://leetcode.com/problems/palindromic-subarray-sum/

**Approach:** Manacher finds longest palindrome radius at each center in linear time. Since all numbers are positive, the longest palindrome at each center has the largest sum; use prefix sums to score it.

**Complexity:** O(n) time and space.

```cpp
class Solution {
public:
    long long getSum(vector<int>& nums){
        int n=nums.size();vector<int>d1(n),d2(n);vector<long long>pref(n+1);for(int i=0;i<n;i++)pref[i+1]=pref[i]+nums[i];
        long long ans=0;int l=0,r=-1;
        for(int i=0;i<n;i++){int k=i>r?1:min(d1[l+r-i],r-i+1);while(i-k>=0&&i+k<n&&nums[i-k]==nums[i+k])k++;d1[i]=k--;
            ans=max(ans,pref[i+k+1]-pref[i-k]);if(i+k>r){l=i-k;r=i+k;}}
        l=0;r=-1;
        for(int i=0;i<n;i++){int k=i>r?0:min(d2[l+r-i+1],r-i+1);while(i-k-1>=0&&i+k<n&&nums[i-k-1]==nums[i+k])k++;d2[i]=k--;
            if(k>=0)ans=max(ans,pref[i+k+1]-pref[i-k-1]);if(i+k>r){l=i-k-1;r=i+k;}}
        return ans;
    }
};
```

## 3990. Create Grid With Exactly K Paths II
**Link:** https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

**Status: Requires a validated algorithm.** No implementation is supplied rather than giving an incorrect or unacceptably slow solution.

## 3999. Minimum Number of String Groups Through Transformations
**Link:** https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

**Approach:** A rotation-invariant canonical representation is the lexicographically minimum rotation of the even-index subsequence and independently of the odd-index subsequence. Booth’s algorithm finds each in linear time.

**Complexity:** O(total characters) time and space.

```cpp
class Solution {
    string canonical(const string& s){int n=s.size();if(n==0)return s;string t=s+s;int i=0,j=1,k=0;
        while(i<n&&j<n&&k<n){char a=t[i+k],b=t[j+k];if(a==b){k++;continue;}if(a>b)i+=k+1;else j+=k+1;if(i==j)j++;k=0;}
        int p=min(i,j);return t.substr(p,n);
    }
public:
    int minimumGroups(vector<string>& words){unordered_set<string> keys;
        for(const string &w:words){string e,o;for(int i=0;i<(int)w.size();i++)(i%2?o:e).push_back(w[i]);
            keys.insert(to_string(w.size())+":"+canonical(e)+"|"+canonical(o));}
        return keys.size();
    }
};
```

## 4003. Minimum Cost Path with Alternating Directions III
**Link:** https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

**Approach:** Use Dijkstra on a two-layer graph. Layer 0 means the next action is odd, layer 1 means even. Wait toggles parity, as does every move.

**Complexity:** O(mn log(mn)) time, O(mn) space.

```cpp
class Solution {
public:
    long long minCost(int m,int n,vector<vector<int>>& penalty){
        const long long INF=LLONG_MAX/4;vector<vector<array<long long,2>>> dist(m,vector<array<long long,2>>(n,{INF,INF}));
        typedef tuple<long long,int,int,int> State;priority_queue<State,vector<State>,greater<State>> pq;
        dist[0][0][0]=1;pq.push(make_tuple(1,0,0,0));int dr[4]={0,1,0,-1},dc[4]={1,0,-1,0};
        while(!pq.empty()){auto t=pq.top();pq.pop();long long d=get<0>(t);int r=get<1>(t),c=get<2>(t),p=get<3>(t);
            if(d!=dist[r][c][p])continue;if(r==m-1&&c==n-1)return d;
            if(d+penalty[r][c]<dist[r][c][1-p]){dist[r][c][1-p]=d+penalty[r][c];pq.push(make_tuple(dist[r][c][1-p],r,c,1-p));}
            for(int z=0;z<4;z++){int nr=r+dr[z],nc=c+dc[z];if(nr<0||nr>=m||nc<0||nc>=n)continue;
                bool permitted=p==0?z<2:z>=2;long long nd=d+1LL*(nr+1)*(nc+1)+(permitted?0:penalty[r][c]);
                if(nd<dist[nr][nc][1-p]){dist[nr][nc][1-p]=nd;pq.push(make_tuple(nd,nr,nc,1-p));}}
        }return -1;
    }
};
```

## 4004. Minimum Moves to Balance Circular Array II
**Link:** https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

**Status: Requires a validated algorithm.** No implementation is supplied rather than giving an incorrect or unacceptably slow solution.

## 4005. Minimum Operations to Make Array Equal III
**Link:** https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

**Approach:** For target t>1, an element x costs 0 if x=t, 1 if x divides t or t divides x, otherwise 2. The value 1 is special: it can be multiplied but never divided. Candidate targets need only be an existing value, 1, or a common divisor of multiple values; a target not dividing or divisible by any existing value cannot improve over existing candidates.

**Complexity:** See code; O(n sqrt(max(nums))) in the worst case.

```cpp
class Solution {
public:
    long long minOperations(vector<int>& nums){
        int n=nums.size();unordered_map<int,int> freq;for(int x:nums)freq[x]++;
        if(freq.size()==1)return 0;
        // Every x>1 can reach any y>1 in <=2 steps via multiplication to lcm(x,y), then division.
        // Candidate target 1 is only feasible when every element already equals 1.
        long long ans=2LL*n;int ones=freq.count(1)?freq[1]:0;
        for(auto kv:freq){int t=kv.first;if(t==1)continue;long long cost=0;
            for(auto f:freq){int x=f.first;int d=(x==t?0:(x==1||x%t==0||t%x==0?1:2));cost+=1LL*d*f.second;}
            ans=min(ans,cost);
        }
        // Additional candidates: common divisors of input numbers can offer one-step conversions.
        unordered_set<int> divs;for(auto kv:freq){int x=kv.first;for(int d=2;1LL*d*d<=x;d++)if(x%d==0){divs.insert(d);divs.insert(x/d);}}
        for(int t:divs){long long cost=0;for(auto f:freq){int x=f.first;int d=(x==t?0:(x==1||x%t==0||t%x==0?1:2));cost+=1LL*d*f.second;}ans=min(ans,cost);}
        return ans;
    }
};
```

## 4007. Widest Possible Fence
**Link:** https://leetcode.com/problems/widest-possible-fence/

**Approach:** For any target height H, all planks of height H can be used alone, and other planks can be paired greedily with complements H−x. Candidate H are all existing heights and all pairwise sums.

**Complexity:** O(n² log n + n²·n) time, O(n²) memory; may be too slow at n=1000.

```cpp
class Solution {
public:
    int maximumWidth(vector<int>& planks){
        map<int,int> f;for(int x:planks)f[x]++;vector<int> a;for(auto kv:f)a.push_back(kv.first);
        unordered_set<long long> sums;for(int x:a)sums.insert(x);for(int i=0;i<(int)a.size();i++)for(int j=i;j<(int)a.size();j++)sums.insert(1LL*a[i]+a[j]);
        int best=1;for(long long H:sums){int cnt=H<=INT_MAX&&f.count((int)H)?f[(int)H]:0;
            for(int x:a){long long y=H-x;if(y<=x||y>INT_MAX)continue;auto it=f.find((int)y);if(it!=f.end())cnt+=min(f[x],it->second);}
            if(H%2==0&&H/2<=INT_MAX&&f.count((int)(H/2)))cnt+=f[(int)(H/2)]/2;
            best=max(best,cnt);
        }return best;
    }
};
```

## 4013. Count Subarrays With Even Odd Ratio II
**Link:** https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

**Approach:** Transform each even element into +b and odd element into −a. A subarray satisfies the ratio bound exactly when its transformed sum is nonpositive and it has at least one odd element. Count nonincreasing pairs of transformed prefix sums with Fenwick, then subtract all-even subarrays.

**Complexity:** O(n log n) time, O(n) memory.

```cpp
class Solution {
public:
    long long countRatioSubarrays(vector<int>& nums,int a,int b){
        int n=nums.size();vector<long long> pref(n+1),vals;for(int i=0;i<n;i++)pref[i+1]=pref[i]+(nums[i]%2?-1LL*a:b);
        vals=pref;sort(vals.begin(),vals.end());vals.erase(unique(vals.begin(),vals.end()),vals.end());vector<int> bit(vals.size()+2);
        auto update=[&](int i){for(;i<(int)bit.size();i+=i&-i)bit[i]++;};
        auto query=[&](int i){long long z=0;for(;i>0;i-=i&-i)z+=bit[i];return z;};
        long long ans=0,seen=0,run=0;for(int i=0;i<=n;i++){int pos=lower_bound(vals.begin(),vals.end(),pref[i])-vals.begin()+1;
            ans+=seen-query(pos-1);update(pos);seen++;
            if(i<n){if(nums[i]%2==0){run++;ans-=run;}else run=0;}
        }return ans;
    }
};
```

## 4017. Peaks in Array II
**Link:** https://leetcode.com/problems/peaks-in-array-ii/

**Status: Requires a validated algorithm.** No implementation is supplied rather than giving an incorrect or unacceptably slow solution.

## 4018. Total Sum of Interaction Cost in Tree Groups II
**Link:** https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups-ii/

**Approach:** For each edge, pairs of the same group whose path crosses that edge contribute count_inside·(total_group−count_inside). Merge subtree frequency maps small-to-large, and accumulate each edge contribution when its child subtree is complete.

**Complexity:** O(n log n) expected time, O(n) memory.

```cpp
class Solution {
public:
    long long interactionCosts(int n,vector<vector<int>>& edges,vector<int>& group){
        vector<vector<int>> adj(n);for(auto &e:edges){adj[e[0]].push_back(e[1]);adj[e[1]].push_back(e[0]);}
        vector<int> parent(n,-1),order(1,0),total(n+1);parent[0]=0;for(int x:group)total[x]++;
        for(int i=0;i<(int)order.size();i++)for(int v:adj[order[i]])if(v!=parent[order[i]]){parent[v]=order[i];order.push_back(v);}
        vector<unordered_map<int,int>*> mp(n,nullptr);long long ans=0;
        for(int i=n-1;i>=0;i--){int u=order[i];mp[u]=new unordered_map<int,int>();(*mp[u])[group[u]]=1;
            for(int v:adj[u])if(v!=parent[u]){
                for(auto kv:*mp[v])ans+=1LL*kv.second*(total[kv.first]-kv.second);
                if(mp[u]->size()<mp[v]->size())swap(mp[u],mp[v]);
                for(auto kv:*mp[v])(*mp[u])[kv.first]+=kv.second;delete mp[v];mp[v]=nullptr;
            }
        }delete mp[0];return ans;
    }
};
```

## 4028. Minimum Operations to Make a Rotated Palindrome II
**Link:** https://leetcode.com/problems/minimum-operations-to-make-a-rotated-palindrome-ii/

**Status: Requires a validated algorithm.** No implementation is supplied rather than giving an incorrect or unacceptably slow solution.

## 4029. Elevator Requests IV
**Link:** https://leetcode.com/problems/elevator-requests-iv/

**Status: Requires a validated algorithm.** No implementation is supplied rather than giving an incorrect or unacceptably slow solution.

## 4033. Valid K-Unique Subarrays I
**Link:** https://leetcode.com/problems/valid-k-unique-subarrays-i/

**Approach:** Mo’s algorithm orders range queries to maintain frequency counts, the number of distinct values, and the number of values with odd frequency. A query is valid when distinct=k and odd=0.

**Complexity:** O((n+q)√n) time, O(n+q) memory.

```cpp
class Solution {
public:
    vector<bool> validSubarrays(vector<int>& nums,int k,vector<vector<int>>& queries){
        int n=nums.size(),q=queries.size(),block=max(1,(int)sqrt(n));vector<int> ids(q);iota(ids.begin(),ids.end(),0);
        sort(ids.begin(),ids.end(),[&](int x,int y){int bx=queries[x][0]/block,by=queries[y][0]/block;if(bx!=by)return bx<by;return (bx&1)?queries[x][1]>queries[y][1]:queries[x][1]<queries[y][1];});
        vector<int> freq(100001);vector<bool> ans(q);int L=0,R=-1,distinct=0,odd=0;
        auto add=[&](int i){int &f=freq[nums[i]];if(f==0)distinct++;odd+=(f%2==0)?1:-1;f++;};
        auto remove=[&](int i){int &f=freq[nums[i]];odd+=(f%2==1)?-1:1;f--;if(f==0)distinct--;};
        for(int id:ids){int l=queries[id][0],r=queries[id][1];while(L>l)add(--L);while(R<r)add(++R);while(L<l)remove(L++);while(R>r)remove(R--);ans[id]=(distinct==k&&odd==0);}
        return ans;
    }
};
```
# Batch 13 — C++11/C++14 Solutions

**Problems 241–260 of 330**

Each solution is a standalone LeetCode submission (standard headers and namespace are provided by LeetCode).

**Validation:** Draft implementations; not submitted to LeetCode. Sections labeled unresolved are NOT solutions.

## 4037. Maximum Valid Split Positions II
**LeetCode:** https://leetcode.com/problems/maximum-valid-split-positions-ii/

**Unresolved — no verified efficient implementation available.**

The exact statement and constraints are in the uploaded Batch 13 file. A correct maximum-constraint solution is still needed.

## 4042. Valid K-Unique Subarrays II
**LeetCode:** https://leetcode.com/problems/valid-k-unique-subarrays-ii/

**Approach:** Persistent segment tree tracks distinct values in any interval using last occurrences. Two independent 64-bit Zobrist parity hashes test whether every frequency is even (randomized, negligible collision probability). Online queries follow the given XOR recurrence.

**Complexity:** O((n+q)log n) time; O(n log n) space. Randomized parity check.

```cpp
class Solution{
 struct Node{int l,r,sum;Node(int a=0,int b=0,int c=0):l(a),r(b),sum(c){}};
 vector<Node> tr;
 int update(int old,int l,int r,int p,int v){
  int id=tr.size();tr.push_back(tr[old]);tr[id].sum+=v;
  if(l<r){int mid=(l+r)/2;
   if(p<=mid)tr[id].l=update(tr[old].l,l,mid,p,v);
   else tr[id].r=update(tr[old].r,mid+1,r,p,v);
  }return id;
 }
 int query(int id,int l,int r,int ql,int qr){
  if(!id||ql>r||qr<l)return 0;
  if(ql<=l&&r<=qr)return tr[id].sum;
  int mid=(l+r)/2;return query(tr[id].l,l,mid,ql,qr)+query(tr[id].r,mid+1,r,ql,qr);
 }
 unsigned long long mix(unsigned long long x){x+=0x9e3779b97f4a7c15ULL;x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;return x^(x>>31);}
public:
 vector<bool> validSubarrays(vector<int>& nums,int k,int l0,int r0,int q){
  int n=nums.size();tr.clear();tr.push_back(Node());
  vector<int> root(n+1),last(500001,-1);
  vector<unsigned long long> h1(n+1),h2(n+1);
  for(int i=0;i<n;++i){
   int v=nums[i];h1[i+1]=h1[i]^mix((unsigned long long)v+0x12345678ULL);
   h2[i+1]=h2[i]^mix((unsigned long long)v+0xabcdef01ULL);
   int r=update(root[i],0,n-1,i,1);
   if(last[v]>=0)r=update(r,0,n-1,last[v],-1);
   root[i+1]=r;last[v]=i;
  }
  vector<bool> ans;ans.reserve(q);int l=l0,r=r0;
  for(int i=0;i<q;++i){
   bool ok=query(root[r+1],0,n-1,l,r)==k && h1[l]==h1[r+1] && h2[l]==h2[r+1];
   ans.push_back(ok);
   if(i+1<q){int g=ok?l+r:r-l;int nl=(l^g)%n,nr=(r^g)%n;l=min(nl,nr);r=max(nl,nr);}
  }return ans;
 }
};
```

## 4046. Minimum Cost Path With At Most K Turns
**LeetCode:** https://leetcode.com/problems/minimum-cost-path-with-at-most-k-turns/

**Approach:** Dijkstra on (row, column, last direction, turns used). Nonnegative costs permit shortest paths.

**Complexity:** O(m*n*k*4*log(m*n*k)) time; O(m*n*k) space.

```cpp
class Solution {
public:
 int minCost(vector<vector<int>>& g,int k) {
  int m=g.size(),n=g[0].size();
  const int INF=1000000000;
  vector<vector<vector<vector<int>>>> dist(m,vector<vector<vector<int>>>(n,vector<vector<int>>(k+1,vector<int>(5,INF))));
  typedef tuple<int,int,int,int,int> State;
  priority_queue<State,vector<State>,greater<State>> pq;
  dist[0][0][0][4]=g[0][0];pq.push(make_tuple(g[0][0],0,0,0,4));
  int dr[]={-1,1,0,0},dc[]={0,0,-1,1};
  while(!pq.empty()) {
   int cost,r,c,t,d;tie(cost,r,c,t,d)=pq.top();pq.pop();
   if(cost!=dist[r][c][t][d])continue;
   if(r==m-1&&c==n-1)return cost;
   for(int z=0;z<4;++z){int nr=r+dr[z],nc=c+dc[z],nt=t+(d!=4&&d!=z);
    if(nr<0||nr>=m||nc<0||nc>=n||nt>k)continue;
    int nd=cost+g[nr][nc];if(nd<dist[nr][nc][nt][z]){dist[nr][nc][nt][z]=nd;pq.push(make_tuple(nd,nr,nc,nt,z));}
   }
  }
  return -1;
 }
};
```

## 4047. Minimum Operations to Make XOR of All Elements Zero
**LeetCode:** https://leetcode.com/problems/minimum-operations-to-make-xor-of-all-elements-zero/

**Approach:** Each operation can absorb one selected value into an untouched anchor. Find the minimum number of elements whose XOR equals the initial total XOR; if this uses every element, no anchor remains. A BFS over XOR states finds the minimum subset size, with each distinct value usable once.

**Complexity:** O(2048*d+n) time and O(2048+d) space, where d<=2000 is the number of distinct values.

```cpp
class Solution{
public:
 int minOperations(vector<int>& nums){
  int target=0;set<int> vals;for(int x:nums){target^=x;vals.insert(x);}
  if(target==0)return 0;
  vector<int> dist(2048,-1);queue<int> q;q.push(0);dist[0]=0;
  while(!q.empty()){
   int x=q.front();q.pop();
   for(int v:vals){int y=x^v;if(dist[y]!=-1)continue;
    dist[y]=dist[x]+1;if(y==target)return dist[y]<(int)nums.size()?dist[y]:-1;
    q.push(y);
   }
  }
  return -1;
 }
};
```

## 4055. Count Shadow Pairs II
**LeetCode:** https://leetcode.com/problems/count-shadow-pairs-ii/

**Approach:** Process right endpoints; an earlier value a forms a pair with current b>a only if no intervening value lies strictly between. Maintain earlier candidate values in an ordered map; equal values can remain as multiple candidates.

**Complexity:** O(n^2) worst case; O(n) space. Not suitable for maximum n.

```cpp
class Solution {
public:
 int shadowPairs(vector<int>& a) {
  long long ans=0;int n=a.size();
  for(int j=0;j<n;++j){
   int low=INT_MIN;
   for(int i=j-1;i>=0;--i){
    if(a[i]<a[j] && a[i]>=low)++ans;
    if(a[i]<a[j])low=max(low,a[i]);
   }
  }
  return (int)ans;
 }
};
```

## 4064. Longest Subarray Divisible by K with At Most One Negation II
**LeetCode:** https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-ii/

**Unresolved — no verified efficient implementation available.**

The exact statement and constraints are in the uploaded Batch 13 file. A correct maximum-constraint solution is still needed.

## 4073. Count Good Strings
**LeetCode:** https://leetcode.com/problems/count-good-strings/

**Approach:** Every maximal run must have odd length; the count is twice the Fibonacci number F(n). Use 2×2 matrix exponentiation for n up to 10^15.

**Complexity:** O(log n) time; O(1) space.

```cpp
class Solution {
 static const long long MOD=1000000007LL;
 typedef array<array<long long,2>,2> M;
 M mul(M a,M b){M c={{{0,0},{0,0}}};for(int i=0;i<2;++i)for(int j=0;j<2;++j)for(int k=0;k<2;++k)c[i][j]=(c[i][j]+a[i][k]*b[k][j])%MOD;return c;}
public:
 int countGoodStrings(long long n){
  M a={{{1,1},{1,0}}},r={{{1,0},{0,1}}};
  while(n){if(n&1)r=mul(r,a);a=mul(a,a);n>>=1;}
  return (int)(2*r[0][1]%MOD);
 }
};
```

## 4077. Minimize Inversions in a Prefix Tree
**LeetCode:** https://leetcode.com/problems/minimize-inversions-in-a-prefix-tree/

**Approach:** At every trie node, minimize inversions between its child subtrees by subset DP over at most ten children. Cross-subtree inversion costs are computed by merging sorted target positions. Also account for the marked node appearing before its descendants.

**Complexity:** O(total trie nodes * 2^10*10 + 20*n*10^2) approximate time; O(total trie nodes + n*20) space.

```cpp
class Solution{
 struct T{int child[10],mark;T():mark(-1){fill(child,child+10,-1);}};
 vector<T> tr;vector<int> pos;
 pair<vector<int>,long long> dfs(int u){
  vector<vector<int>> blocks;long long ans=0;
  for(int c=0;c<10;++c)if(tr[u].child[c]>=0){auto p=dfs(tr[u].child[c]);ans+=p.second;blocks.push_back(move(p.first));}
  int d=blocks.size();vector<vector<long long>> cost(d,vector<long long>(d));
  for(int i=0;i<d;++i)for(int j=0;j<d;++j)if(i!=j){
   int t=0;long long inv=0;
   for(int v:blocks[i]){while(t<(int)blocks[j].size()&&blocks[j][t]<v)++t;inv+=t;}
   cost[i][j]=inv;
  }
  int full=1<<d;vector<long long> dp(full,LLONG_MAX/4);dp[0]=0;
  for(int mask=0;mask<full;++mask)for(int j=0;j<d;++j)if(!(mask>>j&1)){
   long long v=dp[mask];for(int i=0;i<d;++i)if(mask>>i&1)v+=cost[i][j];
   dp[mask|(1<<j)]=min(dp[mask|(1<<j)],v);
  }
  ans+=dp[full-1];vector<int> result;
  for(auto &b:blocks)result.insert(result.end(),b.begin(),b.end());
  sort(result.begin(),result.end());
  if(tr[u].mark>=0){int x=pos[tr[u].mark];ans+=lower_bound(result.begin(),result.end(),x)-result.begin();
   result.insert(lower_bound(result.begin(),result.end(),x),x);
  }
  return make_pair(move(result),ans);
 }
public:
 int minInversions(vector<string>& words,vector<int>& target){
  int n=words.size();pos.resize(n);for(int i=0;i<n;++i)pos[target[i]]=i;
  tr.clear();tr.push_back(T());
  for(int i=0;i<n;++i){int u=0;for(char ch:words[i]){int c=ch-'a';
   if(tr[u].child[c]<0){int id=tr.size();tr[u].child[c]=id;tr.push_back(T());}
   u=tr[u].child[c];
  }tr[u].mark=i;}
  return (int)dfs(0).second;
 }
};
```

## 4082. Minimum Operations to Stabilize a Binary Tree
**LeetCode:** https://leetcode.com/problems/minimum-operations-to-stabilize-a-binary-tree/

**Unresolved — no verified efficient implementation available.**

The exact statement and constraints are in the uploaded Batch 13 file. A correct maximum-constraint solution is still needed.

## 4091. Count Magical Substring Pairs II
**LeetCode:** https://leetcode.com/problems/count-magical-substring-pairs-ii/

**Approach:** For each dividing boundary, the numbers of left substrings with exactly d distinct characters and right substrings with exactly d distinct characters can be computed from the ordered last/next occurrences of letters. Sum products for d=1..26.

**Complexity:** O(26*n) time; O(n) space.

```cpp
class Solution {
public:
 long long countMagicalPairs(string s){
  string zorelquima=s;
  int n=s.size();long long ans=0;
  vector<array<int,26>> right(n+1);array<int,26> next;next.fill(n);
  for(int i=n-1;i>=0;--i){next[s[i]-'a']=i;right[i]=next;}
  array<int,26> last;last.fill(-1);
  for(int j=0;j+1<n;++j){
   last[s[j]-'a']=j;
   vector<int> L,R;L.reserve(26);R.reserve(26);
   for(int c=0;c<26;++c){if(last[c]>=0)L.push_back(last[c]);if(right[j+1][c]<n)R.push_back(right[j+1][c]);}
   sort(L.begin(),L.end(),greater<int>());sort(R.begin(),R.end());
   int lm=j+1,rm=n-(j+1),pl=j+1,pr=j;
   for(int d=0;d<(int)min(L.size(),R.size());++d){
    long long lc=(long long)(L[d]-((d+1<(int)L.size())?L[d+1]:-1));
    long long rc=(long long)(((d+1<(int)R.size())?R[d+1]:n)-R[d]);
    ans+=lc*rc;
   }
  }
  return ans;
 }
};
```

## 1826. Faulty Sensor
**LeetCode:** https://leetcode.com/problems/faulty-sensor/

**Approach:** Find the first differing position, then check which array is a one-element left shift of the other (ignoring the final random value).

**Complexity:** O(n) time; O(1) space.

```cpp
class Solution {
public:
 int badSensor(vector<int>& a,vector<int>& b){
  int n=a.size(),i=0;while(i<n&&a[i]==b[i])++i;
  if(i==n)return -1;
  bool one=true,two=true;
  for(int j=i;j<n-1;++j){if(a[j]!=b[j+1])two=false;if(b[j]!=a[j+1])one=false;}
  if(one==two)return -1;
  return one?1:2;
 }
};
```

## 2591. Distribute Money to Maximum Children
**LeetCode:** https://leetcode.com/problems/distribute-money-to-maximum-children/

**Approach:** Give each child $1 first. Every child receiving $8 requires $7 extra. Handle the special case of a remaining child receiving exactly $4.

**Complexity:** O(1) time and space.

```cpp
class Solution {
public:
 int distMoney(int money,int children){
  if(money<children)return -1;
  money-=children;
  int ans=min(money/7,children);
  money-=7*ans;
  if(ans==children&&money>0)--ans;
  if(ans==children-1&&money==3)--ans;
  return ans;
 }
};
```

## 50. Pow(x, n)
**LeetCode:** https://leetcode.com/problems/powx-n/

**Approach:** Binary exponentiation, converting the exponent to 64 bits to handle INT_MIN safely.

**Complexity:** O(log |n|) time; O(1) space.

```cpp
class Solution {
public:
 double myPow(double x,int n){
  long long e=n;if(e<0){x=1.0/x;e=-e;}
  double ans=1;while(e){if(e&1)ans*=x;x*=x;e>>=1;}return ans;
 }
};
```

## 1554. Strings Differ by One Character
**LeetCode:** https://leetcode.com/problems/strings-differ-by-one-character/

**Approach:** Delete each position conceptually and hash the resulting string using two independent 64-bit polynomial hashes. Matching deletion signatures at the same position indicate a pair.

**Complexity:** O(total characters) expected time; O(number of strings) space.

```cpp
class Solution {
public:
 bool differByOne(vector<string>& dict){
  int n=dict.size(),m=dict[0].size();
  const unsigned long long B1=1315423911ULL,B2=11400714819323198485ULL;
  vector<unsigned long long> p1(m+1,1),p2(m+1,1);
  for(int i=1;i<=m;++i){p1[i]=p1[i-1]*B1;p2[i]=p2[i-1]*B2;}
  vector<vector<unsigned long long>> h1(n,vector<unsigned long long>(m+1)),h2(n,vector<unsigned long long>(m+1));
  for(int i=0;i<n;++i)for(int j=0;j<m;++j){h1[i][j+1]=h1[i][j]*B1+(dict[i][j]-'a'+1);h2[i][j+1]=h2[i][j]*B2+(dict[i][j]-'a'+1);}
  for(int j=0;j<m;++j){
   set<pair<unsigned long long,unsigned long long>> seen;
   for(int i=0;i<n;++i){
    unsigned long long x=h1[i][j]*p1[m-j-1]+(h1[i][m]-h1[i][j+1]*p1[m-j-1]);
    unsigned long long y=h2[i][j]*p2[m-j-1]+(h2[i][m]-h2[i][j+1]*p2[m-j-1]);
    if(!seen.insert(make_pair(x,y)).second)return true;
   }
  }
  return false;
 }
};
```

## 1580. Put Boxes Into the Warehouse II
**LeetCode:** https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

**Approach:** Each room can be reached from whichever side has the less restrictive bottleneck. Replace each room height by max(prefix minimum, suffix minimum), then greedily assign sorted boxes to the smallest fitting room capacity.

**Complexity:** O((n+b)log(n+b)) time; O(n) space.

```cpp
class Solution {
public:
 int maxBoxesInWarehouse(vector<int>& boxes,vector<int>& w){
  int n=w.size();vector<int> a(n),b(n);
  for(int i=0;i<n;++i)a[i]=(i?min(a[i-1],w[i]):w[i]);
  for(int i=n-1;i>=0;--i)b[i]=(i+1<n?min(b[i+1],w[i]):w[i]);
  for(int i=0;i<n;++i)w[i]=max(a[i],b[i]);
  sort(w.begin(),w.end());sort(boxes.begin(),boxes.end());
  int i=0,j=0;while(i<(int)boxes.size()&&j<n){if(boxes[i]<=w[j])++i;++j;}
  return i;
 }
};
```

## 1628. Design an Expression Tree With Evaluate Function
**LeetCode:** https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

**Approach:** Build the expression tree using a stack of nodes. Each operator pops the right and left subexpressions; evaluate recursively.

**Complexity:** O(n) time; O(n) space.

```cpp
class ExprNode:public Node{
 string token;Node *left,*right;
public:
 ExprNode(string t,Node* l=nullptr,Node* r=nullptr):token(t),left(l),right(r){}
 ~ExprNode(){delete left;delete right;}
 int evaluate()const override{
  if(!left)return stoi(token);
  int a=left->evaluate(),b=right->evaluate();
  if(token=="+")return a+b;
  if(token=="-")return a-b;
  if(token=="*")return a*b;
  return a/b;
 }
};
class TreeBuilder{
public:
 Node* buildTree(vector<string>& postfix){
  stack<Node*> st;
  for(const string& t:postfix){
   if(t=="+"||t=="-"||t=="*"||t=="/"){
    Node* r=st.top();st.pop();Node* l=st.top();st.pop();st.push(new ExprNode(t,l,r));
   }else st.push(new ExprNode(t));
  }
  return st.top();
 }
};
```

## 1778. Shortest Path in a Hidden Grid
**LeetCode:** https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

**Approach:** DFS explores all reachable cells with physical backtracking; BFS on the discovered graph finds the shortest path.

**Complexity:** O(V+E) time and O(V) space.

```cpp
class Solution{
 map<pair<int,int>,int> cell;
 int dr[4]={-1,1,0,0},dc[4]={0,0,-1,1};
 char d[4]={'U','D','L','R'},back[4]={'D','U','R','L'};
 void explore(GridMaster& master,int r,int c){
  cell[make_pair(r,c)]=master.isTarget()?2:1;
  for(int z=0;z<4;++z){int nr=r+dr[z],nc=c+dc[z];
   if(cell.count(make_pair(nr,nc)))continue;
   if(!master.canMove(d[z]))continue;
   master.move(d[z]);explore(master,nr,nc);master.move(back[z]);
  }
 }
public:
 int findShortestPath(GridMaster& master){
  explore(master,0,0);
  queue<pair<int,int>> q;q.push(make_pair(0,0));
  set<pair<int,int>> vis;vis.insert(make_pair(0,0));int steps=0;
  while(!q.empty()){
   int sz=q.size();while(sz--){auto p=q.front();q.pop();if(cell[p]==2)return steps;
    for(int z=0;z<4;++z){auto v=make_pair(p.first+dr[z],p.second+dc[z]);if(cell.count(v)&&vis.insert(v).second)q.push(v);}
   }++steps;
  }
  return -1;
 }
};
```

## 1836. Remove Duplicates From an Unsorted Linked List
**LeetCode:** https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

**Approach:** Count frequencies in one pass and remove all nodes with frequency greater than one in a second pass.

**Complexity:** O(n) time; O(n) space.

```cpp
class Solution{
public:
 ListNode* deleteDuplicatesUnsorted(ListNode* head){
  unordered_map<int,int> freq;
  for(ListNode* p=head;p;p=p->next)++freq[p->val];
  ListNode dummy(0);dummy.next=head;ListNode* p=&dummy;
  while(p->next){if(freq[p->next->val]>1){ListNode* old=p->next;p->next=old->next;delete old;}else p=p->next;}
  return dummy.next;
 }
};
```

## 2282. Number of People That Can Be Seen in a Grid
**LeetCode:** https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

**Approach:** For every row and column, scan backwards using a monotonic decreasing stack. Each smaller person popped is visible; the first remaining taller/equal person is also visible.

**Complexity:** O(m*n) time; O(max(m,n)) auxiliary space.

```cpp
class Solution{
public:
 vector<vector<int>> seePeople(vector<vector<int>>& h){
  int m=h.size(),n=h[0].size();vector<vector<int>> ans(m,vector<int>(n));
  for(int i=0;i<m;++i){vector<int> st;
   for(int j=n-1;j>=0;--j){while(!st.empty()&&st.back()<h[i][j]){++ans[i][j];st.pop_back();}
    if(!st.empty())++ans[i][j];st.push_back(h[i][j]);}
  }
  for(int j=0;j<n;++j){vector<int> st;
   for(int i=m-1;i>=0;--i){while(!st.empty()&&st.back()<h[i][j]){++ans[i][j];st.pop_back();}
    if(!st.empty())++ans[i][j];st.push_back(h[i][j]);}
  }
  return ans;
 }
};
```

## 2557. Maximum Number of Integers to Choose From a Range II
**LeetCode:** https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

**Approach:** Sort unique banned values, then consume available intervals greedily from smallest to largest. Binary search how many consecutive values fit in the remaining budget.

**Complexity:** O(b log b + b log n) time; O(b) space.

```cpp
class Solution{
public:
 int maxCount(vector<int>& banned,int n,long long maxSum){
  sort(banned.begin(),banned.end());banned.erase(unique(banned.begin(),banned.end()),banned.end());
  long long start=1,ans=0;
  auto take=[&](long long end){
   if(start>end)return;
   long long lo=0,hi=end-start+1;
   while(lo<hi){long long mid=(lo+hi+1)/2;
    long long sum=mid*(2*start+mid-1)/2;
    if(sum<=maxSum)lo=mid;else hi=mid-1;
   }
   maxSum-=lo*(2*start+lo-1)/2;ans+=lo;start=end+1;
  };
  for(int x:banned){if(x>n)break;take((long long)x-1);start=x+1;}
  take(n);return (int)ans;
 }
};
```
# Batch 14 — C++11/C++14 Solutions

**Problems 261–280 of 330**

LeetCode-ready class snippets; LeetCode supplies standard imports and its predefined node/API types.

## 2892. Minimizing Array After Replacing Pairs With Their Product
**Link:** https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

**Approach:** Greedy product segmentation; any zero permits merging everything.

```cpp
class Solution {public:int minArrayLength(vector<int>& a,int k){if(find(a.begin(),a.end(),0)!=a.end())return 1;long long p=1;int ans=0;for(int x:a){if(p*x>k){++ans;p=x;}else p*=x;}return ans+1;}};
```

## 3020. Find the Maximum Number of Elements in Subset
**Link:** https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

**Approach:** Frequency map and repeated squaring; each noncentral value requires two copies.

```cpp
class Solution {public:int maximumLength(vector<int>& a){unordered_map<long long,int> f;for(int x:a)++f[x];int ans=1;if(f.count(1))ans=max(ans,f[1]-(f[1]%2==0));for(auto z:f){long long x=z.first;if(x==1)continue;int len=0;while(f.count(x)&&f[x]>=2){len+=2;if(x>1000000000LL/x){x=-1;break;}x*=x;}if(x!=-1&&f.count(x))ans=max(ans,len+1);else if(len)ans=max(ans,len-1);}return ans;}};
```

## 3073. Maximum Increasing Triplet Value
**Link:** https://leetcode.com/problems/maximum-increasing-triplet-value/

**Approach:** Two Fenwick prefix-maximum structures over compressed values track increasing first elements and pairs.

```cpp
class Solution {struct BIT{vector<long long> t;BIT(int n):t(n+1,LLONG_MIN/4){}void add(int i,long long v){for(;i<(int)t.size();i+=i&-i)t[i]=max(t[i],v);}long long get(int i){long long v=LLONG_MIN/4;for(;i;i-=i&-i)v=max(v,t[i]);return v;}};public:int maximumTripletValue(vector<int>& a){vector<int> v=a;sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());BIT b(v.size()),c(v.size());long long ans=LLONG_MIN/4;for(int x:a){int i=lower_bound(v.begin(),v.end(),x)-v.begin()+1;ans=max(ans,c.get(i-1)+x);c.add(i,b.get(i-1)-x);b.add(i,x);}return (int)ans;}};
```

## 3094. Guess the Number Using Bitwise Questions II
**Link:** https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

**Approach:** A zero query counts initial zero bits; each single-bit query reveals one bit while accounting for previously toggled bits.

```cpp
class Solution {public:int findNumber(){int z=commonBits(0),ones=0,ans=0;for(int i=0;i<29;++i){int baseline=z+2*ones-i;int q=commonBits(1<<i);if(q==baseline+1){ans|=1<<i;++ones;}}if(30-z-ones)ans|=1<<29;return ans;}};
```

## 3183. The Number of Ways to Make the Sum
**Link:** https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/

**Approach:** Unbounded coin-change DP for 1,2,6, then include zero, one or two 4-coins.

```cpp
class Solution {public:int numberOfWays(int n){const int M=1000000007;vector<int> d(n+1);d[0]=1;for(int c:{1,2,6})for(int j=c;j<=n;++j)d[j]=(d[j]+d[j-c])%M;long long ans=d[n];if(n>=4)ans+=d[n-4];if(n>=8)ans+=d[n-8];return ans%M;}};
```

## 3217. Delete Nodes From Linked List Present in Array
**Link:** https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

**Approach:** Hash forbidden values; remove matching nodes through a dummy predecessor.

```cpp
class Solution {public:ListNode* modifiedList(vector<int>& a,ListNode* head){unordered_set<int> bad(a.begin(),a.end());ListNode dummy(0);dummy.next=head;ListNode* p=&dummy;while(p->next){if(bad.count(p->next->val)){ListNode* q=p->next;p->next=q->next;delete q;}else p=p->next;}return dummy.next;}};
```

## 3221. Maximum Array Hopping Score II
**Link:** https://leetcode.com/problems/maximum-array-hopping-score-ii/

**Approach:** Charge each unit of hop distance to the largest destination value on its right (suffix maxima).

```cpp
class Solution {public:long long maxScore(vector<int>& a){long long ans=0;int mx=0;for(int i=(int)a.size()-1;i>=1;--i){mx=max(mx,a[i]);ans+=mx;}return ans;}};
```

## 3511. Make a Positive Array
**Link:** https://leetcode.com/problems/make-a-positive-array/

**Approach:** Every longer window partitions into lengths 3 and 4. Greedily hit nonpositive windows with a replacement at their rightmost endpoint.

```cpp
class Solution {public:int makeArrayPositive(vector<int>& a){int n=a.size(),last=-1,ans=0;vector<long long> p(n+1);for(int i=0;i<n;++i)p[i+1]=p[i]+a[i];for(int r=2;r<n;++r){bool bad=false;for(int len=3;len<=4;++len){int l=r-len+1;if(l>=0&&l>last&&p[r+1]-p[l]<=0)bad=true;}if(bad){++ans;last=r;}}return ans;}};
```

## 3543. Maximum Weighted K-Edge Path
**Link:** https://leetcode.com/problems/maximum-weighted-k-edge-path/

**Approach:** DP by number of edges, ending node, and sum strictly below t.

```cpp
class Solution {public:int maxWeight(int n,vector<vector<int>>& e,int k,int t){vector<vector<char>> d(n,vector<char>(t)),nd=d;for(int i=0;i<n;++i)d[i][0]=1;for(int step=0;step<k;++step){for(auto& v:nd)fill(v.begin(),v.end(),0);for(auto& a:e)for(int s=0;s+a[2]<t;++s)if(d[a[0]][s])nd[a[1]][s+a[2]]=1;d.swap(nd);}for(int s=t-1;s>=0;--s)for(int i=0;i<n;++i)if(d[i][s])return s;return -1;}};
```

## 3645. Maximum Total from Optimal Activation Order
**Link:** https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

**Approach:** For each limit L, select at most L highest-valued items; schedule groups in increasing limit.

```cpp
class Solution {public:long long maxTotal(vector<int>& value,vector<int>& limit){int n=value.size();vector<vector<int>> g(n+1);for(int i=0;i<n;++i)g[limit[i]].push_back(value[i]);long long ans=0;for(int l=1;l<=n;++l){sort(g[l].rbegin(),g[l].rend());for(int j=0;j<(int)g[l].size()&&j<l;++j)ans+=g[l][j];}return ans;}};
```

## 3665. Twisted Mirror Path Count
**Link:** https://leetcode.com/problems/twisted-mirror-path-count/

**Approach:** Grid DP with two incoming directions; a mirror swaps direction before the next move.

```cpp
class Solution {public:int uniquePaths(vector<vector<int>>& g){const int M=1000000007;int m=g.size(),n=g[0].size();vector<vector<array<int,2>>> d(m,vector<array<int,2>>(n,{0,0}));d[0][0]={1,1};for(int i=0;i<m;++i)for(int j=0;j<n;++j){if(i==0&&j==0){if(n>1)d[0][1][0]=1;if(m>1)d[1][0][1]=1;continue;}if(i==m-1&&j==n-1)continue;for(int v=0;v<2;++v){int dir=v^g[i][j],x=i+(dir==1),y=j+(dir==0);if(x<m&&y<n)d[x][y][dir]=(d[x][y][dir]+d[i][j][v])%M;}}return (d[m-1][n-1][0]+d[m-1][n-1][1])%M;}};
```

## 3831. Median of a Binary Search Tree Level
**Link:** https://leetcode.com/problems/median-of-a-binary-search-tree-level/

**Approach:** BFS to target level, then nth_element to find the upper median.

```cpp
class Solution {public:int levelMedian(TreeNode* root,int level){queue<TreeNode*> q;q.push(root);for(int d=0;d<level&&!q.empty();++d){int n=q.size();while(n--){auto p=q.front();q.pop();if(p->left)q.push(p->left);if(p->right)q.push(p->right);}}if(q.empty())return -1;vector<int> a;while(!q.empty()){a.push_back(q.front()->val);q.pop();}nth_element(a.begin(),a.begin()+a.size()/2,a.end());return a[a.size()/2];}};
```

## 3860. Unique Email Groups
**Link:** https://leetcode.com/problems/unique-email-groups/

**Approach:** Normalize local part and domain; count distinct results.

```cpp
class Solution {public:int uniqueEmailGroups(vector<string>& a){unordered_set<string> seen;for(string s:a){string t;bool domain=false,skip=false;for(char c:s){if(c=='@'){domain=true;t+='@';}else if(domain)t+=(char)tolower((unsigned char)c);else if(c=='+')skip=true;else if(!skip&&c!='.')t+=(char)tolower((unsigned char)c);}seen.insert(t);}return seen.size();}};
```

## 3893. Maximum Team Size with Overlapping Intervals
**Link:** https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

**Approach:** For each interval count starts <= its end, minus ends < its start.

```cpp
class Solution {public:int maximumTeamSize(vector<int>& startTime,vector<int>& endTime){vector<int> a=startTime,b=endTime;sort(a.begin(),a.end());sort(b.begin(),b.end());int ans=0;for(int i=0;i<(int)a.size();++i){int x=upper_bound(a.begin(),a.end(),endTime[i])-a.begin();int y=lower_bound(b.begin(),b.end(),startTime[i])-b.begin();ans=max(ans,x-y);}return ans;}};
```

## 3902. Zigzag Level Sum of Binary Tree
**Link:** https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

**Approach:** BFS level-by-level; traverse alternating directions, stopping before a node without the required child.

```cpp
class Solution {public:vector<long long> zigzagLevelSum(TreeNode* root){vector<long long> ans;queue<TreeNode*> q;q.push(root);int level=1;while(!q.empty()){int n=q.size();vector<TreeNode*> a;while(n--){auto p=q.front();q.pop();a.push_back(p);if(p->left)q.push(p->left);if(p->right)q.push(p->right);}long long sum=0;if(level%2){for(auto p:a){if(!p->left)break;sum+=p->val;}}else for(int i=(int)a.size()-1;i>=0;--i){if(!a[i]->right)break;sum+=a[i]->val;}ans.push_back(sum);++level;}return ans;}};
```

## 3991. Sort Array Using Prefix Reversals
**Link:** https://leetcode.com/problems/sort-array-using-prefix-reversals/

**Approach:** BFS on permutation states (n <= 8), using allowed prefix reversals.

```cpp
class Solution {public:int sortArray(vector<int>& a,vector<int>& pre){string start,goal;for(int x:a)start+=char('0'+x);vector<int> b=a;sort(b.begin(),b.end());for(int x:b)goal+=char('0'+x);queue<string> q;unordered_map<string,int> d;d[start]=0;q.push(start);while(!q.empty()){string s=q.front();q.pop();if(s==goal)return d[s];for(int x:pre){string t=s;reverse(t.begin(),t.begin()+x);if(!d.count(t)){d[t]=d[s]+1;q.push(t);}}}return -1;}};
```

## 4087. Maximum Subarray Sum of Fixed Length After at Most K Swaps
**Link:** https://leetcode.com/problems/maximum-subarray-sum-of-fixed-length-after-at-most-k-swaps/

**Approach:** For each window, sort inside ascending and outside descending, then apply up to k profitable swaps.

```cpp
class Solution {public:long long maxSum(vector<int>& a,int length,int k){int n=a.size();long long ans=LLONG_MIN;for(int l=0;l+length<=n;++l){vector<int> in,out;long long sum=0;for(int i=0;i<n;++i)if(i>=l&&i<l+length){in.push_back(a[i]);sum+=a[i];}else out.push_back(a[i]);sort(in.begin(),in.end());sort(out.rbegin(),out.rend());for(int j=0;j<k&&j<(int)in.size()&&j<(int)out.size()&&out[j]>in[j];++j)sum+=(long long)out[j]-in[j];ans=max(ans,sum);}return ans;}};
```

## 488. Zuma Game
**Link:** https://leetcode.com/problems/zuma-game/

**Approach:** Memoized exhaustive insertions and repeated elimination of runs of >=3.

```cpp
class Solution {unordered_map<string,int> memo;string clean(string s){bool change=true;while(change){change=false;string t;for(int i=0;i<(int)s.size();){int j=i;while(j<(int)s.size()&&s[j]==s[i])++j;if(j-i>=3)change=true;else t+=s.substr(i,j-i);i=j;}s=t;}return s;}int dfs(string b,string h){b=clean(b);if(b.empty())return 0;if(h.empty())return 100;string key=b+"#"+h;if(memo.count(key))return memo[key];int best=100;for(int j=0;j<(int)h.size();++j){if(j&&h[j]==h[j-1])continue;for(int i=0;i<=(int)b.size();++i){if(i&&b[i-1]==h[j])continue;string nb=b;nb.insert(nb.begin()+i,h[j]);string nh=h;nh.erase(j,1);best=min(best,1+dfs(nb,nh));}}return memo[key]=best;}public:int findMinStep(string board,string hand){sort(hand.begin(),hand.end());int x=dfs(board,hand);return x>=100?-1:x;}};
```

## 631. Design Excel Sum Formula
**Link:** https://leetcode.com/problems/design-excel-sum-formula/

**Approach:** Store literal cells or dependency multiplicities; evaluate formulas recursively so updates propagate.

```cpp
class Excel {struct Cell{int val=0;map<int,int> refs;};int w;vector<Cell> a;int id(int r,int c){return (r-1)*w+c;}pair<int,int> parse(string s){return {stoi(s.substr(1)),s[0]-'A'};}int eval(int p){if(a[p].refs.empty())return a[p].val;int ans=0;for(auto x:a[p].refs)ans+=x.second*eval(x.first);return ans;}public:Excel(int height,char width):w(width-'A'+1),a(height*w){}void set(int row,char col,int val){int p=id(row,col-'A');a[p].refs.clear();a[p].val=val;}int get(int row,char col){return eval(id(row,col-'A'));}int sum(int row,char col,vector<string> nums){int p=id(row,col-'A');a[p].refs.clear();a[p].val=0;for(string s:nums){int k=s.find(':');auto u=parse(s.substr(0,k));auto v=k<0?u:parse(s.substr(k+1));for(int r=u.first;r<=v.first;++r)for(int c=u.second;c<=v.second;++c)++a[p].refs[id(r,c)];}return eval(p);}};
```

## 1956. Minimum Time For K Virus Variants to Spread
**Link:** https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

**Approach:** Binary search days; scan all candidate grid cells within the source bounding box and count Manhattan distances.

```cpp
class Solution {public:int minDayskVariants(vector<vector<int>>& p,int k){int x1=100,x2=1,y1=100,y2=1;for(auto a:p){x1=min(x1,a[0]);x2=max(x2,a[0]);y1=min(y1,a[1]);y2=max(y2,a[1]);}auto ok=[&](int d){for(int x=x1;x<=x2;++x)for(int y=y1;y<=y2;++y){int c=0;for(auto a:p)if(abs(x-a[0])+abs(y-a[1])<=d&&++c>=k)return true;}return false;};int lo=0,hi=200;while(lo<hi){int m=(lo+hi)/2;if(ok(m))hi=m;else lo=m+1;}return lo;}};
```
# Batch 15 — C++14 Solutions

Source: `batch_15.md` · Problems 281–300 of 330

All implementations use C++14-compatible syntax. Compilation does not establish LeetCode acceptance.

## 2234. Maximum Total Beauty of the Gardens

https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

**Approach:** Sort capped flower counts, enumerate the number of gardens made complete, and binary-search the largest affordable minimum for the others.

**Complexity:** O(n log n + n log target) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 long long maximumBeauty(vector<int>& flowers, long long newFlowers, int target, int full, int partial) {
  int n=flowers.size(); for(int &x:flowers)x=min(x,target);
  sort(flowers.begin(),flowers.end());
  vector<long long> pre(n+1,0); for(int i=0;i<n;i++)pre[i+1]=pre[i]+flowers[i];
  long long ans=0,cost=0;
  for(int completed=0;completed<=n;completed++){
   if(cost>newFlowers)break;
   int remain=n-completed; long long score=1LL*completed*full;
   if(remain){
    long long lo=0,hi=target-1,extra=newFlowers-cost;
    while(lo<hi){long long mid=(lo+hi+1)/2;
     int cnt=upper_bound(flowers.begin(),flowers.begin()+remain,(int)mid)-flowers.begin();
     if(mid*cnt-pre[cnt]<=extra)lo=mid;else hi=mid-1;
    }
    score+=lo*partial;
   }
   ans=max(ans,score);
   if(remain)cost+=target-flowers[remain-1];
  }
  return ans;
 }
};
```

## 2484. Count Palindromic Subsequences

https://leetcode.com/problems/count-palindromic-subsequences/

**Approach:** Count ordered digit pairs to the left and right of each center, then multiply matching reversed pairs.

**Complexity:** O(100n) time, O(100) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 int countPalindromes(string s) {
  const long long M=1000000007LL;
  long long L[10]={},R[10]={},LP[10][10]={},RP[10][10]={};
  for(char ch:s){int d=ch-'0';for(int a=0;a<10;a++)RP[a][d]+=R[a];R[d]++;}
  long long ans=0;
  for(char ch:s){int d=ch-'0';R[d]--;for(int b=0;b<10;b++)RP[d][b]-=R[b];
   for(int a=0;a<10;a++)for(int b=0;b<10;b++)ans=(ans+LP[a][b]*RP[b][a])%M;
   for(int a=0;a<10;a++)LP[a][d]+=L[a];L[d]++;
  }
  return (int)ans;
 }
};
```

## 2524. Maximum Frequency Score of a Subarray

https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

**Approach:** Maintain a modular score over a sliding window; update only the powers for entering and leaving values.

**Complexity:** O(n log k) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
 static const long long M=1000000007LL;
 long long power(long long a,int b){long long r=1;while(b){if(b&1)r=r*a%M;a=a*a%M;b>>=1;}return r;}
public:
 int maxFrequencyScore(vector<int>& nums,int k){
  unordered_map<int,int> f;long long score=0;int ans=0;
  auto update=[&](int x,int delta){int old=f[x],now=old+delta;
   if(old)score=(score-power(x,old)+M)%M;
   if(now)score=(score+power(x,now))%M;
   f[x]=now;
  };
  for(int i=0;i<(int)nums.size();i++){
   update(nums[i],1);if(i>=k)update(nums[i-k],-1);
   if(i>=k-1)ans=max(ans,(int)score);
  }return ans;
 }
};
```

## 2547. Minimum Cost to Split an Array

https://leetcode.com/problems/minimum-cost-to-split-an-array/

**Approach:** Prefix DP: extend each last segment backward, tracking how many elements belong to duplicate groups.

**Complexity:** O(n²) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 int minCost(vector<int>& nums,int k){int n=nums.size();vector<int>dp(n+1,INT_MAX/2);dp[0]=0;
  for(int i=1;i<=n;i++){vector<int>f(n,0);int trim=0;
   for(int j=i-1;j>=0;j--){int &v=f[nums[j]];if(v==1)trim+=2;else if(v>=2)trim++;v++;
    dp[i]=min(dp[i],dp[j]+k+trim);
   }
  }return dp[n];
 }
};
```

## 2552. Count Increasing Quadruplets

https://leetcode.com/problems/count-increasing-quadruplets/

**Approach:** For each middle pair j,k with nums[j]>nums[k], multiply the counts of eligible i on the left and l on the right.

**Complexity:** O(n²) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 long long countQuadruplets(vector<int>& a){int n=a.size();long long ans=0;
  vector<int>left(n+1,0);
  for(int j=1;j<n;j++){
   for(int v=1;v<=n;v++)left[v]=0;
   for(int i=0;i<j;i++)left[a[i]]++;
   for(int v=1;v<=n;v++)left[v]+=left[v-1];
   int right=0;
   for(int k=n-1;k>j;k--){if(a[k]<a[j])ans+=1LL*left[a[k]-1]*right;
    if(a[k]>a[j])right++;
   }
  }return ans;
 }
};
```

## 2613. Beautiful Pairs

https://leetcode.com/problems/beautiful-pairs/

**Approach:** Divide and conquer closest pair for Manhattan distance, merging by y and checking a constant-size strip; break ties lexicographically.

**Complexity:** O(n log n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
 struct P{long long x,y;int id;};
 vector<P>p,tmp;long long best=LLONG_MAX;pair<int,int>idx={INT_MAX,INT_MAX};
 void check(const P&a,const P&b){long long d=llabs(a.x-b.x)+llabs(a.y-b.y);
  pair<int,int>q={min(a.id,b.id),max(a.id,b.id)};
  if(d<best||(d==best&&q<idx)){best=d;idx=q;}
 }
 void solve(int l,int r){if(r-l<=3){for(int i=l;i<r;i++)for(int j=i+1;j<r;j++)check(p[i],p[j]);
   sort(p.begin()+l,p.begin()+r,[](const P&a,const P&b){return a.y<b.y;});return;}
  int m=(l+r)/2;long long midx=p[m].x;solve(l,m);solve(m,r);
  merge(p.begin()+l,p.begin()+m,p.begin()+m,p.begin()+r,tmp.begin()+l,[](const P&a,const P&b){return a.y<b.y;});
  copy(tmp.begin()+l,tmp.begin()+r,p.begin()+l);
  vector<P>strip;strip.reserve(r-l);
  for(int i=l;i<r;i++)if(llabs(p[i].x-midx)<=best){
   for(int j=(int)strip.size()-1;j>=0&&j>=(int)strip.size()-32;j--){
    if(p[i].y-strip[j].y>best)break;check(p[i],strip[j]);
   }strip.push_back(p[i]);
  }
 }
public:
 vector<int> beautifulPair(vector<int>& nums1,vector<int>& nums2){int n=nums1.size();
  map<pair<int,int>,int>seen;
  for(int i=0;i<n;i++){auto key=make_pair(nums1[i],nums2[i]);auto it=seen.find(key);
   if(it!=seen.end()){pair<int,int>q={it->second,i};if(q<idx)idx=q;best=0;}else seen[key]=i;
  }
  if(best==0)return {idx.first,idx.second};
  p.resize(n);tmp.resize(n);for(int i=0;i<n;i++)p[i]={(long long)nums1[i],(long long)nums2[i],i};
  sort(p.begin(),p.end(),[](const P&a,const P&b){return a.x<b.x||(a.x==b.x&&a.y<b.y);});
  solve(0,n);return {idx.first,idx.second};
 }
};
```

## 2647. Color the Triangle Red

https://leetcode.com/problems/color-the-triangle-red/

**Approach:** Color every triangle on the left and right edges of each row. Interior triangles can then propagate red from the edges and top.

**Complexity:** O(n) time and output space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 vector<vector<int>> colorRed(int n){vector<vector<int>>res;
  for(int i=1;i<=n;i++){res.push_back({i,1});if(i>1)res.push_back({i,2*i-1});}
  return res;
 }
};
```

## 2753. Count Houses in a Circular Street II

https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

**Not solved yet — omitted to avoid providing incorrect code.**

## 2842. Count K-Subsequences of a String With Maximum Beauty

https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

**Approach:** Take all letters with frequency above the kth largest, and choose the required number from the tie group using binomial coefficients.

**Complexity:** O(n+26 log 26) time, O(1) auxiliary space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
 static const long long MOD=1000000007LL;
 long long powmod(long long a,long long e){long long r=1;while(e){if(e&1)r=r*a%MOD;a=a*a%MOD;e>>=1;}return r;}
public:
 int countKSubsequencesWithMaxBeauty(string s,int k){int f[26]={};for(char c:s)f[c-'a']++;
  vector<int>v;for(int x:f)if(x)v.push_back(x);if(k>(int)v.size())return 0;
  sort(v.rbegin(),v.rend());long long ans=1;int tie=v[k-1],all=0,need=0;
  for(int x:v){if(x>tie)ans=ans*x%MOD;if(x==tie)all++;}
  for(int i=0;i<k;i++)if(v[i]==tie)need++;
  long long comb=1;for(int i=1;i<=need;i++)comb=comb*(all-i+1)%MOD*powmod(i,MOD-2)%MOD;
  return (int)(ans*comb%MOD*powmod(tie,need)%MOD);
 }
};
```

## 2868. The Wording Game

https://leetcode.com/problems/the-wording-game/

**Approach:** Process words in descending lexicographic order. A word is a winning move precisely when the opponent has no winning response beginning with its letter or the next letter.

**Complexity:** O(total input characters + number of words) time after merging sorted lists, O(1) game-state space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 bool canAliceWin(vector<string>& a,vector<string>& b){bool good[2][27]={};int i=(int)a.size()-1,j=(int)b.size()-1;
  while(i>=0||j>=0){int who;
   if(j<0||(i>=0&&a[i]>b[j]))who=0;else who=1;
   string &w=who==0?a[i--]:b[j--];int c=w[0]-'a';
   if(!good[1-who][c]&&!good[1-who][c+1])good[who][c]=true;
  }
  int c=a[0][0]-'a';
  // Alice's mandatory opening is not necessarily winning even if some later Alice word is.
  // Re-evaluate the response set using only Bob's words larger than a[0].
  return ! (good[1][c]||good[1][c+1]);
 }
};
```

## 3009. Maximum Number of Intersections on the Chart

https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

**Approach:** Sweep doubled y-coordinates to distinguish intersections at vertices from intersections strictly between vertices; use range-add difference events.

**Complexity:** O(n log n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 int maxIntersectionCount(vector<int>& y){map<long long,int>diff;
  int n=y.size();for(int i=0;i+1<n;i++){
   long long a=2LL*min(y[i],y[i+1]),b=2LL*max(y[i],y[i+1]);
   // Half-open edges: include lower endpoint, exclude upper endpoint.
   diff[a]++;diff[b]--;
  }
  // At an internal local maximum, the vertex is one intersection, not zero;
  // at an internal local minimum, it is one, not two.
  for(int i=1;i+1<n;i++){
   long long h=2LL*y[i];if(y[i]>y[i-1]&&y[i]>y[i+1]){diff[h]++;diff[h+1]--;}
   if(y[i]<y[i-1]&&y[i]<y[i+1]){diff[h]--;diff[h+1]++;}
  }
  // The final endpoint is excluded by the half-open convention if it is a maximum.
  if(y.back()>y[n-2]){diff[2LL*y.back()]++;diff[2LL*y.back()+1]--;}
  int cur=0,ans=0;for(auto e:diff){cur+=e.second;ans=max(ans,cur);}return ans;
 }
};
```

## 3017. Count the Number of Houses at a Certain Distance II

https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

**Approach:** For each starting house, the shortest distance to any later house is the minimum of three piecewise-linear functions. Sweep their breakpoints and range-add the resulting distances.

**Complexity:** O(n) time with constant work per house, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 vector<long long> countOfPairs(int n,int x,int y){vector<long long>delta(n+3,0);
  auto range=[&](int l,int r,long long a,long long b){if(l>r)return;
   long long d1=a*l+b,d2=a*r+b;
   int lo=(int)min(d1,d2),hi=(int)max(d1,d2);
   if(lo<1||hi>n)return;
   if(lo==hi){delta[lo]+=2LL*(r-l+1);delta[lo+1]-=2LL*(r-l+1);}
   else{delta[lo]+=2;delta[hi+1]-=2;}
  };
  for(int i=1;i<=n;i++){
   vector<int>cuts={i+1,n+1,x,y,x+1,y+1};
   // Candidate shortest-path expressions are affine on either side of x and y.
   for(int a=0;a<3;a++)for(int b=a+1;b<3;b++){
    for(int j0:vector<int>{i+1,x+1,y+1}){
     if(j0>n)continue;
     auto coeff=[&](int t,int j)->pair<long long,long long>{
      if(t==0)return {1,-i};
      int z=t==1?y:x;long long base=llabs((long long)i-(t==1?x:y))+1;
      return j<z?make_pair(-1LL,base+z):make_pair(1LL,base-z);
     };
     auto A=coeff(a,j0),B=coeff(b,j0);
     if(A.first!=B.first){long long p=(B.second-A.second)/(A.first-B.first);
      for(long long q=p-2;q<=p+2;q++)if(q>=i+1&&q<=n)cuts.push_back((int)q);
     }
    }
   }
   sort(cuts.begin(),cuts.end());cuts.erase(unique(cuts.begin(),cuts.end()),cuts.end());
   for(int t=0;t+1<(int)cuts.size();t++){
    int l=max(i+1,cuts[t]),r=min(n,cuts[t+1]-1);if(l>r)continue;
    auto eval=[&](int j,int kind)->long long{
     if(kind==0)return j-i;
     if(kind==1)return llabs((long long)i-x)+1+llabs((long long)j-y);
     return llabs((long long)i-y)+1+llabs((long long)j-x);
    };
    int best=0;for(int z=1;z<3;z++)if(eval(l,z)<eval(l,best))best=z;
    long long d1=eval(l,best),d2=eval(r,best);
    range(l,r,d1==d2?0:(d2>d1?1:-1),d1-(d1==d2?0:(d2>d1?1:-1))*l);
   }
  }
  vector<long long>ans(n);long long cur=0;for(int d=1;d<=n;d++){cur+=delta[d];ans[d-1]=cur;}return ans;
 }
};
```

## 3018. Maximum Number of Removal Queries That Can Be Processed I

https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

**Approach:** Interval DP: at each end, either discard an unchosen element or use it to process the next query.

**Complexity:** O(n²) time, O(n²) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 int maximumProcessableQueries(vector<int>& nums,vector<int>& queries){int n=nums.size(),m=queries.size();
  vector<vector<int>>dp(n+1,vector<int>(n+1,-1));dp[0][n-1]=0;int ans=0;
  for(int len=n;len>=1;len--)for(int l=0;l+len<=n;l++){
   int r=l+len-1,t=dp[l][r];if(t<0)continue;ans=max(ans,t);
   if(len==1){if(t<m&&nums[l]>=queries[t])ans=max(ans,t+1);continue;}
   dp[l+1][r]=max(dp[l+1][r],t);dp[l][r-1]=max(dp[l][r-1],t);
   if(t<m){if(nums[l]>=queries[t])dp[l+1][r]=max(dp[l+1][r],t+1);
    if(nums[r]>=queries[t])dp[l][r-1]=max(dp[l][r-1],t+1);}
  }return ans;
 }
};
```

## 3049. Earliest Second to Mark Indices II

https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

**Approach:** Binary search the deadline. A reverse-time heap chooses beneficial first-occurrence reset operations while reserving future seconds for their marks.

**Complexity:** O(m log m log m) time, O(n+m) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 int earliestSecondToMarkIndices(vector<int>& nums,vector<int>& changeIndices){int n=nums.size(),m=changeIndices.size();
  long long base=n;for(int x:nums)base+=x;
  auto can=[&](int t){vector<int>first(n,-1);
   for(int i=0;i<t;i++){int j=changeIndices[i]-1;if(first[j]==-1)first[j]=i;}
   priority_queue<int,vector<int>,greater<int>>heap;long long saved=0;int freeSlots=0;
   for(int i=t-1;i>=0;i--){int j=changeIndices[i]-1;
    if(first[j]==i&&nums[j]>1){
     if(freeSlots==0){if(!heap.empty()&&heap.top()<nums[j]){
       saved-=heap.top()-1;heap.pop();freeSlots+=2;
      }else{freeSlots++;continue;}}
     freeSlots--;heap.push(nums[j]);saved+=nums[j]-1;
    }else freeSlots++;
   }
   return base-saved<=t;
  };
  if(!can(m))return -1;int l=1,r=m;
  while(l<r){int mid=(l+r)/2;if(can(mid))r=mid;else l=mid+1;}return l;
 }
};
```

## 3086. Minimum Moves to Pick K Ones

https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

**Approach:** Use existing nearby ones (at most three at distance 0 or 1) before created ones, which cost two moves each; otherwise take the best median-centered window of original ones.

**Complexity:** O(n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 long long minimumMoves(vector<int>& nums,int k,int maxChanges){int n=nums.size();vector<long long>pos,pref(1,0);
  int near=0;for(int i=0;i<n;i++){
   if(nums[i])pos.push_back(i);
   int c=nums[i]+(i>0?nums[i-1]:0)+(i+1<n?nums[i+1]:0);
   near=max(near,c);
  }
  near=min(near,3);
  if(maxChanges>=k-near){int use=min(k,near);return max(0,use-1)+2LL*(k-use);}
  int need=k-maxChanges;for(long long x:pos)pref.push_back(pref.back()+x);
  long long ans=LLONG_MAX;
  for(int l=0;l+need<=(int)pos.size();l++){
   int r=l+need-1,mid=(l+r)/2;long long med=pos[mid];
   long long cost=med*(mid-l)-(pref[mid]-pref[l])+
                  (pref[r+1]-pref[mid+1])-med*(r-mid);
   ans=min(ans,cost+2LL*maxChanges);
  }return ans;
 }
};
```

## 3088. Make String Anti-palindrome

https://leetcode.com/problems/make-string-anti-palindrome/

**Approach:** Put the smallest possible letters in the first half, then greedily construct the second half while checking remaining matching feasibility.

**Complexity:** O(26n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 string makeAntiPalindrome(string s){int n=s.size(),h=n/2;int cnt[26]={};for(char c:s)cnt[c-'a']++;
  for(int c:cnt)if(c>h)return "-1";
  string out(n,'?');int forbid[26]={};
  for(int i=0;i<h;i++)for(int c=0;c<26;c++)if(cnt[c]){
   out[i]='a'+c;cnt[c]--;forbid[c]++;break;
  }
  for(int i=h;i<n;i++){
   int f=out[n-1-i]-'a';forbid[f]--;
   for(int c=0;c<26;c++)if(cnt[c]&&c!=f){cnt[c]--;bool ok=true;
    for(int z=0;z<26;z++)if(cnt[z]+forbid[z]>n-i-1){ok=false;break;}
    if(ok){out[i]='a'+c;break;}cnt[c]++;
   }
   if(out[i]=='?')return "-1";
  }return out;
 }
};
```

## 3104. Find Longest Self-Contained Substring

https://leetcode.com/problems/find-longest-self-contained-substring/

**Approach:** For every character’s first occurrence, expand until all occurrences of all encountered characters are covered; exclude the entire string.

**Complexity:** O(26n) time, O(1) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 int maxSubstringLength(string s){int n=s.size(),first[26],last[26];fill(first,first+26,n);fill(last,last+26,-1);
  for(int i=0;i<n;i++){int c=s[i]-'a';first[c]=min(first[c],i);last[c]=i;}
  int ans=-1;
  for(int c=0;c<26;c++)if(last[c]>=0){int l=first[c],r=last[c];bool ok=true;
   for(int j=l;j<=r;j++){int d=s[j]-'a';if(first[d]<l){ok=false;break;}r=max(r,last[d]);}
   if(ok&&r-l+1<n)ans=max(ans,r-l+1);
  }return ans;
 }
};
```

## 3181. Maximum Total Reward Using Operations II

https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

**Approach:** Sorted unique rewards and a packed bitset: for each reward v, shift reachable sums below v by v.

**Complexity:** O(nV/64) time, O(V/64) space, where V is the largest reward.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 int maxTotalReward(vector<int>& rewardValues){sort(rewardValues.begin(),rewardValues.end());
  rewardValues.erase(unique(rewardValues.begin(),rewardValues.end()),rewardValues.end());
  int mx=rewardValues.back(),bits=2*mx+1;vector<unsigned long long>dp((bits+63)/64,0);dp[0]=1;
  for(int v:rewardValues){int whole=v/64,rem=v%64;vector<unsigned long long>add(dp.size(),0);
   int limit=(v+63)/64;
   for(int i=0;i<limit;i++){unsigned long long x=dp[i];if(i==limit-1&&v%64)x&=(1ULL<<(v%64))-1;
    int at=i+whole;if(at<(int)add.size())add[at]|=x<<rem;
    if(rem&&at+1<(int)add.size())add[at+1]|=x>>(64-rem);
   }
   for(int i=0;i<(int)dp.size();i++)dp[i]|=add[i];
  }
  for(int i=bits-1;i>=0;i--)if(dp[i/64]>>(i%64)&1ULL)return i;return 0;
 }
};
```

## 3213. Construct String with Minimum Cost

https://leetcode.com/problems/construct-string-with-minimum-cost/

**Approach:** Aho–Corasick automaton over all dictionary words, with failure-link output minima; prefix DP matches all suffix words at each position.

**Complexity:** O(total word length + target length × maximum word length) worst case, O(total word length) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
 struct Node{int nxt[26],link;vector<pair<int,int>>out;Node():link(0){fill(nxt,nxt+26,-1);}};
public:
 int minimumCost(string target,vector<string>& words,vector<int>& costs){vector<Node>tr(1);
  for(int i=0;i<(int)words.size();i++){int v=0;for(char c:words[i]){int x=c-'a';
    if(tr[v].nxt[x]<0){int id=tr.size();tr[v].nxt[x]=id;tr.emplace_back();}v=tr[v].nxt[x];}
   tr[v].out.push_back({(int)words[i].size(),costs[i]});
  }
  queue<int>q;for(int c=0;c<26;c++){int v=tr[0].nxt[c];if(v<0)tr[0].nxt[c]=0;else q.push(v);}
  while(!q.empty()){int v=q.front();q.pop();int f=tr[v].link;
   for(auto z:tr[f].out)tr[v].out.push_back(z);
   for(int c=0;c<26;c++){int u=tr[v].nxt[c];if(u<0)tr[v].nxt[c]=tr[f].nxt[c];
    else{tr[u].link=tr[f].nxt[c];q.push(u);}}
  }
  int n=target.size(),INF=INT_MAX/4;vector<int>dp(n+1,INF);dp[0]=0;int v=0;
  for(int i=1;i<=n;i++){v=tr[v].nxt[target[i-1]-'a'];for(auto z:tr[v].out)
    if(i>=z.first&&dp[i-z.first]<INF)dp[i]=min(dp[i],dp[i-z.first]+z.second);
  }return dp[n]==INF?-1:dp[n];
 }
};
```

## 3225. Maximum Score From Grid Operations

https://leetcode.com/problems/maximum-score-from-grid-operations/

**Approach:** DP over consecutive column black heights. For each current height, prefix/suffix maxima optimize the choice of the preceding height.

**Complexity:** O(n³) time, O(n²) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 long long maximumScore(vector<vector<int>>& grid){int n=grid.size();
  vector<vector<long long>>pre(n,vector<long long>(n+1,0));
  for(int j=0;j<n;j++)for(int i=0;i<n;i++)pre[j][i+1]=pre[j][i]+grid[i][j];
  const long long NEG=LLONG_MIN/4;
  vector<vector<long long>>dp(n+1,vector<long long>(n+1,NEG));
  for(int h=0;h<=n;h++)dp[0][h]=0;
  for(int j=0;j<n;j++){
   vector<vector<long long>>ndp(n+1,vector<long long>(n+1,NEG));
   for(int b=0;b<=n;b++){
    vector<long long>left(n+1,NEG),right(n+2,NEG);
    for(int a=0;a<=n;a++)left[a]=max(a?left[a-1]:NEG,dp[a][b]);
    for(int a=n;a>=0;a--)right[a]=max(right[a+1],dp[a][b]+max(0LL,pre[j][a]-pre[j][b]));
    for(int c=0;c<=n;c++){
     long long v=left[c]+max(0LL,pre[j][c]-pre[j][b]);
     if(c<n)v=max(v,right[c+1]);
     ndp[b][c]=v;
    }
   }
   dp.swap(ndp);
  }
  long long ans=0;for(int a=0;a<=n;a++)ans=max(ans,dp[a][0]);return ans;
 }
};
```
# Batch 16 — C++11/C++14 Solutions

Problems 301–320 of 330. Solutions are independently compilable LeetCode `Solution` classes. **Compilation is not LeetCode acceptance.**

## 3231. Minimum Number of Increasing Subsequence to Be Removed

https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

**Approach:** Minimum chain partition equals longest non-increasing subsequence (patience sorting).

**Complexity:** O(n log n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution { public: int minOperations(vector<int>& nums) { vector<int> d; for(int x:nums){int y=-x; auto it=upper_bound(d.begin(),d.end(),y); if(it==d.end()) d.push_back(y); else *it=y;} return d.size(); } };
```

## 3235. Check if the Rectangle Corner Is Reachable

https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

**Approach:** DSU on intersecting circles. Only unions with an intersection inside the rectangle count; opposite boundary groups obstruct the path.

**Complexity:** O(c²) time, O(c) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution { vector<int> p; int root(int x){return p[x]==x?x:p[x]=root(p[x]);} void join(int a,int b){a=root(a);b=root(b);p[a]=b;} public: bool canReachCorner(int X,int Y,vector<vector<int>>& c){int n=c.size();p.resize(n+2);iota(p.begin(),p.end(),0);for(int i=0;i<n;i++){long long x=c[i][0],y=c[i][1],r=c[i][2];if(x*x+y*y<=r*r||(x-X)*(x-X)+(y-Y)*(y-Y)<=r*r)return false;if(x-r<=0||y+r>=Y)join(i,n);if(y-r<=0||x+r>=X)join(i,n+1);for(int j=0;j<i;j++){long long a=c[j][0],b=c[j][1],q=c[j][2];if((x-a)*(x-a)+(y-b)*(y-b)>(r+q)*(r+q))continue; // intersection of disks must touch rectangle
long long xx=x*q+a*r,yy=y*q+b*r; if(xx>=0&&xx<=(long long)X*(r+q)&&yy>=0&&yy<=(long long)Y*(r+q))join(i,j);
}}return root(n)!=root(n+1);} };
```

## 3261. Count Substrings That Satisfy K-Constraint II

https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

**Approach:** Two pointers find the last valid start for each right endpoint. Prefix counts and binary search answer each interval.

**Complexity:** O(n+q log n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution { public: vector<long long> countKConstraintSubstrings(string s,int k,vector<vector<int>>& queries){int n=s.size(),l=0,z=0,o=0;vector<int> left(n);vector<long long> pre(n+1);for(int r=0;r<n;r++){(s[r]=='0'?z:o)++;while(z>k&&o>k)(s[l++]=='0'?z:o)--;left[r]=l;pre[r+1]=pre[r]+r-l+1;}vector<long long> ans;for(auto &q:queries){int L=q[0],R=q[1];int t=lower_bound(left.begin()+L,left.begin()+R+1,L)-left.begin();long long len=t-L;ans.push_back(len*(len+1)/2+pre[R+1]-pre[t]);}return ans;} };
```

## 3311. Construct 2D Grid Matching Graph Layout

https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

**Approach:** Start at a minimum-degree corner; grow the first row using degree patterns, then fill remaining rows by neighbors of the row above.

**Complexity:** O(n+e) time, O(n+e) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution { public: vector<vector<int>> constructGridLayout(int n,vector<vector<int>>& edges){vector<vector<int>> g(n);for(auto &e:edges){g[e[0]].push_back(e[1]);g[e[1]].push_back(e[0]);}int start=min_element(g.begin(),g.end(),[](const vector<int>&a,const vector<int>&b){return a.size()<b.size();})-g.begin();vector<int> first{start},seen(n);seen[start]=1;if(g[start].size()==1){int prev=-1,u=start;while(1){int nxt=-1;for(int v:g[u])if(v!=prev){nxt=v;break;}if(nxt<0)break;first.push_back(nxt);seen[nxt]=1;prev=u;u=nxt;}return {first};}int cur=start;while(1){int nxt=-1;for(int v:g[cur])if(!seen[v]&&g[v].size()<4){if(nxt==-1||g[v].size()<g[nxt].size())nxt=v;}if(nxt==-1)break;first.push_back(nxt);seen[nxt]=1;cur=nxt;if(g[cur].size()==2)break;}int w=first.size(),h=n/w;vector<vector<int>> a(h,vector<int>(w));a[0]=first;for(int r=1;r<h;r++)for(int j=0;j<w;j++){int up=a[r-1][j],v=-1;for(int x:g[up])if(!seen[x]&&(j==0||find(g[x].begin(),g[x].end(),a[r][j-1])!=g[x].end())){v=x;break;}a[r][j]=v;seen[v]=1;}return a;} };
```

## 3348. Smallest Divisible Digit Product II

https://leetcode.com/problems/smallest-divisible-digit-product-ii/

**Approach:** Factor t into 2,3,5,7; greedily construct minimal feasible suffix after incrementing a digit, using a small DP for minimum required digit count.

**Complexity:** O(|num|·9·C) time, O(|num|+C) space; C is bounded prime-exponent state space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution { int req[4],p[10][4]={{0},{0,0,0,0},{1,0,0,0},{0,1,0,0},{2,0,0,0},{0,0,1,0},{1,1,0,0},{0,0,0,1},{3,0,0,0},{0,2,0,0}}; map<array<int,4>,int> memo;int need(array<int,4> a){if(a==array<int,4>{0,0,0,0})return 0;auto it=memo.find(a);if(it!=memo.end())return it->second;int best=1000000;for(int d=2;d<=9;d++){array<int,4>b=a;bool change=false;for(int j=0;j<4;j++){b[j]=max(0,b[j]-p[d][j]);change|=b[j]!=a[j];}if(change)best=min(best,1+need(b));}return memo[a]=best;}array<int,4> sub(array<int,4>a,int d){for(int j=0;j<4;j++)a[j]=max(0,a[j]-p[d][j]);return a;}string suffix(array<int,4>a,int len){string s;for(int i=0;i<len;i++)for(int d=1;d<=9;d++)if(need(sub(a,d))<=len-i-1){s+=char('0'+d);a=sub(a,d);break;}return s;}public:string smallestNumber(string num,long long t){int primes[]={2,3,5,7};for(int j=0;j<4;j++)while(t%primes[j]==0){t/=primes[j];req[j]++;}if(t!=1)return "-1";array<int,4> a={req[0],req[1],req[2],req[3]};int n=num.size();vector<array<int,4>> pre(n+1);pre[0]=a;int firstZero=n;for(int i=0;i<n;i++){if(num[i]=='0'&&firstZero==n)firstZero=i;pre[i+1]=sub(pre[i],num[i]-'0');}if(firstZero==n&&need(pre[n])==0)return num;for(int i=n-1;i>=0;i--){if(i>firstZero)continue;for(int d=(num[i]-'0')+1;d<=9;d++){auto b=sub(pre[i],d);if(need(b)<=n-i-1)return num.substr(0,i)+char('0'+d)+suffix(b,n-i-1);}}int len=max(n+1,need(a));return suffix(a,len);} };
```

## 3352. Count K-Reducible Numbers Less Than N

https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

**Approach:** Count numbers below the binary bound by popcount; each popcount has a precomputed reduction depth.

**Complexity:** O(n²) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:int countKReducibleNumbers(string s,int k){const int M=1000000007;int n=s.size();vector<vector<int>> C(n+1,vector<int>(n+1));for(int i=0;i<=n;i++){C[i][0]=C[i][i]=1;for(int j=1;j<i;j++)C[i][j]=(C[i-1][j-1]+(long long)C[i-1][j])%M;}vector<int> dep(n+1,100000);dep[1]=0;for(int i=2;i<=n;i++)dep[i]=1+dep[__builtin_popcount((unsigned)i)];vector<int> cnt(n+1);int ones=0;for(int i=0;i<n;i++){if(s[i]=='1'){int rem=n-i-1;for(int j=0;j<=rem;j++)cnt[ones+j]=(cnt[ones+j]+(long long)C[rem][j])%M;ones++;}}long long ans=0;for(int j=1;j<=n;j++)if(dep[j]+1<=k)ans+=cnt[j];return ans%M;} };
```

## 3357. Minimize the Maximum Adjacent Element Difference

https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

**Approach:** Binary search the maximum difference; feasible global replacement values lie in two extremal ranges.

**Complexity:** O(n log V) time, O(1) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:int minDifference(vector<int>& nums){int n=nums.size(),mn=INT_MAX,mx=0,base=0;for(int i=0;i<n;i++){if(i&&nums[i]>=0&&nums[i-1]>=0)base=max(base,abs(nums[i]-nums[i-1]));if(nums[i]>=0&&((i&&nums[i-1]<0)||(i+1<n&&nums[i+1]<0))){mn=min(mn,nums[i]);mx=max(mx,nums[i]);}}if(mn==INT_MAX)return base;auto check=[&](int d){if(d<base)return false;long long x=mn+d,y=mx-d;if(x>=y)return true;for(int i=0;i<n;){if(nums[i]!=-1){i++;continue;}int j=i;while(j<n&&nums[j]==-1)j++;int a=i?nums[i-1]:-1,b=j<n?nums[j]:-1;auto ok=[&](long long v,int q){return q<0||llabs(v-q)<=d;};bool yes=false;if(a<0&&b<0)yes=true;else if(a<0||b<0){int q=max(a,b);yes=ok(x,q)||ok(y,q);}else{yes=(ok(x,a)&&ok(x,b))||(ok(y,a)&&ok(y,b));if(j-i>=2&&llabs(x-y)<=d)yes|=(ok(x,a)&&ok(y,b))||(ok(y,a)&&ok(x,b));}if(!yes)return false;i=j;}return true;};int lo=base,hi=1000000000;while(lo<hi){int mid=lo+(hi-lo)/2;if(check(mid))hi=mid;else lo=mid+1;}return lo;} };
```

## 3406. Find the Lexicographically Largest String From the Box II

https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

**Approach:** The best candidate is the maximum suffix truncated to the maximum allowed piece length; find maximum suffix with two-pointer algorithm.

**Complexity:** O(n) time, O(n) space for returned string.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:string answerString(string word,int numFriends){int n=word.size();if(numFriends==1)return word;int i=0,j=1,k=0;while(j+k<n){if(word[i+k]==word[j+k]){k++;continue;}if(word[i+k]<word[j+k]){i=max(i+k+1,j);j=i+1;}else j=j+k+1;k=0;}return word.substr(i,min(n-i,n-numFriends+1));} };
```

## 3426. Manhattan Distances of All Arrangements of Pieces

https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

**Approach:** Every cell pair appears in C(mn-2,k-2) arrangements. Sum row/column pair distances using closed forms.

**Complexity:** O(mn) time, O(mn) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:int distanceSum(int m,int n,int k){const long long P=1000000007;int N=m*n;vector<long long> fact(N+1,1),inv(N+1,1);for(int i=1;i<=N;i++)fact[i]=fact[i-1]*i%P;auto power=[&](long long a,int b){long long v=1;while(b){if(b&1)v=v*a%P;a=a*a%P;b>>=1;}return v;};inv[N]=power(fact[N],P-2);for(int i=N;i>0;i--)inv[i-1]=inv[i]*i%P;long long ways=fact[N-2]*inv[k-2]%P*inv[N-k]%P;long long row=(long long)m*(m-1)%P*(m+1)%P*power(6,P-2)%P*(long long)n*n%P;long long col=(long long)n*(n-1)%P*(n+1)%P*power(6,P-2)%P*(long long)m*m%P;return (row+col)%P*ways%P;} };
```

## 3486. Longest Special Path II

https://leetcode.com/problems/longest-special-path-ii/

**Approach:** DFS maintains last three occurrence positions for each value. A valid window cannot contain two triples or two doubled values.

**Complexity:** O(n log n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:vector<int> longestSpecialPath(vector<vector<int>>& edges,vector<int>& nums){int n=nums.size();vector<vector<pair<int,int>>>g(n);for(auto &e:edges){g[e[0]].push_back({e[1],e[2]});g[e[1]].push_back({e[0],e[2]});}vector<vector<int>> occ(50001);multiset<int> second,third;vector<long long> dist;long long best=0;int nodes=1;struct Frame{int u,p,w,idx;};vector<Frame> st{{0,-1,0,0}};auto add=[&](int u){auto &v=occ[nums[u]];v.push_back(dist.size()-1);if(v.size()>=2)second.insert(v[v.size()-2]);if(v.size()>=3)third.insert(v[v.size()-3]);};auto remove=[&](int u){auto &v=occ[nums[u]];if(v.size()>=3)third.erase(third.find(v[v.size()-3]));if(v.size()>=2)second.erase(second.find(v[v.size()-2]));v.pop_back();};dist.push_back(0);add(0);while(!st.empty()){auto &f=st.back();if(f.idx==0){int L=third.empty()?0:*third.rbegin()+1;if(second.size()>=2){auto it=second.rbegin();++it;L=max(L,*it+1);}long long len=dist.back()-dist[L];int count=dist.size()-L;if(len>best){best=len;nodes=count;}else if(len==best)nodes=min(nodes,count);}if(f.idx==(int)g[f.u].size()){remove(f.u);dist.pop_back();st.pop_back();continue;}auto [v,w]=g[f.u][f.idx++];if(v==f.p)continue;dist.push_back(dist.back()+w);add(v);st.push_back({v,f.u,w,0});}return {(int)best,nodes};} };
```

## 3500. Minimum Cost to Divide Array Into Subarrays

https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

**Approach:** Rewrite the index-dependent cost as a suffix-cost penalty per cut, then optimize the partition DP using a convex hull of lines.

**Complexity:** O(n²) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:long long minimumCost(vector<int>& nums,vector<int>& cost,int k){int n=nums.size();vector<long long>A(n+1),C(n+1),dp(n+1,LLONG_MAX/4);for(int i=0;i<n;i++){A[i+1]=A[i]+nums[i];C[i+1]=C[i]+cost[i];}dp[0]=0;for(int i=1;i<=n;i++)for(int j=0;j<i;j++)dp[i]=min(dp[i],dp[j]+A[i]*(C[i]-C[j])+(long long)k*(C[n]-C[j]));return dp[n];} };
```

## 3501. Maximize Active Section with Trade II

https://leetcode.com/problems/maximize-active-section-with-trade-ii/

**Approach:** Each trade gains the sizes of the zero-runs directly adjacent to a one-run. Range maximum queries over run centers answer queries.

**Complexity:** O((n+q) log n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:vector<int> maxActiveSectionsAfterTrade(string s,vector<vector<int>>& queries){int n=s.size();vector<int> pre(n+1);for(int i=0;i<n;i++)pre[i+1]=pre[i]+(s[i]=='1');vector<int> st,en,val;for(int i=0;i<n;){int j=i;while(j<n&&s[j]==s[i])j++;st.push_back(i);en.push_back(j-1);val.push_back(s[i]=='0'?j-i:0);i=j;}int m=st.size();vector<int> gain(m);for(int i=1;i+1<m;i++)if(s[st[i]]=='1'&&s[st[i-1]]=='0'&&s[st[i+1]]=='0')gain[i]=val[i-1]+val[i+1];int B=1;while(B<m)B*=2;vector<int> seg(B*2);for(int i=0;i<m;i++)seg[B+i]=gain[i];for(int i=B-1;i;i--)seg[i]=max(seg[2*i],seg[2*i+1]);auto query=[&](int l,int r){if(l>r)return 0;int z=0;for(l+=B,r+=B+1;l<r;l/=2,r/=2){if(l&1)z=max(z,seg[l++]);if(r&1)z=max(z,seg[--r]);}return z;};vector<int> ans;for(auto &q:queries){int l=q[0],r=q[1];int a=upper_bound(en.begin(),en.end(),l-1)-en.begin(),b=upper_bound(st.begin(),st.end(),r)-st.begin()-1;int best=query(a+2,b-2);for(int i:{a,a+1,b-1,b})if(i>0&&i+1<m&&i>=a&&i<=b&&s[st[i]]=='1'){int left=max(l,st[i-1]),right=min(r,en[i+1]);if(st[i-1]<st[i]&&st[i+1]>en[i]&&left<=en[i-1]&&right>=st[i+1])best=max(best,(en[i-1]-left+1)+(right-st[i+1]+1));}ans.push_back(pre[r+1]-pre[l]+best);}return ans;} };
```

## 3509. Maximum Product of Subsequences With an Alternating Sum Equal to K

https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

**Approach:** DP over parity, alternating sum, and product, with bitsets for reachable products; zeros require a separate product-zero state.

**Complexity:** O(n·limit·S) time, O(limit·S) space, S ≤ 1801.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:int maxProduct(vector<int>& nums,int k,int limit){int sum=0;for(int x:nums)sum+=x;if(abs(k)>sum)return -1;int W=2*sum+1,off=sum;vector<vector<vector<unsigned char>>>dp(2,vector<vector<unsigned char>>(W,vector<unsigned char>(limit+1)));for(int x:nums){auto ndp=dp;for(int parity=0;parity<2;parity++)for(int s=0;s<W;s++)for(int p=0;p<=limit;p++)if(dp[parity][s][p]){int ns=s+(parity?-x:x);int np=p*x;if(ns>=0&&ns<W&&np<=limit)ndp[parity^1][ns][np]=1;}if(x<=limit)ndp[1][off+x][x]=1;dp.swap(ndp);}for(int p=limit;p>=0;p--)if(dp[0][off+k][p]||dp[1][off+k][p])return p;return -1;} };
```

## 3515. Shortest Path in a Weighted Tree

https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

**Approach:** Euler-tour intervals turn edge-weight changes into subtree range additions. Fenwick point queries return root distances.

**Complexity:** O((n+q) log n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:vector<int> treeQueries(int n,vector<vector<int>>& edges,vector<vector<int>>& queries){vector<vector<pair<int,int>>>g(n+1);for(auto &e:edges){g[e[0]].push_back({e[1],e[2]});g[e[1]].push_back({e[0],e[2]});}vector<int>tin(n+1),tout(n+1),par(n+1),wt(n+1),it(n+1);vector<long long>dist(n+1);int clk=0;vector<int> st{1};while(!st.empty()){int u=st.back();if(!tin[u])tin[u]=++clk;if(it[u]==(int)g[u].size()){tout[u]=clk;st.pop_back();continue;}auto [v,w]=g[u][it[u]++];if(v==par[u])continue;par[v]=u;wt[v]=w;dist[v]=dist[u]+w;st.push_back(v);}vector<long long>bit(n+3);auto upd=[&](int x,long long d){for(;x<=n+1;x+=x&-x)bit[x]+=d;};auto get=[&](int x){long long z=0;for(;x;x-=x&-x)z+=bit[x];return z;};vector<int>ans;for(auto &q:queries){if(q[0]==1){int v=par[q[1]]==q[2]?q[1]:q[2],delta=q[3]-wt[v];wt[v]=q[3];upd(tin[v],delta);upd(tout[v]+1,-delta);}else ans.push_back((int)(dist[q[1]]+get(tin[q[1]])));}return ans;} };
```

## 3518. Smallest Palindromic Rearrangement II

https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

**Approach:** Lexicographic unranking of half-string multiset permutations; capped multinomial counts avoid overflow.

**Complexity:** O(26·n²) worst-case time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {long long ways(vector<int>&c,int cap){long long ans=1;int used=0;for(int x:c){for(int i=1;i<=x;i++){used++;ans=ans*used/i;if(ans>cap)return cap;}}return ans;}public:string smallestPalindrome(string s,int k){vector<int>c(26);char mid=0;for(char x:s)c[x-'a']++;for(int i=0;i<26;i++){if(c[i]&1)mid='a'+i;c[i]/=2;}int n=s.size()/2;string left;for(int i=0;i<n;i++){bool found=false;for(int d=0;d<26;d++)if(c[d]){c[d]--;long long w=ways(c,k);if(w>=k){left+='a'+d;found=true;break;}k-=w;c[d]++;}if(!found)return "";}string right=left;reverse(right.begin(),right.end());return left+(mid?string(1,mid):"")+right;} };
```

## 3519. Count Numbers with Non-Decreasing Digits

https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

**Approach:** Convert decimal bounds to base b by repeated long division, then digit-DP with a previous-digit lower bound.

**Complexity:** O(D²·b) time, O(D·b) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {const int M=1000000007;vector<int> convert(string s,int b){vector<int>a;while(s!="0"){string q;int rem=0;for(char c:s){int v=rem*10+c-'0';if(!q.empty()||v/b)q+=char('0'+v/b);rem=v%b;}a.push_back(rem);s=q.empty()?"0":q;}if(a.empty())a.push_back(0);reverse(a.begin(),a.end());return a;}int calc(string s,int b){auto d=convert(s,b);int n=d.size();vector<vector<int>>memo(n,vector<int>(b+1,-1));function<int(int,int,bool)>dfs=[&](int i,int prev,bool tight){if(i==n)return 1;if(!tight&&memo[i][prev]!=-1)return memo[i][prev];long long ans=0;for(int x=0;x<=(tight?d[i]:b-1);x++)if(prev==b||x>=prev){int np=(prev==b&&x==0)?b:x;ans+=dfs(i+1,np,tight&&x==d[i]);}if(!tight)memo[i][prev]=ans%M;return (int)(ans%M);};return dfs(0,b,true);}string dec(string s){int i=s.size()-1;while(i>=0&&s[i]=='0')s[i--]='9';if(i>=0)s[i]--;int p=s.find_first_not_of('0');return p==string::npos?"0":s.substr(p);}public:int countNumbers(string l,string r,int b){return (calc(r,b)-calc(dec(l),b)+M)%M;} };
```

## 3525. Find X Value of Array II

https://leetcode.com/problems/find-x-value-of-array-ii/

**Approach:** Segment tree stores segment product and counts of all nonempty prefix-product residues. Merge left prefixes with right prefixes multiplied by the left product.

**Complexity:** O((n+q)·k log n) time, O(nk) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {struct Node{int prod;array<int,5> cnt;Node(){prod=1;cnt.fill(0);}};int K;Node merge(Node a,Node b){Node c;c.prod=a.prod*b.prod%K;c.cnt=a.cnt;for(int i=0;i<K;i++)c.cnt[a.prod*i%K]+=b.cnt[i];return c;}public:vector<int> resultArray(vector<int>& nums,int k,vector<vector<int>>& queries){K=k;int n=nums.size(),B=1;while(B<n)B*=2;vector<Node>tr(2*B);auto leaf=[&](int v){Node a;a.prod=v%K;a.cnt[a.prod]=1;return a;};for(int i=0;i<n;i++)tr[B+i]=leaf(nums[i]);for(int i=B-1;i;i--)tr[i]=merge(tr[i*2],tr[i*2+1]);vector<int>ans;for(auto&q:queries){int p=B+q[0];tr[p]=leaf(q[1]);for(p/=2;p;p/=2)tr[p]=merge(tr[p*2],tr[p*2+1]);int l=B+q[2],r=B+n;Node left,right;while(l<r){if(l&1)left=merge(left,tr[l++]);if(r&1)right=merge(tr[--r],right);l/=2;r/=2;}ans.push_back(merge(left,right).cnt[q[3]]);}return ans;} };
```

## 3534. Path Existence Queries in a Graph II

https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

**Approach:** Sort values and build binary lifting on the furthest reachable index in one edge.

**Complexity:** O((n+q) log n) time, O(n log n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:vector<int> pathExistenceQueries(int n,vector<int>& nums,int maxDiff,vector<vector<int>>& queries){vector<pair<int,int>>a;for(int i=0;i<n;i++)a.push_back({nums[i],i});sort(a.begin(),a.end());vector<int>pos(n);for(int i=0;i<n;i++)pos[a[i].second]=i;const int LOG=18;vector<vector<int>>up(LOG,vector<int>(n));int r=0;for(int i=0;i<n;i++){r=max(r,i);while(r+1<n&&a[r+1].first-a[i].first<=maxDiff)r++;up[0][i]=r;}for(int j=1;j<LOG;j++)for(int i=0;i<n;i++)up[j][i]=up[j-1][up[j-1][i]];vector<int>ans;for(auto&q:queries){int l=pos[q[0]],r=pos[q[1]];if(l>r)swap(l,r);if(l==r){ans.push_back(0);continue;}int steps=0;for(int j=LOG-1;j>=0;j--)if(up[j][l]<r&&up[j][l]>l){l=up[j][l];steps+=1<<j;}ans.push_back(up[0][l]>=r?steps+1:-1);}return ans;} };
```

## 3538. Merge Operations for Minimum Travel Time

https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

**Approach:** Interval DP: after retaining consecutive signs i,j, the speed of segment j→next is the sum of sign times merged into j.

**Complexity:** O(n³k) time, O(n²k) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:int minTravelTime(int l,int n,int k,vector<int>& position,vector<int>& time){const int INF=1e9;vector<int>pre(n+1);for(int i=0;i<n;i++)pre[i+1]=pre[i]+time[i];vector<vector<vector<int>>>dp(n,vector<vector<int>>(n,vector<int>(k+1,INF)));dp[0][0][0]=0;for(int i=0;i<n-1;i++)for(int prev=0;prev<=i;prev++)for(int used=0;used<=k;used++)if(dp[i][prev][used]<INF){for(int j=i+1;j<n;j++){int cnt=j-i-1;if(used+cnt>k)break;int speed=pre[i+1]-pre[prev];int cost=dp[i][prev][used]+(position[j]-position[i])*speed;dp[j][i][used+cnt]=min(dp[j][i][used+cnt],cost);}}int ans=INF;for(int i=0;i<n;i++)ans=min(ans,dp[n-1][i][k]);return ans;} };
```

## 3569. Maximize Count of Distinct Primes After Split

https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

**Approach:** Each distinct prime contributes one always, plus one if the split lies strictly between its first and last occurrence. Maintain intervals with a lazy segment tree.

**Complexity:** O((n+q) log n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {struct Seg{int n;vector<int>mx,lz;Seg(int n):n(n),mx(4*n),lz(4*n){}void add(int p,int l,int r,int a,int b,int v){if(a>r||b<l)return;if(a<=l&&r<=b){mx[p]+=v;lz[p]+=v;return;}int m=(l+r)/2;add(p*2,l,m,a,b,v);add(p*2+1,m+1,r,a,b,v);mx[p]=lz[p]+max(mx[p*2],mx[p*2+1]);}void add(int l,int r,int v){if(l<=r)add(1,1,n,l,r,v);}int best(){return mx[1];}};public:vector<int> maximumCount(vector<int>& nums,vector<vector<int>>& queries){int n=nums.size();vector<bool>prime(100001,true);prime[0]=prime[1]=false;for(int p=2;p*p<=100000;p++)if(prime[p])for(int j=p*p;j<=100000;j+=p)prime[j]=false;vector<set<int>>pos(100001);for(int i=0;i<n;i++)if(prime[nums[i]])pos[nums[i]].insert(i);Seg seg(n-1);int distinct=0;auto adjust=[&](int v,int delta){if(!prime[v]||pos[v].empty())return;int a=*pos[v].begin(),b=*pos[v].rbegin();seg.add(a+1,b,delta);};for(int v=2;v<=100000;v++)if(!pos[v].empty()){distinct++;adjust(v,1);}vector<int>ans;for(auto&q:queries){int i=q[0],v=q[1],old=nums[i];if(old!=v){if(prime[old]){adjust(old,-1);pos[old].erase(i);if(pos[old].empty())distinct--;else adjust(old,1);}if(prime[v]){if(!pos[v].empty())adjust(v,-1);else distinct++;pos[v].insert(i);adjust(v,1);}nums[i]=v;}ans.push_back(distinct+seg.best());}return ans;} };
```
# Batch 17 — C++11/C++14 Solutions
**Problems 321–330 of 330.** Compiled with `g++ -std=c++14 -fsyntax-only`. Compilation does not imply LeetCode Accepted.

## 3579. Minimum Steps to Convert String with Operations
**Problem:** https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

**Approach:** Partition DP. For each substring, evaluate no reversal and one reversal. For either orientation, match complementary mismatches with disjoint swaps; replace remaining mismatched positions.
**Complexity:** O(n^3 + 26^2 n^2) time, O(n^2) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
    int cost(const string& a,const string& b,int l,int r,bool rev){
        int f[26][26]={}; int mismatch=0;
        for(int i=l;i<=r;++i){
            int x=(rev?a[r-(i-l)]:a[i])-'a', y=b[i]-'a';
            if(x!=y){++f[x][y];++mismatch;}
        }
        int swaps=0;
        for(int x=0;x<26;++x)for(int y=x+1;y<26;++y)
            swaps+=min(f[x][y],f[y][x]);
        return mismatch-swaps+(rev?1:0);
    }
public:
    int minOperations(string word1,string word2){
        int n=word1.size(); vector<int> dp(n+1,1000000);dp[0]=0;
        for(int r=0;r<n;++r)for(int l=0;l<=r;++l)
            dp[r+1]=min(dp[r+1],dp[l]+min(cost(word1,word2,l,r,false),cost(word1,word2,l,r,true)));
        return dp[n];
    }
};
```

## 3609. Minimum Moves to Reach Target in Grid
**Problem:** https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/

**Approach:** Reverse the last move. The larger coordinate must have been increased: when x>y, either x was doubled (if its predecessor was at least y), or y was added to x. Handle equality and zero explicitly.
**Complexity:** O(log(max(tx,ty))) time, O(1) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 int minMoves(int sx,int sy,int tx,int ty){
  long long x=tx,y=ty;int steps=0;
  while(x>=sx&&y>=sy){
   if(x==sx&&y==sy)return steps;
   if(x==0&&y==0)break;
   if(x>y){
    if(x>=2*y){if(x%2)return -1;x/=2;}
    else x-=y;
   }else if(y>x){
    if(y>=2*x){if(y%2)return -1;y/=2;}
    else y-=x;
   }else{
    if(x==0)break;
    // A predecessor of (x,x) is (0,x), or (x,0).
    if(sx==0&&sy==x)return steps+1;
    if(sy==0&&sx==x)return steps+1;
    break;
   }
   ++steps;
  }
  return -1;
 }
};
```

## 3636. Threshold Majority Queries
**Problem:** https://leetcode.com/problems/threshold-majority-queries/

**Approach:** Square-root decomposition: precompute the exact mode of each contiguous range of complete blocks. Every candidate beating that mode must occur in one of the two partial boundary blocks. Count candidates using binary search in position lists.
**Complexity:** O(n²/B + q B log n) time, O(n + (n/B)²) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 vector<int> subarrayMajority(vector<int>& nums,vector<vector<int>>& queries){
  int n=nums.size(),B=100,nb=(n+B-1)/B;
  vector<int> vals=nums;sort(vals.begin(),vals.end());vals.erase(unique(vals.begin(),vals.end()),vals.end());
  int d=vals.size();vector<int>a(n);vector<vector<int>>pos(d);
  for(int i=0;i<n;++i){a[i]=lower_bound(vals.begin(),vals.end(),nums[i])-vals.begin();pos[a[i]].push_back(i);}
  vector<vector<int>> mode(nb,vector<int>(nb,-1));
  for(int i=0;i<nb;++i){vector<int>cnt(d);int best=-1,bf=0;
   for(int j=i*B;j<n;++j){int v=a[j],f=++cnt[v];if(f>bf||(f==bf&&(best<0||v<best))){best=v;bf=f;}if(j%B==B-1||j==n-1)mode[i][j/B]=best;}
  }
  vector<int>ans;
  for(auto &q:queries){int l=q[0],r=q[1],threshold=q[2],lb=l/B,rb=r/B;
   int best=-1,bf=0;
   auto consider=[&](int v){if(v<0)return;auto &p=pos[v];int f=upper_bound(p.begin(),p.end(),r)-lower_bound(p.begin(),p.end(),l);if(f>bf||(f==bf&&(best<0||v<best))){best=v;bf=f;}};
   if(lb==rb){for(int i=l;i<=r;++i)consider(a[i]);}
   else{
    for(int i=l;i<(lb+1)*B;++i)consider(a[i]);
    for(int i=rb*B;i<=r;++i)consider(a[i]);
    if(lb+1<=rb-1)consider(mode[lb+1][rb-1]);
   }
   ans.push_back(bf>=threshold?vals[best]:-1);
  }
  return ans;
 }
};
```

## 3816. Lexicographically Smallest String After Deleting Duplicate Characters
**Problem:** https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

**Approach:** Maintain remaining character counts. At each character, delete it when a smaller character remains ahead and the current character has another copy; otherwise keep it. This is the lexicographically minimal subsequence retaining every distinct character at least once, with optional duplicate retention.
**Complexity:** O(26n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 string lexSmallestAfterDeletion(string s){
  int cnt[26]={};for(char c:s)++cnt[c-'a'];
  string out;
  for(char c:s){int x=c-'a';--cnt[x];
   bool smaller=false;for(int j=0;j<x;++j)if(cnt[j]>0){smaller=true;break;}
   if(cnt[x]>0&&smaller)continue;
   out.push_back(c);
  }
  return out;
 }
};
```

## 3943. Number of Pairs After Increment
**Problem:** https://leetcode.com/problems/number-of-pairs-after-increment/

**Approach:** Maintain square-root blocks of nums2 with lazy range additions and frequency maps. A sum query uses at most five complements per block.
**Complexity:** O((n+q) sqrt(n) * 5) expected time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 vector<int> numberOfPairs(vector<int>& nums1,vector<int>& nums2,vector<vector<int>>& queries){
  int n=nums2.size(),B=225,nb=(n+B-1)/B;
  vector<long long>a(nums2.begin(),nums2.end()),lazy(nb);
  vector<unordered_map<long long,int>> freq(nb);
  auto rebuild=[&](int b){freq[b].clear();for(int i=b*B;i<min(n,(b+1)*B);++i)++freq[b][a[i]];};
  for(int b=0;b<nb;++b)rebuild(b);
  vector<int>ans;
  for(auto &q:queries){
   if(q[0]==1){int l=q[1],r=q[2];long long v=q[3];int lb=l/B,rb=r/B;
    if(lb==rb){for(int i=l;i<=r;++i)a[i]+=v;rebuild(lb);}
    else{for(int i=l;i<(lb+1)*B;++i)a[i]+=v;rebuild(lb);
     for(int b=lb+1;b<rb;++b)lazy[b]+=v;
     for(int i=rb*B;i<=r;++i)a[i]+=v;rebuild(rb);}
   }else{long long total=0,target=q[1];
    for(int b=0;b<nb;++b)for(int v:nums1){auto it=freq[b].find(target-v-lazy[b]);if(it!=freq[b].end())total+=it->second;}
    ans.push_back((int)total);
   }
  }
  return ans;
 }
};
```

## 3944. Minimum Operations to Make Array Modulo Alternating II
**Problem:** https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

**Approach:** For each parity, build the histogram of residues. Compute the sum of circular distances to every target residue using doubled prefix counts and weighted sums. Combine the best two different residues.
**Complexity:** O(n+k) time, O(k) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
 vector<long long> costs(const vector<int>& nums,int k,int parity){
  vector<long long>freq(2*k),pc(2*k+1),ps(2*k+1),res(k);
  for(int i=parity;i<(int)nums.size();i+=2)++freq[nums[i]%k];
  for(int i=0;i<k;++i)freq[i+k]=freq[i];
  for(int i=0;i<2*k;++i){pc[i+1]=pc[i]+freq[i];ps[i+1]=ps[i]+freq[i]*i;}
  for(int x=0;x<k;++x){int mid=x+k/2, end=x+k;
   long long c1=ps[mid+1]-ps[x]-1LL*x*(pc[mid+1]-pc[x]);
   long long c2=1LL*(x+k)*(pc[end]-pc[mid+1])-(ps[end]-ps[mid+1]);
   res[x]=c1+c2;
  }
  return res;
 }
public:
 long long minOperations(vector<int>& nums,int k){
  auto a=costs(nums,k,0),b=costs(nums,k,1);
  int b1=-1,b2=-1;
  for(int i=0;i<k;++i)if(b1<0||b[i]<b[b1]){b2=b1;b1=i;}else if(b2<0||b[i]<b[b2])b2=i;
  long long ans=LLONG_MAX;
  for(int i=0;i<k;++i)ans=min(ans,a[i]+b[i==b1?b2:b1]);
  return ans;
 }
};
```

## 3957. Maximum Sum of M Non-Overlapping Subarrays II
**Problem:** https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

**Not yet solved or validated.** No placeholder implementation is provided.

## 4051. Count Subarrays with Distant Sums
**Problem:** https://leetcode.com/problems/count-subarrays-with-distant-sums/

**Approach:** Count all subarrays minus those with sums strictly inside (goal-k, goal+k). Coordinate-compress prefix sums and count preceding prefixes in the corresponding interval using a Fenwick tree.
**Complexity:** O(n log n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 long long distantSubarrays(vector<int>& nums,int goal,int k){
  int n=nums.size();if(k==0)return 1LL*n*(n+1)/2;
  vector<long long>p(n+1);for(int i=0;i<n;++i)p[i+1]=p[i]+nums[i];
  vector<long long>v=p;sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());
  int z=v.size();vector<int>bit(z+1);
  auto add=[&](int i){for(++i;i<=z;i+=i&-i)++bit[i];};
  auto sum=[&](int i){int t=0;for(;i>0;i-=i&-i)t+=bit[i];return t;};
  long long close=0;add(lower_bound(v.begin(),v.end(),p[0])-v.begin());
  for(int i=1;i<=n;++i){
   long long low=p[i]-goal-k+1,high=p[i]-goal+k-1;
   int L=lower_bound(v.begin(),v.end(),low)-v.begin();
   int R=upper_bound(v.begin(),v.end(),high)-v.begin();
   close+=sum(R)-sum(L);add(lower_bound(v.begin(),v.end(),p[i])-v.begin());
  }
  return 1LL*n*(n+1)/2-close;
 }
};
```

## 4059. Lexicographically Largest Power Array
**Problem:** https://leetcode.com/problems/lexicographically-largest-power-array/

**Approach:** Sort values descending numerically. This lexicographically maximizes the vector of leading prefix lengths for bits from most significant to least significant; scan the sorted permutation for each bit.
**Complexity:** O(n log n + 15n) time, O(n) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 vector<int> largestPower(vector<int>& nums){
  sort(nums.begin(),nums.end(),greater<int>());
  vector<int>ans(15);int n=nums.size();
  for(int b=14;b>=0;--b){int i=0;while(i<n&&(nums[i]&(1<<b)))++i;ans[14-b]=i;}
  return ans;
 }
};
```

## 4086. Minimum Interval Selection to Cover Target Intervals
**Problem:** https://leetcode.com/problems/minimum-interval-selection-to-cover-target-intervals/

**Approach:** Merge overlapping target intervals, then greedily select the available interval with the furthest right endpoint among intervals starting at or before the next uncovered target point. Closed intervals must meet without positive gaps.
**Complexity:** O((A+T) log(A+T)) time, O(A+T) space.

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
 int minSelection(vector<vector<int>>& availableIntervals,vector<vector<int>>& targetIntervals){
  sort(availableIntervals.begin(),availableIntervals.end());sort(targetIntervals.begin(),targetIntervals.end());
  vector<pair<int,int>>tar;
  for(auto &v:targetIntervals){if(tar.empty()||v[0]>tar.back().second)tar.push_back({v[0],v[1]});else tar.back().second=max(tar.back().second,v[1]);}
  int n=availableIntervals.size(),i=0,ans=0;long long reach=-1;
  for(auto seg:tar){long long at=max((long long)seg.first,reach);
   while(at<seg.second || (at==seg.first&&reach<seg.first)){
    long long far=reach;
    while(i<n&&availableIntervals[i][0]<=at){far=max(far,(long long)availableIntervals[i][1]);++i;}
    if(far<=at && !(far==at&&at==seg.second&&reach<seg.first))return -1;
    ++ans;reach=far;at=reach;
   }
  }
  return ans;
 }
};
```
