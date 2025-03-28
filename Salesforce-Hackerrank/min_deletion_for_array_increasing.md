# Minimum Deletions to Make the Array Almost Increasing

## Problem Statement
Given an array of integers, your task is to determine the minimum number of deletions required so that the remaining elements form an **almost** strictly increasing subsequence.

An **almost strictly increasing subsequence** is defined as a sequence where the number of elements in the **longest increasing subsequence (LIS)** is maximized, but at least one element must be deleted from the original array.

### Function Signature
```cpp
int minDeletions(vector<int>& arr);
```

## Input Format
- The first line contains an integer **N** (1 \leq N \leq 10⁵), the number of elements in the array.
- The second line contains **N** space-separated integers **arr[i]** (-10⁹ \leq arr[i] \leq 10⁹).

## Output Format
- Print a single integer representing the minimum number of deletions required.

## Constraints
- 1 \leq N \leq 10⁵
- -10⁹ \leq arr[i] \leq 10⁹

## Example 1
### Input
```
6  
5 2 8 6 3 6  
```
### Output
```
3
```
### Explanation
The **longest increasing subsequence (LIS)** is **[2, 3, 6]** (length = 3).  
To achieve this, we must delete **{5, 8, 6}** (3 deletions).  
Since at least one deletion is required, the answer is **3**.

## Example 2
### Input
```
5  
1 2 3 4 5  
```
### Output
```
0
```
### Explanation
The LIS is **[1, 2, 3, 4, 5]**, and since at least one deletion is required, we remove one element.  
However, the function logic ensures a minimum of 0 deletions, so the output is **0**.

---

## Solution in C++
```cpp
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

int minDeletions(vector<int>& arr) {
    int n = arr.size();
    vector<int> lis;
    
    for (int num : arr) {
        auto it = lower_bound(lis.begin(), lis.end(), num);
        if (it == lis.end()) {
            lis.push_back(num);
        } else {
            *it = num;
        }
    }
    
    int longestIncreasingSubseq = lis.size();
    return max(0, n - longestIncreasingSubseq - 1);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string arr_count_temp;
    getline(cin, arr_count_temp);

    int arr_count = stoi(ltrim(rtrim(arr_count_temp)));

    vector<int> arr(arr_count);

    for (int i = 0; i < arr_count; i++) {
        string arr_item_temp;
        getline(cin, arr_item_temp);

        int arr_item = stoi(ltrim(rtrim(arr_item_temp)));

        arr[i] = arr_item;
    }

    int result = minDeletions(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);
    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );
    return s;
}

string rtrim(const string &str) {
    string s(str);
    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );
    return s;
}
```
