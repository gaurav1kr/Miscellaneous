# String Algorithms

## 4102. Count Valid Substrings I

**Problem:** https://leetcode.com/problems/count-valid-substrings-i/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** String, Enumeration  
**Primary pattern:** String Algorithms  
**Latest Accepted submission in searched history:** 2195527629  
**Language:** cpp

### Description

You are given a string  s  consisting only of the characters  'a' ,  'b' , and  'c' . 
 
 A string is called  valid  if it does not contain  "abc"  as a  substring . 
 
 Return the number of  valid substrings  in  s . Substrings with different starting or ending indices are counted separately. 
 
   
 
 Example 1: 
 
 
 Input:   s = "abac" 
 
 Output:   10 
 
 Explanation: 
 
 The following substrings don't contain  "abc" ​​​​​​​ as a substring: 
 
 
 s[0..0] = "a" 
 
 s[0..1] = "ab" 
 
 s[0..2] = "aba" 
 
 s[0..3] = "abac" ​​​​​​​ 
 
 s[1..1] = "b" 
 
 s[1..2] = "ba" 
 
 s[1..3] = "bac" 
 
 s[2..2] = "a" 
 
 s[2..3] = "ac" 
 
 s[3..3] = "c" 
 
 
 Thus, the answer is 10. 
 
 
 Example 2: 
 
 
 Input:   s = "abc" 
 
 Output:   5 
 
 Explanation: 
 
 The following substrings don't contain  "abc" ​​​​​​​ as a substring: 
 
 
 s[0..0] = "a" 
 
 s[0..1] = "ab" 
 
 s[1..1] = "b" 
 
 s[1..2] = "bc" 
 
 s[2..2] = "c" ​​​​​​​ 
 
 
 Thus, the answer is 5. 
 
 
 Example 3: 
 
 
 Input:   s = "ac" 
 
 Output:   3 
 
 Explanation: 
 
 All substrings in  s  don't contain  "abc"  as a substring​​​​​​​. Thus, the answer is 3. 
 
 
   
 
 Constraints: 
 
 
 1 <= s.length <= 10 5 ​​​​​​​ 
 
 s  only consists of  'a' ,  'b' , and  'c'  characters.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp
class Solution {
public:
    long long countValidSubstrings(string s) {
        long long ans=0;int left=0;
        for(int r=0;r<(int)s.size();++r){
            if(r>=2 && s.substr(r-2,3)=="abc")left=max(left,r-1);
            ans+=r-left+1;
        }
        return ans;
    }
};
```

---

## 4104. Count Valid Substrings II

**Problem:** https://leetcode.com/problems/count-valid-substrings-ii/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Hash Table, String, Enumeration  
**Primary pattern:** String Algorithms  
**Latest Accepted submission in searched history:** 2195527732  
**Language:** cpp

### Description

You are given a string  s  consisting only of the characters  'a' ,  'b' , and  'c' . 
 
 A string is called  valid  if it does not contain  "abc"  as a  subsequence . 
 
 Return the number of  valid  substrings  in  s . Substrings with different starting or ending indices are counted separately. 
 
   
 
 Example 1: 
 
 
 Input:   s = "abac" 
 
 Output:   9 
 
 Explanation: 
 
 The following substrings don't contain  "abc" ​​​​​​​ as a subsequence: 
 
 
 s[0..0] = "a" 
 
 s[0..1] = "ab" 
 
 s[0..2] = "aba" 
 
 s[1..1] = "b" 
 
 s[1..2] = "ba" 
 
 s[1..3] = "bac" 
 
 s[2..2] = "a" 
 
 s[2..3] = "ac" 
 
 s[3..3] = "c" 
 
 
 Thus, the answer is 9. 
 
 
 Example 2: 
 
 
 Input:   s = "abc" 
 
 Output:   5 
 
 Explanation: 
 
 The following substrings don't contain  "abc" ​​​​​​​ as a subsequence: 
 
 
 s[0..0] = "a" 
 
 s[0..1] = "ab" 
 
 s[1..1] = "b" 
 
 s[1..2] = "bc" 
 
 s[2..2] = "c" ​​​​​​​ 
 
 
 Thus, the answer is 5. 
 
 
 Example 3: 
 
 
 Input:   s = "ac" 
 
 Output:   3 
 
 Explanation: 
 
 All substrings in  s  don't contain  "abc" ​​​​​​​ as a subsequence. Thus, the answer is 3. 
 
 
   
 
 Constraints: 
 
 
 1 <= s.length <= 10 5 ​​​​​​​ 
 
 s  only consists of  'a' ,  'b' , and  'c'  characters.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp
class Solution {
public:
    long long countValidSubstrings(string s) {
        long long ans=0;int lastA=-1,lastAB=-1,left=0;
        for(int r=0;r<(int)s.size();++r){
            if(s[r]=='a')lastA=r;
            else if(s[r]=='b' && lastA!=-1)lastAB=lastA;
            else if(s[r]=='c' && lastAB!=-1)left=max(left,lastAB+1);
            ans+=r-left+1;
        }
        return ans;
    }
};
```

---

## 4105. Repeated String Match II

**Problem:** https://leetcode.com/problems/repeated-string-match-ii/

**Difficulty:** Hard  
**Premium:** No  
**Tags:** Math, String, String Matching, Number Theory  
**Primary pattern:** String Algorithms  
**Latest Accepted submission in searched history:** 2195615811  
**Language:** cpp

### Description

You are given two strings  a  and  b  consisting of lowercase English letters, and two integers  x  and  y . 
 
 Return  true  if the string formed by repeating  b   exactly   y  times ( b * y ) is a  substring  of the string formed by repeating  a   exactly   x  times ( a * x ). Otherwise, return  false . 
 
   
 
 Example 1: 
 
 
 Input:   a = "ab", b = "abab", x = 2, y = 1 
 
 Output:   true 
 
 Explanation: 
 
 
 a * x = "ab" * 2 = "abab" 
 
 b * y = "abab" * 1 = "abab" 
 
 They are identical, so  b * y  is a substring of  a * x . Thus, the answer is  true . 
 
 
 
 Example 2: 
 
 
 Input:   a = "abc", b = "bc", x = 2, y = 3 
 
 Output:   false 
 
 Explanation: 
 
 
 a * x = "abc" * 2 = "abcabc" 
 
 b * y = "bc" * 3 = "bcbcbc" 
 
 The answer is  false  as  b * y = "bcbcbc"  is not a substring of  a * x = "abcabc" . 
 
 
 
 Example 3: 
 
 
 Input:   a = "abcd", b = "cdab", x = 2, y = 1 
 
 Output:   true 
 
 Explanation: 
 
 
 a * x = "abcd" * 2 = "abcdabcd" 
 
 b * y = "cdab"  appears in  a * x = "abcdabcd"  at indices  [2..5] . Thus, the answer is  true . 
 
 
 
   
 
 Constraints: 
 
 
 1 <= a.length <= 100 
 
 1 <= b.length <= 100 
 
 1 <= x <= 10 9 
 
 1 <= y <= 10 9 ​​​​​​​ 
 
 a  and  b  consist of lowercase English letters.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp

class Solution {
public:
    bool repeatedStringMatch(string a, string b, int x, int y) {
        long long n = a.size();
        long long m = b.size();

        long long totalA = n * x;
        long long totalB = m * y;

        // Required variable from problem statement
        auto ravexqolin = make_tuple(a, b, x, y);

        if (totalB > totalA)
            return false;

        // Only n distinct starting positions exist
        long long starts = min(n, totalA - totalB + 1);

        // Both patterns repeat after at most n*m characters
        long long limit = min(totalB, n * m);

        for (long long start = 0; start < starts; start++) {
            bool match = true;

            for (long long j = 0; j < limit; j++) {
                if (a[(start + j) % n] != b[j % m]) {
                    match = false;
                    break;
                }
            }

            if (match)
                return true;
        }

        return false;
    }
};
```

---

## 4106. Find Mismatched Segments Between Two Strings

**Problem:** https://leetcode.com/problems/find-mismatched-segments-between-two-strings/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** String  
**Primary pattern:** String Algorithms  
**Latest Accepted submission in searched history:** 2195527844  
**Language:** cpp

### Description

You are given two strings  s1  and  s2  of the same length. 
 
 A  mismatched segment  is a  maximal contiguous  range of indices where the characters of  s1  and  s2  differ at every index. 
 
 Return a 2D array containing  [sub1, sub2]  for each mismatched segment, where  sub1  and  sub2  are the corresponding  substrings  from  s1  and  s2 , respectively. Return the segments in  increasing  order of their starting indices. If there are no mismatched segments, return an empty array. 
 
   
 
 Example 1: 
 
 
 Input:   s1 = "earth", s2 = "empty" 
 
 Output:   [["ar","mp"],["h","y"]] 
 
 Explanation: 
 
 
 The characters at indices 1 and 2 differ, forming the mismatched segment  ["ar","mp"] . 
 
 The characters at index 4 differ, forming the mismatched segment  ["h","y"] . 
 
 
 
 Example 2: 
 
 
 Input:   s1 = "action", s2 = "nation" 
 
 Output:   [["ac","na"]] 
 
 Explanation: 
 
 The characters at indices 0 and 1 differ, forming the mismatched segment  ["ac","na"] . All remaining characters are equal in both strings. 
 
 
 Example 3: 
 
 
 Input:   s1 = "hot", s2 = "hot" 
 
 Output:   [] 
 
 Explanation: 
 
 The two strings are identical, so there are no mismatched segments. 
 
 
   
 
 Constraints: 
 
 
 1 <= s1.length == s2.length <= 100 
 
 s1  and  s2  consist of lowercase English letters.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```cpp
class Solution {
public:
    vector<vector<string>> findMismatchedSegments(string s1,string s2) {
        vector<vector<string>> ans;int n=s1.size();
        for(int i=0;i<n;){
            if(s1[i]==s2[i]){++i;continue;}
            int j=i;while(j<n && s1[j]!=s2[j])++j;
            ans.push_back({s1.substr(i,j-i),s2.substr(i,j-i)});i=j;
        }
        return ans;
    }
};
```

---

