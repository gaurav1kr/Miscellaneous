# Shell Scripting

## 192. Word Frequency

**Problem:** https://leetcode.com/problems/word-frequency/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Shell  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187254818  
**Language:** bash

### Description

Write a bash script to calculate the  frequency  of each word in a text file  words.txt . 
 
 For simplicity sake, you may assume: 
 
 
 words.txt  contains only lowercase characters and space  ' '  characters. 
 
 Each word must consist of lowercase characters only. 
 
 Words are separated by one or more whitespace characters. 
 
 
 Example: 
 
 Assume that  words.txt  has the following content: 
 
```text
the day is sunny the the
the sunny is is
```
 
 
 Your script should output the following, sorted by descending frequency: 
 
```text
the 4
is 3
sunny 2
day 1
```
 
 
 Note: 
 
 
 Don't worry about handling ties, it is guaranteed that each word's frequency count is unique. 
 
 Could you write it in one-line using  Unix pipes ?

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```bash
tr -s '[:space:]' '\n' < words.txt | grep -v '^$' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
```

---

## 193. Valid Phone Numbers

**Problem:** https://leetcode.com/problems/valid-phone-numbers/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Shell  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187254893  
**Language:** bash

### Description

Given a text file  file.txt  that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers. 
 
 You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit) 
 
 You may also assume each line in the text file must not contain leading or trailing white spaces. 
 
 Example: 
 
 Assume that  file.txt  has the following content: 
 
```text
987-123-4567
123 456 7890
(123) 456-7890
```
 
 
 Your script should output the following valid phone numbers: 
 
```text
987-123-4567
(123) 456-7890
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```bash
grep -E '^([0-9]{3}-[0-9]{3}-[0-9]{4}|\([0-9]{3}\) [0-9]{3}-[0-9]{4})$' file.txt
```

---

## 194. Transpose File

**Problem:** https://leetcode.com/problems/transpose-file/

**Difficulty:** Medium  
**Premium:** No  
**Tags:** Shell  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187254978  
**Language:** bash

### Description

Given a text file  file.txt , transpose its content. 
 
 You may assume that each row has the same number of columns, and each field is separated by the  ' '  character. 
 
 Example: 
 
 If  file.txt  has the following content: 
 
```text
name age
alice 21
ryan 30
```
 
 
 Output the following: 
 
```text
name alice ryan
age 21 30
```

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```bash
awk '{ for (i = 1; i <= NF; i++) { if (NR == 1) col[i] = $i; else col[i] = col[i] " " $i } } END { for (i = 1; i <= NF; i++) print col[i] }' file.txt
```

---

## 195. Tenth Line

**Problem:** https://leetcode.com/problems/tenth-line/

**Difficulty:** Easy  
**Premium:** No  
**Tags:** Shell  
**Primary pattern:** Other Unclassified  
**Latest Accepted submission in searched history:** 2187255048  
**Language:** bash

### Description

Given a text file  file.txt , print just the 10th line of the file. 
 
 Example: 
 
 Assume that  file.txt  has the following content: 
 
```text
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
```
 
 
 Your script should output the tenth line, which is: 
 
```text
Line 10
```
 
 Note: 
1. If the file contains less than 10 lines, what should you output? 
2. There's at least three different solutions. Try to explore all possibilities.

### Approach

_To be analyzed against the submitted code; not automatically verified._

**Time complexity:** _Pending code analysis_  
**Space complexity:** _Pending code analysis_

### Submitted solution

```bash
sed -n '10p' file.txt
```

---
