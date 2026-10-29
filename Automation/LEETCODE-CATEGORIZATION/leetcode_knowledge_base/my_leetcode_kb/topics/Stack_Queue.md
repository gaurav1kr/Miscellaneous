# Stack / Queue

**Problems:** 19

## Quick revision checklist

LIFO/FIFO processing, parser state, or online operations.

## Problem index

- [155. Min Stack](#155-min-stack) — Medium; code: yes
- [225. Implement Stack using Queues](#225-implement-stack-using-queues) — Easy; code: yes
- [232. Implement Queue using Stacks](#232-implement-queue-using-stacks) — Easy; code: yes
- [281. Zigzag Iterator](#281-zigzag-iterator) — Medium; code: yes
- [284. Peeking Iterator](#284-peeking-iterator) — Medium; code: yes
- [346. Moving Average from Data Stream](#346-moving-average-from-data-stream) — Easy; code: yes
- [636. Exclusive Time of Functions](#636-exclusive-time-of-functions) — Medium; code: yes
- [682. Baseball Game](#682-baseball-game) — Easy; code: yes
- [735. Asteroid Collision](#735-asteroid-collision) — Medium; code: yes
- [933. Number of Recent Calls](#933-number-of-recent-calls) — Easy; code: yes
- [946. Validate Stack Sequences](#946-validate-stack-sequences) — Medium; code: yes
- [1381. Design a Stack With Increment Operation](#1381-design-a-stack-with-increment-operation) — Medium; code: yes
- [1441. Build an Array With Stack Operations](#1441-build-an-array-with-stack-operations) — Medium; code: yes
- [1476. Subrectangle Queries](#1476-subrectangle-queries) — Medium; code: yes
- [1700. Number of Students Unable to Eat Lunch](#1700-number-of-students-unable-to-eat-lunch) — Easy; code: yes
- [2069. Walking Robot Simulation II](#2069-walking-robot-simulation-ii) — Medium; code: yes
- [2073. Time Needed to Buy Tickets](#2073-time-needed-to-buy-tickets) — Easy; code: yes
- [2534. Time Taken to Cross the Door](#2534-time-taken-to-cross-the-door) — Hard; code: yes
- [3834. Merge Adjacent Equal Elements](#3834-merge-adjacent-equal-elements) — Medium; code: yes

---

## 155. Min Stack

**Problem:** https://leetcode.com/problems/min-stack/

**Difficulty:** Medium | **Premium:** No

**Tags:** Stack, Design

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue

**Data structures (inferred):** Stack

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. 
 
 Implement the MinStack class: 

 MinStack() initializes the stack object. 
 
 void push(int value) pushes the element value onto the stack. 
 
 void pop() removes the element on the top of the stack. 
 
 int top() gets the top element of the stack. 
 
 int getMin() retrieves the minimum element in the stack. 

 You must implement a solution with O(1) time complexity for each function. 

 Example 1: 
 
```
Input

["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output

[null,null,null,null,-3,null,0,-2]

Explanation

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top(); // return 0
minStack.getMin(); // return -2
```

 Constraints: 

 -2 31 <= val <= 2 31 - 1 
 
 Methods pop , top and getMin operations will always be called on non-empty stacks. 
 
 At most 3 * 10 4 calls will be made to push , pop , top , and getMin .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <stack>

using namespace std;

class MinStack {
    stack<int> s, min_s;
public:
    void push(int val) {
        s.push(val);
        if (min_s.empty() || val <= min_s.top()) min_s.push(val);
    }
    void pop() {
        if (s.top() == min_s.top()) min_s.pop();
        s.pop();
    }
    int top() { return s.top(); }
    int getMin() { return min_s.top(); }
};
```


## 225. Implement Stack using Queues

**Problem:** https://leetcode.com/problems/implement-stack-using-queues/

**Difficulty:** Easy | **Premium:** No

**Tags:** Stack, Design, Queue

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue

**Data structures (inferred):** Queue, Stack

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack ( push , top , pop , and empty ). 
 
 Implement the MyStack class: 

 void push(int x) Pushes element x to the top of the stack. 
 
 int pop() Removes the element on the top of the stack and returns it. 
 
 int top() Returns the element on the top of the stack. 
 
 boolean empty() Returns true if the stack is empty, false otherwise. 

 Notes: 

 You must use only standard operations of a queue, which means that only push to back , peek/pop from front , size and is empty operations are valid. 
 
 Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations. 

 Example 1: 
 
```
Input

["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

Output

[null, null, null, 2, 2, false]

Explanation

MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
```

 Constraints: 

 1 <= x <= 9 
 
 At most 100 calls will be made to push , pop , top , and empty . 
 
 All the calls to pop and top are valid. 

 Follow-up: Can you implement the stack using only one queue?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class MyStack 
{
    queue<int> q1;
    queue<int> q2 ;
public:
    MyStack()
    {
        
    }
    
    void push(int x) 
    {
        q2.push(x);
        while (!q1.empty()) 
        {
            q2.push(q1.front());
            q1.pop();
        }
        queue<int> q = q1;
        q1 = q2;
        q2 = q;
    }
    
    int pop() 
    {
        if (q1.empty())
            return -1;
        int x = q1.front() ;
        q1.pop();
        return x ;
    }
    
    int top() 
    {
          if (q1.empty())
            return -1;
        return q1.front();  
    }
    
    bool empty() 
    {
        return q1.empty() ;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
```


## 232. Implement Queue using Stacks

**Problem:** https://leetcode.com/problems/implement-queue-using-stacks/

**Difficulty:** Easy | **Premium:** No

**Tags:** Stack, Design, Queue

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue

**Data structures (inferred):** Queue, Stack

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue ( push , peek , pop , and empty ). 
 
 Implement the MyQueue class: 

 void push(int x) Pushes element x to the back of the queue. 
 
 int pop() Removes the element from the front of the queue and returns it. 
 
 int peek() Returns the element at the front of the queue. 
 
 boolean empty() Returns true if the queue is empty, false otherwise. 

 Notes: 

 You must use only standard operations of a stack, which means only push to top , peek/pop from top , size , and is empty operations are valid. 
 
 Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations. 

 Example 1: 
 
```
Input

["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output

[null, null, null, 1, 1, false]

Explanation

MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```

 Constraints: 

 1 <= x <= 9 
 
 At most 100  calls will be made to push , pop , peek , and empty . 
 
 All the calls to pop and peek are valid. 

 Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class MyQueue {
    stack<int> input, output;
public:
    void push(int x) {
        input.push(x);
    }
    int pop() {
        peek();
        int val = output.top(); output.pop();
        return val;
    }
    int peek() {
        if (output.empty()) {
            while (!input.empty()) {
                output.push(input.top());
                input.pop();
            }
        }
        return output.top();
    }
    bool empty() {
        return input.empty() && output.empty();
    }
};
```


## 281. Zigzag Iterator

**Problem:** https://leetcode.com/problems/zigzag-iterator/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Design, Queue, Iterator

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Queue, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given two vectors of integers v1 and v2 , implement an iterator to return their elements alternately. 
 
 Implement the ZigzagIterator class: 

 ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2 . 
 
 boolean hasNext() returns true if the iterator still has elements, and false otherwise. 
 
 int next() returns the current element of the iterator and moves the iterator to the next element. 

 Example 1: 
 
```
Input:
 v1 = [1,2], v2 = [3,4,5,6]

Output:
 [1,3,2,4,5,6]

Explanation:
 By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
```

 Example 2: 
 
```
Input:
 v1 = [1], v2 = []

Output:
 [1]
```

 Example 3: 
 
```
Input:
 v1 = [], v2 = [1]

Output:
 [1]
```

 Constraints: 

 0 <= v1.length, v2.length <= 1000 
 
 1 <= v1.length + v2.length <= 2000 
 
 -2 31 <= v1[i], v2[i] <= 2 31 - 1 

 Follow up: What if you are given k vectors? How well can your code be extended to such cases? 
 
 Clarification for the follow-up question: 
 
 The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". 
 
 Follow-up Example: 
 
```
Input:
 v1 = [1,2,3], v2 = [4,5,6,7], v3 = [8,9]

Output:
 [1,4,8,2,5,9,3,6,7]
```

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class ZigzagIterator
{
    vector< vector< int >>a;
    queue< pair< int, int >>q;
public:
    ZigzagIterator(vector< int>& v1, vector< int>& v2) : a
    {
        v1, v2
    }
    {
        for (int i = 0; i < 2;++i) if(!a[i].empty()) q.push( { i, 0 });
    }
    int next()
    {
        auto p = q.front();
        q.pop();
        int x = a[p.first][p.second];
        if (p.second + 1 < (int) a[p.first].size()) q.push( { p.first, p.second + 1 });
        return x;
    }
    bool hasNext()
    {
        return !q.empty();
    }
};
```


## 284. Peeking Iterator

**Problem:** https://leetcode.com/problems/peeking-iterator/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Design, Iterator

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations. 
 
 Implement the PeekingIterator class: 

 PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator . 
 
 int next() Returns the next element in the array and moves the pointer to the next element. 
 
 boolean hasNext() Returns true if there are still elements in the array. 
 
 int peek() Returns the next element in the array without moving the pointer. 

 Note: Each language may have a different implementation of the constructor and Iterator , but they all support the int next() and boolean hasNext() functions. 

 Example 1: 
 
```
Input

["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]

Output

[null, 1, 2, 2, 3, false]

Explanation

PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [
1
,2,3]
peekingIterator.next(); // return 1, the pointer moves to the next element [1,
2
,3].
peekingIterator.peek(); // return 2, the pointer does not move [1,
2
,3].
peekingIterator.next(); // return 2, the pointer moves to the next element [1,2,
3
]
peekingIterator.next(); // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False
```

 Constraints: 

 1 <= nums.length <= 1000 
 
 1 <= nums[i] <= 1000 
 
 All the calls to next and peek are valid. 
 
 At most 1000 calls will be made to next , hasNext , and peek . 

 Follow up: How would you extend your design to be generic and work with all types, not just integer?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class PeekingIterator : public Iterator {
    bool hasPeeked;
    int peekedElem;
public:
	PeekingIterator(const vector<int>& num) : Iterator(num) {
        hasPeeked = false;
	}

	int peek() {
        peekedElem = hasPeeked?peekedElem:Iterator::next();
        hasPeeked = true;
        return peekedElem;
	}

	int next() {
	    int nextElem = hasPeeked?peekedElem:Iterator::next();
	    hasPeeked = false;
	    return nextElem;
	}

	bool hasNext() const {
	    return hasPeeked||Iterator::hasNext();
	}
};
```


## 346. Moving Average from Data Stream

**Problem:** https://leetcode.com/problems/moving-average-from-data-stream/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Design, Queue, Data Stream

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Queue

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window. 
 
 Implement the  MovingAverage class: 

 MovingAverage(int size) Initializes the object with the size of the window size . 
 
 double next(int val) Returns the moving average of the last size values of the stream. 

 Example 1: 
 
```
Input

["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]

Output

[null, 1.0, 5.5, 4.66667, 6.0]

Explanation

MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
```

 Constraints: 

 1 <= size <= 1000 
 
 -10 5 <= val <= 10 5 
 
 At most 10 4 calls will be made to next .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class MovingAverage
{
    queue<int> window;
    int capacity;
    long long sum = 0;
public:
    MovingAverage(int size) : capacity(size) {}
    double next(int val)
    {
        window.push(val);
        sum += val;
        if ((int)window.size() > capacity)
        {
            sum -= window.front();
            window.pop();
        }
        return (double)sum / window.size();
    }
};
```


## 636. Exclusive Time of Functions

**Problem:** https://leetcode.com/problems/exclusive-time-of-functions/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Stack

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Stack, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n - 1 . 
 
 Function calls are stored in a call stack : when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed . Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp. 
 
 You are given a list logs , where logs[i] represents the i th log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}" . For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively . 
 
 A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3 . 
 
 Return the exclusive time of each function in an array, where the value at the i th index represents the exclusive time for the function with ID i . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2019/04/05/diag1b.png] 
 
```
Input:
 n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]

Output:
 [3,4]

Explanation:

Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
```

 Example 2: 
 
```
Input:
 n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]

Output:
 [8]

Explanation:

Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls itself again.
Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.
```

 Example 3: 
 
```
Input:
 n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]

Output:
 [7,1]

Explanation:

Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls function 1.
Function 1 starts at the beginning of time 6, executes 1 unit of time, and ends at the end of time 6.
Function 0 resumes execution at the beginning of time 7 and executes for 1 unit of time.
So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1 spends 1 unit of total time executing.
```

 Constraints: 

 1 <= n <= 100 
 
 2 <= logs.length <= 500 
 
 0 <= function_id < n 
 
 0 <= timestamp <= 10 9 
 
 No two start events will happen at the same timestamp. 
 
 No two end events will happen at the same timestamp. 
 
 Each function has an "end" log for each "start" log.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> result(n, 0);
        stack<int> st;
        int prevTime = 0;

        for (string& log : logs) {
            int pos1 = log.find(":"), pos2 = log.rfind(":");
            int id = stoi(log.substr(0, pos1));
            string type = log.substr(pos1 + 1, pos2 - pos1 - 1);
            int timestamp = stoi(log.substr(pos2 + 1));

            if (!st.empty()) {
                result[st.top()] += timestamp - prevTime;
            }
            prevTime = timestamp;

            if (type == "start") {
                st.push(id);
            } else {
                result[st.top()]++;
                st.pop();
                prevTime++;
            }
        }

        return result;
    }
};
```


## 682. Baseball Game

**Problem:** https://leetcode.com/problems/baseball-game/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Stack, Simulation

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Stack, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record. 
 
 You are given a list of strings operations , where operations[i] is the i th operation you must apply to the record and is one of the following: 

 An integer x .

 Record a new score of x . 

 '+' .

 Record a new score that is the sum of the previous two scores. 

 'D' .

 Record a new score that is the double of the previous score. 

 'C' .

 Invalidate the previous score, removing it from the record. 

 Return the sum of all the scores on the record after applying all the operations . 
 
 The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid. 

 Example 1: 
 
```
Input:
 ops = ["5","2","C","D","+"]

Output:
 30

Explanation:

"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
```

 Example 2: 
 
```
Input:
 ops = ["5","-2","4","C","D","9","+","+"]

Output:
 27

Explanation:

"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
```

 Example 3: 
 
```
Input:
 ops = ["1","C"]

Output:
 0

Explanation:

"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.
```

 Constraints: 

 1 <= operations.length <= 1000 
 
 operations[i] is "C" , "D" , "+" , or a string representing an integer in the range [-3 * 10 4 , 3 * 10 4 ] . 
 
 For operation "+" , there will always be at least two previous scores on the record. 
 
 For operations "C" and "D" , there will always be at least one previous score on the record.

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <vector>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    int calPoints(vector<string>& ops) {
        stack<int> stack;
        
        for (string& op : ops) {
            if (op == "+") {
                int top = stack.top(); stack.pop();
                int newTop = top + stack.top();
                stack.push(top);
                stack.push(newTop);
            } else if (op == "D") {
                stack.push(stack.top() * 2);
            } else if (op == "C") {
                stack.pop();
            } else {
                stack.push(stoi(op));
            }
        }
        
        int result = 0;
        while (!stack.empty()) {
            result += stack.top();
            stack.pop();
        }
        
        return result;
    }
};
```


## 735. Asteroid Collision

**Problem:** https://leetcode.com/problems/asteroid-collision/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Stack, Simulation

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Stack, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space. 
 
 For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. 
 
 Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet. 

 Example 1: 
 
```
Input:
 asteroids = [5,10,-5]

Output:
 [5,10]

Explanation:
 The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
```

 Example 2: 
 
```
Input:
 asteroids = [8,-8]

Output:
 []

Explanation:
 The 8 and -8 collide exploding each other.
```

 Example 3: 
 
```
Input:
 asteroids = [10,2,-5]

Output:
 [10]

Explanation:
 The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
```

 Example 4: 
 
```
Input:
 asteroids = [3,5,-6,2,-1,4]​​​​​​​

Output:
 [-6,2,4]

Explanation:
 The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 destroys -1. Since 2 and 4 are both moving right, they never collide.
```

 Constraints: 

 2 <= asteroids.length <= 10 4 
 
 -1000 <= asteroids[i] <= 1000 
 
 asteroids[i] != 0

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& astr) {
        int prev = -1;
        for (int i = 0; i < astr.size(); i++) {
            bool notSame = true;
            if (astr[i] > 0) {
                astr[++prev] = astr[i];
            } else {
                while (prev >= 0 && astr[prev] > 0) {
                    if (astr[prev] < -astr[i]) {
                        prev--;
                    } else if (astr[prev] == -astr[i]) {
                        prev--;
                        notSame = false;
                        break;
                    } else {

                        break;
                    }
                }

                if (notSame && (prev < 0 || astr[prev] < 0)) {
                    astr[++prev] = astr[i];
                }
            }
        }

        astr.resize(prev + 1);
        return astr;
    }
};
```


## 933. Number of Recent Calls

**Problem:** https://leetcode.com/problems/number-of-recent-calls/

**Difficulty:** Easy | **Premium:** No

**Tags:** Design, Queue, Data Stream

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue

**Data structures (inferred):** Queue

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You have a RecentCounter class which counts the number of recent requests within a certain time frame. 
 
 Implement the RecentCounter class: 

 RecentCounter() Initializes the counter with zero recent requests. 
 
 int ping(int t) Adds a new request at time t , where t represents some time in milliseconds, and returns the number of requests that have happened in the inclusive range [t - 3000, t] , that is, the new request plus every earlier request that is no more than 3000 milliseconds older. 

 It is guaranteed that every call to ping uses a strictly larger value of t than the previous call. 

 Example 1: 
 
```
Input

["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]

Output

[null, 1, 2, 3, 3]

Explanation

RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1); // requests = [
1
], range is [-2999,1], return 1
recentCounter.ping(100); // requests = [
1
, 
100
], range is [-2900,100], return 2
recentCounter.ping(3001); // requests = [
1
, 
100
, 
3001
], range is [1,3001], return 3
recentCounter.ping(3002); // requests = [1, 
100
, 
3001
, 
3002
], range is [2,3002], return 3
```

 Constraints: 

 1 <= t <= 10 9 
 
 Each test case will call ping with strictly increasing values of t . 
 
 At most 10 4 calls will be made to ping .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <queue>

using namespace std;

class RecentCounter {
    queue<int> q;

public:
    RecentCounter() {}

    int ping(int t) {
        q.push(t);
        while (!q.empty() && q.front() < t - 3000)
            q.pop();
        return q.size();
    }
};
```


## 946. Validate Stack Sequences

**Problem:** https://leetcode.com/problems/validate-stack-sequences/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Stack, Simulation

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Stack, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise. 

 Example 1: 
 
```
Input:
 pushed = [1,2,3,4,5], popped = [4,5,3,2,1]

Output:
 true

Explanation:
 We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

 Example 2: 
 
```
Input:
 pushed = [1,2,3,4,5], popped = [4,3,5,1,2]

Output:
 false

Explanation:
 1 cannot be popped before 2.
```

 Constraints: 

 1 <= pushed.length <= 1000 
 
 0 <= pushed[i] <= 1000 
 
 All the elements of pushed are unique . 
 
 popped.length == pushed.length 
 
 popped is a permutation of pushed .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) 
    {
        stack<int> st;
        int i = 0;
        for (int x : pushed) 
        {
            st.push(x);
            while (!st.empty() && st.top() == popped[i]) 
            {
                st.pop();
                i++;
            }
        }
        return i == popped.size();
    }
};
```


## 1381. Design a Stack With Increment Operation

**Problem:** https://leetcode.com/problems/design-a-stack-with-increment-operation/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Stack, Design

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Stack, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Design a stack that supports increment operations on its elements. 
 
 Implement the CustomStack class: 

 CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack. 
 
 void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize . 
 
 int pop() Pops and returns the top of the stack or -1 if the stack is empty. 
 
 void inc(int k, int val) Increments the bottom k elements of the stack by val . If there are less than k elements in the stack, increment all the elements in the stack. 

 Example 1: 
 
```
Input

["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]

Output

[null,null,null,2,null,null,null,null,null,103,202,201,-1]

Explanation

CustomStack stk = new CustomStack(3); // Stack is Empty []
stk.push(1); // stack becomes [1]
stk.push(2); // stack becomes [1, 2]
stk.pop(); // return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2); // stack becomes [1, 2]
stk.push(3); // stack becomes [1, 2, 3]
stk.push(4); // stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100); // stack becomes [101, 102, 103]
stk.increment(2, 100); // stack becomes [201, 202, 103]
stk.pop(); // return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop(); // return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop(); // return 201 --> Return top of the stack 201, stack becomes []
stk.pop(); // return -1 --> Stack is empty return -1.
```

 Constraints: 

 1 <= maxSize, x, k <= 1000 
 
 0 <= val <= 100 
 
 At most 1000 calls will be made to each method of increment , push and pop each separately.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class CustomStack {
    vector<int> stack, inc;
    int maxSize;

public:
    CustomStack(int maxSize) : maxSize(maxSize) {}

    void push(int x) {
        if (stack.size() < maxSize) {
            stack.push_back(x);
            inc.push_back(0);
        }
    }

    int pop() {
        if (stack.empty()) return -1;
        int i = stack.size() - 1;
        if (i > 0) inc[i - 1] += inc[i];
        int res = stack.back() + inc[i];
        stack.pop_back();
        inc.pop_back();
        return res;
    }

    void increment(int k, int val) {
        int i = min(k, (int)stack.size()) - 1;
        if (i >= 0) inc[i] += val;
    }
};
```


## 1441. Build an Array With Stack Operations

**Problem:** https://leetcode.com/problems/build-an-array-with-stack-operations/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Stack, Simulation

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Stack, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array target and an integer n . 
 
 You have an empty stack with the two following operations: 

 "Push" : pushes an integer to the top of the stack. 
 
 "Pop" : removes the integer on the top of the stack. 

 You also have a stream of the integers in the range [1, n] . 
 
 Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target . You should follow the following rules: 

 If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack. 
 
 If the stack is not empty, pop the integer at the top of the stack. 
 
 If, at any moment, the elements in the stack (from the bottom to the top) are equal to target , do not read new integers from the stream and do not do more operations on the stack. 

 Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them . 

 Example 1: 
 
```
Input:
 target = [1,3], n = 3

Output:
 ["Push","Push","Pop","Push"]

Explanation:
 Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Pop the integer on the top of the stack. s = [1].
Read 3 from the stream and push it to the stack. s = [1,3].
```

 Example 2: 
 
```
Input:
 target = [1,2,3], n = 3

Output:
 ["Push","Push","Push"]

Explanation:
 Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Read 3 from the stream and push it to the stack. s = [1,2,3].
```

 Example 3: 
 
```
Input:
 target = [1,2], n = 4

Output:
 ["Push","Push"]

Explanation:
 Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
The answers that read integer 3 from the stream are not accepted.
```

 Constraints: 

 1 <= target.length <= 100 
 
 1 <= n <= 100 
 
 1 <= target[i] <= n 
 
 target is strictly increasing.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> res;
        int i = 1, j = 0;
        while (j < target.size()) {
            res.push_back("Push");
            if (target[j] != i++) res.push_back("Pop");
            else ++j;
        }
        return res;
    }
};
```


## 1476. Subrectangle Queries

**Problem:** https://leetcode.com/problems/subrectangle-queries/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Design, Matrix

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Implement the class SubrectangleQueries  which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods: 
 
 1.  updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) 

 Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2) . 

 2.  getValue(int row, int col) 

 Returns the current value of the coordinate (row,col) from the rectangle. 

 Example 1: 
 
```
Input

["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]

Output

[null,1,null,5,5,null,10,5]

Explanation

SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]); 
// The initial rectangle (4x3) looks like:
// 1 2 1
// 4 3 4
// 3 2 1
// 1 1 1
subrectangleQueries.getValue(0, 2); // return 1
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
// After this update the rectangle looks like:
// 5 5 5
// 5 5 5
// 5 5 5
// 5 5 5 
subrectangleQueries.getValue(0, 2); // return 5
subrectangleQueries.getValue(3, 1); // return 5
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
// After this update the rectangle looks like:
// 5 5 5
// 5 5 5
// 5 5 5
// 10 10 10 
subrectangleQueries.getValue(3, 1); // return 10
subrectangleQueries.getValue(0, 2); // return 5
```

 Example 2: 
 
```
Input

["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]

Output

[null,1,null,100,100,null,20]

Explanation

SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
subrectangleQueries.getValue(0, 0); // return 1
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
subrectangleQueries.getValue(0, 0); // return 100
subrectangleQueries.getValue(2, 2); // return 100
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
subrectangleQueries.getValue(2, 2); // return 20
```

 Constraints: 

 There will be at most 500  operations considering both methods:  updateSubrectangle and getValue . 
 
 1 <= rows, cols <= 100 
 
 rows == rectangle.length 
 
 cols == rectangle[i].length 
 
 0 <= row1 <= row2 < rows 
 
 0 <= col1 <= col2 < cols 
 
 1 <= newValue, rectangle[i][j] <= 10^9 
 
 0 <= row < rows 
 
 0 <= col < cols

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class SubrectangleQueries {
    vector<vector<int>> grid;
public:
    SubrectangleQueries(vector<vector<int>>& rectangle) : grid(rectangle) {}
    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for (int r = row1; r <= row2; ++r)
            for (int c = col1; c <= col2; ++c)
                grid[r][c] = newValue;
    }
    int getValue(int row, int col) { return grid[row][col]; }
};
```


## 1700. Number of Students Unable to Eat Lunch

**Problem:** https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Stack, Queue, Simulation

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Queue, Stack, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches. 
 
 The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack . At each step: 

 If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue. 
 
 Otherwise, they will leave it and go to the queue's end. 

 This continues until none of the queue students want to take the top sandwich and are thus unable to eat. 
 
 You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i ​​​​​​th sandwich in the stack ( i = 0 is the top of the stack) and students[j] is the preference of the j ​​​​​​th student in the initial queue ( j = 0 is the front of the queue). Return the number of students that are unable to eat. 

 Example 1: 
 
```
Input:
 students = [1,1,0,0], sandwiches = [0,1,0,1]

Output:
 0
 
Explanation:

- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
```

 Example 2: 
 
```
Input:
 students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]

Output:
 3
```

 Constraints: 

 1 <= students.length, sandwiches.length <= 100 
 
 students.length == sandwiches.length 
 
 sandwiches[i] is 0 or 1 . 
 
 students[i] is 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        queue<int> q;
        for (int s : students) q.push(s);

        int i = 0, tries = 0;
        while (!q.empty() && tries < q.size()) {
            if (q.front() == sandwiches[i]) {
                q.pop();
                i++;
                tries = 0;
            } else {
                q.push(q.front());
                q.pop();
                tries++;
            }
        }
        return q.size();
    }
};
```


## 2069. Walking Robot Simulation II

**Problem:** https://leetcode.com/problems/walking-robot-simulation-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Design, Simulation

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1) . The grid is aligned with the four cardinal directions ( "North" , "East" , "South" , and "West" ). A robot is initially at cell (0, 0) facing direction "East" . 
 
 The robot can be instructed to move for a specific number of steps . For each step, it does the following. 

 Attempts to move forward one cell in the direction it is facing. 
 
 If the cell the robot is moving to is out of bounds , the robot instead turns 90 degrees counterclockwise and retries the step. 

 After the robot finishes moving the number of steps required, it stops and awaits the next instruction. 
 
 Implement the Robot class: 

 Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East" . 
 
 void step(int num) Instructs the robot to move forward num steps. 
 
 int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y] . 
 
 String getDir() Returns the current direction of the robot, "North" , "East" , "South" , or "West" . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/09/example-1.png] 
 
```
Input

["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]

Output

[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

Explanation

Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2); // It moves two steps East to (2, 0), and faces East.
robot.step(2); // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2); // It moves one step East to (5, 0), and faces East.
 // Moving the next step East would be out of bounds, so it turns and faces North.
 // Then, it moves one step North to (5, 1), and faces North.
robot.step(1); // It moves one step North to (5, 2), and faces 
North
 (not West).
robot.step(4); // Moving the next step North would be out of bounds, so it turns and faces West.
 // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return "West"
```

 Constraints: 

 2 <= width, height <= 100 
 
 1 <= num <= 10 5 
 
 At most 10 4 calls in total will be made to step , getPos , and getDir .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Robot {
 int w,h,per,pos=0; bool moved=false;
public:
 Robot(int width,int height):w(width),h(height),per(2*(width+height-2)){}
 void step(int num){moved=true; pos=(pos+num%per)%per;}
 vector<int> getPos(){
  int t=pos;
  if(t<w-1) return {t,0}; t-=w-1;
  if(t<h-1) return {w-1,t}; t-=h-1;
  if(t<w-1) return {w-1-t,h-1}; t-=w-1;
  return {0,h-1-t};
 }
 string getDir(){
  if(!moved) return "East";
  if(pos==0) return "South";
  if(pos<=w-1) return "East";
  if(pos<=w+h-2) return "North";
  if(pos<=2*w+h-3) return "West";
  return "South";
 }
};
```


## 2073. Time Needed to Buy Tickets

**Problem:** https://leetcode.com/problems/time-needed-to-buy-tickets/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Queue, Simulation

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Queue, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There are n people in a line queuing to buy tickets, where the 0 th person is at the front of the line and the (n - 1) th person is at the back of the line. 
 
 You are given a 0-indexed integer array tickets of length n where the number of tickets that the i th person would like to buy is tickets[i] . 
 
 Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously ) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line. 
 
 Return the time taken for the person initially at position k (0-indexed) to finish buying tickets. 

 Example 1: 

 Input: tickets = [2,3,2], k = 2 
 
 Output: 6 
 
 Explanation: 

 The queue starts as [2,3, 2 ], where the kth person is underlined. 
 
 After the person at the front has bought a ticket, the queue becomes [3, 2 ,1] at 1 second. 
 
 Continuing this process, the queue becomes [ 2 ,1,2] at 2 seconds. 
 
 Continuing this process, the queue becomes [1,2, 1 ] at 3 seconds. 
 
 Continuing this process, the queue becomes [2, 1 ] at 4 seconds. Note: the person at the front left the queue. 
 
 Continuing this process, the queue becomes [ 1 ,1] at 5 seconds. 
 
 Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6. 

 Example 2: 

 Input: tickets = [5,1,1,1], k = 0 
 
 Output: 8 
 
 Explanation: 

 The queue starts as [ 5 ,1,1,1], where the kth person is underlined. 
 
 After the person at the front has bought a ticket, the queue becomes [1,1,1, 4 ] at 1 second. 
 
 Continuing this process for 3 seconds, the queue becomes [ 4] at 4 seconds. 
 
 Continuing this process for 4 seconds, the queue becomes [] at 8 seconds. The kth person has bought all their tickets, so return 8. 

 Constraints: 

 n == tickets.length 
 
 1 <= n <= 100 
 
 1 <= tickets[i] <= 100 
 
 0 <= k < n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int res = 0;
        for (int i = 0; i < tickets.size(); ++i) {
            if (i <= k)
                res += min(tickets[i], tickets[k]);
            else
                res += min(tickets[i], tickets[k] - 1);
        }
        return res;
    }
};
```


## 2534. Time Taken to Cross the Door

**Problem:** https://leetcode.com/problems/time-taken-to-cross-the-door/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Queue, Simulation

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Queue, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There are n persons numbered from 0 to n - 1 and a door. Each person can enter or exit through the door once, taking one second. 
 
 You are given a non-decreasing integer array arrival of size n , where arrival[i] is the arrival time of the i th person at the door. You are also given an array state of size n , where state[i] is 0 if person i wants to enter through the door or 1 if they want to exit through the door. 
 
 If two or more persons want to use the door at the same time, they follow the following rules: 

 If the door was not used in the previous second, then the person who wants to exit goes first. 
 
 If the door was used in the previous second for entering , the person who wants to enter goes first. 
 
 If the door was used in the previous second for exiting , the person who wants to exit goes first. 
 
 If multiple persons want to go in the same direction, the person with the smallest index goes first. 

 Return an array answer of size n where answer[i] is the second at which the i th person crosses the door . 
 
 Note that: 

 Only one person can cross the door at each second. 
 
 A person may arrive at the door and wait without entering or exiting to follow the mentioned rules. 

 Example 1: 
 
```
Input:
 arrival = [0,1,1,2,4], state = [0,1,0,0,1]

Output:
 [0,3,1,2,4]

Explanation:
 At each second we have the following:
- At t = 0: Person 0 is the only one who wants to enter, so they just enter through the door.
- At t = 1: Person 1 wants to exit, and person 2 wants to enter. Since the door was used the previous second for entering, person 2 enters.
- At t = 2: Person 1 still wants to exit, and person 3 wants to enter. Since the door was used the previous second for entering, person 3 enters.
- At t = 3: Person 1 is the only one who wants to exit, so they just exit through the door.
- At t = 4: Person 4 is the only one who wants to exit, so they just exit through the door.
```

 Example 2: 
 
```
Input:
 arrival = [0,0,0], state = [1,0,1]

Output:
 [0,2,1]

Explanation:
 At each second we have the following:
- At t = 0: Person 1 wants to enter while persons 0 and 2 want to exit. Since the door was not used in the previous second, the persons who want to exit get to go first. Since person 0 has a smaller index, they exit first.
- At t = 1: Person 1 wants to enter, and person 2 wants to exit. Since the door was used in the previous second for exiting, person 2 exits.
- At t = 2: Person 1 is the only one who wants to enter, so they just enter through the door.
```

 Constraints: 

 n == arrival.length == state.length 
 
 1 <= n <= 10 5 
 
 0 <= arrival[i] <= n 
 
 arrival is sorted in non-decreasing order. 
 
 state[i] is either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> timeTaken(vector<int>& arrival, vector<int>& state) {
        int n = arrival.size();
        queue<int> q[2];
        vector<int> result(n);
        int i = 0, done = 0, t = 0, previous = 1;
        while (done < n) {
            if (q[0].empty() && q[1].empty() && i < n && t < arrival[i]) {
                t = arrival[i];
                previous = 1;
            }
            while (i < n && arrival[i] <= t) {
                q[state[i]].push(i++);
            }
            int direction = !q[previous].empty() ? previous : 1 - previous;
            if (q[direction].empty()) continue;
            int person = q[direction].front();
            q[direction].pop();
            result[person] = t++;
            previous = direction;
            ++done;
        }
        return result;
    }
};
```


## 3834. Merge Adjacent Equal Elements

**Problem:** https://leetcode.com/problems/merge-adjacent-equal-elements/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Stack, Simulation

**Primary pattern:** Stack / Queue

**Related patterns:** Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Stack, Vector

**Pattern recognition:** LIFO/FIFO processing, parser state, or online operations.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . 
 
 You must repeatedly apply the following merge operation until no more changes can be made: 

 If any two adjacent elements are equal , choose the leftmost such adjacent pair in the current array and replace them with a single element equal to their sum . 

 After each merge operation, the array size decreases by 1. Repeat the process on the updated array until no more changes can be made. 
 
 Return the final array after all possible merge operations. 

 Example 1: 

 Input: nums = [3,1,1,2] 
 
 Output: [3,4] 
 
 Explanation: 

 The middle two elements are equal and merged into 1 + 1 = 2 , resulting in [3, 2, 2] . 
 
 The last two elements are equal and merged into 2 + 2 = 4 , resulting in [3, 4] . 
 
 No adjacent equal elements remain. Thus, the answer is [3, 4] . 

 Example 2: 

 Input: nums = [2,2,4] 
 
 Output: [8] 
 
 Explanation: 

 The first two elements are equal and merged into 2 + 2 = 4 , resulting in [4, 4] . 
 
 The first two elements are equal and merged into 4 + 4 = 8 , resulting in [8] . 

 Example 3: 

 Input: nums = [3,7,5] 
 
 Output: [3,7,5] 
 
 Explanation: 
 
 There are no adjacent equal elements in the array, so no operations are performed. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 5 ​​​​​​​

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<long long> mergeAdjacent(vector<int>& nums) {
        vector<long long> st;
        for(int x:nums){
            st.push_back(x);
            while(st.size()>1 && st.back()==st[st.size()-2]){
                long long v=st.back();st.pop_back();st.back()+=v;
            }
        }
        return st;
    }
};
```

