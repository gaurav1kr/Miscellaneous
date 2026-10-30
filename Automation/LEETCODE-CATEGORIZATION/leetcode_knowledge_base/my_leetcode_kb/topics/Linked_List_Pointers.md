# Linked List / Pointers

**Problems:** 27

## Quick revision checklist

Rewire node links while preserving ownership and pointer invariants.

## Problem index

- [21. Merge Two Sorted Lists](#21-merge-two-sorted-lists) — Easy; code: yes
- [24. Swap Nodes in Pairs](#24-swap-nodes-in-pairs) — Medium; code: yes
- [25. Reverse Nodes in k-Group](#25-reverse-nodes-in-k-group) — Hard; code: yes
- [83. Remove Duplicates from Sorted List](#83-remove-duplicates-from-sorted-list) — Easy; code: yes
- [92. Reverse Linked List II](#92-reverse-linked-list-ii) — Medium; code: yes
- [203. Remove Linked List Elements](#203-remove-linked-list-elements) — Easy; code: yes
- [206. Reverse Linked List](#206-reverse-linked-list) — Easy; code: yes
- [237. Delete Node in a Linked List](#237-delete-node-in-a-linked-list) — Medium; code: yes
- [328. Odd Even Linked List](#328-odd-even-linked-list) — Medium; code: yes
- [622. Design Circular Queue](#622-design-circular-queue) — Medium; code: yes
- [641. Design Circular Deque](#641-design-circular-deque) — Medium; code: yes
- [707. Design Linked List](#707-design-linked-list) — Medium; code: yes
- [708. Insert into a Sorted Circular Linked List](#708-insert-into-a-sorted-circular-linked-list) — Medium; code: yes
- [716. Max Stack](#716-max-stack) — Hard; code: yes
- [725. Split Linked List in Parts](#725-split-linked-list-in-parts) — Medium; code: yes
- [1206. Design Skiplist](#1206-design-skiplist) — Hard; code: yes
- [1472. Design Browser History](#1472-design-browser-history) — Medium; code: yes
- [1474. Delete N Nodes After M Nodes of a Linked List](#1474-delete-n-nodes-after-m-nodes-of-a-linked-list) — Easy; code: yes
- [1669. Merge In Between Linked Lists](#1669-merge-in-between-linked-lists) — Medium; code: yes
- [1670. Design Front Middle Back Queue](#1670-design-front-middle-back-queue) — Medium; code: yes
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](#2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points) — Medium; code: yes
- [2074. Reverse Nodes in Even Length Groups](#2074-reverse-nodes-in-even-length-groups) — Medium; code: yes
- [2181. Merge Nodes in Between Zeros](#2181-merge-nodes-in-between-zeros) — Medium; code: yes
- [2326. Spiral Matrix IV](#2326-spiral-matrix-iv) — Medium; code: yes
- [3062. Winner of the Linked List Game](#3062-winner-of-the-linked-list-game) — Easy; code: yes
- [3263. Convert Doubly Linked List to Array I](#3263-convert-doubly-linked-list-to-array-i) — Easy; code: yes
- [3294. Convert Doubly Linked List to Array II](#3294-convert-doubly-linked-list-to-array-ii) — Medium; code: yes

---

## 21. Merge Two Sorted Lists

**Problem:** https://leetcode.com/problems/merge-two-sorted-lists/

**Difficulty:** Easy | **Premium:** No

**Tags:** Linked List, Recursion

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + m)

**Space complexity:** O(1)

**Complexity reasoning:** Each iteration attaches one node from either sorted list; the remaining suffix is linked directly. n and m are the list lengths.

### Problem description

You are given the heads of two sorted linked lists list1 and list2 . 
 
 Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. 
 
 Return the head of the merged linked list . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg] 
 
```
Input:
 list1 = [1,2,4], list2 = [1,3,4]

Output:
 [1,1,2,3,4,4]
```

 Example 2: 
 
```
Input:
 list1 = [], list2 = []

Output:
 []
```

 Example 3: 
 
```
Input:
 list1 = [], list2 = [0]

Output:
 [0]
```

 Constraints: 

 The number of nodes in both lists is in the range [0, 50] . 
 
 -100 <= Node.val <= 100 
 
 Both list1 and list2 are sorted in non-decreasing order.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy(0), *tail = &dummy;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } else {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }
        tail->next = l1 ? l1 : l2;
        return dummy.next;
    }
};
```


## 24. Swap Nodes in Pairs

**Problem:** https://leetcode.com/problems/swap-nodes-in-pairs/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List, Recursion

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Each pair is visited once and swapped using a fixed number of pointers; there is no recursion or auxiliary collection.

### Problem description

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.) 

 Example 1: 

 Input: head = [1,2,3,4] 
 
 Output: [2,1,4,3] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg] 

 Example 2: 

 Input: head = [] 
 
 Output: [] 

 Example 3: 

 Input: head = [1] 
 
 Output: [1] 

 Example 4: 

 Input: head = [1,2,3] 
 
 Output: [2,1,3] 

 Constraints: 

 The number of nodes in the list is in the range [0, 100] . 
 
 0 <= Node.val <= 100

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
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head; // Base case: If list has 0 or 1 node, no swapping needed.
        
        ListNode* newHead = head->next; // The new head will be the second node.
        ListNode* prev = nullptr;
        while (head && head->next) {
            ListNode* first = head;
            ListNode* second = head->next;
            
            // Swap the pair
            first->next = second->next;
            second->next = first;
            if (prev) prev->next = second; // Connect the previous pair to the current swapped pair.
            
            // Move pointers forward
            prev = first;
            head = first->next;
        }
        return newHead;
    }
};
```


## 25. Reverse Nodes in k-Group

**Problem:** https://leetcode.com/problems/reverse-nodes-in-k-group/

**Difficulty:** Hard | **Premium:** No

**Tags:** Linked List, Recursion

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One pass counts n nodes, then each complete group of k nodes is rewired in O(k), for O(n) total work; only pointers and counters are used.

### Problem description

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list . 
 
 k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is. 
 
 You may not alter the values in the list's nodes, only nodes themselves may be changed. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg] 
 
```
Input:
 head = [1,2,3,4,5], k = 2

Output:
 [2,1,4,3,5]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg] 
 
```
Input:
 head = [1,2,3,4,5], k = 3

Output:
 [3,2,1,4,5]
```

 Constraints: 

 The number of nodes in the list is n . 
 
 1 <= k <= n <= 5000 
 
 0 <= Node.val <= 1000 

 Follow-up: Can you solve the problem in O(1) extra memory space?

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;

        // Dummy node
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy, *curr = head, *next = nullptr;

        // Count total number of nodes
        int count = 0;
        while (curr) {
            count++;
            curr = curr->next;
        }

        // Reverse nodes in k groups
        curr = head;
        while (count >= k) {
            next = curr->next;
            for (int i = 1; i < k; i++) {
                curr->next = next->next;
                next->next = prev->next;
                prev->next = next;
                next = curr->next;
            }
            prev = curr;
            curr = next;
            count -= k;
        }

        return dummy.next;
    }
};
```


## 83. Remove Duplicates from Sorted List

**Problem:** https://leetcode.com/problems/remove-duplicates-from-sorted-list/

**Difficulty:** Easy | **Premium:** No

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** The current pointer advances past each distinct node or bypasses a duplicate; each node is inspected at most a constant number of times.

### Problem description

Given the head of a sorted linked list, delete all duplicates such that each element appears only once . Return the linked list sorted as well . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/01/04/list1.jpg] 
 
```
Input:
 head = [1,1,2]

Output:
 [1,2]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/01/04/list2.jpg] 
 
```
Input:
 head = [1,1,2,3,3]

Output:
 [1,2,3]
```

 Constraints: 

 The number of nodes in the list is in the range [0, 300] . 
 
 -100 <= Node.val <= 100 
 
 The list is guaranteed to be sorted in ascending order.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* current = head;
        while (current && current->next) {
            if (current->val == current->next->val) {
                current->next = current->next->next;
            } else {
                current = current->next;
            }
        }
        return head;
    }
};
```


## 92. Reverse Linked List II

**Problem:** https://leetcode.com/problems/reverse-linked-list-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(right)

**Space complexity:** O(1)

**Complexity reasoning:** Advance left - 1 nodes and perform right - left constant-time front insertions; only a fixed set of pointers is maintained.

### Problem description

Given the head of a singly linked list and two integers left and right where left <= right , reverse the nodes of the list from position left to position right , and return the reversed list . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg] 
 
```
Input:
 head = [1,2,3,4,5], left = 2, right = 4

Output:
 [1,4,3,2,5]
```

 Example 2: 
 
```
Input:
 head = [5], left = 1, right = 1

Output:
 [5]
```

 Constraints: 

 The number of nodes in the list is n . 
 
 1 <= n <= 500 
 
 -500 <= Node.val <= 500 
 
 1 <= left <= right <= n 

 Follow up: Could you do it in one pass?

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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;

        // Move `prev` to the node before `left`
        for (int i = 1; i < left; ++i) {
            prev = prev->next;
        }

        // Reverse the sublist
        ListNode* curr = prev->next;
        ListNode* next = nullptr;
        for (int i = 0; i < right - left; ++i) {
            next = curr->next;
            curr->next = next->next;
            next->next = prev->next;
            prev->next = next;
        }

        return dummy.next;
    }
};
```


## 203. Remove Linked List Elements

**Problem:** https://leetcode.com/problems/remove-linked-list-elements/

**Difficulty:** Easy | **Premium:** No

**Tags:** Linked List, Recursion

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** The loop visits each original node once, either retaining it or bypassing it without allocating auxiliary storage.

### Problem description

Given the head of a linked list and an integer val , remove all the nodes of the linked list that has Node.val == val , and return the new head . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg] 
 
```
Input:
 head = [1,2,6,3,4,5,6], val = 6

Output:
 [1,2,3,4,5]
```

 Example 2: 
 
```
Input:
 head = [], val = 1

Output:
 []
```

 Example 3: 
 
```
Input:
 head = [7,7,7,7], val = 7

Output:
 []
```

 Constraints: 

 The number of nodes in the list is in the range [0, 10 4 ] . 
 
 1 <= Node.val <= 50 
 
 0 <= val <= 50

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode dummy(0), *prev = &dummy;
        dummy.next = head;
        while (head) {
            if (head->val == val) prev->next = head->next;
            else prev = head;
            head = head->next;
        }
        return dummy.next;
    }
};
```


## 206. Reverse Linked List

**Problem:** https://leetcode.com/problems/reverse-linked-list/

**Difficulty:** Easy | **Premium:** No

**Tags:** Linked List, Recursion

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Each node is visited once and its next pointer is reversed using three pointers.

### Problem description

Given the head of a singly linked list, reverse the list, and return the reversed list . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg] 
 
```
Input:
 head = [1,2,3,4,5]

Output:
 [5,4,3,2,1]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg] 
 
```
Input:
 head = [1,2]

Output:
 [2,1]
```

 Example 3: 
 
```
Input:
 head = []

Output:
 []
```

 Constraints: 

 The number of nodes in the list is the range [0, 5000] . 
 
 -5000 <= Node.val <= 5000 

 Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *prev = nullptr, *curr = head;
        while (curr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
};
```


## 237. Delete Node in a Linked List

**Problem:** https://leetcode.com/problems/delete-node-in-a-linked-list/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Copy the successor value and bypass the successor with a constant number of accesses.

### Problem description

There is a singly-linked list head and we want to delete a node node in it. 
 
 You are given the node to be deleted node . You will not be given access to the first node of head . 
 
 All the values of the linked list are unique , and it is guaranteed that the given node node is not the last node in the linked list. 
 
 Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean: 

 The value of the given node should not exist in the linked list. 
 
 The number of nodes in the linked list should decrease by one. 
 
 All the values before node should be in the same order. 
 
 All the values after node should be in the same order. 

 Custom testing: 

 For the input, you should provide the entire linked list head and the node to be given node . node should not be the last node of the list and should be an actual node in the list. 
 
 We will build the linked list and pass the node to your function. 
 
 The output will be the entire list after calling your function. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/01/node1.jpg] 
 
```
Input:
 head = [4,5,1,9], node = 5

Output:
 [4,1,9]

Explanation: 
You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/01/node2.jpg] 
 
```
Input:
 head = [4,5,1,9], node = 1

Output:
 [4,5,9]

Explanation: 
You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
```

 Constraints: 

 The number of the nodes in the given list is in the range [2, 1000] . 
 
 -1000 <= Node.val <= 1000 
 
 The value of each node in the list is unique . 
 
 The node to be deleted is in the list and is not a tail node.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};
```


## 328. Odd Even Linked List

**Problem:** https://leetcode.com/problems/odd-even-linked-list/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Odd and even pointers advance through the list once and reconnect existing nodes in place.

### Problem description

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list . 
 
 The first node is considered odd , and the second node is even , and so on. 
 
 Note that the relative order inside both the even and odd groups should remain as it was in the input. 
 
 You must solve the problem in O(1)  extra space complexity and O(n) time complexity. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg] 
 
```
Input:
 head = [1,2,3,4,5]

Output:
 [1,3,5,2,4]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg] 
 
```
Input:
 head = [2,1,3,5,6,4,7]

Output:
 [2,3,6,7,1,5,4]
```

 Constraints: 

 The number of nodes in the linked list is in the range [0, 10 4 ] . 
 
 -10 6 <= Node.val <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head) return head;
        ListNode* odd = head;
        ListNode* evenHead = head->next;
        ListNode* even = evenHead;
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        odd->next = evenHead;
        return head;
    }
};
```


## 622. Design Circular Queue

**Problem:** https://leetcode.com/problems/design-circular-queue/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Linked List, Design, Queue

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Linked list, Queue, Vector

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Constructor: O(k); each operation: O(1)

**Space complexity:** O(k) stored; O(1) per operation

**Complexity reasoning:** The constructor initializes a vector of capacity k; all queue operations use indices, modulo arithmetic, and constant-time vector access.

### Problem description

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer". 
 
 One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values. 
 
 Implement the MyCircularQueue class: 

 MyCircularQueue(k) Initializes the object with the size of the queue to be k . 
 
 int Front() Gets the front item from the queue. If the queue is empty, return -1 . 
 
 int Rear() Gets the last item from the queue. If the queue is empty, return -1 . 
 
 boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful. 
 
 boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful. 
 
 boolean isEmpty() Checks whether the circular queue is empty or not. 
 
 boolean isFull() Checks whether the circular queue is full or not. 

 You must solve the problem without using the built-in queue data structure in your programming language.  

 Example 1: 
 
```
Input

["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

Output

[null, true, true, true, false, 3, true, true, true, 4]

Explanation

MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear(); // return 3
myCircularQueue.isFull(); // return True
myCircularQueue.deQueue(); // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear(); // return 4
```

 Constraints: 

 1 <= k <= 1000 
 
 0 <= value <= 1000 
 
 At most 3000 calls will be made to  enQueue , deQueue ,  Front ,  Rear ,  isEmpty , and  isFull .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class MyCircularQueue {
private:
    vector<int> data;
    int head, tail, size, capacity;

public:
    MyCircularQueue(int k) : data(k), head(-1), tail(-1), size(0), capacity(k) {}

    bool enQueue(int value) {
        if (isFull()) return false;
        if (isEmpty()) head = 0;
        tail = (tail + 1) % capacity;
        data[tail] = value;
        size++;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) return false;
        if (head == tail) head = tail = -1;
        else head = (head + 1) % capacity;
        size--;
        return true;
    }

    int Front() { return isEmpty() ? -1 : data[head]; }
    int Rear() { return isEmpty() ? -1 : data[tail]; }
    bool isEmpty() { return size == 0; }
    bool isFull() { return size == capacity; }
};
```


## 641. Design Circular Deque

**Problem:** https://leetcode.com/problems/design-circular-deque/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Linked List, Design, Queue

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Linked list, Queue, Vector

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Constructor: O(k); each operation: O(1)

**Space complexity:** O(k) stored; O(1) per operation

**Complexity reasoning:** The constructor allocates k + 1 slots; front/back insertions, deletions, and queries update circular indices without shifting elements.

### Problem description

Design your implementation of the circular double-ended queue (deque). 
 
 Implement the MyCircularDeque class: 

 MyCircularDeque(int k) Initializes the deque with a maximum size of k . 
 
 boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise. 
 
 boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise. 
 
 boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise. 
 
 boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise. 
 
 int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty. 
 
 int getRear() Returns the last item from Deque. Returns -1 if the deque is empty. 
 
 boolean isEmpty() Returns true if the deque is empty, or false otherwise. 
 
 boolean isFull() Returns true if the deque is full, or false otherwise. 

 Example 1: 
 
```
Input

["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

Output

[null, true, true, true, false, 2, true, true, true, 4]

Explanation

MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1); // return True
myCircularDeque.insertLast(2); // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear(); // return 2
myCircularDeque.isFull(); // return True
myCircularDeque.deleteLast(); // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront(); // return 4
```

 Constraints: 

 1 <= k <= 1000 
 
 0 <= value <= 1000 
 
 At most 2000 calls will be made to insertFront , insertLast , deleteFront , deleteLast , getFront , getRear , isEmpty , isFull .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class MyCircularDeque {
    vector<int> data;
    int front, rear, size, capacity;

public:
    MyCircularDeque(int k) {
        capacity = k + 1;
        data.resize(capacity);
        front = 0;
        rear = 0;
        size = 0;
    }

    bool insertFront(int value) {
        if (isFull()) return false;
        front = (front - 1 + capacity) % capacity;
        data[front] = value;
        size++;
        return true;
    }

    bool insertLast(int value) {
        if (isFull()) return false;
        data[rear] = value;
        rear = (rear + 1) % capacity;
        size++;
        return true;
    }

    bool deleteFront() {
        if (isEmpty()) return false;
        front = (front + 1) % capacity;
        size--;
        return true;
    }

    bool deleteLast() {
        if (isEmpty()) return false;
        rear = (rear - 1 + capacity) % capacity;
        size--;
        return true;
    }

    int getFront() {
        return isEmpty() ? -1 : data[front];
    }

    int getRear() {
        return isEmpty() ? -1 : data[(rear - 1 + capacity) % capacity];
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == capacity - 1;
    }
};
```


## 707. Design Linked List

**Problem:** https://leetcode.com/problems/design-linked-list/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List, Design

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Stack / Queue

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Constructor: O(1); get/addAtIndex/deleteAtIndex: O(n); addAtHead: O(1); addAtTail: O(n)

**Space complexity:** O(n) stored; O(1) auxiliary per operation

**Complexity reasoning:** The doubly linked list holds n nodes. Indexed operations walk from the head up to the requested index; adding at the head touches only the sentinels.

### Problem description

Design your implementation of the linked list. You can choose to use a singly or doubly linked list. 
A node in a singly linked list should have two attributes: val and next . val is the value of the current node, and next is a pointer/reference to the next node. 
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed . 
 
 Implement the MyLinkedList class: 

 MyLinkedList() Initializes the MyLinkedList object. 
 
 int get(int index) Get the value of the index th node in the linked list. If the index is invalid, return -1 . 
 
 void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. 
 
 void addAtTail(int val) Append a node of value val as the last element of the linked list. 
 
 void addAtIndex(int index, int val) Add a node of value val before the index th node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted . 
 
 void deleteAtIndex(int index) Delete the index th node in the linked list, if the index is valid. 

 Example 1: 
 
```
Input

["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]

Output

[null, null, null, null, 2, null, 3]

Explanation

MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2); // linked list becomes 1->2->3
myLinkedList.get(1); // return 2
myLinkedList.deleteAtIndex(1); // now the linked list is 1->3
myLinkedList.get(1); // return 3
```

 Constraints: 

 0 <= index, val <= 1000 
 
 Please do not use the built-in LinkedList library. 
 
 At most 2000 calls will be made to get , addAtHead , addAtTail , addAtIndex and deleteAtIndex .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node(int x) : val(x), prev(nullptr), next(nullptr) {}
};

class MyLinkedList {
public:
    Node* head;
    Node* tail;
    int size;

    MyLinkedList() {
        head = new Node(0);
        tail = new Node(0);
        head->next = tail;
        tail->prev = head;
        size = 0;
    }

    int get(int index) {
        if (index < 0 || index >= size) return -1;
        Node* curr = head->next;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        return curr->val;
    }

    void addAtHead(int val) {
        addAtIndex(0, val);
    }

    void addAtTail(int val) {
        addAtIndex(size, val);
    }

    void addAtIndex(int index, int val) {
        if (index < 0 || index > size) return;
        Node* prevNode = head;
        for (int i = 0; i < index; i++) {
            prevNode = prevNode->next;
        }
        Node* newNode = new Node(val);
        newNode->next = prevNode->next;
        newNode->prev = prevNode;
        prevNode->next->prev = newNode;
        prevNode->next = newNode;
        size++;
    }

    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;
        Node* curr = head;
        for (int i = 0; i <= index; i++) {
            curr = curr->next;
        }
        curr->prev->next = curr->next;
        curr->next->prev = curr->prev;
        delete curr;
        size--;
    }
};
```


## 708. Insert into a Sorted Circular Linked List

**Problem:** https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary; O(1) new node

**Complexity reasoning:** The loop examines at most one full cycle of n nodes to find the insertion position, then changes two links.

### Problem description

Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list. 
 
 If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted. 
 
 If the list is empty (i.e., the given node is null ), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2019/01/19/example_1_before_65p.jpg] 

```
Input:
 head = [3,4,1], insertVal = 2

Output:
 [3,4,1,2]

Explanation:
 In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
```

 Example 2: 
 
```
Input:
 head = [], insertVal = 1

Output:
 [1]

Explanation:
 The list is empty (given head is 
null
). We create a new single circular list and return the reference to that single node.
```

 Example 3: 
 
```
Input:
 head = [1], insertVal = 0

Output:
 [1,0]
```

 Constraints: 

 The number of nodes in the list is in the range [0, 5 * 10 4 ] . 
 
 -10 6 <= Node.val, insertVal <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        Node* node = new Node(insertVal);
        if (!head) {
            node->next = node;
            return node;
        }
        Node* cur = head;
        while (true) {
            Node* next = cur->next;
            bool middle = cur->val <= insertVal && insertVal <= next->val;
            bool wrap = cur->val > next->val
                     && (insertVal >= cur->val || insertVal <= next->val);
            if (middle || wrap || next == head) {
                cur->next = node;
                node->next = next;
                return head;
            }
            cur = next;
        }
    }
};
```


## 716. Max Stack

**Problem:** https://leetcode.com/problems/max-stack/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Linked List, Stack, Design, Doubly-Linked List, Ordered Set

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Stack / Queue

**Data structures (inferred):** Linked list, Ordered map, Stack, Vector

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** push/pop/popMax: O(log d); top/peekMax: O(1)

**Space complexity:** O(n) stored; O(1) auxiliary per operation

**Complexity reasoning:** A list stores n stack values and a balanced map indexes d distinct values. Map insertion/erasure costs O(log d); list and vector-end operations are constant amortized time. top and rbegin are constant time.

### Problem description

Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element. 
 
 Implement the MaxStack class: 

 MaxStack() Initializes the stack object. 
 
 void push(int x) Pushes element x onto the stack. 
 
 int pop() Removes the element on top of the stack and returns it. 
 
 int top() Gets the element on the top of the stack without removing it. 
 
 int peekMax() Retrieves the maximum element in the stack without removing it. 
 
 int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one. 

 You must come up with a solution that supports O(1) for each top call and O(logn) for each other call. 

 Example 1: 
 
```
Input

["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]

Output

[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation

MaxStack stk = new MaxStack();
stk.push(5); // [
5
] the top of the stack and the maximum number is 5.
stk.push(1); // [
5
, 
1
] the top of the stack is 1, but the maximum is 5.
stk.push(5); // [5, 1, 
5
] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top(); // return 5, [5, 1, 
5
] the stack did not change.
stk.popMax(); // return 5, [
5
, 
1
] the stack is changed now, and the top is different from the max.
stk.top(); // return 1, [
5
, 
1
] the stack did not change.
stk.peekMax(); // return 5, [
5
, 
1
] the stack did not change.
stk.pop(); // return 1, [
5
] the top of the stack and the max element is now 5.
stk.top(); // return 5, [
5
] the stack did not change.
```

 Constraints: 

 -10 7 <= x <= 10 7 
 
 At most 10 5  calls will be made to push , pop , top , peekMax , and popMax . 
 
 There will be at least one element in the stack when pop , top , peekMax , or popMax is called.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class MaxStack {
    list<int> values;
    map<int, vector<list<int>::iterator>> positions;

public:
    MaxStack() {}

    void push(int x) {
        values.push_back(x);
        auto it = values.end();
        --it;
        positions[x].push_back(it);
    }

    int pop() {
        int x = values.back();
        values.pop_back();
        positions[x].pop_back();
        if (positions[x].empty()) {
            positions.erase(x);
        }
        return x;
    }

    int top() {
        return values.back();
    }

    int peekMax() {
        return positions.rbegin()->first;
    }

    int popMax() {
        int x = peekMax();
        auto& nodes = positions[x];
        values.erase(nodes.back());
        nodes.pop_back();
        if (nodes.empty()) {
            positions.erase(x);
        }
        return x;
    }
};
```


## 725. Split Linked List in Parts

**Problem:** https://leetcode.com/problems/split-linked-list-in-parts/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list, Vector

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + k)

**Space complexity:** O(k) output; O(1) auxiliary excluding output

**Complexity reasoning:** Count n nodes, traverse each node again while cutting parts, and create exactly k result pointers.

### Problem description

Given the head of a singly linked list and an integer k , split the linked list into k consecutive linked list parts. 
 
 The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null. 
 
 The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later. 
 
 Return an array of the k parts . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/06/13/split1-lc.jpg] 
 
```
Input:
 head = [1,2,3], k = 5

Output:
 [[1],[2],[3],[],[]]

Explanation:

The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/06/13/split2-lc.jpg] 
 
```
Input:
 head = [1,2,3,4,5,6,7,8,9,10], k = 3

Output:
 [[1,2,3,4],[5,6,7],[8,9,10]]

Explanation:

The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
```

 Constraints: 

 The number of nodes in the list is in the range [0, 1000] . 
 
 0 <= Node.val <= 1000 
 
 1 <= k <= 50

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int n = 0;
        for (ListNode* p = head; p; p = p->next) ++n;
        int base = n / k, extra = n % k;
        vector<ListNode*> result;
        for (int i = 0; i < k; ++i) {
            result.push_back(head);
            int len = base + (i < extra);
            for (int j = 1; j < len; ++j) head = head->next;
            if (len > 0) {
                ListNode* next = head->next;
                head->next = nullptr;
                head = next;
            }
        }
        return result;
    }
};
```


## 1206. Design Skiplist

**Problem:** https://leetcode.com/problems/design-skiplist/

**Difficulty:** Hard | **Premium:** No

**Tags:** Linked List, Design

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Stack / Queue

**Data structures (inferred):** Linked list, Vector

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Expected O(log n) per search/add/erase; worst O(n) per operation; destructor O(n)

**Space complexity:** O(n) expected stored; O(1) auxiliary per operation (16 fixed levels)

**Complexity reasoning:** Randomized levels give expected logarithmic traversal and constant expected pointers per node. The fixed 16-level cap allows linear worst-case scans; update arrays are fixed-size.

### Problem description

Design a Skiplist without using any built-in libraries. 
 
 A skiplist is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists is just simple linked lists. 
 
 For example, we have a Skiplist containing [30,40,50,60,70,90] and we want to add 80 and 45 into it. The Skiplist works this way: 
 
 [Figure: https://assets.leetcode.com/uploads/2019/09/27/1506_skiplist.gif] 
 Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons 
 
 You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, add, erase and search can be faster than O(n) . It can be proven that the average time complexity for each operation is O(log(n)) and space complexity is O(n) . 
 
 See more about Skiplist: https://en.wikipedia.org/wiki/Skip_list 
 
 Implement the Skiplist class: 

 Skiplist() Initializes the object of the skiplist. 
 
 bool search(int target) Returns true if the integer target exists in the Skiplist or false otherwise. 
 
 void add(int num) Inserts the value num into the SkipList. 
 
 bool erase(int num) Removes the value num from the Skiplist and returns true . If num does not exist in the Skiplist, do nothing and return false . If there exist multiple num values, removing any one of them is fine. 

 Note that duplicates may exist in the Skiplist, your code needs to handle this situation. 

 Example 1: 
 
```
Input

["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]

Output

[null, null, null, null, false, null, true, false, true, false]

Explanation

Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0); // return False
skiplist.add(4);
skiplist.search(1); // return True
skiplist.erase(0); // return False, 0 is not in skiplist.
skiplist.erase(1); // return True
skiplist.search(1); // return False, 1 has already been erased.
```

 Constraints: 

 0 <= num, target <= 2 * 10 4 
 
 At most 5 * 10 4 calls will be made to search , add , and erase .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Skiplist {
    static const int LEVELS = 16;
    struct Node {
        int value;
        vector<Node*> next;
        Node(int v, int level) : value(v), next(level, nullptr) {}
    };
    Node* head;
    mt19937 rng;
    int randomLevel() {
        int level = 1;
        while (level < LEVELS && (rng() & 1u)) ++level;
        return level;
    }
public:
    Skiplist() : head(new Node(-1, LEVELS)), rng(random_device{}()) {}
    ~Skiplist() {
        Node* p = head;
        while (p) {
            Node* next = p->next[0];
            delete p;
            p = next;
        }
    }
    bool search(int target) {
        Node* p = head;
        for (int l = LEVELS - 1; l >= 0; --l)
            while (p->next[l] && p->next[l]->value < target)
                p = p->next[l];
        p = p->next[0];
        return p && p->value == target;
    }
    void add(int num) {
        Node* update[LEVELS];
        Node* p = head;
        for (int l = LEVELS - 1; l >= 0; --l) {
            while (p->next[l] && p->next[l]->value < num)
                p = p->next[l];
            update[l] = p;
        }
        int level = randomLevel();
        Node* node = new Node(num, level);
        for (int l = 0; l < level; ++l) {
            node->next[l] = update[l]->next[l];
            update[l]->next[l] = node;
        }
    }
    bool erase(int num) {
        Node* update[LEVELS];
        Node* p = head;
        for (int l = LEVELS - 1; l >= 0; --l) {
            while (p->next[l] && p->next[l]->value < num)
                p = p->next[l];
            update[l] = p;
        }
        Node* node = p->next[0];
        if (!node || node->value != num) return false;
        for (int l = 0; l < static_cast<int>(node->next.size()); ++l)
            update[l]->next[l] = node->next[l];
        delete node;
        return true;
    }
};
```


## 1472. Design Browser History

**Problem:** https://leetcode.com/problems/design-browser-history/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Linked List, Stack, Design, Doubly-Linked List, Data Stream

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Linked list, Stack, Vector

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Constructor: O(h); visit: O(u); back/forward: O(L)

**Space complexity:** O(S) stored; O(L) returned string

**Complexity reasoning:** h is homepage length, u the visited URL length, L the returned URL length, and S total stored string characters. URL copies/assignments and returning a string cost time proportional to its length; index changes alone are O(1).

### Problem description

You have a browser of one tab where you start on the homepage and you can visit another url , get back in the history number of steps or move forward in the history number of steps . 
 
 Implement the BrowserHistory class: 

 BrowserHistory(string homepage) Initializes the object with the homepage  of the browser. 
 
 void visit(string url)  Visits  url from the current page. It clears up all the forward history. 
 
 string back(int steps)  Move steps back in history. If you can only return x steps in the history and steps > x , you will return only x steps. Return the current url  after moving back in history at most steps . 
 
 string forward(int steps)  Move steps forward in history. If you can only forward x steps in the history and steps > x , you will forward only  x steps. Return the current url  after forwarding in history at most steps . 

 Example: 
 
```
Input:

["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

Output:

[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:

BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com"); // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com"); // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com"); // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1); // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1); // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1); // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com"); // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2); // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2); // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7); // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
```

 Constraints: 

 1 <= homepage.length <= 20 
 
 1 <= url.length <= 20 
 
 1 <= steps <= 100 
 
 homepage and url consist of  '.' or lower case English letters. 
 
 At most 5000  calls will be made to visit , back , and forward .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <vector>

using namespace std;

class BrowserHistory {
    vector<string> history;
    int current, last;

public:
    BrowserHistory(string homepage) {
        history.push_back(homepage);
        current = 0;
        last = 0;
    }

    void visit(string url) {
        ++current;
        if (history.size() > current)
            history[current] = url;
        else
            history.push_back(url);
        last = current;
    }

    string back(int steps) {
        current = max(0, current - steps);
        return history[current];
    }

    string forward(int steps) {
        current = min(last, current + steps);
        return history[current];
    }
};
```


## 1474. Delete N Nodes After M Nodes of a Linked List

**Problem:** https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Each node is either skipped as one of m retained nodes or deleted among the next n nodes, so total pointer traversal and deletion are linear in list length.

### Problem description

You are given the head of a linked list and two integers m and n . 
 
 Traverse the linked list and remove some nodes in the following way: 

 Start with the head as the current node. 
 
 Keep the first m nodes starting with the current node. 
 
 Remove the next n nodes 
 
 Keep repeating steps 2 and 3 until you reach the end of the list. 

 Return the head of the modified list after removing the mentioned nodes . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/06/06/sample_1_1848.png] 
 
```
Input:
 head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3

Output:
 [1,2,6,7,11,12]

Explanation:
 Keep the first (m = 2) nodes starting from the head of the linked List (1 ->2) show in black nodes.
Delete the next (n = 3) nodes (3 -> 4 -> 5) show in read nodes.
Continue with the same procedure until reaching the tail of the Linked List.
Head of the linked list after removing nodes is returned.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/06/06/sample_2_1848.png] 
 
```
Input:
 head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3

Output:
 [1,5,9]

Explanation:
 Head of linked list after removing nodes is returned.
```

 Constraints: 

 The number of nodes in the list is in the range [1, 10 4 ] . 
 
 1 <= Node.val <= 10 6 
 
 1 <= m, n <= 1000 

 Follow up: Could you solve this problem by modifying the list in-place?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    ListNode* deleteNodes(ListNode* head, int m, int n) {
        ListNode* current = head;
        while (current) {
            for (int kept = 1; kept < m && current; ++kept) {
                current = current->next;
            }
            if (!current) {
                break;
            }
            ListNode* removed = current->next;
            for (int i = 0; i < n && removed; ++i) {
                ListNode* next = removed->next;
                delete removed;
                removed = next;
            }
            current->next = removed;
            current = removed;
        }
        return head;
    }
};
```


## 1669. Merge In Between Linked Lists

**Problem:** https://leetcode.com/problems/merge-in-between-linked-lists/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(a + (b - a + 1) + m) = O(b + m)

**Space complexity:** O(1)

**Complexity reasoning:** Traverse to position a, advance past b, then scan m nodes to find list2 tail before splicing; m is list2 length.

### Problem description

You are given two linked lists: list1 and list2 of sizes n and m respectively. 
 
 Remove list1 's nodes from the a th node to the b th node, and put list2 in their place. 
 
 The blue edges and nodes in the following figure indicate the result: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/05/fig1.png] 
 
 Build the result list and return its head. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2024/03/01/ll.png] 
 
```
Input:
 list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]

Output:
 [10,1,13,1000000,1000001,1000002,5]

Explanation:
 We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/05/merge_linked_list_ex2.png] 
 
```
Input:
 list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]

Output:
 [0,1,1000000,1000001,1000002,1000003,1000004,6]

Explanation:
 The blue edges and nodes in the above figure indicate the result.
```

 Constraints: 

 3 <= list1.length <= 10 4 
 
 1 <= a <= b < list1.length - 1 
 
 1 <= list2.length <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp

class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *prev = nullptr, *after = list1;
        for (int i = 0; i < a; ++i) {
            prev = after;
            after = after->next;
        }
        for (int i = a; i <= b; ++i)
            after = after->next;

        ListNode* tail = list2;
        while (tail->next) tail = tail->next;

        prev->next = list2;
        tail->next = after;
        return list1;
    }
};
```


## 1670. Design Front Middle Back Queue

**Problem:** https://leetcode.com/problems/design-front-middle-back-queue/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Linked List, Design, Queue, Doubly-Linked List, Data Stream

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Deque, Linked list, Queue

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1) per operation (amortized)

**Space complexity:** O(n) stored; O(1) auxiliary per operation

**Complexity reasoning:** Two std::deque containers support constant-time end operations; balance transfers at most one element between ends per call.

### Problem description

Design a queue that supports push and pop operations in the front, middle, and back. 
 
 Implement the FrontMiddleBack class: 

 FrontMiddleBack() Initializes the queue. 
 
 void pushFront(int val) Adds val to the front of the queue. 
 
 void pushMiddle(int val) Adds val to the middle of the queue. 
 
 void pushBack(int val) Adds val to the back of the queue. 
 
 int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1 . 
 
 int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1 . 
 
 int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1 . 

 Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example: 

 Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6 , 3, 4, 5] . 
 
 Popping the middle from [1, 2, 3 , 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6] . 

 Example 1: 
 
```
Input:

["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]

Output:

[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:

FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1); // [
1
]
q.pushBack(2); // [1, 
2
]
q.pushMiddle(3); // [1, 
3
, 2]
q.pushMiddle(4); // [1, 
4
, 3, 2]
q.popFront(); // return 1 -> [4, 3, 2]
q.popMiddle(); // return 3 -> [4, 2]
q.popMiddle(); // return 4 -> [2]
q.popBack(); // return 2 -> []
q.popFront(); // return -1 -> [] (The queue is empty)
```

 Constraints: 

 1 <= val <= 10 9 
 
 At most  1000  calls will be made to  pushFront ,  pushMiddle ,  pushBack , popFront , popMiddle , and popBack .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <deque>

using namespace std;

class FrontMiddleBackQueue {
    deque<int> front, back;

    void balance() {
        if (front.size() > back.size()) {
            back.push_front(front.back());
            front.pop_back();
        } else if (back.size() > front.size() + 1) {
            front.push_back(back.front());
            back.pop_front();
        }
    }

public:
    void pushFront(int val) {
        front.push_front(val);
        balance();
    }

    void pushMiddle(int val) {
        if (front.size() < back.size())
            front.push_back(val);
        else
            back.push_front(val);
    }

    void pushBack(int val) {
        back.push_back(val);
        balance();
    }

    int popFront() {
        if (front.empty() && back.empty()) return -1;
        int val;
        if (!front.empty()) {
            val = front.front();
            front.pop_front();
        } else {
            val = back.front();
            back.pop_front();
        }
        balance();
        return val;
    }

    int popMiddle() {
        if (front.empty() && back.empty()) return -1;
        int val;
        if (front.size() == back.size()) {
            val = front.back();
            front.pop_back();
        } else {
            val = back.front();
            back.pop_front();
        }
        return val;
    }

    int popBack() {
        if (front.empty() && back.empty()) return -1;
        int val = back.back();
        back.pop_back();
        balance();
        return val;
    }
};
```


## 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

**Problem:** https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list, Vector

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** The three-node sliding window advances once per node and records only the first/last critical positions and minimum gap.

### Problem description

A critical point in a linked list is defined as either a local maxima or a local minima . 
 
 A node is a local maxima if the current node has a value strictly greater than the previous node and the next node. 
 
 A node is a local minima if the current node has a value strictly smaller than the previous node and the next node. 
 
 Note that a node can only be a local maxima/minima if there exists both a previous node and a next node. 
 
 Given a linked list head , return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1] . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/13/a1.png] 
 
```
Input:
 head = [3,1]

Output:
 [-1,-1]

Explanation:
 There are no critical points in [3,1].
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/13/a2.png] 
 
```
Input:
 head = [5,3,1,2,5,1,2]

Output:
 [1,3]

Explanation:
 There are three critical points:
- [5,3,
1
,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,
5
,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,
1
,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/14/a5.png] 
 
```
Input:
 head = [1,3,2,2,3,2,2,2,7]

Output:
 [3,3]

Explanation:
 There are two critical points:
- [1,
3
,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,
3
,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.
```

 Constraints: 

 The number of nodes in the list is in the range [2, 10 5 ] . 
 
 1 <= Node.val <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head){
        int first=-1,last=-1,mn=INT_MAX,idx=1;
        ListNode *prev=head,*cur=head->next;
        while(cur&&cur->next){
            if((cur->val>prev->val&&cur->val>cur->next->val)||
               (cur->val<prev->val&&cur->val<cur->next->val)){
                if(first==-1)first=idx;
                if(last!=-1)mn=min(mn,idx-last);
                last=idx;
            }
            prev=cur;cur=cur->next;++idx;
        }
        if(first==last)return {-1,-1};return {mn,last-first};
    }
};
```


## 2074. Reverse Nodes in Even Length Groups

**Problem:** https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Each group is counted once and even-length groups are reversed in place; total nodes scanned and rewired are O(n).

### Problem description

You are given the head of a linked list. 
 
 The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers ( 1, 2, 3, 4, ... ). The length of a group is the number of nodes assigned to it. In other words, 

 The 1 st node is assigned to the first group. 
 
 The 2 nd and the 3 rd nodes are assigned to the second group. 
 
 The 4 th , 5 th , and 6 th nodes are assigned to the third group, and so on. 

 Note that the length of the last group may be less than or equal to 1 + the length of the second to last group . 
 
 Reverse the nodes in each group with an even length, and return the head of the modified linked list . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/25/eg1.png] 
 
```
Input:
 head = [5,2,6,3,9,1,7,3,8,4]

Output:
 [5,6,2,3,9,1,4,8,3,7]

Explanation:

- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/25/eg2.png] 
 
```
Input:
 head = [1,1,0,6]

Output:
 [1,0,1,6]

Explanation:

- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 1. No reversal occurs.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/11/17/ex3.png] 
 
```
Input:
 head = [1,1,0,6,5]

Output:
 [1,0,1,5,6]

Explanation:

- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 2. The nodes are reversed.
```

 Constraints: 

 The number of nodes in the list is in the range [1, 10 5 ] . 
 
 0 <= Node.val <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        ListNode dummy(0); dummy.next=head;
        ListNode* before=&dummy;
        for (int group=1;before->next;++group) {
            ListNode* end=before;
            int count=0;
            while (count<group && end->next) {end=end->next;++count;}
            ListNode* after=end->next;
            if (count%2==0) {
                ListNode* curr=before->next;
                ListNode* prev=after;
                for (int i=0;i<count;++i) {
                    ListNode* next=curr->next;
                    curr->next=prev;prev=curr;curr=next;
                }
                ListNode* oldFirst=before->next;
                before->next=prev;
                before=oldFirst;
            } else before=end;
        }
        return dummy.next;
    }
};
```


## 2181. Merge Nodes in Between Zeros

**Problem:** https://leetcode.com/problems/merge-nodes-in-between-zeros/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List, Simulation

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Simulation / Implementation

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** The read pointer traverses each value and zero separator once, accumulating segment sums and relinking existing nodes.

### Problem description

You are given the head of a linked list, which contains a series of integers separated by 0 's. The beginning and end of the linked list will have Node.val == 0 . 
 
 For every two consecutive 0 's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0 's. 
 
 Return the head of the modified linked list . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/02/ex1-1.png] 
 
```
Input:
 head = [0,3,1,0,4,5,2,0]

Output:
 [4,11]

Explanation:
 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/02/ex2-1.png] 
 
```
Input:
 head = [0,1,0,3,0,2,2,0]

Output:
 [1,3,4]

Explanation:
 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
```

 Constraints: 

 The number of nodes in the list is in the range [3, 2 * 10 5 ] . 
 
 0 <= Node.val <= 1000 
 
 There are no two consecutive nodes with Node.val == 0 . 
 
 The beginning and end of the linked list have Node.val == 0 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* write=head;
        ListNode* cur=head->next;
        while(cur) {
            int sum=0;
            while(cur&&cur->val!=0){sum+=cur->val;cur=cur->next;}
            if(sum==0) break;
            write->val=sum;
            if(!cur||!cur->next){write->next=nullptr;break;}
            write->next=cur;write=cur;cur=cur->next;
        }
        return head;
    }
};
```


## 2326. Spiral Matrix IV

**Problem:** https://leetcode.com/problems/spiral-matrix-iv/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Linked List, Matrix, Simulation

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Linked list, Vector

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(mn)

**Space complexity:** O(mn)

**Complexity reasoning:** Initializing the m-by-n matrix dominates; each linked-list node is placed once with constant-time direction checks.

### Problem description

You are given two integers m and n , which represent the dimensions of a matrix. 
 
 You are also given the head of a linked list of integers. 
 
 Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise) , starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1 . 
 
 Return the generated matrix . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/05/09/ex1new.jpg] 
 
```
Input:
 m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]

Output:
 [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]

Explanation:
 The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/05/11/ex2.jpg] 
 
```
Input:
 m = 1, n = 4, head = [0,1,2]

Output:
 [[0,1,2,-1]]

Explanation:
 The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
```

 Constraints: 

 1 <= m, n <= 10 5 
 
 1 <= m * n <= 10 5 
 
 The number of nodes in the list is in the range [1, m * n] . 
 
 0 <= Node.val <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:vector<vector<int>> spiralMatrix(int m,int n,ListNode* head){vector<vector<int>> a(m,vector<int>(n,-1));int dr[]={0,1,0,-1},dc[]={1,0,-1,0},r=0,c=0,d=0;while(head){a[r][c]=head->val;head=head->next;if(!head)break;int nr=r+dr[d],nc=c+dc[d];if(nr<0||nr>=m||nc<0||nc>=n||a[nr][nc]!=-1){d=(d+1)%4;nr=r+dr[d];nc=c+dc[d];}r=nr;c=nc;}return a;}};
```


## 3062. Winner of the Linked List Game

**Problem:** https://leetcode.com/problems/winner-of-the-linked-list-game/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers

**Data structures (inferred):** Linked list

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** The pointer advances by two nodes per round, comparing one pair and updating two counters.

### Problem description

You are given the head of a linked list of even length containing integers. 
 
 Each odd-indexed node contains an odd integer and each even-indexed node contains an even integer. 
 
 We call each even-indexed node and its next node a pair , e.g., the nodes with indices 0 and 1 are a pair, the nodes with indices 2 and 3 are a pair, and so on. 
 
 For every pair , we compare the values of the nodes in the pair: 

 If the odd-indexed node is higher, the "Odd" team gets a point. 
 
 If the even-indexed node is higher, the "Even" team gets a point. 

 Return the name of the team with the higher points, if the points are equal, return "Tie" . 

 Example 1: 

 Input: head = [2,1] 
 
 Output: "Even" 
 
 Explanation: There is only one pair in this linked list and that is (2,1) . Since 2 > 1 , the Even team gets the point. 
 
 Hence, the answer would be "Even" . 

 Example 2: 

 Input: head = [2,5,4,7,20,5] 
 
 Output: "Odd" 
 
 Explanation: There are 3 pairs in this linked list. Let's investigate each pair individually: 
 
 (2,5) -> Since 2 < 5 , The Odd team gets the point. 
 
 (4,7) -> Since 4 < 7 , The Odd team gets the point. 
 
 (20,5) -> Since 20 > 5 , The Even team gets the point. 
 
 The Odd team earned 2 points while the Even team got 1 point and the Odd team has the higher points. 
 
 Hence, the answer would be "Odd" . 

 Example 3: 

 Input: head = [4,5,2,1] 
 
 Output: "Tie" 
 
 Explanation: There are 2 pairs in this linked list. Let's investigate each pair individually: 
 
 (4,5) -> Since 4 < 5 , the Odd team gets the point. 
 
 (2,1) -> Since 2 > 1 , the Even team gets the point. 
 
 Both teams earned 1 point. 
 
 Hence, the answer would be "Tie" . 

 Constraints: 

 The number of nodes in the list is in the range [2, 100] . 
 
 The number of nodes in the list is even. 
 
 1 <= Node.val <= 100 
 
 The value of each odd-indexed node is odd. 
 
 The value of each even-indexed node is even.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string gameResult(ListNode* head) {
        int even = 0, odd = 0;
        while (head && head->next) {
            if (head->val > head->next->val) ++even;
            else ++odd;
            head = head->next->next;
        }
        return even > odd ? "Even" : odd > even ? "Odd" : "Tie";
    }
};
```


## 3263. Convert Doubly Linked List to Array I

**Problem:** https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Linked List, Doubly-Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Simulation / Implementation

**Data structures (inferred):** Array / vector, Linked list, Vector

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output; O(1) auxiliary excluding output

**Complexity reasoning:** Traverse n nodes once and append each value to the result vector.

### Problem description

You are given the head of a doubly linked list , which contains nodes that have a next pointer and a previous pointer. 
 
 Return an integer array which contains the elements of the linked list in order . 

 Example 1: 

 Input: head = [1,2,3,4,3,2,1] 
 
 Output: [1,2,3,4,3,2,1] 

 Example 2: 

 Input: head = [2,2,2,2,2] 
 
 Output: [2,2,2,2,2] 

 Example 3: 

 Input: head = [3,2,3,2,3,2] 
 
 Output: [3,2,3,2,3,2] 

 Constraints: 

 The number of nodes in the given list is in the range [1, 50] . 
 
 1 <= Node.val <= 50

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/* LeetCode supplies the doubly-linked-list Node definition. */
class Solution {
public:
    vector<int> toArray(Node* head) {
        vector<int> result;
        for (Node* cur = head; cur != nullptr; cur = cur->next) {
            result.push_back(cur->val);
        }
        return result;
    }
};
```


## 3294. Convert Doubly Linked List to Array II

**Problem:** https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Linked List, Doubly-Linked List

**Primary pattern:** Linked List / Pointers

**Related patterns:** Linked List / Pointers, Simulation / Implementation

**Data structures (inferred):** Array / vector, Linked list, Vector

**Pattern recognition:** Rewire node links while preserving ownership and pointer invariants.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output; O(1) auxiliary excluding output

**Complexity reasoning:** Walk backward to the head and then forward through the n-node list, appending all values to a vector.

### Problem description

You are given an arbitrary node from a doubly linked list , which contains nodes that have a next pointer and a previous pointer. 
 
 Return an integer array which contains the elements of the linked list in order . 

 Example 1: 

 Input: head = [1,2,3,4,5], node = 5 
 
 Output: [1,2,3,4,5] 

 Example 2: 

 Input: head = [4,5,6,7,8], node = 8 
 
 Output: [4,5,6,7,8] 

 Constraints: 

 The number of nodes in the given list is in the range [1, 500] . 
 
 1 <= Node.val <= 1000 
 
 All nodes have unique Node.val .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/* LeetCode supplies the doubly-linked-list Node definition. */
class Solution {
public:
    vector<int> toArray(Node* node) {
        if (!node) return {};
        while (node->prev) node = node->prev;
        vector<int> result;
        while (node) {
            result.push_back(node->val);
            node = node->next;
        }
        return result;
    }
};
```

