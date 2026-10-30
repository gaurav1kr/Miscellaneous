# Heap / Priority Queue

**Problems:** 67

## Quick revision checklist

Repeatedly select the current min/max or maintain top-k candidates.

## Problem index

- [23. Merge k Sorted Lists](#23-merge-k-sorted-lists) — Hard; code: yes
- [215. Kth Largest Element in an Array](#215-kth-largest-element-in-an-array) — Medium; code: yes
- [347. Top K Frequent Elements](#347-top-k-frequent-elements) — Medium; code: yes
- [355. Design Twitter](#355-design-twitter) — Medium; code: yes
- [373. Find K Pairs with Smallest Sums](#373-find-k-pairs-with-smallest-sums) — Medium; code: yes
- [451. Sort Characters By Frequency](#451-sort-characters-by-frequency) — Medium; code: yes
- [506. Relative Ranks](#506-relative-ranks) — Easy; code: yes
- [759. Employee Free Time](#759-employee-free-time) — Hard; code: yes
- [855. Exam Room](#855-exam-room) — Medium; code: yes
- [912. Sort an Array](#912-sort-an-array) — Medium; code: yes
- [973. K Closest Points to Origin](#973-k-closest-points-to-origin) — Medium; code: yes
- [1046. Last Stone Weight](#1046-last-stone-weight) — Easy; code: yes
- [1057. Campus Bikes](#1057-campus-bikes) — Medium; code: yes
- [1086. High Five](#1086-high-five) — Easy; code: yes
- [1094. Car Pooling](#1094-car-pooling) — Medium; code: yes
- [1172. Dinner Plate Stacks](#1172-dinner-plate-stacks) — Hard; code: yes
- [1354. Construct Target Array With Multiple Sums](#1354-construct-target-array-with-multiple-sums) — Hard; code: yes
- [1424. Diagonal Traverse II](#1424-diagonal-traverse-ii) — Medium; code: yes
- [1464. Maximum Product of Two Elements in an Array](#1464-maximum-product-of-two-elements-in-an-array) — Easy; code: yes
- [1500. Design a File Sharing System](#1500-design-a-file-sharing-system) — Medium; code: yes
- [1606. Find Servers That Handled Most Number of Requests](#1606-find-servers-that-handled-most-number-of-requests) — Hard; code: yes
- [1738. Find Kth Largest XOR Coordinate Value](#1738-find-kth-largest-xor-coordinate-value) — Medium; code: yes
- [1801. Number of Orders in the Backlog](#1801-number-of-orders-in-the-backlog) — Medium; code: yes
- [1825. Finding MK Average](#1825-finding-mk-average) — Hard; code: yes
- [1834. Single-Threaded CPU](#1834-single-threaded-cpu) — Medium; code: yes
- [1845. Seat Reservation Manager](#1845-seat-reservation-manager) — Medium; code: yes
- [1878. Get Biggest Three Rhombus Sums in a Grid](#1878-get-biggest-three-rhombus-sums-in-a-grid) — Medium; code: yes
- [1882. Process Tasks Using Servers](#1882-process-tasks-using-servers) — Medium; code: yes
- [1912. Design Movie Rental System](#1912-design-movie-rental-system) — Hard; code: yes
- [1942. The Number of the Smallest Unoccupied Chair](#1942-the-number-of-the-smallest-unoccupied-chair) — Medium; code: yes
- [1985. Find the Kth Largest Integer in the Array](#1985-find-the-kth-largest-integer-in-the-array) — Medium; code: yes
- [2015. Average Height of Buildings in Each Segment](#2015-average-height-of-buildings-in-each-segment) — Medium; code: yes
- [2034. Stock Price Fluctuation ](#2034-stock-price-fluctuation) — Medium; code: yes
- [2099. Find Subsequence of Length K With the Largest Sum](#2099-find-subsequence-of-length-k-with-the-largest-sum) — Easy; code: yes
- [2102. Sequentially Ordinal Rank Tracker](#2102-sequentially-ordinal-rank-tracker) — Hard; code: yes
- [2231. Largest Number After Digit Swaps by Parity](#2231-largest-number-after-digit-swaps-by-parity) — Easy; code: yes
- [2254. Design Video Sharing Platform](#2254-design-video-sharing-platform) — Hard; code: yes
- [2336. Smallest Number in Infinite Set](#2336-smallest-number-in-infinite-set) — Medium; code: yes
- [2342. Max Sum of a Pair With Equal Sum of Digits](#2342-max-sum-of-a-pair-with-equal-sum-of-digits) — Medium; code: yes
- [2343. Query Kth Smallest Trimmed Number](#2343-query-kth-smallest-trimmed-number) — Medium; code: yes
- [2344. Minimum Deletions to Make Array Divisible](#2344-minimum-deletions-to-make-array-divisible) — Hard; code: yes
- [2349. Design a Number Container System](#2349-design-a-number-container-system) — Medium; code: yes
- [2353. Design a Food Rating System](#2353-design-a-food-rating-system) — Medium; code: yes
- [2386. Find the K-Sum of an Array](#2386-find-the-k-sum-of-an-array) — Hard; code: yes
- [2402. Meeting Rooms III](#2402-meeting-rooms-iii) — Hard; code: yes
- [2456. Most Popular Video Creator](#2456-most-popular-video-creator) — Medium; code: yes
- [2500. Delete Greatest Value in Each Row](#2500-delete-greatest-value-in-each-row) — Easy; code: yes
- [2512. Reward Top K Students](#2512-reward-top-k-students) — Medium; code: yes
- [2532. Time to Cross a Bridge](#2532-time-to-cross-a-bridge) — Hard; code: yes
- [2558. Take Gifts From the Richest Pile](#2558-take-gifts-from-the-richest-pile) — Easy; code: yes
- [2593. Find Score of an Array After Marking All Elements](#2593-find-score-of-an-array-after-marking-all-elements) — Medium; code: yes
- [2679. Sum in a Matrix](#2679-sum-in-a-matrix) — Medium; code: yes
- [2974. Minimum Number Game](#2974-minimum-number-game) — Easy; code: yes
- [3066. Minimum Operations to Exceed Threshold Value II](#3066-minimum-operations-to-exceed-threshold-value-ii) — Medium; code: yes
- [3080. Mark Elements on Array by Performing Queries](#3080-mark-elements-on-array-by-performing-queries) — Medium; code: yes
- [3092. Most Frequent IDs](#3092-most-frequent-ids) — Medium; code: yes
- [3264. Final Array State After K Multiplication Operations I](#3264-final-array-state-after-k-multiplication-operations-i) — Easy; code: yes
- [3266. Final Array State After K Multiplication Operations II](#3266-final-array-state-after-k-multiplication-operations-ii) — Hard; code: yes
- [3275. K-th Nearest Obstacle Queries](#3275-k-th-nearest-obstacle-queries) — Medium; code: yes
- [3391. Design a 3D Binary Matrix with Efficient Layer Tracking](#3391-design-a-3d-binary-matrix-with-efficient-layer-tracking) — Medium; code: yes
- [3408. Design Task Manager](#3408-design-task-manager) — Medium; code: yes
- [3478. Choose K Elements With Maximum Sum](#3478-choose-k-elements-with-maximum-sum) — Medium; code: yes
- [3507. Minimum Pair Removal to Sort Array I](#3507-minimum-pair-removal-to-sort-array-i) — Easy; code: yes
- [3510. Minimum Pair Removal to Sort Array II](#3510-minimum-pair-removal-to-sort-array-ii) — Hard; code: yes
- [3815. Design Auction System](#3815-design-auction-system) — Medium; code: yes
- [3885. Design Event Manager](#3885-design-event-manager) — Medium; code: yes
- [4065. Rearrange Array by Removing Distinct Values](#4065-rearrange-array-by-removing-distinct-values) — Easy; code: yes

---

## 23. Merge k Sorted Lists

**Problem:** https://leetcode.com/problems/merge-k-sorted-lists/

**Difficulty:** Hard | **Premium:** No

**Tags:** Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort, Tournament Sort

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Linked List / Pointers

**Data structures (inferred):** Linked list, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(N log k)

**Space complexity:** O(k)

**Complexity reasoning:** N total nodes are each pushed and popped once from a min-heap containing at most k list heads.

### Problem description

You are given an array of k linked-lists lists , each linked-list is sorted in ascending order. 
 
 Merge all the linked-lists into one sorted linked-list and return it. 

 Example 1: 
 
```
Input:
 lists = [[1,4,5],[1,3,4],[2,6]]

Output:
 [1,1,2,3,4,4,5,6]

Explanation:
 The linked-lists are:
[
 1->4->5,
 1->3->4,
 2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
```

 Example 2: 
 
```
Input:
 lists = []

Output:
 []
```

 Example 3: 
 
```
Input:
 lists = [[]]

Output:
 []
```

 Constraints: 

 k == lists.length 
 
 0 <= k <= 10 4 
 
 0 <= lists[i].length <= 500 
 
 -10 4 <= lists[i][j] <= 10 4 
 
 lists[i] is sorted in ascending order . 
 
 The sum of lists[i].length will not exceed 10 4 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
   struct Compare {
    bool operator()(ListNode* a, ListNode* b) {
        return a->val > b->val;
    }
};

ListNode* mergeKLists(vector<ListNode*>& lists) {
    priority_queue<ListNode*, vector<ListNode*>, Compare> pq;
    
    for (auto list : lists)
        if (list) pq.push(list);
    
    ListNode dummy(0), *tail = &dummy;
    
    while (!pq.empty()) {
        tail->next = pq.top();
        pq.pop();
        tail = tail->next;
        if (tail->next) pq.push(tail->next);
    }
    
    return dummy.next;
}
};
```


## 215. Kth Largest Element in an Array

**Problem:** https://leetcode.com/problems/kth-largest-element-in-an-array/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log k)

**Space complexity:** O(k)

**Complexity reasoning:** Each of n elements is pushed to a heap of at most k+1 entries, then excess elements are removed.

### Problem description

Given an integer array nums and an integer k , return the k th largest element in the array . 
 
 Note that it is the k th largest element in the sorted order, not the k th distinct element. 
 
 Can you solve it without sorting? 

 Example 1: 
 
```
Input:
 nums = [3,2,1,5,6,4], k = 2

Output:
 5
```
 
 Example 2: 
 
```
Input:
 nums = [3,2,3,1,2,4,5,5,6], k = 4

Output:
 4
```

 Constraints: 

 1 <= k <= nums.length <= 10 5 
 
 -10 4 <= nums[i] <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        return minHeap.top();
    }
};
```


## 347. Top K Frequent Elements

**Problem:** https://leetcode.com/problems/top-k-frequent-elements/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + u log k)

**Space complexity:** O(u + k)

**Complexity reasoning:** Hash frequencies of n values in expected O(n), then maintain a size-k heap for u distinct values; output holds k items.

### Problem description

Given an integer array nums and an integer k , return the k most frequent elements . You may return the answer in any order . 

 Example 1: 

 Input: nums = [1,1,1,2,2,3], k = 2 
 
 Output: [1,2] 

 Example 2: 

 Input: nums = [1], k = 1 
 
 Output: [1] 

 Example 3: 

 Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2 
 
 Output: [1,2] 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 -10 4 <= nums[i] <= 10 4 
 
 k is in the range [1, the number of unique elements in the array] . 
 
 It is guaranteed that the answer is unique . 

 Follow up: Your algorithm's time complexity must be better than O(n log n) , where n is the array's size.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Step 1: Count the frequency of each element using a hash map
        unordered_map<int, int> freqMap;
        for (int num : nums) {
            freqMap[num]++;
        }
        
        // Step 2: Use a min-heap to store the top K elements
        auto compare = [](pair<int, int>& a, pair<int, int>& b) {
            return a.second > b.second; // Min-heap based on frequency
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(compare)> minHeap(compare);
        
        for (auto& [num, freq] : freqMap) {
            minHeap.push({num, freq});
            if (minHeap.size() > k) {
                minHeap.pop(); // Keep only the top K elements
            }
        }
        
        // Step 3: Extract the elements from the heap
        vector<int> result;
        while (!minHeap.empty()) {
            result.push_back(minHeap.top().first);
            minHeap.pop();
        }
        
        return result;
    }
};
```


## 355. Design Twitter

**Problem:** https://leetcode.com/problems/design-twitter/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, Linked List, Design, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Linked List / Pointers, Stack / Queue

**Data structures (inferred):** Hash map, Hash map / hash set, Hash set, Linked list, Ordered map, Ordered set, Priority queue / heap, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** post O(1) amortized; feed O(T); follow/unfollow O(1) expected

**Space complexity:** O(T + F)

**Complexity reasoning:** The implementation scans up to T historical tweets backwards for each feed; hash-set follow operations are expected constant time. T is total tweets, F stored follow links.

### Problem description

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed. 
 
 Implement the Twitter class: 

 Twitter() Initializes your twitter object. 
 
 void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId . Each call to this function will be made with a unique tweetId . 
 
 List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent . 
 
 void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId . 
 
 void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId . 

 Example 1: 
 
```
Input

["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

Output

[null, null, [5], null, null, [6, 5], null, [5]]

Explanation

Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1); // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2); // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1); // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2); // User 1 unfollows user 2.
twitter.getNewsFeed(1); // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
```

 Constraints: 

 1 <= userId, followerId, followeeId <= 500 
 
 0 <= tweetId <= 10 4 
 
 All the tweets have unique IDs. 
 
 At most 3 * 10 4 calls will be made to postTweet , getNewsFeed , follow , and unfollow . 
 
 A user cannot follow himself.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include<vector>
#include<unordered_map>
#include<unordered_set>
using namespace std ;
class Twitter 
{
public:
    Twitter() 
    {
 
    }
 
    void postTweet(int userId, int tweetId) 
    {
        feed.push_back({ userId, tweetId });
    }
 
    vector<int> getNewsFeed(int userId) 
    {
        vector<int> ret;
        for (int i = feed.size() - 1; i >= 0; --i) 
        {
            auto& [user, tweet] = feed[i];
            if (userId == user || (following[userId].contains(user))) 
            {
                ret.push_back(tweet);
                if (ret.size() == 10) break;
            }
        }
        return ret;
    }
 
    void follow(int followerId, int followeeId) {
        following[followerId].insert(followeeId);
    }
 
    void unfollow(int followerId, int followeeId) {
        following[followerId].erase(followeeId);
    }
 
    std::unordered_map<int, std::unordered_set<int>> following;
    std::vector<std::pair<int, int>> feed;
};
 
/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
```


## 373. Find K Pairs with Smallest Sums

**Problem:** https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(nm log(k+1) + k log(k+1)) worst case

**Space complexity:** O(k)

**Complexity reasoning:** Nested loops examine at most n*m pairs and each qualifying candidate updates a size-k max-heap; sorted nums2 permits early breaks. Final extraction costs O(k log k).

### Problem description

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k . 
 
 Define a pair (u, v) which consists of one element from the first array and one element from the second array. 
 
 Return the k pairs (u 1 , v 1 ), (u 2 , v 2 ), ..., (u k , v k ) with the smallest sums . 

 Example 1: 
 
```
Input:
 nums1 = [1,7,11], nums2 = [2,4,6], k = 3

Output:
 [[1,2],[1,4],[1,6]]

Explanation:
 The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

 Example 2: 
 
```
Input:
 nums1 = [1,1,2], nums2 = [1,2,3], k = 2

Output:
 [[1,1],[1,1]]

Explanation:
 The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```

 Constraints: 

 1 <= nums1.length, nums2.length <= 10 5 
 
 -10 9 <= nums1[i], nums2[i] <= 10 9 
 
 nums1 and nums2 both are sorted in non-decreasing order . 
 
 1 <= k <= 10 4 
 
 k <= nums1.length * nums2.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) 
	{
		vector<vector<int>> res;
		priority_queue<pair<int,pair<int,int>>> pq;
		
		for(auto x:nums1)
		{
			for(auto y:nums2)
			{
				int sum=x+y;
				if( pq.size()<k)
				{
					 pq.push({sum,{x,y}});
				}
				else if(sum < pq.top().first)
				{
					pq.pop();
					pq.push({sum,{x,y}});
				}
				else
					break;
			}
		}
		
		while(!pq.empty() )
		{
		   auto p=pq.top().second;
		   pq.pop();
			
		   res.push_back({p.first,p.second});
		}
		return res;
	}
};
//T.C= O(n * m * log(k)).
//S.C= O(k).
```


## 451. Sort Characters By Frequency

**Problem:** https://leetcode.com/problems/sort-characters-by-frequency/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, String Algorithms, Sorting / Divide and Conquer

**Data structures (inferred):** Hash map / hash set, Priority queue / heap, Sorted array, String, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + A)

**Space complexity:** O(n + A)

**Complexity reasoning:** Count n characters, create n+1 frequency buckets, and traverse them; A=256 possible byte values. Output and bucket array use linear space.

### Problem description

Given a string s , sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string. 
 
 Return the sorted string . If there are multiple answers, return any of them . 

 Example 1: 
 
```
Input:
 s = "tree"

Output:
 "eert"

Explanation:
 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

 Example 2: 
 
```
Input:
 s = "cccaaa"

Output:
 "aaaccc"

Explanation:
 Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
```

 Example 3: 
 
```
Input:
 s = "Aabb"

Output:
 "bbAa"

Explanation:
 "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

 Constraints: 

 1 <= s.length <= 5 * 10 5 
 
 s consists of uppercase and lowercase English letters and digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
  string frequencySort(string str) {
    // Store the frequency each character appears
    vector<int> freqs(256);
    for (const char& ch : str)
      ++freqs[ch];

    // Use a "bucket" container to store which characters have a freqs[i] frequency
    vector<vector<char>> bucket(str.length() + 1);
    for (int i = 255; i >= 0; --i)
      if (freqs[i]) 
        bucket[freqs[i]].push_back(static_cast<char>(i));

    // Loop through all the possible frequencies a character could have
    // Append them to our sorted string 'freq' times
    string sorted;
    for (int freq = str.length(); freq >= 0; --freq) 
      for (const char& ch : bucket[freq])
        sorted += string(freq, ch);

    return sorted;
  }
};
```


## 506. Relative Ranks

**Problem:** https://leetcode.com/problems/relative-ranks/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Build n (score,index) pairs, sort them, and produce n rank strings.

### Problem description

You are given an integer array score of size n , where score[i] is the score of the i th athlete in a competition. All the scores are guaranteed to be unique . 
 
 The athletes are placed based on their scores, where the 1 st place athlete has the highest score, the 2 nd place athlete has the 2 nd highest score, and so on. The placement of each athlete determines their rank: 

 The 1 st place athlete's rank is "Gold Medal" . 
 
 The 2 nd place athlete's rank is "Silver Medal" . 
 
 The 3 rd place athlete's rank is "Bronze Medal" . 
 
 For the 4 th place to the n th place athlete, their rank is their placement number (i.e., the x th place athlete's rank is "x" ). 

 Return an array answer of size n where answer[i] is the rank of the i th athlete. 

 Example 1: 
 
```
Input:
 score = [5,4,3,2,1]

Output:
 ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Explanation:
 The placements are [1
st
, 2
nd
, 3
rd
, 4
th
, 5
th
].
```

 Example 2: 
 
```
Input:
 score = [10,3,8,9,4]

Output:
 ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

Explanation:
 The placements are [1
st
, 5
th
, 3
rd
, 2
nd
, 4
th
].
```

 Constraints: 

 n == score.length 
 
 1 <= n <= 10 4 
 
 0 <= score[i] <= 10 6 
 
 All the values in score are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<pair<int, int>> scores;
        for (int i = 0; i < score.size(); ++i)
            scores.emplace_back(score[i], i);
        sort(scores.rbegin(), scores.rend());

        vector<string> res(score.size());
        for (int i = 0; i < scores.size(); ++i) {
            if (i == 0) res[scores[i].second] = "Gold Medal";
            else if (i == 1) res[scores[i].second] = "Silver Medal";
            else if (i == 2) res[scores[i].second] = "Bronze Medal";
            else res[scores[i].second] = to_string(i + 1);
        }
        return res;
    }
};
```


## 759. Employee Free Time

**Problem:** https://leetcode.com/problems/employee-free-time/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Sweep Line, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(N log N)

**Space complexity:** O(N)

**Complexity reasoning:** Flatten N total intervals, sort by start, then scan to emit gaps.

### Problem description

We are given a list schedule of employees, which represents the working time for each employee. 
 
 Each employee has a list of non-overlapping Intervals , and these intervals are in sorted order. 
 
 Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order. 
 
 (Even though we are representing Intervals in the form [x, y] , the objects inside are Intervals , not lists or arrays. For example, schedule[0][0].start = 1 , schedule[0][0].end = 2 , and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length. 

 Example 1: 
 
```
Input:
 schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]

Output:
 [[3,4]]

Explanation:
 There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
```

 Example 2: 
 
```
Input:
 schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]

Output:
 [[5,6],[7,9]]
```

 Constraints: 

 1 <= schedule.length , schedule[i].length <= 50 
 
 0 <= schedule[i].start < schedule[i].end <= 10^8

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<Interval> employeeFreeTime(vector<vector<Interval>>& schedule) {
        vector<Interval> all;
        for (const auto& employee : schedule) {
            all.insert(all.end(), employee.begin(), employee.end());
        }
        sort(all.begin(), all.end(), [](const Interval& a, const Interval& b) {
            return a.start < b.start;
        });
        vector<Interval> answer;
        if (all.empty()) {
            return answer;
        }
        int end = all[0].end;
        for (int i = 1; i < static_cast<int>(all.size()); ++i) {
            if (all[i].start > end) {
                answer.push_back(Interval(end, all[i].start));
            }
            end = max(end, all[i].end);
        }
        return answer;
    }
};
```


## 855. Exam Room

**Problem:** https://leetcode.com/problems/exam-room/

**Difficulty:** Medium | **Premium:** No

**Tags:** Design, Heap (Priority Queue), Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Stack / Queue

**Data structures (inferred):** Ordered set, Priority queue / heap

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** seat O(s + log s); leave O(log s)

**Space complexity:** O(s)

**Complexity reasoning:** seat() scans s occupied seats and inserts one into std::set; leave() erases by key. The ordered set stores s seats.

### Problem description

There is an exam room with n seats in a single row labeled from 0 to n - 1 . 
 
 When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number 0 . 
 
 Design a class that simulates the mentioned exam room. 
 
 Implement the ExamRoom class: 

 ExamRoom(int n) Initializes the object of the exam room with the number of the seats n . 
 
 int seat() Returns the label of the seat at which the next student will set. 
 
 void leave(int p) Indicates that the student sitting at seat p will leave the room. It is guaranteed that there will be a student sitting at seat p . 

 Example 1: 
 
```
Input

["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
[[10], [], [], [], [], [4], []]

Output

[null, 0, 9, 4, 2, null, 5]

Explanation

ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
examRoom.seat(); // return 9, the student sits at the last seat number 9.
examRoom.seat(); // return 4, the student sits at the last seat number 4.
examRoom.seat(); // return 2, the student sits at the last seat number 2.
examRoom.leave(4);
examRoom.seat(); // return 5, the student sits at the last seat number 5.
```

 Constraints: 

 1 <= n <= 10 9 
 
 It is guaranteed that there is a student sitting at seat p . 
 
 At most 10 4 calls will be made to seat and leave .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <set>

using namespace std;

class ExamRoom {
    int N;
    set<int> seats;

public:
    ExamRoom(int n) : N(n) {}

    int seat() {
        if (seats.empty()) {
            seats.insert(0);
            return 0;
        }

        int prev = -1, maxDist = 0, seatToTake = 0;
        for (int seat : seats) {
            if (prev == -1) {
                if (seat > 0) {
                    maxDist = seat;
                    seatToTake = 0;
                }
            } else {
                int dist = (seat - prev) / 2;
                if (dist > maxDist) {
                    maxDist = dist;
                    seatToTake = prev + dist;
                }
            }
            prev = seat;
        }

        if (N - 1 - *seats.rbegin() > maxDist) {
            seatToTake = N - 1;
        }

        seats.insert(seatToTake);
        return seatToTake;
    }

    void leave(int p) {
        seats.erase(p);
    }
};
```


## 912. Sort an Array

**Problem:** https://leetcode.com/problems/sort-an-array/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n) including input copy; O(log n) stack beyond copy

**Complexity reasoning:** Bottom-up heap construction costs O(n), followed by n extractions with O(log n) recursive heapify; vector is passed by value.

### Problem description

Given an array of integers nums , sort the array in ascending order and return it. 
 
 You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible. 

 Example 1: 
 
```
Input:
 nums = [5,2,3,1]

Output:
 [1,2,3,5]

Explanation:
 After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
```

 Example 2: 
 
```
Input:
 nums = [5,1,1,2,0,0]

Output:
 [0,0,1,1,2,5]

Explanation:
 Note that the values of nums are not necessarily unique.
```

 Constraints: 

 1 <= nums.length <= 5 * 10 4 
 
 -5 * 10 4 <= nums[i] <= 5 * 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
public:
    void heapify(vector<int> & arr, int N, int i)
    {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        if (l < N && arr[l] > arr[largest])
            largest = l;

        if (r < N && arr[r] > arr[largest])
            largest = r;

      
        if (largest != i) 
        {
            swap(arr[i], arr[largest]);
            heapify(arr, N, largest);
        }
    }

    vector<int> sortArray(vector<int> arr)
    {
        int N = arr.size();
        for (int i = N / 2 - 1; i >= 0; i--)
            heapify(arr, N, i);

        for (int i = N - 1; i > 0; i--) 
        {
            swap(arr[0], arr[i]);
            heapify(arr, i, 0);
        }
        return arr;
    }

};
```


## 973. K Closest Points to Origin

**Problem:** https://leetcode.com/problems/k-closest-points-to-origin/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect, K-D Tree

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Math / Number Theory, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log k)

**Space complexity:** O(k)

**Complexity reasoning:** Insert each point into a max-heap capped at k and extract k closest points.

### Problem description

Given an array of points where points[i] = [x i , y i ] represents a point on the X-Y plane and an integer k , return the k closest points to the origin (0, 0) . 
 
 The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x 1 - x 2 ) 2 + (y 1 - y 2 ) 2 ). 
 
 You may return the answer in any order . The answer is guaranteed to be unique (except for the order that it is in). 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg] 
 
```
Input:
 points = [[1,3],[-2,2]], k = 1

Output:
 [[-2,2]]

Explanation:

The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

 Example 2: 
 
```
Input:
 points = [[3,3],[5,-1],[-2,4]], k = 2

Output:
 [[3,3],[-2,4]]

Explanation:
 The answer [[-2,4],[3,3]] would also be accepted.
```

 Constraints: 

 1 <= k <= points.length <= 10 4 
 
 -10 4 <= x i , y i <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // Max-heap to store the k closest points
        priority_queue<pair<int, vector<int>>> maxHeap;

        for (const auto& point : points) {
            int x = point[0], y = point[1];
            int dist = x * x + y * y; // Compute squared distance to avoid floating-point operations
            maxHeap.push({dist, point});

            // Maintain size of the heap to at most k
            if (maxHeap.size() > k) {
                maxHeap.pop();
            }
        }

        vector<vector<int>> result;
        while (!maxHeap.empty()) {
            result.push_back(maxHeap.top().second);
            maxHeap.pop();
        }
        return result;
    }
};
```


## 1046. Last Stone Weight

**Problem:** https://leetcode.com/problems/last-stone-weight/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Heapify n stones, then repeatedly remove the two largest and possibly insert their difference; at most n rounds.

### Problem description

You are given an array of integers stones where stones[i] is the weight of the i th stone. 
 
 We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y . The result of this smash is: 

 If x == y , both stones are destroyed, and 
 
 If x != y , the stone of weight x is destroyed, and the stone of weight y has new weight y - x . 

 At the end of the game, there is at most one stone left. 
 
 Return the weight of the last remaining stone . If there are no stones left, return 0 . 

 Example 1: 
 
```
Input:
 stones = [2,7,4,1,8,1]

Output:
 1

Explanation:
 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
```

 Example 2: 
 
```
Input:
 stones = [1]

Output:
 1
```

 Constraints: 

 1 <= stones.length <= 30 
 
 1 <= stones[i] <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap(stones.begin(), stones.end());
        while (maxHeap.size() > 1) {
            int stone1 = maxHeap.top(); maxHeap.pop();
            int stone2 = maxHeap.top(); maxHeap.pop();
            if (stone1 != stone2) {
                maxHeap.push(stone1 - stone2);
            }
        }
        return maxHeap.empty() ? 0 : maxHeap.top();
    }
};
```


## 1057. Campus Bikes

**Problem:** https://leetcode.com/problems/campus-bikes/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(nm log(nm))

**Space complexity:** O(nm)

**Complexity reasoning:** Generate every worker-bike distance (n*m), sort all tuples, and greedily assign pairs.

### Problem description

On a campus represented on the X-Y plane, there are n workers and m bikes, with n <= m . 
 
 You are given an array workers of length n where workers[i] = [x i , y i ] is the position of the i th worker. You are also given an array bikes of length m where bikes[j] = [x j , y j ] is the position of the j th bike. All the given positions are unique . 
 
 Assign a bike to each worker. Among the available bikes and workers, we choose the (worker i , bike j ) pair with the shortest Manhattan distance between each other and assign the bike to that worker. 
 
 If there are multiple (worker i , bike j ) pairs with the same shortest Manhattan distance , we choose the pair with the smallest worker index . If there are multiple ways to do that, we choose the pair with the smallest bike index . Repeat this process until there are no available workers. 
 
 Return an array answer of length n , where answer[i] is the index ( 0-indexed ) of the bike that the i th worker is assigned to . 
 
 The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y| . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2019/03/06/1261_example_1_v2.png] 
 
```
Input:
 workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]

Output:
 [1,0]

Explanation:
 Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2019/03/06/1261_example_2_v2.png] 
 
```
Input:
 workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]

Output:
 [0,2,1]

Explanation:
 Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].
```

 Constraints: 

 n == workers.length 
 
 m == bikes.length 
 
 1 <= n <= m <= 1000 
 
 workers[i].length == bikes[j].length == 2 
 
 0 <= x i , y i < 1000 
 
 0 <= x j , y j < 1000 
 
 All worker and bike locations are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> assignBikes(vector<vector<int>>& workers,
                            vector<vector<int>>& bikes) {
        vector<tuple<int, int, int>> pairs;
        for (int w = 0; w < static_cast<int>(workers.size()); ++w) {
            for (int b = 0; b < static_cast<int>(bikes.size()); ++b) {
                int distance = abs(workers[w][0] - bikes[b][0])
                             + abs(workers[w][1] - bikes[b][1]);
                pairs.emplace_back(distance, w, b);
            }
        }
        sort(pairs.begin(), pairs.end());
        vector<int> answer(workers.size(), -1);
        vector<bool> used(bikes.size(), false);
        int assigned = 0;
        for (const auto& item : pairs) {
            int w = get<1>(item);
            int b = get<2>(item);
            if (answer[w] == -1 && !used[b]) {
                answer[w] = b;
                used[b] = true;
                if (++assigned == static_cast<int>(workers.size())) {
                    break;
                }
            }
        }
        return answer;
    }
};
```


## 1086. High Five

**Problem:** https://leetcode.com/problems/high-five/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Hash Table, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Ordered map, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n) worst case

**Space complexity:** O(n)

**Complexity reasoning:** Group n scores by ordered student ID, then sort each student’s scores; total sorting is bounded by O(n log n).

### Problem description

Given a list of the scores of different students, items , where items[i] = [ID i , score i ] represents one score from a student with ID i , calculate each student's top five average . 
 
 Return the answer as an array of pairs result , where result[j] = [ID j , topFiveAverage j ] represents the student with ID j and their top five average . Sort result by ID j in increasing order . 
 
 A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division . 

 Example 1: 
 
```
Input:
 items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

Output:
 [[1,87],[2,88]]

Explanation: 

The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
```

 Example 2: 
 
```
Input:
 items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]

Output:
 [[1,100],[7,100]]
```

 Constraints: 

 1 <= items.length <= 1000 
 
 items[i].length == 2 
 
 1 <= ID i <= 1000 
 
 0 <= score i <= 100 
 
 For each ID i , there will be at least five scores.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        map<int, vector<int>> scores;
        for (const auto& item : items) {
            scores[item[0]].push_back(item[1]);
        }
        vector<vector<int>> result;
        for (auto& entry : scores) {
            auto& values = entry.second;
            sort(values.rbegin(), values.rend());
            int sum = accumulate(values.begin(), values.begin() + 5, 0);
            result.push_back({entry.first, sum / 5});
        }
        return result;
    }
};
```


## 1094. Car Pooling

**Problem:** https://leetcode.com/problems/car-pooling/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Heap (Priority Queue), Simulation, Prefix Sum

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Prefix Sum / Difference Array, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Prefix-sum array, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + R)

**Space complexity:** O(R)

**Complexity reasoning:** Update a fixed difference array for n trips and scan R=1001 possible stops; storage is the fixed stop array.

### Problem description

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west). 
 
 You are given the integer capacity and an array trips where trips[i] = [numPassengers i , from i , to i ] indicates that the i th trip has numPassengers i passengers and the locations to pick them up and drop them off are from i and to i respectively. The locations are given as the number of kilometers due east from the car's initial location. 
 
 Passengers are dropped off before new passengers are picked up at the same location. At every point along the route, the total number of passengers in the car must not exceed capacity . 
 
 Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise. 

 Example 1: 
 
```
Input:
 trips = [[2,1,5],[3,3,7]], capacity = 4

Output:
 false

Explanation:

At kilometer 1, 2 passengers are picked up, so the car holds 2.
At kilometer 3, 3 more are picked up, so the car holds 5.
Since 5 > capacity = 4, the trips cannot all be completed.
```

 Example 2: 
 
```
Input:
 trips = [[2,1,5],[3,3,7]], capacity = 5

Output:
 true

Explanation:

At kilometer 1, the car holds 2 passengers.
At kilometer 3, the car holds 5 passengers.
At kilometer 5, the first 2 are dropped off, so the car holds 3.
At kilometer 7, the last 3 are dropped off, so the car holds 0.
The maximum occupancy is 5, which never exceeds capacity = 5.
```

 Constraints: 

 1 <= trips.length <= 1000 
 
 trips[i].length == 3 
 
 1 <= numPassengers i <= 100 
 
 0 <= from i < to i <= 1000 
 
 1 <= capacity <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) 
    {
        int stops[1001] = {};
        for (auto t : trips) stops[t[1]] += t[0], stops[t[2]] -= t[0];
        for (auto i = 0; capacity >= 0 && i < 1001; ++i) capacity -= stops[i];
        return capacity >= 0;
    }
};
```


## 1172. Dinner Plate Stacks

**Problem:** https://leetcode.com/problems/dinner-plate-stacks/

**Difficulty:** Hard | **Premium:** No

**Tags:** Hash Table, Stack, Design, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Stack / Queue

**Data structures (inferred):** Hash map / hash set, Ordered set, Priority queue / heap, Stack, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** join O(c log(U+C)); leave O(c log(U+C)); request O(o log(U+C))

**Space complexity:** O(U+C)

**Complexity reasoning:** Balanced owner/chunk sets and recycled-ID heap maintain U users and C ownership links; c is the user’s chunks and o the owners returned. Request copies o IDs and may insert an ownership link.

### Problem description

You have an infinite number of stacks arranged in a row and numbered (left to right) from 0 , each of the stacks has the same maximum capacity. 
 
 Implement the DinnerPlates class: 

 DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity . 
 
 void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity . 
 
 int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all the stacks are empty. 
 
 int popAtStack(int index) Returns the value at the top of the stack with the given index index and removes it from that stack or returns -1 if the stack with that given index is empty. 

 Example 1: 
 
```
Input

["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
[[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]

Output

[null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]

Explanation:
 
DinnerPlates D = DinnerPlates(2); // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5); // The stacks are now: 2 4
 1 3 5
 ﹈ ﹈ ﹈
D.popAtStack(0); // Returns 2. The stacks are now: 4
 1 3 5
 ﹈ ﹈ ﹈
D.push(20); // The stacks are now: 20 4
 1 3 5
 ﹈ ﹈ ﹈
D.push(21); // The stacks are now: 20 4 21
 1 3 5
 ﹈ ﹈ ﹈
D.popAtStack(0); // Returns 20. The stacks are now: 4 21
 1 3 5
 ﹈ ﹈ ﹈
D.popAtStack(2); // Returns 21. The stacks are now: 4
 1 3 5
 ﹈ ﹈ ﹈ 
D.pop() // Returns 5. The stacks are now: 4
 1 3 
 ﹈ ﹈ 
D.pop() // Returns 4. The stacks are now: 1 3 
 ﹈ ﹈ 
D.pop() // Returns 3. The stacks are now: 1 
 ﹈ 
D.pop() // Returns 1. There are no stacks.
D.pop() // Returns -1. There are still no stacks.
```

 Constraints: 

 1 <= capacity <= 2 * 10 4 
 
 1 <= val <= 2 * 10 4 
 
 0 <= index <= 10 5 
 
 At most 2 * 10 5 calls will be made to push , pop , and popAtStack .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <stack>
#include <set>

using namespace std;

class DinnerPlates {
    int cap;
    vector<stack<int>> stacks;
    set<int> available;

public:
    DinnerPlates(int capacity) : cap(capacity) {}

    void push(int val) {
        if (available.empty()) stacks.emplace_back();
        int idx = available.empty() ? stacks.size() - 1 : *available.begin();
        if (idx == stacks.size()) stacks.emplace_back();
        stacks[idx].push(val);
        if (stacks[idx].size() == cap) available.erase(idx);
        else available.insert(idx);
    }

    int pop() {
        while (!stacks.empty() && stacks.back().empty()) stacks.pop_back();
        if (stacks.empty()) return -1;
        int val = stacks.back().top(); stacks.back().pop();
        available.insert(stacks.size() - 1);
        return val;
    }

    int popAtStack(int index) {
        if (index >= stacks.size() || stacks[index].empty()) return -1;
        int val = stacks[index].top(); stacks[index].pop();
        available.insert(index);
        return val;
    }
};
```


## 1354. Construct Target Array With Multiple Sums

**Problem:** https://leetcode.com/problems/construct-target-array-with-multiple-sums/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O((n+k) log k)

**Space complexity:** O(k+n)

**Complexity reasoning:** A set of k available servers and a min-heap of at most k busy servers process each of n requests; counts and result take O(k) space.

### Problem description

You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure : 

 let x be the sum of all elements currently in your array. 
 
 choose index i , such that 0 <= i < n and set the value of arr at index i to x . 
 
 You may repeat this procedure as many times as needed. 

 Return true if it is possible to construct the target array from arr , otherwise, return false . 

 Example 1: 
 
```
Input:
 target = [9,3,5]

Output:
 true

Explanation:
 Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
```

 Example 2: 
 
```
Input:
 target = [1,1,1,2]

Output:
 false

Explanation:
 Impossible to create target array from [1,1,1,1].
```

 Example 3: 
 
```
Input:
 target = [8,5]

Output:
 true
```

 Constraints: 

 n == target.length 
 
 1 <= n <= 5 * 10 4 
 
 1 <= target[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

class Solution {
public:
    bool isPossible(vector<int>& target) {
        long total = accumulate(target.begin(), target.end(), 0L);
        priority_queue<int> pq(target.begin(), target.end());

        while (pq.top() > 1) {
            int maxVal = pq.top(); pq.pop();
            long rest = total - maxVal;
            if (rest == 0 || maxVal <= rest) return false;

            int newVal = maxVal % rest;
            if (newVal == 0 && rest != 1) return false;
            pq.push(newVal == 0 ? rest : newVal);
            total = rest + newVal;
        }

        return true;
    }
};
```


## 1424. Diagonal Traverse II

**Problem:** https://leetcode.com/problems/diagonal-traverse-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Ordered map, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn log k)

**Space complexity:** O(mn + k)

**Complexity reasoning:** Compute all m*n XOR prefix values in a full prefix matrix and maintain a size-k min-heap.

### Problem description

Given a 2D integer array nums , return all elements of nums in diagonal order as shown in the below images . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/04/08/sample_1_1784.png] 
 
```
Input:
 nums = [[1,2,3],[4,5,6],[7,8,9]]

Output:
 [1,4,2,7,5,3,8,6,9]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/04/08/sample_2_1784.png] 
 
```
Input:
 nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]

Output:
 [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i].length <= 10 5 
 
 1 <= sum(nums[i].length) <= 10 5 
 
 1 <= nums[i][j] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        map<int, vector<int>> diag;
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = 0; j < nums[i].size(); ++j) {
                diag[i + j].push_back(nums[i][j]);
            }
        }

        vector<int> res;
        for (auto& [_, v] : diag) {
            reverse(v.begin(), v.end());
            res.insert(res.end(), v.begin(), v.end());
        }

        return res;
    }
};
```


## 1464. Maximum Product of Two Elements in an Array

**Problem:** https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n) amortized

**Space complexity:** O(n)

**Complexity reasoning:** Each order is inserted into a buy/sell price heap; matching removes or reinserts heap entries, with total successful matches bounded by O(n) amortized.

### Problem description

You are given an array of integers nums . 
 
 Choose two different indices i and j of that array. 
 
 Return the maximum value of (nums[i] - 1) * (nums[j] - 1) . 

 Example 1: 
 
```
Input:
 nums = [3,4,5,2]

Output:
 12 

Explanation:
 If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
```

 Example 2: 
 
```
Input:
 nums = [1,5,4,5]

Output:
 16

Explanation:
 Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
```

 Example 3: 
 
```
Input:
 nums = [3,7]

Output:
 12
```

 Constraints: 

 2 <= nums.length <= 500 
 
 1 <= nums[i] <= 10^3

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max1 = 0, max2 = 0;
        for (int n : nums) {
            if (n > max1) {
                max2 = max1;
                max1 = n;
            } else if (n > max2) {
                max2 = n;
            }
        }
        return (max1 - 1) * (max2 - 1);
    }
};
```


## 1500. Design a File Sharing System

**Problem:** https://leetcode.com/problems/design-a-file-sharing-system/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Hash Table, Design, Sorting, Heap (Priority Queue), Data Stream

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Sorting / Divide and Conquer, Stack / Queue

**Data structures (inferred):** Hash map, Hash map / hash set, Ordered map, Ordered set, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** add O(log m) typical; calculate O(1)

**Space complexity:** O(m)

**Complexity reasoning:** A queue and three balanced multisets maintain the m-element window; each add performs a constant number of inserts/erases and rebalances, while midSum answers queries.

### Problem description

We will use a file-sharing system to share a very large file which consists of m small chunks with IDs from 1 to m . 
 
 When users join the system, the system should assign a unique ID to them. The unique ID should be used once for each user, but when a user leaves the system, the ID can be reused again. 
 
 Users can request a certain chunk of the file, the system should return a list of IDs of all the users who own this chunk. If the user receives a non-empty list of IDs, they receive the requested chunk successfully. 

Implement the FileSharing class: 

 FileSharing(int m) Initializes the object with a file of m chunks. 
 
 int join(int[] ownedChunks) : A new user joined the system owning some chunks of the file, the system should assign an id to the user which is the smallest positive integer not taken by any other user. Return the assigned id. 
 
 void leave(int userID) : The user with userID will leave the system, you cannot take file chunks from them anymore. 
 
 int[] request(int userID, int chunkID) : The user userID requested the file chunk with chunkID . Return a list of the IDs of all users that own this chunk sorted in ascending order. 

 Example: 
 
```
Input:

["FileSharing","join","join","join","request","request","leave","request","leave","join"]
[[4],[[1,2]],[[2,3]],[[4]],[1,3],[2,2],[1],[2,1],[2],[[]]]

Output:

[null,1,2,3,[2],[1,2],null,[],null,1]

Explanation:

FileSharing fileSharing = new FileSharing(4); // We use the system to share a file of 4 chunks.

fileSharing.join([1, 2]); // A user who has chunks [1,2] joined the system, assign id = 1 to them and return 1.

fileSharing.join([2, 3]); // A user who has chunks [2,3] joined the system, assign id = 2 to them and return 2.

fileSharing.join([4]); // A user who has chunk [4] joined the system, assign id = 3 to them and return 3.

fileSharing.request(1, 3); // The user with id = 1 requested the third file chunk, as only the user with id = 2 has the file, return [2] . Notice that user 1 now has chunks [1,2,3].

fileSharing.request(2, 2); // The user with id = 2 requested the second file chunk, users with ids [1,2] have this chunk, thus we return [1,2].

fileSharing.leave(1); // The user with id = 1 left the system, all the file chunks with them are no longer available for other users.

fileSharing.request(2, 1); // The user with id = 2 requested the first file chunk, no one in the system has this chunk, we return empty list [].

fileSharing.leave(2); // The user with id = 2 left the system.

fileSharing.join([]); // A user who doesn't have any chunks joined the system, assign id = 1 to them and return 1. Notice that ids 1 and 2 are free and we can reuse them.
```

 Constraints: 

 1 <= m <= 10 5 
 
 0 <= ownedChunks.length <= min(100, m) 
 
 1 <= ownedChunks[i] <= m 
 
 Values of ownedChunks are unique. 
 
 1 <= chunkID <= m 
 
 userID is guaranteed to be a user in the system if you assign the IDs correctly . 
 
 At most 10 4 calls will be made to join , leave and request . 
 
 Each call to leave will have a matching call for join . 

 Follow-up: 

 What happens if the system identifies the user by their IP address instead of their unique ID and users disconnect and connect from the system with the same IP? 
 
 If the users in the system join and leave the system frequently without requesting any chunks, will your solution still be efficient? 
 
 If all users join the system one time, request all files, and then leave, will your solution still be efficient? 
 
 If the system will be used to share n files where the ith file consists of m[i] , what are the changes you have to make?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class FileSharing {
    int chunkCount;
    int nextId = 1;
    priority_queue<int, vector<int>, greater<int>> freeIds;
    unordered_map<int, set<int>> userChunks;
    unordered_map<int, set<int>> chunkOwners;

public:
    FileSharing(int m) : chunkCount(m) {}

    int join(vector<int> ownedChunks) {
        int id;
        if (freeIds.empty()) {
            id = nextId++;
        } else {
            id = freeIds.top();
            freeIds.pop();
        }
        userChunks[id] = {};
        for (int chunk : ownedChunks) {
            if (userChunks[id].insert(chunk).second) {
                chunkOwners[chunk].insert(id);
            }
        }
        return id;
    }

    void leave(int userID) {
        auto it = userChunks.find(userID);
        if (it == userChunks.end()) {
            return;
        }
        for (int chunk : it->second) {
            chunkOwners[chunk].erase(userID);
        }
        userChunks.erase(it);
        freeIds.push(userID);
    }

    vector<int> request(int userID, int chunkID) {
        vector<int> owners(chunkOwners[chunkID].begin(),
                           chunkOwners[chunkID].end());
        if (!owners.empty() && userChunks.count(userID) &&
            userChunks[userID].insert(chunkID).second) {
            chunkOwners[chunkID].insert(userID);
        }
        return owners;
    }
};
```


## 1606. Find Servers That Handled Most Number of Requests

**Problem:** https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Heap (Priority Queue), Simulation, Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Ordered set, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Append original indices, sort tasks by arrival, and enqueue/dequeue each task once in a priority queue.

### Problem description

You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time . The requests are assigned to servers according to a specific algorithm: 

 The i th (0-indexed) request arrives. 
 
 If all servers are busy, the request is dropped (not handled at all). 
 
 If the (i % k) th server is available, assign the request to that server. 
 
 Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the i th server is busy, try to assign the request to the (i+1) th server, then the (i+2) th server, and so on. 

 You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the i th request, and another array load , where load[i] represents the load of the i th request (the time it takes to complete). Your goal is to find the busiest server(s) . A server is considered busiest if it handled the most number of requests successfully among all the servers. 
 
 Return a list containing the IDs (0-indexed) of the busiest server(s) . You may return the IDs in any order. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/08/load-1.png] 
 
```
Input:
 k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 

Output:
 [1] 

Explanation:
 
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.
```

 Example 2: 
 
```
Input:
 k = 3, arrival = [1,2,3,4], load = [1,2,1,2]

Output:
 [0]

Explanation:
 
The first 3 requests are handled by first 3 servers.
Request 3 comes in. It is handled by server 0 since the server is available.
Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.
```

 Example 3: 
 
```
Input:
 k = 3, arrival = [1,2,3], load = [10,12,11]

Output:
 [0,1,2]

Explanation:
 Each server handles a single request, so they are all considered the busiest.
```

 Constraints: 

 1 <= k <= 10 5 
 
 1 <= arrival.length, load.length <= 10 5 
 
 arrival.length == load.length 
 
 1 <= arrival[i], load[i] <= 10 9 
 
 arrival is strictly increasing .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <queue>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        set<int> free;
        for (int i = 0; i < k; ++i) free.insert(i);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> busy;
        vector<int> count(k, 0);
        int n = arrival.size();
        for (int i = 0; i < n; ++i) {
            while (!busy.empty() && busy.top().first <= arrival[i]) {
                free.insert(busy.top().second);
                busy.pop();
            }
            if (free.empty()) continue;
            auto it = free.lower_bound(i % k);
            if (it == free.end()) it = free.begin();
            int server = *it;
            free.erase(it);
            count[server]++;
            busy.emplace(arrival[i] + load[i], server);
        }

        int maxReq = *max_element(count.begin(), count.end());
        vector<int> res;
        for (int i = 0; i < k; ++i)
            if (count[i] == maxReq) res.push_back(i);
        return res;
    }
};
```


## 1738. Find Kth Largest XOR Coordinate Value

**Problem:** https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Divide and Conquer, Bit Manipulation, Sorting, Heap (Priority Queue), Matrix, Prefix Sum, Quickselect

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Prefix Sum / Difference Array, Sorting / Divide and Conquer, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Prefix-sum array, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** constructor O(n); reserve O(log n); unreserve O(log n)

**Space complexity:** O(n)

**Complexity reasoning:** Constructor pushes n seats into a min-heap; reservation and return each change the heap once.

### Problem description

You are given a 2D matrix of size m x n , consisting of non-negative integers. You are also given an integer k . 
 
 The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed) . 
 
 Find the k th largest value (1-indexed) of all the coordinates of matrix . 

 Example 1: 
 
```
Input:
 matrix = [[5,2],[1,6]], k = 1

Output:
 7

Explanation:
 The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
```

 Example 2: 
 
```
Input:
 matrix = [[5,2],[1,6]], k = 2

Output:
 5

Explanation:
 The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
```

 Example 3: 
 
```
Input:
 matrix = [[5,2],[1,6]], k = 3

Output:
 4

Explanation:
 The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.
```

 Constraints: 

 m == matrix.length 
 
 n == matrix[i].length 
 
 1 <= m, n <= 1000 
 
 0 <= matrix[i][j] <= 10 6 
 
 1 <= k <= m * n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> pre(m + 1, vector<int>(n + 1));
        priority_queue<int, vector<int>, greater<>> pq;

        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j) {
                pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1];
                pq.push(pre[i][j]);
                if (pq.size() > k) pq.pop();
            }

        return pq.top();
    }
};
```


## 1801. Number of Orders in the Backlog

**Problem:** https://leetcode.com/problems/number-of-orders-in-the-backlog/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Heap (Priority Queue), Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn * r^2 * log(mn)) upper bound

**Space complexity:** O(mn)

**Complexity reasoning:** For every cell, examine rhombus radii up to r=min(m,n), traversing O(radius) boundary cells; insert sums into an ordered set of at most O(mn*r) candidates (bound O(mn*r) space in general).

### Problem description

You are given a 2D integer array orders , where each orders[i] = [price i , amount i , orderType i ] denotes that amount i orders have been placed of type orderType i at the price price i . The orderType i is: 

 0 if it is a batch of buy orders, or 
 
 1 if it is a batch of sell orders. 

 Note that orders[i] represents a batch of amount i independent orders with the same price and order type. All orders represented by orders[i] will be placed before all orders represented by orders[i+1] for all valid i . 
 
 There is a backlog that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens: 

 If the order is a buy order, you look at the sell order with the smallest price in the backlog. If that sell order's price is smaller than or equal to the current buy order's price, they will match and be executed, and that sell order will be removed from the backlog. Else, the buy order is added to the backlog. 
 
 Vice versa, if the order is a sell order, you look at the buy order with the largest price in the backlog. If that buy order's price is larger than or equal to the current sell order's price, they will match and be executed, and that buy order will be removed from the backlog. Else, the sell order is added to the backlog. 

 Return the total amount of orders in the backlog after placing all the orders from the input . Since this number can be large, return it modulo 10 9 + 7 . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/03/11/ex1.png] 
 
```
Input:
 orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]

Output:
 6

Explanation:
 Here is what happens with the orders:
- 5 orders of type buy with price 10 are placed. There are no sell orders, so the 5 orders are added to the backlog.
- 2 orders of type sell with price 15 are placed. There are no buy orders with prices larger than or equal to 15, so the 2 orders are added to the backlog.
- 1 order of type sell with price 25 is placed. There are no buy orders with prices larger than or equal to 25 in the backlog, so this order is added to the backlog.
- 4 orders of type buy with price 30 are placed. The first 2 orders are matched with the 2 sell orders of the least price, which is 15 and these 2 sell orders are removed from the backlog. The 3
rd
 order is matched with the sell order of the least price, which is 25 and this sell order is removed from the backlog. Then, there are no more sell orders in the backlog, so the 4
th
 order is added to the backlog.
Finally, the backlog has 5 buy orders with price 10, and 1 buy order with price 30. So the total number of orders in the backlog is 6.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/03/11/ex2.png] 
 
```
Input:
 orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]

Output:
 999999984

Explanation:
 Here is what happens with the orders:
- 10
9
 orders of type sell with price 7 are placed. There are no buy orders, so the 10
9
 orders are added to the backlog.
- 3 orders of type buy with price 15 are placed. They are matched with the 3 sell orders with the least price which is 7, and those 3 sell orders are removed from the backlog.
- 999999995 orders of type buy with price 5 are placed. The least price of a sell order is 7, so the 999999995 orders are added to the backlog.
- 1 order of type sell with price 5 is placed. It is matched with the buy order of the highest price, which is 5, and that buy order is removed from the backlog.
Finally, the backlog has (1000000000-3) sell orders with price 7, and (999999995-1) buy orders with price 5. So the total number of orders = 1999999991, which is equal to 999999984 % (10
9
 + 7).
```

 Constraints: 

 1 <= orders.length <= 10 5 
 
 orders[i].length == 3 
 
 1 <= price i , amount i <= 10 9 
 
 orderType i is either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 int getNumberOfBacklogOrders(vector<vector<int>>& orders){
  priority_queue<pair<int,int>> buy;
  priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> sell;
  for(auto& o:orders){int price=o[0],amount=o[1],type=o[2];
   if(type==0){while(amount && !sell.empty() && sell.top().first<=price){auto p=sell.top();sell.pop();int take=min(amount,p.second);amount-=take;p.second-=take;if(p.second)sell.push(p);}if(amount)buy.push({price,amount});}
   else {while(amount && !buy.empty() && buy.top().first>=price){auto p=buy.top();buy.pop();int take=min(amount,p.second);amount-=take;p.second-=take;if(p.second)buy.push(p);}if(amount)sell.push({price,amount});}
  }
  const int MOD=1000000007;long long ans=0;
  while(!buy.empty()){ans=(ans+buy.top().second)%MOD;buy.pop();}
  while(!sell.empty()){ans=(ans+sell.top().second)%MOD;sell.pop();}
  return ans;
 }
};
```


## 1825. Finding MK Average

**Problem:** https://leetcode.com/problems/finding-mk-average/

**Difficulty:** Hard | **Premium:** No

**Tags:** Design, Queue, Heap (Priority Queue), Data Stream, Ordered Set, Treap

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Stack / Queue

**Data structures (inferred):** Ordered set, Priority queue / heap, Queue

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O((n+t) log n)

**Space complexity:** O(n+t)

**Complexity reasoning:** Two heaps manage n servers; each of t tasks and each server release triggers logarithmic heap work. Result stores t assignments.

### Problem description

You are given two integers, m and k , and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream. 
 
 The MKAverage can be calculated using these steps: 

 If the number of the elements in the stream is less than m you should consider the MKAverage to be -1 . Otherwise, copy the last m elements of the stream to a separate container. 
 
 Remove the smallest k elements and the largest k elements from the container. 
 
 Calculate the average value for the rest of the elements rounded down to the nearest integer . 

 Implement the MKAverage class: 

 MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k . 
 
 void addElement(int num) Inserts a new element num into the stream. 
 
 int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer . 

 Example 1: 
 
```
Input

["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]

Output

[null, null, null, -1, null, 3, null, null, null, 5]

Explanation

MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3); // current elements are [3]
obj.addElement(1); // current elements are [3,1]
obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
obj.addElement(10); // current elements are [3,1,10]
obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
 // After removing smallest and largest 1 element the container will be [3].
 // The average of [3] equals 3/1 = 3, return 3
obj.addElement(5); // current elements are [3,1,10,5]
obj.addElement(5); // current elements are [3,1,10,5,5]
obj.addElement(5); // current elements are [3,1,10,5,5,5]
obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
 // After removing smallest and largest 1 element the container will be [5].
 // The average of [5] equals 5/1 = 5, return 5
```

 Constraints: 

 3 <= m <= 10 5 
 
 1 < k*2 < m 
 
 1 <= num <= 10 5 
 
 At most 10 5 calls will be made to addElement and calculateMKAverage .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <queue>
#include <set>
using namespace std;

class MKAverage {
    int m, k;
    queue<int> q;
    multiset<int> lo, mid, hi;
    long long midSum = 0;

public:
    MKAverage(int m_, int k_) : m(m_), k(k_) {}

    void addElement(int num) {
        q.push(num);
        lo.insert(num);

        if (lo.size() > k) {
            mid.insert(*lo.rbegin());
            midSum += *lo.rbegin();
            lo.erase(prev(lo.end()));
        }

        if (mid.size() > m - 2 * k) {
            hi.insert(*mid.rbegin());
            midSum -= *mid.rbegin();
            mid.erase(prev(mid.end()));
        }

        if (q.size() > m) {
            int old = q.front(); q.pop();
            if (lo.count(old)) lo.erase(lo.find(old));
            else if (mid.count(old)) {
                mid.erase(mid.find(old));
                midSum -= old;
            } else hi.erase(hi.find(old));

            if (lo.size() < k && !mid.empty()) {
                lo.insert(*mid.begin());
                midSum -= *mid.begin();
                mid.erase(mid.begin());
            }

            if (mid.size() < m - 2 * k && !hi.empty()) {
                mid.insert(*hi.begin());
                midSum += *hi.begin();
                hi.erase(hi.begin());
            }
        }
    }

    int calculateMKAverage() {
        if (q.size() < m) return -1;
        return midSum / (m - 2 * k);
    }
};
```


## 1834. Single-Threaded CPU

**Problem:** https://leetcode.com/problems/single-threaded-cpu/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Append indices, sort n tasks by enqueue time, and process each through a min-heap ordered by duration and index.

### Problem description

You are given n ​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks , where tasks[i] = [enqueueTime i , processingTime i ] means that the i ​​​​​​th ​​​​ task will be available to process at enqueueTime i and will take processingTime i to finish processing. 
 
 You have a single-threaded CPU that can process at most one task at a time and will act in the following way: 

 If the CPU is idle and there are no available tasks to process, the CPU remains idle. 
 
 If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time . If multiple tasks have the same shortest processing time, it will choose the task with the smallest index. 
 
 Once a task is started, the CPU will process the entire task without stopping. 
 
 The CPU can finish a task then start a new one instantly. 

 Return the order in which the CPU will process the tasks. 

 Example 1: 
 
```
Input:
 tasks = [[1,2],[2,4],[3,2],[4,1]]

Output:
 [0,2,3,1]

Explanation: 
The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
```

 Example 2: 
 
```
Input:
 tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]

Output:
 [4,3,2,0,1]

Explanation
: 
The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.
```

 Constraints: ​​​​​​​ 

 1 <= tasks.length <= 10 5 
 
 tasks[i] = [enqueueTime i , processingTime i ] 
 
 1 <= enqueueTime i , processingTime i <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n = tasks.size();
        for (int i = 0; i < n; ++i)
            tasks[i].push_back(i);  // append index

        sort(tasks.begin(), tasks.end());

        auto cmp = [](vector<int>& a, vector<int>& b) {
            return a[1] > b[1] || (a[1] == b[1] && a[2] > b[2]);
        };

        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> pq(cmp);
        vector<int> res;
        long time = 0;
        int i = 0;

        while (i < n || !pq.empty()) {
            if (pq.empty() && time < tasks[i][0])
                time = tasks[i][0];
            while (i < n && tasks[i][0] <= time)
                pq.push(tasks[i++]);
            auto curr = pq.top(); pq.pop();
            time += curr[1];
            res.push_back(curr[2]);
        }

        return res;
    }
};
```


## 1845. Seat Reservation Manager

**Problem:** https://leetcode.com/problems/seat-reservation-manager/

**Difficulty:** Medium | **Premium:** No

**Tags:** Design, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Stack / Queue

**Data structures (inferred):** Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** constructor O(n log n); reserve/unreserve O(log n)

**Space complexity:** O(n)

**Complexity reasoning:** The constructor inserts n seat IDs into a min-heap; each operation pushes or pops one seat.

### Problem description

Design a system that manages the reservation state of n seats that are numbered from 1 to n . 
 
 Implement the SeatManager class: 

 SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n . All seats are initially available. 
 
 int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number. 
 
 void unreserve(int seatNumber) Unreserves the seat with the given seatNumber . 

 Example 1: 
 
```
Input

["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]

Output

[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation

SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve(); // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve(); // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve(); // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve(); // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve(); // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve(); // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
```

 Constraints: 

 1 <= n <= 10 5 
 
 1 <= seatNumber <= n 
 
 For each call to reserve , it is guaranteed that there will be at least one unreserved seat. 
 
 For each call to unreserve , it is guaranteed that seatNumber will be reserved. 
 
 At most 10 5 calls in total will be made to reserve and unreserve .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <queue>
using namespace std;

class SeatManager {
    priority_queue<int, vector<int>, greater<int>> pq;
    int next = 1;

public:
    SeatManager(int n) {
        for (int i = 1; i <= n; ++i) pq.push(i);
    }

    int reserve() {
        int res = pq.top(); pq.pop();
        return res;
    }

    void unreserve(int seatNumber) {
        pq.push(seatNumber);
    }
};
```


## 1878. Get Biggest Three Rhombus Sums in a Grid

**Problem:** https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Math, Sorting, Heap (Priority Queue), Matrix, Prefix Sum

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Prefix Sum / Difference Array, Math / Number Theory, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Ordered set, Prefix-sum array, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn r^2 + Q log Q)

**Space complexity:** O(Q)

**Complexity reasoning:** For each of mn top vertices, examine up to r=min(m,n) radii and walk O(radius) perimeter cells. Insert Q distinct sums into an ordered set; Q ≤ O(mnr).

### Problem description

You are given an m x n integer matrix grid ​​​. 
 
 A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid ​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum : 
 [Figure: https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-desc-2.png] 
 
 Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner. 
 
 Return the biggest three distinct rhombus sums in the grid in descending order . If there are less than three distinct values, return all of them . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex1.png] 
 
```
Input:
 grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]

Output:
 [228,216,211]

Explanation:
 The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex2.png] 
 
```
Input:
 grid = [[1,2,3],[4,5,6],[7,8,9]]

Output:
 [20,9,8]

Explanation:
 The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
```

 Example 3: 
 
```
Input:
 grid = [[7,7,7]]

Output:
 [7]

Explanation:
 All three possible rhombus sums are the same, so return [7].
```

 Constraints: 

 m == grid.length 
 
 n == grid[i].length 
 
 1 <= m, n <= 50 
 
 1 <= grid[i][j] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int> getBiggestThree(vector<vector<int>>& grid){int m=grid.size(),n=grid[0].size();set<int,greater<int>> sums;for(int r=0;r<m;++r)for(int c=0;c<n;++c){sums.insert(grid[r][c]);for(int k=1;r+2*k<m&&c-k>=0&&c+k<n;++k){int sum=0;for(int d=0;d<k;++d){sum+=grid[r+d][c+d];sum+=grid[r+k+d][c+k-d];sum+=grid[r+2*k-d][c-d];sum+=grid[r+k-d][c-k+d];}sums.insert(sum);}}vector<int> ans;for(int x:sums){if(ans.size()==3)break;ans.push_back(x);}return ans;}};
```


## 1882. Process Tasks Using Servers

**Problem:** https://leetcode.com/problems/process-tasks-using-servers/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O((n+t) log n)

**Space complexity:** O(n+t)

**Complexity reasoning:** Initialize the n-server free heap; every task is assigned once and every busy-to-free transition performs logarithmic heap operations.

### Problem description

You are given two 0-indexed integer arrays servers and tasks of lengths n ​​​​​​ and m ​​​​​​ respectively. servers[i] is the weight of the i ​​​​​​th ​​​​ server, and tasks[j] is the time needed to process the j ​​​​​​th ​​​​ task in seconds . 
 
 Tasks are assigned to the servers using a task queue . Initially, all servers are free, and the queue is empty . 
 
 At second j , the j th task is inserted into the queue (starting with the 0 th task being inserted at second 0 ). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight , and in case of a tie, it is assigned to a free server with the smallest index . 
 
 If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above. 
 
 A server that is assigned task j at second t will be free again at second t + tasks[j] . 
 
 Build an array ans ​​​​ of length m , where ans[j] is the index of the server the j ​​​​​​th task will be assigned to. 
 
 Return the array ans ​​​​. 

 Example 1: 
 
```
Input:
 servers = [3,3,2], tasks = [1,2,3,2,1,2]

Output:
 [2,2,0,2,1,2]

Explanation: 
Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.
```

 Example 2: 
 
```
Input:
 servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]

Output:
 [1,4,1,4,1,3,2]

Explanation: 
Events in chronological order go as follows: 
- At second 0, task 0 is added and processed using server 1 until second 2.
- At second 1, task 1 is added and processed using server 4 until second 2.
- At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
- At second 3, task 3 is added and processed using server 4 until second 7.
- At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
- At second 5, task 5 is added and processed using server 3 until second 7.
- At second 6, task 6 is added and processed using server 2 until second 7.
```

 Constraints: 

 servers.length == n 
 
 tasks.length == m 
 
 1 <= n, m <= 2 * 10 5 
 
 1 <= servers[i], tasks[j] <= 2 * 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> free, busy;
        for (int i = 0; i < servers.size(); ++i)
            free.emplace(servers[i], i);

        vector<int> res;
        long long time = 0;
        for (int i = 0; i < tasks.size(); ++i) {
            time = max(time, (long long)i);
            while (!busy.empty() && busy.top().first <= time) {
                auto [_, id] = busy.top(); busy.pop();
                free.emplace(servers[id], id);
            }
            if (free.empty()) {
                time = busy.top().first;
                while (!busy.empty() && busy.top().first <= time) {
                    auto [_, id] = busy.top(); busy.pop();
                    free.emplace(servers[id], id);
                }
            }
            auto [w, id] = free.top(); free.pop();
            res.push_back(id);
            busy.emplace(time + tasks[i], id);
        }
        return res;
    }
};
```


## 1912. Design Movie Rental System

**Problem:** https://leetcode.com/problems/design-movie-rental-system/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, Design, Heap (Priority Queue), Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Ordered map, Ordered set, Priority queue / heap, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** constructor O(E log E); search/report O(1) bounded by 5; rent/drop O(log E)

**Space complexity:** O(E)

**Complexity reasoning:** Ordered maps and sets index E movie entries; each rental transition updates balanced trees. Search and report return at most five results.

### Problem description

You have a movie renting company consisting of n shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies. 
 
 Each movie is given as a 2D integer array entries where entries[i] = [shop i , movie i , price i ] indicates that there is a copy of movie movie i at shop shop i with a rental price of price i . Each shop carries at most one copy of a movie movie i . 
 
 The system should support the following functions: 

 Search : Finds the cheapest 5 shops that have an unrented copy of a given movie. The shops should be sorted by price in ascending order, and in case of a tie, the one with the smaller shop i should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned. 
 
 Rent : Rents an unrented copy of a given movie from a given shop. 
 
 Drop : Drops off a previously rented copy of a given movie at a given shop. 
 
 Report : Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shop j , movie j ] describes that the j th cheapest rented movie movie j was rented from the shop shop j . The movies in res should be sorted by price in ascending order, and in case of a tie, the one with the smaller shop j should appear first, and if there is still tie, the one with the smaller movie j should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned. 

 Implement the MovieRentingSystem class: 

 MovieRentingSystem(int n, int[][] entries) Initializes the MovieRentingSystem object with n shops and the movies in entries . 
 
 List<Integer> search(int movie) Returns a list of shops that have an unrented copy of the given movie as described above. 
 
 void rent(int shop, int movie) Rents the given movie from the given shop . 
 
 void drop(int shop, int movie) Drops off a previously rented movie at the given shop . 
 
 List<List<Integer>> report() Returns a list of cheapest rented movies as described above. 

 Note: The test cases will be generated such that rent will only be called if the shop has an unrented copy of the movie, and drop will only be called if the shop had previously rented out the movie. 

 Example 1: 
 
```
Input

["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]

Output

[null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]

Explanation

MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
movieRentingSystem.search(1); // return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest; shop 0 and 2 are the same price, so order by shop number.
movieRentingSystem.rent(0, 1); // Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
movieRentingSystem.rent(1, 2); // Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
movieRentingSystem.report(); // return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
movieRentingSystem.drop(1, 2); // Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
movieRentingSystem.search(2); // return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.
```

 Constraints: 

 1 <= n <= 3 * 10 5 
 
 1 <= entries.length <= 10 5 
 
 0 <= shop i < n 
 
 1 <= movie i , price i <= 10 4 
 
 Each shop carries at most one copy of a movie movie i . 
 
 At most 10 5 calls in total will be made to search , rent , drop and report .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class MovieRentingSystem {map<int,set<pair<int,int>>> available;set<tuple<int,int,int>> rented;map<pair<int,int>,int> price;public:MovieRentingSystem(int n,vector<vector<int>>& entries){for(auto &e:entries){int shop=e[0],movie=e[1],p=e[2];price[{shop,movie}]=p;available[movie].insert({p,shop});}}vector<int> search(int movie){vector<int> ans;auto it=available.find(movie);if(it==available.end())return ans;for(auto &x:it->second){if(ans.size()==5)break;ans.push_back(x.second);}return ans;}void rent(int shop,int movie){int p=price[{shop,movie}];available[movie].erase({p,shop});rented.insert(make_tuple(p,shop,movie));}void drop(int shop,int movie){int p=price[{shop,movie}];rented.erase(make_tuple(p,shop,movie));available[movie].insert({p,shop});}vector<vector<int>> report(){vector<vector<int>> ans;for(auto &x:rented){if(ans.size()==5)break;ans.push_back({get<1>(x),get<2>(x)});}return ans;}};
```


## 1942. The Number of the Smallest Unoccupied Chair

**Problem:** https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Sort n arrival events, then release occupied chairs and allocate the smallest available chair using two heaps.

### Problem description

There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity . When a friend arrives at the party, they sit on the unoccupied chair with the smallest number . 

 For example, if chairs 0 , 1 , and 5 are occupied when a friend comes, they will sit on chair number 2 . 

 When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair. 
 
 You are given a 0-indexed 2D integer array times where times[i] = [arrival i , leaving i ] , indicating the arrival and leaving times of the i th friend respectively, and an integer targetFriend . All arrival times are distinct . 
 
 Return the chair number that the friend numbered targetFriend will sit on . 

 Example 1: 
 
```
Input:
 times = [[1,4],[2,3],[4,6]], targetFriend = 1

Output:
 1

Explanation:
 
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.
```

 Example 2: 
 
```
Input:
 times = [[3,10],[1,5],[2,6]], targetFriend = 0

Output:
 2

Explanation:
 
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.
```

 Constraints: 

 n == times.length 
 
 2 <= n <= 10 4 
 
 times[i].length == 2 
 
 1 <= arrival i < leaving i <= 10 5 
 
 0 <= targetFriend <= n - 1 
 
 Each arrival i time is distinct .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int smallestChair(vector<vector<int>>& times,int targetFriend){int target=times[targetFriend][0],n=times.size();vector<array<int,3>> events;for(int i=0;i<n;++i)events.push_back({times[i][0],times[i][1],i});sort(events.begin(),events.end());priority_queue<int,vector<int>,greater<int>> free;priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> busy;int next=0;for(auto e:events){while(!busy.empty()&&busy.top().first<=e[0]){free.push(busy.top().second);busy.pop();}int chair;if(free.empty())chair=next++;else{chair=free.top();free.pop();}if(e[2]==targetFriend)return chair;busy.push({e[1],chair});}return -1;}};
```


## 1985. Find the Kth Largest Integer in the Array

**Problem:** https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue / heap, Sorted array, String, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n * L)

**Space complexity:** O(log n + L) auxiliary (excluding input and returned string)

**Complexity reasoning:** Sorting n numeric strings uses O(n log n) comparisons; each equal-length lexicographic comparison can inspect up to L digits. std::sort uses O(log n) stack; returning a string copies up to L characters.

### Problem description

You are given an array of strings nums and an integer k . Each string in nums represents an integer without leading zeros. 
 
 Return the string that represents the k th largest integer in nums . 
 
 Note : Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"] , "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer. 

 Example 1: 
 
```
Input:
 nums = ["3","6","7","10"], k = 4

Output:
 "3"

Explanation:

The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4
th
 largest integer in nums is "3".
```

 Example 2: 
 
```
Input:
 nums = ["2","21","12","1"], k = 3

Output:
 "2"

Explanation:

The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3
rd
 largest integer in nums is "2".
```

 Example 3: 
 
```
Input:
 nums = ["0","0"], k = 2

Output:
 "0"

Explanation:

The numbers in nums sorted in non-decreasing order are ["0","0"].
The 2
nd
 largest integer in nums is "0".
```

 Constraints: 

 1 <= k <= nums.length <= 10 4 
 
 1 <= nums[i].length <= 100 
 
 nums[i] consists of only digits. 
 
 nums[i] will not have any leading zeros.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string kthLargestNumber(vector<string>& nums, int k) {
        sort(nums.begin(), nums.end(), [](const string& a, const string& b) {
            return a.size() == b.size() ? a < b : a.size() < b.size();
        });
        return nums[nums.size() - k];
    }
};
```


## 2015. Average Height of Buildings in Each Segment

**Problem:** https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Sorting, Heap (Priority Queue), Prefix Sum

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Prefix Sum / Difference Array, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Ordered map, Prefix-sum array, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Each of n buildings creates two events in an ordered map; updates cost O(log n), then a linear sweep creates at most O(n) segments.

### Problem description

A perfectly straight street is represented by a number line. The street has building(s) on it and is represented by a 2D integer array buildings , where buildings[i] = [start i , end i , height i ] . This means that there is a building with height i in the half-closed segment [start i , end i ) . 
 
 You want to describe the heights of the buildings on the street with the minimum number of non-overlapping segments . The street can be represented by the 2D integer array street where street[j] = [left j , right j , average j ] describes a half-closed segment [left j , right j ) of the road where the average heights of the buildings in the segment is average j . 

 For example, if buildings = [[1,5,2],[3,10,4]], the street could be represented by street = [[1,3,2],[3,5,3],[5,10,4]] because:

 From 1 to 3, there is only the first building with an average height of 2 / 1 = 2 . 
 
 From 3 to 5, both the first and the second building are there with an average height of (2+4) / 2 = 3 . 
 
 From 5 to 10, there is only the second building with an average height of 4 / 1 = 4 . 

 Given buildings , return the 2D integer array street as described above ( excluding any areas of the street where there are no buldings). You may return the array in any order . 
 
 The average of n elements is the sum of the n elements divided ( integer division ) by n . 
 
 A half-closed segment [a, b) is the section of the number line between points a and b including point a and not including point b . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/09/21/image-20210921224001-2.png] 
 
```
Input:
 buildings = [[1,4,2],[3,9,4]]

Output:
 [[1,3,2],[3,4,3],[4,9,4]]

Explanation:

From 1 to 3, there is only the first building with an average height of 2 / 1 = 2.
From 3 to 4, both the first and the second building are there with an average height of (2+4) / 2 = 3.
From 4 to 9, there is only the second building with an average height of 4 / 1 = 4.
```

 Example 2: 
 
```
Input:
 buildings = [[1,3,2],[2,5,3],[2,8,3]]

Output:
 [[1,3,2],[3,8,3]]

Explanation:

From 1 to 2, there is only the first building with an average height of 2 / 1 = 2.
From 2 to 3, all three buildings are there with an average height of (2+3+3) / 3 = 2.
From 3 to 5, both the second and the third building are there with an average height of (3+3) / 2 = 3.
From 5 to 8, there is only the last building with an average height of 3 / 1 = 3.
The average height from 1 to 3 is the same so we can group them into one segment.
The average height from 3 to 8 is the same so we can group them into one segment.
```

 Example 3: 
 
```
Input:
 buildings = [[1,2,1],[5,6,1]]

Output:
 [[1,2,1],[5,6,1]]

Explanation:

From 1 to 2, there is only the first building with an average height of 1 / 1 = 1.
From 2 to 5, there are no buildings, so it is not included in the output.
From 5 to 6, there is only the second building with an average height of 1 / 1 = 1.
We cannot group the segments together because an empty space with no buildings seperates the segments.
```

 Constraints: 

 1 <= buildings.length <= 10 5 
 
 buildings[i].length == 3 
 
 0 <= start i < end i <= 10 8 
 
 1 <= height i <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> averageHeightOfBuildings(vector<vector<int>>& buildings) {
        map<int, pair<long long, long long>> delta;
        for (const auto& b : buildings) {
            delta[b[0]].first += b[2];
            delta[b[0]].second += 1;
            delta[b[1]].first -= b[2];
            delta[b[1]].second -= 1;
        }
        vector<vector<int>> answer;
        long long sum = 0, count = 0;
        for (auto it = delta.begin(); it != delta.end(); ++it) {
            sum += it->second.first;
            count += it->second.second;
            auto nextIt = next(it);
            if (nextIt == delta.end() || count == 0) continue;
            int avg = (int)(sum / count);
            if (!answer.empty() && answer.back()[1] == it->first &&
                answer.back()[2] == avg) {
                answer.back()[1] = nextIt->first;
            } else {
                answer.push_back({it->first, nextIt->first, avg});
            }
        }
        return answer;
    }
};
```


## 2034. Stock Price Fluctuation 

**Problem:** https://leetcode.com/problems/stock-price-fluctuation/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, Design, Heap (Priority Queue), Data Stream, Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Stack / Queue

**Data structures (inferred):** Hash map / hash set, Ordered map, Ordered set, Priority queue / heap

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** update O(log n); current O(log n); maximum/minimum O(1)

**Space complexity:** O(n) total

**Complexity reasoning:** Ordered map and multiset store n distinct timestamps/prices; update performs logarithmic insertion/erasure. current uses map operator[] (O(log n)); extrema read begin/rbegin.

### Problem description

You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp. 
 
 Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record. 
 
 Design an algorithm that: 

 Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp. 
 
 Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded. 
 
 Finds the maximum price the stock has been based on the current records. 
 
 Finds the minimum price the stock has been based on the current records. 

 Implement the StockPrice class: 

 StockPrice() Initializes the object with no price records. 
 
 void update(int timestamp, int price) Updates the price of the stock at the given timestamp . 
 
 int current() Returns the latest price of the stock. 
 
 int maximum() Returns the maximum price of the stock. 
 
 int minimum() Returns the minimum price of the stock. 

 Example 1: 
 
```
Input

["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]

Output

[null, null, null, 5, 10, null, 5, null, 2]

Explanation

StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5); // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current(); // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum(); // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3); // The previous timestamp 1 had the wrong price, so it is updated to 3.
 // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum(); // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2); // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum(); // return 2, the minimum price is 2 at timestamp 4.
```

 Constraints: 

 1 <= timestamp, price <= 10 9 
 
 At most 10 5 calls will be made in total to update , current , maximum , and minimum . 
 
 current , maximum , and minimum will be called only after update has been called at least once .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <map>
#include <set>
using namespace std;

class StockPrice {
    map<int, int> timePrice;
    multiset<int> prices;
    int currentTime = 0;

public:
    void update(int timestamp, int price) {
        if (timePrice.count(timestamp)) {
            prices.erase(prices.find(timePrice[timestamp]));
        }
        timePrice[timestamp] = price;
        prices.insert(price);
        currentTime = max(currentTime, timestamp);
    }

    int current() {
        return timePrice[currentTime];
    }

    int maximum() {
        return *prices.rbegin();
    }

    int minimum() {
        return *prices.begin();
    }
};
```


## 2099. Find Subsequence of Length K With the Largest Sum

**Problem:** https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Hash Table, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log k + k log k)

**Space complexity:** O(k) auxiliary plus O(k) output

**Complexity reasoning:** Keep at most k value/index pairs in a min-heap while scanning n values, extract k entries, and sort the selected entries by original index.

### Problem description

You are given an integer array nums and an integer k . You want to find a subsequence of nums of length k that has the largest sum. 
 
 Return any such subsequence as an integer array of length k . 
 
 A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements. 

 Example 1: 
 
```
Input:
 nums = [2,1,3,3], k = 2

Output:
 [3,3]

Explanation:

The subsequence has the largest sum of 3 + 3 = 6.
```

 Example 2: 
 
```
Input:
 nums = [-1,-2,3,4], k = 3

Output:
 [-1,3,4]

Explanation:
 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
```

 Example 3: 
 
```
Input:
 nums = [3,4,3,3], k = 2

Output:
 [3,4]

Explanation:

The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
```

 Constraints: 

 1 <= nums.length <= 1000 
 
 -10 5  <= nums[i] <= 10 5 
 
 1 <= k <= nums.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        for (int i = 0; i < nums.size(); ++i) {
            pq.push({nums[i], i});
            if (pq.size() > k) pq.pop();
        }

        vector<pair<int, int>> top(pq.size());
        int idx = 0;
        while (!pq.empty()) {
            top[idx++] = pq.top();
            pq.pop();
        }

        sort(top.begin(), top.end(), [](auto& a, auto& b) {
            return a.second < b.second;
        });

        vector<int> res;
        for (auto& [val, i] : top) res.push_back(val);
        return res;
    }
};
```


## 2102. Sequentially Ordinal Rank Tracker

**Problem:** https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

**Difficulty:** Hard | **Premium:** No

**Tags:** Design, Heap (Priority Queue), Data Stream, Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Stack / Queue

**Data structures (inferred):** Ordered set, Priority queue / heap

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** add O(log n); get O(log n)

**Space complexity:** O(n) total

**Complexity reasoning:** Two balanced ordered sets maintain ranked entries; add performs a constant number of set operations, and get transfers one entry between sets. String copying/comparison additionally depends on name length.

### Problem description

A scenic location is represented by its name and attractiveness score , where name is a unique string among all locations and score is an integer. Locations can be ranked from the best to the worst. The higher the score, the better the location. If the scores of two locations are equal, then the location with the lexicographically smaller name is better. 
 
 You are building a system that tracks the ranking of locations with the system initially starting with no locations. It supports: 

 Adding scenic locations, one at a time . 
 
 Querying the i th best location of all locations already added , where i is the number of times the system has been queried (including the current query).

 For example, when the system is queried for the 4 th time, it returns the 4 th best location of all locations already added. 

 Note that the test data are generated so that at any time , the number of queries does not exceed the number of locations added to the system. 
 
 Implement the SORTracker class: 

 SORTracker() Initializes the tracker system. 
 
 void add(string name, int score) Adds a scenic location with name and score to the system. 
 
 string get() Queries and returns the i th best location, where i is the number of times this method has been invoked (including this invocation). 

 Example 1: 
 
```
Input

["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]

Output

[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

Explanation

SORTracker tracker = new SORTracker(); // Initialize the tracker system.
tracker.add("bradford", 2); // Add location with name="bradford" and score=2 to the system.
tracker.add("branford", 3); // Add location with name="branford" and score=3 to the system.
tracker.get(); // The sorted locations, from best to worst, are: branford, bradford.
 // Note that branford precedes bradford due to its 
higher score
 (3 > 2).
 // This is the 1
st
 time get() is called, so return the best location: "branford".
tracker.add("alps", 2); // Add location with name="alps" and score=2 to the system.
tracker.get(); // Sorted locations: branford, alps, bradford.
 // Note that alps precedes bradford even though they have the same score (2).
 // This is because "alps" is 
lexicographically smaller
 than "bradford".
 // Return the 2
nd
 best location "alps", as it is the 2
nd
 time get() is called.
tracker.add("orland", 2); // Add location with name="orland" and score=2 to the system.
tracker.get(); // Sorted locations: branford, alps, bradford, orland.
 // Return "bradford", as it is the 3
rd
 time get() is called.
tracker.add("orlando", 3); // Add location with name="orlando" and score=3 to the system.
tracker.get(); // Sorted locations: branford, orlando, alps, bradford, orland.
 // Return "bradford".
tracker.add("alpine", 2); // Add location with name="alpine" and score=2 to the system.
tracker.get(); // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
 // Return "bradford".
tracker.get(); // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
 // Return "orland".
```

 Constraints: 

 name consists of lowercase English letters, and is unique among all locations. 
 
 1 <= name.length <= 10 
 
 1 <= score <= 10 5 
 
 At any time, the number of calls to get does not exceed the number of calls to add . 
 
 At most 4 * 10 4 calls in total will be made to add and get .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class SORTracker {
    typedef pair<int,string> Entry;
    struct Better {
        bool operator()(const Entry& a, const Entry& b) const {
            if (a.first != b.first) return a.first > b.first;
            return a.second < b.second;
        }
    };
    set<Entry, Better> top, rest;
public:
    SORTracker() {}
    void add(string name, int score) {
        Entry e = {score, name};
        if (!top.empty() && Better()(e, *prev(top.end()))) {
            top.insert(e);
            auto it = prev(top.end());
            rest.insert(*it);
            top.erase(it);
        } else {
            rest.insert(e);
        }
    }
    string get() {
        auto it = rest.begin();
        Entry e = *it;
        rest.erase(it);
        top.insert(e);
        return e.second;
    }
};
```


## 2231. Largest Number After Digit Swaps by Parity

**Problem:** https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

**Difficulty:** Easy | **Premium:** No

**Tags:** Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer

**Data structures (inferred):** Priority queue / heap, Sorted array

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(d log d)

**Space complexity:** O(d)

**Complexity reasoning:** Convert the d-digit number to a string, sort odd and even digit groups, then reconstruct the digits.

### Problem description

You are given a positive integer num . You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits). 
 
 Return the largest possible value of num after any number of swaps. 

 Example 1: 
 
```
Input:
 num = 1234

Output:
 3412

Explanation:
 Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
```

 Example 2: 
 
```
Input:
 num = 65875

Output:
 87655

Explanation:
 Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
```

 Constraints: 

 1 <= num <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 int largestInteger(int num){string s=to_string(num),even,odd;for(char c:s)( (c-'0')%2?odd:even).push_back(c);
  sort(even.rbegin(),even.rend());sort(odd.rbegin(),odd.rend());int i=0,j=0;for(char&c:s)c=((c-'0')%2?odd[j++]:even[i++]);return stoi(s);
 }
};
```


## 2254. Design Video Sharing Platform

**Problem:** https://leetcode.com/problems/design-video-sharing-platform/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Hash Table, Design, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Stack / Queue

**Data structures (inferred):** Hash map, Hash map / hash set, Ordered map, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** upload O(L + log r) average; remove O(log r) average; watch O(w) average; like/dislike/getters O(1) average

**Space complexity:** O(V + r) total

**Complexity reasoning:** Hash map stores V total video characters; recycled IDs occupy a heap of size r. Upload copies L characters; watch copies w requested characters. Heap operations cost O(log r), with expected O(1) hash lookup.

### Problem description

You have a video sharing platform where users can upload and delete videos. Each video is a string of digits, where the i th digit of the string represents the content of the video at minute i . For example, the first digit represents the content at minute 0 in the video, the second digit represents the content at minute 1 in the video, and so on. Viewers of videos can also like and dislike videos. Internally, the platform keeps track of the number of views, likes, and dislikes on each video. 
 
 When a video is uploaded, it is associated with the smallest available integer videoId starting from 0 . Once a video is deleted, the videoId associated with that video can be reused for another video. 
 
 Implement the VideoSharingPlatform class: 

 VideoSharingPlatform() Initializes the object. 
 
 int upload(String video) The user uploads a video . Return the videoId associated with the video. 
 
 void remove(int videoId) If there is a video associated with videoId , remove the video. 
 
 String watch(int videoId, int startMinute, int endMinute) If there is a video associated with videoId , increase the number of views on the video by 1 and return the substring of the video string starting at startMinute and ending at min(endMinute, video.length - 1 ) ( inclusive ). Otherwise, return "-1" . 
 
 void like(int videoId) Increases the number of likes on the video associated with videoId by 1 if there is a video associated with videoId . 
 
 void dislike(int videoId) Increases the number of dislikes on the video associated with videoId by 1 if there is a video associated with videoId . 
 
 int[] getLikesAndDislikes(int videoId) Return a 0-indexed integer array values of length 2 where values[0] is the number of likes and values[1] is the number of dislikes on the video associated with videoId . If there is no video associated with videoId , return [-1] . 
 
 int getViews(int videoId) Return the number of views on the video associated with videoId , if there is no video associated with videoId , return -1 . 

 Example 1: 
 
```
Input

["VideoSharingPlatform", "upload", "upload", "remove", "remove", "upload", "watch", "watch", "like", "dislike", "dislike", "getLikesAndDislikes", "getViews"]
[[], ["123"], ["456"], [4], [0], ["789"], [1, 0, 5], [1, 0, 1], [1], [1], [1], [1], [1]]

Output

[null, 0, 1, null, null, 0, "456", "45", null, null, null, [1, 2], 2]

Explanation

VideoSharingPlatform videoSharingPlatform = new VideoSharingPlatform();
videoSharingPlatform.upload("123"); // The smallest available videoId is 0, so return 0.
videoSharingPlatform.upload("456"); // The smallest available 
videoId
 is 1, so return 1.
videoSharingPlatform.remove(4); // There is no video associated with videoId 4, so do nothing.
videoSharingPlatform.remove(0); // Remove the video associated with videoId 0.
videoSharingPlatform.upload("789"); // Since the video associated with videoId 0 was deleted,
 // 0 is the smallest available 
videoId
, so return 0.
videoSharingPlatform.watch(1, 0, 5); // The video associated with videoId 1 is "456".
 // The video from minute 0 to min(5, 3 - 1) = 2 is "456", so return "456".
videoSharingPlatform.watch(1, 0, 1); // The video associated with videoId 1 is "456".
 // The video from minute 0 to min(1, 3 - 1) = 1 is "45", so return "45".
videoSharingPlatform.like(1); // Increase the number of likes on the video associated with videoId 1.
videoSharingPlatform.dislike(1); // Increase the number of dislikes on the video associated with videoId 1.
videoSharingPlatform.dislike(1); // Increase the number of dislikes on the video associated with videoId 1.
videoSharingPlatform.getLikesAndDislikes(1); // There is 1 like and 2 dislikes on the video associated with videoId 1, so return [1, 2].
videoSharingPlatform.getViews(1); // The video associated with videoId 1 has 2 views, so return 2.
```

 Example 2: 
 
```
Input

["VideoSharingPlatform", "remove", "watch", "like", "dislike", "getLikesAndDislikes", "getViews"]
[[], [0], [0, 0, 1], [0], [0], [0], [0]]

Output

[null, null, "-1", null, null, [-1], -1]

Explanation

VideoSharingPlatform videoSharingPlatform = new VideoSharingPlatform();
videoSharingPlatform.remove(0); // There is no video associated with videoId 0, so do nothing.
videoSharingPlatform.watch(0, 0, 1); // There is no video associated with videoId 0, so return "-1".
videoSharingPlatform.like(0); // There is no video associated with videoId 0, so do nothing.
videoSharingPlatform.dislike(0); // There is no video associated with videoId 0, so do nothing.
videoSharingPlatform.getLikesAndDislikes(0); // There is no video associated with videoId 0, so return [-1].
videoSharingPlatform.getViews(0); // There is no video associated with videoId 0, so return -1.
```

 Constraints: 

 1 <= video.length <= 10 5 
 
 The sum of video.length over all calls to upload does not exceed 10 5 
 
 video consists of digits. 
 
 0 <= videoId <= 10 5 
 
 0 <= startMinute < endMinute < 10 5 
 
 startMinute < video.length 
 
 The sum of endMinute - startMinute over all calls to watch does not exceed 10 5 . 
 
 At most 10 5 calls in total will be made to all functions.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class VideoSharingPlatform {
    struct Video { string content; int likes = 0, dislikes = 0, views = 0; };
    unordered_map<int, Video> videos;
    priority_queue<int, vector<int>, greater<int>> available;
    int nextId = 0;
public:
    VideoSharingPlatform() {}
    int upload(string video) {
        int id;
        if (available.empty()) id = nextId++;
        else { id = available.top(); available.pop(); }
        videos[id] = Video{video, 0, 0, 0};
        return id;
    }
    void remove(int videoId) {
        if (videos.erase(videoId)) available.push(videoId);
    }
    string watch(int videoId, int startMinute, int endMinute) {
        auto it = videos.find(videoId);
        if (it == videos.end()) return "-1";
        ++it->second.views;
        if (startMinute >= (int)it->second.content.size()) return "";
        return it->second.content.substr(startMinute, endMinute - startMinute + 1);
    }
    void like(int videoId) { if (videos.count(videoId)) ++videos[videoId].likes; }
    void dislike(int videoId) { if (videos.count(videoId)) ++videos[videoId].dislikes; }
    vector<int> getLikesAndDislikes(int videoId) {
        if (!videos.count(videoId)) return {-1};
        return {videos[videoId].likes, videos[videoId].dislikes};
    }
    int getViews(int videoId) { return videos.count(videoId) ? videos[videoId].views : -1; }
};
```


## 2336. Smallest Number in Infinite Set

**Problem:** https://leetcode.com/problems/smallest-number-in-infinite-set/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, Design, Heap (Priority Queue), Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Stack / Queue

**Data structures (inferred):** Hash map / hash set, Ordered set, Priority queue / heap

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** popSmallest O(log r); addBack O(log r)

**Space complexity:** O(r)

**Complexity reasoning:** An ordered set holds r returned values below next; extracting or inserting an element costs logarithmic time. The direct next++ path is O(1).

### Problem description

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...] . 
 
 Implement the SmallestInfiniteSet class: 

 SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers. 
 
 int popSmallest() Removes and returns the smallest integer contained in the infinite set. 
 
 void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set. 

 Example 1: 
 
```
Input

["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]

Output

[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation

SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2); // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1); // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
 // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
```

 Constraints: 

 1 <= num <= 1000 
 
 At most 1000 calls will be made in total to popSmallest and addBack .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class SmallestInfiniteSet {
    int next = 1;
    set<int> returned;
public:
    SmallestInfiniteSet() {}
    int popSmallest() {
        if (!returned.empty()) { int x=*returned.begin(); returned.erase(returned.begin()); return x; }
        return next++;
    }
    void addBack(int num) { if (num < next) returned.insert(num); }
};
```


## 2342. Max Sum of a Pair With Equal Sum of Digits

**Problem:** https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n D) expected

**Space complexity:** O(u)

**Complexity reasoning:** For each of n integers, compute its digit sum in O(D) digits and update a hash map keyed by digit sum; u is the number of distinct sums.

### Problem description

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j , such that i != j , and the sum of digits of the number nums[i] is equal to that of nums[j] . 
 
 Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions. If no such pair of indices exists, return -1. 

 Example 1: 
 
```
Input:
 nums = [18,43,36,13,7]

Output:
 54

Explanation:
 The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
```

 Example 2: 
 
```
Input:
 nums = [10,12,19,14]

Output:
 -1

Explanation:
 There are no two numbers that satisfy the conditions, so we return -1.
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public:
    int maximumSum(vector<int>& nums) {
        unordered_map<int,int> best; int ans=-1;
        for(int x:nums){int d=0,t=x;while(t){d+=t%10;t/=10;}
            if(best.count(d)) ans=max(ans,x+best[d]);
            best[d]=max(best[d],x);
        }
        return ans;
    }
};
```


## 2343. Query Kth Smallest Trimmed Number

**Problem:** https://leetcode.com/problems/query-kth-smallest-trimmed-number/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Radix Sort, Quickselect

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue / heap, Sorted array, String, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n L + q)

**Space complexity:** O(n L + q)

**Complexity reasoning:** Stable bucket sorting each of L digit positions processes n indices with 10 buckets; store all L+1 index orders and answer q queries in O(1) each.

### Problem description

You are given a 0-indexed array of strings nums , where each string is of equal length and consists of only digits. 
 
 You are also given a 0-indexed 2D integer array queries where queries[i] = [k i , trim i ] . For each queries[i] , you need to: 

 Trim each number in nums to its rightmost trim i digits. 
 
 Determine the index of the k i th smallest trimmed number in nums . If two trimmed numbers are equal, the number with the lower index is considered to be smaller. 
 
 Reset each number in nums to its original length. 

 Return an array answer of the same length as queries , where answer[i] is the answer to the i th query. 
 
 Note : 

 To trim to the rightmost x digits means to keep removing the leftmost digit, until only x digits remain. 
 
 Strings in nums may contain leading zeros. 

 Example 1: 
 
```
Input:
 nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]

Output:
 [2,2,1,0]

Explanation:

1. After trimming to the last digit, nums = ["2","3","1","4"]. The smallest number is 1 at index 2.
2. Trimmed to the last 3 digits, nums is unchanged. The 2
nd
 smallest number is 251 at index 2.
3. Trimmed to the last 2 digits, nums = ["02","73","51","14"]. The 4
th
 smallest number is 73.
4. Trimmed to the last 2 digits, the smallest number is 2 at index 0.
 Note that the trimmed number "02" is evaluated as 2.
```

 Example 2: 
 
```
Input:
 nums = ["24","37","96","04"], queries = [[2,1],[2,2]]

Output:
 [3,0]

Explanation:

1. Trimmed to the last digit, nums = ["4","7","6","4"]. The 2
nd
 smallest number is 4 at index 3.
 There are two occurrences of 4, but the one at index 0 is considered smaller than the one at index 3.
2. Trimmed to the last 2 digits, nums is unchanged. The 2
nd
 smallest number is 24.
```

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i].length <= 100 
 
 nums[i] consists of only digits. 
 
 All nums[i].length are equal . 
 
 1 <= queries.length <= 100 
 
 queries[i].length == 2 
 
 1 <= k i <= nums.length 
 
 1 <= trim i <= nums[i].length 

 Follow up: Could you use the Radix Sort Algorithm to solve this problem? What will be the complexity of that solution?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public:
    vector<int> smallestTrimmedNumbers(vector<string>& nums, vector<vector<int>>& queries) {
        int n=nums.size(),L=nums[0].size();
        vector<vector<int>> order(L+1,vector<int>(n)); iota(order[0].begin(),order[0].end(),0);
        for(int len=1;len<=L;++len){
            vector<vector<int>> bucket(10);
            for(int idx:order[len-1]) bucket[nums[idx][L-len]-'0'].push_back(idx);
            int j=0;for(auto &b:bucket)for(int idx:b)order[len][j++]=idx;
        }
        vector<int> ans;for(auto &q:queries)ans.push_back(order[q[1]][q[0]-1]);return ans;
    }
};
```


## 2344. Minimum Deletions to Make Array Divisible

**Problem:** https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Math, Sorting, Heap (Priority Queue), Number Theory, Euclidean Algorithm, Greatest Common Divisor

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Math / Number Theory, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(m log A + n log n)

**Space complexity:** O(log n) auxiliary

**Complexity reasoning:** Compute gcd of m divisor values (A bounds their magnitudes), sort n candidate values, then scan for the first divisor. Sorting is in-place aside from recursion stack.

### Problem description

You are given two positive integer arrays nums and numsDivide . You can delete any number of elements from nums . 
 
 Return the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide . If this is not possible, return -1 . 
 
 Note that an integer x divides y if y % x == 0 . 

 Example 1: 
 
```
Input:
 nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]

Output:
 2

Explanation:
 
The smallest element in [2,3,2,4,3] is 2, which does not divide all the elements of numsDivide.
We use 2 deletions to delete the elements in nums that are equal to 2 which makes nums = [3,4,3].
The smallest element in [3,4,3] is 3, which divides all the elements of numsDivide.
It can be shown that 2 is the minimum number of deletions needed.
```

 Example 2: 
 
```
Input:
 nums = [4,3,6], numsDivide = [8,2,6,10]

Output:
 -1

Explanation:
 
We want the smallest element in nums to divide all the elements of numsDivide.
There is no way to delete elements from nums to allow this.
```

 Constraints: 

 1 <= nums.length, numsDivide.length <= 10 5 
 
 1 <= nums[i], numsDivide[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public:
    int minOperations(vector<int>& nums, vector<int>& numsDivide) {
        int g=0;for(int x:numsDivide)g=__gcd(g,x);
        sort(nums.begin(),nums.end());
        for(int i=0;i<(int)nums.size();++i)if(g%nums[i]==0)return i;
        return -1;
    }
};
```


## 2349. Design a Number Container System

**Problem:** https://leetcode.com/problems/design-a-number-container-system/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, Design, Heap (Priority Queue), Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Stack / Queue

**Data structures (inferred):** Hash map, Hash map / hash set, Ordered map, Ordered set, Priority queue / heap

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** change O(log n) average; find O(1) average

**Space complexity:** O(n) total

**Complexity reasoning:** Hash maps locate old/new assignments in expected constant time; balanced sets insert/erase indices in O(log n). find reads the smallest index from a set.

### Problem description

Design a number container system that can do the following: 

 Insert or Replace a number at the given index in the system. 
 
 Return the smallest index for the given number in the system. 

 Implement the NumberContainers class: 

 NumberContainers() Initializes the number container system. 
 
 void change(int index, int number) Fills the container at index with the number . If there is already a number at that index , replace it. 
 
 int find(int number) Returns the smallest index for the given number , or -1 if there is no index that is filled by number in the system. 

 Example 1: 
 
```
Input

["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]

Output

[null, -1, null, null, null, null, 1, null, 2]

Explanation

NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
```

 Constraints: 

 1 <= index, number <= 10 9 
 
 At most 10 5 calls will be made in total to change and find .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class NumberContainers {
    unordered_map<int,int> at;
    unordered_map<int,set<int>> indices;
public:
    NumberContainers() {}
    void change(int index,int number) {
        auto it=at.find(index);
        if(it!=at.end()) indices[it->second].erase(index);
        at[index]=number;indices[number].insert(index);
    }
    int find(int number) {
        auto it=indices.find(number);
        return it==indices.end()||it->second.empty()?-1:*it->second.begin();
    }
};
```


## 2353. Design a Food Rating System

**Problem:** https://leetcode.com/problems/design-a-food-rating-system/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, String, Design, Heap (Priority Queue), Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, Ordered set, Priority queue / heap, String, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** constructor O(n log n * L); changeRating O(log n * L); highestRated O(L) average

**Space complexity:** O(n L) total

**Complexity reasoning:** Per-cuisine balanced sets rank n foods, with string comparisons/copies up to L characters; updates erase and reinsert, while highestRated returns a copied food name.

### Problem description

Design a food rating system that can do the following: 

 Modify the rating of a food item listed in the system. 
 
 Return the highest-rated food item for a type of cuisine in the system. 

 Implement the FoodRatings class: 

 FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods , cuisines and ratings , all of which have a length of n .

 foods[i] is the name of the i th food, 
 
 cuisines[i] is the type of cuisine of the i th food, and 
 
 ratings[i] is the initial rating of the i th food. 

 void changeRating(String food, int newRating) Changes the rating of the food item with the name food . 
 
 String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine . If there is a tie, return the item with the lexicographically smaller name. 

 Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y , or if i is the first position such that x[i] != y[i] , then x[i] comes before y[i] in alphabetic order. 

 Example 1: 
 
```
Input

["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]

Output

[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation

FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
 // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
 // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
 // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
 // Both "sushi" and "ramen" have a rating of 16.
 // However, "ramen" is lexicographically smaller than "sushi".
```

 Constraints: 

 1 <= n <= 2 * 10 4 
 
 n == foods.length == cuisines.length == ratings.length 
 
 1 <= foods[i].length, cuisines[i].length <= 10 
 
 foods[i] , cuisines[i] consist of lowercase English letters. 
 
 1 <= ratings[i] <= 10 8 
 
 All the strings in foods are distinct . 
 
 food will be the name of a food item in the system across all calls to changeRating . 
 
 cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated . 
 
 At most 2 * 10 4 calls in total will be made to changeRating and highestRated .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class FoodRatings 
{
private:
    struct compare
	{
        bool operator() (const pair<int, string>& a, const pair<int, string>& b) const 
		{
            if (a.first == b.first) return (a.second < b.second);
            return (a.first > b.first);
        }
    };
    
    unordered_map<string, set<pair<int, string>, compare>> rank;
    unordered_map<string, string> food2cuisine;
    unordered_map<string, int> food2rating;
	
public:

    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) 
	{
        int n = foods.size();
        for (int i = 0; i < n; i++) 
		{
            rank[cuisines[i]].insert({ratings[i], foods[i]});
            food2cuisine[foods[i]] = cuisines[i];
            food2rating[foods[i]] = ratings[i];
        }
    }
    
    void changeRating(string food, int newRating) 
	{
        auto& cuisine = food2cuisine[food];
        rank[cuisine].erase({food2rating[food], food});
        rank[cuisine].insert({newRating, food});
        food2rating[food] = newRating;
    }
    
  
    string highestRated(string cuisine) 
	{
        return (rank[cuisine].begin())->second;
    }

};
```


## 2386. Find the K-Sum of an Array

**Problem:** https://leetcode.com/problems/find-the-k-sum-of-an-array/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n + k log k)

**Space complexity:** O(n + k)

**Complexity reasoning:** Sort n absolute values and enumerate k smallest subset losses using a heap with at most O(k) states. Assumes nonempty nums.

### Problem description

You are given an integer array nums and a positive integer k . You can choose any subsequence of the array and sum all of its elements together. 
 
 We define the K-Sum of the array as the k th largest subsequence sum that can be obtained ( not necessarily distinct). 
 
 Return the K-Sum of the array . 
 
 A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements. 
 
 Note that the empty subsequence is considered to have a sum of 0 . 

 Example 1: 
 
```
Input:
 nums = [2,4,-2], k = 5

Output:
 2

Explanation:
 All the possible subsequence sums that we can obtain are the following sorted in decreasing order:
6, 4, 4, 2, 
2
, 0, 0, -2.
The 5-Sum of the array is 2.
```

 Example 2: 
 
```
Input:
 nums = [1,-2,3,4,-10,12], k = 16

Output:
 10

Explanation:
 The 16-Sum of the array is 10.
```

 Constraints: 

 n == nums.length 
 
 1 <= n <= 10 5 
 
 -10 9 <= nums[i] <= 10 9 
 
 1 <= k <= min(2000, 2 n )

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public: long long kSum(vector<int>& nums,int k){long long base=0;vector<long long>a;for(int x:nums){if(x>0)base+=x;a.push_back(llabs((long long)x));}sort(a.begin(),a.end());priority_queue<pair<long long,int>,vector<pair<long long,int>>,greater<pair<long long,int>>>pq;pq.push({a[0],0});long long loss=0;for(int i=1;i<k;i++){auto p=pq.top();pq.pop();loss=p.first;int j=p.second;if(j+1<(int)a.size()){pq.push({loss+a[j+1],j+1});pq.push({loss-a[j]+a[j+1],j+1});}}return base-loss;}};
```


## 2402. Meeting Rooms III

**Problem:** https://leetcode.com/problems/meeting-rooms-iii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, Sorting, Heap (Priority Queue), Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(m log m + (m+n) log n)

**Space complexity:** O(m + n) auxiliary

**Complexity reasoning:** Sort m meetings; each room enters/leaves the free and busy heaps at most O(m+n) times, with heap sizes bounded by n.

### Problem description

You are given an integer n . There are n rooms numbered from 0 to n - 1 . 
 
 You are given a 2D integer array meetings where meetings[i] = [start i , end i ] means that a meeting will be held during the half-closed time interval [start i , end i ) . All the values of start i are unique . 
 
 Meetings are allocated to rooms in the following manner: 

 Each meeting will take place in the unused room with the lowest number. 
 
 If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting. 
 
 When a room becomes unused, meetings that have an earlier original start time should be given the room. 

 Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number. 
 
 A half-closed interval [a, b) is the interval between a and b including a and not including b . 

 Example 1: 
 
```
Input:
 n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]

Output:
 0

Explanation:

- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0.
```

 Example 2: 
 
```
Input:
 n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]

Output:
 1

Explanation:

- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1.
```

 Constraints: 

 1 <= n <= 100 
 
 1 <= meetings.length <= 10 5 
 
 meetings[i].length == 2 
 
 0 <= start i < end i <= 5 * 10 5 
 
 All the values of start i are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int mostBooked(int n,vector<vector<int>>& meetings){sort(meetings.begin(),meetings.end());priority_queue<int,vector<int>,greater<int>>free;for(int i=0;i<n;i++)free.push(i);using P=pair<long long,int>;priority_queue<P,vector<P>,greater<P>>busy;vector<int>count(n);for(auto&m:meetings){long long start=m[0],dur=m[1]-m[0];while(!busy.empty()&&busy.top().first<=start){free.push(busy.top().second);busy.pop();}int room;long long end;if(!free.empty()){room=free.top();free.pop();end=start+dur;}else{auto p=busy.top();busy.pop();room=p.second;end=p.first+dur;}busy.push({end,room});count[room]++;}return max_element(count.begin(),count.end())-count.begin();}};
```


## 2456. Most Popular Video Creator

**Problem:** https://leetcode.com/problems/most-popular-video-creator/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, String, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, Priority queue / heap, Sorted array, String, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n L) expected

**Space complexity:** O(n L)

**Complexity reasoning:** Process n creator/ID strings through hash maps, copying and hashing strings of length at most L; final scans visit distinct creators.

### Problem description

You are given two string arrays creators and ids , and an integer array views , all of length n . The i th video on a platform was created by creators[i] , has an id of ids[i] , and has views[i] views. 
 
 The popularity of a creator is the sum of the number of views on all of the creator's videos. Find the creator with the highest popularity and the id of their most viewed video. 

 If multiple creators have the highest popularity, find all of them. 
 
 If multiple videos have the highest view count for a creator, find the lexicographically smallest id. 

 Note: It is possible for different videos to have the same id , meaning that id s do not uniquely identify a video. For example, two videos with the same ID are considered as distinct videos with their own viewcount. 
 
 Return a 2D array of strings answer where answer[i] = [creators i , id i ] means that creators i has the highest popularity and id i is the id of their most popular video. The answer can be returned in any order. 

 Example 1: 

 Input: creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4] 
 
 Output: [["alice","one"],["bob","two"]] 
 
 Explanation: 
 
 The popularity of alice is 5 + 5 = 10. 
The popularity of bob is 10. 
The popularity of chris is 4. 
alice and bob are the most popular creators. 
For bob, the video with the highest view count is "two". 
For alice, the videos with the highest view count are "one" and "three". Since "one" is lexicographically smaller than "three", it is included in the answer. 

 Example 2: 

 Input: creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2] 
 
 Output: [["alice","b"]] 
 
 Explanation: 
 
 The videos with id "b" and "c" have the highest view count. 
Since "b" is lexicographically smaller than "c", it is included in the answer. 

 Constraints: 

 n == creators.length == ids.length == views.length 
 
 1 <= n <= 10 5 
 
 1 <= creators[i].length, ids[i].length <= 5 
 
 creators[i] and ids[i] consist only of lowercase English letters. 
 
 0 <= views[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: vector<vector<string>> mostPopularCreator(vector<string>& creators,vector<string>& ids,vector<int>& views){unordered_map<string,long long> total;unordered_map<string,pair<int,string>> best;for(int i=0;i<(int)views.size();++i){string c=creators[i];total[c]+=views[i];if(!best.count(c)||views[i]>best[c].first||(views[i]==best[c].first&&ids[i]<best[c].second))best[c]={views[i],ids[i]};}long long mx=0;for(auto &p:total)mx=max(mx,p.second);vector<vector<string>>ans;for(auto &p:total)if(p.second==mx)ans.push_back({p.first,best[p.first].second});return ans;} };
```


## 2500. Delete Greatest Value in Each Row

**Problem:** https://leetcode.com/problems/delete-greatest-value-in-each-row/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting, Heap (Priority Queue), Matrix, Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(r c log c)

**Space complexity:** O(log c) auxiliary

**Complexity reasoning:** Sort each of r rows of c values and scan all r*c cells column by column; std::sort uses O(log c) stack.

### Problem description

You are given an m x n matrix grid consisting of positive integers. 
 
 Perform the following operation until grid becomes empty: 

 Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them. 
 
 Add the maximum of deleted elements to the answer. 

 Note that the number of columns decreases by one after each operation. 
 
 Return the answer after performing the operations described above . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/10/19/q1ex1.jpg] 
 
```
Input:
 grid = [[1,2,4],[3,3,1]]

Output:
 8

Explanation:
 The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/10/19/q1ex2.jpg] 
 
```
Input:
 grid = [[10]]

Output:
 10

Explanation:
 The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.
```

 Constraints: 

 m == grid.length 
 
 n == grid[i].length 
 
 1 <= m, n <= 50 
 
 1 <= grid[i][j] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int deleteGreatestValue(vector<vector<int>>& grid){for(auto&r:grid)sort(r.begin(),r.end());int ans=0;for(int j=0;j<(int)grid[0].size();j++){int mx=0;for(auto&r:grid)mx=max(mx,r[j]);ans+=mx;}return ans;}};
```


## 2512. Reward Top K Students

**Problem:** https://leetcode.com/problems/reward-top-k-students/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, String, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Hash set, Ordered set, Priority queue / heap, Sorted array, String, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(W + n log n) expected

**Space complexity:** O(W + n)

**Complexity reasoning:** Hash W feedback-word characters, tokenize and score reports totaling W characters, and sort n student scores. Hash lookup is expected O(1) per word excluding hashing cost.

### Problem description

You are given two string arrays positive_feedback and negative_feedback , containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative. 
 
 Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3 , whereas each negative word decreases the points by 1 . 
 
 You are given n feedback reports, represented by a 0-indexed string array report  and a 0-indexed integer array student_id , where student_id[i] represents the ID of the student who has received the feedback report report[i] . The ID of each student is unique . 
 
 Given an integer k , return the top k students after ranking them in non-increasing order by their points . In case more than one student has the same points, the one with the lower ID ranks higher. 

 Example 1: 
 
```
Input:
 positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2

Output:
 [1,2]

Explanation:
 
Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.
```

 Example 2: 
 
```
Input:
 positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2

Output:
 [2,1]

Explanation:
 
- The student with ID 1 has 1 positive feedback and 1 negative feedback, so he has 3-1=2 points. 
- The student with ID 2 has 1 positive feedback, so he has 3 points. 
Since student 2 has more points, [2,1] is returned.
```

 Constraints: 

 1 <= positive_feedback.length, negative_feedback.length <= 10 4 
 
 1 <= positive_feedback[i].length, negative_feedback[j].length <= 100 
 
 Both positive_feedback[i] and negative_feedback[j] consists of lowercase English letters. 
 
 No word is present in both positive_feedback and negative_feedback . 
 
 n == report.length == student_id.length 
 
 1 <= n <= 10 4 
 
 report[i] consists of lowercase English letters and spaces ' ' . 
 
 There is a single space between consecutive words of report[i] . 
 
 1 <= report[i].length <= 100 
 
 1 <= student_id[i] <= 10 9 
 
 All the values of student_id[i] are unique . 
 
 1 <= k <= n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int> topStudents(vector<string>& positive_feedback,vector<string>& negative_feedback,vector<string>& report,vector<int>& student_id,int k){unordered_set<string>pos(positive_feedback.begin(),positive_feedback.end()),neg(negative_feedback.begin(),negative_feedback.end());vector<pair<int,int>>v;for(int i=0;i<(int)report.size();i++){istringstream ss(report[i]);string w;int score=0;while(ss>>w){if(pos.count(w))score+=3;if(neg.count(w))score--;}v.push_back({-score,student_id[i]});}sort(v.begin(),v.end());vector<int>ans;for(int i=0;i<k;i++)ans.push_back(v[i].second);return ans;}};
```


## 2532. Time to Cross a Bridge

**Problem:** https://leetcode.com/problems/time-to-cross-a-bridge/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Heap (Priority Queue), Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O((n+k) log k)

**Space complexity:** O(k)

**Complexity reasoning:** Each of n boxes crosses in at most two bridge moves, and worker transitions use four heaps holding at most k workers; each heap operation is O(log k).

### Problem description

There are k workers who want to move n boxes from the right (old) warehouse to the left (new) warehouse. You are given the two integers n and k , and a 2D integer array time of size k x 4 where time[i] = [right i , pick i , left i , put i ] . 
 
 The warehouses are separated by a river and connected by a bridge. Initially, all k workers are waiting on the left side of the bridge. To move the boxes, the i th worker can do the following: 

 Cross the bridge to the right side in right i minutes. 
 
 Pick a box from the right warehouse in pick i minutes. 
 
 Cross the bridge to the left side in left i minutes. 
 
 Put the box into the left warehouse in put i minutes. 

 The i th worker is less efficient than the j th worker if either condition is met: 

 left i + right i > left j + right j 
 
 left i + right i == left j + right j and i > j 

 The following rules regulate the movement of the workers through the bridge: 

 Only one worker can use the bridge at a time. 
 
 When the bridge is unused prioritize the least efficient worker (who have picked up the box) on the right side to cross. If not, prioritize the least efficient worker on the left side to cross. 
 
 If enough workers have already been dispatched from the left side to pick up all the remaining boxes, no more workers will be sent from the left side. 

 Return the elapsed minutes at which the last box reaches the left side of the bridge . 

 Example 1: 

 Input: n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]] 
 
 Output: 6 
 
 Explanation: 
 
```
From 0 to 1 minutes: worker 2 crosses the bridge to the right.
From 1 to 2 minutes: worker 2 picks up a box from the right warehouse.
From 2 to 6 minutes: worker 2 crosses the bridge to the left.
From 6 to 7 minutes: worker 2 puts a box at the left warehouse.
The whole process ends after 7 minutes. We return 6 because the problem asks for the instance of time at which the last worker reaches the left side of the bridge.
```

 Example 2: 

 Input: n = 3, k = 2, time = [[1,5,1,8],[10,10,10,10]] 
 
 Output: 37 
 
 Explanation: 
 
```

```

 The last box reaches the left side at 37 seconds. Notice, how we do not put the last boxes down, as that would take more time, and they are already on the left with the workers. 

 Constraints: 

 1 <= n, k <= 10 4 
 
 time.length == k 
 
 time[i].length == 4 
 
 1 <= left i , pick i , right i , put i <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 int findCrossingTime(int n,int k,vector<vector<int>>& time){
  using P=pair<int,int>;
  priority_queue<P> left,right;
  priority_queue<P,vector<P>,greater<P>> pick,put;
  for(int i=0;i<k;++i)left.push({time[i][0]+time[i][2],i});
  long long t=0;int remaining=n;
  while(remaining>0||!right.empty()||!pick.empty()){
   while(!pick.empty()&&pick.top().first<=t){int i=pick.top().second;pick.pop();right.push({time[i][0]+time[i][2],i});}
   while(!put.empty()&&put.top().first<=t){int i=put.top().second;put.pop();left.push({time[i][0]+time[i][2],i});}
   if(!right.empty()){
    int i=right.top().second;right.pop();t+=time[i][2];put.push({t+time[i][3],i});
   }else if(remaining>0&&!left.empty()){
    int i=left.top().second;left.pop();t+=time[i][0];--remaining;pick.push({t+time[i][1],i});
   }else{
    long long next=LLONG_MAX;
    if(!pick.empty())next=min(next,(long long)pick.top().first);
    if(!put.empty())next=min(next,(long long)put.top().first);
    if(next==LLONG_MAX)break;t=next;
   }
  }
  // The final bridge crossing completes before the worker puts down the box.
  return (int)t;
 }
};
```


## 2558. Take Gifts From the Richest Pile

**Problem:** https://leetcode.com/problems/take-gifts-from-the-richest-pile/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Heap (Priority Queue), Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + k log n)

**Space complexity:** O(n)

**Complexity reasoning:** Build a max-heap of n gifts, perform k pop/push updates, then drain n values to sum them.

### Problem description

You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following: 

 Choose the pile with the maximum number of gifts. 
 
 If there is more than one pile with the maximum number of gifts, choose any. 
 
 Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile. 

 Return the number of gifts remaining after k seconds. 

 Example 1: 
 
```
Input:
 gifts = [25,64,9,4,100], k = 4

Output:
 29

Explanation:
 
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.
```

 Example 2: 
 
```
Input:
 gifts = [1,1,1,1], k = 4

Output:
 4

Explanation:
 
In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile. 
That is, you can't take any pile with you. 
So, the total gifts remaining are 4.
```

 Constraints: 

 1 <= gifts.length <= 10 3 
 
 1 <= gifts[i] <= 10 9 
 
 1 <= k <= 10 3

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 long long pickGifts(vector<int>& gifts,int k){
  priority_queue<int> pq(gifts.begin(),gifts.end());
  while(k--){int x=pq.top();pq.pop();pq.push((int)sqrt(x));}
  long long ans=0;while(!pq.empty()){ans+=pq.top();pq.pop();}return ans;
 }
};
```


## 2593. Find Score of an Array After Marking All Elements

**Problem:** https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Sorting, Heap (Priority Queue), Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Sort n (value,index) pairs, then scan once while marking each selected index and its neighbors.

### Problem description

You are given an array nums consisting of positive integers. 
 
 Starting with score = 0 , apply the following algorithm: 

 Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index. 
 
 Add the value of the chosen integer to score . 
 
 Mark the chosen element and its two adjacent elements if they exist . 
 
 Repeat until all the array elements are marked. 

 Return the score you get after applying the above algorithm . 

 Example 1: 
 
```
Input:
 nums = [2,1,3,4,5,2]

Output:
 7

Explanation:
 We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [
2
,
1
,
3
,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [
2
,
1
,
3
,4,
5
,
2
].
- 4 is the only remaining unmarked element, so we mark it: [
2
,
1
,
3
,
4
,
5
,
2
].
Our score is 1 + 2 + 4 = 7.
```

 Example 2: 
 
```
Input:
 nums = [2,3,5,1,3,2]

Output:
 5

Explanation:
 We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,
5
,
1
,
3
,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [
2
,
3
,
5
,
1
,
3
,2].
- 2 is the only remaining unmarked element, so we mark it: [
2
,
3
,
5
,
1
,
3
,
2
].
Our score is 1 + 2 + 2 = 5.
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:long long findScore(vector<int>& nums){int n=nums.size();vector<pair<int,int>> order;for(int i=0;i<n;i++)order.push_back({nums[i],i});sort(order.begin(),order.end());vector<char> used(n);long long ans=0;for(auto &p:order){int i=p.second;if(used[i])continue;ans+=p.first;used[i]=1;if(i)used[i-1]=1;if(i+1<n)used[i+1]=1;}return ans;}};
```


## 2679. Sum in a Matrix

**Problem:** https://leetcode.com/problems/sum-in-a-matrix/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Heap (Priority Queue), Matrix, Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(r c log c)

**Space complexity:** O(log c) auxiliary

**Complexity reasoning:** Sort each of r rows containing c elements and scan all r*c entries to accumulate column maxima.

### Problem description

You are given a 0-indexed 2D integer array nums . Initially, your score is 0 . Perform the following operations until the matrix becomes empty: 

 From each row in the matrix, select the largest number and remove it. In the case of a tie, it does not matter which number is chosen. 
 
 Identify the highest number amongst all those removed in step 1. Add that number to your score . 

 Return the final score . 

 Example 1: 
 
```
Input:
 nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]

Output:
 15

Explanation:
 In the first operation, we remove 7, 6, 6, and 3. We then add 7 to our score. Next, we remove 2, 4, 5, and 2. We add 5 to our score. Lastly, we remove 1, 2, 3, and 1. We add 3 to our score. Thus, our final score is 7 + 5 + 3 = 15.
```

 Example 2: 
 
```
Input:
 nums = [[1]]

Output:
 1

Explanation:
 We remove 1 and add it to the answer. We return 1.
```

 Constraints: 

 1 <= nums.length <= 300 
 
 1 <= nums[i].length <= 500 
 
 0 <= nums[i][j] <= 10 3

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int matrixSum(vector<vector<int>>&nums){for(auto&r:nums)sort(r.begin(),r.end());int ans=0;for(int j=0;j<(int)nums[0].size();j++){int mx=0;for(auto&r:nums)mx=max(mx,r[j]);ans+=mx;}return ans;}};
```


## 2974. Minimum Number Game

**Problem:** https://leetcode.com/problems/minimum-number-game/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Sorting, Heap (Priority Queue), Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(log n) auxiliary

**Complexity reasoning:** Sort n values in place and swap each adjacent pair; std::sort uses logarithmic recursion stack.

### Problem description

You are given a 0-indexed integer array nums of even length and there is also an empty array arr . Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows: 

 Every round, first Alice will remove the minimum element from nums , and then Bob does the same. 
 
 Now, first Bob will append the removed element in the array arr , and then Alice does the same. 
 
 The game continues until nums becomes empty. 

 Return the resulting array arr . 

 Example 1: 
 
```
Input:
 nums = [5,4,2,3]

Output:
 [3,2,5,4]

Explanation:
 In round one, first Alice removes 2 and then Bob removes 3. Then in arr firstly Bob appends 3 and then Alice appends 2. So arr = [3,2].
At the begining of round two, nums = [5,4]. Now, first Alice removes 4 and then Bob removes 5. Then both append in arr which becomes [3,2,5,4].
```

 Example 2: 
 
```
Input:
 nums = [2,5]

Output:
 [5,2]

Explanation:
 In round one, first Alice removes 2 and then Bob removes 5. Then in arr firstly Bob appends and then Alice appends. So arr = [5,2].
```

 Constraints: 

 2 <= nums.length <= 100 
 
 1 <= nums[i] <= 100 
 
 nums.length % 2 == 0

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int> numberGame(vector<int>& nums){sort(nums.begin(),nums.end());for(int i=0;i<(int)nums.size();i+=2)swap(nums[i],nums[i+1]);return nums;}};
```


## 3066. Minimum Operations to Exceed Threshold Value II

**Problem:** https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Heap (Priority Queue), Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + t log n)

**Space complexity:** O(n)

**Complexity reasoning:** Heapify n values and perform t merge operations, each removing two minima and inserting one new value; t <= n-1.

### Problem description

You are given a 0-indexed integer array nums , and an integer k . 
 
 You are allowed to perform some operations on nums , where in a single operation, you can: 

 Select the two smallest integers x and y from nums . 
 
 Remove x and y from nums . 
 
 Insert (min(x, y) * 2 + max(x, y)) at any position in the array. 

 Note that you can only apply the described operation if nums contains at least two elements. 
 
 Return the minimum number of operations needed so that all elements of the array are greater than or equal to k . 

 Example 1: 

 Input: nums = [2,11,10,1,3], k = 10 
 
 Output: 2 
 
 Explanation: 

 In the first operation, we remove elements 1 and 2, then add 1 * 2 + 2 to nums . nums becomes equal to [4, 11, 10, 3] . 
 
 In the second operation, we remove elements 3 and 4, then add 3 * 2 + 4 to nums . nums becomes equal to [10, 11, 10] . 

 At this stage, all the elements of nums are greater than or equal to 10 so we can stop.  
 
 It can be shown that 2 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10. 

 Example 2: 

 Input: nums = [1,1,2,4,9], k = 20 
 
 Output: 4 
 
 Explanation: 

 After one operation, nums becomes equal to [2, 4, 9, 3] .  
 
 After two operations, nums becomes equal to [7, 4, 9] .  
 
 After three operations, nums becomes equal to [15, 9] .  
 
 After four operations, nums becomes equal to [33] . 

 At this stage, all the elements of nums are greater than 20 so we can stop.  
 
 It can be shown that 4 is the minimum number of operations needed so that all elements of the array are greater than or equal to 20. 

 Constraints: 

 2 <= nums.length <= 2 * 10 5 
 
 1 <= nums[i] <= 10 9 
 
 1 <= k <= 10 9 
 
 The input is generated such that an answer always exists. That is, after performing some number of operations, all elements of the array are greater than or equal to k .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int minOperations(vector<int>&nums,int k){priority_queue<long long,vector<long long>,greater<long long>>pq(nums.begin(),nums.end());int ans=0;while(pq.top()<k){long long x=pq.top();pq.pop();long long y=pq.top();pq.pop();pq.push(2*x+y);ans++;}return ans;}};
```


## 3080. Mark Elements on Array by Performing Queries

**Problem:** https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Sorting, Heap (Priority Queue), Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n + q log n)

**Space complexity:** O(n + q)

**Complexity reasoning:** Build a heap of n (value,index) pairs; each entry is popped at most once across q queries, and every query also performs constant bookkeeping.

### Problem description

You are given a 0-indexed array nums of size n consisting of positive integers. 
 
 You are also given a 2D array queries of size m where queries[i] = [index i , k i ] . 
 
 Initially all elements of the array are unmarked . 
 
 You need to apply m queries on the array in order, where on the i th query you do the following: 

 Mark the element at index index i if it is not already marked. 
 
 Then mark k i unmarked elements in the array with the smallest values. If multiple such elements exist, mark the ones with the smallest indices. And if less than k i unmarked elements exist, then mark all of them. 

 Return an array answer of size m where answer[i] is the sum of unmarked elements in the array after the i th query . 

 Example 1: 

 Input: nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]] 
 
 Output: [8,3,0] 
 
 Explanation: 
 
 We do the following queries on the array: 

 Mark the element at index 1 , and 2 of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are nums = [ 1 , 2 ,2, 1 ,2,3,1] . The sum of unmarked elements is 2 + 2 + 3 + 1 = 8 . 
 
 Mark the element at index 3 , since it is already marked we skip it. Then we mark 3 of the smallest unmarked elements with the smallest indices, the marked elements now are nums = [ 1 , 2 , 2 , 1 , 2 ,3, 1 ] . The sum of unmarked elements is 3 . 
 
 Mark the element at index 4 , since it is already marked we skip it. Then we mark 2 of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are nums = [ 1 , 2 , 2 , 1 , 2 , 3 , 1 ] . The sum of unmarked elements is 0 . 

 Example 2: 

 Input: nums = [1,4,2,3], queries = [[0,1]] 
 
 Output: [7] 
 
 Explanation: We do one query which is mark the element at index 0 and mark the smallest element among unmarked elements. The marked elements will be nums = [ 1 ,4, 2 ,3] , and the sum of unmarked elements is 4 + 3 = 7 . 

 Constraints: 

 n == nums.length 
 
 m == queries.length 
 
 1 <= m <= n <= 10 5 
 
 1 <= nums[i] <= 10 5 
 
 queries[i].length == 2 
 
 0 <= index i , k i <= n - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<long long> unmarkedSumArray(vector<int>& nums,vector<vector<int>>& queries){
 int n=nums.size();long long sum=accumulate(nums.begin(),nums.end(),0LL);
 priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
 for(int i=0;i<n;i++)pq.push({nums[i],i});vector<char> marked(n);vector<long long> ans;
 for(auto &q:queries){int i=q[0],k=q[1];if(!marked[i]){marked[i]=1;sum-=nums[i];}
 while(k&&!pq.empty()){auto p=pq.top();pq.pop();if(marked[p.second])continue;marked[p.second]=1;sum-=p.first;--k;}ans.push_back(sum);}return ans;
}};
```


## 3092. Most Frequent IDs

**Problem:** https://leetcode.com/problems/most-frequent-ids/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Heap (Priority Queue), Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, Ordered set, Priority queue / heap, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n) total

**Space complexity:** O(n)

**Complexity reasoning:** For each of n updates, erase and insert frequencies in a multiset (O(log n)); hash map lookup is expected O(1), and output stores n maxima.

### Problem description

The problem involves tracking the frequency of IDs in a collection that changes over time. You have two integer arrays, nums and freq , of equal length n . Each element in nums represents an ID, and the corresponding element in freq indicates how many times that ID should be added to or removed from the collection at each step. 

 Addition of IDs: If freq[i] is positive, it means freq[i] IDs with the value nums[i] are added to the collection at step i . 
 
 Removal of IDs: If freq[i] is negative, it means -freq[i] IDs with the value nums[i] are removed from the collection at step i . 

 Return an array ans of length n , where ans[i] represents the count of the most frequent ID in the collection after the i th  step. If the collection is empty at any step, ans[i] should be 0 for that step. 

 Example 1: 

 Input: nums = [2,3,2,1], freq = [3,2,-3,1] 
 
 Output: [3,3,2,2] 
 
 Explanation: 
 
 After step 0, we have 3 IDs with the value of 2. So ans[0] = 3 . 
After step 1, we have 3 IDs with the value of 2 and 2 IDs with the value of 3. So ans[1] = 3 . 
After step 2, we have 2 IDs with the value of 3. So ans[2] = 2 . 
After step 3, we have 2 IDs with the value of 3 and 1 ID with the value of 1. So ans[3] = 2 . 

 Example 2: 

 Input: nums = [5,5,3], freq = [2,-2,1] 
 
 Output: [2,0,1] 
 
 Explanation: 
 
 After step 0, we have 2 IDs with the value of 5. So ans[0] = 2 . 
After step 1, there are no IDs. So ans[1] = 0 . 
After step 2, we have 1 ID with the value of 3. So ans[2] = 1 . 

 Constraints: 

 1 <= nums.length == freq.length <= 10 5 
 
 1 <= nums[i] <= 10 5 
 
 -10 5 <= freq[i] <= 10 5 
 
 freq[i] != 0 
 
 The input is generated such that the occurrences of an ID will not be negative in any step.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<long long> mostFrequentIDs(vector<int>& nums,vector<int>& freq){
 unordered_map<int,long long> f;multiset<long long> ms;vector<long long> ans;
 for(int i=0;i<(int)nums.size();i++){long long old=f[nums[i]];if(old>0)ms.erase(ms.find(old));long long now=f[nums[i]]+=freq[i];if(now>0)ms.insert(now);ans.push_back(ms.empty()?0:*ms.rbegin());}return ans;
}};
```


## 3264. Final Array State After K Multiplication Operations I

**Problem:** https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Math, Heap (Priority Queue), Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue / heap, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(k n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Each of k operations scans the n-element array with min_element and multiplies the chosen minimum in place.

### Problem description

You are given an integer array nums , an integer k , and an integer multiplier . 
 
 You need to perform k operations on nums . In each operation: 

 Find the minimum value x in nums . If there are multiple occurrences of the minimum value, select the one that appears first . 
 
 Replace the selected minimum value x with x * multiplier . 

 Return an integer array denoting the final state of nums after performing all k operations. 

 Example 1: 

 Input: nums = [2,1,3,5,6], k = 5, multiplier = 2 
 
 Output: [8,4,6,5,6] 
 
 Explanation: 

 Operation 
 Result 

 After operation 1 
 [2, 2, 3, 5, 6] 

 After operation 2 
 [4, 2, 3, 5, 6] 

 After operation 3 
 [4, 4, 3, 5, 6] 

 After operation 4 
 [4, 4, 6, 5, 6] 

 After operation 5 
 [8, 4, 6, 5, 6] 

 Example 2: 

 Input: nums = [1,2], k = 3, multiplier = 4 
 
 Output: [16,8] 
 
 Explanation: 

 Operation 
 Result 

 After operation 1 
 [4, 2] 

 After operation 2 
 [4, 8] 

 After operation 3 
 [16, 8] 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100 
 
 1 <= k <= 10 
 
 1 <= multiplier <= 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: vector<int> getFinalState(vector<int>& nums,int k,int multiplier){while(k--){int i=min_element(nums.begin(),nums.end())-nums.begin();nums[i]*=multiplier;}return nums;} };
```


## 3266. Final Array State After K Multiplication Operations II

**Problem:** https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Heap (Priority Queue), Simulation

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n + t log n + log k + n)

**Space complexity:** O(n)

**Complexity reasoning:** Initialize an n-element heap; simulate t <= k multiplications until the minimum reaches the original maximum, then distribute remaining k operations using modular exponentiation. If multiplier > 1 and values are positive, t is bounded by the value range and n; worst case O(k log n).

### Problem description

You are given an integer array nums , an integer k , and an integer multiplier . 
 
 You need to perform k operations on nums . In each operation: 

 Find the minimum value x in nums . If there are multiple occurrences of the minimum value, select the one that appears first . 
 
 Replace the selected minimum value x with x * multiplier . 

 After the k operations, apply modulo 10 9 + 7 to every value in nums . 
 
 Return an integer array denoting the final state of nums after performing all k operations and then applying the modulo. 

 Example 1: 

 Input: nums = [2,1,3,5,6], k = 5, multiplier = 2 
 
 Output: [8,4,6,5,6] 
 
 Explanation: 

 Operation 
 Result 

 After operation 1 
 [2, 2, 3, 5, 6] 

 After operation 2 
 [4, 2, 3, 5, 6] 

 After operation 3 
 [4, 4, 3, 5, 6] 

 After operation 4 
 [4, 4, 6, 5, 6] 

 After operation 5 
 [8, 4, 6, 5, 6] 

 After applying modulo 
 [8, 4, 6, 5, 6] 

 Example 2: 

 Input: nums = [100000,2000], k = 2, multiplier = 1000000 
 
 Output: [999999307,999999993] 
 
 Explanation: 

 Operation 
 Result 

 After operation 1 
 [100000, 2000000000] 

 After operation 2 
 [100000000000, 2000000000] 

 After applying modulo 
 [999999307, 999999993] 

 Constraints: 

 1 <= nums.length <= 10 4 
 
 1 <= nums[i] <= 10 9 
 
 1 <= k <= 10 9 
 
 1 <= multiplier <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { const long long MOD=1000000007;
 long long power(long long a,long long b){long long r=1;for(;b;b>>=1,a=a*a%MOD)if(b&1)r=r*a%MOD;return r;}
public:
 vector<int> getFinalState(vector<int>& nums,int k,int multiplier){int n=nums.size();if(multiplier==1)return nums;long long mx=*max_element(nums.begin(),nums.end());
 using P=pair<long long,int>;priority_queue<P,vector<P>,greater<P>>pq;for(int i=0;i<n;++i)pq.push({nums[i],i});
 while(k>0&&pq.top().first<mx){auto [v,i]=pq.top();pq.pop();pq.push({v*multiplier,i});--k;}
 vector<P> v;while(!pq.empty()){v.push_back(pq.top());pq.pop();}long long rounds=k/n,extra=k%n,base=power(multiplier,rounds);
 for(int i=0;i<n;++i){long long x=v[i].first%MOD*base%MOD;if(i<extra)x=x*multiplier%MOD;nums[v[i].second]=(int)x;}return nums;}
};
```


## 3275. K-th Nearest Obstacle Queries

**Problem:** https://leetcode.com/problems/k-th-nearest-obstacle-queries/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(q log k)

**Space complexity:** O(k + q)

**Complexity reasoning:** Maintain a max-heap of at most k obstacle distances across q queries, and append one result per query.

### Problem description

There is an infinite 2D plane. 
 
 You are given a positive integer k . You are also given a 2D array queries , which contains the following queries: 

 queries[i] = [x, y] : Build an obstacle at coordinate (x, y) in the plane. It is guaranteed that there is no obstacle at this coordinate when this query is made. 

 After each query, you need to find the distance of the k th nearest obstacle from the origin. 
 
 Return an integer array results where results[i] denotes the k th nearest obstacle after query i , or results[i] == -1 if there are less than k obstacles. 
 
 Note that initially there are no obstacles anywhere. 
 
 The distance of an obstacle at coordinate (x, y) from the origin is given by |x| + |y| . 

 Example 1: 

 Input: queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2 
 
 Output: [-1,7,5,3] 
 
 Explanation: 

 Initially, there are 0 obstacles. 
 
 After queries[0] , there are less than 2 obstacles. 
 
 After queries[1] , there are obstacles at distances 3 and 7. 
 
 After queries[2] , there are obstacles at distances 3, 5, and 7. 
 
 After queries[3] , there are obstacles at distances 3, 3, 5, and 7. 

 Example 2: 

 Input: queries = [[5,5],[4,4],[3,3]], k = 1 
 
 Output: [10,8,6] 
 
 Explanation: 

 After queries[0] , there is an obstacle at distance 10. 
 
 After queries[1] , there are obstacles at distances 8 and 10. 
 
 After queries[2] , there are obstacles at distances 6, 8, and 10. 

 Constraints: 

 1 <= queries.length <= 2 * 10 5 
 
 All queries[i] are unique. 
 
 -10 9 <= queries[i][0], queries[i][1] <= 10 9 
 
 1 <= k <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: vector<int> resultsArray(vector<vector<int>>&queries,int k){priority_queue<int>pq;vector<int>ans;for(auto&q:queries){pq.push(abs(q[0])+abs(q[1]));if((int)pq.size()>k)pq.pop();ans.push_back((int)pq.size()==k?pq.top():-1);}return ans;} };
```


## 3391. Design a 3D Binary Matrix with Efficient Layer Tracking

**Problem:** https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Hash Table, Design, Heap (Priority Queue), Matrix, Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Hash map / hash set, Ordered set, Priority queue / heap, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** constructor O(n^3 + n log n); setCell/unsetCell O(log n); largestMatrix O(1)

**Space complexity:** O(n^3)

**Complexity reasoning:** Allocate n^3 cells and initialize a balanced set of n layer counts; updates erase/insert one ranked layer, while largestMatrix reads the last set entry.

### Problem description

You are given a n x n x n binary 3D array matrix . 
 
 Implement the Matrix3D class: 

 Matrix3D(int n) Initializes the object with the 3D binary array matrix , where all elements are initially set to 0. 
 
 void setCell(int x, int y, int z) Sets the value at matrix[x][y][z] to 1. 
 
 void unsetCell(int x, int y, int z) Sets the value at matrix[x][y][z] to 0. 
 
 int largestMatrix() Returns the index x where matrix[x] contains the most number of 1's. If there are multiple such indices, return the largest x . 

 Example 1: 

 Input: 
 ["Matrix3D", "setCell", "largestMatrix", "setCell", "largestMatrix", "setCell", "largestMatrix"] 
[[3], [0, 0, 0], [], [1, 1, 2], [], [0, 0, 1], []] 
 
 Output: 
 [null, null, 0, null, 1, null, 0] 
 
 Explanation 
Matrix3D matrix3D = new Matrix3D(3); // Initializes a 3 x 3 x 3 3D array matrix , filled with all 0's. 
matrix3D.setCell(0, 0, 0); // Sets matrix[0][0][0] to 1. 
matrix3D.largestMatrix(); // Returns 0. matrix[0] has the most number of 1's. 
matrix3D.setCell(1, 1, 2); // Sets matrix[1][1][2] to 1. 
matrix3D.largestMatrix(); // Returns 1. matrix[0] and matrix[1] tie with the most number of 1's, but index 1 is bigger. 
matrix3D.setCell(0, 0, 1); // Sets matrix[0][0][1] to 1. 
matrix3D.largestMatrix(); // Returns 0. matrix[0] has the most number of 1's. 
 
 Example 2: 

 Input: 
 ["Matrix3D", "setCell", "largestMatrix", "unsetCell", "largestMatrix"] 
[[4], [2, 1, 1], [], [2, 1, 1], []] 
 
 Output: 
 [null, null, 2, null, 3] 
 
 Explanation 
Matrix3D matrix3D = new Matrix3D(4); // Initializes a 4 x 4 x 4 3D array matrix , filled with all 0's. 
matrix3D.setCell(2, 1, 1); // Sets matrix[2][1][1] to 1. 
matrix3D.largestMatrix(); // Returns 2. matrix[2] has the most number of 1's. 
matrix3D.unsetCell(2, 1, 1); // Sets matrix[2][1][1] to 0. 
matrix3D.largestMatrix(); // Returns 3. All indices from 0 to 3 tie with the same number of 1's, but index 3 is the biggest. 

 Constraints: 

 1 <= n <= 100 
 
 0 <= x, y, z < n 
 
 At most 10 5 calls are made in total to setCell and unsetCell . 
 
 At most 10 4 calls are made to largestMatrix .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Matrix3D {
    int n;
    vector<unsigned char> cells;
    vector<int> count;
    set<pair<int,int>> rank;
    int idx(int x,int y,int z) {
        return (x*n+y)*n+z;
    }
    void change(int x,int y,int z,int value) {
        int i=idx(x,y,z);
        if(cells[i]==value)return;
        rank.erase( {
            count[x],x
        }
        );
        count[x]+=value?1:-1;
        cells[i]=value;
        rank.insert( {
            count[x],x
        }
        );
    }
    public:Matrix3D(int n):n(n),cells(n*n*n,0),count(n,0) {
        for(int x=0; x<n; x++)rank.insert( {
            0,x
        }
        );
    }
    void setCell(int x,int y,int z) {
        change(x,y,z,1);
    }
    void unsetCell(int x,int y,int z) {
        change(x,y,z,0);
    }
    int largestMatrix() {
        return rank.rbegin()->second;
    }
}
;
```


## 3408. Design Task Manager

**Problem:** https://leetcode.com/problems/design-task-manager/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, Design, Heap (Priority Queue), Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Stack / Queue

**Data structures (inferred):** Hash map, Hash map / hash set, Ordered map, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Constructor: O(t log t); add/edit: O(log h) expected; rmv: O(1) expected; execTop: O(r log h) expected, amortized O(log h) per inserted heap entry

**Space complexity:** O(t + h)

**Complexity reasoning:** With t initial tasks and h accumulated heap entries, each add/edit pushes a priority-queue record; stale entries are removed lazily. execTop may discard r stale entries before finding a live task. The hash table stores active tasks and the heap can retain old records.

### Problem description

There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks. 
 
 Implement the TaskManager class: 

 TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority] , which adds a task to the specified user with the given priority. 

 void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId . It is guaranteed that taskId does not exist in the system. 

 void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority . It is guaranteed that taskId exists in the system. 

 void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system. 

 int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId . After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1. 

 Note that a user may be assigned multiple tasks. 

 Example 1: 

 Input: 
 ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"] 
[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []] 
 
 Output: 
 [null, null, null, 3, null, null, 5] 
 
 Explanation 
TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3. 
taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4. 
taskManager.edit(102, 8); // Updates priority of task 102 to 8. 
taskManager.execTop(); // return 3. Executes task 103 for User 3. 
taskManager.rmv(101); // Removes task 101 from the system. 
taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5. 
taskManager.execTop(); // return 5. Executes task 105 for User 5. 

 Constraints: 

 1 <= tasks.length <= 10 5 
 
 0 <= userId <= 10 5 
 
 0 <= taskId <= 10 5 
 
 0 <= priority <= 10 9 
 
 0 <= newPriority <= 10 9 
 
 At most 2 * 10 5 calls will be made in total to add , edit , rmv , and execTop methods. 
 
 The input is generated such that taskId will be valid.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class TaskManager {struct Item{int user,priority;};unordered_map<int,Item>tasks;priority_queue<pair<int,int>>pq;public:TaskManager(vector<vector<int>>&init){for(auto&t:init)add(t[0],t[1],t[2]);}void add(int userId,int taskId,int priority){tasks[taskId]={userId,priority};pq.push({priority,taskId});}void edit(int taskId,int newPriority){tasks[taskId].priority=newPriority;pq.push({newPriority,taskId});}void rmv(int taskId){tasks.erase(taskId);}int execTop(){while(!pq.empty()){auto p=pq.top();pq.pop();auto it=tasks.find(p.second);if(it==tasks.end()||it->second.priority!=p.first)continue;int user=it->second.user;tasks.erase(it);return user;}return -1;}};
```


## 3478. Choose K Elements With Maximum Sum

**Problem:** https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Sorting, Heap (Priority Queue)

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n + n log(k+1))

**Space complexity:** O(n + k)

**Complexity reasoning:** Sort n indices by nums1, then process equal-value groups. Each nums2 value is pushed into a min-heap capped at k, giving O(log(k+1)) per insertion/removal; the output and index arrays require O(n) space.

### Problem description

You are given two integer arrays, nums1 and nums2 , both of length n , along with a positive integer k . 
 
 For each index i from 0 to n - 1 , perform the following: 

 Find all indices j where nums1[j] is less than nums1[i] . 
 
 Choose at most k values of nums2[j] at these indices to maximize the total sum. 

 Return an array answer of size n , where answer[i] represents the result for the corresponding index i . 

 Example 1: 

 Input: nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2 
 
 Output: [80,30,0,80,50] 
 
 Explanation: 

 For i = 0 : Select the 2 largest values from nums2 at indices [1, 2, 4] where nums1[j] < nums1[0] , resulting in 50 + 30 = 80 . 
 
 For i = 1 : Select the 2 largest values from nums2 at index [2] where nums1[j] < nums1[1] , resulting in 30. 
 
 For i = 2 : No indices satisfy nums1[j] < nums1[2] , resulting in 0. 
 
 For i = 3 : Select the 2 largest values from nums2 at indices [0, 1, 2, 4] where nums1[j] < nums1[3] , resulting in 50 + 30 = 80 . 
 
 For i = 4 : Select the 2 largest values from nums2 at indices [1, 2] where nums1[j] < nums1[4] , resulting in 30 + 20 = 50 . 

 Example 2: 

 Input: nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1 
 
 Output: [0,0,0,0] 
 
 Explanation: 
 
 Since all elements in nums1 are equal, no indices satisfy the condition nums1[j] < nums1[i] for any i , resulting in 0 for all positions. 

 Constraints: 

 n == nums1.length == nums2.length 
 
 1 <= n <= 10 5 
 
 1 <= nums1[i], nums2[i] <= 10 6 
 
 1 <= k <= n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<long long> findMaxSum(vector<int>& nums1,vector<int>& nums2,int k){int n=nums1.size();vector<int> id(n);iota(id.begin(),id.end(),0);sort(id.begin(),id.end(),[&](int a,int b){return nums1[a]<nums1[b];});priority_queue<int,vector<int>,greater<int>> pq;long long sum=0;vector<long long> ans(n);for(int i=0;i<n;){int j=i;while(j<n&&nums1[id[j]]==nums1[id[i]]){ans[id[j]]=sum;j++;}for(int t=i;t<j;t++){int v=nums2[id[t]];pq.push(v);sum+=v;if((int)pq.size()>k){sum-=pq.top();pq.pop();}}i=j;}return ans;}};
```


## 3507. Minimum Pair Removal to Sort Array I

**Problem:** https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Hash Table, Linked List, Heap (Priority Queue), Simulation, Doubly-Linked List, Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Linked List / Pointers, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Linked list, Priority queue / heap, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n^2)

**Space complexity:** O(n)

**Complexity reasoning:** Each of at most n-1 merges scans the current array to test sortedness and locate the minimum adjacent sum; vector::erase also shifts O(n) elements. The copied working array has n entries.

### Problem description

Given an array nums , you can perform the following operation any number of times: 

 Select the adjacent pair with the minimum sum in nums . If multiple such pairs exist, choose the leftmost one. 
 
 Replace the pair with their sum. 

 Return the minimum number of operations needed to make the array non-decreasing . 
 
 An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists). 

 Example 1: 

 Input: nums = [5,2,3,1] 
 
 Output: 2 
 
 Explanation: 

 The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4] . 
 
 The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6] . 

 The array nums became non-decreasing in two operations. 

 Example 2: 

 Input: nums = [1,2,2] 
 
 Output: 0 
 
 Explanation: 
 
 The array nums is already sorted. 

 Constraints: 

 1 <= nums.length <= 50 
 
 -1000 <= nums[i] <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int minimumPairRemoval(vector<int>&nums){vector<long long>a(nums.begin(),nums.end());int ans=0;while(true){bool sorted=true;for(int i=1;i<(int)a.size();i++)if(a[i]<a[i-1])sorted=false;if(sorted)return ans;int p=0;for(int i=1;i+1<(int)a.size();i++)if(a[i]+a[i+1]<a[p]+a[p+1])p=i;a[p]+=a[p+1];a.erase(a.begin()+p+1);ans++;}}};
```


## 3510. Minimum Pair Removal to Sort Array II

**Problem:** https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, Linked List, Heap (Priority Queue), Simulation, Doubly-Linked List, Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Linked List / Pointers, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Linked list, Priority queue, Priority queue / heap, Queue, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Initialize a heap with n-1 adjacent sums and track inversions with a bad counter. Each merge updates only neighboring links and adds O(1) heap records, so O(n) total heap pushes/pops cost O(log n) each. Arrays and heap use O(n) space.

### Problem description

Given an array nums , you can perform the following operation any number of times: 

 Select the adjacent pair with the minimum sum in nums . If multiple such pairs exist, choose the leftmost one. 
 
 Replace the pair with their sum. 

 Return the minimum number of operations needed to make the array non-decreasing . 
 
 An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists). 

 Example 1: 

 Input: nums = [5,2,3,1] 
 
 Output: 2 
 
 Explanation: 

 The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4] . 
 
 The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6] . 

 The array nums became non-decreasing in two operations. 

 Example 2: 

 Input: nums = [1,2,2] 
 
 Output: 0 
 
 Explanation: 
 
 The array nums is already sorted. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 -10 9 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int minimumPairRemoval(vector<int>&nums){int n=nums.size();vector<long long>v(nums.begin(),nums.end());vector<int>pr(n),nx(n),ver(n);vector<bool>alive(n,true);for(int i=0;i<n;i++){pr[i]=i-1;nx[i]=i+1;}using T=tuple<long long,int,int>;priority_queue<T,vector<T>,greater<T>>pq;int bad=0;for(int i=0;i+1<n;i++){pq.emplace(v[i]+v[i+1],i,0);bad+=v[i]>v[i+1];}int ans=0;while(bad){auto [sum,i,stamp]=pq.top();pq.pop();int j=nx[i];if(!alive[i]||j>=n||!alive[j]||ver[i]!=stamp||v[i]+v[j]!=sum)continue;int a=pr[i],b=nx[j];bad-=v[i]>v[j];if(a>=0)bad-=v[a]>v[i];if(b<n)bad-=v[j]>v[b];v[i]+=v[j];alive[j]=false;nx[i]=b;if(b<n)pr[b]=i;ver[i]++;if(a>=0){bad+=v[a]>v[i];ver[a]++;pq.emplace(v[a]+v[i],a,ver[a]);}if(b<n){bad+=v[i]>v[b];pq.emplace(v[i]+v[b],i,ver[i]);}ans++;}return ans;}};
```


## 3815. Design Auction System

**Problem:** https://leetcode.com/problems/design-auction-system/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, Design, Heap (Priority Queue), Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Stack / Queue

**Data structures (inferred):** Hash map, Hash map / hash set, Ordered map, Ordered set, Priority queue / heap

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** addBid/updateBid/removeBid: O(log b) expected; getHighestBidder: O(1) expected

**Space complexity:** O(B + I)

**Complexity reasoning:** For b bids on the affected item, ordered-set insert/erase costs O(log b), while unordered-map lookups are expected O(1). The largest set element is read through rbegin in constant time. B is the total stored bids and I the number of item entries.

### Problem description

You are asked to design an auction system that manages bids from multiple users in real time. 
 
 Each bid is associated with a userId , an itemId , and a bidAmount . 
 
 Implement the AuctionSystem class:​​​​​​​ 

 AuctionSystem() : Initializes the AuctionSystem object. 
 
 void addBid(int userId, int itemId, int bidAmount) : Adds a new bid for itemId by userId with bidAmount . If the same userId already has a bid on itemId , replace it with the new bidAmount . 
 
 void updateBid(int userId, int itemId, int newAmount) : Updates the existing bid of userId for itemId to newAmount . It is guaranteed that this bid exists . 
 
 void removeBid(int userId, int itemId) : Removes the bid of userId for itemId . It is guaranteed that this bid exists . 
 
 int getHighestBidder(int itemId) : Returns the userId of the highest bidder for itemId . If multiple users have the same highest bidAmount , return the user with the highest userId . If no bids exist for the item, return -1. 

 Example 1: 

 Input: 
 ["AuctionSystem", "addBid", "addBid", "getHighestBidder", "updateBid", "getHighestBidder", "removeBid", "getHighestBidder", "getHighestBidder"] 
[[], [1, 7, 5], [2, 7, 6], [7], [1, 7, 8], [7], [2, 7], [7], [3]] 
 
 Output: 
 [null, null, null, 2, null, 1, null, 1, -1] 
 
 Explanation 
AuctionSystem auctionSystem = new AuctionSystem(); // Initialize the Auction system 
auctionSystem.addBid(1, 7, 5); // User 1 bids 5 on item 7 
auctionSystem.addBid(2, 7, 6); // User 2 bids 6 on item 7 
auctionSystem.getHighestBidder(7); // return 2 as User 2 has the highest bid 
auctionSystem.updateBid(1, 7, 8); // User 1 updates bid to 8 on item 7 
auctionSystem.getHighestBidder(7); // return 1 as User 1 now has the highest bid 
auctionSystem.removeBid(2, 7); // Remove User 2's bid on item 7 
auctionSystem.getHighestBidder(7); // return 1 as User 1 is the current highest bidder 
auctionSystem.getHighestBidder(3); // return -1 as no bids exist for item 3 

 Constraints: 

 1 <= userId, itemId <= 5 * 10 4 
 
 1 <= bidAmount, newAmount <= 10 9 
 
 At most 5 * 10 4 total calls to addBid , updateBid , removeBid , and getHighestBidder . 
 
 The input is generated such that for updateBid and removeBid , the bid from the given userId for the given itemId will be valid.

### C++ solution

**Source:** accepted_cpp_submission

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


## 3885. Design Event Manager

**Problem:** https://leetcode.com/problems/design-event-manager/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Design, Heap (Priority Queue), Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, Ordered set, Priority queue / heap, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Constructor: O(n log n); updatePriority/pollHighest: O(log n); empty poll: O(1)

**Space complexity:** O(n)

**Complexity reasoning:** The constructor inserts n events into an ordered set and hash map. Updating removes and reinserts one ordered-set key; polling removes its smallest key. The ordered set holds at most n events, and hash operations are expected O(1).

### Problem description

You are given an initial list of events, where each event has a unique eventId and a priority . 
 
 Implement the EventManager class: 

 EventManager(int[][] events) Initializes the manager with the given events, where events[i] = [eventId i , priority ​​​​​​​i ] . 
 
 void updatePriority(int eventId, int newPriority) Updates the priority of the active event with id eventId to newPriority . 
 
 int pollHighest() Removes and returns the eventId of the active event with the highest priority. If multiple active events have the same priority, return the smallest eventId among them. If there are no active events, return -1. 

 An event is called active if it has not been removed by pollHighest() . 

 Example 1: 

 Input: 
 ["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"] 
[[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []] 
 
 Output: 
 [null, 2, null, 5, 9] 
 
 Explanation 
EventManager eventManager = new EventManager([[5,7], [2,7], [9,4]]); // Initializes the manager with three events 
eventManager.pollHighest(); // both events 5 and 2 have priority 7, so return the smaller id 2 
eventManager.updatePriority(9, 7); // event 9 now has priority 7 
eventManager.pollHighest(); // remaining highest priority events are 5 and 9, return 5 
eventManager.pollHighest(); // return 9 
 
 Example 2: 

 Input: 
 ["EventManager", "pollHighest", "pollHighest", "pollHighest"] 
[[[[4, 1], [7, 2]]], [], [], []] 
 
 Output: 
 [null, 7, 4, -1] 
 
 Explanation 
EventManager eventManager = new EventManager([[4,1], [7,2]]); // Initializes the manager with two events 
eventManager.pollHighest(); // return 7 
eventManager.pollHighest(); // return 4 
eventManager.pollHighest(); // no events remain, return -1 

 Constraints: 

 1 <= events.length <= 10 5 
 
 events[i] = [eventId, priority] 
 
 1 <= eventId <= 10 9 
 
 1 <= priority <= 10 9 
 
 All the values of eventId in events are unique . 
 
 1 <= newPriority <= 10 9 
 
 For every call to updatePriority , eventId refers to an active event. 
 
 At most 10 5 calls in total will be made to updatePriority and pollHighest .

### C++ solution

**Source:** accepted_cpp_submission

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


## 4065. Rearrange Array by Removing Distinct Values

**Problem:** https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Hash Table, Sorting, Heap (Priority Queue), Simulation, Counting, Ordered Set

**Primary pattern:** Heap / Priority Queue

**Related patterns:** Heap / Priority Queue, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Ordered map, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Repeatedly select the current min/max or maintain top-k candidates.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log d + f d)

**Space complexity:** O(n + d)

**Complexity reasoning:** Count n values in an ordered map of d distinct keys, taking O(log d) per update. Then perform f = maximum frequency full traversals of d keys, appending n total output values; hence O(fd) for the round scans and O(n) for the returned array.

### Problem description

You are given an integer array nums . 
 
 You start with an empty array ans . Repeat the following operation until nums is empty : 

 Identify all distinct values currently present in nums . 
 
 Remove one occurrence of every distinct value currently in nums , and append those values to ans in ascending order. 

 Return the array ans . 

 Example 1: 

 Input: nums = [3,1,3,2,1,3] 
 
 Output: [1,2,3,1,3,3] 
 
 Explanation: 

 Operation 
 Appended to ans 
 nums after 
 ans after 

 1 
 1, 2, 3 
 [3, 1, 3] 
 [1, 2, 3] 

 2 
 1, 3 
 [3] 
 [1, 2, 3, 1, 3] 

 3 
 3 
 [] 
 [1, 2, 3, 1, 3, 3] 

 nums is now empty, so the answer is [1, 2, 3, 1, 3, 3] . 

 Example 2: 

 Input: nums = [7,7,4,4,4] 
 
 Output: [4,7,4,7,4] 
 
 Explanation: 

 Operation 
 Appended to ans 
 nums after 
 ans after 

 1 
 4, 7 
 [7, 4, 4] 
 [4, 7] 

 2 
 4, 7 
 [4] 
 [4, 7, 4, 7] 

 3 
 4 
 [] 
 [4, 7, 4, 7, 4] 

 nums is now empty, so the answer is [4, 7, 4, 7, 4] . 

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    public: vector<int> rearrangeArray(vector<int>& nums) {
        map<int,int> f;
        int mx=0;
        for(int x:nums)mx=max(mx,++f[x]);
        vector<int> ans;
        for(int round=0; round<mx; round++)for(auto &p:f)if(p.second>round)ans.push_back(p.first);
        return ans;
    }
}
;
```

