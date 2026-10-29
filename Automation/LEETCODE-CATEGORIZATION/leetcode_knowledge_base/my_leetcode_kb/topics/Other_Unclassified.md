# Other / Unclassified

**Problems:** 44

## Quick revision checklist



## Problem index

- [1114. Print in Order](#1114-print-in-order) — Easy; code: yes
- [1115. Print FooBar Alternately](#1115-print-foobar-alternately) — Medium; code: yes
- [1116. Print Zero Even Odd](#1116-print-zero-even-odd) — Medium; code: yes
- [1117. Building H2O](#1117-building-h2o) — Medium; code: yes
- [1188. Design Bounded Blocking Queue](#1188-design-bounded-blocking-queue) — Medium; code: yes
- [1195. Fizz Buzz Multithreaded](#1195-fizz-buzz-multithreaded) — Medium; code: yes
- [1226. The Dining Philosophers](#1226-the-dining-philosophers) — Medium; code: yes
- [1279. Traffic Light Controlled Intersection](#1279-traffic-light-controlled-intersection) — Easy; code: yes
- [1291. Sequential Digits](#1291-sequential-digits) — Medium; code: yes
- [2753. Count Houses in a Circular Street II](#2753-count-houses-in-a-circular-street-ii) — Hard; code: yes
- [3253. Construct String with Minimum Cost (Easy)](#3253-construct-string-with-minimum-cost-easy) — Medium; code: yes
- [3778. Minimum Distance Excluding One Maximum Weighted Edge](#3778-minimum-distance-excluding-one-maximum-weighted-edge) — Medium; code: yes
- [3802. Number of Ways to Paint Sheets](#3802-number-of-ways-to-paint-sheets) — Hard; code: yes
- [3893. Maximum Team Size with Overlapping Intervals](#3893-maximum-team-size-with-overlapping-intervals) — Medium; code: yes
- [3907. Count Smaller Elements With Opposite Parity](#3907-count-smaller-elements-with-opposite-parity) — Medium; code: yes
- [3963. Create Grid With Exactly One Path](#3963-create-grid-with-exactly-one-path) — Easy; code: yes
- [4029. Elevator Requests IV](#4029-elevator-requests-iv) — Hard; code: yes
- [4070. Minimum Rotations to Dial a Number I](#4070-minimum-rotations-to-dial-a-number-i) — Easy; code: yes
- [4071. Minimum Rotations to Dial a Number II](#4071-minimum-rotations-to-dial-a-number-ii) — Medium; code: yes
- [4072. Maximum Alternating Subarray Sum With One Deletion](#4072-maximum-alternating-subarray-sum-with-one-deletion) — Medium; code: yes
- [4073. Count Good Strings](#4073-count-good-strings) — Hard; code: yes
- [4074. Maximum Product Pair With Target Sum](#4074-maximum-product-pair-with-target-sum) — Easy; code: yes
- [4075. Longest Resilient Subarray I](#4075-longest-resilient-subarray-i) — Medium; code: yes
- [4076. Longest Resilient Subarray II](#4076-longest-resilient-subarray-ii) — Medium; code: yes
- [4077. Minimize Inversions in a Prefix Tree](#4077-minimize-inversions-in-a-prefix-tree) — Hard; code: yes
- [4078. Three Fibonacci Sum](#4078-three-fibonacci-sum) — Easy; code: yes
- [4079. Prime Subset Selection I](#4079-prime-subset-selection-i) — Medium; code: yes
- [4080. Design Bus Seat Booking System](#4080-design-bus-seat-booking-system) — Medium; code: yes
- [4081. Prime Subset Selection II](#4081-prime-subset-selection-ii) — Hard; code: yes
- [4082. Minimum Operations to Stabilize a Binary Tree](#4082-minimum-operations-to-stabilize-a-binary-tree) — Hard; code: yes
- [4083. Minimum Deletions to Make Array Sharp](#4083-minimum-deletions-to-make-array-sharp) — Easy; code: yes
- [4084. Last Visited Cell in a Directional Grid](#4084-last-visited-cell-in-a-directional-grid) — Medium; code: yes
- [4085. Find Root of a Colored Tree](#4085-find-root-of-a-colored-tree) — Medium; code: yes
- [4086. Minimum Interval Selection to Cover Target Intervals](#4086-minimum-interval-selection-to-cover-target-intervals) — Hard; code: yes
- [4087. Maximum Subarray Sum of Fixed Length After at Most K Swaps](#4087-maximum-subarray-sum-of-fixed-length-after-at-most-k-swaps) — Medium; code: yes
- [4088. Difference Between Peaks and Valleys](#4088-difference-between-peaks-and-valleys) — Easy; code: yes
- [4089. Count Subarrays With Loose Bounds](#4089-count-subarrays-with-loose-bounds) — Medium; code: yes
- [4090. Count Magical Substring Pairs I](#4090-count-magical-substring-pairs-i) — Medium; code: yes
- [4091. Count Magical Substring Pairs II](#4091-count-magical-substring-pairs-ii) — Hard; code: yes
- [4092. Binary Digit Score](#4092-binary-digit-score) — Easy; code: yes
- [4093. Maximize Sum After At Most K Digit Rearrangements](#4093-maximize-sum-after-at-most-k-digit-rearrangements) — Medium; code: yes
- [4094. Count Frequency Staircase Subarrays I](#4094-count-frequency-staircase-subarrays-i) — Medium; code: yes
- [4095. Count Frequency Staircase Subarrays II](#4095-count-frequency-staircase-subarrays-ii) — Hard; code: yes
- [4096. Simulate Bomb Explosions and Falling Boxes](#4096-simulate-bomb-explosions-and-falling-boxes) — Medium; code: yes

---

## 1114. Print in Order

**Problem:** https://leetcode.com/problems/print-in-order/

**Difficulty:** Easy | **Premium:** No

**Tags:** Concurrency

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Suppose we have a class: 
 
```
public class Foo {
 public void first() { print("first"); }
 public void second() { print("second"); }
 public void third() { print("third"); }
}
```

 The same instance of Foo will be passed to three different threads. Thread A will call first() , thread B will call second() , and thread C will call third() . Design a mechanism and modify the program to ensure that second() is executed after first() , and third() is executed after second() . 
 
 Note: 
 
 We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness. 

 Example 1: 
 
```
Input:
 nums = [1,2,3]

Output:
 "firstsecondthird"

Explanation:
 There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
```

 Example 2: 
 
```
Input:
 nums = [1,3,2]

Output:
 "firstsecondthird"

Explanation:
 The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
```

 Constraints: 

 nums is a permutation of [1, 2, 3] .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Foo {
    mutex mu;
    condition_variable cv;
    int stage = 0;
public:
    Foo() = default;
    void first(function<void()> printFirst) {
        unique_lock<mutex> lock(mu);
        printFirst();
        stage = 1;
        cv.notify_all();
    }
    void second(function<void()> printSecond) {
        unique_lock<mutex> lock(mu);
        cv.wait(lock, [&] { return stage >= 1; });
        printSecond();
        stage = 2;
        cv.notify_all();
    }
    void third(function<void()> printThird) {
        unique_lock<mutex> lock(mu);
        cv.wait(lock, [&] { return stage >= 2; });
        printThird();
    }
};
```


## 1115. Print FooBar Alternately

**Problem:** https://leetcode.com/problems/print-foobar-alternately/

**Difficulty:** Medium | **Premium:** No

**Tags:** Concurrency

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Suppose you are given the following code: 
 
```
class FooBar {
 public void foo() {
 for (int i = 0; i < n; i++) {
 print("foo");
 }
 }

 public void bar() {
 for (int i = 0; i < n; i++) {
 print("bar");
 }
 }
}
```

 The same instance of FooBar will be passed to two different threads: 

 thread A will call foo() , while 
 
 thread B will call bar() . 

 Modify the given program to output "foobar" n times. 

 Example 1: 
 
```
Input:
 n = 1

Output:
 "foobar"

Explanation:
 There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.
```

 Example 2: 
 
```
Input:
 n = 2

Output:
 "foobarfoobar"

Explanation:
 "foobar" is being output 2 times.
```

 Constraints: 

 1 <= n <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class FooBar {
    int n;
    mutex mu;
    condition_variable cv;
    bool fooTurn = true;
public:
    FooBar(int n) : n(n) {}
    void foo(function<void()> printFoo) {
        for (int i = 0; i < n; ++i) {
            unique_lock<mutex> lock(mu);
            cv.wait(lock, [&] { return fooTurn; });
            printFoo();
            fooTurn = false;
            cv.notify_all();
        }
    }
    void bar(function<void()> printBar) {
        for (int i = 0; i < n; ++i) {
            unique_lock<mutex> lock(mu);
            cv.wait(lock, [&] { return !fooTurn; });
            printBar();
            fooTurn = true;
            cv.notify_all();
        }
    }
};
```


## 1116. Print Zero Even Odd

**Problem:** https://leetcode.com/problems/print-zero-even-odd/

**Difficulty:** Medium | **Premium:** No

**Tags:** Concurrency

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You have a function printNumber that can be called with an integer parameter and prints it to the console. 

 For example, calling printNumber(7) prints 7 to the console. 

 You are given an instance of the class ZeroEvenOdd that has three functions: zero , even , and odd . The same instance of ZeroEvenOdd will be passed to three different threads: 

 Thread A: calls zero() that should only output 0 's. 
 
 Thread B: calls even() that should only output even numbers. 
 
 Thread C: calls odd() that should only output odd numbers. 

 Modify the given class to output the series "010203040506..." where the length of the series must be 2n . 
 
 Implement the ZeroEvenOdd class: 

 ZeroEvenOdd(int n) Initializes the object with the number n that represents the numbers that should be printed. 
 
 void zero(printNumber) Calls printNumber to output one zero. 
 
 void even(printNumber) Calls printNumber to output one even number. 
 
 void odd(printNumber) Calls printNumber to output one odd number. 

 Example 1: 
 
```
Input:
 n = 2

Output:
 "0102"

Explanation:
 There are three threads being fired asynchronously.
One of them calls zero(), the other calls even(), and the last one calls odd().
"0102" is the correct output.
```

 Example 2: 
 
```
Input:
 n = 5

Output:
 "0102030405"
```

 Constraints: 

 1 <= n <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class ZeroEvenOdd {
    int n, next = 1, turn = 0; // 0 zero, 1 odd, 2 even
    mutex mu;
    condition_variable cv;
public:
    ZeroEvenOdd(int n) : n(n) {}
    void zero(function<void(int)> printNumber) {
        for (int i = 1; i <= n; ++i) {
            unique_lock<mutex> lock(mu);
            cv.wait(lock, [&] { return turn == 0; });
            printNumber(0);
            turn = (i % 2 ? 1 : 2);
            cv.notify_all();
        }
    }
    void odd(function<void(int)> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            unique_lock<mutex> lock(mu);
            cv.wait(lock, [&] { return turn == 1; });
            printNumber(i);
            turn = 0;
            cv.notify_all();
        }
    }
    void even(function<void(int)> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            unique_lock<mutex> lock(mu);
            cv.wait(lock, [&] { return turn == 2; });
            printNumber(i);
            turn = 0;
            cv.notify_all();
        }
    }
};
```


## 1117. Building H2O

**Problem:** https://leetcode.com/problems/building-h2o/

**Difficulty:** Medium | **Premium:** No

**Tags:** Concurrency

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There are two kinds of threads: oxygen and hydrogen . Your goal is to group these threads to form water molecules. 
 
 There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given releaseHydrogen and releaseOxygen methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do. 
 
 In other words: 

 If an oxygen thread arrives at the barrier when no hydrogen threads are present, it must wait for two hydrogen threads. 
 
 If a hydrogen thread arrives at the barrier when no other threads are present, it must wait for an oxygen thread and another hydrogen thread. 

 We do not have to worry about matching the threads up explicitly; the threads do not necessarily know which other threads they are paired up with. The key is that threads pass the barriers in complete sets; thus, if we examine the sequence of threads that bind and divide them into groups of three, each group should contain one oxygen and two hydrogen threads. 
 
 Write synchronization code for oxygen and hydrogen molecules that enforces these constraints. 

 Example 1: 
 
```
Input:
 water = "HOH"

Output:
 "HHO"

Explanation:
 "HOH" and "OHH" are also valid answers.
```

 Example 2: 
 
```
Input:
 water = "OOHHHH"

Output:
 "HHOHHO"

Explanation:
 "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
```

 Constraints: 

 3 * n == water.length 
 
 1 <= n <= 20 
 
 water[i] is either 'H' or 'O' . 
 
 There will be exactly 2 * n 'H' in water . 
 
 There will be exactly n 'O' in water .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class H2O {
    mutex mu;
    condition_variable cv;
    int h = 0, o = 0, finished = 0;
    void complete() {
        if (++finished == 3) {
            h = o = finished = 0;
            cv.notify_all();
        }
    }
public:
    void hydrogen(function<void()> releaseHydrogen) {
        unique_lock<mutex> lock(mu);
        cv.wait(lock, [&] { return h < 2 && finished < 3; });
        ++h;
        releaseHydrogen();
        complete();
        cv.notify_all();
    }
    void oxygen(function<void()> releaseOxygen) {
        unique_lock<mutex> lock(mu);
        cv.wait(lock, [&] { return o < 1 && finished < 3; });
        ++o;
        releaseOxygen();
        complete();
        cv.notify_all();
    }
};
```


## 1188. Design Bounded Blocking Queue

**Problem:** https://leetcode.com/problems/design-bounded-blocking-queue/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Concurrency

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Queue

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Implement a thread-safe bounded blocking queue that has the following methods: 

 BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity . 
 
 void enqueue(int element) Adds an element to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full. 
 
 int dequeue() Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty. 
 
 int size() Returns the number of elements currently in the queue. 

 Your implementation will be tested using multiple threads at the same time. Each thread will either be a producer thread that only makes calls to the enqueue method or a consumer thread that only makes calls to the dequeue method. The size method will be called after every test case. 
 
 Please do not use built-in implementations of bounded blocking queue as this will not be accepted in an interview. 

 Example 1: 
 
```
Input:

1
1
["BoundedBlockingQueue","enqueue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","dequeue"]
[[2],[1],[],[],[0],[2],[3],[4],[]]

Output:

[1,0,2,2]

Explanation:

Number of producer threads = 1
Number of consumer threads = 1

BoundedBlockingQueue queue = new BoundedBlockingQueue(2); // initialize the queue with capacity = 2.

queue.enqueue(1); // The producer thread enqueues 1 to the queue.
queue.dequeue(); // The consumer thread calls dequeue and returns 1 from the queue.
queue.dequeue(); // Since the queue is empty, the consumer thread is blocked.
queue.enqueue(0); // The producer thread enqueues 0 to the queue. The consumer thread is unblocked and returns 0 from the queue.
queue.enqueue(2); // The producer thread enqueues 2 to the queue.
queue.enqueue(3); // The producer thread enqueues 3 to the queue.
queue.enqueue(4); // The producer thread is blocked because the queue's capacity (2) is reached.
queue.dequeue(); // The consumer thread returns 2 from the queue. The producer thread is unblocked and enqueues 4 to the queue.
queue.size(); // 2 elements remaining in the queue. size() is always called at the end of each test case.
```

 Example 2: 
 
```
Input:

3
4
["BoundedBlockingQueue","enqueue","enqueue","enqueue","dequeue","dequeue","dequeue","enqueue"]
[[3],[1],[0],[2],[],[],[],[3]]

Output:

[1,0,2,1]

Explanation:

Number of producer threads = 3
Number of consumer threads = 4

BoundedBlockingQueue queue = new BoundedBlockingQueue(3); // initialize the queue with capacity = 3.

queue.enqueue(1); // Producer thread P1 enqueues 1 to the queue.
queue.enqueue(0); // Producer thread P2 enqueues 0 to the queue.
queue.enqueue(2); // Producer thread P3 enqueues 2 to the queue.
queue.dequeue(); // Consumer thread C1 calls dequeue.
queue.dequeue(); // Consumer thread C2 calls dequeue.
queue.dequeue(); // Consumer thread C3 calls dequeue.
queue.enqueue(3); // One of the producer threads enqueues 3 to the queue.
queue.size(); // 1 element remaining in the queue.

Since the number of threads for producer/consumer is greater than 1, we do not know how the threads will be scheduled in the operating system, even though the input seems to imply the ordering. Therefore, any of the output [1,0,2] or [1,2,0] or [0,1,2] or [0,2,1] or [2,0,1] or [2,1,0] will be accepted.
```

 Constraints: 

 1 <= Number of Prdoucers <= 8 
 
 1 <= Number of Consumers <= 8 
 
 1 <= size <= 30 
 
 0 <= element <= 20 
 
 The number of calls to enqueue is greater than or equal to the number of calls to dequeue . 
 
 At most 40 calls will be made to enque , deque , and size .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class BoundedBlockingQueue {
    queue<int> q;
    int capacity;
    mutex m;
    condition_variable notFull;
    condition_variable notEmpty;

public:
    BoundedBlockingQueue(int capacity) : capacity(capacity) {}

    void enqueue(int element) {
        unique_lock<mutex> lock(m);
        notFull.wait(lock, [&]() {
            return static_cast<int>(q.size()) < capacity;
        });
        q.push(element);
        lock.unlock();
        notEmpty.notify_one();
    }

    int dequeue() {
        unique_lock<mutex> lock(m);
        notEmpty.wait(lock, [&]() {
            return !q.empty();
        });
        int value = q.front();
        q.pop();
        lock.unlock();
        notFull.notify_one();
        return value;
    }

    int size() {
        lock_guard<mutex> lock(m);
        return static_cast<int>(q.size());
    }
};
```


## 1195. Fizz Buzz Multithreaded

**Problem:** https://leetcode.com/problems/fizz-buzz-multithreaded/

**Difficulty:** Medium | **Premium:** No

**Tags:** Concurrency

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You have the four functions: 

 printFizz that prints the word "fizz" to the console, 
 
 printBuzz that prints the word "buzz" to the console, 
 
 printFizzBuzz that prints the word "fizzbuzz" to the console, and 
 
 printNumber that prints a given integer to the console. 

 You are given an instance of the class FizzBuzz that has four functions: fizz , buzz , fizzbuzz and number . The same instance of FizzBuzz will be passed to four different threads: 

 Thread A: calls fizz() that should output the word "fizz" . 
 
 Thread B: calls buzz() that should output the word "buzz" . 
 
 Thread C: calls fizzbuzz() that should output the word "fizzbuzz" . 
 
 Thread D: calls number() that should only output the integers. 

 Modify the given class to output the series [1, 2, "fizz", 4, "buzz", ...] where the i th token ( 1-indexed ) of the series is: 

 "fizzbuzz" if i is divisible by 3 and 5 , 
 
 "fizz" if i is divisible by 3 and not 5 , 
 
 "buzz" if i is divisible by 5 and not 3 , or 
 
 i if i is not divisible by 3 or 5 . 

 Implement the FizzBuzz class: 

 FizzBuzz(int n) Initializes the object with the number n that represents the length of the sequence that should be printed. 
 
 void fizz(printFizz) Calls printFizz to output "fizz" . 
 
 void buzz(printBuzz) Calls printBuzz to output "buzz" . 
 
 void fizzbuzz(printFizzBuzz) Calls printFizzBuzz to output "fizzbuzz" . 
 
 void number(printNumber) Calls printnumber to output the numbers. 

 Example 1: 
 
```
Input:
 n = 15

Output:
 [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"]
```
 
 Example 2: 
 
```
Input:
 n = 5

Output:
 [1,2,"fizz",4,"buzz"]
```

 Constraints: 

 1 <= n <= 50

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class FizzBuzz {
    int n, cur = 1;
    mutex mu;
    condition_variable cv;
    void run(int type, function<void()> word, function<void(int)> number) {
        while (true) {
            unique_lock<mutex> lock(mu);
            cv.wait(lock, [&] {
                if (cur > n) return true;
                int t = (cur % 15 == 0) ? 3 :
                        (cur % 3 == 0) ? 1 : (cur % 5 == 0) ? 2 : 0;
                return t == type;
            });
            if (cur > n) return;
            if (type == 0) number(cur);
            else word();
            ++cur;
            cv.notify_all();
        }
    }
public:
    FizzBuzz(int n) : n(n) {}
    void fizz(function<void()> printFizz) { run(1, printFizz, {}); }
    void buzz(function<void()> printBuzz) { run(2, printBuzz, {}); }
    void fizzbuzz(function<void()> printFizzBuzz) { run(3, printFizzBuzz, {}); }
    void number(function<void(int)> printNumber) { run(0, {}, printNumber); }
};
```


## 1226. The Dining Philosophers

**Problem:** https://leetcode.com/problems/the-dining-philosophers/

**Difficulty:** Medium | **Premium:** No

**Tags:** Concurrency

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Five silent philosophers sit at a round table with bowls of spaghetti. Forks are placed between each pair of adjacent philosophers. 
 
 Each philosopher must alternately think and eat. However, a philosopher can only eat spaghetti when they have both left and right forks. Each fork can be held by only one philosopher and so a philosopher can use the fork only if it is not being used by another philosopher. After an individual philosopher finishes eating, they need to put down both forks so that the forks become available to others. A philosopher can take the fork on their right or the one on their left as they become available, but cannot start eating before getting both forks. 
 
 Eating is not limited by the remaining amounts of spaghetti or stomach space; an infinite supply and an infinite demand are assumed. 
 
 Design a discipline of behaviour (a concurrent algorithm) such that no philosopher will starve;  i.e. , each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think. 
 
 [Figure: https://assets.leetcode.com/uploads/2019/09/24/an_illustration_of_the_dining_philosophers_problem.png] 
 
 The problem statement and the image above are taken from wikipedia.org 

 The philosophers' ids are numbered from 0 to 4 in a clockwise order. Implement the function  void wantsToEat(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork) where: 

 philosopher  is the id of the philosopher who wants to eat. 
 
 pickLeftFork  and  pickRightFork  are functions you can call to pick the corresponding forks of that philosopher. 
 
 eat  is a function you can call to let the philosopher eat once he has picked both forks. 
 
 putLeftFork  and  putRightFork  are functions you can call to put down the corresponding forks of that philosopher. 
 
 The philosophers are assumed to be thinking as long as they are not asking to eat (the function is not being called with their number). 

 Five threads, each representing a philosopher, will simultaneously use one object of your class to simulate the process. The function may be called for the same philosopher more than once, even before the last call ends. 

 Example 1: 
 
```
Input:
 n = 1

Output:
 [[3,2,1],[3,1,1],[3,0,3],[3,1,2],[3,2,2],[4,2,1],[4,1,1],[2,2,1],[2,1,1],[1,2,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[4,2,2],[1,1,1],[1,0,3],[1,1,2],[1,2,2],[0,1,1],[0,2,1],[0,0,3],[0,1,2],[0,2,2]]

Explanation:

n is the number of times each philosopher will call the function.
The output array describes the calls you made to the functions controlling the forks and the eat function, its format is:
output[i] = [a, b, c] (three integers)
- a is the id of a philosopher.
- b specifies the fork: {1 : left, 2 : right}.
- c specifies the operation: {1 : pick, 2 : put, 3 : eat}.
```

 Constraints: 

 1 <= n <= 60

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class DiningPhilosophers {
    mutex forks[5];
public:
    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
        int left = philosopher;
        int right = (philosopher + 1) % 5;
        lock(forks[left], forks[right]);
        lock_guard<mutex> leftLock(forks[left], adopt_lock);
        lock_guard<mutex> rightLock(forks[right], adopt_lock);
        pickLeftFork();
        pickRightFork();
        eat();
        putRightFork();
        putLeftFork();
    }
};
```


## 1279. Traffic Light Controlled Intersection

**Problem:** https://leetcode.com/problems/traffic-light-controlled-intersection/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Concurrency

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There is an intersection of two roads. First road is road A where cars travel from North to South in direction 1 and from South to North in direction 2. Second road is road B where cars travel from West to East in direction 3 and from East to West in direction 4. 
 
 [Figure: https://assets.leetcode.com/uploads/2019/11/11/exp.png] 
 
 There is a traffic light located on each road before the intersection. A traffic light can either be green or red. 

 Green means cars can cross the intersection in both directions of the road. 
 
 Red means cars in both directions cannot cross the intersection and must wait until the light turns green. 

 The traffic lights cannot be green on both roads at the same time. That means when the light is green on road A, it is red on road B and when the light is green on road B, it is red on road A. 
 
 Initially, the traffic light is green on road A and red  on road B. When the light is green on one road, all cars can cross the intersection in both directions until the light becomes green on the other road. No two cars traveling on different roads should cross at the same time. 
 
 Design a deadlock-free traffic light controlled system at this intersection. 
 
 Implement the function  void carArrived(carId, roadId, direction, turnGreen, crossCar) where: 

 carId  is the id of the car that arrived. 
 
 roadId  is the id of the road that the car travels on. 
 
 direction  is the direction of the car. 
 
 turnGreen  is a function you can call to turn the traffic light to green on the current road. 
 
 crossCar  is a function you can call to let the current car cross the intersection. 

 Your answer is considered correct if it avoids cars deadlock in the intersection. Turning the light green on a road when it was already green is considered a wrong answer. 

 Example 1: 
 
```
Input:
 cars = [1,3,5,2,4], directions = [2,1,2,4,3], arrivalTimes = [10,20,30,40,50]

Output:
 [
"Car 1 Has Passed Road A In Direction 2", // Traffic light on road A is green, car 1 can cross the intersection.
"Car 3 Has Passed Road A In Direction 1", // Car 3 crosses the intersection as the light is still green.
"Car 5 Has Passed Road A In Direction 2", // Car 5 crosses the intersection as the light is still green.
"Traffic Light On Road B Is Green", // Car 2 requests green light for road B.
"Car 2 Has Passed Road B In Direction 4", // Car 2 crosses as the light is green on road B now.
"Car 4 Has Passed Road B In Direction 3" // Car 4 crosses the intersection as the light is still green.
]
```

 Example 2: 
 
```
Input:
 cars = [1,2,3,4,5], directions = [2,4,3,3,1], arrivalTimes = [10,20,30,40,40]

Output:
 [
"Car 1 Has Passed Road A In Direction 2", // Traffic light on road A is green, car 1 can cross the intersection.
"Traffic Light On Road B Is Green", // Car 2 requests green light for road B.
"Car 2 Has Passed Road B In Direction 4", // Car 2 crosses as the light is green on road B now.
"Car 3 Has Passed Road B In Direction 3", // Car 3 crosses as the light is green on road B now.
"Traffic Light On Road A Is Green", // Car 5 requests green light for road A.
"Car 5 Has Passed Road A In Direction 1", // Car 5 crosses as the light is green on road A now.
"Traffic Light On Road B Is Green", // Car 4 requests green light for road B. Car 4 blocked until car 5 crosses and then traffic light is green on road B.
"Car 4 Has Passed Road B In Direction 3" // Car 4 crosses as the light is green on road B now.
]

Explanation:
 This is a dead-lock free scenario. Note that the scenario when car 4 crosses before turning light into green on road A and allowing car 5 to pass is also 
correct
 and 
Accepted
 scenario.
```

 Constraints: 

 1 <= cars.length <= 20 
 
 cars.length = directions.length 
 
 cars.length = arrivalTimes.length 
 
 All values of cars are unique 
 
 1 <= directions[i] <= 4 
 
 arrivalTimes is non-decreasing

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class TrafficLight {
    mutex m;
    int green = 1;

public:
    TrafficLight() {}

    void carArrived(int carId, int roadId, int direction,
                    function<void()> turnGreen,
                    function<void()> crossCar) {
        lock_guard<mutex> guard(m);
        if (green != roadId) {
            turnGreen();
            green = roadId;
        }
        crossCar();
    }
};
```


## 1291. Sequential Digits

**Problem:** https://leetcode.com/problems/sequential-digits/

**Difficulty:** Medium | **Premium:** No

**Tags:** Enumeration

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Queue, Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

An integer has sequential digits if and only if each digit in the number is one more than the previous digit. 
 
 Return a sorted list of all the integers in the range [low, high]  inclusive that have sequential digits. 

 Example 1: 
 
```
Input:
 low = 100, high = 300

Output:
 [123,234]
```
 
 Example 2: 
 
```
Input:
 low = 1000, high = 13000

Output:
 [1234,2345,3456,4567,5678,6789,12345]
```

 Constraints: 

 10 <= low <= high <= 10^9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        queue<int> q;
        for (int i = 1; i <= 9; ++i)
            q.push(i);

        vector<int> res;
        while (!q.empty()) {
            int num = q.front(); q.pop();
            if (num >= low && num <= high) res.push_back(num);
            if (num % 10 < 9) {
                int next = num * 10 + (num % 10 + 1);
                if (next <= high) q.push(next);
            }
        }
        return res;
    }
};
```


## 2753. Count Houses in a Circular Street II

**Problem:** https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an object street of class Street that represents a circular street and a positive integer k which represents a maximum bound for the number of houses in that street (in other words, the number of houses is less than or equal to k ). Houses' doors could be open or closed initially (at least one is open). 
 
 Initially, you are standing in front of a door to a house on this street. Your task is to count the number of houses in the street. 
 
 The class Street contains the following functions which may help you: 

 void closeDoor() : Close the door of the house you are in front of. 
 
 boolean isDoorOpen() : Returns true if the door of the current house is open and false otherwise. 
 
 void moveRight() : Move to the right house. 

 Note that by circular street, we mean if you number the houses from 1 to n , then the right house of house i is house i+1 for i < n , and the right house of house n is house 1 . 
 
 Return ans which represents the number of houses on this street. 

 Example 1: 
 
```
Input:
 street = [1,1,1,1], k = 10

Output:
 4

Explanation:
 There are 4 houses, and all their doors are open. 
The number of houses is less than k, which is 10.
```

 Example 2: 
 
```
Input:
 street = [1,0,1,1,0], k = 5

Output:
 5

Explanation:
 There are 5 houses, and the doors of the 1st, 3rd, and 4th house (moving in the right direction) are open, and the rest are closed.
The number of houses is equal to k, which is 5.
```

 Constraints: 

 n == number of houses 
 
 1 <= n <= k <= 10 5 
 
 street is circular by definition provided in the statement. 
 
 The input is generated such that at least one of the doors is open.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int houseCount(Street* street, int k) {
        while (!street->isDoorOpen()) street->moveRight();
        int answer=0;
        for (int distance=1;distance<=k;++distance) {
            street->moveRight();
            if(street->isDoorOpen()) {
                answer=distance;
                street->closeDoor();
            }
        }
        return answer;
    }
};
```


## 3253. Construct String with Minimum Cost (Easy)

**Problem:** https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Hash map, Ordered map, Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string target , an array of strings words , and an integer array costs , both arrays of the same length. 
 
 Imagine an empty string s . 
 
 You can perform the following operation any number of times (including zero ): 

 Choose an index i in the range [0, words.length - 1] . 
 
 Append words[i] to s . 
 
 The cost of operation is costs[i] . 

 Return the minimum cost to make s equal to target . If it's not possible, return -1. 

 Example 1: 

 Input: target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5] 
 
 Output: 7 
 
 Explanation: 
 
 The minimum cost can be achieved by performing the following operations: 

 Select index 1 and append "abc" to s at a cost of 1, resulting in s = "abc" . 
 
 Select index 2 and append "d" to s at a cost of 1, resulting in s = "abcd" . 
 
 Select index 4 and append "ef" to s at a cost of 5, resulting in s = "abcdef" . 

 Example 2: 

 Input: target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100] 
 
 Output: -1 
 
 Explanation: 
 
 It is impossible to make s equal to target , so we return -1. 

 Constraints: 

 1 <= target.length <= 2000 
 
 1 <= words.length == costs.length <= 50 
 
 1 <= words[i].length <= target.length 
 
 target and words[i] consist only of lowercase English letters. 
 
 1 <= costs[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int minimumCost(string target, vector<string>& words, vector<int>& costs) {
        unordered_map<string, int> cheapest;
        for (int i = 0; i < static_cast<int>(words.size()); ++i) {
            if (!cheapest.count(words[i])) cheapest[words[i]] = costs[i];
            else cheapest[words[i]] = min(cheapest[words[i]], costs[i]);
        }
        const long long INF = (1LL << 60);
        int n = target.size();
        vector<long long> dp(n + 1, INF);
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            if (dp[i] == INF) continue;
            for (const auto& item : cheapest) {
                int len = item.first.size();
                if (i + len <= n && target.compare(i, len, item.first) == 0) {
                    dp[i + len] = min(dp[i + len], dp[i] + item.second);
                }
            }
        }
        return dp[n] == INF ? -1 : static_cast<int>(dp[n]);
    }
};
```


## 3778. Minimum Distance Excluding One Maximum Weighted Edge

**Problem:** https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Priority queue, Queue, Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a positive integer n and a 2D integer array edges , where edges[i] = [u i , v i , w i ] . 
 
 There is a weighted connected simple undirected graph with n nodes labeled from 0 to n - 1 . Each [u i , v i , w i ] in edges represents an edge between node u i and node v i with positive weight w i . 
 
 The cost of a path is the sum of weights of the edges in the path, excluding the edge with the maximum weight. If there are multiple edges in the path with the maximum weight, only the first such edge is excluded. 
 
 Return an integer representing the minimum cost of a path going from node 0 to node n - 1 . 

 Example 1: 

 Input: n = 5, edges = [[0,1,2],[1,2,7],[2,3,7],[3,4,4]] 
 
 Output: 13 
 
 Explanation: 
 
 There is only one path going from node 0 to node 4: 0 -> 1 -> 2 -> 3 -> 4 . 
 
 The edge weights on this path are 2, 7, 7, and 4. 
 
 Excluding the first edge with maximum weight, which is 1 -> 2 , the cost of this path is 2 + 7 + 4 = 13 . 

 Example 2: 

 Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,50000]] 
 
 Output: 0 
 
 Explanation: 
 
 There are two paths going from node 0 to node 2: 

 0 -> 1 -> 2 

 The edge weights on this path are 1 and 1. 
 
 Excluding the first edge with maximum weight, which is 0 -> 1 , the cost of this path is 1. 

 0 -> 2 

 The only edge weight on this path is 1. 
 
 Excluding the first edge with maximum weight, which is 0 -> 2 , the cost of this path is 0. 
 
 The minimum cost is min(1, 0) = 0 . 

 Constraints: 

 2 <= n <= 5 * 10 4 
 
 n - 1 <= edges.length <= 10 9 
 
 edges[i] = [u i , v i , w i ] 
 
 0 <= u i < v i < n 
 
 [u i , v i ] != [u j , v j ] 
 
 1 <= w i <= 5 * 10 4 
 
 The graph is connected.

### C++ solution

**Source:** accepted_cpp_submission

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


## 3802. Number of Ways to Paint Sheets

**Problem:** https://leetcode.com/problems/number-of-ways-to-paint-sheets/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer n representing the number of sheets. 
 
 You are also given an integer array limit of size m , where limit[i] is the maximum number of sheets that can be painted using color i . 
 
 You must paint all n sheets under the following conditions: 

 Exactly two distinct colors are used. 
 
 Each color must cover a single contiguous segment of sheets. 
 
 The number of sheets painted with color i cannot exceed limit[i] . 

 Return an integer denoting the number of distinct ways to paint all sheets. Since the answer may be large, return it modulo 10 9 + 7 . 
 
 Note: Two ways differ if at least one sheet is painted with a different color. 

 Example 1: 

 Input: n = 4, limit = [3,1,2] 
 
 Output: 6 
 
 Explanation: ​​​​​​​ 
For each ordered pair (i, j) , where color i is used for the first segment and color j for the second segment ( i != j ), a split of x and 4 - x is valid if 1 <= x <= limit[i] and 1 <= 4 - x <= limit[j] .

 Valid pairs and counts are: 

 (0, 1): x = 3 
 
 (0, 2): x = 2, 3 
 
 (1, 0): x = 1 
 
 (2, 0): x = 1, 2 

 Therefore, there are 6 valid ways in total. 

 Example 2: 

 Input: n = 3, limit = [1,2] 
 
 Output: 2 
 
 Explanation: 
 
 For each ordered pair (i, j) , where color i is used for the first segment and color j for the second segment ( i != j ), a split of x and 3 - x is valid if 1 <= x <= limit[i] and 1 <= 3 - x <= limit[j] . 
 
 Valid pairs and counts are: 

 (0, 1): x = 1 
 
 (1, 0): x = 2 

 Hence, there are 2 valid ways in total. 

 Example 3: 

 Input: n = 3, limit = [2,2] 
 
 Output: 4 
 
 Explanation: 
 
 For each ordered pair (i, j) , where color i is used for the first segment and color j for the second segment ( i != j ), a split of x and 3 - x is valid if 1 <= x <= limit[i] and 1 <= 3 - x <= limit[j] . 
 
 Valid pairs and counts are: 

 (0, 1): x = 1, 2 
 
 (1, 0): x = 1, 2 

 Therefore, there are 4 valid ways in total. 

 Constraints: 

 2 <= n <= 10 9 
 
 2 <= m == limit.length <= 10 5 
 
 1 <= limit[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

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


## 3893. Maximum Team Size with Overlapping Intervals

**Problem:** https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two integer arrays startTime and endTime of length n . 

 startTime[i] represents the start time of the i th employee. 
 
 endTime[i] represents the end time of the i th employee. 

 Two employees i and j can interact if their time intervals overlap . Two intervals are considered overlapping if they share at least one common time point. 
 
 A team is valid if there exists at least one employee in the team who can interact with every other member of the team. 
 
 Return an integer denoting the maximum possible size of such a team. 

 Example 1: 

 Input: startTime = [1,2,3], endTime = [4,5,6] 
 
 Output: 3 
 
 Explanation: 

 For i = 0 with interval [1, 4] . 
 
 It overlaps with i = 1 having interval [2, 5] and i = 2 having interval [3, 6] . 
 
 Thus, index 0 can interact with all other indices, so the team size is 3. 

 Example 2: 

 Input: startTime = [2,5,8], endTime = [3,7,9] 
 
 Output: 1 
 
 Explanation: 

 For i = 0 , interval [2, 3] does not overlap with [5, 7] or [8, 9] . 
 
 For i = 1 , interval [5, 7] does not overlap with [2, 3] or [8, 9] . 
 
 For i = 2 , interval [8, 9] does not overlap with [2, 3] or [5, 7] . 
 
 Thus, no index can interact with others, so the maximum team size is 1. 

 Example 3: 

 Input: startTime = [3,4,6], endTime = [8,5,7] 
 
 Output: 3 
 
 Explanation: 

 For i = 0 with interval [3, 8] . 
 
 It overlaps with i = 1 having interval [4, 5] and i = 2 having interval [6, 7] . 
 
 Thus, index 0 can interact with all other indices, so the team size is 3. 

 Constraints: 

 1 <= n == startTime.length == endTime.length <= 10 5 
 
 0 <= startTime[i] <= endTime[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int maximumTeamSize(vector<int>& startTime,vector<int>& endTime){vector<int> a=startTime,b=endTime;sort(a.begin(),a.end());sort(b.begin(),b.end());int ans=0;for(int i=0;i<(int)a.size();++i){int x=upper_bound(a.begin(),a.end(),endTime[i])-a.begin();int y=lower_bound(b.begin(),b.end(),startTime[i])-b.begin();ans=max(ans,x-y);}return ans;}};
```


## 3907. Count Smaller Elements With Opposite Parity

**Problem:** https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of length n . 
 
 The score of an index i is defined as the number of indices j such that: 

 i < j < n 
 
 nums[j] < nums[i] 
 
 nums[i] and nums[j] have different parity (one is even and the other is odd). 

 Return an integer array answer of length n , where answer[i] is the score of index i . 

 Example 1: 

 Input: nums = [5,2,4,1,3] 
 
 Output: [2,1,2,0,0] 
 
 Explanation: 

 For i = 0 , the elements nums[1] = 2 and nums[2] = 4 are smaller and have different parity. 
 
 For i = 1 , the element nums[3] = 1 is smaller and has different parity. 
 
 For i = 2 , the elements nums[3] = 1 and nums[4] = 3 are smaller and have different parity. 
 
 No valid elements exist for the remaining indices. 

 Thus, the answer = [2, 1, 2, 0, 0] . 

 Example 2: 

 Input: nums = [4,4,1] 
 
 Output: [1,1,0] 
 
 Explanation: ​​​​​​​ 
 
 For i = 0 and i = 1 , the element nums[2] = 1 is smaller and has different parity. Thus, the answer = [1, 1, 0] . 

 Example 3: 

 Input: nums = [7] 
 
 Output: [0] 
 
 Explanation: 
 
 No elements exist to the right of index 0, so its score is 0. Thus, the answer = [0] . 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9 ​​​​​​​

### C++ solution

**Source:** accepted_cpp_submission

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


## 3963. Create Grid With Exactly One Path

**Problem:** https://leetcode.com/problems/create-grid-with-exactly-one-path/

**Difficulty:** Easy | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two integers m and n , representing the number of rows and columns of a grid. 
 
 Construct any m x n grid consisting only of the characters '.' and '#' , where: 

 '.' represents a free cell. 
 
 '#' represents an obstacle cell. 

 A valid path is a sequence of free cells that: 

 Starts at the top-left cell (0, 0) . 
 
 Ends at the bottom-right cell (m - 1, n - 1) . 
 
 Moves only:

 Right, from (i, j) to (i, j + 1) , or 
 
 Down, from (i, j) to (i + 1, j) . 

 Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell. 

 Example 1: 

 Input: m = 2, n = 3 
 
 Output: ["..#","#.."] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2026/05/26/screenshot-2026-05-26-at-61005pm.png] 
 
 The only valid path is: (0,0) → (0,1) → (1,1) → (1,2) 

 Example 2: 

 Input: m = 3, n = 3 
 
 Output: ["..#","#..","##."] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2026/05/26/screenshot-2026-05-26-at-61129pm.png] 
 
 The only valid path is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2) 

 Example 3: 

 Input: m = 1, n = 4 
 
 Output: ["...."] 
 
 Explanation: 
 
 The only valid path is: (0,0) → (0,1) → (0,2) → (0,3) 

 Constraints: 

 1 <= m, n <= 25

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<string> createGrid(int m, int n) {
        vector<string> grid(m, string(n, '#'));
        for (int j = 0; j < n; ++j) grid[0][j] = '.';
        for (int i = 0; i < m; ++i) grid[i][n - 1] = '.';
        return grid;
    }
};
```


## 4029. Elevator Requests IV

**Problem:** https://leetcode.com/problems/elevator-requests-iv/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Ordered map, Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer n denoting the number of floors in a building, where the floors are numbered from 0 to n - 1 . 
 
 You are also given an integer start and a 2D integer array requests , where requests[i] = [arrival i , floor i ] indicates that a request for floor i is made at time arrival i . 
 
 At time 0, the elevator is at floor start . 
 
 At each second, the elevator may move up by 1 floor, move down by 1 floor, or remain on its current floor. 
 
 A request can be fulfilled only at or after its arrival time; it is fulfilled instantly when the elevator is on its requested floor at any time from its arrival time onward. 
 
 Return the minimum time needed to fulfill all requests. 

 Example 1: 

 Input: n = 9, start = 0, requests = [[0,8],[6,5]] 
 
 Output: 9 
 
 Explanation: 

 Move from floor 0 ( start ) to floor 5 ( requests[1][1] ) in 5 seconds, reaching at time 5. Since requests[1][0] = 6 , wait until time 6 to fulfill it. 
 
 Move from floor 5 to floor 8 ( requests[0][1] ) in 3 seconds, fulfilling it at time 9. 

 Thus, all requests are fulfilled by time 9. 

 Example 2: 

 Input: n = 8, start = 5, requests = [[1,7],[7,3]] 
 
 Output: 7 
 
 Explanation: 

 Move from floor 5 ( start ) to floor 7 ( requests[0][1] ) in 2 seconds, reaching at time 2. Since requests[0][0] = 1 has already passed, floor 7 is fulfilled at time 2. 
 
 Move from floor 7 to floor 3 ( requests[1][1] ) in 4 seconds, reaching at time 6. Since requests[1][0] = 7 , wait until time 7. 

 Thus, all requests are fulfilled by time 7. 

 Example 3: 

 Input: n = 7, start = 3, requests = [[0,5],[0,1],[6,3]] 
 
 Output: 8 
 
 Explanation: 

 Move from floor 3 ( start ) to floor 5 ( requests[0][1] ) in 2 seconds, fulfilling it at time 2. 
 
 Move from floor 5 to floor 1 ( requests[1][1] ) in 4 seconds, fulfilling it at time 6. 
 
 Move from floor 1 to floor 3 ( requests[2][1] ) in 2 seconds, reaching at time 8. Its request arrived at requests[2][0] = 6 , so floor 3 is fulfilled at time 8. 

 Thus, all requests are fulfilled by time 8. 

 Constraints: 

 1 <= n <= 10 9 
 
 1 <= requests.length <= 500 
 
 requests[i] == [arrival i , floor i ] 
 
 0 <= arrival i <= 10 9 
 
 0 <= start, floor i <= n - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp

class Solution {
    using ll = long long;
    static constexpr ll INF = (1LL << 62);

public:
    long long elevatorRequests(
        int n,
        int start,
        vector<vector<int>>& requests
    ) {
        vector<vector<int>> noravelqui = requests;

        map<ll, ll> latest;

        for (const auto& r : noravelqui) {
            latest[r[1]] = max(latest[r[1]], (ll)r[0]);
        }

        int m = (int)latest.size();

        vector<ll> floor, arrival;

        for (const auto& p : latest) {
            floor.push_back(p.first);
            arrival.push_back(p.second);
        }

        auto feasible = [&](ll T) -> bool {
            vector<ll> left(m, INF), right(m, INF);
            vector<ll> nextLeft(m), nextRight(m);

            // Intervals of length 1.
            for (int i = 0; i < m; ++i) {
                if (arrival[i] <= T) {
                    left[i] = 0;
                    right[i] = 0;
                }
            }

            for (int len = 1; len < m; ++len) {
                fill(nextLeft.begin(), nextLeft.end(), INF);
                fill(nextRight.begin(), nextRight.end(), INF);

                for (int l = 0; l + len <= m; ++l) {
                    int r = l + len - 1;

                    if (left[l] != INF) {
                        ll t = left[l];

                        if (l > 0) {
                            ll nt = t + floor[l] - floor[l - 1];

                            if (nt <= T - arrival[l - 1]) {
                                nextLeft[l - 1] =
                                    min(nextLeft[l - 1], nt);
                            }
                        }

                        if (r + 1 < m) {
                            ll nt = t + floor[r + 1] - floor[l];

                            if (nt <= T - arrival[r + 1]) {
                                nextRight[l] =
                                    min(nextRight[l], nt);
                            }
                        }
                    }

                    if (right[l] != INF) {
                        ll t = right[l];

                        if (l > 0) {
                            ll nt = t + floor[r] - floor[l - 1];

                            if (nt <= T - arrival[l - 1]) {
                                nextLeft[l - 1] =
                                    min(nextLeft[l - 1], nt);
                            }
                        }

                        if (r + 1 < m) {
                            ll nt = t + floor[r + 1] - floor[r];

                            if (nt <= T - arrival[r + 1]) {
                                nextRight[l] =
                                    min(nextRight[l], nt);
                            }
                        }
                    }
                }

                left.swap(nextLeft);
                right.swap(nextRight);
            }

            return (
                left[0] + llabs(floor[0] - start) <= T ||
                right[0] + llabs(floor[m - 1] - start) <= T
            );
        };

        ll maxArrival = 0;

        for (ll a : arrival)
            maxArrival = max(maxArrival, a);

        ll low = 0;
        ll high = maxArrival + 3LL * n;

        while (low < high) {
            ll mid = low + (high - low) / 2;

            if (feasible(mid))
                high = mid;
            else
                low = mid + 1;
        }

        return low;
    }
};
```


## 4070. Minimum Rotations to Dial a Number I

**Problem:** https://leetcode.com/problems/minimum-rotations-to-dial-a-number-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string s of length 10 consisting of digits. 
 
 The dial contains the digits 0 through 9 in order and is circular , so 0 and 9 are adjacent. The pointer initially points to 0. 
 
 To dial each digit of s in order , rotate the pointer until it points to that digit. Each rotation moves the pointer to an adjacent digit, and you may rotate in either direction. Dialing a digit that the pointer already points to requires no rotations. 
 
 Return the minimum total number of rotations needed to dial every digit of s . 

 Example 1: 

 Input: s = "0192837465" 
 
 Output: 25 
 
 Explanation: 

 Step 
 From 
 To 
 Rotations 

 1 
 0 
 0 
 0 

 2 
 0 
 1 
 1 

 3 
 1 
 9 
 2 

 4 
 9 
 2 
 3 

 5 
 2 
 8 
 4 

 6 
 8 
 3 
 5 

 7 
 3 
 7 
 4 

 8 
 7 
 4 
 3 

 9 
 4 
 6 
 2 

 10 
 6 
 5 
 1 

 The total is 0 + 1 + 2 + 3 + 4 + 5 + 4 + 3 + 2 + 1 = 25 , which is the minimum total number of rotations. 

 Example 2: 

 Input: s = "1200210200" 
 
 Output: 12 
 
 Explanation: 

 Step 
 From 
 To 
 Rotations 

 1 
 0 
 1 
 1 

 2 
 1 
 2 
 1 

 3 
 2 
 0 
 2 

 4 
 0 
 0 
 0 

 5 
 0 
 2 
 2 

 6 
 2 
 1 
 1 

 7 
 1 
 0 
 1 

 8 
 0 
 2 
 2 

 9 
 2 
 0 
 2 

 10 
 0 
 0 
 0 

 The total is 1 + 1 + 2 + 0 + 2 + 1 + 1 + 2 + 2 + 0 = 12 , which is the minimum total number of rotations. 

 Constraints: 

 s.length == 10 
 
 s consists only of digits '0' to '9'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    public: int minRotations(string s) {
        int p=0,ans=0;
        for(char c:s) {
            int x=c-'0',d=abs(x-p);
            ans+=min(d,10-d);
            p=x;
        }
        return ans;
    }
}
;
```


## 4071. Minimum Rotations to Dial a Number II

**Problem:** https://leetcode.com/problems/minimum-rotations-to-dial-a-number-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer n and a string s of length n consisting of digits. 
 
 The dial contains the digits 0 through 9 in order and is circular , so 0 and 9 are adjacent. The pointer initially points to 0. 
 
 To dial each digit of s in order , rotate the pointer until it points to that digit. Each rotation moves the pointer to an adjacent digit, and you may rotate in either direction. Dialing a digit that the pointer already points to requires no rotations. 
 
 Before dialing, you may perform the following operation at most once : 

 Choose an index k such that 0 <= k < n and reverse the suffix s[k..n - 1] . 

 Return the minimum total number of rotations needed to dial the string after optimally choosing whether to perform the operation and which suffix to reverse. 

 Example 1: 

 Input: n = 4, s = "1502" 
 
 Output: 9 
 
 Explanation: 
 
 Reverse the suffix starting at k = 1 to obtain "1205" , then dial it. 

 Step 
 From 
 To 
 Rotations 

 1 
 0 
 1 
 1 

 2 
 1 
 2 
 1 

 3 
 2 
 0 
 2 

 4 
 0 
 5 
 5 

 The total is 1 + 1 + 2 + 5 = 9 , which is the minimum total number of rotations. 

 Example 2: 

 Input: n = 4, s = "2916" 
 
 Output: 12 
 
 Explanation: 
 
 Choose not to reverse a suffix and dial "2916" . 

 Step 
 From 
 To 
 Rotations 

 1 
 0 
 2 
 2 

 2 
 2 
 9 
 3 

 3 
 9 
 1 
 2 

 4 
 1 
 6 
 5 

 The total is 2 + 3 + 2 + 5 = 12 , which is the minimum total number of rotations. 

 Example 3: 

 Input: n = 4, s = "4219" 
 
 Output: 6 
 
 Explanation: 
 
 Reverse the suffix starting at k = 0 , which reverses the entire string, to obtain "9124" , then dial it. 

 Step 
 From 
 To 
 Rotations 

 1 
 0 
 9 
 1 

 2 
 9 
 1 
 2 

 3 
 1 
 2 
 1 

 4 
 2 
 4 
 2 

 The total is 1 + 2 + 1 + 2 = 6 , which is the minimum total number of rotations. 

 Constraints: 

 1 <= n == s.length <= 10 5 ​​​​​​​ 
 
 s consists only of digits '0' to '9'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    int dist(char a, char b) {
        int d = abs(a - b);
        return min(d, 10 - d);
    }
public:
    int minRotations(int n, string s) {
        int base = dist('0', s[0]);
        for (int i = 1; i < n; ++i) base += dist(s[i - 1], s[i]);
        int ans = base;
        for (int k = 0; k < n; ++k) {
            int before = k == 0 ? dist('0', s[0]) : dist(s[k - 1], s[k]);
            int after = k == 0 ? dist('0', s[n - 1]) : dist(s[k - 1], s[n - 1]);
            ans = min(ans, base - before + after);
        }
        return ans;
    }
};
```


## 4072. Maximum Alternating Subarray Sum With One Deletion

**Problem:** https://leetcode.com/problems/maximum-alternating-subarray-sum-with-one-deletion/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . 
 
 You may delete at most one element from nums , then choose a subarray of the resulting array. 
 
 Return the maximum possible alternating sum of the chosen subarray. 
 
 The alternating sum of an array is the sum of its elements at even indices minus the sum of its elements at odd indices. The chosen subarray is reindexed starting from 0 before calculating its alternating sum. 

 Example 1: 

 Input: nums = [5,-5,1] 
 
 Output: 11 
 
 Explanation: 
 
 Choose not to delete an element and select the entire array. Its alternating sum is 5 - (-5) + 1 = 11 , which is the maximum possible. 

 Example 2: 

 Input: nums = [10,-5,-100] 
 
 Output: 110 
 
 Explanation: 
 
 Delete nums[1] = -5 to obtain [10,-100] , then select the entire resulting array. Its alternating sum is 10 - (-100) = 110 , which is the maximum possible. 

 Example 3: 

 Input: nums = [4,7] 
 
 Output: 7 
 
 Explanation: 
 
 Choose not to delete an element and select the subarray [7] . Its alternating sum is 7, which is the maximum possible. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 -10 5 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

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


## 4073. Count Good Strings

**Problem:** https://leetcode.com/problems/count-good-strings/

**Difficulty:** Hard | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer n . 
 
 A string is considered good if it consists only of the characters 'a' and 'b' , and one of the following holds: 

 It contains exactly one distinct character, and its length is odd . 
 
 It can be written as s = s1 + s2 , where s1 and s2 are non-empty good strings, and the last character of s1 is different from the first character of s2 . 

 Return the number of good strings of length n , modulo 10 9 + 7 . 
 
 Here, + denotes string concatenation. 

 Example 1: 

 Input: n = 4 
 
 Output: 6 
 
 Explanation: 

 The good strings are "aaab" , "abbb" , "baaa" , "bbba" , "abab" , and "baba" . 
 
 For example, "aaab" = "aaa" + "b" . Both parts are good because each contains one distinct character and has odd length, and their characters at the boundary are different. 
 
 Also, "ab" = "a" + "b" is good, so "abab" = "ab" + "ab" is good because the boundary characters are different. 
 
 Thus, the answer is 6. 

 Example 2: 

 Input: n = 3 
 
 Output: 4 
 
 Explanation: 
 
 The good strings are "aaa" , "bbb" , "aba" , and "bab" . Thus, the answer is 4. 

 Example 3: 

 Input: n = 2 
 
 Output: 2 
 
 Explanation: 
 
 The good strings are "ab" and "ba" . Thus, the answer is 2. 

 Constraints: 

 1 <= n <= 10 15

### C++ solution

**Source:** accepted_cpp_submission

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


## 4074. Maximum Product Pair With Target Sum

**Problem:** https://leetcode.com/problems/maximum-product-pair-with-target-sum/

**Difficulty:** Easy | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and an integer target . 
 
 A pair of distinct indices (i, j) is valid if: 

 nums[i] + nums[j] == target 
 
 nums[i] > nums[j] 

 Return a valid pair [i, j] whose product nums[i] * nums[j] is maximum among all valid pairs. If no valid pair exists, return [-1, -1] . 
 
 If multiple valid pairs achieve the maximum product, you may return any of them. 

 Example 1: 

 Input: nums = [1,2,3,4], target = 5 
 
 Output: [2,1] 
 
 Explanation: 
 
 There are 2 valid pairs: 

 No. 
 (i, j) 
 nums[i] 
 nums[j] 
 Sum 
 Product 

 1 
 (3, 0) 
 4 
 1 
 5 
 4 

 2 
 (2, 1) 
 3 
 2 
 5 
 6 

 Both pairs sum to 5 and satisfy nums[i] > nums[j] . The second pair has the larger product, 3 * 2 = 6 , so the answer is [2, 1] . 

 Example 2: 

 Input: nums = [-3,-1,4,2], target = 1 
 
 Output: [3,1] 
 
 Explanation: 
 
 There are 2 valid pairs: 

 No. 
 (i, j) 
 nums[i] 
 nums[j] 
 Sum 
 Product 

 1 
 (2, 0) 
 4 
 -3 
 1 
 -12 

 2 
 (3, 1) 
 2 
 -1 
 1 
 -2 

 Since -2 > -12 , the pair at indices (3, 1) is chosen and the answer is [3, 1] . 

 Example 3: 

 Input: nums = [3,3,5], target = 6 
 
 Output: [-1,-1] 
 
 Explanation: 
 
 ​​​​​​​ No valid pair exists, since nums[0] and nums[1] sum to 6 but are equal. 

 Constraints: 

 2 <= nums.length <= 100 
 
 -100 <= nums[i], target <= 100 ​​​​​​​

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    public: vector<int> maxProductPair(vector<int>& a,int target) {
        long long best=LLONG_MIN;
        vector<int> ans= {
            -1,-1
        }
        ;
        for(int i=0; i<(int)a.size(); i++)for(int j=0; j<(int)a.size(); j++)if(i!=j&&a[i]>a[j]&&a[i]+a[j]==target) {
            long long p=1LL*a[i]*a[j];
            if(p>best) {
                best=p;
                ans= {
                    i,j
                }
                ;
            }
        }
        return ans;
    }
}
;
```


## 4075. Longest Resilient Subarray I

**Problem:** https://leetcode.com/problems/longest-resilient-subarray-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and an integer k . 
 
 A subarray is resilient if, for every position in it, deleting the element at that position leaves the remaining elements with a sum divisible by k . 
 
 For a subarray of length 1, the remaining sum is 0, which is divisible by k . 
 
 Return the length of the longest resilient subarray . 

 Example 1: 

 Input: nums = [2,4,6,3], k = 2 
 
 Output: 3 
 
 Explanation: 
 
 The subarray [2, 4, 6] sums to 12. Deleting 2, 4, or 6 leaves a sum of 10, 8, or 6, respectively, each of which is divisible by 2. Therefore, the answer is 3. 

 Example 2: 

 Input: nums = [1,4,7,1], k = 3 
 
 Output: 4 
 
 Explanation: 
 
 The subarray [1, 4, 7, 1] sums to 13. Deleting the first 1, the 4, the 7, or the last 1 leaves a sum of 12, 9, 6, or 12, respectively, each of which is divisible by 3. Therefore, the answer is 4. 

 Example 3: 

 Input: nums = [5,5,4,8], k = 4 
 
 Output: 2 
 
 Explanation: 
 
 The subarray [5, 5] is not resilient, since deleting either 5 leaves a sum of 5, which is not divisible by 4. 
 
 The subarray [4, 8] sums to 12. Deleting 4 or 8 leaves a sum of 8 or 4, respectively, each of which is divisible by 4. Therefore, the answer is 2. 

 Constraints: 

 1 <= nums.length <= 2500 
 
 1 <= nums[i] <= 10 5 
 
 1 <= k <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int resilientSubarray(vector<int>& nums, int k) {
        int n = nums.size(), ans = 1;
        for (int l = 0; l < n; ++l) {
            int residue = nums[l] % k;
            for (int r = l + 1; r < n; ++r) {
                if (nums[r] % k != residue) break;
                int len = r - l + 1;
                if (1LL * (len - 1) * residue % k == 0) ans = max(ans, len);
            }
        }
        return ans;
    }
};
```


## 4076. Longest Resilient Subarray II

**Problem:** https://leetcode.com/problems/longest-resilient-subarray-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and an integer k . 
 
 A subarray is resilient if, for every position in it, deleting the element at that position leaves the remaining elements with a sum divisible by k . 
 
 For a subarray of length 1, the remaining sum is 0, which is divisible by k . 
 
 Return the length of the longest resilient subarray . 

 Example 1: 

 Input: nums = [2,4,6,3], k = 2 
 
 Output: 3 
 
 Explanation: 
 
 The subarray [2, 4, 6] sums to 12. Deleting 2, 4, or 6 leaves a sum of 10, 8, or 6, respectively, each of which is divisible by 2. Therefore, the answer is 3. 

 Example 2: 

 Input: nums = [1,4,7,1], k = 3 
 
 Output: 4 
 
 Explanation: 
 
 The subarray [1, 4, 7, 1] sums to 13. Deleting the first 1, the 4, the 7, or the last 1 leaves a sum of 12, 9, 6, or 12, respectively, each of which is divisible by 3. Therefore, the answer is 4. 

 Example 3: 

 Input: nums = [5,5,4,8], k = 4 
 
 Output: 2 
 
 Explanation: 
 
 The subarray [5, 5] is not resilient, since deleting either 5 leaves a sum of 5, which is not divisible by 4. 
 
 The subarray [4, 8] sums to 12. Deleting 4 or 8 leaves a sum of 8 or 4, respectively, each of which is divisible by 4. Therefore, the answer is 2. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 5 
 
 1 <= k <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    int gcdInt(int a, int b) {
        while (b) { int t = a % b; a = b; b = t; }
        return a;
    }
public:
    int resilientSubarray(vector<int>& nums, int k) {
        int n = nums.size(), ans = 1;
        for (int i = 0; i < n;) {
            int j = i, r = nums[i] % k;
            while (j < n && nums[j] % k == r) ++j;
            int len = j - i, period = k / gcdInt(k, r);
            int best = 1 + ((len - 1) / period) * period;
            ans = max(ans, best);
            i = j;
        }
        return ans;
    }
};
```


## 4077. Minimize Inversions in a Prefix Tree

**Problem:** https://leetcode.com/problems/minimize-inversions-in-a-prefix-tree/

**Difficulty:** Hard | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array words of n unique strings containing only lowercase English letters from 'a' to 'j' . You are also given an integer array target containing each index from 0 to n - 1 exactly once. 
 
 Build a prefix tree from words : 

 The root represents the empty string "" . 
 
 Each other node represents a different non-empty prefix of a word. The parent of a node is the prefix obtained by removing its last character. 
 
 The node representing the complete word words[i] is marked with index i . A marked node may also have children. 

 You may choose the order of the children of each node independently . You cannot change which node is a child's parent. 
 
 Traverse the tree starting at the root. When visiting a node, first record its index if it is marked. Then visit its children in the chosen order, completing the traversal of each child before moving to the next. This is a pre-order traversal . 
 
 The recorded indices form an array traversal of length n . Let pos[i] be the position of index i in target . 
 
 An inversion is a pair of positions (a, b) such that 0 <= a < b < n and pos[traversal[a]] > pos[traversal[b]] . 
 
 Return the minimum possible number of inversions over all choices of child orderings. 

 Example 1: 

 [Figure: https://assets.leetcode.com/uploads/2026/03/04/screenshot-2026-03-04-at-55332pm.png] ​​​​​​​​​​​​​​​​​​​​​ 
 
 Input: words = ["bad","bag","fig","fed"], target = [3,1,0,2] 
 
 Output: 2 
 
 Explanation: 
 
 Visit the root's "f" child before its "b" child. Within the "f" branch, visit "fed" before "fig" . Within the "b" branch, visit "bag" before "bad" . 
 
 This produces traversal = [3,2,1,0] : 

 Traversal position 
 Word index 
 Word 
 Position in target 

 0 
 3 
 "fed" 
 0 

 1 
 2 
 "fig" 
 3 

 2 
 1 
 "bag" 
 1 

 3 
 0 
 "bad" 
 2 

 The positions in target are [0,3,1,2] . The inversions are the pairs of traversal positions (1,2) and (1,3) , since 3 > 1 and 3 > 2 . 
 
 No child ordering produces fewer than 2 inversions. 

 Example 2: 

 Input: words = ["ab","ac","ba","bc"], target = [0,3,1,2] 
 
 Output: 1 
 
 Explanation: 
 
 Visit the root's "a" child before its "b" child. Within these branches, visit "ab" before "ac" , and "bc" before "ba" . 
 
 This produces traversal = [0,1,3,2] : 

 Traversal position 
 Word index 
 Word 
 Position in target 

 0 
 0 
 "ab" 
 0 

 1 
 1 
 "ac" 
 2 

 2 
 3 
 "bc" 
 1 

 3 
 2 
 "ba" 
 3 

 The positions in target are [0,2,1,3] . The only inversion is the pair of traversal positions (1,2) , since 2 > 1 . 
 
 No child ordering produces zero inversions. 

 Constraints: 

 1 <= n == words.length <= 10 4 
 
 1 <= words[i].length <= 20 
 
 words[i] contains only lowercase English letters from 'a' to 'j' ​​​​​​​ 
 
 All words[i] are unique 
 
 0 <= target[i] <= n - 1 
 
 target is a permutation of integers from 0 to n - 1

### C++ solution

**Source:** accepted_cpp_submission

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


## 4078. Three Fibonacci Sum

**Problem:** https://leetcode.com/problems/three-fibonacci-sum/

**Difficulty:** Easy | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer n . 
 
 The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers. Its first few terms are 0, 1, 1, 2, 3, 5, 8, 13, ... . 
 
 Return true if n can be expressed as the sum of three consecutive terms in the Fibonacci sequence, and false otherwise. 

 Example 1: 

 Input: n = 16 
 
 Output: true 
 
 Explanation: 
 
 The three consecutive terms 3, 5, and 8 have a sum of 3 + 5 + 8 = 16 . 

 Example 2: 

 Input: n = 8 
 
 Output: false 
 
 Explanation: 
 
 Although 1 + 2 + 5 = 8 , these terms are not consecutive in the Fibonacci sequence. No three consecutive terms have a sum of 8. 

 Example 3: 

 Input: n = 2 
 
 Output: true 
 
 Explanation: 
 
 The first three terms have a sum of 0 + 1 + 1 = 2 . 

 Constraints: 

 1 <= n <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    public: bool threeFibonacciSum(int n) {
        long long a=0,b=1;
        while(a+b+(a+b)<=n) {
            if(2*(a+b)==n)return true;
            long long c=a+b;
            a=b;
            b=c;
        }
        return false;
    }
}
;
```


## 4079. Prime Subset Selection I

**Problem:** https://leetcode.com/problems/prime-subset-selection-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two integers n and s . 
 
 Consider all prime numbers less than or equal to n . Select some of these primes such that: 

 The sum of the selected primes is less than or equal to s . 
 
 The number of selected primes is maximized . 
 
 Each prime can be selected at most once . 

 Return an integer array containing the selected primes in increasing order. If multiple optimal selections exist, return any of them. 
 
 If no prime can be selected, return an empty array. 

 Example 1: 

 Input: n = 7, s = 20 
 
 Output: [2,3,5,7] 
 
 Explanation: 

 The prime numbers less than or equal to n = 7 are 2, 3, 5, and 7. 
 
 The sum of all these primes is 2 + 3 + 5 + 7 = 17 , which is less than or equal to s = 20 . 
 
 Thus, the answer is [2, 3, 5, 7] . 

 Example 2: 

 Input: n = 15, s = 15 
 
 Output: [3,5,7] 
 
 Explanation: 

 The prime numbers less than or equal to n = 15 are 2, 3, 5, 7, 11, and 13. 
 
 One possible selection is [3, 5, 7] , whose sum is 3 + 5 + 7 = 15 . 
 
 The four smallest available primes have sum 2 + 3 + 5 + 7 = 17 , which exceeds s = 15 . Therefore, selecting four or more primes is impossible, and the maximum number of selected primes is three. 
 
 Thus, [3, 5, 7] is one possible answer. Other valid answers include [2, 3, 5] , [2, 3, 7] , and [2, 5, 7] . 

 Example 3: 

 Input: n = 5, s = 1 
 
 Output: [] 
 
 Explanation: 

 The smallest prime number is 2, which is greater than s = 1 . 
 
 Thus, no prime can be selected, so the answer is an empty array. 

 Constraints: 

 1 <= n <= 10 6 
 
 1 <= s <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> maxPrimes(int n, int s) {
        vector<bool> prime(n + 1, true);
        prime[0] = false;
        if (n >= 1) prime[1] = false;
        for (int p = 2; 1LL * p * p <= n; ++p) {
            if (prime[p]) for (int x = p * p; x <= n; x += p) prime[x] = false;
        }
        vector<int> ans;
        long long sum = 0;
        for (int p = 2; p <= n; ++p) {
            if (!prime[p]) continue;
            if (sum + p > s) break;
            sum += p;
            ans.push_back(p);
        }
        return ans;
    }
};
```


## 4080. Design Bus Seat Booking System

**Problem:** https://leetcode.com/problems/design-bus-seat-booking-system/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are asked to design a seat booking system for a bus. 
 
 The bus has n rows. Each row has four seats labeled "A" , "B" , "C" , and "D" . 
 
 Seats "A" and "D" are window seats; seats "B" and "C" are middle seats. In each row, seat "A" is adjacent to seat "B" , and seat "D" is adjacent to seat "C" . 
 
 Booking rules: 

 Booking a middle seat ( "B" or "C" ) always takes 1 second. 
 
 Booking a window seat ( "A" or "D" ) takes 1 second if its adjacent middle seat is not booked, or 3 seconds (an extra delay of 2 seconds) if its adjacent middle seat is already booked. 

 A seat is identified by a string such as "A1" or "D20" (one letter from A to D followed by its row number). 
 
 Implement the BusBooking class: 

 BusBooking(int n) : Initializes the system with n empty rows. 
 
 void toggle(string seat) : Books seat if it is free, or frees it if it is already booked. 
 
 int getTotalTime() : Returns the total time (in seconds) taken to book all currently booked seats, where the seats are booked in the order their toggle calls were made. If no seats are currently booked, return 0. 
 
 int getMinTime() : Returns the smallest possible total time (in seconds) to book all currently booked seats, over every possible order of booking them. If no seats are currently booked, return 0. 

 Note : The time cost of a seat is fixed at the moment it is booked, based on the seats booked at that time. Booking or freeing other seats afterward does not change the cost of a seat that is already booked. 

 Example 1: 

 Input: 
 ["BusBooking", "toggle", "toggle", "getTotalTime", "getMinTime", "toggle", "toggle", "getTotalTime", "getMinTime"] 
[[20], ["B3"], ["A3"], [], [], ["C3"], ["D3"], [], []] 
 
 Output: 
 [null, null, null, 4, 2, null, null, 8, 4] 
 
 Explanation 
BusBooking busBooking = new BusBooking(20); // start with 20 empty rows 
busBooking.toggle("B3"); // book "B3" , a middle seat, which costs 1 second. Total time is now 1. 
busBooking.toggle("A3"); // book "A3" , a window seat. Its adjacent middle "B3" is already booked, so it costs 3 seconds. Total time is now 1 + 3 = 4 . 
busBooking.getTotalTime(); // return 4, since in toggle order "B3" costs 1 and "A3" costs 3. 
busBooking.getMinTime(); // return 2. Booking "A3" before "B3" avoids the delay, so 2 seats takes 2 second to book. 
busBooking.toggle("C3"); // book "C3" , a middle seat, which costs 1 second. Total time is now 1 + 4 = 5 . 
busBooking.toggle("D3"); // book "D3" , a window seat. Its adjacent middle "C3" is already booked, so it costs 3 seconds. Total time is now 5 + 3 = 8 . 
busBooking.getTotalTime(); // return 8, since in toggle order the seat costs are 1, 3, 1, 3. 
busBooking.getMinTime(); // return 4. With the best possible booking order, no delay is added, so the 4 booked seats take 4 * 1 = 4 seconds. 
 
 Example 2: 

 Input: 
 ["BusBooking", "toggle", "toggle", "getTotalTime", "toggle", "toggle", "toggle", "getTotalTime", "getMinTime"] 
[[10], ["C7"], ["D7"], [], ["D7"], ["C7"], ["D7"], [], []] 
 
 Output: 
 [null, null, null, 4, null, null, null, 1, 1] 
 
 Explanation 
BusBooking busBooking = new BusBooking(10); // start with 10 empty rows 
busBooking.toggle("C7"); // book "C7" , a middle seat, which costs 1 second. Total time is now 1. 
busBooking.toggle("D7"); // book "D7" , a window seat. Its adjacent middle "C7" is already booked, so it costs 3 seconds. Total time is now 1 + 3 = 4 . 
busBooking.getTotalTime(); // return 4, since in toggle order "C7" costs 1 and "D7" costs 3. 
busBooking.toggle("D7"); // "D7" is already booked, so free it. This removes its cost of 3. Total time is now 4 - 3 = 1 . 
busBooking.toggle("C7"); // "C7" is already booked, so free it. This removes its cost of 1. Total time is now 1 - 1 = 0 , and row 7 is empty. 
busBooking.toggle("D7"); // book "D7" again, a window seat. Its adjacent middle "C7" is not booked this time, so it costs only 1 second. Total time is now 0 + 1 = 1 . 
busBooking.getTotalTime(); // return 1, since only "D7" is booked and it cost 1 this time. 
busBooking.getMinTime(); // return 1. With the best possible booking order, the 1 booked seat takes 1 * 1 = 1 second. 

 Constraints: 

 1 <= n <= 10 5 ​​​​​​​ 
 
 seat[0] is one of 'A' , 'B' , 'C' , 'D' . 
 
 The remaining characters of seat form an integer row with 1 <= row <= n . 
 
 The total number of calls to toggle , getTotalTime , and getMinTime does not exceed 10 5 .

### C++ solution

**Source:** accepted_cpp_submission

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


## 4081. Prime Subset Selection II

**Problem:** https://leetcode.com/problems/prime-subset-selection-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two integers n and s . 
 
 Consider all prime numbers less than or equal to n . Select a subset of these primes such that: 

 Each prime can be selected at most once . 
 
 The sum of the selected primes is as large as possible while remaining less than or equal to s . 
 
 Among subsets with the maximum sum, select one containing the fewest primes. 
 
 If multiple subsets remain tied, select the one whose elements, written in increasing order, form the lexicographically smallest array. 

 Return an integer array containing the selected primes in increasing order. If no valid non-empty subset exists, return an empty array. 

 Example 1: 

 Input: n = 7, s = 20 
 
 Output: [2, 3, 5, 7] 
 
 Explanation: 

 The prime numbers less than or equal to n = 7 are 2, 3, 5, and 7. 
 
 The sum of all these primes is 2 + 3 + 5 + 7 = 17 , which is less than or equal to s = 20 . 
 
 Thus, the answer is [2, 3, 5, 7] . 

 Example 2: 

 Input: n = 15, s = 18 
 
 Output: [5,13] 
 
 Explanation: 

 The prime numbers less than or equal to 15 are 2, 3, 5, 7, 11, and 13. 
 
 The subsets with sum 18 are [5, 13] , [7, 11] , [2, 3, 13] , and [2, 5, 11] . Since this sum equals s , it is the maximum possible sum. 
 
 Among these subsets, [5, 13] and [7, 11] contain the fewest primes: two. 
 
 Between these two subsets, [5, 13] is lexicographically smaller because its first element, 5, is smaller than 7. Thus, the answer is [5, 13] . 

 Example 3: 

 Input: n = 5, s = 1 
 
 Output: [] 
 
 Explanation: 

 The smallest prime number is 2, which is greater than s = 1 . 
 
 Thus, no prime can be selected, so the answer is an empty array. 

 Constraints: 

 1 <= n <= 1000 
 
 1 <= s <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> maxPrimeSubset(int n, int s) {
        vector<bool> prime(n + 1, true);
        if (n >= 0) prime[0] = false;
        if (n >= 1) prime[1] = false;
        for (int p = 2; p * p <= n; ++p) {
            if (prime[p]) {
                for (int x = p * p; x <= n; x += p) prime[x] = false;
            }
        }
        vector<vector<int>> dp(s + 1);
        vector<bool> reachable(s + 1, false);
        reachable[0] = true;
        for (int p = 2; p <= n; ++p) {
            if (!prime[p]) continue;
            for (int sum = s; sum >= p; --sum) {
                if (!reachable[sum - p]) continue;
                vector<int> candidate = dp[sum - p];
                candidate.push_back(p);
                if (!reachable[sum] || candidate.size() < dp[sum].size() ||
                    (candidate.size() == dp[sum].size() && candidate < dp[sum])) {
                    reachable[sum] = true;
                    dp[sum] = std::move(candidate);
                }
            }
        }
        for (int sum = s; sum >= 1; --sum) {
            if (reachable[sum]) return dp[sum];
        }
        return {};
    }
};
```


## 4082. Minimum Operations to Stabilize a Binary Tree

**Problem:** https://leetcode.com/problems/minimum-operations-to-stabilize-a-binary-tree/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Hash map, Ordered map, Priority queue, Queue, Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given the root of a binary tree . Each node contains an integer value representing its current state. 
 
 A binary tree is considered stable if for every node u : 

 If u.left exists, then |u.val - u.left.val| <= 1 
 
 If u.right exists, then |u.val - u.right.val| <= 1 

 In one operation, you may choose any node and increase or decrease its value by 1. 
 
 Return the minimum number of operations required to make the entire binary tree stable . 

 Example 1: 

 Input: root = [5,8,3] 
 
 Output: 3 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2026/02/16/screenshot-2026-02-16-at-21240pm.png] 

 Let u be the root node with value 5. Decrease the left child value from 8 to 6 using 2 operations. Then |u.val - u.left.val| = |5 - 6| = 1 . 
 
 Increase the right child value from 3 to 4 using 1 operation. Then |u.val - u.right.val| = |5 - 4| = 1 . 
 
 Thus, the answer is 2 + 1 = 3 . 

 Example 2: 

 Input: root = [2,-1,-4] 
 
 Output: 5 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2026/02/16/screenshot-2026-02-16-at-21340pm.png] 

 Let u be the root node with value 2. Decrease the value of u from 2 to −2 using 4 operations. 
 
 Decrease the right child value from −4 to −3 using 1 operation. Then |u.val - u.right.val| = |-2 - (−3)| = 1 . 
 
 Thus, the answer is 4 + 1 = 5 . 

 Example 3: 

 Input: root = [0,-2,2,-3,null,1] 
 
 Output: 3 
 
 Explanation: 
 
 ​​​​​​​ [Figure: https://assets.leetcode.com/uploads/2026/02/16/screenshot-2026-02-16-at-21826pm.png] ​​​​​​​​​​​​​​ 

 Let u be the root node with value 0. Increase the left child value from −2 to −1 using 1 operation, and decrease the right child value from 2 to 1 using 1 operation. 
 
 Now |u.val - u.left.val| = |0 - (−1)| = 1 and |u.val - u.right.val| = |0 - 1| = 1 . 
 
 Let v be the left child of u , now having value −1. Increase its left child from −3 to −2 using 1 operation so that |v.val - v.left.val| = |−1 - (−2)| = 1 . 
 
 The right subtree already satisfies the condition since |1 - 1| = 0 . 
 
 Thus, the answer is 1 + 1 + 1 = 3 .​​​​​​​ 

 Constraints: 

 The number of nodes in the tree is in the range [1, 5 * 10 4 ] . 
 
 -10 5 <= Node.val <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    struct Slope {
        priority_queue<long long> L;
        priority_queue<long long,vector<long long>,greater<long long>> R;
        long long shiftL=0,shiftR=0,cost=0;
        void addLeft(long long x) { // max(x-v,0)
            if(!R.empty())cost+=max(0LL,x-(R.top()+shiftR));
            R.push(x-shiftR);
            long long y=R.top()+shiftR;R.pop();
            L.push(y-shiftL);
        }
        void addRight(long long x) { // max(v-x,0)
            if(!L.empty())cost+=max(0LL,(L.top()+shiftL)-x);
            L.push(x-shiftL);
            long long y=L.top()+shiftL;L.pop();
            R.push(y-shiftR);
        }
        void window() {--shiftL;++shiftR;}
        size_t size()const{return L.size()+R.size();}
        void absorb(Slope &other) {
            cost+=other.cost;
            while(!other.L.empty()) {
                long long x=other.L.top()+other.shiftL;other.L.pop();
                addLeft(x);
            }
            while(!other.R.empty()) {
                long long x=other.R.top()+other.shiftR;other.R.pop();
                addRight(x);
            }
        }
    };
public:
    long long stabilizeBinaryTree(TreeNode* root) {
        if(!root)return 0;
        vector<TreeNode*> order(1,root);
        for(size_t i=0;i<order.size();++i) {
            TreeNode* u=order[i];
            if(u->left)order.push_back(u->left);
            if(u->right)order.push_back(u->right);
        }
        unordered_map<TreeNode*,Slope*> dp;
        for(int i=(int)order.size()-1;i>=0;--i) {
            TreeNode* u=order[i];
            Slope* cur=new Slope();
            cur->addLeft(u->val);cur->addRight(u->val);
            for(TreeNode* v:{u->left,u->right})if(v) {
                Slope* child=dp[v];
                child->window();
                if(cur->size()<child->size())swap(cur,child);
                cur->absorb(*child);
                delete child;
                dp.erase(v);
            }
            dp[u]=cur;
        }
        long long result=dp[root]->cost;
        delete dp[root];
        return result;
    }
};
```


## 4083. Minimum Deletions to Make Array Sharp

**Problem:** https://leetcode.com/problems/minimum-deletions-to-make-array-sharp/

**Difficulty:** Easy | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . 
 
 You may delete any number of elements from nums . The remaining elements keep their original order. 
 
 The resulting array a is sharp if the bitwise XOR of every pair of adjacent elements is non-zero . That is, a[i] XOR a[i + 1] != 0 for every index i such that 0 <= i < a.length - 1 . An array with at most one element is sharp. 
 
 Return the minimum number of deletions needed to make nums sharp. 
 
 Bitwise XOR compares the corresponding bits of two integers. A bit in the result is 1 if the corresponding bits differ, and 0 otherwise. 

 Example 1: 

 Input: nums = [1,1,2,2,2,3] 
 
 Output: 3 
 
 Explanation: 

 The pairs at indices (0, 1) , (2, 3) , and (3, 4) each have an XOR of 0. 
 
 Deleting one 1 and two 2s leaves [1, 2, 3] , where 1 XOR 2 == 3 and 2 XOR 3 == 1 are both non-zero. Therefore, the answer is 3. 

 Example 2: 

 Input: nums = [4,4,9,4] 
 
 Output: 1 
 
 Explanation: 

 The pair at indices (0, 1) has an XOR of 0. 
 
 Deleting either of these two 4s leaves [4, 9, 4] , where 4 XOR 9 == 13 and 9 XOR 4 == 13 are both non-zero. 

 Constraints: 

 2 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    public: int minDeletions(vector<int>& a) {
        int ans=0;
        for(int i=1; i<(int)a.size(); i++)ans+=a[i]==a[i-1];
        return ans;
    }
}
;
```


## 4084. Last Visited Cell in a Directional Grid

**Problem:** https://leetcode.com/problems/last-visited-cell-in-a-directional-grid/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an m x n matrix grid where each cell contains one of the following characters: 

 'L' : move one cell left. 
 
 'R' : move one cell right. 
 
 'U' : move one cell up. 
 
 'D' : move one cell down. 

 You start at cell (0, 0) , which is considered visited. At each step, move to the cell indicated by the character in your current cell. 
 
 The process ends if the indicated move would either leave the grid or enter a cell that has already been visited. In either case, the move is not made. 
 
 Return an integer array [r, c] representing the row and column indices of the last visited cell . The indices are 0-based . 

 Example 1: 

 Input: grid = [["R","D"],["U","L"]] 
 
 Output: [1,0] 
 
 Explanation: 

 Start at cell (0, 0) , which contains 'R' , so move right to (0, 1) . 
 
 At cell (0, 1) , the character is 'D' , so move down to (1, 1) . 
 
 At cell (1, 1) , the character is 'L' , so move left to (1, 0) . 
 
 At cell (1, 0) , the character is 'U' , which indicates moving to (0, 0) . However, (0, 0) has already been visited, so this move is not made. 
 
 Therefore, the process ends at the last visited cell (1, 0) , so the answer is [1, 0] . 

 Example 2: 

 Input: grid = [["R","R","R"]] 
 
 Output: [0,2] 
 
 Explanation: 

 Start at cell (0, 0) , which contains 'R' , so move right to (0, 1) . 
 
 At cell (0, 1) , the character is 'R' , so move right to (0, 2) . 
 
 At cell (0, 2) , the character is 'R' , which indicates moving to (0, 3) . However, (0, 3) is outside the grid, so this move is not made. 
 
 Therefore, the process ends at the last visited cell (0, 2) , so the answer is [0, 2] . 

 Constraints: 

 1 <= m == grid.length <= 10 5 
 
 1 <= n == grid[i].length <= 10 5 
 
 m * n <= 10 5 
 
 grid[i][j] is one of 'L' , 'R' , 'U' , or 'D' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> lastVisitedCell(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> seen(m, vector<bool>(n, false));
        int r = 0, c = 0;
        while (true) {
            seen[r][c] = true;
            int nr = r, nc = c;
            if (grid[r][c] == 'L') --nc;
            else if (grid[r][c] == 'R') ++nc;
            else if (grid[r][c] == 'U') --nr;
            else ++nr;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || seen[nr][nc]) break;
            r = nr;
            c = nc;
        }
        return {r, c};
    }
};
```


## 4085. Find Root of a Colored Tree

**Problem:** https://leetcode.com/problems/find-root-of-a-colored-tree/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an undirected tree of n nodes labeled from 0 to n - 1 , represented by a 2D integer array edges of length n - 1 , where edges[i] = [u i , v i ] indicates that there is an undirected edge between nodes u i and v i . 
 
 You are also given a string colors of length n , where colors[i] is one of 'R' , 'B' , or 'W' , and denotes the color of node i . 
 
 A node chosen as root must satisfy both of the following conditions once the tree is oriented away from it: 

 Binary-tree property: Every node has at most two children. 
 
 Layered color pattern: All nodes at the same depth have the same color. Starting at depth 0, these colors follow one of the three repeating sequences:

 R → B → W → R → B → W → ... 
 
 B → W → R → B → W → R → ... 
 
 W → R → B → W → R → B → ... 

 Return the index of any root that satisfies both conditions, or -1 if no such root exists. 
 
 A tree is a connected undirected graph with no cycles. 
 
 The depth of a node is the number of edges on the path from the root to that node. The root has depth 0. A child of a node is an adjacent node whose depth is one greater. 
 
 The degree of a node is the number of edges incident to it. 

 Example 1: 

 Input: edges = [[3,1],[3,2],[1,4],[2,0]], colors = "BRRWB" 
 
 Output: 3 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2025/06/15/treee.jpg] 
 
 Rooting at node 3 gives each node at most two children and every edge advances to the next color in the cycle ( W → R → B ), so return 3. 

 Example 2: 

 Input: edges = [[0,1],[1,2],[2,3]], colors = "RBRB" 
 
 Output: -1 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2025/06/15/treee2.jpg] 
 
 No root satisfies the required color step on every edge, so return -1. 

 Constraints: 

 2 <= n <= 10 5 
 
 edges.length == n - 1 
 
 edges[i] = [u i , v i ] 
 
 0 <= u i , v i < n 
 
 colors.length == n 
 
 colors[i] is one of 'R' , 'B' , 'W' . 
 
 The input graph is a tree and every node has degree at most three.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int findColoredRoot(vector<vector<int>>& edges, string colors) {
        int n = colors.size();
        vector<int> degree(n, 0), indegree(n, 0);
        auto id = [](char c) { return c == 'R' ? 0 : (c == 'B' ? 1 : 2); };
        for (const auto& e : edges) {
            int u = e[0], v = e[1];
            ++degree[u]; ++degree[v];
            int a = id(colors[u]), b = id(colors[v]);
            if ((a + 1) % 3 == b) ++indegree[v];
            else if ((b + 1) % 3 == a) ++indegree[u];
            else return -1;
        }
        int root = -1;
        for (int i = 0; i < n; ++i) {
            if (indegree[i] == 0) {
                if (root != -1 || degree[i] > 2) return -1;
                root = i;
            } else if (indegree[i] != 1) return -1;
        }
        return root;
    }
};
```


## 4086. Minimum Interval Selection to Cover Target Intervals

**Problem:** https://leetcode.com/problems/minimum-interval-selection-to-cover-target-intervals/

**Difficulty:** Hard | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two 2D integer arrays, availableIntervals and targetIntervals , each representing a list of closed intervals . 
 
 Select a subset of intervals from availableIntervals so that every real point contained in any interval in targetIntervals belongs to at least one selected interval. 
 
 Points outside the target intervals do not need to be covered. Selected intervals may overlap or extend beyond the target intervals. 
 
 Return the minimum number of intervals you need to select. If it is impossible to cover all the target intervals, return -1. 

 Example 1: 

 Input: availableIntervals = [[1,4],[1,7],[3,9],[5,10],[10,15]], targetIntervals = [[1,3],[2,5],[7,8],[10,13],[11,15],[12,13]] 
 
 Output: 3 
 
 Explanation: 
 
 The target intervals cover the ranges [1, 5] , [7, 8] , and [10, 15] . By selecting [1, 4] , [3, 9] , and [10, 15] from availableIntervals , all target intervals can be fully covered with three intervals. 

 Example 2: 

 Input: availableIntervals = [[4,6],[1,4],[2,5]], targetIntervals = [[3,4],[2,5],[6,7]] 
 
 Output: -1 
 
 Explanation: 
 
 It is impossible to select intervals from availableIntervals to cover all the intervals in targetIntervals . 

 Example 3: 

 Input: availableIntervals = [[1,2],[3,4]], targetIntervals = [[1,4]] 
 
 Output: -1 
 
 Explanation: 
 
 Selecting both available intervals leaves every real point strictly between 2 and 3 uncovered. For example, 2.5 belongs to the target interval but to neither available interval. 

 Constraints: 

 1 <= availableIntervals.length, targetIntervals.length <= 5 * 10 4 
 
 availableIntervals[i].length == targetIntervals[j].length == 2 
 
 1 <= availableIntervals[i][0] <= availableIntervals[i][1] <= 10 5 
 
 1 <= targetIntervals[j][0] <= targetIntervals[j][1] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

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


## 4087. Maximum Subarray Sum of Fixed Length After at Most K Swaps

**Problem:** https://leetcode.com/problems/maximum-subarray-sum-of-fixed-length-after-at-most-k-swaps/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and two integers length and k . 
 
 You may perform at most k swap operations on nums . 
 
 In one swap operation, you may choose two distinct indices i and j and swap nums[i] and nums[j] . 
 
 Return the maximum possible sum of a subarray of length exactly length after performing the swaps. 

 Example 1: 

 Input: nums = [1,-1,0,2], length = 2, k = 1 
 
 Output: 3 
 
 Explanation: 

 Swap the elements at indices 1 and 3, resulting in [1, 2, 0, -1] . 
 
 The subarray [1, 2] has length 2 and sum 3. 
 
 No subarray of length 2 can have a larger sum, since 1 and 2 are the two largest elements. 

 Example 2: 

 Input: nums = [4,3,2,4], length = 3, k = 2 
 
 Output: 11 
 
 Explanation: 

 Swap the elements at indices 2 and 3, resulting in [4, 3, 4, 2] . 
 
 The subarray [4, 3, 4] has length 3 and sum 11. 
 
 This is the sum of the three largest elements, so no larger answer is possible. Only one swap is needed. 

 Example 3: 

 Input: nums = [-1,-2], length = 2, k = 0 
 
 Output: -3 
 
 Explanation: 
 
 No swaps are allowed. The only subarray of length 2 is [-1, -2] , whose sum is -3. 

 Constraints: 

 1 <= nums.length <= 300 
 
 -10 9 <= nums[i] <= 10 9 
 
 1 <= length <= nums.length 
 
 0 <= k <= nums.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:long long maxSum(vector<int>& a,int length,int k){int n=a.size();long long ans=LLONG_MIN;for(int l=0;l+length<=n;++l){vector<int> in,out;long long sum=0;for(int i=0;i<n;++i)if(i>=l&&i<l+length){in.push_back(a[i]);sum+=a[i];}else out.push_back(a[i]);sort(in.begin(),in.end());sort(out.rbegin(),out.rend());for(int j=0;j<k&&j<(int)in.size()&&j<(int)out.size()&&out[j]>in[j];++j)sum+=(long long)out[j]-in[j];ans=max(ans,sum);}return ans;}};
```


## 4088. Difference Between Peaks and Valleys

**Problem:** https://leetcode.com/problems/difference-between-peaks-and-valleys/

**Difficulty:** Easy | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of length n . 
 
 An index i is called a peak if all of the following conditions hold: 

 0 < i < n - 1 
 
 nums[i] > nums[i - 1] 
 
 nums[i] > nums[i + 1] 

 An index i is called a valley if all of the following conditions hold: 

 0 < i < n - 1 
 
 nums[i] < nums[i - 1] 
 
 nums[i] < nums[i + 1] 

 Return an integer denoting the difference between the sum of all peak values and the sum of all valley values. 

 Example 1: 

 Input: nums = [1,5,2,4,1,3,0] 
 
 Output: 9 
 
 Explanation: 

 The peak values are nums[1] = 5 , nums[3] = 4 , and nums[5] = 3 . 
 
 The valley values are nums[2] = 2 and nums[4] = 1 . 
 
 The difference between the sum of the peak values and the sum of the valley values is (5 + 4 + 3) - (2 + 1) = 9 . Hence, the answer is 9. 

 Example 2: 

 Input: nums = [-5,-6,-1,-2,5,3,2] 
 
 Output: 12 
 
 Explanation: 

 The peak values are nums[2] = -1 and nums[4] = 5 . 
 
 The valley values are nums[1] = -6 and nums[3] = -2 . 
 
 The difference between the sum of the peak values and the sum of the valley values is (-1 + 5) - (-6 + (-2)) = 12 . Hence, the answer is 12. 

 Example 3: 

 Input: nums = [6,5,2,5,5,3,6] 
 
 Output: -5 
 
 Explanation: 

 There are no peak values in the array. 
 
 The valley values are nums[2] = 2 and nums[5] = 3 . 
 
 The difference between the sum of the peak values and the sum of the valley values is (0) - (2 + 3) = -5 . Hence, the answer is -5. 

 Constraints: 

 3 <= n == nums.length <= 100 
 
 -100 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

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


## 4089. Count Subarrays With Loose Bounds

**Problem:** https://leetcode.com/problems/count-subarrays-with-loose-bounds/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and two integers minK and maxK . 
 
 A loose-bound subarray is a subarray in which every element is greater than or equal to minK and less than or equal to maxK . 
 
 Return the number of loose-bound subarrays in nums . 
 
 A subarray is a contiguous non-empty sequence of elements within an array. 

 Example 1: 

 Input: nums = [1,4,7,3], minK = 1, maxK = 5 
 
 Output: 4 
 
 Explanation: 
 
 The loose-bound subarrays are [1] , [4] , [3] , and [1, 4] . The minimum value in these subarrays is at least minK = 1 and the maximum value is at most maxK = 5 . 

 Example 2: 

 Input: nums = [1,1], minK = 1, maxK = 1 
 
 Output: 3 
 
 Explanation: 
 
 The loose-bound subarrays are [1] , [1] , and [1, 1] . The minimum value in these subarrays is at least minK = 1 and the maximum value is at most maxK = 1 . 

 Constraints: 

 2 <= nums.length <= 10 5 
 
 1 <= nums[i], minK, maxK <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

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


## 4090. Count Magical Substring Pairs I

**Problem:** https://leetcode.com/problems/count-magical-substring-pairs-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string s of length n consisting of lowercase English letters. 
 
 For every triplet of indices (i, j, k) satisfying 0 <= i <= j < k < n , define: 

 s1 = s[i..j] 
 
 s2 = s[j + 1..k] 

 A pair of substrings (s1, s2) is called magical if the number of distinct characters in s1 is equal to the number of distinct characters in s2 . 
 
 Return the number of triplets (i, j, k) for which (s1, s2) is a magical pair. 
 
 A substring is a contiguous non-empty sequence of characters within a string. 

 Example 1: 

 Input: s = "aba" 
 
 Output: 2 
 
 Explanation: 
 
 There are 2 valid triplets: 

 No. 
 (i, j, k) 
 s1 
 s2 
 distinct(s1) 
 distinct(s2) 

 1 
 (0, 0, 1) 
 "a" 
 "b" 
 1 
 1 

 2 
 (1, 1, 2) 
 "b" 
 "a" 
 1 
 1 

 Example 2: 

 Input: s = "kkk" 
 
 Output: 4 
 
 Explanation: 
 
 There are 4 valid triplets: 

 No. 
 (i, j, k) 
 s1 
 s2 
 distinct(s1) 
 distinct(s2) 

 1 
 (0, 0, 1) 
 "k" 
 "k" 
 1 
 1 

 2 
 (0, 0, 2) 
 "k" 
 "kk" 
 1 
 1 

 3 
 (0, 1, 2) 
 "kk" 
 "k" 
 1 
 1 

 4 
 (1, 1, 2) 
 "k" 
 "k" 
 1 
 1 

 Example 3: 

 Input: s = "abcac" 
 
 Output: 7 
 
 Explanation: 
 
 There are 7 valid triplets: 

 No. 
 (i, j, k) 
 s1 
 s2 
 distinct(s1) 
 distinct(s2) 

 1 
 (0, 0, 1) 
 "a" 
 "b" 
 1 
 1 

 2 
 (1, 1, 2) 
 "b" 
 "c" 
 1 
 1 

 3 
 (2, 2, 3) 
 "c" 
 "a" 
 1 
 1 

 4 
 (3, 3, 4) 
 "a" 
 "c" 
 1 
 1 

 5 
 (0, 1, 3) 
 "ab" 
 "ca" 
 2 
 2 

 6 
 (0, 1, 4) 
 "ab" 
 "cac" 
 2 
 2 

 7 
 (1, 2, 4) 
 "bc" 
 "ac" 
 2 
 2 

 Constraints: 

 2 <= s.length <= 2000 
 
 s consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

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


## 4091. Count Magical Substring Pairs II

**Problem:** https://leetcode.com/problems/count-magical-substring-pairs-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string s of length n consisting of lowercase English letters. 
 
 For every triplet of indices (i, j, k) satisfying 0 <= i <= j < k < n , define: 

 s1 = s[i..j] 
 
 s2 = s[j + 1..k] 

 A pair of substrings (s1, s2) is called magical if the number of distinct characters in s1 is equal to the number of distinct characters in s2 . 
 
 Return the number of triplets (i, j, k) for which (s1, s2) is a magical pair. 
 
 A substring is a contiguous non-empty sequence of characters within a string. 

 Example 1: 

 Input: s = "aba" 
 
 Output: 2 
 
 Explanation: 
 
 There are 2 valid triplets: 

 No. 
 (i, j, k) 
 s1 
 s2 
 distinct(s1) 
 distinct(s2) 

 1 
 (0, 0, 1) 
 "a" 
 "b" 
 1 
 1 

 2 
 (1, 1, 2) 
 "b" 
 "a" 
 1 
 1 

 Example 2: 

 Input: s = "kkk" 
 
 Output: 4 
 
 Explanation: 
 
 There are 4 valid triplets: 

 No. 
 (i, j, k) 
 s1 
 s2 
 distinct(s1) 
 distinct(s2) 

 1 
 (0, 0, 1) 
 "k" 
 "k" 
 1 
 1 

 2 
 (0, 0, 2) 
 "k" 
 "kk" 
 1 
 1 

 3 
 (0, 1, 2) 
 "kk" 
 "k" 
 1 
 1 

 4 
 (1, 1, 2) 
 "k" 
 "k" 
 1 
 1 

 Example 3: 

 Input: s = "abcac" 
 
 Output: 7 
 
 Explanation: 
 
 There are 7 valid triplets: 

 No. 
 (i, j, k) 
 s1 
 s2 
 distinct(s1) 
 distinct(s2) 

 1 
 (0, 0, 1) 
 "a" 
 "b" 
 1 
 1 

 2 
 (1, 1, 2) 
 "b" 
 "c" 
 1 
 1 

 3 
 (2, 2, 3) 
 "c" 
 "a" 
 1 
 1 

 4 
 (3, 3, 4) 
 "a" 
 "c" 
 1 
 1 

 5 
 (0, 1, 3) 
 "ab" 
 "ca" 
 2 
 2 

 6 
 (0, 1, 4) 
 "ab" 
 "cac" 
 2 
 2 

 7 
 (1, 2, 4) 
 "bc" 
 "ac" 
 2 
 2 

 Constraints: 

 2 <= s.length <= 10 5 
 
 s consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

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


## 4092. Binary Digit Score

**Problem:** https://leetcode.com/problems/binary-digit-score/

**Difficulty:** Easy | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Not inferred

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two integers a and b . 
 
 Let s1 and s2 be the number of set bits in the binary representations of a and b , respectively. 
 
 The score of these integers is defined as follows: 

 If s1 >= s2 , the score is s1 * s2 . 
 
 Otherwise, the score is s2 / s1 using integer division. 

 Return an integer representing the score of a and b . 
 
 A set bit refers to a bit in the binary representation of a number that has a value of 1. 

 Example 1: 

 Input: a = 14, b = 6 
 
 Output: 6 
 
 Explanation: 

 The binary representation of a = 14 is "1110" , so s1 = 3 . 
 
 The binary representation of b = 6 is "110" , so s2 = 2 . 
 
 Since s1 > s2 , the score of a and b is s1 * s2 = 3 * 2 = 6 . 

 Example 2: 

 Input: a = 5, b = 15 
 
 Output: 2 
 
 Explanation: 

 The binary representation of a = 5 is "101" , so s1 = 2 . 
 
 The binary representation of b = 15 is "1111" , so s2 = 4 . 
 
 Since s1 < s2 , the score of a and b is s2 / s1 = 4 / 2 = 2 . 

 Example 3: 

 Input: a = 10, b = 12 
 
 Output: 4 
 
 Explanation: 

 The binary representation of a = 10 is "1010" , so s1 = 2 . 
 
 The binary representation of b = 12 is "1100" , so s2 = 2 . 
 
 Since s1 == s2 , the score of a and b is s1 * s2 = 2 * 2 = 4 . 

 Constraints: 

 1 <= a, b <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    int bits(int x) {
        int cnt = 0;
        while (x) {
            x &= x - 1;
            ++cnt;
        }
        return cnt;
    }
public:
    int calculateScore(int a, int b) {
        int x = bits(a), y = bits(b);
        return x >= y ? x * y : y / x;
    }
};
```


## 4093. Maximize Sum After At Most K Digit Rearrangements

**Problem:** https://leetcode.com/problems/maximize-sum-after-at-most-k-digit-rearrangements/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of length n and an integer k . 
 
 In one operation, you may choose any element of nums and rearrange its decimal digits in any order to form a new integer. 
 
 Return the maximum possible sum of the array after performing at most k operations. 

 Example 1: 

 Input: nums = [123,45], k = 1 
 
 Output: 366 
 
 Explanation: 

 We choose nums[0] = 123 and rearrange its digits to form 321. 
 
 The array becomes [321, 45] . Thus, the total sum is 321 + 45 = 366 . 

 Example 2: 

 Input: nums = [102,90,14], k = 2 
 
 Output: 341 
 
 Explanation: 

 We choose nums[0] = 102 and rearrange its digits to form 210. 
 
 We choose nums[2] = 14 and rearrange its digits to form 41. 
 
 The array becomes [210, 90, 41] . Thus, the total sum is 210 + 90 + 41 = 341 . 

 Constraints: 

 1 <= n == nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9 
 
 1 <= k <= n

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    long long maximizeSum(vector<int>& nums, int k) {
        vector<int> bremovilta = nums;
        vector<long long> gains;
        long long sum = 0;
        for (int x : bremovilta) {
            sum += x;
            string s = to_string(x);
            sort(s.rbegin(), s.rend());
            long long best = stoll(s);
            gains.push_back(best - x);
        }
        sort(gains.rbegin(), gains.rend());
        for (int i = 0; i < k; ++i) sum += gains[i];
        return sum;
    }
};
```


## 4094. Count Frequency Staircase Subarrays I

**Problem:** https://leetcode.com/problems/count-frequency-staircase-subarrays-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . 
 
 Consider the distinct values of a subarray in the order in which they first appear. 
 
 If there are k distinct values, the subarray is called a frequency staircase if the first distinct value occurs exactly once , the second distinct value occurs exactly twice , and so on, with the k th distinct value occurring exactly k times. 
 
 Equivalently, the frequencies of the distinct values, in the order of their first occurrence, must be exactly 1, 2, 3, ..., k . 
 
 Return the number of frequency staircase subarrays in nums . 
 
 A subarray is a contiguous non-empty sequence of elements within an array. 
 
 The frequency of a value in a subarray is the number of times it occurs in that subarray. 

 Example 1: 

 Input: nums = [5,8,8,2,2,2] 
 
 Output: 9 
 
 Explanation: 
 
 Every single-element subarray has frequencies [1] , and there are 6 of them. 3 longer subarrays also qualify: 

 Subarray 
 Values by first appearance 
 Frequencies 

 nums[0...2] = [5, 8, 8] 
 5, then 8 
 [1, 2] 

 nums[2...4] = [8, 2, 2] 
 8, then 2 
 [1, 2] 

 nums[0...5] = [5, 8, 8, 2, 2, 2] 
 5, then 8, then 2 
 [1, 2, 3] 

 So the answer is 6 + 3 = 9 . 

 Example 2: 

 Input: nums = [6,6,9,9] 
 
 Output: 5 
 
 Explanation: 
 
 Every single-element subarray has frequencies [1] , and there are 4 of them. 1 longer subarray also qualifies: 

 Subarray 
 Values by first appearance 
 Frequencies 

 nums[1...3] = [6, 9, 9] 
 6, then 9 
 [1, 2] 

 So the answer is 4 + 1 = 5 . 

 Example 3: 

 Input: nums = [2,3,4,4,3,4] 
 
 Output: 8 
 
 Explanation: 
 
 Every single-element subarray has frequencies [1] , and there are 6 of them. 2 longer subarrays also qualify: 

 Subarray 
 Values by first appearance 
 Frequencies 

 nums[1...3] = [3, 4, 4] 
 3, then 4 
 [1, 2] 

 nums[0...5] = [2, 3, 4, 4, 3, 4] 
 2, then 3, then 4 
 [1, 2, 3] 

 So the answer is 6 + 2 = 8 . 

 Constraints: 

 1 <= nums.length <= 1500 
 
 1 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int countStaircase(vector<int>& nums) {
        vector<int> qalverinos = nums;
        int n = qalverinos.size(), ans = 0;
        vector<int> seen(100001, -1), freq(100001, 0), rank(100001, 0);
        for (int l = 0; l < n; ++l) {
            int distinct = 0, good = 0;
            for (int r = l; r < n; ++r) {
                int x = qalverinos[r];
                if (seen[x] != l) {
                    seen[x] = l;
                    freq[x] = 0;
                    rank[x] = ++distinct;
                }
                if (freq[x] == rank[x]) --good;
                ++freq[x];
                if (freq[x] == rank[x]) ++good;
                if (good == distinct) ++ans;
            }
        }
        return ans;
    }
};
```


## 4095. Count Frequency Staircase Subarrays II

**Problem:** https://leetcode.com/problems/count-frequency-staircase-subarrays-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . 
 
 Consider the distinct values of a subarray in the order in which they first appear. 
 
 If there are k distinct values, the subarray is called a frequency staircase if the first distinct value occurs exactly once , the second distinct value occurs exactly twice , and so on, with the k th distinct value occurring exactly k times. 
 
 Equivalently, the frequencies of the distinct values, in the order of their first occurrence, must be exactly 1, 2, 3, ..., k . 
 
 Return the number of frequency staircase subarrays in nums . 
 
 A subarray is a contiguous non-empty sequence of elements within an array. 
 
 The frequency of a value in a subarray is the number of times it occurs in that subarray. 

 Example 1: 

 Input: nums = [5,8,8,2,2,2] 
 
 Output: 9 
 
 Explanation: 
 
 Every single-element subarray has frequencies [1] , and there are 6 of them. 3 longer subarrays also qualify: 

 Subarray 
 Values by first appearance 
 Frequencies 

 nums[0...2] = [5, 8, 8] 
 5, then 8 
 [1, 2] 

 nums[2...4] = [8, 2, 2] 
 8, then 2 
 [1, 2] 

 nums[0...5] = [5, 8, 8, 2, 2, 2] 
 5, then 8, then 2 
 [1, 2, 3] 

 So the answer is 6 + 3 = 9 . 

 Example 2: 

 Input: nums = [6,6,9,9] 
 
 Output: 5 
 
 Explanation: 
 
 Every single-element subarray has frequencies [1] , and there are 4 of them. 1 longer subarray also qualifies: 

 Subarray 
 Values by first appearance 
 Frequencies 

 nums[1...3] = [6, 9, 9] 
 6, then 9 
 [1, 2] 

 So the answer is 4 + 1 = 5 . 

 Example 3: 

 Input: nums = [2,3,4,4,3,4] 
 
 Output: 8 
 
 Explanation: 
 
 Every single-element subarray has frequencies [1] , and there are 6 of them. 2 longer subarrays also qualify: 

 Subarray 
 Values by first appearance 
 Frequencies 

 nums[1...3] = [3, 4, 4] 
 3, then 4 
 [1, 2] 

 nums[0...5] = [2, 3, 4, 4, 3, 4] 
 2, then 3, then 4 
 [1, 2, 3] 

 So the answer is 6 + 2 = 8 . 

 Constraints: 

 1 <= nums.length <= 5 * 10 4 
 
 1 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp

class Solution {
public:
    int countStaircase(vector<int>& nums) {
        int n = nums.size();
        const int MAXV = 100000;

        vector<int> global(MAXV + 1, 0);
        vector<int> counts;

        for (int x : nums)
            ++global[x];

        for (int f : global) {
            if (f > 0)
                counts.push_back(f);
        }

        sort(counts.rbegin(), counts.rend());

        // Maximum globally feasible staircase size.
        int K = 0;

        for (int k = 1;
             k <= (int)counts.size() &&
             1LL * k * (k + 1) / 2 <= n;
             ++k) {

            bool possible = true;

            for (int j = 0; j < k; ++j) {
                if (counts[j] < k - j) {
                    possible = false;
                    break;
                }
            }

            if (!possible)
                break;

            K = k;
        }

        // Every single-element subarray is valid.
        int answer = n;

        if (K < 2)
            return answer;

        int maxLen = K * (K + 1) / 2;

        vector<int> freq(MAXV + 1, 0);
        vector<int> rank(MAXV + 1, 0);
        vector<int> stamp(MAXV + 1, 0);

        int generation = 0;

        for (int left = 0; left < n; ++left) {
            ++generation;

            int distinct = 0;
            int bad = 0;

            int bound = min(n, left + maxLen);

            for (int right = left; right < bound; ++right) {
                int x = nums[right];

                if (stamp[x] != generation) {
                    stamp[x] = generation;
                    freq[x] = 0;
                    rank[x] = ++distinct;

                    if (distinct > K)
                        break;
                }

                int target = rank[x];
                int oldFreq = freq[x];

                ++freq[x];

                if (oldFreq == 0) {
                    if (target > 1)
                        ++bad;
                } else if (oldFreq == target - 1) {
                    --bad;
                } else if (oldFreq == target) {
                    ++bad;
                }

                // Frequency cannot decrease as we extend
                // the current subarray.
                if (freq[x] > target)
                    break;

                int len = right - left + 1;

                if (distinct >= 2 &&
                    len == distinct * (distinct + 1) / 2 &&
                    bad == 0) {
                    ++answer;
                }
            }
        }

        return answer;
    }
};
```


## 4096. Simulate Bomb Explosions and Falling Boxes

**Problem:** https://leetcode.com/problems/simulate-bomb-explosions-and-falling-boxes/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Not available

**Primary pattern:** Other / Unclassified

**Related patterns:** None

**Data structures (inferred):** Vector

**Pattern recognition:** Inspect constraints and derive an invariant.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 2D character array grid of size m x n , where each cell contains one of the following symbols: 

 '#' : a box. 
 
 '-' : an empty cell. 
 
 '*' : a bomb. 

 Each second, the following events occur in order : 

 Explosions: A bomb explodes if it is orthogonally adjacent to at least one box (shares a side with it). An exploding bomb destroys all boxes in its 8 neighboring cells , including diagonally adjacent cells, turning them into empty cells. All explosions happen simultaneously , based on the grid at the beginning of that second. Empty cells and bombs remain unchanged. 
 
 Gravity: After the explosions, all non-static boxes simultaneously fall down by exactly one row. A box is static if it is in the bottommost row, immediately above a bomb, or immediately above another static box. 

 Bombs never move or disappear, and the same bomb may explode multiple times. Boxes above non-static boxes can fall together with them. 
 
 Return the final grid after 10 100 seconds. 

 Example 1: 

 Input: grid = [["#","#","#"],["-","-","*"],["-","-","-"]] 
 
 Output: [["-","-","-"],["-","-","*"],["#","-","-"]] 
 
 Explanation: 
 
 Let (r, c) represent the cell in the r th row from the top and c th column from the left. For example, (0, 0) denotes the top-left most cell. 
 
 The 1 st second: 

 Since the bomb at (1, 2) is orthogonally adjacent to the box at (0, 2) , the boxes at (0, 1) and (0, 2) become empty cells. 
 
 The box at (0, 0) falls to (1, 0) . 

 The 2 nd second: 

 The bomb at (1, 2) is not orthogonally adjacent to any box. Therefore, nothing happens. 
 
 The box at (1, 0) falls to (2, 0) . 

 Nothing happens afterwards. 

 Example 2: 

 Input: grid = [["-","*"],["#","-"]] 
 
 Output: [["-","*"],["#","-"]] 
 
 Explanation: 
Nothing happens because the bomb is not orthogonally adjacent to any box. 
 
 Example 3: 

 Input: grid = [["-","*","#"],["#","-","-"]] 
 
 Output: [["-","*","-"],["-","-","-"]] 
 
 Explanation: 
 
 The 1 st second: 

 The bomb at (0, 1) is orthogonally adjacent to the box at (0, 2) . Therefore, the boxes at (0, 2) and (1, 0) become empty cells. 

 Nothing happens afterwards. 

 Example 4: 

 Input: grid = [["#","*","-","#"],["-","-","*","-"]] 
 
 Output: [["-","*","-","-"],["-","-","*","-"]] 
 
 Explanation: 
 
 The 1 st second: 

 Since the bomb at (0, 1) is orthogonally adjacent to the box at (0, 0) , the box at (0, 0) becomes an empty cell. The other bomb at (1, 2) is not orthogonally adjacent to any box. 
 
 The box at (0, 3) falls to (1, 3) . 

 The 2 nd second: 

 Since the bomb at (1, 2) is orthogonally adjacent to the box at (1, 3) , the box at (1, 3) becomes an empty cell. The other bomb at (0, 1) is not orthogonally adjacent to any box. 

 Nothing happens afterwards. 

 1 <= m == grid.length <= 100 
 
 1 <= n == grid[i].length <= 100 
 
 grid[i][j] is '#' , '-' , or '*' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp

class Solution {
public:
    vector<vector<char>> finalGrid(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        for (int step = 0; step < m; ++step) {

            // Step 1: Find bombs that explode.
            vector<vector<bool>> destroy(m, vector<bool>(n, false));

            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (grid[i][j] != '*')
                        continue;

                    bool explode = false;

                    const int dr[4] = {-1, 1, 0, 0};
                    const int dc[4] = {0, 0, -1, 1};

                    for (int d = 0; d < 4; ++d) {
                        int x = i + dr[d];
                        int y = j + dc[d];

                        if (x >= 0 && x < m &&
                            y >= 0 && y < n &&
                            grid[x][y] == '#') {
                            explode = true;
                            break;
                        }
                    }

                    if (!explode)
                        continue;

                    // Destroy boxes in all 8 neighboring cells.
                    for (int dx = -1; dx <= 1; ++dx) {
                        for (int dy = -1; dy <= 1; ++dy) {
                            int x = i + dx;
                            int y = j + dy;

                            if (x >= 0 && x < m &&
                                y >= 0 && y < n &&
                                grid[x][y] == '#') {
                                destroy[x][y] = true;
                            }
                        }
                    }
                }
            }

            bool changed = false;

            // Apply all explosions simultaneously.
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (destroy[i][j]) {
                        grid[i][j] = '-';
                        changed = true;
                    }
                }
            }

            // Step 2: Apply gravity.
            // Bottom-up ensures boxes fall only one row.
            for (int j = 0; j < n; ++j) {
                for (int i = m - 2; i >= 0; --i) {
                    if (grid[i][j] == '#' &&
                        grid[i + 1][j] == '-') {

                        swap(grid[i][j], grid[i + 1][j]);
                        changed = true;
                    }
                }
            }

            if (!changed)
                break;
        }

        return grid;
    }
};
```

