# JavaScript

## 2618. Check if Object Instance of Class

**Problem:** https://leetcode.com/problems/check-if-object-instance-of-class/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195484203  
**Language:** javascript

### Description

Write a function that checks if a given value is an instance of a given class or superclass. For this problem, an object is considered an instance of a given class if that object has access to that class's methods. 
 
 There are no constraints on the data types that can be passed to the function. For example, the value or the class could be  undefined . 
 
   
 
 Example 1: 
 
```text
Input:
 func = () => checkIfInstanceOf(new Date(), Date)

Output:
 true

Explanation: 
The object returned by the Date constructor is, by definition, an instance of Date.
```
 
 
 Example 2: 
 
```text
Input:
 func = () => { class Animal {}; class Dog extends Animal {}; return checkIfInstanceOf(new Dog(), Animal); }

Output:
 true

Explanation:

class Animal {};
class Dog extends Animal {};
checkIfInstanceOf(new Dog(), Animal); // true

Dog is a subclass of Animal. Therefore, a Dog object is an instance of both Dog and Animal.
```
 
 
 Example 3: 
 
```text
Input:
 func = () => checkIfInstanceOf(Date, Date)

Output:
 false

Explanation: 
A date constructor cannot logically be an instance of itself.
```
 
 
 Example 4: 
 
```text
Input:
 func = () => checkIfInstanceOf(5, Number)

Output:
 true

Explanation: 
5 is a Number. Note that the "instanceof" keyword would return false. However, it is still considered an instance of Number because it accesses the Number methods. For example "toFixed()".
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var checkIfInstanceOf = function(obj, classFunction) {
  if (obj == null || typeof classFunction !== 'function') return false;
  return Object(classFunction.prototype).isPrototypeOf(Object(obj));
};
```

---

## 2619. Array Prototype Last

**Problem:** https://leetcode.com/problems/array-prototype-last/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195484382  
**Language:** javascript

### Description

Write code that enhances all arrays such that you can call the  array.last()  method on any array and it will return the last element. If there are no elements in the array, it should return  -1 . 
 
 You may assume the array is the output of  JSON.parse . 
 
   
 
 Example 1: 
 
```text
Input:
 nums = [null, {}, 3]

Output:
 3

Explanation:
 Calling nums.last() should return the last element: 3.
```
 
 
 Example 2: 
 
```text
Input:
 nums = []

Output:
 -1

Explanation:
 Because there are no elements, return -1.
```
 
 
   
 
 Constraints: 
 
 
 arr  is a valid JSON array 
 
 0 <= arr.length <= 1000

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
Array.prototype.last = function() {
  return this.length ? this[this.length - 1] : -1;
};
```

---

## 2620. Counter

**Problem:** https://leetcode.com/problems/counter/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195484530  
**Language:** javascript

### Description

Given an integer  n , return a  counter  function. This  counter  function initially returns  n  and then returns 1 more than the previous value every subsequent time it is called ( n ,  n + 1 ,  n + 2 , etc). 
 
   
 
 Example 1: 
 
```text
Input:
 
n = 10 
["call","call","call"]

Output:
 [10,11,12]

Explanation: 

counter() = 10 // The first time counter() is called, it returns n.
counter() = 11 // Returns 1 more than the previous time.
counter() = 12 // Returns 1 more than the previous time.
```
 
 
 Example 2: 
 
```text
Input:
 
n = -2
["call","call","call","call","call"]

Output:
 [-2,-1,0,1,2]

Explanation:
 counter() initially returns -2. Then increases after each sebsequent call.
```
 
 
   
 
 Constraints: 
 
 
 -1000   <= n <= 1000 
 
 0 <= calls.length <= 1000 
 
 calls[i] === "call"

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var createCounter = function(n) {
  return function() { return n++; };
};
```

---

## 2621. Sleep

**Problem:** https://leetcode.com/problems/sleep/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195484703  
**Language:** javascript

### Description

Given a positive integer  millis , write an asynchronous function that sleeps for  millis  milliseconds. It can resolve any value. 
 
 Note  that  minor  deviation from  millis  in the actual sleep duration is acceptable. 
 
   
 
 Example 1: 
 
```text
Input:
 millis = 100

Output:
 100

Explanation:
 It should return a promise that resolves after 100ms.
let t = Date.now();
sleep(100).then(() => {
  console.log(Date.now() - t); // 100
});
```
 
 
 Example 2: 
 
```text
Input:
 millis = 200

Output:
 200

Explanation:
 It should return a promise that resolves after 200ms.
```
 
 
   
 
 Constraints: 
 
 
 1 <= millis <= 1000

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
async function sleep(millis) {
  return new Promise(resolve => setTimeout(resolve, millis));
}
```

---

## 2622. Cache With Time Limit

**Problem:** https://leetcode.com/problems/cache-with-time-limit/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195484869  
**Language:** javascript

### Description

Write a class that allows getting and setting key-value pairs, however a  time until expiration  is associated with each key. 
 
 The class has three public methods: 
 
 set(key, value, duration) : accepts an integer  key , an integer  value , and a  duration  in milliseconds. Once the  duration  has elapsed, the key should be inaccessible. The method should return  true  if the same un-expired key already exists and  false  otherwise. Both the value and duration should be overwritten if the key already exists. 
 
 get(key) : if an un-expired key exists, it should return the associated value. Otherwise it should return  -1 . 
 
 count() : returns the count of un-expired keys. 
 
   
 
 Example 1: 
 
```text
Input:
 
actions = ["TimeLimitedCache", "set", "get", "count", "get"]
values = [[], [1, 42, 100], [1], [], [1]]
timeDelays = [0, 0, 50, 50, 150]

Output:
 [null, false, 42, 1, -1]

Explanation:

At t=0, the cache is constructed.
At t=0, a key-value pair (1: 42) is added with a time limit of 100ms. The value doesn't exist so false is returned.
At t=50, key=1 is requested and the value of 42 is returned.
At t=50, count() is called and there is one active key in the cache.
At t=100, key=1 expires.
At t=150, get(1) is called but -1 is returned because the cache is empty.
```
 
 
 Example 2: 
 
```text
Input:
 
actions = ["TimeLimitedCache", "set", "set", "get", "get", "get", "count"]
values = [[], [1, 42, 50], [1, 50, 100], [1], [1], [1], []]
timeDelays = [0, 0, 40, 50, 120, 200, 250]

Output:
 [null, false, true, 50, 50, -1, 0]

Explanation:

At t=0, the cache is constructed.
At t=0, a key-value pair (1: 42) is added with a time limit of 50ms. The value doesn't exist so false is returned.
At t=40, a key-value pair (1: 50) is added with a time limit of 100ms. A non-expired value already existed so true is returned and the old value was overwritten.
At t=50, get(1) is called which returned 50.
At t=120, get(1) is called which returned 50.
At t=140, key=1 expires.
At t=200, get(1) is called but the cache is empty so -1 is returned.
At t=250, count() returns 0 because the cache is empty.
```
 
 
   
 
 Constraints: 
 
 
 0 <= key, value <= 10 9 
 
 0 <= duration <= 1000 
 
 1 <= actions.length <= 100 
 
 actions.length === values.length 
 
 actions.length === timeDelays.length 
 
 0 <= timeDelays[i] <= 1450 
 
 actions[i]  is one of "TimeLimitedCache", "set", "get" and "count" 
 
 First action is always "TimeLimitedCache" and must be executed immediately, with a 0-millisecond delay

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var TimeLimitedCache = function() { this.map = new Map(); };
TimeLimitedCache.prototype.set = function(key,value,duration) {
  const old=this.map.get(key);
  if (old) clearTimeout(old.timer);
  const timer=setTimeout(()=>this.map.delete(key),duration);
  this.map.set(key,{value,timer});
  return old!==undefined;
};
TimeLimitedCache.prototype.get = function(key) {
  return this.map.has(key) ? this.map.get(key).value : -1;
};
TimeLimitedCache.prototype.count = function() { return this.map.size; };
```

---

## 2623. Memoize

**Problem:** https://leetcode.com/problems/memoize/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195485086  
**Language:** javascript

### Description

Given a function  fn , return a  memoized  version of that function. 
 
 A  memoized  function is a function that will never be called twice with the same inputs. Instead it will return a cached value. 
 
 You can assume there are  3  possible input functions:  sum ,  fib ,  and  factorial . 
 
 
 sum   accepts two integers  a  and  b  and returns  a + b . Assume that if a value has already been cached for the arguments  (b, a)  where  a != b , it cannot be used for the arguments  (a, b) . For example, if the arguments are  (3, 2)  and  (2, 3) , two separate calls should be made. 
 
 fib   accepts a single integer  n  and returns  1  if  n <= 1   or   fib(n - 1) + fib(n - 2)   otherwise. 
 
 factorial  accepts a single integer  n  and returns  1  if  n <= 1  or  factorial(n - 1) * n  otherwise. 
 
 
   
 
 Example 1: 
 
```text
Input:

fnName = "sum"
actions = ["call","call","getCallCount","call","getCallCount"]
values = [[2,2],[2,2],[],[1,2],[]]

Output:
 [4,4,1,3,2]

Explanation:

const sum = (a, b) => a + b;
const memoizedSum = memoize(sum);
memoizedSum(2, 2); // "call" - returns 4. sum() was called as (2, 2) was not seen before.
memoizedSum(2, 2); // "call" - returns 4. However sum() was not called because the same inputs were seen before.
// "getCallCount" - total call count: 1
memoizedSum(1, 2); // "call" - returns 3. sum() was called as (1, 2) was not seen before.
// "getCallCount" - total call count: 2
```
 
 
 Example 2: 
 
```text
Input:

fnName = "factorial"
actions = ["call","call","call","getCallCount","call","getCallCount"]
values = [[2],[3],[2],[],[3],[]]

Output:
 [2,6,2,2,6,2]

Explanation:

const factorial = (n) => (n <= 1) ? 1 : (n * factorial(n - 1));
const memoFactorial = memoize(factorial);
memoFactorial(2); // "call" - returns 2.
memoFactorial(3); // "call" - returns 6.
memoFactorial(2); // "call" - returns 2. However factorial was not called because 2 was seen before.
// "getCallCount" - total call count: 2
memoFactorial(3); // "call" - returns 6. However factorial was not called because 3 was seen before.
// "getCallCount" - total call count: 2
```
 
 
 Example 3: 
 
```text
Input:

fnName = "fib"
actions = ["call","getCallCount"]
values = [[5],[]]

Output:
 [8,1]

Explanation:

fib(5) = 8 // "call"
// "getCallCount" - total call count: 1
```
 
 
   
 
 Constraints: 
 
 
 0 <= a, b <= 10 5 
 
 1 <= n <= 10 
 
 1 <= actions.length <= 10 5 
 
 actions.length === values.length 
 
 actions[i]  is one of "call" and "getCallCount" 
 
 fnName  is one of "sum", "factorial" and "fib"

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
function memoize(fn) {
  const cache=new Map();
  return function(...args) {
    const key=JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result=fn(...args); cache.set(key,result); return result;
  };
}
```

---

## 2624. Snail Traversal

**Problem:** https://leetcode.com/problems/snail-traversal/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195485256  
**Language:** javascript

### Description

Write code that enhances all arrays such that you can call the  snail(rowsCount, colsCount)  method that transforms the 1D array into a 2D array organised in the pattern known as  snail traversal order . Invalid input values should output an empty array. If  rowsCount * colsCount !== nums.length , the input is considered invalid. 
 
 Snail traversal order   starts at the top left cell with the first value of the current array. It then moves through the entire first column from top to bottom, followed by moving to the next column on the right and traversing it from bottom to top. This pattern continues, alternating the direction of traversal with each column, until the entire current array is covered. For example, when given the input array  [19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15]  with  rowsCount = 5  and  colsCount = 4 , the desired output matrix is shown below. Note that iterating the matrix following the arrows corresponds to the order of numbers in the original array. 
 
   
 
 
 
   
 
 Example 1: 
 
```text
Input:
 
nums = [19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15]
rowsCount = 5
colsCount = 4

Output:
 
[
 [19,17,16,15],
 [10,1,14,4],
 [3,2,12,20],
 [7,5,18,11],
 [9,8,6,13]
]
```
 
 
 Example 2: 
 
```text
Input:
 
nums = [1,2,3,4]
rowsCount = 1
colsCount = 4

Output:
 [[1, 2, 3, 4]]
```
 
 
 Example 3: 
 
```text
Input:
 
nums = [1,3]
rowsCount = 2
colsCount = 2

Output:
 []

Explanation:
 2 multiplied by 2 is 4, and the original array [1,3] has a length of 2; therefore, the input is invalid.
```
 
 
   
 
 Constraints: 
 
 
 0 <= nums.length <= 250 
 
 1 <= nums[i] <= 1000 
 
 1 <= rowsCount <= 250 
 
 1 <= colsCount <= 250

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
Array.prototype.snail = function(rowsCount,colsCount) {
  if (rowsCount<=0 || colsCount<=0 || rowsCount*colsCount!==this.length) return [];
  const out=Array.from({length:rowsCount},()=>Array(colsCount));
  for (let c=0;c<colsCount;c++) for(let r=0;r<rowsCount;r++)
    out[c%2===0?r:rowsCount-1-r][c]=this[c*rowsCount+r];
  return out;
};
```

---

## 2625. Flatten Deeply Nested Array

**Problem:** https://leetcode.com/problems/flatten-deeply-nested-array/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195485416  
**Language:** javascript

### Description

Given a  multi-dimensional  array  arr  and a depth  n , return a  flattened  version of that array. 
 
 A  multi-dimensional  array is a recursive data structure that contains integers or other  multi-dimensional  arrays. 
 
 A  flattened  array is a version of that array with some or all of the sub-arrays removed and replaced with the actual elements in that sub-array. This flattening operation should only be done if the current depth of nesting is less than  n . The depth of the elements in the first array are considered to be  0 . 
 
 Please solve it without the built-in  Array.flat  method. 
 
   
 
 Example 1: 
 
```text
Input

arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 0

Output

[1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]

Explanation

Passing a depth of n=0 will always result in the original array. This is because the smallest possible depth of a subarray (0) is not less than n=0. Thus, no subarray should be flattened.
```
 
 
 Example 2: 
 
```text
Input

arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 1

Output

[1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]

Explanation

The subarrays starting with 4, 7, and 13 are all flattened. This is because their depth of 0 is less than 1. However [9, 10, 11] remains unflattened because its depth is 1.
```
 
 
 Example 3: 
 
```text
Input

arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 2

Output

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Explanation

The maximum depth of any subarray is 1. Thus, all of them are flattened.
```
 
 
   
 
 Constraints: 
 
 
 0 <= count of numbers in arr <= 10 5 
 
 0 <= count of subarrays in arr <= 10 5 
 
 maxDepth <= 1000 
 
 -1000 <= each number <= 1000 
 
 0 <= n <= 1000

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var flat = function(arr,n) {
  const result=[];
  function dfs(a,depth) {
    for(const x of a) {
      if(Array.isArray(x) && depth>0) dfs(x,depth-1);
      else result.push(x);
    }
  }
  dfs(arr,n); return result;
};
```

---

## 2626. Array Reduce Transformation

**Problem:** https://leetcode.com/problems/array-reduce-transformation/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195485584  
**Language:** javascript

### Description

Given an integer array  nums , a reducer function  fn , and an initial value  init , return the final result obtained by executing the  fn  function on each element of the array, sequentially, passing in the return value from the calculation on the preceding element. 
 
 This result is achieved through the following operations:  val = fn(init, nums[0]), val = fn(val, nums[1]), val = fn(val, nums[2]), ...  until every element in the array has been processed. The ultimate value of  val  is then returned. 
 
 If the length of the array is 0, the function should return  init . 
 
 Please solve it without using the built-in  Array.reduce  method. 
 
   
 
 Example 1: 
 
```text
Input:
 
nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr; }
init = 0

Output:
 10

Explanation:

initially, the value is init=0.
(0) + nums[0] = 1
(1) + nums[1] = 3
(3) + nums[2] = 6
(6) + nums[3] = 10
The final answer is 10.
```
 
 
 Example 2: 
 
```text
Input:
 
nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr * curr; }
init = 100

Output:
 130

Explanation:

initially, the value is init=100.
(100) + nums[0] * nums[0] = 101
(101) + nums[1] * nums[1] = 105
(105) + nums[2] * nums[2] = 114
(114) + nums[3] * nums[3] = 130
The final answer is 130.
```
 
 
 Example 3: 
 
```text
Input:
 
nums = []
fn = function sum(accum, curr) { return 0; }
init = 25

Output:
 25

Explanation:
 For empty arrays, the answer is always init.
```
 
 
   
 
 Constraints: 
 
 
 0 <= nums.length <= 1000 
 
 0 <= nums[i] <= 1000 
 
 0 <= init <= 1000

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var reduce = function(nums,fn,init) {
  let result=init;
  for(let i=0;i<nums.length;i++) result=fn(result,nums[i]);
  return result;
};
```

---

## 2627. Debounce

**Problem:** https://leetcode.com/problems/debounce/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195609306  
**Language:** javascript

### Description

Given a function  fn  and a time in milliseconds  t , return a  debounced  version of that function. 
 
 A  debounced  function is a function whose execution is delayed by  t  milliseconds and whose execution is cancelled if it is called again within that window of time. The debounced function should also receive the passed parameters. 
 
 For example, let's say  t = 50ms , and the function was called at  30ms ,  60ms , and  100ms . 
 
 The first 2 function calls would be cancelled, and the 3rd function call would be executed at  150ms . 
 
 If instead  t = 35ms , The 1st call would be cancelled, the 2nd would be executed at  95ms , and the 3rd would be executed at  135ms . 
 
 
 
 The above diagram shows how debounce will transform events. Each rectangle represents 100ms and the debounce time is 400ms. Each color represents a different set of inputs. 
 
 Please solve it without using lodash's  _.debounce()  function. 
 
   
 
 Example 1: 
 
```text
Input:
 
t = 50
calls = [
  {"t": 50, inputs: [1]},
  {"t": 75, inputs: [2]}
]

Output:
 [{"t": 125, inputs: [2]}]

Explanation:

let start = Date.now();
function log(...inputs) { 
  console.log([Date.now() - start, inputs ])
}
const dlog = debounce(log, 50);
setTimeout(() => dlog(1), 50);
setTimeout(() => dlog(2), 75);

The 1st call is cancelled by the 2nd call because the 2nd call occurred before 100ms
The 2nd call is delayed by 50ms and executed at 125ms. The inputs were (2).
```
 
 
 Example 2: 
 
```text
Input:
 
t = 20
calls = [
  {"t": 50, inputs: [1]},
  {"t": 100, inputs: [2]}
]

Output:
 [{"t": 70, inputs: [1]}, {"t": 120, inputs: [2]}]

Explanation:

The 1st call is delayed until 70ms. The inputs were (1).
The 2nd call is delayed until 120ms. The inputs were (2).
```
 
 
 Example 3: 
 
```text
Input:
 
t = 150
calls = [
  {"t": 50, inputs: [1, 2]},
  {"t": 300, inputs: [3, 4]},
  {"t": 300, inputs: [5, 6]}
]

Output:
 [{"t": 200, inputs: [1,2]}, {"t": 450, inputs: [5, 6]}]

Explanation:

The 1st call is delayed by 150ms and ran at 200ms. The inputs were (1, 2).
The 2nd call is cancelled by the 3rd call
The 3rd call is delayed by 150ms and ran at 450ms. The inputs were (5, 6).
```
 
 
   
 
 Constraints: 
 
 
 0 <= t <= 1000 
 
 1 <= calls.length <= 10 
 
 0 <= calls[i].t <= 1000 
 
 0 <= calls[i].inputs.length <= 10

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timer;

    return function(...args) {
        clearTimeout(timer);

        timer = setTimeout(() => {
            fn(...args);
        }, t);
    };
};


/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
```

---

## 2628. JSON Deep Equal

**Problem:** https://leetcode.com/problems/json-deep-equal/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195485744  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var areDeeplyEqual = function(o1,o2) {
  if(o1===o2) return true;
  if(o1===null || o2===null || typeof o1!=='object' || typeof o2!=='object') return false;
  if(Array.isArray(o1)!==Array.isArray(o2)) return false;
  const a=Object.keys(o1),b=Object.keys(o2);
  if(a.length!==b.length) return false;
  return a.every(k=>Object.prototype.hasOwnProperty.call(o2,k) && areDeeplyEqual(o1[k],o2[k]));
};
```

---

## 2629. Function Composition

**Problem:** https://leetcode.com/problems/function-composition/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195485914  
**Language:** javascript

### Description

Given an array of functions  [f 1 , f 2 , f 3 , ..., f n ] , return a new function  fn  that is the  function composition  of the array of functions. 
 
 The  function composition  of  [f(x), g(x), h(x)]  is  fn(x) = f(g(h(x))) . 
 
 The  function composition  of an empty list of functions is the  identity function   f(x) = x . 
 
 You may assume each function in the array accepts one integer as input and returns one integer as output. 
 
   
 
 Example 1: 
 
```text
Input:
 functions = [x => x + 1, x => x * x, x => 2 * x], x = 4

Output:
 65

Explanation:

Evaluating from right to left ...
Starting with x = 4.
2 * (4) = 8
(8) * (8) = 64
(64) + 1 = 65
```
 
 
 Example 2: 
 
```text
Input:
 functions = [x => 10 * x, x => 10 * x, x => 10 * x], x = 1

Output:
 1000

Explanation:

Evaluating from right to left ...
10 * (1) = 10
10 * (10) = 100
10 * (100) = 1000
```
 
 
 Example 3: 
 
```text
Input:
 functions = [], x = 42

Output:
 42

Explanation:

The composition of zero functions is the identity function
```
 
 
   
 
 Constraints: 
 
 
 -1000 <= x <= 1000 
 
 0 <= functions.length <= 1000 
 
 all functions accept and return a single integer

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var compose = function(functions) {
  return function(x) {
    for(let i=functions.length-1;i>=0;i--) x=functions[i](x);
    return x;
  };
};
```

---

## 2630. Memoize II

**Problem:** https://leetcode.com/problems/memoize-ii/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195486117  
**Language:** javascript

### Description

Given a function  fn , return a  memoized  version of that function. 
 
 A  memoized  function is a function that will never be called twice with the same inputs. Instead it will return a cached value. 
 
 fn  can be any function and there are no constraints on what type of values it accepts. Inputs are considered identical if they are  ===  to each other. 
 
   
 
 Example 1: 
 
```text
Input:
 
getInputs = () => [[2,2],[2,2],[1,2]]
fn = function (a, b) { return a + b; }

Output:
 [{"val":4,"calls":1},{"val":4,"calls":1},{"val":3,"calls":2}]

Explanation:

const inputs = getInputs();
const memoized = memoize(fn);
for (const arr of inputs) {
  memoized(...arr);
}

For the inputs of (2, 2): 2 + 2 = 4, and it required a call to fn().
For the inputs of (2, 2): 2 + 2 = 4, but those inputs were seen before so no call to fn() was required.
For the inputs of (1, 2): 1 + 2 = 3, and it required another call to fn() for a total of 2.
```
 
 
 Example 2: 
 
```text
Input:
 
getInputs = () => [[{},{}],[{},{}],[{},{}]] 
fn = function (a, b) { return ({...a, ...b}); }

Output:
 [{"val":{},"calls":1},{"val":{},"calls":2},{"val":{},"calls":3}]

Explanation:

Merging two empty objects will always result in an empty object. It may seem like there should only be 1 call to fn() because of cache-hits, however none of those objects are === to each other.
```
 
 
 Example 3: 
 
```text
Input:
 
getInputs = () => { const o = {}; return [[o,o],[o,o],[o,o]]; }
fn = function (a, b) { return ({...a, ...b}); }

Output:
 [{"val":{},"calls":1},{"val":{},"calls":1},{"val":{},"calls":1}]

Explanation:

Merging two empty objects will always result in an empty object. The 2nd and 3rd third function calls result in a cache-hit. This is because every object passed in is identical.
```
 
 
   
 
 Constraints: 
 
 
 1 <= inputs.length <= 10 5 
 
 0 <= inputs.flat().length <= 10 5 
 
 inputs[i][j] != NaN

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
function memoize(fn) {
  const root=new Map(),VALUE=Symbol('value');
  return function(...args) {
    let node=root;
    for(const arg of args) {
      if(!node.has(arg)) node.set(arg,new Map());
      node=node.get(arg);
    }
    if(node.has(VALUE)) return node.get(VALUE);
    const result=fn.apply(this,args);
    node.set(VALUE,result);
    return result;
  };
}
```

---

## 2631. Group By

**Problem:** https://leetcode.com/problems/group-by/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195486275  
**Language:** javascript

### Description

Write code that enhances all arrays such that you can call the  array.groupBy(fn)  method on any array and it will return a  grouped  version of the array. 
 
 A  grouped  array is an object where each key is the output of  fn(arr[i])  and each value is an array containing all items in the original array which generate that key. 
 
 The provided callback  fn  will accept an item in the array and return a string key. 
 
 The order of each value list should be the order the items appear in the array. Any order of keys is acceptable. 
 
 Please solve it without lodash's  _.groupBy  function. 
 
   
 
 Example 1: 
 
```text
Input:
 
array = [
  {"id":"1"},
  {"id":"1"},
  {"id":"2"}
], 
fn = function (item) { 
  return item.id; 
}

Output:
 
{ 
  "1": [{"id": "1"}, {"id": "1"}],   
  "2": [{"id": "2"}] 
}

Explanation:

Output is from array.groupBy(fn).
The selector function gets the "id" out of each item in the array.
There are two objects with an "id" of 1. Both of those objects are put in the first array.
There is one object with an "id" of 2. That object is put in the second array.
```
 
 
 Example 2: 
 
```text
Input:
 
array = [
  [1, 2, 3],
  [1, 3, 5],
  [1, 5, 9]
]
fn = function (list) { 
  return String(list[0]); 
}

Output:
 
{ 
  "1": [[1, 2, 3], [1, 3, 5], [1, 5, 9]] 
}

Explanation:

The array can be of any type. In this case, the selector function defines the key as being the first element in the array. 
All the arrays have 1 as their first element so they are grouped together.
{
  "1": [[1, 2, 3], [1, 3, 5], [1, 5, 9]]
}
```
 
 
 Example 3: 
 
```text
Input:
 
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fn = function (n) { 
  return String(n > 5);
}

Output:

{
  "true": [6, 7, 8, 9, 10],
  "false": [1, 2, 3, 4, 5]
}

Explanation:

The selector function splits the array by whether each number is greater than 5.
```
 
 
   
 
 Constraints: 
 
 
 0 <= array.length <= 10 5 
 
 fn  returns a string

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
Array.prototype.groupBy = function(fn) {
  const groups={};
  for(const item of this) {
    const key=fn(item);
    if(!Object.prototype.hasOwnProperty.call(groups,key)) groups[key]=[];
    groups[key].push(item);
  }
  return groups;
};
```

---

## 2632. Curry

**Problem:** https://leetcode.com/problems/curry/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195486474  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var curry = function(fn) {
  function curried(...args) {
    if(args.length>=fn.length) return fn(...args);
    return (...next)=>curried(...args,...next);
  }
  return curried;
};
```

---

## 2633. Convert Object to JSON String

**Problem:** https://leetcode.com/problems/convert-object-to-json-string/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195486664  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var jsonStringify = function(object) {
  function stringify(v) {
    if(v===null) return 'null';
    if(typeof v==='string') return '"'+v.replace(/[\"\\\u0000-\u001f]/g,c=>({ '"':'\\"','\\':'\\\\','\b':'\\b','\f':'\\f','\n':'\\n','\r':'\\r','\t':'\\t' }[c] || '\\u'+c.charCodeAt(0).toString(16).padStart(4,'0')))+'"';
    if(typeof v!=='object') return String(v);
    if(Array.isArray(v)) return '['+v.map(stringify).join(',')+']';
    return '{'+Object.keys(v).map(k=>stringify(k)+':'+stringify(v[k])).join(',')+'}';
  }
  return stringify(object);
};
```

---

## 2634. Filter Elements from Array

**Problem:** https://leetcode.com/problems/filter-elements-from-array/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195486825  
**Language:** javascript

### Description

Given an integer array  arr  and a filtering function  fn , return a filtered array  filteredArr . 
 
 The  fn  function takes one or two arguments: 
 
 
 arr[i]  - number from the  arr 
 
 i  - index of  arr[i] 
 
 
 filteredArr  should only contain the elements from the  arr  for which the expression  fn(arr[i], i)  evaluates to a  truthy  value. A  truthy  value is a value where  Boolean(value)  returns  true . 
 
 Please solve it without the built-in  Array.filter  method. 
 
   
 
 Example 1: 
 
```text
Input:
 arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; }

Output:
 [20,30]

Explanation:

const newArray = filter(arr, fn); // [20, 30]
The function filters out values that are not greater than 10
```
 
 
 Example 2: 
 
```text
Input:
 arr = [1,2,3], fn = function firstIndex(n, i) { return i === 0; }

Output:
 [1]

Explanation:

fn can also accept the index of each element
In this case, the function removes elements not at index 0
```
 
 
 Example 3: 
 
```text
Input:
 arr = [-2,-1,0,1,2], fn = function plusOne(n) { return n + 1 }

Output:
 [-2,0,1,2]

Explanation:

Falsey values such as 0 should be filtered out
```
 
 
   
 
 Constraints: 
 
 
 0 <= arr.length <= 1000 
 
 -10 9  <= arr[i] <= 10 9

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var filter = function(arr,fn) {
  const result=[];
  for(let i=0;i<arr.length;i++) if(fn(arr[i],i)) result.push(arr[i]);
  return result;
};
```

---

## 2635. Apply Transform Over Each Element in Array

**Problem:** https://leetcode.com/problems/apply-transform-over-each-element-in-array/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195487022  
**Language:** javascript

### Description

Given an integer array  arr  and a mapping function  fn , return a new array with a transformation applied to each element. 
 
 The returned array should be created such that  returnedArray[i] = fn(arr[i], i) . 
 
 Please solve it without the built-in  Array.map  method. 
 
   
 
 Example 1: 
 
```text
Input:
 arr = [1,2,3], fn = function plusone(n) { return n + 1; }

Output:
 [2,3,4]

Explanation:

const newArray = map(arr, plusone); // [2,3,4]
The function increases each value in the array by one.
```
 
 
 Example 2: 
 
```text
Input:
 arr = [1,2,3], fn = function plusI(n, i) { return n + i; }

Output:
 [1,3,5]

Explanation:
 The function increases each value by the index it resides in.
```
 
 
 Example 3: 
 
```text
Input:
 arr = [10,20,30], fn = function constant() { return 42; }

Output:
 [42,42,42]

Explanation:
 The function always returns 42.
```
 
 
   
 
 Constraints: 
 
 
 0 <= arr.length <= 1000 
 
 -10 9  <= arr[i] <= 10 9 
 
 fn  returns an integer.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var map = function(arr, fn) { const out = []; for (let i=0;i<arr.length;i++) out.push(fn(arr[i],i)); return out; };
```

---

## 2636. Promise Pool

**Problem:** https://leetcode.com/problems/promise-pool/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195487189  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var promisePool = async function(functions, n) {
  let next=0;
  async function worker() {
    while(next<functions.length) { const i=next++; await functions[i](); }
  }
  await Promise.all(Array.from({length:Math.min(n,functions.length)},worker));
};
```

---

## 2637. Promise Time Limit

**Problem:** https://leetcode.com/problems/promise-time-limit/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195487374  
**Language:** javascript

### Description

Given an asynchronous function  fn  and a time  t  in milliseconds, return a new  time limited  version of the input function.  fn  takes arguments provided to the  time limited  function. 
 
 The  time limited  function should follow these rules: 
 
 
 If the  fn  completes within the time limit of  t  milliseconds, the  time limited  function should resolve with the result. 
 
 If the execution of the  fn  exceeds the time limit, the  time limited  function should reject with the string  "Time Limit Exceeded" . 
 
 
   
 
 Example 1: 
 
```text
Input:
 
fn = async (n) => { 
  await new Promise(res => setTimeout(res, 100)); 
  return n * n; 
}
inputs = [5]
t = 50

Output:
 {"rejected":"Time Limit Exceeded","time":50}

Explanation:

const limited = timeLimit(fn, t)
const start = performance.now()
let result;
try {
   const res = await limited(...inputs)
   result = {"resolved": res, "time": Math.floor(performance.now() - start)};
} catch (err) {
   result = {"rejected": err, "time": Math.floor(performance.now() - start)};
}
console.log(result) // Output

The provided function is set to resolve after 100ms. However, the time limit is set to 50ms. It rejects at t=50ms because the time limit was reached.
```
 
 
 Example 2: 
 
```text
Input:
 
fn = async (n) => { 
  await new Promise(res => setTimeout(res, 100)); 
  return n * n; 
}
inputs = [5]
t = 150

Output:
 {"resolved":25,"time":100}

Explanation:

The function resolved 5 * 5 = 25 at t=100ms. The time limit is never reached.
```
 
 
 Example 3: 
 
```text
Input:
 
fn = async (a, b) => { 
  await new Promise(res => setTimeout(res, 120)); 
  return a + b; 
}
inputs = [5,10]
t = 150

Output:
 {"resolved":15,"time":120}

Explanation:

​​​​The function resolved 5 + 10 = 15 at t=120ms. The time limit is never reached.
```
 
 
 Example 4: 
 
```text
Input:
 
fn = async () => { 
  throw "Error";
}
inputs = []
t = 1000

Output:
 {"rejected":"Error","time":0}

Explanation:

The function immediately throws an error.
```
 
 
   
 
 Constraints: 
 
 
 0 <= inputs.length <= 10 
 
 0 <= t <= 1000 
 
 fn  returns a promise

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var timeLimit = function(fn,t) { return async function(...args) {
  let timer;
  try { return await Promise.race([
    Promise.resolve().then(()=>fn(...args)),
    new Promise((_,reject)=>{timer=setTimeout(()=>reject('Time Limit Exceeded'),t);})
  ]); } finally { clearTimeout(timer); }
}; };
```

---

## 2648. Generate Fibonacci Sequence

**Problem:** https://leetcode.com/problems/generate-fibonacci-sequence/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195487583  
**Language:** javascript

### Description

Write a generator function that returns a generator object which yields the  fibonacci sequence . 
 
 The  fibonacci sequence  is defined by the relation  X n  = X n-1  + X n-2 . 
 
 The first few numbers of the series are  0, 1, 1, 2, 3, 5, 8, 13 . 
 
   
 
 Example 1: 
 
```text
Input:
 callCount = 5

Output:
 [0,1,1,2,3]

Explanation:

const gen = fibGenerator();
gen.next().value; // 0
gen.next().value; // 1
gen.next().value; // 1
gen.next().value; // 2
gen.next().value; // 3
```
 
 
 Example 2: 
 
```text
Input:
 callCount = 0

Output:
 []

Explanation:
 gen.next() is never called so nothing is outputted
```
 
 
   
 
 Constraints: 
 
 
 0 <= callCount <= 50

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var fibGenerator = function*() { let a=0,b=1; while(true) {yield a; [a,b]=[b,a+b];} };
```

---

## 2649. Nested Array Generator

**Problem:** https://leetcode.com/problems/nested-array-generator/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195487766  
**Language:** javascript

### Description

Given a  multi-dimensional array  of integers, return a generator object which yields integers in the same order as  inorder traversal . 
 
 A  multi-dimensional array  is a recursive data structure that contains both integers and other  multi-dimensional arrays . 
 
 inorder traversal  iterates over each array from left to right, yielding any integers it encounters or applying  inorder traversal  to any arrays it encounters. 
 
   
 
 Example 1: 
 
```text
Input:
 arr = [[[6]],[1,3],[]]

Output:
 [6,1,3]

Explanation:

const generator = inorderTraversal(arr);
generator.next().value; // 6
generator.next().value; // 1
generator.next().value; // 3
generator.next().done; // true
```
 
 
 Example 2: 
 
```text
Input:
 arr = []

Output:
 []

Explanation:
 There are no integers so the generator doesn't yield anything.
```
 
 
   
 
 Constraints: 
 
 
 0 <= arr.flat().length <= 10 5 
 
 0 <= arr.flat()[i] <= 10 5 
 
 maxNestingDepth <= 10 5 
 
 
   
 Can you solve this without creating a new flattened version of the array?

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var inorderTraversal = function*(arr) {
  const stack=[arr[Symbol.iterator]()];
  while(stack.length) {
    const next=stack[stack.length-1].next();
    if(next.done) {stack.pop();continue;}
    if(Array.isArray(next.value)) stack.push(next.value[Symbol.iterator]());
    else yield next.value;
  }
};
```

---

## 2650. Design Cancellable Function

**Problem:** https://leetcode.com/problems/design-cancellable-function/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195617930  
**Language:** javascript

### Description

Sometimes you have a long running task, and you may wish to cancel it before it completes. To help with this goal, write a function  cancellable  that accepts a generator object and returns an array of two values: a  cancel function  and a  promise . 
 
 You may assume the generator function will only yield promises. It is your function's responsibility to pass the values resolved by the promise back to the generator. If the promise rejects, your function should throw that error back to the generator. 
 
 If the cancel callback is called before the generator is done, your function should throw an error back to the generator. That error should be the string  "Cancelled"  (Not an  Error  object). If the error was caught, the returned promise should resolve with the next value that was yielded or returned. Otherwise, the promise should reject with the thrown error. No more code should be executed. 
 
 When the generator is done, the promise your function returned should resolve the value the generator returned. If, however, the generator throws an error, the returned promise should reject with the error. 
 
 An example of how your code would be used: 
 
```text
function* tasks() {
  const val = yield new Promise(resolve => resolve(2 + 2));
  yield new Promise(resolve => setTimeout(resolve, 100));
  return val + 1; // calculation shouldn't be done.
}
const [cancel, promise] = cancellable(tasks());
setTimeout(cancel, 50);
promise.catch(console.log); // logs "Cancelled" at t=50ms
```
 
 
 If instead  cancel()  was not called or was called after  t=100ms , the promise would have resolved  5 . 
 
   
 
 Example 1: 
 
```text
Input:
 
generatorFunction = function*() { 
  return 42; 
}
cancelledAt = 100

Output:
 {"resolved": 42}

Explanation:

const generator = generatorFunction();
const [cancel, promise] = cancellable(generator);
setTimeout(cancel, 100);
promise.then(console.log); // resolves 42 at t=0ms

The generator immediately yields 42 and finishes. Because of that, the returned promise immediately resolves 42. Note that cancelling a finished generator does nothing.
```
 
 
 Example 2: 
 
```text
Input:

generatorFunction = function*() { 
  const msg = yield new Promise(res => res("Hello")); 
  throw `Error: ${msg}`; 
}
cancelledAt = null

Output:
 {"rejected": "Error: Hello"}

Explanation:

A promise is yielded. The function handles this by waiting for it to resolve and then passes the resolved value back to the generator. Then an error is thrown which has the effect of causing the promise to reject with the same thrown error.
```
 
 
 Example 3: 
 
```text
Input:
 
generatorFunction = function*() { 
  yield new Promise(res => setTimeout(res, 200)); 
  return "Success"; 
}
cancelledAt = 100

Output:
 {"rejected": "Cancelled"}

Explanation:

While the function is waiting for the yielded promise to resolve, cancel() is called. This causes an error message to be sent back to the generator. Since this error is uncaught, the returned promise rejected with this error.
```
 
 
 Example 4: 
 
```text
Input:

generatorFunction = function*() { 
  let result = 0; 
  yield new Promise(res => setTimeout(res, 100));
  result += yield new Promise(res => res(1)); 
  yield new Promise(res => setTimeout(res, 100)); 
  result += yield new Promise(res => res(1)); 
  return result;
}
cancelledAt = null

Output:
 {"resolved": 2}

Explanation:

4 promises are yielded. Two of those promises have their values added to the result. After 200ms, the generator finishes with a value of 2, and that value is resolved by the returned promise.
```
 
 
 Example 5: 
 
```text
Input:
 
generatorFunction = function*() { 
  let result = 0; 
  try { 
    yield new Promise(res => setTimeout(res, 100)); 
    result += yield new Promise(res => res(1)); 
    yield new Promise(res => setTimeout(res, 100)); 
    result += yield new Promise(res => res(1)); 
  } catch(e) { 
    return result; 
  } 
  return result; 
}
cancelledAt = 150

Output:
 {"resolved": 1}

Explanation:

The first two yielded promises resolve and cause the result to increment. However, at t=150ms, the generator is cancelled. The error sent to the generator is caught and the result is returned and finally resolved by the returned promise.
```
 
 
 Example 6: 
 
```text
Input:
 
generatorFunction = function*() { 
  try { 
    yield new Promise((resolve, reject) => reject("Promise Rejected")); 
  } catch(e) { 
    let a = yield new Promise(resolve => resolve(2));
    let b = yield new Promise(resolve => resolve(2)); 
    return a + b; 
  }; 
}
cancelledAt = null

Output:
 {"resolved": 4}

Explanation:

The first yielded promise immediately rejects. This error is caught. Because the generator hasn't been cancelled, execution continues as usual. It ends up resolving 2 + 2 = 4.
```
 
 
   
 
 Constraints: 
 
 
 cancelledAt == null or 0 <= cancelledAt <= 1000 
 
 generatorFunction  returns a generator object

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */

/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
    let cancel;

    const cancelPromise = new Promise((resolve, reject) => {
        cancel = () => reject("Cancelled");
    });

    // Prevent unhandled rejection
    cancelPromise.catch(() => {});

    const promise = (async () => {
        let result = generator.next();

        while (!result.done) {
            try {
                const value = await Promise.race([
                    result.value,
                    cancelPromise
                ]);

                result = generator.next(value);
            } catch (error) {
                result = generator.throw(error);
            }
        }

        return result.value;
    })();

    return [cancel, promise];
};


/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */
```

---

## 2665. Counter II

**Problem:** https://leetcode.com/problems/counter-ii/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195487964  
**Language:** javascript

### Description

Write a function  createCounter . It should accept an initial integer  init . It should return an object with three functions. 
 
 The three functions are: 
 
 
 increment()  increases the current value by 1 and then returns it. 
 
 decrement()  reduces the current value by 1 and then returns it. 
 
 reset()  sets the current value to  init  and then returns it. 
 
 
   
 
 Example 1: 
 
```text
Input:
 init = 5, calls = ["increment","reset","decrement"]

Output:
 [6,5,4]

Explanation:

const counter = createCounter(5);
counter.increment(); // 6
counter.reset(); // 5
counter.decrement(); // 4
```
 
 
 Example 2: 
 
```text
Input:
 init = 0, calls = ["increment","increment","decrement","reset","reset"]

Output:
 [1,2,1,0,0]

Explanation:

const counter = createCounter(0);
counter.increment(); // 1
counter.increment(); // 2
counter.decrement(); // 1
counter.reset(); // 0
counter.reset(); // 0
```
 
 
   
 
 Constraints: 
 
 
 -1000 <= init <= 1000 
 
 0 <= calls.length <= 1000 
 
 calls[i]  is one of "increment", "decrement" and "reset"

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var createCounter = function(init) { let v=init; return {
 increment:()=>++v, decrement:()=>--v, reset:()=>{v=init;return v;}
}; };
```

---

## 2666. Allow One Function Call

**Problem:** https://leetcode.com/problems/allow-one-function-call/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195488149  
**Language:** javascript

### Description

Given a function  fn , return a new function that is identical to the original function except that it ensures  fn  is called at most once. 
 
 
 The first time the returned function is called, it should return the same result as  fn . 
 
 Every subsequent time it is called, it should return  undefined . 
 
 
   
 
 Example 1: 
 
```text
Input:
 fn = (a,b,c) => (a + b + c), calls = [[1,2,3],[2,3,6]]

Output:
 [{"calls":1,"value":6}]

Explanation:

const onceFn = once(fn);
onceFn(1, 2, 3); // 6
onceFn(2, 3, 6); // undefined, fn was not called
```
 
 
 Example 2: 
 
```text
Input:
 fn = (a,b,c) => (a * b * c), calls = [[5,7,4],[2,3,6],[4,6,8]]

Output:
 [{"calls":1,"value":140}]

Explanation:

const onceFn = once(fn);
onceFn(5, 7, 4); // 140
onceFn(2, 3, 6); // undefined, fn was not called
onceFn(4, 6, 8); // undefined, fn was not called
```
 
 
   
 
 Constraints: 
 
 
 calls  is a valid JSON array 
 
 1 <= calls.length <= 10 
 
 1 <= calls[i].length <= 100 
 
 2 <= JSON.stringify(calls).length <= 1000

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var once = function(fn) {let called=false;return function(...args){if(called)return undefined;called=true;return fn.apply(this,args);};};
```

---

## 2667. Create Hello World Function

**Problem:** https://leetcode.com/problems/create-hello-world-function/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195488292  
**Language:** javascript

### Description

Write a function  createHelloWorld . It should return a new function that always returns  "Hello World" .
 
   
 
 Example 1: 
 
```text
Input:
 args = []

Output:
 "Hello World"

Explanation:

const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".
```
 
 
 Example 2: 
 
```text
Input:
 args = [{},null,42]

Output:
 "Hello World"

Explanation:

const f = createHelloWorld();
f({}, null, 42); // "Hello World"

Any arguments could be passed to the function but it should still always return "Hello World".
```
 
 
   
 
 Constraints: 
 
 
 0 <= args.length <= 10

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var createHelloWorld = function(){return function(...args){return 'Hello World';};};
```

---

## 2675. Array of Objects to Matrix

**Problem:** https://leetcode.com/problems/array-of-objects-to-matrix/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195488465  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var jsonToMatrix = function(arr) {
  const rows=[], keys=new Set();
  function visit(x,path,row) {
    if(x!==null && typeof x==='object') {
      for(const k of Object.keys(x)) visit(x[k],path?path+'.'+k:k,row);
    } else {row[path]=x;keys.add(path);}
  }
  for(const x of arr){const row={};visit(x,'',row);rows.push(row);}
  const cols=[...keys].sort();
  return [cols,...rows.map(r=>cols.map(k=>Object.prototype.hasOwnProperty.call(r,k)?r[k]:''))];
};
```

---

## 2676. Throttle

**Problem:** https://leetcode.com/problems/throttle/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195609488  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let waiting = false;
    let nextArgs = null;

    function execute() {
        if (nextArgs === null) {
            waiting = false;
            return;
        }

        const args = nextArgs;
        nextArgs = null;

        fn(...args);
        setTimeout(execute, t);
    }

    return function(...args) {
        if (waiting) {
            nextArgs = args;
            return;
        }

        fn(...args);
        waiting = true;
        setTimeout(execute, t);
    };
};


/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
```

---

## 2677. Chunk Array

**Problem:** https://leetcode.com/problems/chunk-array/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195488646  
**Language:** javascript

### Description

Given an array  arr  and a chunk size  size , return a  chunked  array. 
 
 A  chunked  array contains the original elements in  arr , but consists of subarrays each of length  size . The length of the last subarray may be less than  size  if  arr.length  is not evenly divisible by  size . 
 
 Please solve it without using lodash's  _.chunk  function. 
 
   
 
 Example 1: 
 
```text
Input:
 arr = [1,2,3,4,5], size = 1

Output:
 [[1],[2],[3],[4],[5]]

Explanation:
 The arr has been split into subarrays each with 1 element.
```
 
 
 Example 2: 
 
```text
Input:
 arr = [1,9,6,3,2], size = 3

Output:
 [[1,9,6],[3,2]]

Explanation:
 The arr has been split into subarrays with 3 elements. However, only two elements are left for the 2nd subarray.
```
 
 
 Example 3: 
 
```text
Input:
 arr = [8,5,3,2,6], size = 6

Output:
 [[8,5,3,2,6]]

Explanation:
 Size is greater than arr.length thus all elements are in the first subarray.
```
 
 
 Example 4: 
 
```text
Input:
 arr = [], size = 1

Output:
 []

Explanation:
 There are no elements to be chunked so an empty array is returned.
```
 
 
   
 
 Constraints: 
 
 
 arr  is a valid JSON array 
 
 2 <= JSON.stringify(arr).length <= 10 5 
 
 1 <= size <= arr.length + 1

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var chunk = function(arr,size){const out=[];for(let i=0;i<arr.length;i+=size)out.push(arr.slice(i,i+size));return out;};
```

---

## 2690. Infinite Method Object

**Problem:** https://leetcode.com/problems/infinite-method-object/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195488822  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var createInfiniteObject = function(){return new Proxy({}, {get:(_,key)=>()=>key});};
```

---

## 2691. Immutability Helper

**Problem:** https://leetcode.com/problems/immutability-helper/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195609996  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript

var ImmutableHelper = function(obj) {
    this.obj = obj;
};

ImmutableHelper.prototype.produce = function(mutator) {
    const states = new WeakMap();

    function createProxy(target, parent = null) {
        if (states.has(target)) {
            return states.get(target).proxy;
        }

        const state = {
            original: target,
            copy: null,
            parent: parent,
            proxy: null
        };

        function markChanged() {
            if (state.copy !== null) return;

            state.copy = Array.isArray(target)
                ? target.slice()
                : { ...target };

            if (parent !== null) {
                markParent(parent, target, state);
            }
        }

        function markParent(parentState, child, childState) {
            if (parentState.copy === null) {
                parentState.copy = Array.isArray(parentState.original)
                    ? parentState.original.slice()
                    : { ...parentState.original };

                if (parentState.parent !== null) {
                    const grandparent = parentState.parent;
                    markParent(grandparent, parentState.original, parentState);
                }
            }

            for (const key of Object.keys(parentState.copy)) {
                if (parentState.copy[key] === child) {
                    parentState.copy[key] = childState.copy;
                }
            }
        }

        const proxy = new Proxy(target, {
            get(target, key) {
                const source = state.copy || target;
                const value = source[key];

                if (value !== null && typeof value === "object") {
                    return createProxy(value, state);
                }

                return value;
            },

            set(target, key, value) {
                markChanged();
                state.copy[key] = value;
                return true;
            }
        });

        state.proxy = proxy;
        states.set(target, state);

        return proxy;
    }

    const proxy = createProxy(this.obj);
    mutator(proxy);

    const root = states.get(this.obj);
    return root.copy || this.obj;
};
```

---

## 2692. Make Object Immutable

**Problem:** https://leetcode.com/problems/make-object-immutable/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195610151  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/**
 * @param {Object|Array} obj
 * @return {Object|Array} immutable obj
 */

/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var makeImmutable = function(obj) {
    const methods = new Set([
        "pop", "push", "shift", "unshift",
        "splice", "sort", "reverse"
    ]);

    function createProxy(target) {
        return new Proxy(target, {
            get(target, key, receiver) {
                if (Array.isArray(target) && methods.has(key)) {
                    return function() {
                        throw `Error Calling Method: ${key}`;
                    };
                }

                const value = Reflect.get(target, key, receiver);

                if (value !== null && typeof value === "object") {
                    return createProxy(value);
                }

                return value;
            },

            set(target, key) {
                if (Array.isArray(target)) {
                    throw `Error Modifying Index: ${String(key)}`;
                }

                throw `Error Modifying: ${String(key)}`;
            },

            deleteProperty(target, key) {
                if (Array.isArray(target)) {
                    throw `Error Modifying Index: ${String(key)}`;
                }

                throw `Error Modifying: ${String(key)}`;
            }
        });
    }

    return createProxy(obj);
};


/**
 * const obj = makeImmutable({x: 5});
 * obj.x = 6; // throws "Error Modifying x"
 */
```

---

## 2693. Call Function with Custom Context

**Problem:** https://leetcode.com/problems/call-function-with-custom-context/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195491469  
**Language:** javascript

### Description

Enhance all functions to have the  callPolyfill  method. The method accepts an object  obj  as its first parameter and any number of additional arguments. The  obj  becomes the  this  context for the function. The additional arguments are passed to the function (that the  callPolyfill  method belongs on). 
 
 For example if you had the function: 
 
```text
function tax(price, taxRate) {
  const totalCost = price * (1 + taxRate);
  console.log(`The cost of ${this.item} is ${totalCost}`);
}
```
 
 
 Calling this function like  tax(10, 0.1)  will log  "The cost of undefined is 11" . This is because the  this  context was not defined. 
 
 However, calling the function like  tax.callPolyfill({item: "salad"}, 10, 0.1)  will log  "The cost of salad is 11" . The  this  context was appropriately set, and the function logged an appropriate output. 
 
 Please solve this without using the built-in  Function.call  method. 
 
   
 
 Example 1: 
 
```text
Input:

fn = function add(b) {
  return this.a + b;
}
args = [{"a": 5}, 7]

Output:
 12

Explanation:

fn.callPolyfill({"a": 5}, 7); // 12
callPolyfill sets the "this" context to {"a": 5}. 7 is passed as an argument.
```
 
 
 Example 2: 
 
```text
Input:
 
fn = function tax(price, taxRate) { 
 return `The cost of the ${this.item} is ${price * taxRate}`; 
}
args = [{"item": "burger"}, 10, 1.1]

Output:
 "The cost of the burger is 11"

Explanation:
 callPolyfill sets the "this" context to {"item": "burger"}. 10 and 1.1 are passed as additional arguments.
```
 
 
   
 
 Constraints: 
 
 
 typeof args[0] == 'object' and args[0] != null 
 
 1 <= args.length <= 100 
 
 2 <= JSON.stringify(args[0]).length <= 10 5

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
Function.prototype.callPolyfill = function(context,...args){return this.apply(context,args);};
```

---

## 2694. Event Emitter

**Problem:** https://leetcode.com/problems/event-emitter/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195491651  
**Language:** javascript

### Description

Design an  EventEmitter  class. This interface is similar (but with some differences) to the one found in Node.js or the Event Target interface of the DOM. The  EventEmitter  should allow for subscribing to events and emitting them. 
 
 Your  EventEmitter  class should have the following two methods: 
 
 
 subscribe  - This method takes in two arguments: the name of an event as a string and a callback function. This callback function will later be called when the event is emitted. 
	An event should be able to have multiple listeners for the same event. When emitting an event with multiple callbacks, each should be called in the order in which they were subscribed. An array of results should be returned. You can assume no callbacks passed to  subscribe  are referentially identical. 
	The  subscribe  method should also return an object with an  unsubscribe  method that enables the user to unsubscribe. When it is called, the callback should be removed from the list of subscriptions and  undefined  should be returned. 
 
 emit  - This method takes in two arguments: the name of an event as a string and an optional array of arguments that will be passed to the callback(s). If there are no callbacks subscribed to the given event, return an empty array. Otherwise, return an array of the results of all callback calls in the order they were subscribed. 
 
 
   
 
 Example 1: 
 
```text
Input:
 
actions = ["EventEmitter", "emit", "subscribe", "subscribe", "emit"], 
values = [[], ["firstEvent"], ["firstEvent", "function cb1() { return 5; }"],  ["firstEvent", "function cb1() { return 6; }"], ["firstEvent"]]

Output:
 [[],["emitted",[]],["subscribed"],["subscribed"],["emitted",[5,6]]]

Explanation:
 
const emitter = new EventEmitter();
emitter.emit("firstEvent"); // [], no callback are subscribed yet
emitter.subscribe("firstEvent", function cb1() { return 5; });
emitter.subscribe("firstEvent", function cb2() { return 6; });
emitter.emit("firstEvent"); // [5, 6], returns the output of cb1 and cb2
```
 
 
 Example 2: 
 
```text
Input:
 
actions = ["EventEmitter", "subscribe", "emit", "emit"], 
values = [[], ["firstEvent", "function cb1(...args) { return args.join(','); }"], ["firstEvent", [1,2,3]], ["firstEvent", [3,4,6]]]

Output:
 [[],["subscribed"],["emitted",["1,2,3"]],["emitted",["3,4,6"]]]

Explanation: 
Note that the emit method should be able to accept an OPTIONAL array of arguments.

const emitter = new EventEmitter();
emitter.subscribe("firstEvent, function cb1(...args) { return args.join(','); });
emitter.emit("firstEvent", [1, 2, 3]); // ["1,2,3"]
emitter.emit("firstEvent", [3, 4, 6]); // ["3,4,6"]
```
 
 
 Example 3: 
 
```text
Input:
 
actions = ["EventEmitter", "subscribe", "emit", "unsubscribe", "emit"], 
values = [[], ["firstEvent", "(...args) => args.join(',')"], ["firstEvent", [1,2,3]], [0], ["firstEvent", [4,5,6]]]

Output:
 [[],["subscribed"],["emitted",["1,2,3"]],["unsubscribed",0],["emitted",[]]]

Explanation:

const emitter = new EventEmitter();
const sub = emitter.subscribe("firstEvent", (...args) => args.join(','));
emitter.emit("firstEvent", [1, 2, 3]); // ["1,2,3"]
sub.unsubscribe(); // undefined
emitter.emit("firstEvent", [4, 5, 6]); // [], there are no subscriptions
```
 
 
 Example 4: 
 
```text
Input:
 
actions = ["EventEmitter", "subscribe", "subscribe", "unsubscribe", "emit"], 
values = [[], ["firstEvent", "x => x + 1"], ["firstEvent", "x => x + 2"], [0], ["firstEvent", [5]]]

Output:
 [[],["subscribed"],["subscribed"],["unsubscribed",0],["emitted",[7]]]

Explanation:

const emitter = new EventEmitter();
const sub1 = emitter.subscribe("firstEvent", x => x + 1);
const sub2 = emitter.subscribe("firstEvent", x => x + 2);
sub1.unsubscribe(); // undefined
emitter.emit("firstEvent", [5]); // [7]
```
 
 
   
 
 Constraints: 
 
 
 1 <= actions.length <= 10 
 
 values.length === actions.length 
 
 All test cases are valid, e.g. you don't need to handle scenarios when unsubscribing from a non-existing subscription. 
 
 There are only 4 different actions:  EventEmitter ,  emit ,  subscribe , and  unsubscribe . 
 
 The  EventEmitter  action doesn't take any arguments. 
 
 The  emit  action takes between either 1 or 2 arguments. The first argument is the name of the event we want to emit, and the 2nd argument is passed to the callback functions. 
 
 The  subscribe  action takes 2 arguments, where the first one is the event name and the second is the callback function. 
 
 The  unsubscribe  action takes one argument, which is the 0-indexed order of the subscription made before.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
class EventEmitter {
  constructor(){this.events=new Map();}
  subscribe(eventName,callback){const list=this.events.get(eventName)||[];list.push(callback);this.events.set(eventName,list);
    return {unsubscribe:()=>{const i=list.indexOf(callback);if(i!==-1)list.splice(i,1);}};
  }
  emit(eventName,args=[]){return (this.events.get(eventName)||[]).map(fn=>fn(...args));}
}
```

---

## 2695. Array Wrapper

**Problem:** https://leetcode.com/problems/array-wrapper/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195491823  
**Language:** javascript

### Description

Create a class  ArrayWrapper  that accepts an array of integers in its constructor. This class should have two features: 
 
 
 When two instances of this class are added together with the  +  operator, the resulting value is the sum of all the elements in both arrays. 
 
 When the  String()  function is called on the instance, it will return a comma separated string surrounded by brackets. For example,  [1,2,3] . 
 
 
   
 
 Example 1: 
 
```text
Input:
 nums = [[1,2],[3,4]], operation = "Add"

Output:
 10

Explanation:

const obj1 = new ArrayWrapper([1,2]);
const obj2 = new ArrayWrapper([3,4]);
obj1 + obj2; // 10
```
 
 
 Example 2: 
 
```text
Input:
 nums = [[23,98,42,70]], operation = "String"

Output:
 "[23,98,42,70]"

Explanation:

const obj = new ArrayWrapper([23,98,42,70]);
String(obj); // "[23,98,42,70]"
```
 
 
 Example 3: 
 
```text
Input:
 nums = [[],[]], operation = "Add"

Output:
 0

Explanation:

const obj1 = new ArrayWrapper([]);
const obj2 = new ArrayWrapper([]);
obj1 + obj2; // 0
```
 
 
   
 
 Constraints: 
 
 
 0 <= nums.length <= 1000 
 
 0 <= nums[i] <= 1000 
 
 Note: nums is the array passed to the constructor

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
class ArrayWrapper {
 constructor(nums){this.nums=nums;}
 valueOf(){return this.nums.reduce((a,b)=>a+b,0);}
 toString(){return '['+this.nums.join(',')+']';}
}
```

---

## 2700. Differences Between Two Objects

**Problem:** https://leetcode.com/problems/differences-between-two-objects/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195491998  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var objDiff = function(obj1,obj2){
 function diff(a,b){if(a===b)return {};if(a===null||b===null||typeof a!=='object'||typeof b!=='object'||Array.isArray(a)!==Array.isArray(b))return [a,b];
   const out={};for(const k of Object.keys(a))if(Object.prototype.hasOwnProperty.call(b,k)){
     const d=diff(a[k],b[k]);if(Array.isArray(d)||Object.keys(d).length)out[k]=d;
   }return out;
 }return diff(obj1,obj2);
};
```

---

## 2703. Return Length of Arguments Passed

**Problem:** https://leetcode.com/problems/return-length-of-arguments-passed/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195492170  
**Language:** javascript

### Description

Write a function  argumentsLength  that returns the count of arguments passed to it.
 
   
 
 Example 1: 
 
```text
Input:
 args = [5]

Output:
 1

Explanation:

argumentsLength(5); // 1

One value was passed to the function so it should return 1.
```
 
 
 Example 2: 
 
```text
Input:
 args = [{}, null, "3"]

Output:
 3

Explanation:
 
argumentsLength({}, null, "3"); // 3

Three values were passed to the function so it should return 3.
```
 
 
   
 
 Constraints: 
 
 
 args  is a valid JSON array 
 
 0 <= args.length <= 100

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var argumentsLength = function(...args){return args.length;};
```

---

## 2704. To Be Or Not To Be

**Problem:** https://leetcode.com/problems/to-be-or-not-to-be/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195492329  
**Language:** javascript

### Description

Write a function  expect  that helps developers test their code. It should take in any value  val  and return an object with the following two functions. 
 
 
 toBe(val)  accepts another value and returns  true  if the two values  ===  each other. If they are not equal, it should throw an error  "Not Equal" . 
 
 notToBe(val)  accepts another value and returns  true  if the two values  !==  each other. If they are equal, it should throw an error  "Equal" . 
 
 
   
 
 Example 1: 
 
```text
Input:
 func = () => expect(5).toBe(5)

Output:
 {"value": true}

Explanation:
 5 === 5 so this expression returns true.
```
 
 
 Example 2: 
 
```text
Input:
 func = () => expect(5).toBe(null)

Output:
 {"error": "Not Equal"}

Explanation:
 5 !== null so this expression throw the error "Not Equal".
```
 
 
 Example 3: 
 
```text
Input:
 func = () => expect(5).notToBe(null)

Output:
 {"value": true}

Explanation:
 5 !== null so this expression returns true.
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var expect = function(val){return {
 toBe:(other)=>{if(val!==other)throw new Error('Not Equal');return true;},
 notToBe:(other)=>{if(val===other)throw new Error('Equal');return true;}
};};
```

---

## 2705. Compact Object

**Problem:** https://leetcode.com/problems/compact-object/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195492498  
**Language:** javascript

### Description

Given an object or array  obj , return a  compact object . 
 
 A  compact object  is the same as the original object, except with keys containing  falsy  values removed. This operation applies to the object and any nested objects. Arrays are considered objects where the indices are keys. A value is considered  falsy  when  Boolean(value)  returns  false . 
 
 You may assume the  obj  is the output of  JSON.parse . In other words, it is valid JSON. 
 
   
 
 Example 1: 
 
```text
Input:
 obj = [null, 0, false, 1]

Output:
 [1]

Explanation:
 All falsy values have been removed from the array.
```
 
 
 Example 2: 
 
```text
Input:
 obj = {"a": null, "b": [false, 1]}

Output:
 {"b": [1]}

Explanation:
 obj["a"] and obj["b"][0] had falsy values and were removed.
```
 
 
 Example 3: 
 
```text
Input:
 obj = [null, 0, 5, [0], [false, 16]]

Output:
 [5, [], [16]]

Explanation:
 obj[0], obj[1], obj[3][0], and obj[4][0] were falsy and removed.
```
 
 
   
 
 Constraints: 
 
 
 obj  is a valid JSON object 
 
 2 <= JSON.stringify(obj).length <= 10 6

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var compactObject = function(obj){
 if(Array.isArray(obj))return obj.filter(Boolean).map(compactObject);
 if(obj!==null&&typeof obj==='object'){
   const out={};for(const [k,v] of Object.entries(obj))if(v)out[k]=compactObject(v);return out;
 }return obj;
};
```

---

## 2715. Timeout Cancellation

**Problem:** https://leetcode.com/problems/timeout-cancellation/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195492659  
**Language:** javascript

### Description

Given a function  fn , an array of arguments  args , and a timeout  t  in milliseconds, return a cancel function  cancelFn . 
 
 After a delay of  cancelTimeMs , the returned cancel function  cancelFn  will be invoked. 
 
```text
setTimeout(cancelFn, cancelTimeMs)
```
 
 
 Initially, the execution of the function  fn  should be delayed by  t  milliseconds. 
 
 If, before the delay of  t  milliseconds, the function  cancelFn  is invoked, it should cancel the delayed execution of  fn . Otherwise, if  cancelFn  is not invoked within the specified delay  t ,  fn  should be executed with the provided  args  as arguments. 
 
   
 
 Example 1: 
 
```text
Input:
 fn = (x) => x * 5, args = [2], t = 20

Output:
 [{"time": 20, "returned": 10}]

Explanation:
 
const cancelTimeMs = 50;
const cancelFn = cancellable((x) => x * 5, [2], 20);
setTimeout(cancelFn, cancelTimeMs);

The cancellation was scheduled to occur after a delay of cancelTimeMs (50ms), which happened after the execution of fn(2) at 20ms.
```
 
 
 Example 2: 
 
```text
Input:
 fn = (x) => x**2, args = [2], t = 100

Output:
 []

Explanation:
 
const cancelTimeMs = 50;
const cancelFn = cancellable((x) => x**2, [2], 100);
setTimeout(cancelFn, cancelTimeMs);

The cancellation was scheduled to occur after a delay of cancelTimeMs (50ms), which happened before the execution of fn(2) at 100ms, resulting in fn(2) never being called.
```
 
 
 Example 3: 
 
```text
Input:
 fn = (x1, x2) => x1 * x2, args = [2,4], t = 30

Output:
 [{"time": 30, "returned": 8}]

Explanation: 

const cancelTimeMs = 100;
const cancelFn = cancellable((x1, x2) => x1 * x2, [2,4], 30);
setTimeout(cancelFn, cancelTimeMs);

The cancellation was scheduled to occur after a delay of cancelTimeMs (100ms), which happened after the execution of fn(2,4) at 30ms.
```
 
 
   
 
 Constraints: 
 
 
 fn  is a function 
 
 args  is a valid JSON array 
 
 1 <= args.length <= 10 
 
 20 <= t <= 1000 
 
 10 <= cancelTimeMs <= 1000

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var cancellable = function(fn,args,t){const id=setTimeout(()=>fn(...args),t);return ()=>clearTimeout(id);};
```

---

## 2721. Execute Asynchronous Functions in Parallel

**Problem:** https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195492850  
**Language:** javascript

### Description

Given an array of asynchronous functions  functions , return a new promise  promise . Each function in the array accepts no arguments and returns a promise. All the promises should be executed in parallel. 
 
 promise  resolves: 
 
 
 When all the promises returned from  functions  were resolved successfully in parallel. The resolved value of  promise  should be an array of all the resolved values of promises in the same order as they were in the  functions . The  promise  should resolve when all the asynchronous functions in the array have completed execution in parallel. 
 
 
 promise  rejects: 
 
 
 When any of the promises returned from  functions  were rejected.  promise  should also reject with the reason of the first rejection. 
 
 
 Please solve it without using the built-in  Promise.all  function. 
 
   
 
 Example 1: 
 
```text
Input:
 functions = [
  () => new Promise(resolve => setTimeout(() => resolve(5), 200))
]

Output:
 {"t": 200, "resolved": [5]}

Explanation:
 
promiseAll(functions).then(console.log); // [5]

The single function was resolved at 200ms with a value of 5.
```
 
 
 Example 2: 
 
```text
Input:
 functions = [
    () => new Promise(resolve => setTimeout(() => resolve(1), 200)), 
    () => new Promise((resolve, reject) => setTimeout(() => reject("Error"), 100))
]

Output:
 {"t": 100, "rejected": "Error"}

Explanation:
 Since one of the promises rejected, the returned promise also rejected with the same error at the same time.
```
 
 
 Example 3: 
 
```text
Input:
 functions = [
    () => new Promise(resolve => setTimeout(() => resolve(4), 50)), 
    () => new Promise(resolve => setTimeout(() => resolve(10), 150)), 
    () => new Promise(resolve => setTimeout(() => resolve(16), 100))
]

Output:
 {"t": 150, "resolved": [4, 10, 16]}

Explanation:
 All the promises resolved with a value. The returned promise resolved when the last promise resolved.
```
 
 
   
 
 Constraints: 
 
 
 functions  is an array of functions that returns promises 
 
 1 <= functions.length <= 10

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var promiseAll = function(functions){return new Promise((resolve,reject)=>{
 const results=Array(functions.length);if(!functions.length){resolve([]);return;}
 let left=functions.length;functions.forEach((fn,i)=>{
  Promise.resolve().then(fn).then(v=>{results[i]=v;if(--left===0)resolve(results);},reject);
 });
});};
```

---

## 2722. Join Two Arrays by ID

**Problem:** https://leetcode.com/problems/join-two-arrays-by-id/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195493063  
**Language:** javascript

### Description

Given two arrays  arr1  and  arr2 , return a new array  joinedArray . All the objects in each of the two inputs arrays will contain an  id  field that has an integer value.  
 
 joinedArray  is an array formed by merging  arr1  and  arr2  based on their  id  key. The length of  joinedArray  should be the length of unique values of  id . The returned array should be sorted in  ascending  order based on the  id  key. 
 
 If a given  id  exists in one array but not the other, the single object with that  id  should be included in the result array without modification. 
 
 If two objects share an  id , their properties should be merged into a single object: 
 
 
 If a key only exists in one object, that single key-value pair should be included in the object. 
 
 If a key is included in both objects, the value in the object from  arr2  should override the value from  arr1 . 
 
 
   
 
 Example 1: 
 
```text
Input:
 
arr1 = [
    {"id": 1, "x": 1},
    {"id": 2, "x": 9}
], 
arr2 = [
    {"id": 3, "x": 5}
]

Output:
 
[
    {"id": 1, "x": 1},
    {"id": 2, "x": 9},
    {"id": 3, "x": 5}
]

Explanation:
 There are no duplicate ids so arr1 is simply concatenated with arr2.
```
 
 
 Example 2: 
 
```text
Input:
 
arr1 = [
    {"id": 1, "x": 2, "y": 3},
    {"id": 2, "x": 3, "y": 6}
], 
arr2 = [
    {"id": 2, "x": 10, "y": 20},
    {"id": 3, "x": 0, "y": 0}
]

Output:
 
[
    {"id": 1, "x": 2, "y": 3},
    {"id": 2, "x": 10, "y": 20},
    {"id": 3, "x": 0, "y": 0}
]

Explanation:
 The two objects with id=1 and id=3 are included in the result array without modifiction. The two objects with id=2 are merged together. The keys from arr2 override the values in arr1.
```
 
 
 Example 3: 
 
```text
Input:
 
arr1 = [
    {"id": 1, "b": {"b": 94},"v": [4, 3], "y": 48}
]
arr2 = [
    {"id": 1, "b": {"c": 84}, "v": [1, 3]}
]

Output:
 [
    {"id": 1, "b": {"c": 84}, "v": [1, 3], "y": 48}
]

Explanation:
 The two objects with id=1 are merged together. For the keys "b" and "v" the values from arr2 are used. Since the key "y" only exists in arr1, that value is taken form arr1.
```
 
 
   
 
 Constraints: 
 
 
 arr1  and  arr2  are valid JSON arrays 
 
 Each object in  arr1  and  arr2  has a unique integer  id  key 
 
 2 <= JSON.stringify(arr1).length <= 10 6 
 
 2 <= JSON.stringify(arr2).length <= 10 6

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var join = function(arr1,arr2){const m=new Map();for(const x of arr1)m.set(x.id,{...x});for(const x of arr2)m.set(x.id,{...(m.get(x.id)||{}),...x});return [...m.values()].sort((a,b)=>a.id-b.id);};
```

---

## 2723. Add Two Promises

**Problem:** https://leetcode.com/problems/add-two-promises/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195493241  
**Language:** javascript

### Description

Given two promises  promise1  and  promise2 , return a new promise.  promise1  and  promise2  will both resolve with a number. The returned promise should resolve with the sum of the two numbers.
 
   
 
 Example 1: 
 
```text
Input:
 
promise1 = new Promise(resolve => setTimeout(() => resolve(2), 20)), 
promise2 = new Promise(resolve => setTimeout(() => resolve(5), 60))

Output:
 7

Explanation:
 The two input promises resolve with the values of 2 and 5 respectively. The returned promise should resolve with a value of 2 + 5 = 7. The time the returned promise resolves is not judged for this problem.
```
 
 
 Example 2: 
 
```text
Input:
 
promise1 = new Promise(resolve => setTimeout(() => resolve(10), 50)), 
promise2 = new Promise(resolve => setTimeout(() => resolve(-12), 30))

Output:
 -2

Explanation:
 The two input promises resolve with the values of 10 and -12 respectively. The returned promise should resolve with a value of 10 + -12 = -2.
```
 
 
   
 
 Constraints: 
 
 
 promise1  and  promise2  are promises that resolve with a number

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var addTwoPromises = async function(promise1,promise2){const [a,b]=await Promise.all([promise1,promise2]);return a+b;};
```

---

## 2724. Sort By

**Problem:** https://leetcode.com/problems/sort-by/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195493401  
**Language:** javascript

### Description

Given an array  arr  and a function  fn , return a sorted array  sortedArr . You can assume  fn  only returns numbers and those numbers determine the sort order of  sortedArr .  sortedArr  must be sorted in  ascending order  by  fn  output. 
 
 You may assume that  fn  will never duplicate numbers for a given array. 
 
   
 
 Example 1: 
 
```text
Input:
 arr = [5, 4, 1, 2, 3], fn = (x) => x

Output:
 [1, 2, 3, 4, 5]

Explanation:
 fn simply returns the number passed to it so the array is sorted in ascending order.
```
 
 
 Example 2: 
 
```text
Input:
 arr = [{"x": 1}, {"x": 0}, {"x": -1}], fn = (d) => d.x

Output:
 [{"x": -1}, {"x": 0}, {"x": 1}]

Explanation:
 fn returns the value for the "x" key. So the array is sorted based on that value.
```
 
 
 Example 3: 
 
```text
Input:
 arr = [[3, 4], [5, 2], [10, 1]], fn = (x) => x[1]

Output:
 [[10, 1], [5, 2], [3, 4]]

Explanation:
 arr is sorted in ascending order by number at index=1.
```
 
 
   
 
 Constraints: 
 
 
 arr  is a valid JSON array 
 
 fn  is a function that returns a number 
 
 1 <= arr.length <= 5 * 10 5

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var sortBy = function(arr,fn){return arr.sort((a,b)=>fn(a)-fn(b));};
```

---

## 2725. Interval Cancellation

**Problem:** https://leetcode.com/problems/interval-cancellation/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195493576  
**Language:** javascript

### Description

Given a function  fn , an array of arguments  args , and an interval time  t , return a cancel function  cancelFn . 
 
 After a delay of  cancelTimeMs , the returned cancel function  cancelFn  will be invoked. 
 
```text
setTimeout(cancelFn, cancelTimeMs)
```
 
 
 The function  fn  should be called with  args  immediately and then called again every  t  milliseconds until  cancelFn  is called at  cancelTimeMs  ms. 
 
   
 
 Example 1: 
 
```text
Input:
 fn = (x) => x * 2, args = [4], t = 35

Output:
 
[
   {"time": 0, "returned": 8},
   {"time": 35, "returned": 8},
   {"time": 70, "returned": 8},
   {"time": 105, "returned": 8},
   {"time": 140, "returned": 8},
   {"time": 175, "returned": 8}
]

Explanation:
 
const cancelTimeMs = 190;
const cancelFn = cancellable((x) => x * 2, [4], 35);
setTimeout(cancelFn, cancelTimeMs);

Every 35ms, fn(4) is called. Until t=190ms, then it is cancelled.
1st fn call is at 0ms. fn(4) returns 8.
2nd fn call is at 35ms. fn(4) returns 8.
3rd fn call is at 70ms. fn(4) returns 8.
4th fn call is at 105ms. fn(4) returns 8.
5th fn call is at 140ms. fn(4) returns 8.
6th fn call is at 175ms. fn(4) returns 8.
Cancelled at 190ms
```
 
 
 Example 2: 
 
```text
Input:
 fn = (x1, x2) => (x1 * x2), args = [2, 5], t = 30

Output:
 
[
   {"time": 0, "returned": 10},
   {"time": 30, "returned": 10},
   {"time": 60, "returned": 10},
   {"time": 90, "returned": 10},
   {"time": 120, "returned": 10},
   {"time": 150, "returned": 10}
]

Explanation:
 
const cancelTimeMs = 165; 
const cancelFn = cancellable((x1, x2) => (x1 * x2), [2, 5], 30) 
setTimeout(cancelFn, cancelTimeMs)

Every 30ms, fn(2, 5) is called. Until t=165ms, then it is cancelled.
1st fn call is at 0ms 
2nd fn call is at 30ms 
3rd fn call is at 60ms 
4th fn call is at 90ms 
5th fn call is at 120ms 
6th fn call is at 150ms
Cancelled at 165ms
```
 
 
 Example 3: 
 
```text
Input:
 fn = (x1, x2, x3) => (x1 + x2 + x3), args = [5, 1, 3], t = 50

Output:
 
[
   {"time": 0, "returned": 9},
   {"time": 50, "returned": 9},
   {"time": 100, "returned": 9},
   {"time": 150, "returned": 9}
]

Explanation:
 
const cancelTimeMs = 180;
const cancelFn = cancellable((x1, x2, x3) => (x1 + x2 + x3), [5, 1, 3], 50)
setTimeout(cancelFn, cancelTimeMs)

Every 50ms, fn(5, 1, 3) is called. Until t=180ms, then it is cancelled. 
1st fn call is at 0ms
2nd fn call is at 50ms
3rd fn call is at 100ms
4th fn call is at 150ms
Cancelled at 180ms
```
 
 
   
 
 Constraints: 
 
 
 fn  is a function 
 
 args  is a valid JSON array 
 
 1 <= args.length <= 10 
 
 30 <= t <= 100 
 
 10 <=  cancelTimeMs  <= 500

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var cancellable = function(fn,args,t){fn(...args);const id=setInterval(()=>fn(...args),t);return ()=>clearInterval(id);};
```

---

## 2726. Calculator with Method Chaining

**Problem:** https://leetcode.com/problems/calculator-with-method-chaining/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195493822  
**Language:** javascript

### Description

Design a  Calculator  class. The class should provide the mathematical operations of addition, subtraction, multiplication, division, and exponentiation. It should also allow consecutive operations to be performed using method chaining. The  Calculator  class constructor should accept a number which serves as the initial value of  result . 
 
 Your  Calculator   class should have the following methods: 
 
 
 add  - This method adds the given number  value  to the  result  and returns the updated  Calculator . 
 
 subtract  - This method subtracts the given number  value  from the  result  and returns the updated  Calculator . 
 
 multiply  - This method multiplies the  result   by the given number  value  and returns the updated  Calculator . 
 
 divide  - This method divides the  result  by the given number  value  and returns the updated  Calculator . If the passed value is  0 , an error  "Division by zero is not allowed"  should be thrown. 
 
 power  - This method raises the  result  to the power of the given number  value  and returns the updated  Calculator . 
 
 getResult  - This method returns the  result . 
 
 
 Solutions within  10 -5  of the actual result are considered correct. 
 
   
 
 Example 1: 
 
```text
Input:
 
actions = ["Calculator", "add", "subtract", "getResult"], 
values = [10, 5, 7]

Output:
 8

Explanation:
 
new Calculator(10).add(5).subtract(7).getResult() // 10 + 5 - 7 = 8
```
 
 
 Example 2: 
 
```text
Input:
 
actions = ["Calculator", "multiply", "power", "getResult"], 
values = [2, 5, 2]

Output:
 100

Explanation:
 
new Calculator(2).multiply(5).power(2).getResult() // (2 * 5) ^ 2 = 100
```
 
 
 Example 3: 
 
```text
Input:
 
actions = ["Calculator", "divide", "getResult"], 
values = [20, 0]

Output:
 "Division by zero is not allowed"

Explanation:
 
new Calculator(20).divide(0).getResult() // 20 / 0 

The error should be thrown because we cannot divide by zero.
```
 
 
   
 
 Constraints: 
 
 
 actions  is a valid JSON array of strings 
 
 values  is a valid JSON array of numbers 
 
 2 <= actions.length <= 2 * 10 4 
 
 1 <= values.length <= 2 * 10 4  - 1 
 
 actions[i]  is one of "Calculator", "add", "subtract", "multiply", "divide", "power", and "getResult" 
 
 First action is always "Calculator" 
 
 Last action is always "getResult"

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
class Calculator {
 constructor(value){this.value=value;}
 add(value){this.value+=value;return this;}
 subtract(value){this.value-=value;return this;}
 multiply(value){this.value*=value;return this;}
 divide(value){if(value===0)throw new Error('Division by zero is not allowed');this.value/=value;return this;}
 power(value){this.value**=value;return this;}
 getResult(){return this.value;}
}
```

---

## 2727. Is Object Empty

**Problem:** https://leetcode.com/problems/is-object-empty/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195494000  
**Language:** javascript

### Description

Given an object or an array, return if it is empty. 
 
 
 An empty object contains no key-value pairs. 
 
 An empty array contains no elements. 
 
 
 You may assume the object or array is the output of  JSON.parse . 
 
   
 
 Example 1: 
 
```text
Input:
 obj = {"x": 5, "y": 42}

Output:
 false

Explanation:
 The object has 2 key-value pairs so it is not empty.
```
 
 
 Example 2: 
 
```text
Input:
 obj = {}

Output:
 true

Explanation:
 The object doesn't have any key-value pairs so it is empty.
```
 
 
 Example 3: 
 
```text
Input:
 obj = [null, false, 0]

Output:
 false

Explanation:
 The array has 3 elements so it is not empty.
```
 
 
   
 
 Constraints: 
 
 
 obj  is a valid JSON object or array 
 
 2 <= JSON.stringify(obj).length <= 10 5 
 
 
   
 Can you solve it in O(1) time?

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var isEmpty = function(obj){return Object.keys(obj).length===0;};
```

---

## 2754. Bind Function to Context

**Problem:** https://leetcode.com/problems/bind-function-to-context/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195494354  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
Function.prototype.bindPolyfill = function(obj,...args){const fn=this;return function(...more){return fn.apply(obj,[...args,...more]);};};
```

---

## 2755. Deep Merge of Two Objects

**Problem:** https://leetcode.com/problems/deep-merge-of-two-objects/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195494533  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var deepMerge = function(obj1,obj2){
 if(obj1===null||obj2===null||typeof obj1!=='object'||typeof obj2!=='object'||Array.isArray(obj1)!==Array.isArray(obj2))return obj2;
 const out=Array.isArray(obj1)?obj1.slice():{...obj1};
 for(const k of Object.keys(obj2))out[k]=Object.prototype.hasOwnProperty.call(obj1,k)?deepMerge(obj1[k],obj2[k]):obj2[k];
 return out;
};
```

---

## 2756. Query Batching

**Problem:** https://leetcode.com/problems/query-batching/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195610594  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/**
 * @param {Function} queryMultiple
 * @param {number} t
 * @return {void}
 */

/**
 * @param {Function} queryMultiple
 * @param {number} t
 */
var QueryBatcher = function(queryMultiple, t) {
    this.queryMultiple = queryMultiple;
    this.t = t;
    this.waiting = false;
    this.queue = [];
};

/**
 * @param {string} key
 * @return {Promise<string>}
 */
QueryBatcher.prototype.getValue = function(key) {
    return new Promise((resolve) => {
        this.queue.push({ key, resolve });

        if (!this.waiting) {
            this.execute();
        }
    });
};

QueryBatcher.prototype.execute = function() {
    if (this.queue.length === 0) {
        this.waiting = false;
        return;
    }

    this.waiting = true;

    const batch = this.queue;
    this.queue = [];

    const keys = batch.map(item => item.key);

    this.queryMultiple(keys).then(results => {
        batch.forEach((item, i) => {
            item.resolve(results[i]);
        });
    });

    setTimeout(() => {
        this.execute();
    }, this.t);
};


/**
 * async function queryMultiple(keys) { 
 *   return keys.map(key => key + '!');
 * }
 *
 * const batcher = new QueryBatcher(queryMultiple, 100);
 * batcher.getValue('a').then(console.log); // resolves "a!" at t=0ms 
 * batcher.getValue('b').then(console.log); // resolves "b!" at t=100ms 
 * batcher.getValue('c').then(console.log); // resolves "c!" at t=100ms 
 */
```

---

## 2757. Generate Circular Array Values

**Problem:** https://leetcode.com/problems/generate-circular-array-values/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195494693  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var cycleGenerator = function*(arr,startIndex){let i=startIndex;while(true){const jump=yield arr[i];i=((i+(jump??0))%arr.length+arr.length)%arr.length;}};
```

---

## 2758. Next Day

**Problem:** https://leetcode.com/problems/next-day/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195494863  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
Date.prototype.nextDay = function(){const d=new Date(this.valueOf());d.setUTCDate(d.getUTCDate()+1);return d.toISOString().slice(0,10);};
```

---

## 2759. Convert JSON String to Object

**Problem:** https://leetcode.com/problems/convert-json-string-to-object/

**Difficulty:** Hard  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195495046  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var jsonParse = function(str){return JSON.parse(str);};
```

---

## 2774. Array Upper Bound

**Problem:** https://leetcode.com/problems/array-upper-bound/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195495225  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
Array.prototype.upperBound = function(target){let l=0,r=this.length;while(l<r){const m=l+Math.floor((r-l)/2);if(this[m]<=target)l=m+1;else r=m;}return l>0 && this[l-1]===target?l-1:-1;};
```

---

## 2775. Undefined to Null

**Problem:** https://leetcode.com/problems/undefined-to-null/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195495416  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
var undefinedToNull = function(obj){if(obj===undefined)return null;if(Array.isArray(obj))return obj.map(undefinedToNull);if(obj&&typeof obj==='object'){for(const k of Object.keys(obj))obj[k]=undefinedToNull(obj[k]);}return obj;};
```

---

## 2776. Convert Callback Based Function to Promise Based Function

**Problem:** https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195610775  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/**
 * @param {Function} fn
 * @return {Function<Promise<number>>}
 */

/**
 * @param {Function} fn
 * @return {Function}
 */
var promisify = function(fn) {
    return function(...args) {
        return new Promise((resolve, reject) => {
            fn((result, error) => {
                if (error) {
                    reject(error);
                } else {
                    resolve(result);
                }
            }, ...args);
        });
    };
};


/**
 * const asyncFunc = promisify(callback => callback(42));
 * asyncFunc().then(console.log); // 42
 */
```

---

## 2777. Date Range Generator

**Problem:** https://leetcode.com/problems/date-range-generator/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195496838  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/**
 * @param {string} start
 * @param {string} end
 * @param {number} step
 * @return {Generator<string>}
 */
var dateRangeGenerator = function* (start, end, step) {
    let day = Date.parse(start);
    const last = Date.parse(end);
    const increment = step * 86400000;
    while (day <= last) {
        yield new Date(day).toISOString().slice(0, 10);
        day += increment;
    }
};
```

---

## 2794. Create Object from Two Arrays

**Problem:** https://leetcode.com/problems/create-object-from-two-arrays/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195497177  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/** @param {Array} keysArr @param {Array} valuesArr @return {Object} */
var createObject = function(keysArr, valuesArr) {
    const obj = Object.create(null);
    for (let i = 0; i < keysArr.length; i++) {
        const key = String(keysArr[i]);
        if (!Object.hasOwn(obj, key)) obj[key] = valuesArr[i];
    }
    return obj;
};
```

---

## 2795. Parallel Execution of Promises for Individual Results Retrieval

**Problem:** https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195497331  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/** @param {Function[]} functions @return {Promise} */
var promiseAllSettled = async function(functions) {
    return Promise.allSettled(functions.map(fn => Promise.resolve().then(fn)));
};
```

---

## 2796. Repeat String

**Problem:** https://leetcode.com/problems/repeat-string/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195497515  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
String.prototype.replicate = function(times) {
    let result = '', block = String(this);
    while (times > 0) {
        if (times % 2 === 1) result += block;
        times = Math.floor(times / 2);
        if (times > 0) block += block;
    }
    return result;
};
```

---

## 2797. Partial Function with Placeholders

**Problem:** https://leetcode.com/problems/partial-function-with-placeholders/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195497692  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/** @param {Function} fn @param {any[]} args @return {Function} */
var partial = function(fn, args) {
    return function(...restArgs) {
        let j = 0;
        const result = args.map(x => x === '_' ? restArgs[j++] : x);
        return fn(...result, ...restArgs.slice(j));
    };
};
```

---

## 2803. Factorial Generator

**Problem:** https://leetcode.com/problems/factorial-generator/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195610947  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/**
 * @param {number} n
 * @yields {number}
 */

/**
 * @param {number} n
 * @yields {number}
 */
var factorial = function* (n) {
    let result = 1;

    if (n === 0) {
        yield 1;
        return;
    }

    for (let i = 1; i <= n; i++) {
        result *= i;
        yield result;
    }
};

/**
 * const gen = factorial(2);
 * gen.next().value; // 1
 * gen.next().value; // 2
 */
```

---

## 2804. Array Prototype ForEach

**Problem:** https://leetcode.com/problems/array-prototype-foreach/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195499100  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
Array.prototype.forEach = function(callback, context) {
    for (let i = 0; i < this.length; i++) {
        if (i in this) callback.call(context, this[i], i, this);
    }
};
```

---

## 2805. Custom Interval

**Problem:** https://leetcode.com/problems/custom-interval/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195499265  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
const activeIntervals = new Map();
let nextIntervalId = 1;
function customInterval(fn, delay, period) {
    const id = nextIntervalId++;
    let count = 0;
    function run() {
        if (!activeIntervals.has(id)) return;
        fn();
        if (!activeIntervals.has(id)) return;
        count++;
        activeIntervals.set(id, setTimeout(run, delay + period * count));
    }
    activeIntervals.set(id, setTimeout(run, delay));
    return id;
}
function customClearInterval(id) {
    clearTimeout(activeIntervals.get(id));
    activeIntervals.delete(id);
}
```

---

## 2821. Delay the Resolution of Each Promise

**Problem:** https://leetcode.com/problems/delay-the-resolution-of-each-promise/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195500626  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/** @param {Function[]} functions @param {number} ms @return {Function[]} */
var delayAll = function(functions, ms) {
    return functions.map(fn => (...args) =>
        Promise.resolve().then(() => fn(...args)).then(
            value => new Promise(resolve => setTimeout(() => resolve(value), ms)),
            error => new Promise((_, reject) => setTimeout(() => reject(error), ms))
        )
    );
};
```

---

## 2822. Inversion of Object

**Problem:** https://leetcode.com/problems/inversion-of-object/

**Difficulty:** Easy  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195500822  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/** @param {Object|Array} obj @return {Object} */
var invertObject = function(obj) {
    const out = {};
    for (const [key, value] of Object.entries(obj)) {
        const v = String(value);
        if (!Object.prototype.hasOwnProperty.call(out, v)) out[v] = key;
        else if (Array.isArray(out[v])) out[v].push(key);
        else out[v] = [out[v], key];
    }
    return out;
};
```

---

## 2823. Deep Object Filter

**Problem:** https://leetcode.com/problems/deep-object-filter/

**Difficulty:** Medium  
**Premium:** Yes  
**Tags:** Unknown  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2195611232  
**Language:** javascript

### Description

_Description not available through the current account/session._

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```javascript
/**
 * @param {Object|Array} obj
 * @param {Function} fn
 * @return {Object|Array|undefined}
 */

/**
 * @param {Object|Array} obj
 * @param {Function} fn
 * @return {Object|Array|undefined}
 */
var deepFilter = function(obj, fn) {
    if (obj === null || typeof obj !== "object") {
        return fn(obj) ? obj : undefined;
    }

    if (Array.isArray(obj)) {
        const result = [];

        for (const value of obj) {
            const filtered = deepFilter(value, fn);

            if (filtered !== undefined) {
                result.push(filtered);
            }
        }

        return result.length > 0 ? result : undefined;
    }

    const result = {};

    for (const key of Object.keys(obj)) {
        const filtered = deepFilter(obj[key], fn);

        if (filtered !== undefined) {
            result[key] = filtered;
        }
    }

    return Object.keys(result).length > 0
        ? result
        : undefined;
};
```

---
