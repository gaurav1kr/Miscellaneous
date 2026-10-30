# String Algorithms

**Problems:** 219

## Quick revision checklist

Prefix/suffix structure, substring matching, or character constraints.

## Problem index

- [6. Zigzag Conversion](#6-zigzag-conversion) — Medium; code: yes
- [8. String to Integer (atoi)](#8-string-to-integer-atoi) — Medium; code: yes
- [20. Valid Parentheses](#20-valid-parentheses) — Easy; code: yes
- [38. Count and Say](#38-count-and-say) — Medium; code: yes
- [43. Multiply Strings](#43-multiply-strings) — Medium; code: yes
- [58. Length of Last Word](#58-length-of-last-word) — Easy; code: yes
- [65. Valid Number](#65-valid-number) — Hard; code: yes
- [67. Add Binary](#67-add-binary) — Easy; code: yes
- [68. Text Justification](#68-text-justification) — Hard; code: yes
- [71. Simplify Path](#71-simplify-path) — Medium; code: yes
- [168. Excel Sheet Column Title](#168-excel-sheet-column-title) — Easy; code: yes
- [171. Excel Sheet Column Number](#171-excel-sheet-column-number) — Easy; code: yes
- [224. Basic Calculator](#224-basic-calculator) — Hard; code: yes
- [227. Basic Calculator II](#227-basic-calculator-ii) — Medium; code: yes
- [243. Shortest Word Distance](#243-shortest-word-distance) — Easy; code: yes
- [245. Shortest Word Distance III](#245-shortest-word-distance-iii) — Medium; code: yes
- [247. Strobogrammatic Number II](#247-strobogrammatic-number-ii) — Medium; code: yes
- [248. Strobogrammatic Number III](#248-strobogrammatic-number-iii) — Hard; code: yes
- [271. Encode and Decode Strings](#271-encode-and-decode-strings) — Medium; code: yes
- [273. Integer to English Words](#273-integer-to-english-words) — Hard; code: yes
- [293. Flip Game](#293-flip-game) — Easy; code: yes
- [318. Maximum Product of Word Lengths](#318-maximum-product-of-word-lengths) — Medium; code: yes
- [394. Decode String](#394-decode-string) — Medium; code: yes
- [405. Convert a Number to Hexadecimal](#405-convert-a-number-to-hexadecimal) — Easy; code: yes
- [412. Fizz Buzz](#412-fizz-buzz) — Easy; code: yes
- [415. Add Strings](#415-add-strings) — Easy; code: yes
- [434. Number of Segments in a String](#434-number-of-segments-in-a-string) — Easy; code: yes
- [439. Ternary Expression Parser](#439-ternary-expression-parser) — Medium; code: yes
- [459. Repeated Substring Pattern](#459-repeated-substring-pattern) — Easy; code: yes
- [468. Validate IP Address](#468-validate-ip-address) — Medium; code: yes
- [482. License Key Formatting](#482-license-key-formatting) — Easy; code: yes
- [504. Base 7](#504-base-7) — Easy; code: yes
- [520. Detect Capital](#520-detect-capital) — Easy; code: yes
- [521. Longest Uncommon Subsequence I](#521-longest-uncommon-subsequence-i) — Easy; code: yes
- [537. Complex Number Multiplication](#537-complex-number-multiplication) — Medium; code: yes
- [539. Minimum Time Difference](#539-minimum-time-difference) — Medium; code: yes
- [544. Output Contest Matches](#544-output-contest-matches) — Medium; code: yes
- [551. Student Attendance Record I](#551-student-attendance-record-i) — Easy; code: yes
- [564. Find the Closest Palindrome](#564-find-the-closest-palindrome) — Hard; code: yes
- [591. Tag Validator](#591-tag-validator) — Hard; code: yes
- [592. Fraction Addition and Subtraction](#592-fraction-addition-and-subtraction) — Medium; code: yes
- [604. Design Compressed String Iterator](#604-design-compressed-string-iterator) — Easy; code: yes
- [640. Solve the Equation](#640-solve-the-equation) — Medium; code: yes
- [657. Robot Return to Origin](#657-robot-return-to-origin) — Easy; code: yes
- [686. Repeated String Match](#686-repeated-string-match) — Medium; code: yes
- [709. To Lower Case](#709-to-lower-case) — Easy; code: yes
- [722. Remove Comments](#722-remove-comments) — Medium; code: yes
- [751. IP to CIDR](#751-ip-to-cidr) — Medium; code: yes
- [761. Special Binary String](#761-special-binary-string) — Hard; code: yes
- [772. Basic Calculator III](#772-basic-calculator-iii) — Hard; code: yes
- [796. Rotate String](#796-rotate-string) — Easy; code: yes
- [800. Similar RGB Color](#800-similar-rgb-color) — Easy; code: yes
- [806. Number of Lines To Write String](#806-number-of-lines-to-write-string) — Easy; code: yes
- [824. Goat Latin](#824-goat-latin) — Easy; code: yes
- [830. Positions of Large Groups](#830-positions-of-large-groups) — Easy; code: yes
- [831. Masking Personal Information](#831-masking-personal-information) — Medium; code: yes
- [843. Guess the Word](#843-guess-the-word) — Hard; code: yes
- [856. Score of Parentheses](#856-score-of-parentheses) — Medium; code: yes
- [880. Decoded String at Index](#880-decoded-string-at-index) — Medium; code: yes
- [899. Orderly Queue](#899-orderly-queue) — Hard; code: yes
- [906. Super Palindromes](#906-super-palindromes) — Hard; code: yes
- [937. Reorder Data in Log Files](#937-reorder-data-in-log-files) — Medium; code: yes
- [944. Delete Columns to Make Sorted](#944-delete-columns-to-make-sorted) — Easy; code: yes
- [972. Equal Rational Numbers](#972-equal-rational-numbers) — Hard; code: yes
- [1003. Check If Word Is Valid After Substitutions](#1003-check-if-word-is-valid-after-substitutions) — Medium; code: yes
- [1021. Remove Outermost Parentheses](#1021-remove-outermost-parentheses) — Easy; code: yes
- [1041. Robot Bounded In Circle](#1041-robot-bounded-in-circle) — Medium; code: yes
- [1047. Remove All Adjacent Duplicates In String](#1047-remove-all-adjacent-duplicates-in-string) — Easy; code: yes
- [1071. Greatest Common Divisor of Strings](#1071-greatest-common-divisor-of-strings) — Easy; code: yes
- [1078. Occurrences After Bigram](#1078-occurrences-after-bigram) — Easy; code: yes
- [1106. Parsing A Boolean Expression](#1106-parsing-a-boolean-expression) — Hard; code: yes
- [1108. Defanging an IP Address](#1108-defanging-an-ip-address) — Easy; code: yes
- [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](#1111-maximum-nesting-depth-of-two-valid-parentheses-strings) — Medium; code: yes
- [1119. Remove Vowels from a String](#1119-remove-vowels-from-a-string) — Easy; code: yes
- [1154. Day of the Year](#1154-day-of-the-year) — Easy; code: yes
- [1180. Count Substrings with Only One Distinct Letter](#1180-count-substrings-with-only-one-distinct-letter) — Easy; code: yes
- [1190. Reverse Substrings Between Each Pair of Parentheses](#1190-reverse-substrings-between-each-pair-of-parentheses) — Medium; code: yes
- [1209. Remove All Adjacent Duplicates in String II](#1209-remove-all-adjacent-duplicates-in-string-ii) — Medium; code: yes
- [1249. Minimum Remove to Make Valid Parentheses](#1249-minimum-remove-to-make-valid-parentheses) — Medium; code: yes
- [1256. Encode Number](#1256-encode-number) — Medium; code: yes
- [1271. Hexspeak](#1271-hexspeak) — Easy; code: yes
- [1309. Decrypt String from Alphabet to Integer Mapping](#1309-decrypt-string-from-alphabet-to-integer-mapping) — Easy; code: yes
- [1324. Print Words Vertically](#1324-print-words-vertically) — Medium; code: yes
- [1360. Number of Days Between Two Dates](#1360-number-of-days-between-two-dates) — Easy; code: yes
- [1374. Generate a String With Characters That Have Odd Counts](#1374-generate-a-string-with-characters-that-have-odd-counts) — Easy; code: yes
- [1404. Number of Steps to Reduce a Number in Binary Representation to One](#1404-number-of-steps-to-reduce-a-number-in-binary-representation-to-one) — Medium; code: yes
- [1408. String Matching in an Array](#1408-string-matching-in-an-array) — Easy; code: yes
- [1417. Reformat The String](#1417-reformat-the-string) — Easy; code: yes
- [1427. Perform String Shifts](#1427-perform-string-shifts) — Easy; code: yes
- [1446. Consecutive Characters](#1446-consecutive-characters) — Easy; code: yes
- [1447. Simplified Fractions](#1447-simplified-fractions) — Medium; code: yes
- [1451. Rearrange Words in a Sentence](#1451-rearrange-words-in-a-sentence) — Medium; code: yes
- [1507. Reformat Date](#1507-reformat-date) — Easy; code: yes
- [1513. Number of Substrings With Only 1s](#1513-number-of-substrings-with-only-1s) — Medium; code: yes
- [1528. Shuffle String](#1528-shuffle-string) — Easy; code: yes
- [1544. Make The String Great](#1544-make-the-string-great) — Easy; code: yes
- [1545. Find Kth Bit in Nth Binary String](#1545-find-kth-bit-in-nth-binary-string) — Medium; code: yes
- [1556. Thousand Separator](#1556-thousand-separator) — Easy; code: yes
- [1573. Number of Ways to Split a String](#1573-number-of-ways-to-split-a-string) — Medium; code: yes
- [1576. Replace All ?'s to Avoid Consecutive Repeating Characters](#1576-replace-all-s-to-avoid-consecutive-repeating-characters) — Easy; code: yes
- [1592. Rearrange Spaces Between Words](#1592-rearrange-spaces-between-words) — Easy; code: yes
- [1598. Crawler Log Folder](#1598-crawler-log-folder) — Easy; code: yes
- [1614. Maximum Nesting Depth of the Parentheses](#1614-maximum-nesting-depth-of-the-parentheses) — Easy; code: yes
- [1629. Slowest Key](#1629-slowest-key) — Easy; code: yes
- [1662. Check If Two String Arrays are Equivalent](#1662-check-if-two-string-arrays-are-equivalent) — Easy; code: yes
- [1678. Goal Parser Interpretation](#1678-goal-parser-interpretation) — Easy; code: yes
- [1694. Reformat Phone Number](#1694-reformat-phone-number) — Easy; code: yes
- [1758. Minimum Changes To Make Alternating Binary String](#1758-minimum-changes-to-make-alternating-binary-string) — Easy; code: yes
- [1759. Count Number of Homogenous Substrings](#1759-count-number-of-homogenous-substrings) — Medium; code: yes
- [1773. Count Items Matching a Rule](#1773-count-items-matching-a-rule) — Easy; code: yes
- [1784. Check if Binary String Has at Most One Segment of Ones](#1784-check-if-binary-string-has-at-most-one-segment-of-ones) — Easy; code: yes
- [1812. Determine Color of a Chessboard Square](#1812-determine-color-of-a-chessboard-square) — Easy; code: yes
- [1816. Truncate Sentence](#1816-truncate-sentence) — Easy; code: yes
- [1844. Replace All Digits with Characters](#1844-replace-all-digits-with-characters) — Easy; code: yes
- [1859. Sorting the Sentence](#1859-sorting-the-sentence) — Easy; code: yes
- [1869. Longer Contiguous Segments of Ones than Zeros](#1869-longer-contiguous-segments-of-ones-than-zeros) — Easy; code: yes
- [1880. Check if Word Equals Summation of Two Words](#1880-check-if-word-equals-summation-of-two-words) — Easy; code: yes
- [1904. The Number of Full Rounds You Have Played](#1904-the-number-of-full-rounds-you-have-played) — Medium; code: yes
- [1910. Remove All Occurrences of a Substring](#1910-remove-all-occurrences-of-a-substring) — Medium; code: yes
- [1933. Check if String Is Decomposable Into Value-Equal Substrings](#1933-check-if-string-is-decomposable-into-value-equal-substrings) — Easy; code: yes
- [1945. Sum of Digits of String After Convert](#1945-sum-of-digits-of-string-after-convert) — Easy; code: yes
- [1957. Delete Characters to Make Fancy String](#1957-delete-characters-to-make-fancy-string) — Easy; code: yes
- [1967. Number of Strings That Appear as Substrings in Word](#1967-number-of-strings-that-appear-as-substrings-in-word) — Easy; code: yes
- [2011. Final Value of Variable After Performing Operations](#2011-final-value-of-variable-after-performing-operations) — Easy; code: yes
- [2042. Check if Numbers Are Ascending in a Sentence](#2042-check-if-numbers-are-ascending-in-a-sentence) — Easy; code: yes
- [2047. Number of Valid Words in a Sentence](#2047-number-of-valid-words-in-a-sentence) — Easy; code: yes
- [2075. Decode the Slanted Ciphertext](#2075-decode-the-slanted-ciphertext) — Medium; code: yes
- [2114. Maximum Number of Words Found in Sentences](#2114-maximum-number-of-words-found-in-sentences) — Easy; code: yes
- [2120. Execution of All Suffix Instructions Staying in a Grid](#2120-execution-of-all-suffix-instructions-staying-in-a-grid) — Medium; code: yes
- [2124. Check if All A's Appears Before All B's](#2124-check-if-all-a-s-appears-before-all-b-s) — Easy; code: yes
- [2125. Number of Laser Beams in a Bank](#2125-number-of-laser-beams-in-a-bank) — Medium; code: yes
- [2129. Capitalize the Title](#2129-capitalize-the-title) — Easy; code: yes
- [2138. Divide a String Into Groups of Size k](#2138-divide-a-string-into-groups-of-size-k) — Easy; code: yes
- [2185. Counting Words With a Given Prefix](#2185-counting-words-with-a-given-prefix) — Easy; code: yes
- [2194. Cells in a Range on an Excel Sheet](#2194-cells-in-a-range-on-an-excel-sheet) — Easy; code: yes
- [2211. Count Collisions on a Road](#2211-count-collisions-on-a-road) — Medium; code: yes
- [2232. Minimize Result by Adding Parentheses to Expression](#2232-minimize-result-by-adding-parentheses-to-expression) — Medium; code: yes
- [2243. Calculate Digit Sum of a String](#2243-calculate-digit-sum-of-a-string) — Easy; code: yes
- [2255. Count Prefixes of a Given String](#2255-count-prefixes-of-a-given-string) — Easy; code: yes
- [2264. Largest 3-Same-Digit Number in String](#2264-largest-3-same-digit-number-in-string) — Easy; code: yes
- [2278. Percentage of Letter in String](#2278-percentage-of-letter-in-string) — Easy; code: yes
- [2288. Apply Discount to Prices](#2288-apply-discount-to-prices) — Medium; code: yes
- [2296. Design a Text Editor](#2296-design-a-text-editor) — Hard; code: yes
- [2299. Strong Password Checker II](#2299-strong-password-checker-ii) — Easy; code: yes
- [2315. Count Asterisks](#2315-count-asterisks) — Easy; code: yes
- [2390. Removing Stars From a String](#2390-removing-stars-from-a-string) — Medium; code: yes
- [2409. Count Days Spent Together](#2409-count-days-spent-together) — Easy; code: yes
- [2414. Length of the Longest Alphabetical Continuous Substring](#2414-length-of-the-longest-alphabetical-continuous-substring) — Medium; code: yes
- [2437. Number of Valid Clock Times](#2437-number-of-valid-clock-times) — Easy; code: yes
- [2446. Determine if Two Events Have Conflict](#2446-determine-if-two-events-have-conflict) — Easy; code: yes
- [2450. Number of Distinct Binary Strings After Applying Operations](#2450-number-of-distinct-binary-strings-after-applying-operations) — Medium; code: yes
- [2468. Split Message Based on Limit](#2468-split-message-based-on-limit) — Hard; code: yes
- [2490. Circular Sentence](#2490-circular-sentence) — Easy; code: yes
- [2496. Maximum Value of a String in an Array](#2496-maximum-value-of-a-string-in-an-array) — Easy; code: yes
- [2515. Shortest Distance to Target String in a Circular Array](#2515-shortest-distance-to-target-string-in-a-circular-array) — Easy; code: yes
- [2546. Apply Bitwise Operations to Make Strings Equal](#2546-apply-bitwise-operations-to-make-strings-equal) — Medium; code: yes
- [2575. Find the Divisibility Array of a String](#2575-find-the-divisibility-array-of-a-string) — Medium; code: yes
- [2609. Find the Longest Balanced Substring of a Binary String](#2609-find-the-longest-balanced-substring-of-a-binary-string) — Easy; code: yes
- [2678. Number of Senior Citizens](#2678-number-of-senior-citizens) — Easy; code: yes
- [2696. Minimum String Length After Removing Substrings](#2696-minimum-string-length-after-removing-substrings) — Easy; code: yes
- [2710. Remove Trailing Zeros From a String](#2710-remove-trailing-zeros-from-a-string) — Easy; code: yes
- [2785. Sort Vowels in a String](#2785-sort-vowels-in-a-string) — Medium; code: yes
- [2788. Split Strings by Separator](#2788-split-strings-by-separator) — Easy; code: yes
- [2802. Find The K-th Lucky Number](#2802-find-the-k-th-lucky-number) — Medium; code: yes
- [2810. Faulty Keyboard](#2810-faulty-keyboard) — Easy; code: yes
- [2828. Check if a String Is an Acronym of Words](#2828-check-if-a-string-is-an-acronym-of-words) — Easy; code: yes
- [2839. Check if Strings Can be Made Equal With Operations I](#2839-check-if-strings-can-be-made-equal-with-operations-i) — Easy; code: yes
- [2914. Minimum Number of Changes to Make Binary String Beautiful](#2914-minimum-number-of-changes-to-make-binary-string-beautiful) — Medium; code: yes
- [2937. Make Three Strings Equal](#2937-make-three-strings-equal) — Easy; code: yes
- [2942. Find Words Containing Character](#2942-find-words-containing-character) — Easy; code: yes
- [3019. Number of Changing Keys](#3019-number-of-changing-keys) — Easy; code: yes
- [3110. Score of a String](#3110-score-of-a-string) — Easy; code: yes
- [3114. Latest Time You Can Obtain After Replacing Characters](#3114-latest-time-you-can-obtain-after-replacing-characters) — Easy; code: yes
- [3136. Valid Word](#3136-valid-word) — Easy; code: yes
- [3163. String Compression III](#3163-string-compression-iii) — Medium; code: yes
- [3168. Minimum Number of Chairs in a Waiting Room](#3168-minimum-number-of-chairs-in-a-waiting-room) — Easy; code: yes
- [3174. Clear Digits](#3174-clear-digits) — Easy; code: yes
- [3210. Find the Encrypted String](#3210-find-the-encrypted-string) — Easy; code: yes
- [3227. Vowels Game in a String](#3227-vowels-game-in-a-string) — Medium; code: yes
- [3234. Count the Number of Substrings With Dominant Ones](#3234-count-the-number-of-substrings-with-dominant-ones) — Medium; code: yes
- [3248. Snake in Matrix](#3248-snake-in-matrix) — Easy; code: yes
- [3271. Hash Divided String](#3271-hash-divided-string) — Medium; code: yes
- [3274. Check if Two Chessboard Squares Have the Same Color](#3274-check-if-two-chessboard-squares-have-the-same-color) — Easy; code: yes
- [3280. Convert Date to Binary](#3280-convert-date-to-binary) — Easy; code: yes
- [3303. Find the Occurrence of First Almost Equal Substring](#3303-find-the-occurrence-of-first-almost-equal-substring) — Hard; code: yes
- [3324. Find the Sequence of Strings Appeared on the Screen](#3324-find-the-sequence-of-strings-appeared-on-the-screen) — Medium; code: yes
- [3330. Find the Original Typed String I](#3330-find-the-original-typed-string-i) — Easy; code: yes
- [3340. Check Balanced String](#3340-check-balanced-string) — Easy; code: yes
- [3407. Substring Matching Pattern](#3407-substring-matching-pattern) — Easy; code: yes
- [3456. Find Special Substring of Length K](#3456-find-special-substring-of-length-k) — Easy; code: yes
- [3461. Check If Digits Are Equal in String After Operations I](#3461-check-if-digits-are-equal-in-string-after-operations-i) — Easy; code: yes
- [3463. Check If Digits Are Equal in String After Operations II](#3463-check-if-digits-are-equal-in-string-after-operations-ii) — Hard; code: yes
- [3498. Reverse Degree of a String](#3498-reverse-degree-of-a-string) — Easy; code: yes
- [3499. Maximize Active Section with Trade I](#3499-maximize-active-section-with-trade-i) — Medium; code: yes
- [3517. Smallest Palindromic Rearrangement I](#3517-smallest-palindromic-rearrangement-i) — Medium; code: yes
- [3561. Resulting String After Adjacent Removals](#3561-resulting-string-after-adjacent-removals) — Medium; code: yes
- [3571. Find the Shortest Superstring II](#3571-find-the-shortest-superstring-ii) — Easy; code: yes
- [3582. Generate Tag for Video Caption](#3582-generate-tag-for-video-caption) — Easy; code: yes
- [3598. Longest Common Prefix Between Adjacent Strings After Removals](#3598-longest-common-prefix-between-adjacent-strings-after-removals) — Medium; code: yes
- [3602. Hexadecimal and Hexatrigesimal Conversion](#3602-hexadecimal-and-hexatrigesimal-conversion) — Easy; code: yes
- [3612. Process String with Special Operations I](#3612-process-string-with-special-operations-i) — Medium; code: yes
- [3614. Process String with Special Operations II](#3614-process-string-with-special-operations-ii) — Hard; code: yes
- [3696. Maximum Distance Between Unequal Words in Array I](#3696-maximum-distance-between-unequal-words-in-array-i) — Easy; code: yes
- [3703. Remove K-Balanced Substrings](#3703-remove-k-balanced-substrings) — Medium; code: yes
- [3706. Maximum Distance Between Unequal Words in Array II](#3706-maximum-distance-between-unequal-words-in-array-ii) — Medium; code: yes
- [3744. Find Kth Character in Expanded String](#3744-find-kth-character-in-expanded-string) — Medium; code: yes
- [3798. Largest Even Number](#3798-largest-even-number) — Easy; code: yes
- [3813. Vowel-Consonant Score](#3813-vowel-consonant-score) — Easy; code: yes
- [3817. Good Indices in a Digit String](#3817-good-indices-in-a-digit-string) — Medium; code: yes
- [3838. Weighted Word Mapping](#3838-weighted-word-mapping) — Easy; code: yes
- [3856. Trim Trailing Vowels](#3856-trim-trailing-vowels) — Easy; code: yes
- [3863. Minimum Operations to Sort a String](#3863-minimum-operations-to-sort-a-string) — Medium; code: yes
- [3894. Traffic Signal Color](#3894-traffic-signal-color) — Easy; code: yes
- [3921. Score Validator](#3921-score-validator) — Easy; code: yes
- [3922. Minimum Flips to Make Binary String Coherent](#3922-minimum-flips-to-make-binary-string-coherent) — Medium; code: yes
- [3931. Check Adjacent Digit Differences](#3931-check-adjacent-digit-differences) — Easy; code: yes
- [3986. Number of Elapsed Seconds Between Two Times](#3986-number-of-elapsed-seconds-between-two-times) — Easy; code: yes
- [4021. Minimum Operations to Make a Rotated Palindrome I](#4021-minimum-operations-to-make-a-rotated-palindrome-i) — Medium; code: yes
- [4028. Minimum Operations to Make a Rotated Palindrome II](#4028-minimum-operations-to-make-a-rotated-palindrome-ii) — Hard; code: yes

---

## 6. Zigzag Conversion

**Problem:** https://leetcode.com/problems/zigzag-conversion/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n + r)

**Complexity reasoning:** Each input character is appended to one of r row strings, then the rows are concatenated; row storage and output hold n characters.

### Problem description

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) 
 
```
P A H N
A P L S I I G
Y I R
```

 And then read line by line: "PAHNAPLSIIGYIR" 
 
 Write the code that will take a string and make this conversion given a number of rows: 
 
```
string convert(string s, int numRows);
```

 Example 1: 
 
```
Input:
 s = "PAYPALISHIRING", numRows = 3

Output:
 "PAHNAPLSIIGYIR"
```

 Example 2: 
 
```
Input:
 s = "PAYPALISHIRING", numRows = 4

Output:
 "PINALSIGYAHRPI"

Explanation:

P I N
A L S I G
Y A H R
P I
```

 Example 3: 
 
```
Input:
 s = "A", numRows = 1

Output:
 "A"
```

 Constraints: 

 1 <= s.length <= 1000 
 
 s consists of English letters (lower-case and upper-case), ',' and '.' . 
 
 1 <= numRows <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= (int)s.size()) return s;
        vector<string> rows(numRows);
        int row = 0, direction = 1;
        for (char c : s) {
            rows[row] += c;
            if (row == 0) direction = 1;
            else if (row == numRows - 1) direction = -1;
            row += direction;
        }
        string result;
        for (const string& part : rows) result += part;
        return result;
    }
};
```


## 8. String to Integer (atoi)

**Problem:** https://leetcode.com/problems/string-to-integer-atoi/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** The pointer scans whitespace, sign and digits at most once, maintaining only integer counters; the input string is passed by value.

### Problem description

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer. 
 
 The algorithm for myAtoi(string s) is as follows: 

 Whitespace : Ignore any leading whitespace ( " " ). 
 
 Signedness : Determine the sign by checking if the next character is '-' or '+' , assuming positivity if neither present. 
 
 Conversion : Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0. 
 
 Rounding : If the integer is out of the 32-bit signed integer range [-2 31 , 2 31 - 1] , then round the integer to remain in the range. Specifically, integers less than -2 31 should be rounded to -2 31 , and integers greater than 2 31 - 1 should be rounded to 2 31 - 1 . 

 Return the integer as the final result. 
 
 Note: ​​​​​​​ You must not use any built-in library function that converts a string to a number (for example, atoi , stoi , Integer.parseInt , int() , parseInt , Number() ). Perform the conversion manually. 

 Example 1: 

 Input: s = "42" 
 
 Output: 42 
 
 Explanation: 
 
```
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
 ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
 ^
Step 3: "
42
" ("42" is read in)
 ^
```

 Example 2: 

 Input: s = " -042" 
 
 Output: -42 
 
 Explanation: 
 
```
Step 1: "
 
-042" (leading whitespace is read and ignored)
 ^
Step 2: " 
-
042" ('-' is read, so the result should be negative)
 ^
Step 3: " -
042
" ("042" is read in, leading zeros ignored in the result)
 ^
```

 Example 3: 

 Input: s = "1337c0d3" 
 
 Output: 1337 
 
 Explanation: 
 
```
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
 ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
 ^
Step 3: "
1337
c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
 ^
```

 Example 4: 

 Input: s = "0-1" 
 
 Output: 0 
 
 Explanation: 
 
```
Step 1: "0-1" (no characters read because there is no leading whitespace)
 ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
 ^
Step 3: "
0
-1" ("0" is read in; reading stops because the next character is a non-digit)
 ^
```

 Example 5: 

 Input: s = "words and 987" 
 
 Output: 0 
 
 Explanation: 
 
 Reading stops at the first non-digit character 'w'. 

 Constraints: 

 0 <= s.length <= 200 
 
 s consists of English letters (lower-case and upper-case), digits ( 0 - 9 ), ' ' , '+' , '-' , and '.' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <string>
#include <climits>
using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        int i = 0, sign = 1, result = 0;
        while (i < s.size() && s[i] == ' ') ++i;
        
        if (i < s.size() && (s[i] == '+' || s[i] == '-')) {
            sign = s[i] == '+' ? 1 : -1;
            ++i;
        }
        
        while (i < s.size() && isdigit(s[i])) {
            int digit = s[i] - '0';
            if (result > (INT_MAX - digit) / 10) return sign == 1 ? INT_MAX : INT_MIN;
            result = result * 10 + digit;
            ++i;
        }
        
        return result * sign;
    }
};
```


## 20. Valid Parentheses

**Problem:** https://leetcode.com/problems/valid-parentheses/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Stack, Bracket Sequences

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Hash map, Ordered map, Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n) expected

**Space complexity:** O(n)

**Complexity reasoning:** Each bracket is processed once with constant-size hash lookups; the stack can hold n opening brackets.

### Problem description

Given a string s containing just the characters '(' , ')' , '{' , '}' , '[' and ']' , determine if the input string is valid. 
 
 An input string is valid if: 

 Open brackets must be closed by the same type of brackets. 
 
 Open brackets must be closed in the correct order. 
 
 Every close bracket has a corresponding open bracket of the same type. 

 Example 1: 

 Input: s = "()" 
 
 Output: true 

 Example 2: 

 Input: s = "()[]{}" 
 
 Output: true 

 Example 3: 

 Input: s = "(]" 
 
 Output: false 

 Example 4: 

 Input: s = "([])" 
 
 Output: true 

 Example 5: 

 Input: s = "([)]" 
 
 Output: false 

 Constraints: 

 1 <= s.length <= 10 4 
 
 s consists of parentheses only '()[]{}' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <stack>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> pairs = {{')', '('}, {']', '['}, {'}', '{'}};
        
        for (char c : s) {
            if (pairs.count(c)) {
                if (st.empty() || st.top() != pairs[c]) return false;
                st.pop();
            } else {
                st.push(c);
            }
        }
        return st.empty();
    }
};
```


## 38. Count and Say

**Problem:** https://leetcode.com/problems/count-and-say/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(L)

**Space complexity:** O(L)

**Complexity reasoning:** Across all n generated terms, each previous term is scanned once; L is the sum of their lengths, and the two working strings occupy at most the largest term size.

### Problem description

The count-and-say sequence is a sequence of digit strings defined by the recursive formula: 

 countAndSay(1) = "1" 
 
 countAndSay(n) is the run-length encoding of countAndSay(n - 1) . 

 Run-length encoding (RLE) is a string compression method that works by replacing each maximal group of consecutive identical characters with the concatenation of the length of the group followed by the character itself. For example, to compress the string "3322251" we replace "33" with "23" , replace "222" with "32" , replace "5" with "15" , and replace "1" with "11" . Thus the compressed string becomes "23321511" . 
 
 Given a positive integer n , return the n th element of the count-and-say sequence . 

 Example 1: 

 Input: n = 4 
 
 Output: "1211" 
 
 Explanation: 
 
```
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
```

 Example 2: 

 Input: n = 1 
 
 Output: "1" 
 
 Explanation: 
 
 This is the base case. 

 Constraints: 

 1 <= n <= 30 

 Follow up: Could you solve it iteratively?

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <string>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        string result = "1";
        for (int i = 1; i < n; ++i) {
            string temp = "";
            for (int j = 0; j < result.size(); ++j) {
                int count = 1;
                while (j + 1 < result.size() && result[j] == result[j + 1]) {
                    ++j;
                    ++count;
                }
                temp += to_string(count) + result[j];
            }
            result = temp;
        }
        return result;
    }
};
```


## 43. Multiply Strings

**Problem:** https://leetcode.com/problems/multiply-strings/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(nm + n + m)

**Space complexity:** O(n + m)

**Complexity reasoning:** Every pair of digits is multiplied once; the intermediate digit vector and output have n+m positions.

### Problem description

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2 , also represented as a string. 
 
 Note:  You must not use any built-in BigInteger library or convert the inputs to integer directly. 

 Example 1: 
 
```
Input:
 num1 = "2", num2 = "3"

Output:
 "6"
```
 
 Example 2: 
 
```
Input:
 num1 = "123", num2 = "456"

Output:
 "56088"
```

 Constraints: 

 1 <= num1.length, num2.length <= 200 
 
 num1 and num2 consist of digits only. 
 
 Both num1 and num2  do not contain any leading zero, except the number 0 itself.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string multiply(string num1, string num2) {
    if (num1 == "0" || num2 == "0") return "0"; // If any number is 0, result is 0
    
    int n = num1.size(), m = num2.size();
    vector<int> result(n + m, 0); // To store intermediate results

    // Multiply each digit of num1 with each digit of num2
    for (int i = n - 1; i >= 0; i--) {
        for (int j = m - 1; j >= 0; j--) {
            int mul = (num1[i] - '0') * (num2[j] - '0'); // Multiply digits
            int sum = mul + result[i + j + 1];           // Add to the current position

            result[i + j + 1] = sum % 10;               // Store single digit at current position
            result[i + j] += sum / 10;                  // Carry to the next position
        }
    }

    // Convert result vector to string, skipping leading zeros
    string product;
    for (int num : result) {
        if (!(product.empty() && num == 0)) { // Skip leading zeros
            product.push_back(num + '0');
        }
    }
    
    return product;
}
};
```


## 58. Length of Last Word

**Problem:** https://leetcode.com/problems/length-of-last-word/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Two backward scans skip trailing spaces and count the last word; only indices and a counter are used, excluding the by-value input.

### Problem description

Given a string s consisting of words and spaces, return the length of the last word in the string. 
 
 A word is a maximal substring consisting of non-space characters only. 

 Example 1: 
 
```
Input:
 s = "Hello World"

Output:
 5

Explanation:
 The last word is "World" with length 5.
```

 Example 2: 
 
```
Input:
 s = " fly me to the moon "

Output:
 4

Explanation:
 The last word is "moon" with length 4.
```

 Example 3: 
 
```
Input:
 s = "luffy is still joyboy"

Output:
 6

Explanation:
 The last word is "joyboy" with length 6.
```

 Constraints: 

 1 <= s.length <= 10 4 
 
 s consists of only English letters and spaces ' ' . 
 
 There will be at least one word in s .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1, len = 0;
        while (i >= 0 && s[i] == ' ') i--;
        while (i >= 0 && s[i] != ' ') {
            len++;
            i--;
        }
        return len;
    }
};
```


## 65. Valid Number

**Problem:** https://leetcode.com/problems/valid-number/

**Difficulty:** Hard | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** The finite-state flags are updated in one pass with no growing auxiliary container; the input is passed by value.

### Problem description

Given a string s , return whether s is a valid number . 
 
For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789" , while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53" . 
 
 Formally, a  valid number is defined using one of the following definitions: 

 An integer number followed by an optional exponent . 
 
 A decimal number followed by an optional exponent . 

 An integer number is defined with an optional sign '-' or '+' followed by digits . 
 
 A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions: 

 Digits followed by a dot '.' . 
 
 Digits followed by a dot '.' followed by digits . 
 
 A dot '.' followed by digits . 

 An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number . 
 
 The digits are defined as one or more digits. 

 Example 1: 

 Input: s = "0" 
 
 Output: true 

 Example 2: 

 Input: s = "e" 
 
 Output: false 

 Example 3: 

 Input: s = "." 
 
 Output: false 

 Constraints: 

 1 <= s.length <= 20 
 
 s consists of only English letters (both uppercase and lowercase), digits ( 0-9 ), plus '+' , minus '-' , or dot '.' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    bool isNumber(string s) {
        bool num = false, dot = false, exp = false;
        for (int i = 0; i < s.size(); ++i) {
            if (isdigit(s[i])) num = true;
            else if (s[i] == '.') {
                if (dot || exp) return false;
                dot = true;
            } else if (s[i] == 'e' || s[i] == 'E') {
                if (exp || !num) return false;
                exp = true; num = false;
            } else if (s[i] == '+' || s[i] == '-') {
                if (i > 0 && s[i - 1] != 'e' && s[i - 1] != 'E') return false;
            } else return false;
        }
        return num;
    }
};
```


## 67. Add Binary

**Problem:** https://leetcode.com/problems/add-binary/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String, Bit Manipulation, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + m)

**Space complexity:** O(max(n, m))

**Complexity reasoning:** Each binary digit is consumed once, a possible carry adds one digit, and the result is reversed in place.

### Problem description

Given two binary strings a and b , return their sum as a binary string . 

 Example 1: 
 
```
Input:
 a = "11", b = "1"

Output:
 "100"
```
 
 Example 2: 
 
```
Input:
 a = "1010", b = "1011"

Output:
 "10101"
```

 Constraints: 

 1 <= a.length, b.length <= 10 4 
 
 a and b consist only of '0' or '1' characters. 
 
 Each string does not contain leading zeros except for the zero itself.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        string result = "";
        int carry = 0, i = a.size() - 1, j = b.size() - 1;
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            result += (sum % 2) + '0';
            carry = sum / 2;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```


## 68. Text Justification

**Problem:** https://leetcode.com/problems/text-justification/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + L)

**Space complexity:** O(L)

**Complexity reasoning:** Each word is packed and emitted once, and L total characters are written across the padded lines; the result stores L characters.

### Problem description

Given an array of strings words and a width maxWidth , format the text such that each line has exactly maxWidth characters and is fully (left and right) justified. 
 
 You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters. 
 
 Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. 
 
 For the last line of text, it should be left-justified, and no extra space is inserted between words. 
 
 Note: 

 A word is defined as a character sequence consisting of non-space characters only. 
 
 Each word's length is guaranteed to be greater than 0 and not exceed maxWidth . 
 
 The input array words contains at least one word. 

 Example 1: 
 
```
Input:
 words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16

Output:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

 Example 2: 
 
```
Input:
 words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16

Output:

[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

Explanation:
 Note that the last line is "shall be " instead of "shall be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
```

 Example 3: 
 
```
Input:
 words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20

Output:

[
  "Science  is  what we",
 "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

 Constraints: 

 1 <= words.length <= 300 
 
 1 <= words[i].length <= 20 
 
 words[i] consists of only English letters and symbols. 
 
 1 <= maxWidth <= 100 
 
 words[i].length <= maxWidth

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> result;
        int n = words.size(), index = 0;
        
        while (index < n) {
            int totalChars = words[index].size();
            int last = index + 1;
            while (last < n && totalChars + 1 + words[last].size() <= maxWidth) {
                totalChars += 1 + words[last].size();
                last++;
            }

            string line = words[index];
            int gaps = last - index - 1;

            if (last == n || gaps == 0) {
                for (int i = index + 1; i < last; i++) {
                    line += " " + words[i];
                }
                while (line.size() < maxWidth) {
                    line += " ";
                }
            } else {
                int spaces = (maxWidth - totalChars + gaps) / gaps;
                int extra = (maxWidth - totalChars + gaps) % gaps;

                for (int i = index + 1; i < last; i++) {
                    line += string(spaces + (i - index <= extra ? 1 : 0), ' ') + words[i];
                }
            }

            result.push_back(line);
            index = last;
        }

        return result;
    }
};
```


## 71. Simplify Path

**Problem:** https://leetcode.com/problems/simplify-path/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Tokenization scans the path, and the directory vector plus reconstructed canonical path store at most n characters.

### Problem description

You are given an absolute path for a Unix-style file system, which always begins with a slash '/' . Your task is to transform this absolute path into its simplified canonical path . 
 
 The rules of a Unix-style file system are as follows: 

 A single period '.' represents the current directory. 
 
 A double period '..' represents the previous/parent directory. 
 
 Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/' . 
 
 Any sequence of periods that does not match the rules above should be treated as a valid directory or file name . For example, '...' and '....' are valid directory or file names. 

 The simplified canonical path should follow these rules : 

 The path must start with a single slash '/' . 
 
 Directories within the path must be separated by exactly one slash '/' . 
 
 The path must not end with a slash '/' , unless it is the root directory. 
 
 The path must not have any single or double periods ( '.' and '..' ) used to denote current or parent directories. 

 Return the simplified canonical path . 

 Example 1: 

 Input: path = "/home/" 
 
 Output: "/home" 
 
 Explanation: 
 
 The trailing slash should be removed. 

 Example 2: 

 Input: path = "/home//foo/" 
 
 Output: "/home/foo" 
 
 Explanation: 
 
 Multiple consecutive slashes are replaced by a single one. 

 Example 3: 

 Input: path = "/home/user/Documents/../Pictures" 
 
 Output: "/home/user/Pictures" 
 
 Explanation: 
 
 A double period ".." refers to the directory up a level (the parent directory). 

 Example 4: 

 Input: path = "/../" 
 
 Output: "/" 
 
 Explanation: 
 
 Going one level up from the root directory is not possible. 

 Example 5: 

 Input: path = "/.../a/../b/c/../d/./" 
 
 Output: "/.../b/d" 
 
 Explanation: 
 
 "..." is a valid name for a directory in this problem. 

 Constraints: 

 1 <= path.length <= 3000 
 
 path consists of English letters, digits, period '.' , slash '/' or '_' . 
 
 path is a valid absolute Unix path.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <sstream>
#include <vector>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        stringstream ss(path);
        string dir;
        
        while (getline(ss, dir, '/')) {
            if (dir == "..") {
                if (!stack.empty()) stack.pop_back();
            } else if (!dir.empty() && dir != ".") {
                stack.push_back(dir);
            }
        }
        
        string result = "/";
        for (int i = 0; i < stack.size(); i++) {
            result += stack[i];
            if (i < stack.size() - 1) result += "/";
        }
        return result;
    }
};
```


## 168. Excel Sheet Column Title

**Problem:** https://leetcode.com/problems/excel-sheet-column-title/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(d²)

**Space complexity:** O(d)

**Complexity reasoning:** There are d base-26 digits; prepending a character to the growing std::string shifts existing characters on every iteration.

### Problem description

Given an integer columnNumber , return its corresponding column title as it appears in an Excel sheet . 
 
 For example: 
 
```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
```

 Example 1: 
 
```
Input:
 columnNumber = 1

Output:
 "A"
```

 Example 2: 
 
```
Input:
 columnNumber = 28

Output:
 "AB"
```

 Example 3: 
 
```
Input:
 columnNumber = 701

Output:
 "ZY"
```

 Constraints: 

 1 <= columnNumber <= 2 31 - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string convertToTitle(int columnNumber) {
        string result = "";
        while (columnNumber) {
            columnNumber--;
            result = char('A' + columnNumber % 26) + result;
            columnNumber /= 26;
        }
        return result;
    }
};
```


## 171. Excel Sheet Column Number

**Problem:** https://leetcode.com/problems/excel-sheet-column-number/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Each title character contributes one base-26 digit; the accumulator uses constant storage, excluding the by-value parameter.

### Problem description

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number . 
 
 For example: 
 
```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
```

 Example 1: 
 
```
Input:
 columnTitle = "A"

Output:
 1
```

 Example 2: 
 
```
Input:
 columnTitle = "AB"

Output:
 28
```

 Example 3: 
 
```
Input:
 columnTitle = "ZY"

Output:
 701
```

 Constraints: 

 1 <= columnTitle.length <= 7 
 
 columnTitle consists only of uppercase English letters. 
 
 columnTitle is in the range ["A", "FXSHRXW"] .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
using namespace std;

class Solution {
public:
    int titleToNumber(string columnTitle) {
        int result = 0;
        for (char c : columnTitle) {
            result = result * 26 + (c - 'A' + 1);
        }
        return result;
    }
};
```


## 224. Basic Calculator

**Problem:** https://leetcode.com/problems/basic-calculator/

**Difficulty:** Hard | **Premium:** No

**Tags:** Math, String, Stack, Recursion

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The outer scan and nested digit scan together visit each character a constant number of times; saved parenthesis contexts can fill the stack.

### Problem description

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation . 
 
 Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval() . 

 Example 1: 
 
```
Input:
 s = "1 + 1"

Output:
 2
```

 Example 2: 
 
```
Input:
 s = " 2-1 + 2 "

Output:
 3
```

 Example 3: 
 
```
Input:
 s = "(1+(4+5+2)-3)+(6+8)"

Output:
 23
```

 Constraints: 

 1 <= s.length <= 3 * 10 5 
 
 s consists of digits, '+' , '-' , '(' , ')' , and ' ' . 
 
 s represents a valid expression. 
 
 '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid). 
 
 '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid). 
 
 There will be no two consecutive operators in the input. 
 
 Every number and running calculation will fit in a signed 32-bit integer.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    int calculate(string s) 
    {
        long long int sum = 0;
        int sign = 1;
        stack<pair<int,int>> st;

        for(int i=0; i<s.size();i++)
        {
            if(isdigit(s[i]))
            {
                long long int num = 0;
                while(i<s.size() && isdigit(s[i]))
                {
                    num = num * 10 + (s[i] - '0');
                    i++;
                }
                i--;
                sum += num * sign;
                sign = 1;
            }
            else if(s[i] == '(')
            {
                st.push({sum, sign});
                sum = 0;
                sign = 1;
            }
            else if(s[i] == ')')
            {
                sum = st.top().first + (st.top().second * sum);
                st.pop();

            }
            else if(s[i] == '-')
            {
                sign = -1 * sign;
            }
        }
        return sum;
    }
};
```


## 227. Basic Calculator II

**Problem:** https://leetcode.com/problems/basic-calculator-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String, Stack

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One pass evaluates digit groups and applies operators using only current number, previous term and accumulated result.

### Problem description

Given a string s which represents an expression, evaluate this expression and return its value .  
 
 The integer division should truncate toward zero. 
 
 You may assume that the given expression is always valid. All intermediate results will be in the range of [-2 31 , 2 31 - 1] . 
 
 Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval() . 

 Example 1: 
 
```
Input:
 s = "3+2*2"

Output:
 7
```
 
 Example 2: 
 
```
Input:
 s = " 3/2 "

Output:
 1
```
 
 Example 3: 
 
```
Input:
 s = " 3+5 / 2 "

Output:
 5
```

 Constraints: 

 1 <= s.length <= 3 * 10 5 
 
 s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces. 
 
 s represents a valid expression. 
 
 All the integers in the expression are non-negative integers in the range [0, 2 31 - 1] . 
 
 The answer is guaranteed to fit in a 32-bit integer .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int calculate(string s) {
        int num = 0, n = s.size(), result = 0, last = 0;
        char op = '+';
        for (int i = 0; i < n; ++i) {
            if (isdigit(s[i])) {
                num = num * 10 + (s[i] - '0');
            }
            if (!isdigit(s[i]) && !isspace(s[i]) || i == n - 1) {
                if (op == '+') { result += last; last = num; }
                else if (op == '-') { result += last; last = -num; }
                else if (op == '*') { last *= num; }
                else if (op == '/') { last /= num; }
                op = s[i];
                num = 0;
            }
        }
        return result + last;
    }
};
```


## 243. Shortest Word Distance

**Problem:** https://leetcode.com/problems/shortest-word-distance/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(nL)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Each of n words is compared against two targets; L bounds word-comparison length, while indices and minimum distance are constant-size (target arguments are copied).

### Problem description

Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2 , return the shortest distance between these two words in the list . 

 Example 1: 
 
```
Input:
 wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"

Output:
 3
```

 Example 2: 
 
```
Input:
 wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"

Output:
 1
```

 Constraints: 

 2 <= wordsDict.length <= 3 * 10 4 
 
 1 <= wordsDict[i].length <= 10 
 
 wordsDict[i] consists of lowercase English letters. 
 
 word1 and word2 are in wordsDict . 
 
 word1 != word2

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
public:
    int shortestDistance(vector< string>& wordsDict, string word1, string word2)
    {
        int a = - 1, b = - 1, best = INT_MAX;
        for (int i = 0; i < (int) wordsDict.size();++i)
        {
            if (wordsDict[i] == word1)
            {
                a = i;
            }
            if (wordsDict[i] == word2)
            {
                b = i;
            }
            if (a >= 0 && b >= 0)
            {
                best = min(best, abs(a - b));
            }
        }
        return best;
    }
};
```


## 245. Shortest Word Distance III

**Problem:** https://leetcode.com/problems/shortest-word-distance-iii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(nL)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** The code scans all n words, comparing with target strings (up to L characters each), and tracks only last-seen positions.

### Problem description

Given an array of strings wordsDict and two strings that already exist in the array word1 and word2 , return the shortest distance between the occurrence of these two words in the list . 
 
 Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list. 

 Example 1: 
 
```
Input:
 wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"

Output:
 1
```
 
 Example 2: 
 
```
Input:
 wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"

Output:
 3
```

 Constraints: 

 1 <= wordsDict.length <= 10 5 
 
 1 <= wordsDict[i].length <= 10 
 
 wordsDict[i] consists of lowercase English letters. 
 
 word1 and word2 are in wordsDict .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
public:
    int shortestWordDistance(vector< string>& wordsDict, string word1, string word2)
    {
        int a = - 1, b = - 1, best = INT_MAX;
        for (int i = 0; i < (int) wordsDict.size();++i)
        {
            if (word1 == word2)
            {
                if (wordsDict[i] == word1)
                {
                    if (a != - 1)
                    {
                        best = min(best, i - a);
                    }
                    a = i;
                }
            }
            else
            {
                if (wordsDict[i] == word1)
                {
                    a = i;
                }
                if (wordsDict[i] == word2)
                {
                    b = i;
                }
                if (a != - 1 && b != - 1)
                {
                    best = min(best, abs(a - b));
                }
            }
        }
        return best;
    }
};
```


## 247. Strobogrammatic Number II

**Problem:** https://leetcode.com/problems/strobogrammatic-number-ii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, String, Recursion

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n · 5^⌈n/2⌉)

**Space complexity:** O(n · 5^⌈n/2⌉)

**Complexity reasoning:** Recursive construction branches over five outer pairs and copies O(n)-length strings for each generated candidate; returned strings dominate storage.

### Problem description

Given an integer n , return all the strobogrammatic numbers that are of length n . You may return the answer in any order . 
 
 A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). 

 Example 1: 
 
```
Input:
 n = 2

Output:
 ["11","69","88","96"]
```
 
 Example 2: 
 
```
Input:
 n = 1

Output:
 ["0","1","8"]
```

 Constraints: 

 1 <= n <= 14

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
    vector< string>build(int n, int total)
    {
        if (n == 0) return { "" };
        if (n == 1) return { "0", "1", "8" };
        vector< string>out;
        for (auto&mid : build(n - 2, total))
        {
            for (auto p : vector< string> { "00", "11", "69", "88", "96" })
            {
                if (n == total && p == "00")
                {
                    continue;
                }
                out.push_back(p.substr(0, 1) + mid + p.substr(1, 1));
            }
        }
        return out;
    }
public:
    vector< string>findStrobogrammatic(int n)
    {
        return build(n, n);
    }
};
```


## 248. Strobogrammatic Number III

**Problem:** https://leetcode.com/problems/strobogrammatic-number-iii/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, String, Recursion

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(H · 5^⌈H/2⌉)

**Space complexity:** O(H)

**Complexity reasoning:** For each length up to H, DFS explores up to five choices per pair and checks completed O(H)-character candidates against bounds; one mutable string and recursion stack are retained.

### Problem description

Given two strings low and high that represent two integers low and high where low <= high , return the number of strobogrammatic numbers in the range [low, high] . 
 
 A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). 

 Example 1: 
 
```
Input:
 low = "50", high = "100"

Output:
 3
```
 
 Example 2: 
 
```
Input:
 low = "0", high = "0"

Output:
 1
```

 Constraints: 

 1 <= low.length, high.length <= 15 
 
 low and high consist of only digits. 
 
 low <= high 
 
 low and high do not contain any leading zeros except for zero itself.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    int ans = 0;
    string low, high;
    void build(string& s, int l, int r) {
        if (l > r) {
            if ((s.size() > low.size() || s >= low) &&
                (s.size() < high.size() || s <= high)) ++ans;
            return;
        }
        const vector<pair<char,char>> pairs = {
            {'0','0'}, {'1','1'}, {'6','9'}, {'8','8'}, {'9','6'}
        };
        for (const auto& p : pairs) {
            if (l == r && p.first != p.second) continue;
            if (l == 0 && s.size() > 1 && p.first == '0') continue;
            s[l] = p.first;
            s[r] = p.second;
            build(s, l + 1, r - 1);
        }
    }
public:
    int strobogrammaticInRange(string low, string high) {
        this->low = low;
        this->high = high;
        ans = 0;
        for (int len = low.size(); len <= (int)high.size(); ++len) {
            string s(len, ' ');
            build(s, 0, len - 1);
        }
        return ans;
    }
};
```


## 271. Encode and Decode Strings

**Problem:** https://leetcode.com/problems/encode-and-decode-strings/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, String, Design

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(N + k log M)

**Space complexity:** O(N + k)

**Complexity reasoning:** Encoding/decoding copies N total payload characters; k length prefixes require O(log M) digits each, where M is the maximum individual string length. Returned data occupies corresponding space.

### Problem description

Design an algorithm to encode a list of strings to a string . The encoded string is then sent over the network and is decoded back to the original list of strings. 
 
 Machine 1 (sender) has the function: 
 
```
string encode(vector<string> strs) {
 // ... your code
 return encoded_string;
}
```
 
Machine 2 (receiver) has the function:

```
vector<string> decode(string s) {
 //... your code
 return strs;
}
```

 So Machine 1 does: 
 
```
string encoded_string = encode(strs);
```

 and Machine 2 does: 
 
```
vector<string> strs2 = decode(encoded_string);
```

 strs2 in Machine 2 should be the same as strs in Machine 1. 
 
 Implement the encode and decode methods. 
 
 You are not allowed to solve the problem using any serialize methods (such as eval ). 

 Example 1: 
 
```
Input:
 dummy_input = ["Hello","World"]

Output:
 ["Hello","World"]

Explanation:

Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
```

 Example 2: 
 
```
Input:
 dummy_input = [""]

Output:
 [""]
```

 Constraints: 

 1 <= strs.length <= 200 
 
 0 <= strs[i].length <= 200 
 
 strs[i] contains any possible characters out of 256 valid ASCII characters. 

 Follow up: Could you write a generalized algorithm to work on any possible set of characters?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Codec {
public:
    string encode(vector<string>& strs) {
        string result;
        for (const string& s : strs) {
            result += to_string(s.size()) + "#" + s;
        }
        return result;
    }
    vector<string> decode(string s) {
        vector<string> result;
        size_t i = 0;
        while (i < s.size()) {
            size_t marker = s.find('#', i);
            size_t length = stoul(s.substr(i, marker - i));
            i = marker + 1;
            result.push_back(s.substr(i, length));
            i += length;
        }
        return result;
    }
};
```


## 273. Integer to English Words

**Problem:** https://leetcode.com/problems/integer-to-english-words/

**Difficulty:** Hard | **Premium:** No

**Tags:** Math, String, Recursion

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(log N)

**Space complexity:** O(log N)

**Complexity reasoning:** The fixed 31-entry vocabulary is scanned for each recursive magnitude, and generated English words plus recursive calls scale with the number of decimal digits.

### Problem description

Convert a non-negative integer num to its English words representation. 

 Example 1: 
 
```
Input:
 num = 123

Output:
 "One Hundred Twenty Three"
```

 Example 2: 
 
```
Input:
 num = 12345

Output:
 "Twelve Thousand Three Hundred Forty Five"
```

 Example 3: 
 
```
Input:
 num = 1234567

Output:
 "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

 Constraints: 

 0 <= num <= 2 31 - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
public:
  string numberToWords (int num)
  {
    vector < int >numbers = {
      1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20,
      19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    };

    vector < string > words = {
      "Billion", "Million", "Thousand", "Hundred", "Ninety", "Eighty",
      "Seventy", "Sixty", "Fifty", "Forty", "Thirty", "Twenty",
      "Nineteen", "Eighteen", "Seventeen", "Sixteen", "Fifteen", "Fourteen",
      "Thirteen", "Twelve", "Eleven", "Ten", "Nine", "Eight", "Seven",
      "Six", "Five", "Four", "Three", "Two", "One"
    };

    string result;

    for (int i = 0; i < 31; i++)
      {
	if (num >= numbers[i])
	  {
	    if (num >= 100)
	      result += numberToWords (num / numbers[i]) + " " + words[i] + " ";
	    else
	      result += words[i] + " ";

	    num %= numbers[i];

	    if (num == 0)
	      break;
	  }
      }

    return result.empty ()? "Zero" : result.substr (0, result.size () - 1);
  }
};
```


## 293. Flip Game

**Problem:** https://leetcode.com/problems/flip-game/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(n²)

**Complexity reasoning:** Up to n adjacent ++ pairs each trigger a full O(n) string copy, and all generated strings are retained.

### Problem description

You are playing a Flip Game with your friend. 
 
 You are given a string currentState that contains only '+' and '-' . You and your friend take turns to flip two consecutive "++" into "--" . The game ends when a person can no longer make a move, and therefore the other person will be the winner. 
 
 Return all possible states of the string currentState after one valid move . You may return the answer in any order . If there is no valid move, return an empty list [] . 

 Example 1: 
 
```
Input:
 currentState = "++++"

Output:
 ["--++","+--+","++--"]
```

 Example 2: 
 
```
Input:
 currentState = "+"

Output:
 []
```

 Constraints: 

 1 <= currentState.length <= 500 
 
 currentState[i] is either '+' or '-' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
public:
    vector<string> generatePossibleNextMoves(string currentState) {
        vector<string> result;
        for (int i = 0; i + 1 < (int)currentState.size(); ++i)
        {
            if (currentState[i] == '+' && currentState[i + 1] == '+')
            {
                string next = currentState;
                next[i] = '-';
                next[i + 1] = '-';
                result.push_back(next);
            }
        }
        return result;
    }
};
```


## 318. Maximum Product of Word Lengths

**Problem:** https://leetcode.com/problems/maximum-product-of-word-lengths/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String, Bit Manipulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(C + n²)

**Space complexity:** O(n)

**Complexity reasoning:** Building bitmasks examines C total word characters; every pair of n masks is checked, with one mask per word.

### Problem description

Given a string array words , return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters . If no such two words exist, return 0 . 

 Example 1: 
 
```
Input:
 words = ["abcw","baz","foo","bar","xtfn","abcdef"]

Output:
 16

Explanation:
 The two words can be "abcw", "xtfn".
```

 Example 2: 
 
```
Input:
 words = ["a","ab","abc","d","cd","bcd","abcd"]

Output:
 4

Explanation:
 The two words can be "ab", "cd".
```

 Example 3: 
 
```
Input:
 words = ["a","aa","aaa","aaaa"]

Output:
 0

Explanation:
 No such pair of words.
```

 Constraints: 

 2 <= words.length <= 1000 
 
 1 <= words[i].length <= 1000 
 
 words[i] consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int maxProduct(vector<string>& words) {
        int n = words.size();
        vector<int> masks(n, 0);
        for (int i = 0; i < n; ++i)
            for (char c : words[i]) masks[i] |= 1 << (c - 'a');
        int answer = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if ((masks[i] & masks[j]) == 0)
                    answer = max(answer,
                                 (int)(words[i].size() * words[j].size()));
            }
        }
        return answer;
    }
};
```


## 394. Decode String

**Problem:** https://leetcode.com/problems/decode-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack, Recursion

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + D²)

**Space complexity:** O(n + D)

**Complexity reasoning:** The input is scanned once, but repeated std::string concatenation while expanding nested groups can copy existing prefixes; D is decoded output length, and saved prefix strings occupy O(n+D).

### Problem description

Given an encoded string, return its decoded string. 
 
 The encoding rule is: k[encoded_string] , where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer. 
 
 You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k . For example, there will not be input like 3a or 2[4] . 
 
 The test cases are generated so that the length of the output will never exceed 10 5 . 

 Example 1: 
 
```
Input:
 s = "3[a]2[bc]"

Output:
 "aaabcbc"
```

 Example 2: 
 
```
Input:
 s = "3[a2[c]]"

Output:
 "accaccacc"
```

 Example 3: 
 
```
Input:
 s = "2[abc]3[cd]ef"

Output:
 "abcabccdcdcdef"
```

 Constraints: 

 1 <= s.length <= 30 
 
 s consists of lowercase English letters, digits, and square brackets '[]' . 
 
 s is guaranteed to be a valid input. 
 
 All the integers in s are in the range [1, 300] .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
   string decodeString(const string &s) {
    stack<string> strStack;
    stack<int> numStack;
    string currentStr = "";
    int currentNum = 0;

    for (char c : s) {
        if (isdigit(c)) {
            // Build the number
            currentNum = currentNum * 10 + (c - '0');
        } else if (c == '[') {
            // Push the current string and number onto their respective stacks
            strStack.push(currentStr);
            numStack.push(currentNum);

            // Reset current string and number
            currentStr = "";
            currentNum = 0;
        } else if (c == ']') {
            // Pop from the stacks
            string tempStr = currentStr;
            int repeatCount = numStack.top();
            numStack.pop();
            currentStr = strStack.top();
            strStack.pop();

            // Repeat the string and append it
            while (repeatCount-- > 0) {
                currentStr += tempStr;
            }
        } else {
            // Append current character to the current string
            currentStr += c;
        }
    }

    return currentStr;
}
};
```


## 405. Convert a Number to Hexadecimal

**Problem:** https://leetcode.com/problems/convert-a-number-to-hexadecimal/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String, Bit Manipulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Bit Manipulation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** A 32-bit integer needs at most eight hexadecimal digits, so the loop and resulting string have fixed bounds.

### Problem description

Given a 32-bit integer num , return a string representing its hexadecimal representation . For negative integers, two’s complement method is used. 
 
 All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself. 
 
 Note:  You are not allowed to use any built-in library method to directly solve this problem. 

 Example 1: 
 
```
Input:
 num = 26

Output:
 "1a"
```
 
 Example 2: 
 
```
Input:
 num = -1

Output:
 "ffffffff"
```

 Constraints: 

 -2 31 <= num <= 2 31 - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    string toHex(int num) {
        if (num == 0) return "0";
        unsigned int n = num;
        string hex = "";
        string digits = "0123456789abcdef";
        while (n) {
            hex = digits[n % 16] + hex;
            n /= 16;
        }
        return hex;
    }
};
```


## 412. Fizz Buzz

**Problem:** https://leetcode.com/problems/fizz-buzz/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n log n)

**Complexity reasoning:** The loop emits n strings; numeric entries are converted from integers with up to O(log n) digits, which also dominate stored output.

### Problem description

Given an integer n , return a string array answer ( 1-indexed ) where : 

 answer[i] == "FizzBuzz" if i is divisible by 3 and 5 . 
 
 answer[i] == "Fizz" if i is divisible by 3 . 
 
 answer[i] == "Buzz" if i is divisible by 5 . 
 
 answer[i] == i (as a string) if none of the above conditions are true. 

 Example 1: 
 
```
Input:
 n = 3

Output:
 ["1","2","Fizz"]
```
 
 Example 2: 
 
```
Input:
 n = 5

Output:
 ["1","2","Fizz","4","Buzz"]
```
 
 Example 3: 
 
```
Input:
 n = 15

Output:
 ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

 Constraints: 

 1 <= n <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer;
        answer.reserve(n);
        for (int i = 1; i <= n; ++i) {
            if (i % 15 == 0) answer.push_back("FizzBuzz");
            else if (i % 3 == 0) answer.push_back("Fizz");
            else if (i % 5 == 0) answer.push_back("Buzz");
            else answer.push_back(to_string(i));
        }
        return answer;
    }
};
```


## 415. Add Strings

**Problem:** https://leetcode.com/problems/add-strings/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + m)

**Space complexity:** O(max(n, m))

**Complexity reasoning:** Digits are added right-to-left once and the resulting decimal string is reversed in place.

### Problem description

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string . 
 
 You must solve the problem without using any built-in library for handling large integers (such as BigInteger ). You must also not convert the inputs to integers directly. 

 Example 1: 
 
```
Input:
 num1 = "11", num2 = "123"

Output:
 "134"
```

 Example 2: 
 
```
Input:
 num1 = "456", num2 = "77"

Output:
 "533"
```

 Example 3: 
 
```
Input:
 num1 = "0", num2 = "0"

Output:
 "0"
```

 Constraints: 

 1 <= num1.length, num2.length <= 10 4 
 
 num1 and num2 consist of only digits. 
 
 num1 and num2 don't have any leading zeros except for the zero itself.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string addStrings(string num1, string num2) {
        int i = num1.size() - 1, j = num2.size() - 1, carry = 0;
        string result = "";
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) sum += num1[i--] - '0';
            if (j >= 0) sum += num2[j--] - '0';
            result += (sum % 10) + '0';
            carry = sum / 10;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```


## 434. Number of Segments in a String

**Problem:** https://leetcode.com/problems/number-of-segments-in-a-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** A single pass detects transitions from spaces to non-spaces with one counter; the input parameter is passed by value.

### Problem description

Given a string s , return the number of segments in the string . 
 
 A segment is defined to be a contiguous sequence of non-space characters . 

 Example 1: 
 
```
Input:
 s = "Hello, my name is John"

Output:
 5

Explanation:
 The five segments are ["Hello,", "my", "name", "is", "John"]
```

 Example 2: 
 
```
Input:
 s = "Hello"

Output:
 1
```

 Constraints: 

 0 <= s.length <= 300 
 
 s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:" . 
 
 The only space character in s is ' ' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    int countSegments(string s) {
        int count = 0;
        for (int i = 0; i < s.size(); ++i)
            if (s[i] != ' ' && (i == 0 || s[i - 1] == ' '))
                count++;
        return count;
    }
};
```


## 439. Ternary Expression Parser

**Problem:** https://leetcode.com/problems/ternary-expression-parser/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** String, Stack, Recursion

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The expression is scanned backward, with each value pushed and popped a constant number of times; the stack can hold O(n) characters.

### Problem description

Given a string expression representing arbitrarily nested ternary expressions, evaluate the expression, and return the result of it . 
 
 You can always assume that the given expression is valid and only contains digits, '?' , ':' , 'T' , and 'F' where 'T' is true and 'F' is false. All the numbers in the expression are one-digit numbers (i.e., in the range [0, 9] ). 
 
 The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, 'T' or 'F' . 

 Example 1: 
 
```
Input:
 expression = "T?2:3"

Output:
 "2"

Explanation:
 If true, then result is 2; otherwise result is 3.
```

 Example 2: 
 
```
Input:
 expression = "F?1:T?4:5"

Output:
 "4"

Explanation:
 The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4"
or "(F ? 1 : (T ? 4 : 5))" --> "(T ? 4 : 5)" --> "4"
```

 Example 3: 
 
```
Input:
 expression = "T?T?F:5:3"

Output:
 "F"

Explanation:
 The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(T ? (T ? F : 5) : 3)" --> "(T ? F : 3)" --> "F"
"(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F"
```

 Constraints: 

 5 <= expression.length <= 10 4 
 
 expression consists of digits, 'T' , 'F' , '?' , and ':' . 
 
 It is guaranteed that expression is a valid ternary expression and that each number is a one-digit number .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string parseTernary(string expression) {
        stack<char> values;
        for (int i = static_cast<int>(expression.size()) - 1; i >= 0; --i) {
            char c = expression[i];
            if (c == '?') {
                continue;
            }
            if (c == ':') {
                continue;
            }
            if (i + 1 < static_cast<int>(expression.size()) && expression[i + 1] == '?') {
                char yes = values.top();
                values.pop();
                char no = values.top();
                values.pop();
                values.push(c == 'T' ? yes : no);
            } else {
                values.push(c);
            }
        }
        return string(1, values.top());
    }
};
```


## 459. Repeated Substring Pattern

**Problem:** https://leetcode.com/problems/repeated-substring-pattern/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²) worst case

**Space complexity:** O(n)

**Complexity reasoning:** The doubled string and its slice each require linear space; std::string::find performs a naive-compatible worst-case quadratic substring search.

### Problem description

Given a string s , check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 

 Example 1: 
 
```
Input:
 s = "abab"

Output:
 true

Explanation:
 It is the substring "ab" twice.
```

 Example 2: 
 
```
Input:
 s = "aba"

Output:
 false
```

 Example 3: 
 
```
Input:
 s = "abcabcabcabc"

Output:
 true

Explanation:
 It is the substring "abc" four times or the substring "abcabc" twice.
```

 Constraints: 

 1 <= s.length <= 10 4 
 
 s consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        string doubled = s + s;
        return doubled.substr(1, doubled.size() - 2).find(s) != string::npos;
    }
};
```


## 468. Validate IP Address

**Problem:** https://leetcode.com/problems/validate-ip-address/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The address is scanned for separators and tokenized; each token is validated once, and stringstream/token copies use linear storage (IP is passed by value).

### Problem description

Given a string queryIP , return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type. 
 
 A valid IPv4 address is an IP in the form "x 1 .x 2 .x 3 .x 4 " where 0 <= x i <= 255 and x i cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1" , "192.168.1.00" , and "192.168@1.1" are invalid IPv4 addresses. 
 
 A valid IPv6 address is an IP in the form "x 1 :x 2 :x 3 :x 4 :x 5 :x 6 :x 7 :x 8 " where: 

 1 <= x i .length <= 4 
 
 x i is a hexadecimal string which may contain digits, lowercase English letter ( 'a' to 'f' ) and upper-case English letters ( 'A' to 'F' ). 
 
 Leading zeros are allowed in x i . 

 For example, " 2001:0db8:85a3:0000:0000:8a2e:0370:7334" and " 2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while " 2001:0db8:85a3::8A2E:037j:7334" and " 02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses. 

 Example 1: 
 
```
Input:
 queryIP = "172.16.254.1"

Output:
 "IPv4"

Explanation:
 This is a valid IPv4 address, return "IPv4".
```

 Example 2: 
 
```
Input:
 queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output:
 "IPv6"

Explanation:
 This is a valid IPv6 address, return "IPv6".
```

 Example 3: 
 
```
Input:
 queryIP = "256.256.256.256"

Output:
 "Neither"

Explanation:
 This is neither a IPv4 address nor a IPv6 address.
```

 Constraints: 

 queryIP consists only of English letters, digits and the characters '.' and ':' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    string validIPAddress(string IP) {
        if (IP.find('.') != string::npos) {
            if (isIPv4(IP)) return "IPv4";
        } else if (IP.find(':') != string::npos) {
            if (isIPv6(IP)) return "IPv6";
        }
        return "Neither";
    }

    bool isIPv4(string ip) {
        stringstream ss(ip);
        string token;
        int count = 0;
        while (getline(ss, token, '.')) {
            if (++count > 4 || token.empty() || token.size() > 3 || (token[0] == '0' && token.size() > 1))
                return false;
            for (char c : token)
                if (!isdigit(c)) return false;
            if (stoi(token) > 255) return false;
        }
        return count == 4 && ip.back() != '.';
    }

    bool isIPv6(string ip) {
        stringstream ss(ip);
        string token;
        int count = 0;
        while (getline(ss, token, ':')) {
            if (++count > 8 || token.empty() || token.size() > 4) return false;
            for (char c : token)
                if (!isxdigit(c)) return false;
        }
        return count == 8 && ip.back() != ':';
    }
};
```


## 482. License Key Formatting

**Problem:** https://leetcode.com/problems/license-key-formatting/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** One pass removes dashes and uppercases characters; grouping copies each character once into the output.

### Problem description

You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k . 
 
 We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase. 
 
 Return the reformatted license key . 

 Example 1: 
 
```
Input:
 s = "5F3Z-2e-9-w", k = 4

Output:
 "5F3Z-2E9W"

Explanation:
 The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
```

 Example 2: 
 
```
Input:
 s = "2-5g-3-J", k = 2

Output:
 "2-5G-3J"

Explanation:
 The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists of English letters, digits, and dashes '-' . 
 
 1 <= k <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        string cleaned;
        for (char c : s)
            if (c != '-') cleaned += toupper(c);

        int firstGroup = cleaned.size() % k;
        string res = cleaned.substr(0, firstGroup);
        for (int i = firstGroup; i < cleaned.size(); i += k) {
            if (!res.empty()) res += '-';
            res += cleaned.substr(i, k);
        }
        return res;
    }
};
```


## 504. Base 7

**Problem:** https://leetcode.com/problems/base-7/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(d²)

**Space complexity:** O(d)

**Complexity reasoning:** Each of d base-7 digits is prepended to the result, shifting the existing prefix each time.

### Problem description

Given an integer num , return a string of its base 7 representation . 

 Example 1: 
 
```
Input:
 num = 100

Output:
 "202"
```
 
 Example 2: 
 
```
Input:
 num = -7

Output:
 "-10"
```

 Constraints: 

 -10 7 <= num <= 10 7

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    string convertToBase7(int num) {
        if (num == 0) return "0";
        bool neg = num < 0;
        num = abs(num);
        string res;
        while (num > 0) {
            res = to_string(num % 7) + res;
            num /= 7;
        }
        return neg ? "-" + res : res;
    }
};
```


## 520. Detect Capital

**Problem:** https://leetcode.com/problems/detect-capital/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** A single pass counts uppercase characters; only a counter is stored.

### Problem description

We define the usage of capitals in a word to be right when one of the following cases holds: 

 All letters in this word are capitals, like "USA" . 
 
 All letters in this word are not capitals, like "leetcode" . 
 
 Only the first letter in this word is capital, like "Google" . 

 Given a string word , return true if the usage of capitals in it is right. 

 Example 1: 
 
```
Input:
 word = "USA"

Output:
 true
```
 
 Example 2: 
 
```
Input:
 word = "FlaG"

Output:
 false
```

 Constraints: 

 1 <= word.length <= 100 
 
 word consists of lowercase and uppercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    bool detectCapitalUse(string word) {
        int upper = 0;
        for (char c : word)
            if (isupper(c)) upper++;

        return upper == word.size() || upper == 0 || (upper == 1 && isupper(word[0]));
    }
};
```


## 521. Longest Uncommon Subsequence I

**Problem:** https://leetcode.com/problems/longest-uncommon-subsequence-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + m)

**Space complexity:** O(1)

**Complexity reasoning:** String equality may compare every character; lengths are constant-time.

### Problem description

Given two strings a and b , return the length of the longest uncommon subsequence between a and b . If no such uncommon subsequence exists, return -1 . 
 
 An uncommon subsequence between two strings is a string that is a subsequence of exactly one of them . 

 Example 1: 
 
```
Input:
 a = "aba", b = "cdc"

Output:
 3

Explanation:
 One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.
```

 Example 2: 
 
```
Input:
 a = "aaa", b = "bbb"

Output:
 3

Explanation:
 The longest uncommon subsequences are "aaa" and "bbb".
```

 Example 3: 
 
```
Input:
 a = "aaa", b = "aaa"

Output:
 -1

Explanation:
 Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a. So the answer would be 
-1
.
```

 Constraints: 

 1 <= a.length, b.length <= 100 
 
 a and b consist of lower-case English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    int findLUSlength(string a, string b) {
        return a == b ? -1 : max(a.length(), b.length());
    }
};
```


## 537. Complex Number Multiplication

**Problem:** https://leetcode.com/problems/complex-number-multiplication/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + m)

**Space complexity:** O(n + m)

**Complexity reasoning:** Both inputs are copied into parse, scanned and sliced; the formatted result occupies linear space.

### Problem description

A complex number can be represented as a string on the form " real + imaginary i" where: 

 real is the real part and is an integer in the range [-100, 100] . 
 
 imaginary is the imaginary part and is an integer in the range [-100, 100] . 
 
 i 2 == -1 . 

 Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications . 

 Example 1: 
 
```
Input:
 num1 = "1+1i", num2 = "1+1i"

Output:
 "0+2i"

Explanation:
 (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
```

 Example 2: 
 
```
Input:
 num1 = "1+-1i", num2 = "1+-1i"

Output:
 "0+-2i"

Explanation:
 (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
```

 Constraints: 

 num1 and num2 are valid complex numbers.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    string complexNumberMultiply(string num1, string num2) {
        auto [a, b] = parse(num1);
        auto [c, d] = parse(num2);
        int real = a * c - b * d;
        int imag = a * d + b * c;
        return to_string(real) + "+" + to_string(imag) + "i";
    }

    pair<int, int> parse(string s) {
        int plus = s.find('+');
        int a = stoi(s.substr(0, plus));
        int b = stoi(s.substr(plus + 1, s.size() - plus - 2));
        return {a, b};
    }
};
```


## 539. Minimum Time Difference

**Problem:** https://leetcode.com/problems/minimum-time-difference/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Math, String, Sorting

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n)

**Complexity reasoning:** Convert n timestamps, sort their minute values, then scan adjacent and wraparound differences.

### Problem description

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list .

 Example 1: 
 
```
Input:
 timePoints = ["23:59","00:00"]

Output:
 1
```
 
 Example 2: 
 
```
Input:
 timePoints = ["00:00","23:59","00:00"]

Output:
 0
```

 Constraints: 

 2 <= timePoints.length <= 2 * 10 4 
 
 timePoints[i] is in the format "HH:MM" .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> minutes;
        for (string& t : timePoints) {
            int h = stoi(t.substr(0, 2));
            int m = stoi(t.substr(3));
            minutes.push_back(h * 60 + m);
        }

        sort(minutes.begin(), minutes.end());
        int minDiff = INT_MAX;

        for (int i = 1; i < minutes.size(); ++i)
            minDiff = min(minDiff, minutes[i] - minutes[i - 1]);

        minDiff = min(minDiff, 1440 - minutes.back() + minutes.front());
        return minDiff;
    }
};
```


## 544. Output Contest Matches

**Problem:** https://leetcode.com/problems/output-contest-matches/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** String, Recursion, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n log n)

**Complexity reasoning:** At each tournament round the code copies and wraps every team representation; total generated string length across rounds is O(n log n).

### Problem description

During the NBA playoffs, we always set the rather strong team to play with the rather weak team, like making the rank 1 team play with the rank n th team, which is a good strategy to make the contest more interesting. 
 
 Given n teams, return their final contest matches in the form of a string . 
 
 The n teams are labeled from 1 to n , which represents their initial rank (i.e., Rank 1 is the strongest team and Rank n is the weakest team). 
 
 We will use parentheses '(' , and ')' and commas ',' to represent the contest team pairing. We use the parentheses for pairing and the commas for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one. 

 Example 1: 
 
```
Input:
 n = 4

Output:
 "((1,4),(2,3))"

Explanation:

In the first round, we pair the team 1 and 4, the teams 2 and 3 together, as we need to make the strong team and weak team together.
And we got (1, 4),(2, 3).
In the second round, the winners of (1, 4) and (2, 3) need to play again to generate the final winner, so you need to add the paratheses outside them.
And we got the final answer ((1,4),(2,3)).
```

 Example 2: 
 
```
Input:
 n = 8

Output:
 "(((1,8),(4,5)),((2,7),(3,6)))"

Explanation:

First round: (1, 8),(2, 7),(3, 6),(4, 5)
Second round: ((1, 8),(4, 5)),((2, 7),(3, 6))
Third round: (((1, 8),(4, 5)),((2, 7),(3, 6)))
Since the third round will generate the final winner, you need to output the answer (((1,8),(4,5)),((2,7),(3,6))).
```

 Constraints: 

 n == 2 x where x in in the range [1, 12] .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string findContestMatch(int n) {
        vector<string> teams;
        for (int i = 1; i <= n; ++i) {
            teams.push_back(to_string(i));
        }
        while (teams.size() > 1) {
            vector<string> next;
            int size = teams.size();
            for (int i = 0; i < size / 2; ++i) {
                next.push_back("(" + teams[i] + "," + teams[size - 1 - i] + ")");
            }
            teams.swap(next);
        }
        return teams.front();
    }
};
```


## 551. Student Attendance Record I

**Problem:** https://leetcode.com/problems/student-attendance-record-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Scan attendance once while tracking absences and consecutive late arrivals.

### Problem description

You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters: 

 'A' : Absent. 
 
 'L' : Late. 
 
 'P' : Present. 

 The student is eligible for an attendance award if they meet both of the following criteria: 

 The student was absent ( 'A' ) for strictly fewer than 2 days total . 
 
 The student was never late ( 'L' ) for 3 or more consecutive days. 

 Return true if the student is eligible for an attendance award, or false otherwise . 

 Example 1: 
 
```
Input:
 s = "PPALLP"

Output:
 true

Explanation:
 The student has fewer than 2 absences and was never late 3 or more consecutive days.
```

 Example 2: 
 
```
Input:
 s = "PPALLL"

Output:
 false

Explanation:
 The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
```

 Constraints: 

 1 <= s.length <= 1000 
 
 s[i] is either 'A' , 'L' , or 'P' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
using namespace std;

class Solution {
public:
    bool checkRecord(string s) {
        int aCount = 0, lStreak = 0;
        for (char c : s) {
            if (c == 'A') {
                aCount++;
                if (aCount > 1) return false;
                lStreak = 0;
            } else if (c == 'L') {
                lStreak++;
                if (lStreak > 2) return false;
            } else {
                lStreak = 0;
            }
        }
        return true;
    }
};
```


## 564. Find the Closest Palindrome

**Problem:** https://leetcode.com/problems/find-the-closest-palindrome/

**Difficulty:** Hard | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** Ordered set, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(d)

**Space complexity:** O(d)

**Complexity reasoning:** Only a constant number of palindrome candidates are constructed from d-digit prefixes; each string conversion costs O(d).

### Problem description

Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome . If there is a tie, return the smaller one . 
 
 The closest is defined as the absolute difference minimized between two integers. 

 Example 1: 
 
```
Input:
 n = "123"

Output:
 "121"
```

 Example 2: 
 
```
Input:
 n = "1"

Output:
 "0"

Explanation:
 0 and 2 are the closest palindromes but we return the smallest which is 0.
```

 Constraints: 

 1 <= n.length <= 18 
 
 n consists of only digits. 
 
 n does not have leading zeros. 
 
 n is representing an integer in the range [1, 10 18 - 1] .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <cmath>
#include <set>

using namespace std;

class Solution {
public:
    string nearestPalindromic(string n) {
        long num = stol(n);
        int len = n.size();
        set<long> candidates;

        candidates.insert((long)pow(10, len) + 1);
        candidates.insert((long)pow(10, len - 1) - 1);

        long prefix = stol(n.substr(0, (len + 1) / 2));
        for (int i = -1; i <= 1; ++i) {
            string p = to_string(prefix + i);
            string pal = p + string(p.rbegin() + (len % 2), p.rend());
            candidates.insert(stol(pal));
        }

        candidates.erase(num);
        long res = -1, diff = LONG_MAX;
        for (long c : candidates) {
            if (abs(c - num) < diff || (abs(c - num) == diff && c < res)) {
                diff = abs(c - num);
                res = c;
            }
        }
        return to_string(res);
    }
};
```


## 591. Tag Validator

**Problem:** https://leetcode.com/problems/tag-validator/

**Difficulty:** Hard | **Premium:** No

**Tags:** String, Stack

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The parser advances through the code, using find to skip nonoverlapping segments and a stack of tag names.

### Problem description

Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid. 
 
 A code snippet is valid if all the following rules hold: 

 The code must be wrapped in a valid closed tag . Otherwise, the code is invalid. 
 
 A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME> . Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid. 
 
 A valid TAG_NAME only contain upper-case letters , and has length in range [1,9]. Otherwise, the TAG_NAME is invalid . 
 
 A valid TAG_CONTENT may contain other valid closed tags , cdata and any characters (see note1) EXCEPT unmatched < , unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid . 
 
 A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested. 
 
 A < is unmatched if you cannot find a subsequent > . And when you find a < or </ , all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid). 
 
 The cdata has the following format : <![CDATA[CDATA_CONTENT]]> . The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]> . 
 
 CDATA_CONTENT may contain any characters . The function of cdata is to forbid the validator to parse CDATA_CONTENT , so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters . 

 Example 1: 
 
```
Input:
 code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

Output:
 true

Explanation:
 
The code is wrapped in a closed tag : <DIV> and </DIV>. 
The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 
Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as a tag.
So TAG_CONTENT is valid, and then the code is valid. Thus return true.
```

 Example 2: 
 
```
Input:
 code = "<DIV>>> ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

Output:
 true

Explanation:

We first separate the code into : start_tag|tag_content|end_tag.
start_tag -> 
"<DIV>"

end_tag -> 
"</DIV>"

tag_content could also be separated into : text1|cdata|text2.
text1 -> 
">> ![cdata[]] "

cdata -> 
"<![CDATA[<div>]>]]>"
, where the CDATA_CONTENT is 
"<div>]>"

text2 -> 
"]]>>]"

The reason why start_tag is NOT 
"<DIV>>>"
 is because of the rule 6.
The reason why cdata is NOT 
"<![CDATA[<div>]>]]>]]>"
 is because of the rule 7.
```

 Example 3: 
 
```
Input:
 code = "<A> <B> </A> </B>"

Output:
 false

Explanation:
 Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.
```

 Constraints: 

 1 <= code.length <= 500 
 
 code consists of English letters, digits, '<' , '>' , '/' , '!' , '[' , ']' , '.' , and ' ' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool isValid(std::string code) {
        std::vector<std::string> st;
        int n = code.size();
        if (n == 0 || code[0] != '<') return false;
        for (int i = 0; i < n;) {
            if (i > 0 && st.empty()) return false;
            if (code.compare(i, 9, "<![CDATA[") == 0) {
                if (st.empty()) return false;
                size_t end = code.find("]]>", i + 9);
                if (end == std::string::npos) return false;
                i = (int)end + 3;
            } else if (code.compare(i, 2, "</") == 0) {
                size_t end = code.find('>', i + 2);
                if (end == std::string::npos || st.empty()) return false;
                std::string name = code.substr(i + 2, end - i - 2);
                if (name != st.back()) return false;
                st.pop_back();
                i = (int)end + 1;
            } else if (code[i] == '<') {
                size_t end = code.find('>', i + 1);
                if (end == std::string::npos) return false;
                std::string name = code.substr(i + 1, end - i - 1);
                if (name.empty() || name.size() > 9) return false;
                for (char c : name) if (c < 'A' || c > 'Z') return false;
                st.push_back(name);
                i = (int)end + 1;
            } else {
                if (st.empty()) return false;
                ++i;
            }
        }
        return st.empty();
    }
};
```


## 592. Fraction Addition and Subtraction

**Problem:** https://leetcode.com/problems/fraction-addition-and-subtraction/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String, Simulation, Euclidean Algorithm, Greatest Common Divisor

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + f log V)

**Space complexity:** O(1)

**Complexity reasoning:** Parse n characters across f fractions and reduce each accumulated numerator/denominator with gcd on values bounded by V.

### Problem description

Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format. 
 
 The final result should be an irreducible fraction . If your final result is an integer, change it to the format of a fraction that has a denominator 1 . So in this case, 2 should be converted to 2/1 . 

 Example 1: 
 
```
Input:
 expression = "-1/2+1/2"

Output:
 "0/1"
```

 Example 2: 
 
```
Input:
 expression = "-1/2+1/2+1/3"

Output:
 "1/3"
```

 Example 3: 
 
```
Input:
 expression = "1/3-1/2"

Output:
 "-1/6"
```

 Constraints: 

 The input string only contains '0' to '9' , '/' , '+' and '-' . So does the output. 
 
 Each fraction (input and output) has the format ±numerator/denominator . If the first input fraction or the output is positive, then '+' will be omitted. 
 
 The input only contains valid irreducible fractions , where the numerator and denominator of each fraction will always be in the range [1, 10] . If the denominator is 1 , it means this fraction is actually an integer in a fraction format defined above. 
 
 The number of given fractions will be in the range [1, 10] . 
 
 The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <numeric>

using namespace std;

class Solution {
public:
    string fractionAddition(string expression) {
        int num = 0, den = 1, i = 0;
        while (i < expression.size()) {
            int sign = 1;
            if (expression[i] == '-' || expression[i] == '+') sign = (expression[i++] == '-') ? -1 : 1;
            int n = 0;
            while (isdigit(expression[i])) n = n * 10 + (expression[i++] - '0');
            i++; // skip '/'
            int d = 0;
            while (i < expression.size() && isdigit(expression[i])) d = d * 10 + (expression[i++] - '0');
            num = num * d + sign * n * den;
            den *= d;
            int g = gcd(abs(num), den);
            num /= g; den /= g;
        }
        return to_string(num) + "/" + to_string(den);
    }
};
```


## 604. Design Compressed String Iterator

**Problem:** https://leetcode.com/problems/design-compressed-string-iterator/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, String, Design, Iterator

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n) initialization; O(1) amortized per operation

**Space complexity:** O(n)

**Complexity reasoning:** The constructor copies the compressed input; advance parses each run and its count once across all calls.

### Problem description

Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string. 
 
 Implement the StringIterator class: 

 next()  Returns the next character if the original string still has uncompressed characters, otherwise returns a white space . 
 
 hasNext()  Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false . 

 Example 1: 
 
```
Input

["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]

Output

[null, "L", "e", "e", "t", "C", "o", true, "d", true]

Explanation

StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
stringIterator.next(); // return "L"
stringIterator.next(); // return "e"
stringIterator.next(); // return "e"
stringIterator.next(); // return "t"
stringIterator.next(); // return "C"
stringIterator.next(); // return "o"
stringIterator.hasNext(); // return True
stringIterator.next(); // return "d"
stringIterator.hasNext(); // return True
```

 Constraints: 

 1 <= compressedString.length <= 1000 
 
 compressedString consists of lower-case an upper-case English letters and digits. 
 
 The number of a single character repetitions in  compressedString is in the range [1, 10^9] 
 
 At most 100 calls will be made to next and hasNext .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class StringIterator {
    string compressed;
    size_t index = 0;
    long long remaining = 0;
    char current = ' ';

    void advance() {
        if (remaining > 0 || index >= compressed.size()) {
            return;
        }
        current = compressed[index++];
        while (index < compressed.size() && isdigit(compressed[index])) {
            remaining = remaining * 10 + (compressed[index++] - '0');
        }
    }

public:
    StringIterator(string compressedString) : compressed(compressedString) {}

    char next() {
        advance();
        if (remaining == 0) {
            return ' ';
        }
        --remaining;
        return current;
    }

    bool hasNext() {
        advance();
        return remaining > 0;
    }
};
```


## 640. Solve the Equation

**Problem:** https://leetcode.com/problems/solve-the-equation/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String, Simulation, Linear Algebra

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The equation is split into two substrings, each parsed once with constant-size coefficient counters.

### Problem description

Solve a given equation and return the value of 'x' in the form of a string "x=#value" . The equation contains only '+' , '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation. 
 
 If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer. 

 Example 1: 
 
```
Input:
 equation = "x+5-3+x=6+x-2"

Output:
 "x=2"
```

 Example 2: 
 
```
Input:
 equation = "x=x"

Output:
 "Infinite solutions"
```

 Example 3: 
 
```
Input:
 equation = "2x=x"

Output:
 "x=0"
```

 Constraints: 

 3 <= equation.length <= 1000 
 
 equation has exactly one '=' . 
 
 equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x' . 
 
 The input is generated that if there is a single solution, it will be an integer.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    std::pair<int, int> parse(const std::string& s) {
        int coef = 0, constant = 0, sign = 1;
        for (int i = 0; i < (int)s.size();) {
            if (s[i] == '+') { sign = 1; ++i; continue; }
            if (s[i] == '-') { sign = -1; ++i; continue; }
            int num = 0, start = i;
            while (i < (int)s.size() && std::isdigit(s[i]))
                num = num * 10 + s[i++] - '0';
            if (i < (int)s.size() && s[i] == 'x') {
                coef += sign * (i == start ? 1 : num);
                ++i;
            } else constant += sign * num;
        }
        return {coef, constant};
    }
public:
    std::string solveEquation(std::string equation) {
        int eq = equation.find('=');
        auto a = parse(equation.substr(0, eq));
        auto b = parse(equation.substr(eq + 1));
        int coef = a.first - b.first;
        int value = b.second - a.second;
        if (coef == 0) return value == 0 ? "Infinite solutions" : "No solution";
        return "x=" + std::to_string(value / coef);
    }
};
```


## 657. Robot Return to Origin

**Problem:** https://leetcode.com/problems/robot-return-to-origin/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Each movement updates one of two coordinate counters exactly once.

### Problem description

There is a robot starting at the position (0, 0) , the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves. 
 
 You are given a string moves that represents the move sequence of the robot where moves[i] represents its i th move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down). 
 
 Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise . 
 
 Note : The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move. 

 Example 1: 
 
```
Input:
 moves = "UD"

Output:
 true

Explanation
: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
```

 Example 2: 
 
```
Input:
 moves = "LL"

Output:
 false

Explanation
: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
```

 Constraints: 

 1 <= moves.length <= 2 * 10 4 
 
 moves only contains the characters 'U' , 'D' , 'L' and 'R' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        for (char move : moves) {
            if (move == 'U') y++;
            else if (move == 'D') y--;
            else if (move == 'L') x--;
            else if (move == 'R') x++;
        }
        return x == 0 && y == 0;
    }
};
```


## 686. Repeated String Match

**Problem:** https://leetcode.com/problems/repeated-string-match/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm, Boyer–Moore String-Search Algorithm

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O((n + m) + (n + m)m) worst-case

**Space complexity:** O(n + m)

**Complexity reasoning:** Build a repeated string of length O(n+m), then call std::string::find up to twice; naive substring search can compare O((n+m)m) characters.

### Problem description

Given two strings a and b , return the minimum number of times you should repeat string a so that string b is a substring of it . If it is impossible for b ​​​​​​ to be a substring of a after repeating it, return -1 . 
 
 Notice: string "abc" repeated 0 times is "" , repeated 1 time is "abc" and repeated 2 times is "abcabc" . 

 Example 1: 
 
```
Input:
 a = "abcd", b = "cdabcdab"

Output:
 3

Explanation:
 We return 3 because by repeating a three times "ab
cdabcdab
cd", b is a substring of it.
```

 Example 2: 
 
```
Input:
 a = "a", b = "aa"

Output:
 2
```

 Constraints: 

 1 <= a.length, b.length <= 10 4 
 
 a and b consist of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
using namespace std;

class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        int count = 1;
        string repeated = a;
        while (repeated.size() < b.size()) {
            repeated += a;
            count++;
        }
        if (repeated.find(b) != string::npos) return count;
        repeated += a;
        return (repeated.find(b) != string::npos) ? count + 1 : -1;
    }
};
```


## 709. To Lower Case

**Problem:** https://leetcode.com/problems/to-lower-case/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Characters are lowercased in place in the by-value input string.

### Problem description

Given a string s , return the string after replacing every uppercase letter with the same lowercase letter . 

 Example 1: 
 
```
Input:
 s = "Hello"

Output:
 "hello"
```

 Example 2: 
 
```
Input:
 s = "here"

Output:
 "here"
```

 Example 3: 
 
```
Input:
 s = "LOVELY"

Output:
 "lovely"
```

 Constraints: 

 1 <= s.length <= 100 
 
 s consists of printable ASCII characters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <string>
using namespace std;

class Solution {
public:
    string toLowerCase(string str) {
        for (char& c : str) {
            if (isupper(c)) c = tolower(c);
        }
        return str;
    }
};
```


## 722. Remove Comments

**Problem:** https://leetcode.com/problems/remove-comments/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(N)

**Space complexity:** O(N)

**Complexity reasoning:** All source characters are scanned once, while the current line and collected output can hold O(N) characters.

### Problem description

Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the i th line of the source code. This represents the result of splitting the original source code string by the newline character '\n' . 
 
 In C++, there are two types of comments, line comments, and block comments. 

 The string "//" denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored. 
 
 The string "/*" denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of "*/" should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string "/*/" does not yet end the block comment, as the ending would be overlapping the beginning. 

 The first effective comment takes precedence over others. 

 For example, if the string "//" occurs in a block comment, it is ignored. 
 
 Similarly, if the string "/*" occurs in a line or block comment, it is also ignored. 

 If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty. 
 
 There will be no control characters, single quote, or double quote characters. 

 For example, source = "string s = "/* Not a comment. */";" will not be a test case. 

 Also, nothing else such as defines or macros will interfere with the comments. 
 
 It is guaranteed that every open block comment will eventually be closed, so "/*" outside of a line or block comment always starts a new comment. 
 
 Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details. 
 
 After removing the comments from the source code, return the source code in the same format . 

 Example 1: 
 
```
Input:
 source = ["/*Test program */", "int main()", "{ ", " // variable declaration ", "int a, b, c;", "/* This is a test", " multiline ", " comment for ", " testing */", "a = b + c;", "}"]

Output:
 ["int main()","{ "," ","int a, b, c;","a = b + c;","}"]

Explanation:
 The line by line code is visualized as below:
/*Test program */
int main()
{ 
 // variable declaration 
int a, b, c;
/* This is a test
 multiline 
 comment for 
 testing */
a = b + c;
}
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
The line by line output code is visualized as below:
int main()
{ 
 
int a, b, c;
a = b + c;
}
```

 Example 2: 
 
```
Input:
 source = ["a/*comment", "line", "more_comment*/b"]

Output:
 ["ab"]

Explanation:
 The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters. After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
```

 Constraints: 

 1 <= source.length <= 100 
 
 0 <= source[i].length <= 80 
 
 source[i] consists of printable ASCII characters. 
 
 Every open block comment is eventually closed. 
 
 There are no single-quote or double-quote in the input.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        vector<string> res;
        string line;
        bool inBlock = false;
        for (auto& src : source) {
            for (int i = 0; i < src.size(); ++i) {
                if (!inBlock && i + 1 < src.size() && src[i] == '/' && src[i + 1] == '*') {
                    inBlock = true;
                    ++i;
                } else if (inBlock && i + 1 < src.size() && src[i] == '*' && src[i + 1] == '/') {
                    inBlock = false;
                    ++i;
                } else if (!inBlock && i + 1 < src.size() && src[i] == '/' && src[i + 1] == '/') {
                    break;
                } else if (!inBlock) {
                    line += src[i];
                }
            }
            if (!inBlock && !line.empty()) {
                res.push_back(line);
                line.clear();
            }
        }
        return res;
    }
};
```


## 751. IP to CIDR

**Problem:** https://leetcode.com/problems/ip-to-cidr/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** String, Bit Manipulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Bit Manipulation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(log(n+1)) blocks, with fixed 32-bit address width

**Space complexity:** O(log(n+1)) output blocks

**Complexity reasoning:** Each iteration emits a maximal aligned CIDR block; the bit-selection loop and formatting are bounded by 32.

### Problem description

An IP address is a formatted 32-bit unsigned integer where each group of 8 bits is printed as a decimal number and the dot character '.' splits the groups. 

 For example, the binary number 00001111 10001000 11111111 01101011 (spaces added for clarity) formatted as an IP address would be "15.136.255.107" . 

 A CIDR block is a format used to denote a specific set of IP addresses. It is a string consisting of a base IP address, followed by a slash, followed by a prefix length k . The addresses it covers are all the IPs whose first k bits are the same as the base IP address. 

 For example, "123.45.67.89/20" is a CIDR block with a prefix length of 20 . Any IP address whose binary representation matches 01111011 00101101 0100xxxx xxxxxxxx , where x can be either 0 or 1 , is in the set covered by the CIDR block. 

 You are given a start IP address ip and the number of IP addresses we need to cover n . Your goal is to use as few CIDR blocks as possible to cover all the IP addresses in the inclusive range [ip, ip + n - 1] exactly . No other IP addresses outside of the range should be covered. 
 
 Return the shortest list of CIDR blocks that covers the range of IP addresses. If there are multiple answers, return any of them . 

 Example 1: 
 
```
Input:
 ip = "255.0.0.7", n = 10

Output:
 ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]

Explanation:

The IP addresses that need to be covered are:
- 255.0.0.7 -> 11111111 00000000 00000000 00000111
- 255.0.0.8 -> 11111111 00000000 00000000 00001000
- 255.0.0.9 -> 11111111 00000000 00000000 00001001
- 255.0.0.10 -> 11111111 00000000 00000000 00001010
- 255.0.0.11 -> 11111111 00000000 00000000 00001011
- 255.0.0.12 -> 11111111 00000000 00000000 00001100
- 255.0.0.13 -> 11111111 00000000 00000000 00001101
- 255.0.0.14 -> 11111111 00000000 00000000 00001110
- 255.0.0.15 -> 11111111 00000000 00000000 00001111
- 255.0.0.16 -> 11111111 00000000 00000000 00010000
The CIDR block "255.0.0.7/32" covers the first address.
The CIDR block "255.0.0.8/29" covers the middle 8 addresses (binary format of 11111111 00000000 00000000 00001xxx).
The CIDR block "255.0.0.16/32" covers the last address.
Note that while the CIDR block "255.0.0.0/28" does cover all the addresses, it also includes addresses outside of the range, so we cannot use it.
```

 Example 2: 
 
```
Input:
 ip = "117.145.102.62", n = 8

Output:
 ["117.145.102.62/31","117.145.102.64/30","117.145.102.68/31"]
```

 Constraints: 

 7 <= ip.length <= 15 
 
 ip is a valid IPv4 on the form "a.b.c.d" where a , b , c , and d are integers in the range [0, 255] . 
 
 1 <= n <= 1000 
 
 Every implied address ip + x (for x < n ) will be a valid IPv4 address.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    string format(unsigned long long address, int bits) {
        string result;
        for (int shift = 24; shift >= 0; shift -= 8) {
            if (!result.empty()) {
                result += ".";
            }
            result += to_string((address >> shift) & 255ULL);
        }
        return result + "/" + to_string(32 - bits);
    }

public:
    vector<string> ipToCIDR(string ip, int n) {
        unsigned long long address = 0;
        stringstream ss(ip);
        string part;
        while (getline(ss, part, '.')) {
            address = (address << 8) | stoull(part);
        }
        vector<string> answer;
        while (n > 0) {
            int bits = 0;
            while (bits < 32
                && address % (1ULL << (bits + 1)) == 0
                && (1ULL << (bits + 1)) <= static_cast<unsigned long long>(n)) {
                ++bits;
            }
            answer.push_back(format(address, bits));
            unsigned long long size = 1ULL << bits;
            address += size;
            n -= static_cast<int>(size);
        }
        return answer;
    }
};
```


## 761. Special Binary String

**Problem:** https://leetcode.com/problems/special-binary-string/

**Difficulty:** Hard | **Premium:** No

**Tags:** String, Divide and Conquer, Sorting

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Sorting / Divide and Conquer

**Data structures (inferred):** Sorted array, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n² log n) worst-case

**Space complexity:** O(n²) worst-case

**Complexity reasoning:** Recursive decomposition repeatedly copies nested substrings; sorting constructed sibling strings adds comparison costs.

### Problem description

Special binary strings are binary strings with the following two properties: 

 The number of 0 's is equal to the number of 1 's. 
 
 Every prefix of the binary string has at least as many 1 's as 0 's. 

 You are given a special binary string s . 
 
 A move consists of choosing two consecutive, non-empty, special substrings of s , and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string. 
 
 Return the lexicographically largest resulting string possible after applying the mentioned operations on the string . 

 Example 1: 
 
```
Input:
 s = "11011000"

Output:
 "11100100"

Explanation:
 The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
```

 Example 2: 
 
```
Input:
 s = "10"

Output:
 "10"
```

 Constraints: 

 1 <= s.length <= 50 
 
 s[i] is either '0' or '1' . 
 
 s is a special binary string.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string makeLargestSpecial(string s) {
        vector<string> subs;
        int count = 0, start = 0;
        for (int i = 0; i < s.size(); ++i) {
            count += s[i] == '1' ? 1 : -1;
            if (count == 0) {
                subs.push_back("1" + makeLargestSpecial(s.substr(start + 1, i - start - 1)) + "0");
                start = i + 1;
            }
        }
        sort(subs.rbegin(), subs.rend());
        string res;
        for (auto& sub : subs) res += sub;
        return res;
    }
};
```


## 772. Basic Calculator III

**Problem:** https://leetcode.com/problems/basic-calculator-iii/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Math, String, Stack, Recursion

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Recursive-descent parsing advances a shared position through the input; nested parentheses require O(n) call stack.

### Problem description

Implement a basic calculator to evaluate a simple expression string. 
 
 The expression string contains only non-negative integers, '+' , '-' , '*' , '/' operators, and open '(' and closing parentheses ')' . The integer division should truncate toward zero . 
 
 You may assume that the given expression is always valid. All intermediate results will be in the range of [-2 31 , 2 31 - 1] . 
 
 Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval() . 

 Example 1: 
 
```
Input:
 s = "1+1"

Output:
 2
```

 Example 2: 
 
```
Input:
 s = "6-4/2"

Output:
 4
```

 Example 3: 
 
```
Input:
 s = "2*(5+5*2)/3+(6/2+8)"

Output:
 21
```

 Constraints: 

 1 <= s <= 10 4 
 
 s consists of digits, '+' , '-' , '*' , '/' , '(' , and  ')' . 
 
 s is a valid expression.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    string input;
    int pos = 0;

    void spaces() {
        while (pos < static_cast<int>(input.size()) && input[pos] == ' ') {
            ++pos;
        }
    }

    long long factor() {
        spaces();
        int sign = 1;
        while (pos < static_cast<int>(input.size())
               && (input[pos] == '+' || input[pos] == '-')) {
            if (input[pos] == '-') {
                sign = -sign;
            }
            ++pos;
            spaces();
        }
        long long value = 0;
        if (input[pos] == '(') {
            ++pos;
            value = expression();
            spaces();
            ++pos;
        } else {
            while (pos < static_cast<int>(input.size())
                   && isdigit(input[pos])) {
                value = value * 10 + (input[pos++] - '0');
            }
        }
        return sign * value;
    }

    long long term() {
        long long value = factor();
        while (true) {
            spaces();
            if (pos >= static_cast<int>(input.size())
                || (input[pos] != '*' && input[pos] != '/')) {
                return value;
            }
            char op = input[pos++];
            long long rhs = factor();
            value = (op == '*') ? value * rhs : value / rhs;
        }
    }

    long long expression() {
        long long value = term();
        while (true) {
            spaces();
            if (pos >= static_cast<int>(input.size())
                || (input[pos] != '+' && input[pos] != '-')) {
                return value;
            }
            char op = input[pos++];
            long long rhs = term();
            value = (op == '+') ? value + rhs : value - rhs;
        }
    }

public:
    int calculate(string s) {
        input = s;
        pos = 0;
        return static_cast<int>(expression());
    }
};
```


## 796. Rotate String

**Problem:** https://leetcode.com/problems/rotate-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, String Matching

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²) worst-case

**Space complexity:** O(n)

**Complexity reasoning:** Construct s+s, then use std::string::find for goal; a naive search may test O(n) offsets of length O(n).

### Problem description

Given two strings s and goal , return true if and only if s can become goal after some number of shifts on s . 
 
 A shift on s consists of moving the leftmost character of s to the rightmost position. 

 For example, if s = "abcde" , then it will be "bcdea" after one shift. 

 Example 1: 

 Input: s = "abcde", goal = "cdeab" 
 
 Output: true 
 
 Explanation: 
 
 Rotating s to the left by 2 positions moves "ab" to the end, resulting in "cdeab" , which is equal to goal . 

 Example 2: 

 Input: s = "abcde", goal = "abced" 
 
 Output: false 
 
 Explanation: 
 
 No sequence of rotations of s can produce "abced" . The characters appear in a different relative order, so goal is not a rotation of s . 

 Constraints: 

 1 <= s.length, goal.length <= 100 
 
 s and goal consist of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool rotateString(string s, string goal) 
    {
        if (s.size() != goal.size())
        {
            return false ;
        }    
        if( (s+s).find(goal) != string::npos )
            return true ;
        
        return false ;
    }
};
```


## 800. Similar RGB Color

**Problem:** https://leetcode.com/problems/similar-rgb-color/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Math, String, Enumeration

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Exactly three two-digit hexadecimal components are parsed, rounded and appended.

### Problem description

The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand. 

 For example, "#15c" is shorthand for the color "#1155cc" . 

 The similarity between the two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV) 2 - (CD - WX) 2 - (EF - YZ) 2 . 
 
 Given a string color that follows the format "#ABCDEF" , return a string represents the color that is most similar to the given color and has a shorthand (i.e., it can be represented as some "#XYZ" ). 
 
 Any answer which has the same highest similarity as the best answer will be accepted. 

 Example 1: 
 
```
Input:
 color = "#09f166"

Output:
 "#11ee66"

Explanation:
 
The similarity is -(0x09 - 0x11)
2
 -(0xf1 - 0xee)
2
 - (0x66 - 0x66)
2
 = -64 -9 -0 = -73.
This is the highest among any shorthand color.
```

 Example 2: 
 
```
Input:
 color = "#4e3fe1"

Output:
 "#5544dd"
```

 Constraints: 

 color.length == 7 
 
 color[0] == '#' 
 
 color[i] is either digit or character in the range ['a', 'f'] for i > 0 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string similarRGB(string color) {
        const string hex = "0123456789abcdef";
        string answer = "#";
        for (int i = 1; i < 7; i += 2) {
            int value = stoi(color.substr(i, 2), nullptr, 16);
            int digit = (value + 8) / 17;
            digit = min(digit, 15);
            answer += hex[digit];
            answer += hex[digit];
        }
        return answer;
    }
};
```


## 806. Number of Lines To Write String

**Problem:** https://leetcode.com/problems/number-of-lines-to-write-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One pass accumulates letter widths, number of lines, and current line width.

### Problem description

You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a' , widths[1] is the width of 'b' , and so on. 
 
 You are trying to write s across several lines, where each line is no longer than 100 pixels . Starting at the beginning of s , write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s , continue writing as many letters as you can on the second line. Continue this process until you have written all of s . 
 
 Return an array result of length 2 where: 

 result[0] is the total number of lines. 
 
 result[1] is the width of the last line in pixels. 

 Example 1: 
 
```
Input:
 widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"

Output:
 [3,60]

Explanation:
 You can write s as follows:
abcdefghij // 100 pixels wide
klmnopqrst // 100 pixels wide
uvwxyz // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.
```

 Example 2: 
 
```
Input:
 widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"

Output:
 [2,4]

Explanation:
 You can write s as follows:
bbbcccdddaa // 98 pixels wide
a // 4 pixels wide
There are a total of 2 lines, and the last line is 4 pixels wide.
```

 Constraints: 

 widths.length == 26 
 
 2 <= widths[i] <= 10 
 
 1 <= s.length <= 1000 
 
 s contains only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        int lines = 1, width = 0;
        for (char c : s) {
            int w = widths[c - 'a'];
            if (width + w > 100) { ++lines; width = 0; }
            width += w;
        }
        return {lines, width};
    }
};
```


## 824. Goat Latin

**Problem:** https://leetcode.com/problems/goat-latin/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + w²)

**Space complexity:** O(n + w²)

**Complexity reasoning:** Each of w words extends a growing suffix of a characters, so total suffix/output length may be quadratic in word count.

### Problem description

You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only. 
 
 We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows: 

 If a word begins with a vowel ( 'a' , 'e' , 'i' , 'o' , or 'u' ), append "ma" to the end of the word.

 For example, the word "apple" becomes "applema" . 

 If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma" .

 For example, the word "goat" becomes "oatgma" . 

 Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1 .

 For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on. 

 Return the final sentence representing the conversion from sentence to Goat Latin . 

 Example 1: 
 
```
Input:
 sentence = "I speak Goat Latin"

Output:
 "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
```
 
 Example 2: 
 
```
Input:
 sentence = "The quick brown fox jumped over the lazy dog"

Output:
 "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
```

 Constraints: 

 1 <= sentence.length <= 150 
 
 sentence consists of English letters and spaces. 
 
 sentence has no leading or trailing spaces. 
 
 All the words in sentence are separated by a single space.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    string toGoatLatin(string sentence) {
        istringstream iss(sentence);
        string word, res, suffix = "a";
        while (iss >> word) {
            char first = word[0];
            if (string("aeiouAEIOU").find(first) != string::npos)
                word += "ma";
            else
                word = word.substr(1) + first + "ma";
            word += suffix;
            suffix += "a";
            if (!res.empty()) res += " ";
            res += word;
        }
        return res;
    }
};
```


## 830. Positions of Large Groups

**Problem:** https://leetcode.com/problems/positions-of-large-groups/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output

**Complexity reasoning:** Two indices scan maximal equal-character runs; the result stores up to O(n) start/end pairs.

### Problem description

In a string s  of lowercase letters, these letters form consecutive groups of the same character. 
 
 For example, a string like s = "abbxxxxzyy" has the groups "a" , "bb" , "xxxx" , "z" , and  "yy" . 
 
 A group is identified by an interval  [start, end] , where  start  and  end  denote the start and end indices (inclusive) of the group. In the above example,  "xxxx"  has the interval  [3,6] . 
 
 A group is considered  large  if it has 3 or more characters. 
 
 Return  the intervals of every large group sorted in  increasing order by start index . 

 Example 1: 
 
```
Input:
 s = "abbxxxxzzy"

Output:
 [[3,6]]

Explanation:
 
"xxxx" is the only 
large group with start index 3 and end index 6.
```

 Example 2: 
 
```
Input:
 s = "abc"

Output:
 []

Explanation:
 We have groups "a", "b", and "c", none of which are large groups.
```

 Example 3: 
 
```
Input:
 s = "abcdddeeeeaabbbcd"

Output:
 [[3,5],[6,9],[12,14]]

Explanation:
 The large groups are "ddd", "eeee", and "bbb".
```

 Constraints: 

 1 <= s.length <= 1000 
 
 s contains lowercase English letters only.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        vector<vector<int>> result;
        for (int i = 0, j; i < (int)s.size(); i = j) {
            j = i + 1;
            while (j < (int)s.size() && s[j] == s[i]) ++j;
            if (j - i >= 3) result.push_back({i, j - 1});
        }
        return result;
    }
};
```


## 831. Masking Personal Information

**Problem:** https://leetcode.com/problems/masking-personal-information/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Email masking lowercases and slices the input; phone masking collects digits before building the result.

### Problem description

You are given a personal information string s , representing either an email address or a phone number . Return the masked personal information using the below rules . 
 
 Email address: 
 
 An email address is: 

 A name consisting of at least two uppercase and lowercase English letters, followed by 
 
 The '@' symbol, followed by 
 
 The domain consisting of uppercase and lowercase English letters with a dot '.' somewhere in the middle (not the first or last character). 

 To mask an email: 

 The uppercase letters in the name and domain must be converted to lowercase letters. 
 
 The middle letters of the name (i.e., all but the first and last letters) must be replaced by 5 asterisks "*****" . 

 Phone number: 
 
 A phone number is formatted as follows: 

 The phone number contains 10-13 digits. 
 
 The last 10 digits make up the local number . 
 
 The remaining 0-3 digits, in the beginning, make up the country code . 
 
 Separation characters from the set {'+', '-', '(', ')', ' '} separate the above digits in some way. 

 To mask a phone number: 

 Remove all separation characters . 
 
 The masked phone number should have the form:

 "***-***-XXXX" if the country code has 0 digits. 
 
 "+*-***-***-XXXX" if the country code has 1 digit. 
 
 "+**-***-***-XXXX" if the country code has 2 digits. 
 
 "+***-***-***-XXXX" if the country code has 3 digits. 

 "XXXX" is the last 4 digits of the local number . 

 Example 1: 
 
```
Input:
 s = "LeetCode@LeetCode.com"

Output:
 "l*****e@leetcode.com"

Explanation:
 s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
```

 Example 2: 
 
```
Input:
 s = "AB@qq.com"

Output:
 "a*****b@qq.com"

Explanation:
 s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
Note that even though "ab" is 2 characters, it still must have 5 asterisks in the middle.
```

 Example 3: 
 
```
Input:
 s = "1(234)567-890"

Output:
 "***-***-7890"

Explanation:
 s is a phone number.
There are 10 digits, so the local number is 10 digits and the country code is 0 digits.
Thus, the resulting masked number is "***-***-7890".
```

 Constraints: 

 s is either a valid email or a phone number. 
 
 If s is an email:

 8 <= s.length <= 40 
 
 s consists of uppercase and lowercase English letters and exactly one '@' symbol and '.' symbol. 

 If s is a phone number:

 10 <= s.length <= 20 
 
 s consists of digits, spaces, and the symbols '(' , ')' , '-' , and '+' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string maskPII(string s) {
        if (s.find('@') != string::npos) {
            transform(s.begin(), s.end(), s.begin(), [](unsigned char c) { return tolower(c); });
            int at = s.find('@');
            return s.substr(0, 1) + "*****" + s.substr(at - 1, 1) + s.substr(at);
        }
        string digits;
        for (char c : s) if (isdigit(c)) digits += c;
        int country = (int)digits.size() - 10;
        string result = country ? "+" + string(country, '*') + "-" : "";
        return result + "***-***-" + digits.substr(digits.size() - 4);
    }
};
```


## 843. Guess the Word

**Problem:** https://leetcode.com/problems/guess-the-word/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Math, String, Minimax, Interactive, Game Theory

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash set, Ordered set, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(N² L) expected

**Space complexity:** O(NL)

**Complexity reasoning:** Each guess filters up to N remaining words, comparing L characters per candidate; the hash set stores N strings.

### Problem description

You are given an array of unique strings words where words[i] is six letters long. One word of words was chosen as a secret word. 
 
 You are also given the helper object Master . You may call Master.guess(word) where word is a six-letter-long string, and it must be from words . Master.guess(word) returns: 

 -1 if word is not from words , or 
 
 an integer representing the number of exact matches (value and position) of your guess to the secret word. 

 There is a parameter allowedGuesses for each test case where allowedGuesses is the maximum number of times you can call Master.guess(word) . 
 
 For each test case, you should call Master.guess with the secret word without exceeding the maximum number of allowed guesses. You will get: 

 "Either you took too many guesses, or you did not find the secret word." if you called Master.guess more than allowedGuesses times or if you did not call Master.guess with the secret word, or 
 
 "You guessed the secret word correctly." if you called Master.guess with the secret word with the number of calls to Master.guess less than or equal to allowedGuesses . 

 The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the bruteforce method). 

 Example 1: 
 
```
Input:
 secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10

Output:
 You guessed the secret word correctly.

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in words.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.
```

 Example 2: 
 
```
Input:
 secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10

Output:
 You guessed the secret word correctly.

Explanation:
 Since there are two words, you can guess both.
```

 Constraints: 

 1 <= words.length <= 100 
 
 words[i].length == 6 
 
 words[i] consist of lowercase English letters. 
 
 All the strings of words are unique . 
 
 secret exists in words . 
 
 10 <= allowedGuesses <= 30

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int solve(string s1, string s2) {
        int ans = 0;
        for (int i = 0; i < s1.size(); i++) {
            if (s1[i] == s2[i])
                ans++;
        }
        return ans;
    }

    void findSecretWord(vector<string>& words, Master& master) {
        unordered_set<string> st(words.begin(), words.end());

        while (!st.empty()) {
            string first = *st.begin();
            int guessed = master.guess(first);

            for (auto it = st.begin(); it!= st.end();) {
                if(solve(*it,first) != guessed) it = st.erase(it);
                else it++;
            }
            st.erase(first);
        }
    }
};
```


## 856. Score of Parentheses

**Problem:** https://leetcode.com/problems/score-of-parentheses/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack, Bracket Sequences

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each parenthesis is processed once, with a stack holding previous scores for nested groups.

### Problem description

Given a balanced parentheses string s , return the score of the string . 
 
 The score of a balanced parentheses string is based on the following rule: 

 "()" has score 1 . 
 
 AB has score A + B , where A and B are balanced parentheses strings. 
 
 (A) has score 2 * A , where A is a balanced parentheses string. 

 Example 1: 
 
```
Input:
 s = "()"

Output:
 1
```

 Example 2: 
 
```
Input:
 s = "(())"

Output:
 2
```

 Example 3: 
 
```
Input:
 s = "()()"

Output:
 2
```

 Constraints: 

 2 <= s.length <= 50 
 
 s consists of only '(' and ')' . 
 
 s is a balanced parentheses string.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    int scoreOfParentheses(string s)
	{
        stack<int> stack;
        int currentScore = 0;
        for(auto&c : s)
		{
            if(c == '(')
			{
                stack.push(currentScore);
                currentScore = 0;
            }
			else 
			{
                int lastScore = stack.top();
                stack.pop();
                currentScore = lastScore + std::max(1, 2 * currentScore);
            }
        }
        return currentScore;
    }
};
```


## 880. Decoded String at Index

**Problem:** https://leetcode.com/problems/decoded-string-at-index/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** A forward scan computes decoded length; a backward scan reduces the index without expanding the decoded string.

### Problem description

You are given an encoded string s . To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken: 

 If the character read is a letter, that letter is written onto the tape. 
 
 If the character read is a digit d , the entire current tape is repeatedly written d - 1 more times in total. 

 Given an integer k , return the k th letter ( 1-indexed) in the decoded string . 

 Example 1: 
 
```
Input:
 s = "leet2code3", k = 10

Output:
 "o"

Explanation:
 The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10
th
 letter in the string is "o".
```

 Example 2: 
 
```
Input:
 s = "ha22", k = 5

Output:
 "h"

Explanation:
 The decoded string is "hahahaha".
The 5
th
 letter is "h".
```

 Example 3: 
 
```
Input:
 s = "a2345678999999999999999", k = 1

Output:
 "a"

Explanation:
 The decoded string is "a" repeated 8301530446056247680 times.
The 1
st
 letter is "a".
```

 Constraints: 

 2 <= s.length <= 100 
 
 s consists of lowercase English letters and digits 2 through 9 . 
 
 s starts with a letter. 
 
 1 <= k <= 10 9 
 
 It is guaranteed that k is less than or equal to the length of the decoded string. 
 
 The decoded string is guaranteed to have less than 2 63 letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <string>
using namespace std;

class Solution {
public:
    string decodeAtIndex(string s, int k) {
        long long size = 0;
        for (char c : s) {
            if (isdigit(c)) size *= c - '0';
            else size++;
        }
        
        for (int i = s.size() - 1; i >= 0; --i) {
            k %= size;
            if (k == 0 && isalpha(s[i])) return string(1, s[i]);
            if (isdigit(s[i])) size /= s[i] - '0';
            else size--;
        }
        
        return "";
    }
};
```


## 899. Orderly Queue

**Problem:** https://leetcode.com/problems/orderly-queue/

**Difficulty:** Hard | **Premium:** No

**Tags:** Math, String, Sorting, Lexicographically Minimal String Rotation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Sorting / Divide and Conquer

**Data structures (inferred):** Sorted array, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n) if k > 1; O(n²) if k = 1

**Space complexity:** O(n)

**Complexity reasoning:** Sorting handles k>1; for k=1, construct and compare each of n rotations, each length n.

### Problem description

You are given a string s and an integer k . You can choose one of the first k letters of s and append it at the end of the string. 
 
 Return the lexicographically smallest string you could have after applying the mentioned step any number of moves . 

 Example 1: 
 
```
Input:
 s = "cba", k = 1

Output:
 "acb"

Explanation:
 
In the first move, we move the 1
st
 character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1
st
 character 'b' to the end, obtaining the final result "acb".
```

 Example 2: 
 
```
Input:
 s = "baaca", k = 3

Output:
 "aaabc"

Explanation:
 
In the first move, we move the 1
st
 character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3
rd
 character 'c' to the end, obtaining the final result "aaabc".
```

 Constraints: 

 1 <= k <= s.length <= 1000 
 
 s consist of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string orderlyQueue(string s, int k) {
        if (k > 1) {
            sort(s.begin(), s.end());
            return s;
        }

        string res = s;
        for (int i = 1; i < s.size(); ++i) {
            string rotated = s.substr(i) + s.substr(0, i);
            res = min(res, rotated);
        }
        return res;
    }
};
```


## 906. Super Palindromes

**Problem:** https://leetcode.com/problems/super-palindromes/

**Difficulty:** Hard | **Premium:** No

**Tags:** Math, String, Enumeration

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(K log R)

**Space complexity:** O(log R)

**Complexity reasoning:** Both loops enumerate at most K = 99,999 palindromic roots; constructing, squaring and checking each candidate takes O(log R) digit work. The temporary strings use O(log R) space.

### Problem description

Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome. 
 
 Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right] . 

 Example 1: 
 
```
Input:
 left = "4", right = "1000"

Output:
 4

Explanation
: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
```

 Example 2: 
 
```
Input:
 left = "1", right = "2"

Output:
 1
```

 Constraints: 

 1 <= left.length, right.length <= 18 
 
 left and right consist of only digits. 
 
 left and right cannot have leading zeros. 
 
 left and right represent integers in the range [1, 10 18 - 1] . 
 
 left is less than or equal to right .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <cmath>
using namespace std;

class Solution {
public:
    bool isPalindrome(long long x) {
        string s = to_string(x);
        int i = 0, j = s.size() - 1;
        while (i < j) {
            if (s[i++] != s[j--]) return false;
        }
        return true;
    }

    int superpalindromesInRange(string left, string right) {
        long long L = stoll(left), R = stoll(right), ans = 0;

        for (int k = 1; k < 100000; ++k) {
            string s = to_string(k), rs = s;
            reverse(rs.begin(), rs.end());
            long long val = stoll(s + rs);
            val *= val;
            if (val > R) break;
            if (val >= L && isPalindrome(val)) ++ans;
        }

        for (int k = 1; k < 100000; ++k) {
            string s = to_string(k), rs = s.substr(0, s.size() - 1);
            reverse(rs.begin(), rs.end());
            long long val = stoll(s + rs);
            val *= val;
            if (val > R) break;
            if (val >= L && isPalindrome(val)) ++ans;
        }

        return ans;
    }
};
```


## 937. Reorder Data in Log Files

**Problem:** https://leetcode.com/problems/reorder-data-in-log-files/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String, Sorting

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(N log N · L)

**Space complexity:** O(NL + N)

**Complexity reasoning:** stable_sort compares O(N log N) pairs of logs; each comparison scans or copies up to L characters via find, substr and string comparison. Stable sorting can use O(N) auxiliary entries; temporary substrings occupy O(L).

### Problem description

You are given an array of logs . Each log is a space-delimited string of words, where the first word is the identifier . 
 
 There are two types of logs: 

 Letter-logs : All words (except the identifier) consist of lowercase English letters. 
 
 Digit-logs : All words (except the identifier) consist of digits. 

 Reorder these logs so that: 

 The letter-logs come before all digit-logs . 
 
 The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers. 
 
 The digit-logs maintain their relative ordering. 

 Return the final order of the logs. 

 Example 1: 
 
```
Input:
 logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

Output:
 ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Explanation:

The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
```

 Example 2: 
 
```
Input:
 logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

Output:
 ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
```

 Constraints: 

 1 <= logs.length <= 100 
 
 3 <= logs[i].length <= 100 
 
 All the tokens of logs[i] are separated by a single space. 
 
 logs[i] is guaranteed to have an identifier and at least one word after the identifier.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        auto compare = [](const string& a, const string& b) {
            int posA = a.find(' '), posB = b.find(' ');
            bool isDigitA = isdigit(a[posA + 1]);
            bool isDigitB = isdigit(b[posB + 1]);
            
            if (!isDigitA && !isDigitB) {
                string subA = a.substr(posA + 1);
                string subB = b.substr(posB + 1);
                return subA == subB ? a < b : subA < subB;
            }
            return isDigitA ? false : true;
        };

        stable_sort(logs.begin(), logs.end(), compare);
        return logs;
    }
};
```


## 944. Delete Columns to Make Sorted

**Problem:** https://leetcode.com/problems/delete-columns-to-make-sorted/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String, Longest Increasing Subsequence

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(RC)

**Space complexity:** O(1)

**Complexity reasoning:** Each of C columns compares at most R adjacent row pairs, with early termination for unsorted columns.

### Problem description

You are given an array of n strings strs , all of the same length. 
 
 The strings can be arranged such that there is one on each line, making a grid. 

 For example, strs = ["abc", "bce", "cae"] can be arranged as follows: 

```
abc
bce
cae
```

 You want to delete the columns that are not sorted lexicographically . In the above example ( 0-indexed ), columns 0 ( 'a' , 'b' , 'c' ) and 2 ( 'c' , 'e' , 'e' ) are sorted, while column 1 ( 'b' , 'c' , 'a' ) is not, so you would delete column 1. 
 
 Return the number of columns that you will delete . 

 Example 1: 
 
```
Input:
 strs = ["cba","daf","ghi"]

Output:
 1

Explanation:
 The grid looks as follows:
 cba
 daf
 ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
```

 Example 2: 
 
```
Input:
 strs = ["a","b"]

Output:
 0

Explanation:
 The grid looks as follows:
 a
 b
Column 0 is the only column and is sorted, so you will not delete any columns.
```

 Example 3: 
 
```
Input:
 strs = ["zyx","wvu","tsr"]

Output:
 3

Explanation:
 The grid looks as follows:
 zyx
 wvu
 tsr
All 3 columns are not sorted, so you will delete all 3.
```

 Constraints: 

 n == strs.length 
 
 1 <= n <= 100 
 
 1 <= strs[i].length <= 1000 
 
 strs[i] consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int answer = 0;
        for (int col = 0; col < (int)strs[0].size(); ++col)
            for (int row = 1; row < (int)strs.size(); ++row)
                if (strs[row][col] < strs[row - 1][col]) {
                    ++answer;
                    break;
                }
        return answer;
    }
};
```


## 972. Equal Rational Numbers

**Problem:** https://leetcode.com/problems/equal-rational-numbers/

**Difficulty:** Hard | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(A + B + log V)

**Space complexity:** O(A + B)

**Complexity reasoning:** Parsing both strings scans their digits and constructs substrings; Euclidean gcd takes O(log V) arithmetic steps, where V bounds the computed integer values. Input strings are passed by value, and substrings take linear space.

### Problem description

Given two strings s and t , each of which represents a non-negative rational number, return true if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number. 
 
 A rational number can be represented using up to three parts: <IntegerPart> , <NonRepeatingPart> , and a <RepeatingPart> . The number will be represented in one of the following three ways: 

 <IntegerPart> 

 For example, 12 , 0 , and 123 . 

 <IntegerPart> <.> <NonRepeatingPart> 

 For example, 0.5 , 1. , 2.12 , and 123.0001 . 

 <IntegerPart> <.> <NonRepeatingPart> <(> <RepeatingPart> <)> 

 For example, 0.1(6) , 1.(9) , 123.00(1212) . 

 The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets. For example: 

 1/6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66) . 

 Example 1: 
 
```
Input:
 s = "0.(52)", t = "0.5(25)"

Output:
 true

Explanation:
 Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.
```

 Example 2: 
 
```
Input:
 s = "0.1666(6)", t = "0.166(66)"

Output:
 true
```

 Example 3: 
 
```
Input:
 s = "0.9(9)", t = "1."

Output:
 true

Explanation:
 "0.9(9)" represents 0.999999999... repeated forever, which equals 1. [
See this link for an explanation.
]
"1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".
```

 Constraints: 

 Each part consists only of digits. 
 
 The <IntegerPart> does not have leading zeros (except for the zero itself). 
 
 1 <= <IntegerPart>.length <= 4 
 
 0 <= <NonRepeatingPart>.length <= 4 
 
 1 <= <RepeatingPart>.length <= 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    using ll = long long;
    ll gcd(ll a, ll b) {
        while (b) { ll r = a % b; a = b; b = r; }
        return a;
    }
    pair<ll,ll> parse(const string& s) {
        int dot = s.find('.'), open = s.find('(');
        if (dot == (int)string::npos) return {stoll(s), 1};
        ll whole = stoll(s.substr(0, dot));
        string finite = s.substr(dot + 1, (open == (int)string::npos ? s.size() : open) - dot - 1);
        string repeat = open == (int)string::npos ? "" : s.substr(open + 1, s.size() - open - 2);
        ll p10 = 1;
        for (char c : finite) p10 *= 10;
        ll finiteVal = finite.empty() ? 0 : stoll(finite);
        ll numerator = whole * p10 + finiteVal, denominator = p10;
        if (!repeat.empty()) {
            ll power = 1;
            for (char c : repeat) power *= 10;
            ll factor = power - 1;
            numerator = numerator * factor + stoll(repeat);
            denominator *= factor;
        }
        ll g = gcd(numerator, denominator);
        return {numerator / g, denominator / g};
    }
public:
    bool isRationalEqual(string s, string t) {
        auto a = parse(s), b = parse(t);
        return (__int128)a.first * b.second == (__int128)b.first * a.second;
    }
};
```


## 1003. Check If Word Is Valid After Substitutions

**Problem:** https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each character is pushed once and at most three trailing characters are checked and erased; erasing the suffix is constant time. The simulated stack can hold n characters.

### Problem description

Given a string s , determine if it is valid . 
 
 A string s is valid if, starting with an empty string t = "" , you can transform t into s after performing the following operation any number of times : 

 Insert string "abc" into any position in t . More formally, t becomes t left + "abc" + t right , where t == t left + t right . Note that t left and t right may be empty . 

 Return true if s is a valid string, otherwise, return false . 

 Example 1: 
 
```
Input:
 s = "aabcbc"

Output:
 true

Explanation:

"" -> "
abc
" -> "a
abc
bc"
Thus, "aabcbc" is valid.
```

 Example 2: 
 
```
Input:
 s = "abcabcababcc"

Output:
 true

Explanation:

"" -> "
abc
" -> "abc
abc
" -> "abcabc
abc
" -> "abcabcab
abc
c"
Thus, "abcabcababcc" is valid.
```

 Example 3: 
 
```
Input:
 s = "abccba"

Output:
 false

Explanation:
 It is impossible to get "abccba" using the operation.
```

 Constraints: 

 1 <= s.length <= 2 * 10 4 
 
 s consists of letters 'a' , 'b' , and 'c'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        string stack;
        for (char c : s) {
            stack.push_back(c);
            if (stack.size() >= 3 && stack.substr(stack.size() - 3) == "abc") {
                stack.erase(stack.end() - 3, stack.end());
            }
        }
        return stack.empty();
    }
};
```


## 1021. Remove Outermost Parentheses

**Problem:** https://leetcode.com/problems/remove-outermost-parentheses/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Stack, Bracket Sequences

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** A single pass tracks nesting depth and appends non-outer parentheses to the result.

### Problem description

A valid parentheses string is either empty "" , "(" + A + ")" , or A + B , where A and B are valid parentheses strings, and + represents string concatenation. 

 For example, "" , "()" , "(())()" , and "(()(()))" are all valid parentheses strings. 

 A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B , with A and B nonempty valid parentheses strings. 
 
 Given a valid parentheses string s , consider its primitive decomposition: s = P 1 + P 2 + ... + P k , where P i are primitive valid parentheses strings. 
 
 Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s . 

 Example 1: 
 
```
Input:
 s = "(()())(())"

Output:
 "()()()"

Explanation:
 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
```

 Example 2: 
 
```
Input:
 s = "(()())(())(()(()))"

Output:
 "()()()()(())"

Explanation:
 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
```

 Example 3: 
 
```
Input:
 s = "()()"

Output:
 ""

Explanation:
 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s[i] is either '(' or ')' . 
 
 s is a valid parentheses string.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
using namespace std;

class Solution {
public:
    string removeOuterParentheses(string s) {
        string result;
        int count = 0;
        for (char c : s) {
            if (c == '(') {
                if (count > 0) result += c;
                count++;
            } else {
                count--;
                if (count > 0) result += c;
            }
        }
        return result;
    }
};
```


## 1041. Robot Bounded In Circle

**Problem:** https://leetcode.com/problems/robot-bounded-in-circle/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The robot processes every instruction once with constant-size direction state; the input string is passed by value, requiring O(n) storage.

### Problem description

On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that: 

 The north direction is the positive direction of the y-axis. 
 
 The south direction is the negative direction of the y-axis. 
 
 The east direction is the positive direction of the x-axis. 
 
 The west direction is the negative direction of the x-axis. 

 The robot can receive one of three instructions: 

 "G" : go straight 1 unit. 
 
 "L" : turn 90 degrees to the left (i.e., anti-clockwise direction). 
 
 "R" : turn 90 degrees to the right (i.e., clockwise direction). 

 The robot performs the instructions given in order, and repeats them forever. 
 
 Return true if and only if there exists a circle in the plane such that the robot never leaves the circle. 

 Example 1: 
 
```
Input:
 instructions = "GGLLGG"

Output:
 true

Explanation:
 The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.
```

 Example 2: 
 
```
Input:
 instructions = "GG"

Output:
 false

Explanation:
 The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
Based on that, we return false.
```

 Example 3: 
 
```
Input:
 instructions = "GL"

Output:
 true

Explanation:
 The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.
```

 Constraints: 

 1 <= instructions.length <= 100 
 
 instructions[i] is 'G' , 'L' or, 'R' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
       bool isRobotBounded(string instructions) {
        int x = 0, y = 0, i = 0;
        vector<vector<int>> d = {{0, 1}, {1, 0}, {0, -1}, { -1, 0}};
        for (char & ins : instructions)
            if (ins == 'R')
                i = (i + 1) % 4;
            else if (ins == 'L')
                i = (i + 3) % 4;
            else
                x += d[i][0], y += d[i][1];
        return x == 0 && y == 0 || i > 0;
    }
};
```


## 1047. Remove All Adjacent Duplicates In String

**Problem:** https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Stack

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each character is pushed onto or popped from the output string at most once.

### Problem description

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them. 
 
 We repeatedly make duplicate removals on s until we no longer can. 
 
 Return the final string after all such duplicate removals have been made . It can be proven that the answer is unique . 

 Example 1: 
 
```
Input:
 s = "abbaca"

Output:
 "ca"

Explanation:
 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move. The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
```

 Example 2: 
 
```
Input:
 s = "azxxzy"

Output:
 "ay"
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string removeDuplicates(string s) {
        string result;
        for (char c : s) {
            if (!result.empty() && result.back() == c)
                result.pop_back();
            else
                result.push_back(c);
        }
        return result;
    }
};
```


## 1071. Greatest Common Divisor of Strings

**Problem:** https://leetcode.com/problems/greatest-common-divisor-of-strings/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String, Euclidean Algorithm, Greatest Common Divisor

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + m)

**Space complexity:** O(n + m)

**Complexity reasoning:** The two concatenations and their comparison inspect O(n+m) characters; gcd of lengths takes logarithmic time and the returned prefix is at most min(n,m).

### Problem description

For two strings s and t , we say " t divides s " if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times). 
 
 Given two strings str1 and str2 , return the largest string x such that x divides both str1 and str2 . 

 Example 1: 

 Input: str1 = "ABCABC", str2 = "ABC" 
 
 Output: "ABC" 

 Example 2: 

 Input: str1 = "ABABAB", str2 = "ABAB" 
 
 Output: "AB" 

 Example 3: 

 Input: str1 = "LEET", str2 = "CODE" 
 
 Output: "" 

 Example 4: 

 Input: str1 = "AAAAAB", str2 = "AAA" 
 
 Output: "" ​​​​​​​ 

 Constraints: 

 1 <= str1.length, str2.length <= 1000 
 
 str1 and str2 consist of English uppercase letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
using namespace std;

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) return "";
        return str1.substr(0, gcd(str1.size(), str2.size()));
    }
    
    int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
};
```


## 1078. Occurrences After Bigram

**Problem:** https://leetcode.com/problems/occurrences-after-bigram/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + W·F)

**Space complexity:** O(n)

**Complexity reasoning:** Tokenization copies n text characters into words; scanning W words compares up to F characters in the two target words per candidate. Stored words and returned matches occupy O(n) space.

### Problem description

Given two strings first and second , consider occurrences in some text of the form "first second third" , where second comes immediately after first , and third comes immediately after second . 
 
 Return an array of all the words third for each occurrence of "first second third" . 

 Example 1: 
 
```
Input:
 text = "alice is a good girl she is a good student", first = "a", second = "good"

Output:
 ["girl","student"]
```
 
 Example 2: 
 
```
Input:
 text = "we will we will rock you", first = "we", second = "will"

Output:
 ["we","rock"]
```

 Constraints: 

 1 <= text.length <= 1000 
 
 text consists of lowercase English letters and spaces. 
 
 All the words in text are separated by a single space . 
 
 1 <= first.length, second.length <= 10 
 
 first and second consist of lowercase English letters. 
 
 text will not have any leading or trailing spaces.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> findOcurrences(string text, string first, string second) {
        vector<string> res;
        vector<string> words;
        string word;
        for (char c : text) {
            if (c == ' ') {
                words.push_back(word);
                word.clear();
            } else {
                word += c;
            }
        }
        words.push_back(word);
        for (int i = 0; i + 2 < words.size(); ++i) {
            if (words[i] == first && words[i + 1] == second) {
                res.push_back(words[i + 2]);
            }
        }
        return res;
    }
};
```


## 1106. Parsing A Boolean Expression

**Problem:** https://leetcode.com/problems/parsing-a-boolean-expression/

**Difficulty:** Hard | **Premium:** No

**Tags:** String, Stack, Recursion

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Hash set, Ordered set, Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n) expected

**Space complexity:** O(n)

**Complexity reasoning:** Each expression character enters and leaves the stack at most once. The small unordered_set created for each closing parenthesis contains only constant-many truth values; stack depth is O(n).

### Problem description

A boolean expression is an expression that evaluates to either true or false . It can be in one of the following shapes: 

 't' that evaluates to true . 
 
 'f' that evaluates to false . 
 
 '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr . 
 
 '&(subExpr 1 , subExpr 2 , ..., subExpr n )' that evaluates to the logical AND of the inner expressions subExpr 1 , subExpr 2 , ..., subExpr n where n >= 1 . 
 
 '|(subExpr 1 , subExpr 2 , ..., subExpr n )' that evaluates to the logical OR of the inner expressions subExpr 1 , subExpr 2 , ..., subExpr n where n >= 1 . 

 Given a string expression that represents a boolean expression , return the evaluation of that expression . 
 
 It is guaranteed that the given expression is valid and follows the given rules. 

 Example 1: 
 
```
Input:
 expression = "&(|(f))"

Output:
 false

Explanation:
 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
```

 Example 2: 
 
```
Input:
 expression = "|(f,f,f,t)"

Output:
 true

Explanation:
 The evaluation of (false OR false OR false OR true) is true.
```

 Example 3: 
 
```
Input:
 expression = "!(&(f,t))"

Output:
 true

Explanation:
 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
```

 Constraints: 

 1 <= expression.length <= 2 * 10 4 
 
 expression[i] is one following characters: '(' , ')' , '&' , '|' , '!' , 't' , 'f' , and ',' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> st;
        for (char ch : expression) {
            if (ch == ',') continue;
            else if (ch != ')') st.push(ch);
            else {
                unordered_set<char> seen;
                while (st.top() != '(') {
                    seen.insert(st.top());
                    st.pop();
                }
                st.pop(); // '('
                char op = st.top(); st.pop();
                if (op == '&') st.push(seen.count('f') ? 'f' : 't');
                else if (op == '|') st.push(seen.count('t') ? 't' : 'f');
                else st.push(seen.count('t') ? 'f' : 't');
            }
        }
        return st.top() == 't';
    }
};
```


## 1108. Defanging an IP Address

**Problem:** https://leetcode.com/problems/defanging-an-ip-address/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The input is scanned once and each character generates at most three output characters.

### Problem description

Given a valid (IPv4) IP address , return a defanged version of that IP address. 
 
 A defanged IP address  replaces every period "." with "[.]" . 

 Example 1: 
 
```
Input:
 address = "1.1.1.1"

Output:
 "1[.]1[.]1[.]1"
```
 
 Example 2: 
 
```
Input:
 address = "255.100.50.0"

Output:
 "255[.]100[.]50[.]0"
```

 Constraints: 

 The given address is a valid IPv4 address.

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <string>
using namespace std;

class Solution {
public:
    string defangIPaddr(string address) {
        string result = "";
        for (char c : address) {
            if (c == '.') result += "[.]";
            else result += c;
        }
        return result;
    }
};
```


## 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

**Problem:** https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack, Bracket Sequences

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** A single traversal assigns a parity to every parenthesis; the result vector has n elements.

### Problem description

A string is a valid parentheses string  (denoted VPS) if and only if it consists of "(" and ")" characters only, and: 

 It is the empty string, or 
 
 It can be written as  AB  ( A  concatenated with  B ), where  A  and  B  are VPS's, or 
 
 It can be written as  (A) , where  A  is a VPS. 

 We can similarly define the nesting depth depth(S) of any VPS S as follows: 

 depth("") = 0 
 
 depth(A + B) = max(depth(A), depth(B)) , where A and B are VPS's 
 
 depth("(" + A + ")") = 1 + depth(A) , where A is a VPS. 

 For example, "" ,  "()()" , and  "()(()())"  are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's. 
 
 Given a VPS seq , split it into two disjoint subsequences A and B , such that  A and B are VPS's (and  A.length + B.length = seq.length ). The subsequences may not necessarily be contiguous. 
 
 For example, for the sequence 123456789 , one possible split is: 

 A = {1, 3, 5, 7, 9} , 

 B = {2, 4, 6, 8} . 

 This corresponds to the output [0, 1, 0, 1, 0, 1, 0, 1, 0]  where 0 indicates membership in  A  and 1 indicates membership in  B . 
 
 Now choose any such A and B such that  max(depth(A), depth(B)) is the minimum possible value. 
 
 Return an answer array (of length seq.length ) that encodes such a choice of A and B :  answer[i] = 0 if seq[i] is part of A , else answer[i] = 1 .  Note that even though multiple answers may exist, you may return any of them. 

 Example 1: 
 
```
Input:
 seq = "(()())"

Output:
 [0,1,1,1,1,0]
```

 Example 2: 
 
```
Input:
 seq = "()(())()"

Output:
 [0,0,0,1,1,0,1,1]
```

 Constraints: 

 1 <= seq.size <= 10000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        vector<int> res(seq.size());
        int depth = 0;
        for (int i = 0; i < seq.size(); ++i) {
            if (seq[i] == '(') res[i] = depth++ % 2;
            else res[i] = --depth % 2;
        }
        return res;
    }
};
```


## 1119. Remove Vowels from a String

**Problem:** https://leetcode.com/problems/remove-vowels-from-a-string/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each character is checked against a fixed five-character vowel string and optionally copied into the result.

### Problem description

Given a string s , remove the vowels 'a' , 'e' , 'i' , 'o' , and 'u' from it, and return the new string. 

 Example 1: 
 
```
Input:
 s = "leetcodeisacommunityforcoders"

Output:
 "ltcdscmmntyfrcdrs"
```

 Example 2: 
 
```
Input:
 s = "aeiou"

Output:
 ""
```

 Constraints: 

 1 <= s.length <= 1000 
 
 s consists of only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string removeVowels(string s) {
        string result;
        for (char c : s) {
            if (string("aeiou").find(c) == string::npos) {
                result.push_back(c);
            }
        }
        return result;
    }
};
```


## 1154. Day of the Year

**Problem:** https://leetcode.com/problems/day-of-the-year/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Date substrings have fixed lengths, and the month loop processes at most 11 entries of a 12-element table.

### Problem description

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD , return the day number of the year . 

 Example 1: 
 
```
Input:
 date = "2019-01-09"

Output:
 9

Explanation:
 Given date is the 9th day of the year in 2019.
```

 Example 2: 
 
```
Input:
 date = "2019-02-10"

Output:
 41
```

 Constraints: 

 date.length == 10 
 
 date[4] == date[7] == '-' , and all other date[i] 's are digits 
 
 date represents a calendar date between Jan 1 st , 1900 and Dec 31 st , 2019.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
using namespace std;

class Solution {
public:
    int dayOfYear(string date) {
        int year = stoi(date.substr(0, 4));
        int month = stoi(date.substr(5, 2));
        int day = stoi(date.substr(8, 2));

        vector<int> days = { 31,28,31,30,31,30,31,31,30,31,30,31 };
        if ((year % 400 == 0) || (year % 100 != 0 && year % 4 == 0))
            days[1]++;

        int total = 0;
        for (int i = 0; i < month - 1; ++i) total += days[i];
        return total + day;
    }
};
```


## 1180. Count Substrings with Only One Distinct Letter

**Problem:** https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** The code maintains the current equal-character run length and accumulates its contribution in one pass.

### Problem description

Given a string s , return the number of substrings that have only one distinct letter . 

 Example 1: 
 
```
Input:
 s = "aaaba"

Output:
 8

Explanation: 
The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
```

 Example 2: 
 
```
Input:
 s = "aaaaaaaaaa"

Output:
 55
```

 Constraints: 

 1 <= s.length <= 1000 
 
 s[i] consists of only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int countLetters(string s) {
        int run = 0;
        int total = 0;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            if (i > 0 && s[i] == s[i - 1]) {
                ++run;
            } else {
                run = 1;
            }
            total += run;
        }
        return total;
    }
};
```


## 1190. Reverse Substrings Between Each Pair of Parentheses

**Problem:** https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack, Bracket Sequences

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(n)

**Complexity reasoning:** Although characters are read once, reversing nested substrings and concatenating stk.top() + curr can repeatedly copy the same characters at multiple nesting levels. Stack-held strings use O(n) total space.

### Problem description

You are given a string s that consists of lower case English letters and brackets. 
 
 Reverse the strings in each pair of matching parentheses, starting from the innermost one. 
 
 Your result should not contain any brackets. 

 Example 1: 
 
```
Input:
 s = "(abcd)"

Output:
 "dcba"
```

 Example 2: 
 
```
Input:
 s = "(u(love)i)"

Output:
 "iloveu"

Explanation:
 The substring "love" is reversed first, then the whole string is reversed.
```

 Example 3: 
 
```
Input:
 s = "(ed(et(oc))el)"

Output:
 "leetcode"

Explanation:
 First, we reverse the substring "oc", then "etco", and finally, the whole string.
```

 Constraints: 

 1 <= s.length <= 2000 
 
 s only contains lower case English characters and parentheses. 
 
 It is guaranteed that all parentheses are balanced.

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    string reverseParentheses(string s) {
        stack<string> stk;
        string curr = "";
        for (char c : s) {
            if (c == '(') {
                stk.push(curr);
                curr = "";
            } else if (c == ')') {
                reverse(curr.begin(), curr.end());
                curr = stk.top() + curr;
                stk.pop();
            } else {
                curr += c;
            }
        }
        return curr;
    }
};
```


## 1209. Remove All Adjacent Duplicates in String II

**Problem:** https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each input character updates or creates one stack run; eliminated runs are popped once. The final pass writes at most n surviving characters.

### Problem description

You are given a string s and an integer k , a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together. 
 
 We repeatedly make k duplicate removals on s until we no longer can. 
 
 Return the final string after all such duplicate removals have been made . It is guaranteed that the answer is unique . 

 Example 1: 
 
```
Input:
 s = "abcd", k = 2

Output:
 "abcd"

Explanation: 
There's nothing to delete.
```

 Example 2: 
 
```
Input:
 s = "deeedbbcccbdaa", k = 3

Output:
 "aa"

Explanation: 

First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
```

 Example 3: 
 
```
Input:
 s = "pbbcggttciiippooaais", k = 2

Output:
 "ps"
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 2 <= k <= 10 4 
 
 s only contains lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    string removeDuplicates(string s, int k) 
	{
        stack<pair<char, int>> st;
        string ans;
        for (int i = s.size() - 1; i >= 0; i--) 
		{
            char curr = s[i];
            if (!st.empty() && st.top().first == curr) 
			{
                st.top().second++;
                if (st.top().second == k) 
				{
                    st.pop();
                }
            } 
			else 
			{
                st.push({curr, 1});
            }
        }
        while (!st.empty()) 
		{
            char curr = st.top().first;
            while(st.top().second--)  
			{
				ans.push_back(curr);
			}
            st.pop();
        }
        return ans;
    }
};
```


## 1249. Minimum Remove to Make Valid Parentheses

**Problem:** https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** One scan matches parentheses using a stack and validity vector, followed by a second scan to construct the output.

### Problem description

Given a string s of '(' , ')' and lowercase English characters. 
 
 Your task is to remove the minimum number of parentheses ( '(' or ')' , in any positions ) so that the resulting parentheses string is valid and return any valid string. 
 
 Formally, a parentheses string is valid if and only if: 

 It is the empty string, contains only lowercase characters, or 
 
 It can be written as AB ( A concatenated with B ), where A and B are valid strings, or 
 
 It can be written as (A) , where A is a valid string. 

 Example 1: 
 
```
Input:
 s = "lee(t(c)o)de)"

Output:
 "lee(t(c)o)de"

Explanation:
 "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

 Example 2: 
 
```
Input:
 s = "a)b(c)d"

Output:
 "ab(c)d"
```

 Example 3: 
 
```
Input:
 s = "))(("

Output:
 ""

Explanation:
 An empty string is also valid.
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s[i] is either  '(' , ')' , or lowercase English letter.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    string minRemoveToMakeValid(string s) 
    {
        stack<pair<char,int>> stk;
        vector<int> vec(s.size(),0);
        for(int i=0;i<s.size();i++){
            if(!stk.empty() && stk.top().first == '(' && s[i] == ')')
            {
                int num = stk.top().second; 
                vec[num] = 1;
                stk.pop();
                vec[i] = 1;
            }
            else if(s[i] == ')' || s[i] == '(')
            {
                stk.push(make_pair(s[i],i));
            }
            else{
                vec[i] = 1;
            }
        }
        string res = "";
        for(int i=0;i<s.size();i++)
        {
            if(vec[i])
            {
                res += s[i];
            }
        }
        return res;
    }
};
```


## 1256. Encode Number

**Problem:** https://leetcode.com/problems/encode-number/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Math, String, Bit Manipulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Bit Manipulation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(log(num + 1))

**Space complexity:** O(log(num + 1))

**Complexity reasoning:** Each iteration shifts num+1 right by one bit and appends one output bit, then reverses the resulting string.

### Problem description

Given a non-negative integer num , Return its encoding string. 
 
 The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table: 
 
 [Figure: https://assets.leetcode.com/uploads/2019/06/21/encode_number.png] 

 Example 1: 
 
```
Input:
 num = 23

Output:
 "1000"
```

 Example 2: 
 
```
Input:
 num = 107

Output:
 "101100"
```

 Constraints: 

 0 <= num <= 10^9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string encode(int num) {
        long long value = static_cast<long long>(num) + 1;
        string result;
        while (value > 1) {
            result.push_back(char('0' + (value & 1)));
            value >>= 1;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```


## 1271. Hexspeak

**Problem:** https://leetcode.com/problems/hexspeak/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(d)

**Space complexity:** O(d)

**Complexity reasoning:** stoull parses the d-digit decimal input and repeated division generates at most O(d) hexadecimal digits, stored in the answer.

### Problem description

A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit '0' with the letter 'O' , and the digit '1' with the letter 'I' . Such a representation is valid if and only if it consists only of the letters in the set {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'} . 
 
 Given a string num representing a decimal integer n , return the Hexspeak representation of n if it is valid, otherwise return "ERROR" . 

 Example 1: 
 
```
Input:
 num = "257"

Output:
 "IOI"

Explanation:
 257 is 101 in hexadecimal.
```

 Example 2: 
 
```
Input:
 num = "3"

Output:
 "ERROR"
```

 Constraints: 

 1 <= num.length <= 12 
 
 num does not contain leading zeros. 
 
 num represents an integer in the range [1, 10 12 ] .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string toHexspeak(string num) {
        unsigned long long value = stoull(num);
        const string hex = "0123456789ABCDEF";
        string answer;
        while (value > 0) {
            int digit = value % 16;
            if (digit >= 2 && digit <= 9) {
                return "ERROR";
            }
            answer.push_back(digit == 0 ? 'O' : (digit == 1 ? 'I' : hex[digit]));
            value /= 16;
        }
        reverse(answer.begin(), answer.end());
        return answer;
    }
};
```


## 1309. Decrypt String from Alphabet to Integer Mapping

**Problem:** https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The scan consumes either one digit or a fixed two-digit code plus #, then reverses the decoded output.

### Problem description

You are given a string s formed by digits and '#' . We want to map s to English lowercase characters as follows: 

 Characters ( 'a' to 'i' ) are represented by ( '1' to '9' ) respectively. 
 
 Characters ( 'j' to 'z' ) are represented by ( '10#' to '26#' ) respectively. 

 Return the string formed after mapping . 
 
 The test cases are generated so that a unique mapping will always exist. 

 Example 1: 
 
```
Input:
 s = "10#11#12"

Output:
 "jkab"

Explanation:
 "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
```

 Example 2: 
 
```
Input:
 s = "1326#"

Output:
 "acz"
```

 Constraints: 

 1 <= s.length <= 1000 
 
 s consists of digits and the '#' letter. 
 
 s will be a valid string such that mapping is always possible.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    string freqAlphabets(string s) {
        string res;
        for (int i = s.size() - 1; i >= 0; --i) {
            if (s[i] == '#') {
                int val = stoi(s.substr(i - 2, 2));
                res += 'a' + val - 1;
                i -= 2;
            } else {
                res += 'a' + (s[i] - '0') - 1;
            }
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```


## 1324. Print Words Vertically

**Problem:** https://leetcode.com/problems/print-words-vertically/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + MW)

**Space complexity:** O(n + MW)

**Complexity reasoning:** Parsing copies n input characters into words; for maximum word length M and W words, the nested loops build M rows of up to W characters each.

### Problem description

Given a string s . Return all the words vertically in the same order in which they appear in s . 
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed). 
Each word would be put on only one column and that in one column there will be only one word. 

 Example 1: 
 
```
Input:
 s = "HOW ARE YOU"

Output:
 ["HAY","ORO","WEU"]

Explanation: 
Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"
```

 Example 2: 
 
```
Input:
 s = "TO BE OR NOT TO BE"

Output:
 ["TBONTB","OEROOE"," T"]

Explanation: 
Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
" T"
```

 Example 3: 
 
```
Input:
 s = "CONTEST IS COMING"

Output:
 ["CIC","OSO","N M","T I","E N","S G","T"]
```

 Constraints: 

 1 <= s.length <= 200 
 
 s  contains only upper case English letters. 
 
 It's guaranteed that there is only one space between 2 words.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    vector<string> printVertically(string s) {
        istringstream iss(s);
        vector<string> words, res;
        string word;
        int maxLen = 0;
        while (iss >> word) {
            words.push_back(word);
            maxLen = max(maxLen, (int)word.size());
        }

        for (int i = 0; i < maxLen; ++i) {
            string line;
            for (string& w : words)
                line += i < w.size() ? w[i] : ' ';
            while (!line.empty() && line.back() == ' ') line.pop_back();
            res.push_back(line);
        }
        return res;
    }
};
```


## 1360. Number of Days Between Two Dates

**Problem:** https://leetcode.com/problems/number-of-days-between-two-dates/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Each date uses fixed-size substrings, constant arithmetic and a loop over at most 11 months.

### Problem description

Write a program to count the number of days between two dates. 
 
 The two dates are given as strings, their format is YYYY-MM-DD  as shown in the examples. 

 Example 1: 
 
```
Input:
 date1 = "2019-06-29", date2 = "2019-06-30"

Output:
 1
```
 
 Example 2: 
 
```
Input:
 date1 = "2020-01-15", date2 = "2019-12-31"

Output:
 15
```

 Constraints: 

 The given dates are valid dates between the years 1971 and 2100 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    bool leap(int y) { return y % 400 == 0 || (y % 4 == 0 && y % 100 != 0); }
    int days(string s) {
        int y = stoi(s.substr(0, 4)), m = stoi(s.substr(5, 2));
        int d = stoi(s.substr(8, 2));
        int total = 365 * (y - 1) + (y - 1) / 4 - (y - 1) / 100 + (y - 1) / 400;
        int md[] = {31,28,31,30,31,30,31,31,30,31,30,31};
        for (int i = 1; i < m; ++i) total += md[i - 1] + (i == 2 && leap(y));
        return total + d;
    }
public:
    int daysBetweenDates(string date1, string date2) {
        return abs(days(date1) - days(date2));
    }
};
```


## 1374. Generate a String With Characters That Have Odd Counts

**Problem:** https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Constructing the repeated-character output writes n characters.

### Problem description

Given an integer n , return a string with n  characters such that each character in such string occurs an odd number of times . 
 
 The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.   

 Example 1: 
 
```
Input:
 n = 4

Output:
 "pppz"

Explanation:
 "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
```

 Example 2: 
 
```
Input:
 n = 2

Output:
 "xy"

Explanation:
 "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
```

 Example 3: 
 
```
Input:
 n = 7

Output:
 "holasss"
```

 Constraints: 

 1 <= n <= 500

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    string generateTheString(int n) {
        if (n % 2 == 1) return string(n, 'a');
        return string(n - 1, 'a') + 'b';
    }
};
```


## 1404. Number of Steps to Reduce a Number in Binary Representation to One

**Problem:** https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Bit Manipulation, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The algorithm scans the binary digits once from right to left using two counters; the input string is passed by value.

### Problem description

Given the binary representation of an integer as a string s , return the number of steps to reduce it to 1 under the following rules : 

 If the current number is even, you have to divide it by 2 . 

 If the current number is odd, you have to add 1 to it. 

 It is guaranteed that you can always reach one for all test cases. 

 Example 1: 
 
```
Input:
 s = "1101"

Output:
 6

Explanation:
 "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.
```

 Example 2: 
 
```
Input:
 s = "10"

Output:
 1

Explanation:
 "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.
```

 Example 3: 
 
```
Input:
 s = "1"

Output:
 0
```

 Constraints: 

 1 <= s.length <= 500 
 
 s consists of characters '0' or '1' 
 
 s[0] == '1'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    int numSteps(string s) {
        int steps = 0, carry = 0;
        for (int i = s.size() - 1; i > 0; --i) {
            if ((s[i] - '0' + carry) % 2 == 0) steps += 1;
            else {
                steps += 2;
                carry = 1;
            }
        }
        return steps + carry;
    }
};
```


## 1408. String Matching in an Array

**Problem:** https://leetcode.com/problems/string-matching-in-an-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String, String Matching

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(W²L²)

**Space complexity:** O(WL)

**Complexity reasoning:** Every ordered pair of W words may be tested with std::string::find, which has O(L²) worst-case matching cost for word lengths up to L. The returned strings can occupy O(WL) space.

### Problem description

Given an array of string words , return all strings in words that are a substring of another word. You can return the answer in any order . 

 Example 1: 
 
```
Input:
 words = ["mass","as","hero","superhero"]

Output:
 ["as","hero"]

Explanation:
 "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
```

 Example 2: 
 
```
Input:
 words = ["leetcode","et","code"]

Output:
 ["et","code"]

Explanation:
 "et", "code" are substring of "leetcode".
```

 Example 3: 
 
```
Input:
 words = ["blue","green","bu"]

Output:
 []

Explanation:
 No string of words is substring of another string.
```

 Constraints: 

 1 <= words.length <= 100 
 
 1 <= words[i].length <= 30 
 
 words[i] contains only lowercase English letters. 
 
 All the strings of words are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        vector<string> res;
        for (int i = 0; i < words.size(); ++i) {
            for (int j = 0; j < words.size(); ++j) {
                if (i != j && words[j].find(words[i]) != string::npos) {
                    res.push_back(words[i]);
                    break;
                }
            }
        }
        return res;
    }
};
```


## 1417. Reformat The String

**Problem:** https://leetcode.com/problems/reformat-the-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The input is split into letter and digit buffers and then interleaved in a second linear pass.

### Problem description

You are given an alphanumeric string s . ( Alphanumeric string is a string consisting of lowercase English letters and digits). 
 
 You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type. 
 
 Return the reformatted string or return an empty string if it is impossible to reformat the string. 

 Example 1: 
 
```
Input:
 s = "a0b1c2"

Output:
 "0a1b2c"

Explanation:
 No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
```

 Example 2: 
 
```
Input:
 s = "leetcode"

Output:
 ""

Explanation:
 "leetcode" has only characters so we cannot separate them by digits.
```

 Example 3: 
 
```
Input:
 s = "1229857369"

Output:
 ""

Explanation:
 "1229857369" has only digits so we cannot separate them by characters.
```

 Constraints: 

 1 <= s.length <= 500 
 
 s consists of only lowercase English letters and/or digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string reformat(string s) {
        string letters, digits;
        for (char c : s) {
            if (isdigit((unsigned char)c)) digits += c;
            else letters += c;
        }
        if (abs((int)letters.size() - (int)digits.size()) > 1) return "";
        if (digits.size() > letters.size()) swap(digits, letters);
        string ans;
        for (int i = 0; i < (int)letters.size(); ++i) {
            ans += letters[i];
            if (i < (int)digits.size()) ans += digits[i];
        }
        return ans;
    }
};
```


## 1427. Perform String Shifts

**Problem:** https://leetcode.com/problems/perform-string-shifts/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + q)

**Space complexity:** O(n)

**Complexity reasoning:** The q shift operations are reduced to one net rotation; two substrings and their concatenation copy O(n) characters.

### Problem description

You are given a string s containing lowercase English letters, and a matrix shift , where shift[i] = [direction i , amount i ] : 

 direction i can be 0 (for left shift) or 1 (for right shift). 
 
 amount i is the amount by which string s is to be shifted. 
 
 A left shift by 1 means remove the first character of s and append it to the end. 
 
 Similarly, a right shift by 1 means remove the last character of s and add it to the beginning. 

 Return the final string after all operations. 

 Example 1: 
 
```
Input:
 s = "abc", shift = [[0,1],[1,2]]

Output:
 "cab"

Explanation:
 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
```

 Example 2: 
 
```
Input:
 s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]

Output:
 "efgabcd"

Explanation:
  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
```

 Constraints: 

 1 <= s.length <= 100 
 
 s only contains lower case English letters. 
 
 1 <= shift.length <= 100 
 
 shift[i].length == 2 
 
 direction i is either 0 or 1 . 
 
 0 <= amount i <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string stringShift(string s, vector<vector<int>>& shift) {
        int n = s.size();
        if (n == 0) {
            return s;
        }
        int right = 0;
        for (const auto& operation : shift) {
            right += operation[0] == 1 ? operation[1] : -operation[1];
            right %= n;
        }
        right = (right + n) % n;
        return s.substr(n - right) + s.substr(0, n - right);
    }
};
```


## 1446. Consecutive Characters

**Problem:** https://leetcode.com/problems/consecutive-characters/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** One scan tracks the length of the current run. The string argument is passed by value, so its copy occupies O(n) space.

### Problem description

The power of the string is the maximum length of a non-empty substring that contains only one unique character. 
 
 Given a string s , return the power of s . 

 Example 1: 
 
```
Input:
 s = "leetcode"

Output:
 2

Explanation:
 The substring "ee" is of length 2 with the character 'e' only.
```

 Example 2: 
 
```
Input:
 s = "abbcccddddeeeeedcba"

Output:
 5

Explanation:
 The substring "eeeee" is of length 5 with the character 'e' only.
```

 Constraints: 

 1 <= s.length <= 500 
 
 s consists of only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
using namespace std;

class Solution {
public:
    int maxPower(string s) {
        int maxLen = 1, curLen = 1;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i - 1]) {
                curLen++;
                maxLen = max(maxLen, curLen);
            } else {
                curLen = 1;
            }
        }
        return maxLen;
    }
};
```


## 1447. Simplified Fractions

**Problem:** https://leetcode.com/problems/simplified-fractions/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String, Number Theory, Euclidean Algorithm, Greatest Common Divisor

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n² log n)

**Space complexity:** O(n² log n)

**Complexity reasoning:** Enumerates O(n²) numerator/denominator pairs; each gcd takes O(log n). Output strings occupy O(n² log n) characters in the worst case.

### Problem description

Given an integer n , return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n . You can return the answer in any order . 

 Example 1: 
 
```
Input:
 n = 2

Output:
 ["1/2"]

Explanation:
 "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
```

 Example 2: 
 
```
Input:
 n = 3

Output:
 ["1/2","1/3","2/3"]
```

 Example 3: 
 
```
Input:
 n = 4

Output:
 ["1/2","1/3","1/4","2/3","3/4"]

Explanation:
 "2/4" is not a simplified fraction because it can be simplified to "1/2".
```

 Constraints: 

 1 <= n <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <numeric>
using namespace std;

class Solution {
public:
    vector<string> simplifiedFractions(int n) {
        vector<string> res;
        for (int i = 1; i < n; ++i)
            for (int j = i + 1; j <= n; ++j)
                if (gcd(i, j) == 1)
                    res.push_back(to_string(i) + "/" + to_string(j));
        return res;
    }
};
```


## 1451. Rearrange Words in a Sentence

**Problem:** https://leetcode.com/problems/rearrange-words-in-a-sentence/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Sorting

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Sorting / Divide and Conquer

**Data structures (inferred):** Sorted array, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(L + w log w + L)

**Space complexity:** O(L + w)

**Complexity reasoning:** Tokenizes L characters into w words, stable-sorts by word length in O(w log w) comparisons, and rebuilds the output. Word storage and result take O(L) space; stable_sort can allocate O(w) temporary storage.

### Problem description

Given a sentence  text (A  sentence  is a string of space-separated words) in the following format: 

 First letter is in upper case. 
 
 Each word in text are separated by a single space. 

 Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order. 
 
 Return the new text following the format shown above. 

 Example 1: 
 
```
Input:
 text = "Leetcode is cool"

Output:
 "Is cool leetcode"

Explanation: 
There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
Output is ordered by length and the new first word starts with capital letter.
```

 Example 2: 
 
```
Input:
 text = "Keep calm and code on"

Output:
 "On and keep calm code"

Explanation: 
Output is ordered as follows:
"On" 2 letters.
"and" 3 letters.
"keep" 4 letters in case of tie order by position in original text.
"calm" 4 letters.
"code" 4 letters.
```

 Example 3: 
 
```
Input:
 text = "To be or not to be"

Output:
 "To be or to be not"
```

 Constraints: 

 text begins with a capital letter and then contains lowercase letters and single space between words. 
 
 1 <= text.length <= 10^5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string arrangeWords(string text) {
        vector<string> words;
        stringstream ss(text);
        string word;
        while (ss >> word) {
            word[0] = tolower(word[0]);
            words.push_back(word);
        }
        stable_sort(words.begin(), words.end(), [](const string& a, const string& b) {
            return a.size() < b.size();
        });
        words[0][0] = toupper(words[0][0]);
        string res;
        for (string& w : words) res += w + " ";
        res.pop_back();
        return res;
    }
};
```


## 1507. Reformat Date

**Problem:** https://leetcode.com/problems/reformat-date/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** Hash map, Ordered map, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** The date has fixed length, and the 12-entry month map, substring extraction, and formatting have bounded cost.

### Problem description

Given a date string in the form  Day Month Year , where: 

 Day  is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"} . 
 
 Month  is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"} . 
 
 Year  is in the range [1900, 2100] . 

 Convert the date string to the format YYYY-MM-DD , where: 

 YYYY denotes the 4 digit year. 
 
 MM denotes the 2 digit month. 
 
 DD denotes the 2 digit day. 

 Example 1: 
 
```
Input:
 date = "20th Oct 2052"

Output:
 "2052-10-20"
```

 Example 2: 
 
```
Input:
 date = "6th Jun 1933"

Output:
 "1933-06-06"
```

 Example 3: 
 
```
Input:
 date = "26th May 1960"

Output:
 "1960-05-26"
```

 Constraints: 

 The given dates are guaranteed to be valid, so no error handling is necessary.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string reformatDate(string date) {
        unordered_map<string, string> month = {
            {"Jan","01"},{"Feb","02"},{"Mar","03"},{"Apr","04"},{"May","05"},{"Jun","06"},
            {"Jul","07"},{"Aug","08"},{"Sep","09"},{"Oct","10"},{"Nov","11"},{"Dec","12"}
        };
        string day = date.substr(0, date.find_first_not_of("0123456789"));
        if (day.size() == 1) day = "0" + day;
        string mon = month[date.substr(date.find(' ') + 1, 3)];
        string year = date.substr(date.size() - 4);
        return year + "-" + mon + "-" + day;
    }
};
```


## 1513. Number of Substrings With Only 1s

**Problem:** https://leetcode.com/problems/number-of-substrings-with-only-1s/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Scans each character once and accumulates the triangular count for each contiguous run of ones.

### Problem description

Given a binary string s , return the number of substrings with all characters 1 's . Since the answer may be too large, return it modulo 10 9 + 7 . 

 Example 1: 
 
```
Input:
 s = "0110111"

Output:
 9

Explanation:
 There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
```

 Example 2: 
 
```
Input:
 s = "101"

Output:
 2

Explanation:
 Substring "1" is shown 2 times in s.
```

 Example 3: 
 
```
Input:
 s = "111111"

Output:
 21

Explanation:
 Each substring contains only 1's characters.
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s[i] is either '0' or '1' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    int numSub(string s) {
        const int MOD = 1e9 + 7;
        long res = 0, count = 0;
        for (char c : s) {
            if (c == '1') count++;
            else {
                res += count * (count + 1) / 2;
                count = 0;
            }
        }
        res += count * (count + 1) / 2;
        return res % MOD;
    }
};
```


## 1528. Shuffle String

**Problem:** https://leetcode.com/problems/shuffle-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Allocates a result of length n and writes each input character directly to its indexed destination.

### Problem description

You are given a string s and an integer array indices of the same length . The string s will be shuffled such that the character at the i th position moves to indices[i] in the shuffled string. 
 
 Return the shuffled string . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/07/09/q1.jpg] 
 
```
Input:
 s = "codeleet", 
indices
 = [4,5,6,7,0,2,1,3]

Output:
 "leetcode"

Explanation:
 As shown, "codeleet" becomes "leetcode" after shuffling.
```

 Example 2: 
 
```
Input:
 s = "abc", 
indices
 = [0,1,2]

Output:
 "abc"

Explanation:
 After shuffling, each character remains in its position.
```

 Constraints: 

 s.length == indices.length == n 
 
 1 <= n <= 100 
 
 s consists of only lowercase English letters. 
 
 0 <= indices[i] < n 
 
 All values of indices are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string result(s.size(), ' ');
        for (int i = 0; i < s.size(); ++i) {
            result[indices[i]] = s[i];
        }
        return result;
    }
};
```


## 1544. Make The String Great

**Problem:** https://leetcode.com/problems/make-the-string-great/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Stack

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each character is pushed at most once and popped at most once from the result used as a stack.

### Problem description

Given a string s of lower and upper case English letters. 
 
 A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where: 

 0 <= i <= s.length - 2 
 
 s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa . 

 To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good. 
 
 Return the string after making it good. The answer is guaranteed to be unique under the given constraints. 
 
 Notice that an empty string is also good. 

 Example 1: 
 
```
Input:
 s = "leEeetcode"

Output:
 "leetcode"

Explanation:
 In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
```

 Example 2: 
 
```
Input:
 s = "abBAcC"

Output:
 ""

Explanation:
 We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
```

 Example 3: 
 
```
Input:
 s = "s"

Output:
 "s"
```

 Constraints: 

 1 <= s.length <= 100 
 
 s contains only lower and upper case English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    string makeGood(string s) {
        string res;
        for (char c : s) {
            if (!res.empty() && abs(res.back() - c) == 32)
                res.pop_back();
            else
                res.push_back(c);
        }
        return res;
    }
};
```


## 1545. Find Kth Bit in Nth Binary String

**Problem:** https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Recursion, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each call recurses into only one half of the conceptual string, reducing the level by one; recursion depth is n.

### Problem description

Given two positive integers n and k , the binary string S n is formed as follows: 

 S 1 = "0" 
 
 S i = S i - 1 + "1" + reverse(invert(S i - 1 )) for i > 1 

 Where + denotes the concatenation operation, reverse(x) returns the reversed string x , and invert(x) inverts all the bits in x ( 0 changes to 1 and 1 changes to 0 ). 
 
 For example, the first four strings in the above sequence are: 

 S 1 = "0" 
 
 S 2 = "0 1 1" 
 
 S 3 = "011 1 001" 
 
 S 4 = "0111001 1 0110001" 

 Return the k th bit in S n . It is guaranteed that k is valid for the given n . 

 Example 1: 
 
```
Input:
 n = 3, k = 1

Output:
 "0"

Explanation:
 S
3
 is "
0
111001".
The 1
st
 bit is "0".
```

 Example 2: 
 
```
Input:
 n = 4, k = 11

Output:
 "1"

Explanation:
 S
4
 is "0111001101
1
0001".
The 11
th
 bit is "1".
```

 Constraints: 

 1 <= n <= 20 
 
 1 <= k <= 2 n - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    char findKthBit(int n, int k) {
        if (n == 1) return '0';
        int len = (1 << n) - 1, mid = len / 2 + 1;
        if (k == mid) return '1';
        if (k < mid) return findKthBit(n - 1, k);
        char ch = findKthBit(n - 1, len - k + 1);
        return ch == '0' ? '1' : '0';
    }
};
```


## 1556. Thousand Separator

**Problem:** https://leetcode.com/problems/thousand-separator/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(d)

**Space complexity:** O(d)

**Complexity reasoning:** Converts the integer to d decimal digits and scans them once to insert separators; both strings take O(d) space.

### Problem description

Given an integer n , add a dot (".") as the thousands separator and return it in string format. 

 Example 1: 
 
```
Input:
 n = 987

Output:
 "987"
```

 Example 2: 
 
```
Input:
 n = 1234

Output:
 "1.234"
```

 Constraints: 

 0 <= n <= 2 31 - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    string thousandSeparator(int n) {
        if (n == 0) return "0";
        string s = to_string(n), res;
        int len = s.size();
        for (int i = 0; i < len; ++i) {
            if (i && (len - i) % 3 == 0) res += '.';
            res += s[i];
        }
        return res;
    }
};
```


## 1573. Number of Ways to Split a String

**Problem:** https://leetcode.com/problems/number-of-ways-to-split-a-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Counts ones in one pass and counts valid cut positions in a second pass; only scalar counters are used.

### Problem description

Given a binary string s , you can split s into 3 non-empty strings s1 , s2 , and s3 where s1 + s2 + s3 = s . 
 
 Return the number of ways s can be split such that the number of ones is the same in s1 , s2 , and s3 . Since the answer may be too large, return it modulo 10 9 + 7 . 

 Example 1: 
 
```
Input:
 s = "10101"

Output:
 4

Explanation:
 There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"
```

 Example 2: 
 
```
Input:
 s = "1001"

Output:
 0
```

 Example 3: 
 
```
Input:
 s = "0000"

Output:
 3

Explanation:
 There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"
```

 Constraints: 

 3 <= s.length <= 10 5 
 
 s[i] is either '0' or '1' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int numWays(string s) {
        const int MOD = 1e9 + 7;
        int ones = 0;
        for (char c : s) if (c == '1') ones++;
        if (ones % 3 != 0) return 0;
        if (ones == 0) return (long long)(s.size() - 1) * (s.size() - 2) / 2 % MOD;

        int t = ones / 3, cnt = 0, a = 0, b = 0;
        for (char c : s) {
            if (c == '1') cnt++;
            if (cnt == t) a++;
            else if (cnt == 2 * t) b++;
        }
        return (long long)a * b % MOD;
    }
};
```


## 1576. Replace All ?'s to Avoid Consecutive Repeating Characters

**Problem:** https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Scans the mutable string once and tests at most three candidate letters per question mark; edits the by-value input in place.

### Problem description

Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters. 
 
 It is guaranteed that there are no consecutive repeating characters in the given string except for '?' . 
 
 Return the final string after all the conversions (possibly zero) have been made . If there is more than one solution, return any of them . It can be shown that an answer is always possible with the given constraints. 

 Example 1: 
 
```
Input:
 s = "?zs"

Output:
 "azs"

Explanation:
 There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
```

 Example 2: 
 
```
Input:
 s = "ubv?w"

Output:
 "ubvaw"

Explanation:
 There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
```

 Constraints: 

 1 <= s.length <= 100 
 
 s consist of lowercase English letters and '?' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string modifyString(string s) {
        for (int i = 0; i < (int)s.size(); ++i) {
            if (s[i] != '?') continue;
            for (char c = 'a'; c <= 'c'; ++c) {
                if ((i == 0 || s[i - 1] != c) &&
                    (i + 1 == (int)s.size() || s[i + 1] != c)) {
                    s[i] = c; break;
                }
            }
        }
        return s;
    }
};
```


## 1592. Rearrange Spaces Between Words

**Problem:** https://leetcode.com/problems/rearrange-spaces-between-words/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Counts spaces, tokenizes the text, and rebuilds a string of the same total length; words and output require linear storage.

### Problem description

You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word . 
 
 Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized . If you cannot redistribute all the spaces equally, place the extra spaces at the end , meaning the returned string should be the same length as text . 
 
 Return the string after rearranging the spaces . 

 Example 1: 
 
```
Input:
 text = " this is a sentence "

Output:
 "this is a sentence"

Explanation:
 There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
```

 Example 2: 
 
```
Input:
 text = " practice makes perfect"

Output:
 "practice makes perfect "

Explanation:
 There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.
```

 Constraints: 

 1 <= text.length <= 100 
 
 text consists of lowercase English letters and ' ' . 
 
 text contains at least one word.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <sstream>
#include <vector>
using namespace std;

class Solution {
public:
    string reorderSpaces(string text) {
        int space = 0;
        for (char c : text)
            if (c == ' ') space++;

        stringstream ss(text);
        string word;
        vector<string> words;
        while (ss >> word) words.push_back(word);

        int gaps = words.size() - 1;
        string res;
        if (gaps == 0) {
            res = words[0] + string(space, ' ');
        } else {
            int even = space / gaps, rem = space % gaps;
            for (int i = 0; i < words.size(); ++i) {
                res += words[i];
                if (i < words.size() - 1)
                    res += string(even, ' ');
            }
            res += string(rem, ' ');
        }
        return res;
    }
};
```


## 1598. Crawler Log Folder

**Problem:** https://leetcode.com/problems/crawler-log-folder/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String, Stack

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Stack, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(m)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Processes m log entries once, updating a single directory-depth counter; string comparisons have bounded length for the specified log format.

### Problem description

The Leetcode file system keeps a log each time some user performs a change folder operation. 
 
 The operations are described below: 

 "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder ). 
 
 "./" : Remain in the same folder. 
 
 "x/" : Move to the child folder named x (This folder is guaranteed to always exist ). 

 You are given a list of strings logs where logs[i] is the operation performed by the user at the i th step. 
 
 The file system starts in the main folder, then the operations in logs are performed. 
 
 Return the minimum number of operations needed to go back to the main folder after the change folder operations. 

 Example 1: 
 
 [Figure: https://assets.leetcode.com/uploads/2020/09/09/sample_11_1957.png] 
 
```
Input:
 logs = ["d1/","d2/","../","d21/","./"]

Output:
 2

Explanation: 
Use this change folder operation "../" 2 times and go back to the main folder.
```

 Example 2: 
 
 [Figure: https://assets.leetcode.com/uploads/2020/09/09/sample_22_1957.png] 
 
```
Input:
 logs = ["d1/","d2/","./","d3/","../","d31/"]

Output:
 3
```

 Example 3: 
 
```
Input:
 logs = ["d1/","../","../","../"]

Output:
 0
```

 Constraints: 

 1 <= logs.length <= 10 3 
 
 2 <= logs[i].length <= 10 
 
 logs[i] contains lowercase English letters, digits, '.' , and '/' . 
 
 logs[i] follows the format described in the statement. 
 
 Folder names consist of lowercase English letters and digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int minOperations(vector<string>& logs) {
        int depth = 0;
        for (const string& log : logs) {
            if (log == "./") continue;
            else if (log == "../") depth = max(0, depth - 1);
            else depth++;
        }
        return depth;
    }
};
```


## 1614. Maximum Nesting Depth of the Parentheses

**Problem:** https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Stack, Bracket Sequences

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One scan increments/decrements nesting depth and tracks the maximum.

### Problem description

Given a valid parentheses string s , return the nesting depth of s . The nesting depth is the maximum number of nested parentheses. 

 Example 1: 

 Input: s = "(1+(2*3)+((8)/4))+1" 
 
 Output: 3 
 
 Explanation: 
 
 Digit 8 is inside of 3 nested parentheses in the string. 

 Example 2: 

 Input: s = "(1)+((2))+(((3)))" 
 
 Output: 3 
 
 Explanation: 
 
 Digit 3 is inside of 3 nested parentheses in the string. 

 Example 3: 

 Input: s = "()(())((()()))" 
 
 Output: 3 

 Constraints: 

 1 <= s.length <= 100 
 
 s consists of digits 0-9 and characters '+' , '-' , '*' , '/' , '(' , and ')' . 
 
 It is guaranteed that parentheses expression s is a VPS.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    int maxDepth(string s) {
        int depth = 0, maxDepth = 0;
        for (char c : s) {
            if (c == '(') maxDepth = max(maxDepth, ++depth);
            else if (c == ')') depth--;
        }
        return maxDepth;
    }
};
```


## 1629. Slowest Key

**Problem:** https://leetcode.com/problems/slowest-key/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Computes each adjacent release-time difference once and keeps the best duration and key.

### Problem description

A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time. 
 
 You are given a string keysPressed of length n , where keysPressed[i] was the i th key pressed in the testing sequence, and a sorted list releaseTimes , where releaseTimes[i] was the time the i th key was released. Both arrays are 0-indexed . The 0 th key was pressed at the time 0 , and every subsequent key was pressed at the exact time the previous key was released. 
 
 The tester wants to know the key of the keypress that had the longest duration . The i th keypress had a duration of releaseTimes[i] - releaseTimes[i - 1] , and the 0 th keypress had a duration of releaseTimes[0] . 
 
 Note that the same key could have been pressed multiple times during the test, and these multiple presses of the same key may not have had the same duration . 
 
 Return the key of the keypress that had the longest duration . If there are multiple such keypresses, return the lexicographically largest key of the keypresses. 

 Example 1: 
 
```
Input:
 releaseTimes = [9,29,49,50], keysPressed = "cbcd"

Output:
 "c"

Explanation:
 The keypresses were as follows:
Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
Keypress for 'b' had a duration of 29 - 9 = 20 (pressed at time 9 right after the release of the previous character and released at time 29).
Keypress for 'c' had a duration of 49 - 29 = 20 (pressed at time 29 right after the release of the previous character and released at time 49).
Keypress for 'd' had a duration of 50 - 49 = 1 (pressed at time 49 right after the release of the previous character and released at time 50).
The longest of these was the keypress for 'b' and the second keypress for 'c', both with duration 20.
'c' is lexicographically larger than 'b', so the answer is 'c'.
```

 Example 2: 
 
```
Input:
 releaseTimes = [12,23,36,46,62], keysPressed = "spuda"

Output:
 "a"

Explanation:
 The keypresses were as follows:
Keypress for 's' had a duration of 12.
Keypress for 'p' had a duration of 23 - 12 = 11.
Keypress for 'u' had a duration of 36 - 23 = 13.
Keypress for 'd' had a duration of 46 - 36 = 10.
Keypress for 'a' had a duration of 62 - 46 = 16.
The longest of these was the keypress for 'a' with duration 16.
```

 Constraints: 

 releaseTimes.length == n 
 
 keysPressed.length == n 
 
 2 <= n <= 1000 
 
 1 <= releaseTimes[i] <= 10 9 
 
 releaseTimes[i] < releaseTimes[i+1] 
 
 keysPressed contains only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        int maxDur = releaseTimes[0];
        char res = keysPressed[0];
        for (int i = 1; i < releaseTimes.size(); ++i) {
            int dur = releaseTimes[i] - releaseTimes[i - 1];
            if (dur > maxDur || (dur == maxDur && keysPressed[i] > res)) {
                maxDur = dur;
                res = keysPressed[i];
            }
        }
        return res;
    }
};
```


## 1662. Check If Two String Arrays are Equivalent

**Problem:** https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(L₁ + L₂)

**Space complexity:** O(L₁ + L₂)

**Complexity reasoning:** Concatenates both arrays into two strings and compares them; the concatenated strings occupy the total input-character length.

### Problem description

Given two string arrays word1 and word2 , return true if the two arrays represent the same string, and false otherwise. 
 
 A string is represented by an array if the array elements concatenated in order forms the string. 

 Example 1: 
 
```
Input:
 word1 = ["ab", "c"], word2 = ["a", "bc"]

Output:
 true

Explanation:

word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
```

 Example 2: 
 
```
Input:
 word1 = ["a", "cb"], word2 = ["ab", "c"]

Output:
 false
```

 Example 3: 
 
```
Input:
 word1 = ["abc", "d", "defg"], word2 = ["abcddefg"]

Output:
 true
```

 Constraints: 

 1 <= word1.length, word2.length <= 10 3 
 
 1 <= word1[i].length, word2[i].length <= 10 3 
 
 1 <= sum(word1[i].length), sum(word2[i].length) <= 10 3 
 
 word1[i] and word2[i] consist of lowercase letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string s1, s2;
        for (auto& w : word1) s1 += w;
        for (auto& w : word2) s2 += w;
        return s1 == s2;
    }
};
```


## 1678. Goal Parser Interpretation

**Problem:** https://leetcode.com/problems/goal-parser-interpretation/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Advances through each encoded token once, appending one or two decoded characters to the result.

### Problem description

You own a Goal Parser that can interpret a string command . The command consists of an alphabet of "G" , "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G" , "()" as the string "o" , and "(al)" as the string "al" . The interpreted strings are then concatenated in the original order. 
 
 Given the string command , return the Goal Parser 's interpretation of command . 

 Example 1: 
 
```
Input:
 command = "G()(al)"

Output:
 "Goal"

Explanation:
 The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
```

 Example 2: 
 
```
Input:
 command = "G()()()()(al)"

Output:
 "Gooooal"
```

 Example 3: 
 
```
Input:
 command = "(al)G(al)()()G"

Output:
 "alGalooG"
```

 Constraints: 

 1 <= command.length <= 100 
 
 command consists of "G" , "()" , and/or "(al)" in some order.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    string interpret(string command) {
        string res;
        for (int i = 0; i < command.size(); ++i) {
            if (command[i] == 'G') res += 'G';
            else if (command[i] == '(' && command[i + 1] == ')') {
                res += 'o';
                ++i;
            } else {
                res += "al";
                i += 3;
            }
        }
        return res;
    }
};
```


## 1694. Reformat Phone Number

**Problem:** https://leetcode.com/problems/reformat-phone-number/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Filters digits in one pass and builds the formatted number using constant-size substrings per group.

### Problem description

You are given a phone number as a string number . number consists of digits, spaces ' ' , and/or dashes '-' . 
 
 You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows: 

 2 digits: A single block of length 2. 
 
 3 digits: A single block of length 3. 
 
 4 digits: Two blocks of length 2 each. 

 The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2. 
 
 Return the phone number after formatting. 

 Example 1: 
 
```
Input:
 number = "1-23-45 6"

Output:
 "123-456"

Explanation:
 The digits are "123456".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block is "456".
Joining the blocks gives "123-456".
```

 Example 2: 
 
```
Input:
 number = "123 4-567"

Output:
 "123-45-67"

Explanation: 
The digits are "1234567".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks are "45" and "67".
Joining the blocks gives "123-45-67".
```

 Example 3: 
 
```
Input:
 number = "123 4-5678"

Output:
 "123-456-78"

Explanation:
 The digits are "12345678".
Step 1: The 1st block is "123".
Step 2: The 2nd block is "456".
Step 3: There are 2 digits left, so put them in a single block of length 2. The 3rd block is "78".
Joining the blocks gives "123-456-78".
```

 Constraints: 

 2 <= number.length <= 100 
 
 number consists of digits and the characters '-' and ' ' . 
 
 There are at least two digits in number .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
using namespace std;

class Solution {
public:
    string reformatNumber(string number) {
        string digits;
        for (char c : number)
            if (isdigit(c)) digits += c;

        string res;
        int i = 0, n = digits.size();
        while (n - i > 4) {
            res += digits.substr(i, 3) + "-";
            i += 3;
        }
        if (n - i == 4)
            res += digits.substr(i, 2) + "-" + digits.substr(i + 2);
        else
            res += digits.substr(i);
        return res;
    }
};
```


## 1758. Minimum Changes To Make Alternating Binary String

**Problem:** https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Compares each bit against one alternating pattern and derives the mismatch count for the opposite pattern.

### Problem description

You are given a string s consisting only of the characters '0' and '1' . In one operation, you can change any '0' to '1' or vice versa. 
 
 The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not. 
 
 Return the minimum number of operations needed to make s alternating . 

 Example 1: 
 
```
Input:
 s = "0100"

Output:
 1

Explanation:
 If you change the last character to '1', s will be "0101", which is alternating.
```

 Example 2: 
 
```
Input:
 s = "10"

Output:
 0

Explanation:
 s is already alternating.
```

 Example 3: 
 
```
Input:
 s = "1111"

Output:
 2

Explanation:
 You need two operations to reach "0101" or "1010".
```

 Constraints: 

 1 <= s.length <= 10 4 
 
 s[i] is either '0' or '1' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 int minOperations(string s){
  int a=0;for(int i=0;i<(int)s.size();++i)if(s[i]!=(char)('0'+i%2))++a;
  return min(a,(int)s.size()-a);
 }
};
```


## 1759. Count Number of Homogenous Substrings

**Problem:** https://leetcode.com/problems/count-number-of-homogenous-substrings/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Updates the current equal-character run and cumulative substring count once per character.

### Problem description

Given a string s , return the number of homogenous substrings of s . Since the answer may be too large, return it modulo 10 9 + 7 . 
 
 A string is homogenous if all the characters of the string are the same. 
 
 A substring is a contiguous sequence of characters within a string. 

 Example 1: 
 
```
Input:
 s = "abbcccaa"

Output:
 13

Explanation:
 The homogenous substrings are listed as below:
"a" appears 3 times.
"aa" appears 1 time.
"b" appears 2 times.
"bb" appears 1 time.
"c" appears 3 times.
"cc" appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
```

 Example 2: 
 
```
Input:
 s = "xy"

Output:
 2

Explanation:
 The homogenous substrings are "x" and "y".
```

 Example 3: 
 
```
Input:
 s = "zzzzz"

Output:
 15
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists of lowercase letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 int countHomogenous(string s){
  const int MOD=1000000007;long long ans=0,len=0;
  for(int i=0;i<(int)s.size();++i){len=(i>0 && s[i]==s[i-1])?len+1:1;ans=(ans+len)%MOD;}
  return ans;
 }
};
```


## 1773. Count Items Matching a Rule

**Problem:** https://leetcode.com/problems/count-items-matching-a-rule/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(m)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Selects one fixed field and compares it against the rule value for each of m items; field-string comparisons are bounded by their lengths.

### Problem description

You are given an array items , where each items[i] = [type i , color i , name i ] describes the type, color, and name of the i th item. You are also given a rule represented by two strings, ruleKey and ruleValue . 
 
 The i th item is said to match the rule if one of the following is true: 

 ruleKey == "type" and ruleValue == type i . 
 
 ruleKey == "color" and ruleValue == color i . 
 
 ruleKey == "name" and ruleValue == name i . 

 Return the number of items that match the given rule . 

 Example 1: 
 
```
Input:
 items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"

Output:
 1

Explanation:
 There is only one item matching the given rule, which is ["computer","silver","lenovo"].
```

 Example 2: 
 
```
Input:
 items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"

Output:
 2

Explanation:
 There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
```

 Constraints: 

 1 <= items.length <= 10 4 
 
 1 <= type i .length, color i .length, name i .length, ruleValue.length <= 10 
 
 ruleKey is equal to either "type" , "color" , or "name" . 
 
 All strings consist only of lowercase letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int idx = ruleKey == "type" ? 0 : ruleKey == "color" ? 1 : 2;
        int res = 0;
        for (auto& item : items)
            if (item[idx] == ruleValue) ++res;
        return res;
    }
};
```


## 1784. Check if Binary String Has at Most One Segment of Ones

**Problem:** https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** The standard string find searches for the fixed two-character pattern "01" in a single linear scan.

### Problem description

Given a binary string s ​​​​​without leading zeros , return true ​​​ if s contains at most one contiguous segment of ones . Otherwise, return false . 

 Example 1: 
 
```
Input:
 s = "1001"

Output:
 false

Explanation: 
The string has two segments of size 1.
```

 Example 2: 
 
```
Input:
 s = "110"

Output:
 true
```

 Constraints: 

 1 <= s.length <= 100 
 
 s[i] ​​​​ is either '0' or '1' . 
 
 s[0] is  '1' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 bool checkOnesSegment(string s){return s.find("01")==string::npos;}
};
```


## 1812. Determine Color of a Chessboard Square

**Problem:** https://leetcode.com/problems/determine-color-of-a-chessboard-square/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Uses two fixed-position characters and a parity calculation.

### Problem description

You are given coordinates , a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference. 
 
 [Figure: https://assets.leetcode.com/uploads/2021/02/19/screenshot-2021-02-20-at-22159-pm.png] 
 
 Return true if the square is white, and false if the square is black . 
 
 The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second. 

 Example 1: 
 
```
Input:
 coordinates = "a1"

Output:
 false

Explanation:
 From the chessboard above, the square with coordinates "a1" is black, so return false.
```

 Example 2: 
 
```
Input:
 coordinates = "h3"

Output:
 true

Explanation:
 From the chessboard above, the square with coordinates "h3" is white, so return true.
```

 Example 3: 
 
```
Input:
 coordinates = "c7"

Output:
 false
```

 Constraints: 

 coordinates.length == 2 
 
 'a' <= coordinates[0] <= 'h' 
 
 '1' <= coordinates[1] <= '8'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 bool squareIsWhite(string coordinates){
  return ((coordinates[0]-'a')+(coordinates[1]-'1'))%2==1;
 }
};
```


## 1816. Truncate Sentence

**Problem:** https://leetcode.com/problems/truncate-sentence/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Constructs a stringstream from the n-character input, extracts at most k words, and builds the truncated output.

### Problem description

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation). 

 For example, "Hello World" , "HELLO" , and "hello world hello world" are all sentences. 

 You are given a sentence s ​​​​​​ and an integer k ​​​​​​. You want to truncate s ​​​​​​ such that it contains only the first k ​​​​​​ words. Return s ​​​​ ​​ after truncating it. 

 Example 1: 
 
```
Input:
 s = "Hello how are you Contestant", k = 4

Output:
 "Hello how are you"

Explanation:

The words in s are ["Hello", "how", "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".
```

 Example 2: 
 
```
Input:
 s = "What is the solution to this problem", k = 4

Output:
 "What is the solution"

Explanation:

The words in s are ["What", "is", "the", "solution", "to", "this", "problem"].
The first 4 words are ["What", "is", "the", "solution"].
Hence, you should return "What is the solution".
```

 Example 3: 
 
```
Input:
 s = "chopper is not a tanuki", k = 5

Output:
 "chopper is not a tanuki"
```

 Constraints: 

 1 <= s.length <= 500 
 
 k is in the range [1, the number of words in s] . 
 
 s consist of only lowercase and uppercase English letters and spaces. 
 
 The words in s are separated by a single space. 
 
 There are no leading or trailing spaces.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    string truncateSentence(string s, int k) {
        stringstream ss(s);
        string word, res;
        while (k-- && ss >> word) {
            if (!res.empty()) res += " ";
            res += word;
        }
        return res;
    }
};
```


## 1844. Replace All Digits with Characters

**Problem:** https://leetcode.com/problems/replace-all-digits-with-characters/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Updates every second character in the by-value string with constant-time arithmetic.

### Problem description

You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices. 
 
 You must perform an operation shift(c, x) , where c is a character and x is a digit, that returns the x th character after c . 

 For example, shift('a', 5) = 'f' and shift('x', 0) = 'x' . 

 For every odd index i , you want to replace the digit s[i] with the result of the shift(s[i-1], s[i]) operation. 
 
 Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z' . 
 
 Note that shift(c, x) is not a preloaded function, but an operation to be implemented as part of the solution. 

 Example 1: 
 
```
Input:
 s = "a1c1e1"

Output:
 "abcdef"

Explanation: 
The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
```

 Example 2: 
 
```
Input:
 s = "a1b2c3d4e"

Output:
 "abbdcfdhe"

Explanation: 
The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'
```

 Constraints: 

 1 <= s.length <= 100 
 
 s consists only of lowercase English letters and digits. 
 
 shift(s[i-1], s[i]) <= 'z' for all odd indices i .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string replaceDigits(string s){for(int i=1;i<(int)s.size();i+=2)s[i]=char(s[i-1]+s[i]-'0');return s;}};
```


## 1859. Sorting the Sentence

**Problem:** https://leetcode.com/problems/sorting-the-sentence/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Sorting, Bubble Sort

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Sorting / Divide and Conquer

**Data structures (inferred):** Sorted array, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Tokenizes the input, places words into a fixed ten-slot vector, and concatenates them in sentence order.

### Problem description

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters. 
 
 A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence. 

 For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3" . 

 Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence . 

 Example 1: 
 
```
Input:
 s = "is2 sentence4 This1 a3"

Output:
 "This is a sentence"

Explanation:
 Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
```

 Example 2: 
 
```
Input:
 s = "Myself2 Me1 I4 and3"

Output:
 "Me Myself and I"

Explanation:
 Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
```

 Constraints: 

 2 <= s.length <= 200 
 
 s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9 . 
 
 The number of words in s is between 1 and 9 . 
 
 The words in s are separated by a single space. 
 
 s contains no leading or trailing spaces.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string sortSentence(string s) {
        stringstream ss(s);
        string word;
        vector<string> words(10);
        while (ss >> word) {
            int pos = word.back() - '0';
            word.pop_back();
            words[pos - 1] = word;
        }

        string res;
        for (const string& w : words) {
            if (w.empty()) break;
            if (!res.empty()) res += " ";
            res += w;
        }
        return res;
    }
};
```


## 1869. Longer Contiguous Segments of Ones than Zeros

**Problem:** https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Tracks the current run and longest zero/one runs during a single traversal.

### Problem description

Given a binary string s , return true if the longest contiguous segment of 1 ' s is strictly longer than the longest contiguous segment of 0 ' s in s , or return false otherwise . 

 For example, in s = " 11 01 000 10" the longest continuous segment of 1 s has length 2 , and the longest continuous segment of 0 s has length 3 . 

 Note that if there are no 0 's, then the longest continuous segment of 0 's is considered to have a length 0 . The same applies if there is no 1 's. 

 Example 1: 
 
```
Input:
 s = "1101"

Output:
 true

Explanation:

The longest contiguous segment of 1s has length 2: "
11
01"
The longest contiguous segment of 0s has length 1: "11
0
1"
The segment of 1s is longer, so return true.
```

 Example 2: 
 
```
Input:
 s = "111000"

Output:
 false

Explanation:

The longest contiguous segment of 1s has length 3: "
111
000"
The longest contiguous segment of 0s has length 3: "111
000
"
The segment of 1s is not longer, so return false.
```

 Example 3: 
 
```
Input:
 s = "110100010"

Output:
 false

Explanation:

The longest contiguous segment of 1s has length 2: "
11
0100010"
The longest contiguous segment of 0s has length 3: "1101
000
10"
The segment of 1s is not longer, so return false.
```

 Constraints: 

 1 <= s.length <= 100 
 
 s[i] is either '0' or '1' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
using namespace std;

class Solution {
public:
    bool checkZeroOnes(string s) {
        int max1 = 0, max0 = 0, cur = 1;
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] == s[i-1]) cur++;
            else cur = 1;
            if (s[i] == '1') max1 = max(max1, cur);
            else max0 = max(max0, cur);
        }
        if (s[0] == '1') max1 = max(max1, 1);
        else max0 = max(max0, 1);
        return max1 > max0;
    }
};
```


## 1880. Check if Word Equals Summation of Two Words

**Problem:** https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(a+b+c)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Converts each of the three words to a number with one pass over its characters; only integer accumulators are used.

### Problem description

The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0 , 'b' -> 1 , 'c' -> 2 , etc.). 
 
 The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s , which is then converted into an integer. 

 For example, if s = "acb" , we concatenate each letter's letter value, resulting in "021" . After converting it, we get 21 . 

 You are given three strings firstWord , secondWord , and targetWord , each consisting of lowercase English letters 'a' through 'j' inclusive . 
 
 Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord , or false otherwise. 

 Example 1: 
 
```
Input:
 firstWord = "acb", secondWord = "cba", targetWord = "cdb"

Output:
 true

Explanation:

The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.
```

 Example 2: 
 
```
Input:
 firstWord = "aaa", secondWord = "a", targetWord = "aab"

Output:
 false

Explanation:
 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.
```

 Example 3: 
 
```
Input:
 firstWord = "aaa", secondWord = "a", targetWord = "aaaa"

Output:
 true

Explanation:
 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.
```

 Constraints: 

 1 <= firstWord.length, secondWord.length, targetWord.length <= 8 
 
 firstWord , secondWord , and targetWord consist of lowercase English letters from 'a' to 'j' inclusive .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    bool isSumEqual(string firstWord, string secondWord, string targetWord) {
        return toInt(firstWord) + toInt(secondWord) == toInt(targetWord);
    }

    int toInt(string word) {
        int res = 0;
        for (char c : word) res = res * 10 + (c - 'a');
        return res;
    }
};
```


## 1904. The Number of Full Rounds You Have Played

**Problem:** https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Parses fixed-width HH:MM strings and performs constant-time rounding and arithmetic.

### Problem description

You are participating in an online chess tournament. There is a chess round that starts every 15 minutes. The first round of the day starts at 00:00 , and after every 15 minutes, a new round starts. 

 For example, the second round starts at 00:15 , the fourth round starts at 00:45 , and the seventh round starts at 01:30 . 

 You are given two strings loginTime and logoutTime where: 

 loginTime is the time you will login to the game, and 
 
 logoutTime is the time you will logout from the game. 

 If logoutTime is earlier than loginTime , this means you have played from loginTime to midnight and from midnight to logoutTime . 
 
 Return the number of full chess rounds you have played in the tournament . 
 
 Note:  All the given times follow the 24-hour clock. That means the first round of the day starts at 00:00 and the last round of the day starts at 23:45 . 

 Example 1: 
 
```
Input:
 loginTime = "09:31", logoutTime = "10:14"

Output:
 1

Explanation:
 You played one full round from 09:45 to 10:00.
You did not play the full round from 09:30 to 09:45 because you logged in at 09:31 after it began.
You did not play the full round from 10:00 to 10:15 because you logged out at 10:14 before it ended.
```

 Example 2: 
 
```
Input:
 loginTime = "21:30", logoutTime = "03:00"

Output:
 22

Explanation:
 You played 10 full rounds from 21:30 to 00:00 and 12 full rounds from 00:00 to 03:00.
10 + 12 = 22.
```

 Constraints: 

 loginTime and logoutTime are in the format hh:mm . 
 
 00 <= hh <= 23 
 
 00 <= mm <= 59 
 
 loginTime and logoutTime are not equal.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {int minutes(string s){return stoi(s.substr(0,2))*60+stoi(s.substr(3,2));}public:int numberOfRounds(string loginTime,string logoutTime){int a=minutes(loginTime),b=minutes(logoutTime);if(b<a)b+=1440;return max(0,b/15-(a+14)/15);}};
```


## 1910. Remove All Occurrences of a Substring

**Problem:** https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(n) auxiliary

**Complexity reasoning:** Repeated find scans the remaining string and erase shifts its suffix; up to O(n) removals can each cost O(n). The by-value mutable string holds O(n) characters.

### Problem description

Given two strings s and part , perform the following operation on s until all occurrences of the substring part are removed: 

 Find the leftmost occurrence of the substring part and remove it from s . 

 Return s after removing all occurrences of part . 
 
 A substring is a contiguous sequence of characters in a string. 

 Example 1: 
 
```
Input:
 s = "daabcbaabcbc", part = "abc"

Output:
 "dab"

Explanation
: The following operations are done:
- s = "da
abc
baabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "daba
abc
bc", remove "abc" starting at index 4, so s = "dababc".
- s = "dab
abc
", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
```

 Example 2: 
 
```
Input:
 s = "axxxxyyyyb", part = "xy"

Output:
 "ab"

Explanation
: The following operations are done:
- s = "axxx
xy
yyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axx
xy
yyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "ax
xy
yb", remove "xy" starting at index 2 so s = "axyb".
- s = "a
xy
b", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".
```

 Constraints: 

 1 <= s.length <= 1000 
 
 1 <= part.length <= 1000 
 
 s ​​​​​​ and part consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>

using namespace std;

class Solution {
public:
    string removeOccurrences(string s, string part) {
        size_t pos;
        while ((pos = s.find(part)) != string::npos)
            s.erase(pos, part.size());
        return s;
    }
};
```


## 1933. Check if String Is Decomposable Into Value-Equal Substrings

**Problem:** https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Visits each maximal run of equal digits once, checking its length modulo three and counting runs with remainder two.

### Problem description

A value-equal string is a string where all characters are the same. 

 For example, "1111" and "33" are value-equal strings. 
 
 In contrast, "123" is not a value-equal string. 

 Given a digit string s , decompose the string into some number of consecutive value-equal substrings where exactly one substring has a length of 2 and the remaining substrings have a length of 3 . 
 
 Return true if you can decompose s according to the above rules. Otherwise, return false . 
 
 A substring is a contiguous sequence of characters in a string. 

 Example 1: 
 
```
Input:
 s = "000111000"

Output:
 false

Explanation: 
s cannot be decomposed according to the rules because ["000", "111", "000"] does not have a substring of length 2.
```

 Example 2: 
 
```
Input:
 s = "00011111222"

Output:
 true

Explanation: 
s can be decomposed into ["000", "111", "11", "222"].
```

 Example 3: 
 
```
Input:
 s = "011100022233"

Output:
 false

Explanation: 
s cannot be decomposed according to the rules because of the first '0'.
```

 Constraints: 

 1 <= s.length <= 1000 
 
 s consists of only digits '0' through '9' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool isDecomposable(string s) {
        int twos = 0;
        for (int i = 0; i < (int)s.size();) {
            int j = i;
            while (j < (int)s.size() && s[j] == s[i]) {
                ++j;
            }
            int rem = (j - i) % 3;
            if (rem == 1) {
                return false;
            }
            if (rem == 2) {
                ++twos;
            }
            i = j;
        }
        return twos == 1;
    }
};
```


## 1945. Sum of Digits of String After Convert

**Problem:** https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + k log n)

**Space complexity:** O(n)

**Complexity reasoning:** Initial character-to-number conversion scans n letters; each of k digit-sum passes processes a number with at most O(log n) digits after the first. The intermediate numeric string can hold O(n) characters.

### Problem description

You are given a string s consisting of lowercase English letters, and an integer k . Your task is to convert the string into an integer by a special process, and then transform it by summing its digits repeatedly k times. More specifically, perform the following steps: 

 Convert s into an integer by replacing each letter with its position in the alphabet (i.e. replace 'a' with 1 , 'b' with 2 , ..., 'z' with 26 ). 
 
 T ransform the integer by replacing it with the sum of its digits . 
 
 Repeat the transform operation (step 2) k times in total. 

 For example, if s = "zbax" and k = 2 , then the resulting integer would be 8 by the following operations: 

 Convert : "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124 
 
 Transform #1 : 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17 
 
 Transform #2 : 17 ➝ 1 + 7 ➝ 8 

 Return the resulting integer after performing the operations described above. 

 Example 1: 

 Input: s = "iiii", k = 1 
 
 Output: 36 
 
 Explanation: 
 
 The operations are as follows: 
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999 
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36 
Thus the resulting integer is 36. 

 Example 2: 

 Input: s = "leetcode", k = 2 
 
 Output: 6 
 
 Explanation: 
 
 The operations are as follows: 
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545 
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33 
- Transform #2: 33 ➝ 3 + 3 ➝ 6 
Thus the resulting integer is 6. 

 Example 3: 

 Input: s = "zbax", k = 2 
 
 Output: 8 

 Constraints: 

 1 <= s.length <= 100 
 
 1 <= k <= 10 
 
 s consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
using namespace std;

class Solution {
public:
    int getLucky(string s, int k) {
        string num;
        for (char c : s) num += to_string(c - 'a' + 1);
        while (k--) {
            int sum = 0;
            for (char d : num) sum += d - '0';
            num = to_string(sum);
        }
        return stoi(num);
    }
};
```


## 1957. Delete Characters to Make Fancy String

**Problem:** https://leetcode.com/problems/delete-characters-to-make-fancy-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each character is inspected once and appended at most once to the output string.

### Problem description

A fancy string is a string where no three consecutive characters are equal. 
 
 Given a string s , delete the minimum possible number of characters from s to make it fancy . 
 
 Return the final string after the deletion . It can be shown that the answer will always be unique . 

 Example 1: 
 
```
Input:
 s = "le
e
etcode"

Output:
 "leetcode"

Explanation:

Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
```

 Example 2: 
 
```
Input:
 s = "
a
aab
aa
aa"

Output:
 "aabaa"

Explanation:

Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
```

 Example 3: 
 
```
Input:
 s = "aab"

Output:
 "aab"

Explanation:
 No three consecutive characters are equal, so return "aab".
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string makeFancyString(string s){string out;for(char c:s){int n=out.size();if(n>=2&&out[n-1]==c&&out[n-2]==c)continue;out+=c;}return out;}};
```


## 1967. Number of Strings That Appear as Substrings in Word

**Problem:** https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(P · W · L) worst case

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** For P patterns, std::string::find may examine O(W) starting positions and compare up to L characters per position; no extra container is built.

### Problem description

Given an array of strings patterns and a string word , return the number of strings in patterns that exist as a substring in word . 
 
 A substring is a contiguous sequence of characters within a string. 

 Example 1: 
 
```
Input:
 patterns = ["a","abc","bc","d"], word = "abc"

Output:
 3

Explanation:

- "a" appears as a substring in "
a
bc".
- "abc" appears as a substring in "
abc
".
- "bc" appears as a substring in "a
bc
".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.
```

 Example 2: 
 
```
Input:
 patterns = ["a","b","c"], word = "aaaaabbbbb"

Output:
 2

Explanation:

- "a" appears as a substring in "a
a
aaabbbbb".
- "b" appears as a substring in "aaaaabbbb
b
".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.
```

 Example 3: 
 
```
Input:
 patterns = ["a","a","a"], word = "ab"

Output:
 3

Explanation:
 Each of the patterns appears as a substring in word "
a
b".
```

 Constraints: 

 1 <= patterns.length <= 100 
 
 1 <= patterns[i].length <= 100 
 
 1 <= word.length <= 100 
 
 patterns[i] and word consist of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int count = 0;
        for (auto& p : patterns)
            if (word.find(p) != string::npos) count++;
        return count;
    }
};
```


## 2011. Final Value of Variable After Performing Operations

**Problem:** https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Each operation is checked once at its middle character.

### Problem description

There is a programming language with only four operations and one variable X : 

 ++X and X++ increments the value of the variable X by 1 . 
 
 --X and X-- decrements the value of the variable X by 1 . 

 Initially, the value of X is 0 . 
 
 Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations . 

 Example 1: 
 
```
Input:
 operations = ["--X","X++","X++"]

Output:
 1

Explanation:
 The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X = 0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
```

 Example 2: 
 
```
Input:
 operations = ["++X","++X","X++"]

Output:
 3

Explanation: 
The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.
```

 Example 3: 
 
```
Input:
 operations = ["X++","++X","--X","X--"]

Output:
 0

Explanation:
 The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.
```

 Constraints: 

 1 <= operations.length <= 100 
 
 operations[i] will be either "++X" , "X++" , "--X" , or "X--" .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        for (string& op : operations) {
            if (op[1] == '+') ++x;
            else --x;
        }
        return x;
    }
};
```


## 2042. Check if Numbers Are Ascending in a Sentence

**Problem:** https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** A single index walks over the sentence, consuming each digit or non-digit once.

### Problem description

A sentence is a list of tokens separated by a single space with no leading or trailing spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters. 

 For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other tokens such as "puppy" are words. 

 Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s ). 
 
 Return true if so, or false otherwise . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/09/30/example1.png] 
 
```
Input:
 s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"

Output:
 true

Explanation:
 The numbers in s are: 1, 3, 4, 6, 12.
They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.
```

 Example 2: 
 
```
Input:
 s = "hello world 5 x 5"

Output:
 false

Explanation:
 The numbers in s are: 
5
, 
5
. They are not strictly increasing.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/09/30/example3.png] 
 
```
Input:
 s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"

Output:
 false

Explanation:
 The numbers in s are: 7, 
51
, 
50
, 60. They are not strictly increasing.
```

 Constraints: 

 3 <= s.length <= 200 
 
 s consists of lowercase English letters, spaces, and digits from 0 to 9 , inclusive. 
 
 The number of tokens in s is between 2 and 100 , inclusive. 
 
 The tokens in s are separated by a single space. 
 
 There are at least two numbers in s . 
 
 Each number in s is a positive number less than 100 , with no leading zeros. 
 
 s contains no leading or trailing spaces.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool areNumbersAscending(string s){int prev=0;
        for(int i=0;i<(int)s.size();){
            if(!isdigit(s[i])){++i;continue;}
            int x=0;while(i<(int)s.size()&&isdigit(s[i]))x=x*10+s[i++]-'0';
            if(x<=prev)return false;prev=x;
        }
        return true;
    }
};
```


## 2047. Number of Valid Words in a Sentence

**Problem:** https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The string stream tokenizes the sentence and each word is validated character by character; token storage and stream buffering can use O(n) space.

### Problem description

A sentence consists of lowercase letters ( 'a' to 'z' ), digits ( '0' to '9' ), hyphens ( '-' ), punctuation marks ( '!' , '.' , and ',' ), and spaces ( ' ' ) only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' ' . 
 
 A token is a valid word if all three of the following are true: 

 It only contains lowercase letters, hyphens, and/or punctuation ( no digits). 
 
 There is at most one hyphen '-' . If present, it must be surrounded by lowercase characters ( "a-b" is valid, but "-ab" and "ab-" are not valid). 
 
 There is at most one punctuation mark. If present, it must be at the end of the token ( "ab," , "cd!" , and "." are valid, but "a!b" and "c.," are not valid). 

 Examples of valid words include "a-b." , "afad" , "ba-c" , "a!" , and "!" . 
 
 Given a string sentence , return the number of valid words in sentence . 

 Example 1: 
 
```
Input:
 sentence = "
cat
 
and
 
dog
"

Output:
 3

Explanation:
 The valid words in the sentence are "cat", "and", and "dog".
```

 Example 2: 
 
```
Input:
 sentence = "!this 1-s b8d!"

Output:
 0

Explanation:
 There are no valid words in the sentence.
"!this" is invalid because it starts with a punctuation mark.
"1-s" and "b8d" are invalid because they contain digits.
```

 Example 3: 
 
```
Input:
 sentence = "
alice
 
and
 
bob
 
are
 
playing
 stone-game10"

Output:
 5

Explanation:
 The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
"stone-game10" is invalid because it contains digits.
```

 Constraints: 

 1 <= sentence.length <= 1000 
 
 sentence only contains lowercase English letters, digits, ' ' , '-' , '!' , '.' , and ',' . 
 
 There will be at least  1 token.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int countValidWords(string sentence){istringstream in(sentence);string w;int ans=0;
        while(in>>w){bool ok=true;int hy=0,punct=0;
            for(int i=0;i<(int)w.size();++i){char c=w[i];
                if(isdigit(c)){ok=false;break;}
                if(c=='-'){
                    if(++hy>1||i==0||i+1==(int)w.size()||
                       !islower(w[i-1])||!islower(w[i+1]))ok=false;
                }else if(c=='!'||c=='.'||c==','){
                    if(++punct>1||i+1!=(int)w.size())ok=false;
                }else if(!islower(c))ok=false;
            }
            if(ok)++ans;
        }
        return ans;
    }
};
```


## 2075. Decode the Slanted Ciphertext

**Problem:** https://leetcode.com/problems/decode-the-slanted-ciphertext/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** The nested diagonal traversal visits at most rows × cols = n encoded positions; output stores up to n characters.

### Problem description

A string originalText is encoded using a slanted transposition cipher to a string encodedText with the help of a matrix having a fixed number of rows rows . 
 
 originalText is placed first in a top-left to bottom-right manner. 
 [Figure: https://assets.leetcode.com/uploads/2021/11/07/exa11.png] 
 
 The blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the end of originalText . The arrow indicates the order in which the cells are filled. All empty cells are filled with ' ' . The number of columns is chosen such that the rightmost column will not be empty after filling in originalText . 
 
 encodedText is then formed by appending all characters of the matrix in a row-wise fashion. 
 [Figure: https://assets.leetcode.com/uploads/2021/11/07/exa12.png] 
 
 The characters in the blue cells are appended first to encodedText , then the red cells, and so on, and finally the yellow cells. The arrow indicates the order in which the cells are accessed. 
 
 For example, if originalText = "cipher" and rows = 3 , then we encode it in the following manner: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/25/desc2.png] 
 
 The blue arrows depict how originalText is placed in the matrix, and the red arrows denote the order in which encodedText is formed. In the above example, encodedText = "ch ie pr" . 
 
 Given the encoded string encodedText and number of rows rows , return the original string originalText . 
 
 Note: originalText does not have any trailing spaces ' ' . The test cases are generated such that there is only one possible originalText . 

 Example 1: 
 
```
Input:
 encodedText = "ch ie pr", rows = 3

Output:
 "cipher"

Explanation:
 This is the same example described in the problem description.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/26/exam1.png] 
 
```
Input:
 encodedText = "iveo eed l te olc", rows = 4

Output:
 "i love leetcode"

Explanation:
 The figure above denotes the matrix that was used to encode originalText. 
The blue arrows show how we can find originalText from encodedText.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/10/26/eg2.png] 
 
```
Input:
 encodedText = "coding", rows = 1

Output:
 "coding"

Explanation:
 Since there is only 1 row, both originalText and encodedText are the same.
```

 Constraints: 

 0 <= encodedText.length <= 10 6 
 
 encodedText consists of lowercase English letters and ' ' only. 
 
 encodedText is a valid encoding of some originalText that does not have trailing spaces. 
 
 1 <= rows <= 1000 
 
 The testcases are generated such that there is only one possible originalText .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 string decodeCiphertext(string encodedText,int rows){
  if(rows==0) return ""; int cols=encodedText.size()/rows; string out;
  for(int c=0;c<cols;++c) for(int r=0,j=c;r<rows && j<cols;++r,++j)
   out+=encodedText[r*cols+j];
  while(!out.empty() && out.back()==' ') out.pop_back(); return out;
 }
};
```


## 2114. Maximum Number of Words Found in Sentences

**Problem:** https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(C)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** All characters in the sentences are scanned once to count spaces; only counters are maintained.

### Problem description

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
 
 You are given an array of strings sentences , where each sentences[i] represents a single sentence . 
 
 Return the maximum number of words that appear in a single sentence . 

 Example 1: 
 
```
Input:
 sentences = ["alice and bob love leetcode", "i think so too", 
"this is great thanks very much"
]

Output:
 6

Explanation:
 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
```

 Example 2: 
 
```
Input:
 sentences = ["please wait", 
"continue to fight"
, 
"continue to win"
]

Output:
 3

Explanation:
 It is possible that multiple sentences contain the same number of words. 
In this example, the second and third sentences (underlined) have the same number of words.
```

 Constraints: 

 1 <= sentences.length <= 100 
 
 1 <= sentences[i].length <= 100 
 
 sentences[i] consists only of lowercase English letters and ' ' only. 
 
 sentences[i] does not have leading or trailing spaces. 
 
 All the words in sentences[i] are separated by a single space.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 int mostWordsFound(vector<string>& sentences){
  int ans=0;for(const string&s:sentences){int cnt=1;for(char c:s)cnt+=(c==' ');ans=max(ans,cnt);}return ans;
 }
};
```


## 2120. Execution of All Suffix Instructions Staying in a Grid

**Problem:** https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(m²)

**Space complexity:** O(m)

**Complexity reasoning:** Every suffix of the m instructions is simulated until it ends or leaves the grid; the answer has m entries.

### Problem description

There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1) . You are given the integer n and an integer array startPos where startPos = [start row , start col ] indicates that a robot is initially at cell (start row , start col ) . 
 
 You are also given a 0-indexed string s of length m where s[i] is the i th instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down). 
 
 The robot can begin executing from any i th instruction in s . It executes the instructions one by one towards the end of s but it stops if either of these conditions is met: 

 The next instruction will move the robot off the grid. 
 
 There are no more instructions left to execute. 

 Return an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot begins executing from the i th instruction in s . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/12/09/1.png] 
 
```
Input:
 n = 3, startPos = [0,1], s = "RRDDLU"

Output:
 [1,5,4,3,1,0]

Explanation:
 Starting from startPos and beginning execution from the i
th
 instruction:
- 0
th
: "
R
RDDLU". Only one instruction "R" can be executed before it moves off the grid.
- 1
st
: "
RDDLU
". All five instructions can be executed while it stays in the grid and ends at (1, 1).
- 2
nd
: "
DDLU
". All four instructions can be executed while it stays in the grid and ends at (1, 0).
- 3
rd
: "
DLU
". All three instructions can be executed while it stays in the grid and ends at (0, 0).
- 4
th
: "
L
U". Only one instruction "L" can be executed before it moves off the grid.
- 5
th
: "U". If moving up, it would move off the grid.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/12/09/2.png] 
 
```
Input:
 n = 2, startPos = [1,1], s = "LURD"

Output:
 [4,1,0,0]

Explanation:

- 0
th
: "
LURD
".
- 1
st
: "
U
RD".
- 2
nd
: "RD".
- 3
rd
: "D".
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/12/09/3.png] 
 
```
Input:
 n = 1, startPos = [0,0], s = "LRUD"

Output:
 [0,0,0,0]

Explanation:
 No matter which instruction the robot begins execution from, it would move off the grid.
```

 Constraints: 

 m == s.length 
 
 1 <= n, m <= 500 
 
 startPos.length == 2 
 
 0 <= start row , start col < n 
 
 s consists of 'L' , 'R' , 'U' , and 'D' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 vector<int> executeInstructions(int n,vector<int>& startPos,string s){
  vector<int> ans;int m=s.size();
  for(int i=0;i<m;++i){int r=startPos[0],c=startPos[1],j=i;
   for(;j<m;++j){char x=s[j];r+=(x=='D')-(x=='U');c+=(x=='R')-(x=='L');
    if(r<0||r>=n||c<0||c>=n)break;
   }
   ans.push_back(j-i);
  }
  return ans;
 }
};
```


## 2124. Check if All A's Appears Before All B's

**Problem:** https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** The fixed two-character pattern ba is searched for across the string.

### Problem description

Given a string s consisting of only the characters 'a' and 'b' , return true if every 'a' appears before every 'b' in the string . Otherwise, return false . 

 Example 1: 
 
```
Input:
 s = "aaabbb"

Output:
 true

Explanation:

The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.
```

 Example 2: 
 
```
Input:
 s = "abab"

Output:
 false

Explanation:

There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.
```

 Example 3: 
 
```
Input:
 s = "bbb"

Output:
 true

Explanation:

There are no 'a's, hence, every 'a' appears before every 'b' and we return true.
```

 Constraints: 

 1 <= s.length <= 100 
 
 s[i] is either 'a' or 'b' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 bool checkString(string s){return s.find("ba")==string::npos;}
};
```


## 2125. Number of Laser Beams in a Bank

**Problem:** https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Math, String, Matrix

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(C)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Each bank row is scanned once by count; only the previous nonempty row count and total are retained.

### Problem description

Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the i th row, consisting of '0' s and '1' s. '0' means the cell is empty, while '1' means the cell has a security device. 
 
 There is one laser beam between any two security devices if both conditions are met: 

 The two devices are located on two different rows : r 1 and r 2 , where r 1 < r 2 . 
 
 For each row i where r 1 < i < r 2 , there are no security devices in the i th row. 

 Laser beams are independent, i.e., one beam does not interfere nor join with another. 
 
 Return the total number of laser beams in the bank . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/12/24/laser1.jpg] 
 
```
Input:
 bank = ["011001","000000","010100","001000"]

Output:
 8

Explanation:
 Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0
th
 row with any on the 3
rd
 row.
This is because the 2
nd
 row contains security devices, which breaks the second condition.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/12/24/laser2.jpg] 
 
```
Input:
 bank = ["000","111","000"]

Output:
 0

Explanation:
 There does not exist two devices located on two different rows.
```

 Constraints: 

 m == bank.length 
 
 n == bank[i].length 
 
 1 <= m, n <= 500 
 
 bank[i][j] is either '0' or '1' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 int numberOfBeams(vector<string>& bank){
  int prev=0,ans=0;for(const string& row:bank){int cur=count(row.begin(),row.end(),'1');
   if(cur){ans+=prev*cur;prev=cur;}
  }
  return ans;
 }
};
```


## 2129. Capitalize the Title

**Problem:** https://leetcode.com/problems/capitalize-the-title/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** The input title is modified in place, with each word traversed to locate its end and lowercase its characters.

### Problem description

You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that: 

 If the length of the word is 1 or 2 letters, change all letters to lowercase. 
 
 Otherwise, change the first letter to uppercase and the remaining letters to lowercase. 

 Return the capitalized title . 

 Example 1: 
 
```
Input:
 title = "capiTalIze tHe titLe"

Output:
 "Capitalize The Title"

Explanation:

Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.
```

 Example 2: 
 
```
Input:
 title = "First leTTeR of EACH Word"

Output:
 "First Letter of Each Word"

Explanation:

The word "of" has length 2, so it is all lowercase.
The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.
```

 Example 3: 
 
```
Input:
 title = "i lOve leetcode"

Output:
 "i Love Leetcode"

Explanation:

The word "i" has length 1, so it is lowercase.
The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.
```

 Constraints: 

 1 <= title.length <= 100 
 
 title consists of words separated by a single space without any leading or trailing spaces. 
 
 Each word consists of uppercase and lowercase English letters and is non-empty .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 string capitalizeTitle(string title){
  int n=title.size();for(int i=0;i<n;){int j=i;while(j<n && title[j]!=' ')++j;
   for(int k=i;k<j;++k)title[k]=tolower(title[k]);
   if(j-i>2)title[i]=toupper(title[i]);i=j+1;
  }
  return title;
 }
};
```


## 2138. Divide a String Into Groups of Size k

**Problem:** https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + k)

**Space complexity:** O(n + k)

**Complexity reasoning:** At most k−1 padding characters are appended; each padded character is copied once into the returned groups.

### Problem description

A string s can be partitioned into groups of size k using the following procedure: 

 The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each element can be a part of exactly one group. 
 
 For the last group, if the string does not have k characters remaining, a character fill is used to complete the group. 

 Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s . 
 
 Given the string s , the size of each group k and the character fill , return a string array denoting the composition of every group s has been divided into, using the above procedure . 

 Example 1: 
 
```
Input:
 s = "abcdefghi", k = 3, fill = "x"

Output:
 ["abc","def","ghi"]

Explanation:

The first 3 characters "abc" form the first group.
The next 3 characters "def" form the second group.
The last 3 characters "ghi" form the third group.
Since all groups can be completely filled by characters from the string, we do not need to use fill.
Thus, the groups formed are "abc", "def", and "ghi".
```

 Example 2: 
 
```
Input:
 s = "abcdefghij", k = 3, fill = "x"

Output:
 ["abc","def","ghi","jxx"]

Explanation:

Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".
```

 Constraints: 

 1 <= s.length <= 100 
 
 s consists of lowercase English letters only. 
 
 1 <= k <= 100 
 
 fill is a lowercase English letter.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 vector<string> divideString(string s,int k,char fill){
  while(s.size()%k)s+=fill;vector<string> ans;
  for(int i=0;i<(int)s.size();i+=k)ans.push_back(s.substr(i,k));return ans;
 }
};
```


## 2185. Counting Words With a Given Prefix

**Problem:** https://leetcode.com/problems/counting-words-with-a-given-prefix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String, String Matching

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(P · L)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Each of P words is checked against the prefix using a comparison of up to L prefix characters.

### Problem description

You are given an array of strings words and a string pref . 
 
 Return the number of strings in words that contain pref as a prefix . 
 
 A prefix of a string s is any leading contiguous substring of s . 

 Example 1: 
 
```
Input:
 words = ["pay","
at
tention","practice","
at
tend"], 
pref 
= "at"

Output:
 2

Explanation:
 The 2 strings that contain "at" as a prefix are: "
at
tention" and "
at
tend".
```

 Example 2: 
 
```
Input:
 words = ["leetcode","win","loops","success"], 
pref 
= "code"

Output:
 0

Explanation:
 There are no strings that contain "code" as a prefix.
```

 Constraints: 

 1 <= words.length <= 100 
 
 1 <= words[i].length, pref.length <= 100 
 
 words[i] and pref consist of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int ans=0;
        for(const string& w:words) if(w.size()>=pref.size()&&w.compare(0,pref.size(),pref)==0) ++ans;
        return ans;
    }
};
```


## 2194. Cells in a Range on an Excel Sheet

**Problem:** https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(R · C)

**Space complexity:** O(R · C)

**Complexity reasoning:** The nested loops generate every cell name in the requested R-row by C-column range, storing all names in the result.

### Problem description

A cell (r, c) of an excel sheet is represented as a string "<col><row>" where: 

 <col> denotes the column number c of the cell. It is represented by alphabetical letters .

 For example, the 1 st column is denoted by 'A' , the 2 nd by 'B' , the 3 rd by 'C' , and so on. 

 <row> is the row number r of the cell. The r th row is represented by the integer r . 

 You are given a string s  in the format "<col1><row1>:<col2><row2>" , where <col1> represents the column c1 , <row1> represents the row r1 , <col2> represents the column c2 , and <row2> represents the row r2 , such that r1 <= r2 and c1 <= c2 . 
 
 Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2 . The cells should be represented as  strings in the format mentioned above and be sorted in non-decreasing order first by columns and then by rows. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/08/ex1drawio.png] 
 
```
Input:
 s = "K1:L2"

Output:
 ["K1","K2","L1","L2"]

Explanation:

The above diagram shows the cells which should be present in the list.
The red arrows denote the order in which the cells should be presented.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/09/exam2drawio.png] 
 
```
Input:
 s = "A1:F1"

Output:
 ["A1","B1","C1","D1","E1","F1"]

Explanation:

The above diagram shows the cells which should be present in the list.
The red arrow denotes the order in which the cells should be presented.
```

 Constraints: 

 s.length == 5 
 
 'A' <= s[0] <= s[3] <= 'Z' 
 
 '1' <= s[1] <= s[4] <= '9' 
 
 s consists of uppercase English letters, digits and ':' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 vector<string> cellsInRange(string s){vector<string> ans;for(char c=s[0];c<=s[3];++c)for(char r=s[1];r<=s[4];++r)ans.push_back(string()+c+r);return ans;}
};
```


## 2211. Count Collisions on a Road

**Problem:** https://leetcode.com/problems/count-collisions-on-a-road/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Two scans trim non-colliding boundary cars and one scan counts nonstationary cars in the remaining range.

### Problem description

There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point. 
 
 You are given a 0-indexed string directions of length n . directions[i] can be either 'L' , 'R' , or 'S' denoting whether the i th car is moving towards the left , towards the right , or staying at its current point respectively. Each moving car has the same speed . 
 
 The number of collisions can be calculated as follows: 

 When two cars moving in opposite directions collide with each other, the number of collisions increases by 2 . 
 
 When a moving car collides with a stationary car, the number of collisions increases by 1 . 

 After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion. 
 
 Return the total number of collisions that will happen on the road . 

 Example 1: 
 
```
Input:
 directions = "RLRSLL"

Output:
 5

Explanation:

The collisions that will happen on the road are:
- Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 0 + 2 = 2.
- Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
- Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
- Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision and get hit by car 5. The number of collisions becomes 4 + 1 = 5.
Thus, the total number of collisions that will happen on the road is 5.
```

 Example 2: 
 
```
Input:
 directions = "LLRR"

Output:
 0

Explanation:

No cars will collide with each other. Thus, the total number of collisions that will happen on the road is 0.
```

 Constraints: 

 1 <= directions.length <= 10 5 
 
 directions[i] is either 'L' , 'R' , or 'S' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 int countCollisions(string directions){int l=0,r=(int)directions.size()-1;while(l<=r&&directions[l]=='L')++l;while(r>=l&&directions[r]=='R')--r;
  int ans=0;for(int i=l;i<=r;++i)ans+=directions[i]!='S';return ans;
 }
};
```


## 2232. Minimize Result by Adding Parentheses to Expression

**Problem:** https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Enumeration

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n⁴) worst case

**Space complexity:** O(n) auxiliary

**Complexity reasoning:** There are O(n²) pairs of parenthesis positions; each candidate performs multiple substrings/conversions and can build an O(n)-length answer.

### Problem description

You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent positive integers. 
 
 Add a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+' . 
 
 Return expression after adding a pair of parentheses such that expression evaluates to the smallest possible value. If there are multiple answers that yield the same result, return any of them. 
 
 The input has been generated such that the original value of expression , and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer. 

 Example 1: 
 
```
Input:
 expression = "247+38"

Output:
 "2(47+38)"

Explanation:
 The 
expression
 evaluates to 2 * (47 + 38) = 2 * 85 = 170.
Note that "2(4)7+38" is invalid because the right parenthesis must be to the right of the 
'+'
.
It can be shown that 170 is the smallest possible value.
```

 Example 2: 
 
```
Input:
 expression = "12+34"

Output:
 "1(2+3)4"

Explanation:
 The expression evaluates to 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20.
```

 Example 3: 
 
```
Input:
 expression = "999+999"

Output:
 "(999+999)"

Explanation:
 The 
expression
 evaluates to 999 + 999 = 1998.
```

 Constraints: 

 3 <= expression.length <= 10 
 
 expression consists of digits from '1' to '9' and '+' . 
 
 expression starts and ends with digits. 
 
 expression contains exactly one '+' . 
 
 The original value of expression , and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 string minimizeResult(string expression){int plus=expression.find('+'),n=expression.size();long long best=LLONG_MAX;string ans;
  for(int i=0;i<plus;++i)for(int j=plus+2;j<=n;++j){long long a=i?stoll(expression.substr(0,i)):1;
   long long b=stoll(expression.substr(i,plus-i)),c=stoll(expression.substr(plus+1,j-plus-1));
   long long d=j<n?stoll(expression.substr(j)):1;long long val=a*(b+c)*d;
   if(val<best){best=val;ans=expression.substr(0,i)+"("+expression.substr(i,j-i)+")"+expression.substr(j);}
  }return ans;
 }
};
```


## 2243. Calculate Digit Sum of a String

**Problem:** https://leetcode.com/problems/calculate-digit-sum-of-a-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n · (1 + log k)) per round; O(n · r · (1 + log k)) total upper bound

**Space complexity:** O(n)

**Complexity reasoning:** Each round scans all current digits and converts group sums (at most O(log k) digits); r is the number of rounds and the intermediate string is O(n).

### Problem description

You are given a string s consisting of digits and an integer k . 
 
 A round can be completed if the length of s is greater than k . In one round, do the following: 

 Divide s into consecutive groups of size k such that the first k characters are in the first group, the next k characters are in the second group, and so on. Note that the size of the last group can be smaller than k . 
 
 Replace each group of s with a string representing the sum of all its digits. For example, "346" is replaced with "13" because 3 + 4 + 6 = 13 . 
 
 Merge consecutive groups together to form a new string. If the length of the string is greater than k , repeat from step 1 . 

 Return s after all rounds have been completed . 

 Example 1: 
 
```
Input:
 s = "11111222223", k = 3

Output:
 "135"

Explanation:
 
- For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".
 ​​​​​Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5. 
  So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round.
- For the second round, we divide s into "346" and "5".
  Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5. 
  So, s becomes "13" + "5" = "135" after second round. 
Now, s.length <= k, so we return "135" as the answer.
```

 Example 2: 
 
```
Input:
 s = "00000000", k = 3

Output:
 "000"

Explanation:
 
We divide s into "000", "000", and "00".
Then we calculate the digit sum of each group: 0 + 0 + 0 = 0, 0 + 0 + 0 = 0, and 0 + 0 = 0. 
s becomes "0" + "0" + "0" = "000", whose length is equal to k, so we return "000".
```

 Constraints: 

 1 <= s.length <= 100 
 
 2 <= k <= 100 
 
 s consists of digits only.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public: string digitSum(string s,int k){while((int)s.size()>k){string t;for(int i=0;i<(int)s.size();i+=k){int sum=0;for(int j=i;j<min((int)s.size(),i+k);++j)sum+=s[j]-'0';t+=to_string(sum);}s=t;}return s;} };
```


## 2255. Count Prefixes of a Given String

**Problem:** https://leetcode.com/problems/count-prefixes-of-a-given-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(P · L)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Each of P candidate prefixes compares up to L characters against the start of s.

### Problem description

You are given a string array words and a string s , where words[i] and s comprise only of lowercase English letters . 
 
 Return the number of strings in words that are a prefix of s . 
 
 A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string. 

 Example 1: 
 
```
Input:
 words = ["a","b","c","ab","bc","abc"], s = "abc"

Output:
 3

Explanation:

The strings in words which are a prefix of s = "abc" are:
"a", "ab", and "abc".
Thus the number of strings in words which are a prefix of s is 3.
```

 Example 2: 
 
```
Input:
 words = ["a","a"], s = "aa"

Output:
 2

Explanation:

Both of the strings are a prefix of s. 
Note that the same string can occur multiple times in words, and it should be counted each time.
```

 Constraints: 

 1 <= words.length <= 1000 
 
 1 <= words[i].length, s.length <= 10 
 
 words[i] and s consist of lowercase English letters only .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {public:int countPrefixes(vector<string>& words,string s){int ans=0;for(auto &w:words)if(s.size()>=w.size()&&s.compare(0,w.size(),w)==0)++ans;return ans;} };
```


## 2264. Largest 3-Same-Digit Number in String

**Problem:** https://leetcode.com/problems/largest-3-same-digit-number-in-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Every length-three window is checked once; only a constant-size best substring is stored.

### Problem description

You are given a string num representing a large integer. An integer is good if it meets the following conditions: 

 It is a substring of num with length 3 . 
 
 It consists of only one unique digit. 

 Return the maximum good integer as a string or an empty string "" if no such integer exists . 
 
 Note: 

 A substring is a contiguous sequence of characters within a string. 
 
 There may be leading zeroes in num or a good integer. 

 Example 1: 
 
```
Input:
 num = "6
777
133339"

Output:
 "777"

Explanation:
 There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
```

 Example 2: 
 
```
Input:
 num = "23
000
19"

Output:
 "000"

Explanation:
 "000" is the only good integer.
```

 Example 3: 
 
```
Input:
 num = "42352338"

Output:
 ""

Explanation:
 No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
```

 Constraints: 

 3 <= num.length <= 1000 
 
 num only consists of digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {public:string largestGoodInteger(string num){string ans="";for(int i=0;i+2<(int)num.size();++i)if(num[i]==num[i+1]&&num[i]==num[i+2])ans=max(ans,num.substr(i,3));return ans;} };
```


## 2278. Percentage of Letter in String

**Problem:** https://leetcode.com/problems/percentage-of-letter-in-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** std::count scans the entire input string once.

### Problem description

Given a string s and a character letter , return the percentage of characters in s that equal letter rounded down to the nearest whole percent. 

 Example 1: 
 
```
Input:
 s = "foobar", letter = "o"

Output:
 33

Explanation:

The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
```

 Example 2: 
 
```
Input:
 s = "jjjj", letter = "k"

Output:
 0

Explanation:

The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
```

 Constraints: 

 1 <= s.length <= 100 
 
 s consists of lowercase English letters. 
 
 letter is a lowercase English letter.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {public:int percentageLetter(string s,char letter){return 100*count(s.begin(),s.end(),letter)/(int)s.size();} };
```


## 2288. Apply Discount to Prices

**Problem:** https://leetcode.com/problems/apply-discount-to-prices/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + Σ dᵢ) typical

**Space complexity:** O(n + Σ dᵢ)

**Complexity reasoning:** Stream tokenization scans the sentence; valid price tokens are parsed and formatted with dᵢ digits, and the reconstructed sentence is stored.

### Problem description

A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$' . A word represents a price if it is a sequence of digits preceded by a dollar sign. 

 For example, "$100" , "$23" , and "$6" represent prices while "100" , "$" , and "$1e5" do not. 

 You are given a string sentence representing a sentence and an integer discount . For each word representing a price, apply a discount of discount% on the price and update the word in the sentence. All updated prices should be represented with exactly two decimal places. 
 
 Return a string representing the modified sentence . 
 
 Note that all prices will contain at most 10 digits. 

 Example 1: 
 
```
Input:
 sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50

Output:
 "there are $0.50 $1.00 and 5$ candies in the shop"

Explanation:
 
The words which represent prices are "$1" and "$2". 
- A 50% discount on "$1" yields "$0.50", so "$1" is replaced by "$0.50".
- A 50% discount on "$2" yields "$1". Since we need to have exactly 2 decimal places after a price, we replace "$2" with "$1.00".
```

 Example 2: 
 
```
Input:
 sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100

Output:
 "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"

Explanation:
 
Applying a 100% discount on any price will result in 0.
The words representing prices are "$3", "$5", "$6", and "$9".
Each of them is replaced by "$0.00".
```

 Constraints: 

 1 <= sentence.length <= 10 5 
 
 sentence consists of lowercase English letters, digits, ' ' , and '$' . 
 
 sentence does not have leading or trailing spaces. 
 
 All words in sentence are separated by a single space. 
 
 All prices will be positive numbers without leading zeros. 
 
 All prices will have at most 10 digits. 
 
 0 <= discount <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:string discountPrices(string sentence,int discount){istringstream in(sentence);string w,out;while(in>>w){bool ok=w.size()>1&&w[0]=='$';for(int i=1;i<(int)w.size();++i)if(!isdigit((unsigned char)w[i]))ok=false;if(ok){long double x=stold(w.substr(1))*(100-discount)/100;ostringstream os;os<<'$'<<fixed<<setprecision(2)<<x;w=os.str();}if(!out.empty())out+=' ';out+=w;}return out;}};
```


## 2296. Design a Text Editor

**Problem:** https://leetcode.com/problems/design-a-text-editor/

**Difficulty:** Hard | **Premium:** No

**Tags:** Linked List, String, Stack, Design, Simulation, Doubly-Linked List

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Linked List / Pointers, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Linked list, Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** addText O(t); deleteText O(1) amortized; cursorLeft/cursorRight O(k + 10)

**Space complexity:** O(N)

**Complexity reasoning:** Two strings hold the text on either side of the cursor. Cursor movement transfers up to k characters; tail copies at most ten. addText appends t characters.

### Problem description

Design a text editor with a cursor that can do the following: 

 Add text to where the cursor is. 
 
 Delete text from where the cursor is (simulating the backspace key). 
 
 Move the cursor either left or right. 

 When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds. 
 
 Implement the TextEditor class: 

 TextEditor() Initializes the object with empty text. 
 
 void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text . 
 
 int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted. 
 
 string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor. 
 
 string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor. 

 Example 1: 
 
```
Input

["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]

Output

[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]

Explanation

TextEditor textEditor = new TextEditor(); // The current text is "|". (The '|' character represents the cursor)
textEditor.addText("leetcode"); // The current text is "leetcode|".
textEditor.deleteText(4); // return 4
 // The current text is "leet|". 
 // 4 characters were deleted.
textEditor.addText("practice"); // The current text is "leetpractice|". 
textEditor.cursorRight(3); // return "etpractice"
 // The current text is "leetpractice|". 
 // The cursor cannot be moved beyond the actual text and thus did not move.
 // "etpractice" is the last 10 characters to the left of the cursor.
textEditor.cursorLeft(8); // return "leet"
 // The current text is "leet|practice".
 // "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
textEditor.deleteText(10); // return 4
 // The current text is "|practice".
 // Only 4 characters were deleted.
textEditor.cursorLeft(2); // return ""
 // The current text is "|practice".
 // The cursor cannot be moved beyond the actual text and thus did not move. 
 // "" is the last min(10, 0) = 0 characters to the left of the cursor.
textEditor.cursorRight(6); // return "practi"
 // The current text is "practi|ce".
 // "practi" is the last min(10, 6) = 6 characters to the left of the cursor.
```

 Constraints: 

 1 <= text.length, k <= 40 
 
 text consists of lowercase English letters. 
 
 At most 2 * 10 4 calls in total will be made to addText , deleteText , cursorLeft and cursorRight . 

 Follow-up: Could you find a solution with time complexity of O(k) per call?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class TextEditor {string left,right;string tail(){return left.substr(left.size()>10?left.size()-10:0);}public:TextEditor(){}void addText(string text){left+=text;}int deleteText(int k){int t=min(k,(int)left.size());left.resize(left.size()-t);return t;}string cursorLeft(int k){int t=min(k,(int)left.size());while(t--){right.push_back(left.back());left.pop_back();}return tail();}string cursorRight(int k){int t=min(k,(int)right.size());while(t--){left.push_back(right.back());right.pop_back();}return tail();}};
```


## 2299. Strong Password Checker II

**Problem:** https://leetcode.com/problems/strong-password-checker-ii/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Each password character is inspected once; the special-character set has fixed size.

### Problem description

A password is said to be strong if it satisfies all the following criteria: 

 It has at least 8 characters. 
 
 It contains at least one lowercase letter. 
 
 It contains at least one uppercase letter. 
 
 It contains at least one digit . 
 
 It contains at least one special character . The special characters are the characters in the following string: "!@#$%^&*()-+" . 
 
 It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not). 

 Given a string password , return true if it is a strong password . Otherwise, return false . 

 Example 1: 
 
```
Input:
 password = "IloveLe3tcode!"

Output:
 true

Explanation:
 The password meets all the requirements. Therefore, we return true.
```

 Example 2: 
 
```
Input:
 password = "Me+You--IsMyDream"

Output:
 false

Explanation:
 The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
```

 Example 3: 
 
```
Input:
 password = "1aB!"

Output:
 false

Explanation:
 The password does not meet the length requirement. Therefore, we return false.
```

 Constraints: 

 1 <= password.length <= 100 
 
 password consists of letters, digits, and special characters: "!@#$%^&*()-+" .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:bool strongPasswordCheckerII(string password){if(password.size()<8)return false;bool lo=0,up=0,dig=0,sp=0;string specials="!@#$%^&*()-+";for(int i=0;i<(int)password.size();++i){char c=password[i];if(i&&c==password[i-1])return false;lo|=islower((unsigned char)c)!=0;up|=isupper((unsigned char)c)!=0;dig|=isdigit((unsigned char)c)!=0;sp|=specials.find(c)!=string::npos;}return lo&&up&&dig&&sp;}};
```


## 2315. Count Asterisks

**Problem:** https://leetcode.com/problems/count-asterisks/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One scan toggles the inside-bars flag and counts eligible asterisks.

### Problem description

You are given a string s , where every two consecutive vertical bars '|' are grouped into a pair . In other words, the 1 st and 2 nd '|' make a pair, the 3 rd and 4 th '|' make a pair, and so forth. 
 
 Return the number of '*' in s , excluding the '*' between each pair of '|' . 
 
 Note that each '|' will belong to exactly one pair. 

 Example 1: 
 
```
Input:
 s = "l|*e*et|c**o|*de|"

Output:
 2

Explanation:
 The considered characters are underlined: "
l
|*e*et|
c**o
|*de|".
The characters between the first and second '|' are excluded from the answer.
Also, the characters between the third and fourth '|' are excluded from the answer.
There are 2 asterisks considered. Therefore, we return 2.
```

 Example 2: 
 
```
Input:
 s = "iamprogrammer"

Output:
 0

Explanation:
 In this example, there are no asterisks in s. Therefore, we return 0.
```

 Example 3: 
 
```
Input:
 s = "yo|uar|e**|b|e***au|tifu|l"

Output:
 5

Explanation:
 The considered characters are underlined: "
yo
|uar|
e**
|b|
e***au
|tifu|
l
". There are 5 asterisks considered. Therefore, we return 5.
```

 Constraints: 

 1 <= s.length <= 1000 
 
 s consists of lowercase English letters, vertical bars '|' , and asterisks '*' . 
 
 s contains an even number of vertical bars '|' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:int countAsterisks(string s){bool inside=false;int ans=0;for(char c:s){if(c=='|')inside=!inside;else if(c=='*'&&!inside)++ans;}return ans;}};
```


## 2390. Removing Stars From a String

**Problem:** https://leetcode.com/problems/removing-stars-from-a-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each character is appended or causes one removal from the output-as-stack.

### Problem description

You are given a string s , which contains stars * . 
 
 In one operation, you can: 

 Choose a star in s . 
 
 Remove the closest non-star character to its left , as well as remove the star itself. 

 Return the string after all stars have been removed . 
 
 Note: 

 The input will be generated such that the operation is always possible. 
 
 It can be shown that the resulting string will always be unique. 

 Example 1: 
 
```
Input:
 s = "leet**cod*e"

Output:
 "lecoe"

Explanation:
 Performing the removals from left to right:
- The closest character to the 1
st
 star is 't' in "lee
t
**cod*e". s becomes "lee*cod*e".
- The closest character to the 2
nd
 star is 'e' in "le
e
*cod*e". s becomes "lecod*e".
- The closest character to the 3
rd
 star is 'd' in "leco
d
*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
```

 Example 2: 
 
```
Input:
 s = "erase*****"

Output:
 ""

Explanation:
 The entire string is removed, so we return an empty string.
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists of lowercase English letters and stars * . 
 
 The operation above can be performed on s .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string removeStars(string s){string out;for(char c:s){if(c=='*')out.pop_back();else out.push_back(c);}return out;}};
```


## 2409. Count Days Spent Together

**Problem:** https://leetcode.com/problems/count-days-spent-together/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Each date conversion parses fixed-width components and sums at most eleven month lengths.

### Problem description

Alice and Bob are traveling to Rome for separate business meetings. 
 
 You are given 4 strings arriveAlice , leaveAlice , arriveBob , and leaveBob . Alice will be in the city from the dates arriveAlice to leaveAlice ( inclusive ), while Bob will be in the city from the dates arriveBob to leaveBob ( inclusive ). Each will be a 5-character string in the format "MM-DD" , corresponding to the month and day of the date. 
 
 Return the total number of days that Alice and Bob are in Rome together. 
 
 You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] . 

 Example 1: 
 
```
Input:
 arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"

Output:
 3

Explanation:
 Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
```

 Example 2: 
 
```
Input:
 arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"

Output:
 0

Explanation:
 There is no day when Alice and Bob are in Rome together, so we return 0.
```

 Constraints: 

 All dates are provided in the format "MM-DD" . 
 
 Alice and Bob's arrival dates are earlier than or equal to their leaving dates. 
 
 The given dates are valid dates of a non-leap year.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {int day(string s){int m=stoi(s.substr(0,2)),d=stoi(s.substr(3));int a[]={31,28,31,30,31,30,31,31,30,31,30,31};for(int i=0;i<m-1;i++)d+=a[i];return d;}public:int countDaysTogether(string arriveAlice,string leaveAlice,string arriveBob,string leaveBob){return max(0,min(day(leaveAlice),day(leaveBob))-max(day(arriveAlice),day(arriveBob))+1);}};
```


## 2414. Length of the Longest Alphabetical Continuous Substring

**Problem:** https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** One scan tracks the current consecutive alphabetical run and the maximum run length.

### Problem description

An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz" . 

 For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not. 

 Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring. 

 Example 1: 
 
```
Input:
 s = "abacaba"

Output:
 2

Explanation:
 There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.
```

 Example 2: 
 
```
Input:
 s = "abcde"

Output:
 5

Explanation:
 "abcde" is the longest continuous substring.
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists of only English lowercase letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int longestContinuousSubstring(string s){int cur=1,best=1;for(int i=1;i<(int)s.size();i++){cur=(s[i]==s[i-1]+1)?cur+1:1;best=max(best,cur);}return best;}};
```


## 2437. Number of Valid Clock Times

**Problem:** https://leetcode.com/problems/number-of-valid-clock-times/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Enumeration

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** The implementation enumerates exactly 24 × 60 clock times, comparing five characters each.

### Problem description

You are given a string of length 5 called time , representing the current time on a digital clock in the format "hh:mm" . The earliest possible time is "00:00" and the latest possible time is "23:59" . 
 
 In the string time , the digits represented by the ?  symbol are unknown , and must be replaced with a digit from 0 to 9 . 
 
 Return an integer answer , the number of valid clock times that can be created by replacing every ?  with a digit from 0 to 9 . 

 Example 1: 
 
```
Input:
 time = "?5:00"

Output:
 2

Explanation:
 We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.
```

 Example 2: 
 
```
Input:
 time = "0?:0?"

Output:
 100

Explanation:
 Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.
```

 Example 3: 
 
```
Input:
 time = "??:??"

Output:
 1440

Explanation:
 There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.
```

 Constraints: 

 time is a valid string of length 5 in the format "hh:mm" . 
 
 "00" <= hh <= "23" 
 
 "00" <= mm <= "59" 
 
 Some of the digits might be replaced with '?' and need to be replaced with digits from 0 to 9 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int countTime(string time){int ans=0;for(int h=0;h<24;++h)for(int m=0;m<60;++m){string s=to_string(h/10)+to_string(h%10)+":"+to_string(m/10)+to_string(m%10);bool ok=true;for(int i=0;i<5;++i)if(time[i]!='?'&&time[i]!=s[i])ok=false;ans+=ok;}return ans;} };
```


## 2446. Determine if Two Events Have Conflict

**Problem:** https://leetcode.com/problems/determine-if-two-events-have-conflict/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Four fixed-width time strings are compared lexicographically with a constant number of operations.

### Problem description

You are given two arrays of strings that represent two inclusive events that happened on the same day , event1 and event2 , where: 

 event1 = [startTime 1 , endTime 1 ] and 
 
 event2 = [startTime 2 , endTime 2 ] . 

 Event times are valid 24 hours format in the form of HH:MM . 
 
 A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events). 
 
 Return true if there is a conflict between two events. Otherwise, return false . 

 Example 1: 
 
```
Input:
 event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]

Output:
 true

Explanation:
 The two events intersect at time 2:00.
```

 Example 2: 
 
```
Input:
 event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]

Output:
 true

Explanation:
 The two events intersect starting from 01:20 to 02:00.
```

 Example 3: 
 
```
Input:
 event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]

Output:
 false

Explanation:
 The two events do not intersect.
```

 Constraints: 

 event1.length == event2.length == 2 
 
 event1[i].length == event2[i].length == 5 
 
 startTime 1 <= endTime 1 
 
 startTime 2 <= endTime 2 
 
 All the event times follow the HH:MM format.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: bool haveConflict(vector<string>& event1,vector<string>& event2){return event1[0]<=event2[1] && event2[0]<=event1[1];} };
```


## 2450. Number of Distinct Binary Strings After Applying Operations

**Problem:** https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(log n)

**Space complexity:** O(1)

**Complexity reasoning:** Binary exponentiation repeatedly halves exponent n = |s|-k+1, using constant scalar state.

### Problem description

You are given a binary string s and a positive integer k . 
 
 You can apply the following operation on the string any number of times: 

 Choose any substring of size k from s and flip all its characters, that is, turn all 1 's into 0 's, and all 0 's into 1 's. 

 Return the number of distinct strings you can obtain . Since the answer may be too large, return it modulo 10 9 + 7 . 
 
 Note that: 

 A binary string is a string that consists only of the characters 0 and 1 . 
 
 A substring is a contiguous part of a string. 

 Example 1: 
 
```
Input:
 s = "1001", k = 3

Output:
 4

Explanation:
 We can obtain the following strings:
- Applying no operation on the string gives s = "1001".
- Applying one operation on the substring starting at index 0 gives s = "
011
1".
- Applying one operation on the substring starting at index 1 gives s = "1
110
".
- Applying one operation on both the substrings starting at indices 0 and 1 gives s = "
0000
".
It can be shown that we cannot obtain any other string, so the answer is 4.
```

 Example 2: 
 
```
Input:
 s = "10110", k = 5

Output:
 2

Explanation:
 We can obtain the following strings:
- Applying no operation on the string gives s = "10110".
- Applying one operation on the whole string gives s = "01001".
It can be shown that we cannot obtain any other string, so the answer is 2.
```

 Constraints: 

 1 <= k <= s.length <= 10 5 
 
 s[i] is either 0 or 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int countDistinctStrings(string s, int k) {
        const int MOD = 1000000007;
        int exponent = (int)s.size() - k + 1;
        long long answer = 1, base = 2;
        while (exponent > 0) {
            if (exponent & 1) answer = answer * base % MOD;
            base = base * base % MOD;
            exponent >>= 1;
        }
        return (int)answer;
    }
};
```


## 2468. Split Message Based on Limit

**Problem:** https://leetcode.com/problems/split-message-based-on-limit/

**Difficulty:** Hard | **Premium:** No

**Tags:** String, Enumeration

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n² + n log n)

**Space complexity:** O(n + p)

**Complexity reasoning:** Tries up to n candidate part counts, computing digit lengths; for a successful count, builds p strings totaling O(n + p log p) characters. Worst-case candidate checks are O(n log n) digit work; repeated construction may yield O(n²) overall, with output storage O(n + p log p).

### Problem description

You are given a string, message , and a positive integer, limit . 
 
 You must split message into one or more parts based on limit . Each resulting part should have the suffix "<a/b>" , where "b" is to be replaced with the total number of parts and "a" is to be replaced with the index of the part, starting from 1 and going up to b . Additionally, the length of each resulting part (including its suffix) should be equal to limit , except for the last part whose length can be at most limit . 
 
 The resulting parts should be formed such that when their suffixes are removed and they are all concatenated in order , they should be equal to message . Also, the result should contain as few parts as possible. 
 
 Return the parts message would be split into as an array of strings . If it is impossible to split message as required, return an empty array . 

 Example 1: 
 
```
Input:
 message = "this is really a very awesome message", limit = 9

Output:
 ["thi<1/14>","s i<2/14>","s r<3/14>","eal<4/14>","ly <5/14>","a v<6/14>","ery<7/14>"," aw<8/14>","eso<9/14>","me<10/14>"," m<11/14>","es<12/14>","sa<13/14>","ge<14/14>"]

Explanation:

The first 9 parts take 3 characters each from the beginning of message.
The next 5 parts take 2 characters each to finish splitting message. 
In this example, each part, including the last, has length 9. 
It can be shown it is not possible to split message into less than 14 parts.
```

 Example 2: 
 
```
Input:
 message = "short message", limit = 15

Output:
 ["short mess<1/2>","age<2/2>"]

Explanation:

Under the given constraints, the string can be split into two parts: 
- The first part comprises of the first 10 characters, and has a length 15.
- The next part comprises of the last 3 characters, and has a length 8.
```

 Constraints: 

 1 <= message.length <= 10 4 
 
 message consists only of lowercase English letters and ' ' . 
 
 1 <= limit <= 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: vector<string> splitMessage(string message,int limit){int n=message.size();auto digits=[](int x){int d=0;do{++d;x/=10;}while(x);return d;};long long sumDigits=0;for(int parts=1;parts<=n;++parts){sumDigits+=digits(parts);int dp=digits(parts);if(2*dp+3>=limit)continue;long long capacity=1LL*parts*(limit-3-dp)-sumDigits;if(capacity<n)continue;vector<string>ans;int pos=0;for(int i=1;i<=parts;++i){string suffix="<"+to_string(i)+"/"+to_string(parts)+">";int take=min((int)message.size()-pos,limit-(int)suffix.size());if(take<=0)break;ans.push_back(message.substr(pos,take)+suffix);pos+=take;}if(pos==n&&(int)ans.size()==parts)return ans;}return {};} };
```


## 2490. Circular Sentence

**Problem:** https://leetcode.com/problems/circular-sentence/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Checks the first/last characters and scans spaces for adjacent word-boundary matches.

### Problem description

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 

 For example, "Hello World" , "HELLO" , "hello world hello world" are all sentences. 

 Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different. 
 
 A sentence is circular if: 

 The last character of each word in the sentence is equal to the first character of its next word. 
 
 The last character of the last word is equal to the first character of the first word. 

 For example, "leetcode exercises sound delightful" , "eetcode" , "leetcode eats soul" are all circular sentences. However, "Leetcode is cool" , "happy Leetcode" , "Leetcode" and "I like Leetcode" are not circular sentences. 
 
 Given a string sentence , return true if it is circular . Otherwise, return false . 

 Example 1: 
 
```
Input:
 sentence = "leetcode exercises sound delightful"

Output:
 true

Explanation:
 The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
- leetcod
e
's last character is equal to 
e
xercises's first character.
- exercise
s
's last character is equal to 
s
ound's first character.
- soun
d
's last character is equal to 
d
elightful's first character.
- delightfu
l
's last character is equal to 
l
eetcode's first character.
The sentence is circular.
```

 Example 2: 
 
```
Input:
 sentence = "eetcode"

Output:
 true

Explanation:
 The words in sentence are ["eetcode"].
- eetcod
e
's last character is equal to 
e
etcode's first character.
The sentence is circular.
```

 Example 3: 
 
```
Input:
 sentence = "Leetcode is cool"

Output:
 false

Explanation:
 The words in sentence are ["Leetcode", "is", "cool"].
- Leetcod
e
's last character is 
not
 equal to 
i
s's first character.
The sentence is 
not
 circular.
```

 Constraints: 

 1 <= sentence.length <= 500 
 
 sentence consist of only lowercase and uppercase English letters and spaces. 
 
 The words in sentence are separated by a single space. 
 
 There are no leading or trailing spaces.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool isCircularSentence(string sentence){if(sentence.front()!=sentence.back())return false;for(int i=0;i<(int)sentence.size();i++)if(sentence[i]==' '&&sentence[i-1]!=sentence[i+1])return false;return true;}};
```


## 2496. Maximum Value of a String in an Array

**Problem:** https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(L)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Scans each string to test whether it contains only digits; stoi processes numeric strings once. L is total input characters.

### Problem description

The value of an alphanumeric string can be defined as: 

 The numeric representation of the string in base 10 , if it comprises of digits only . 
 
 The length of the string, otherwise. 

 Given an array strs of alphanumeric strings, return the maximum value of any string in strs . 

 Example 1: 
 
```
Input:
 strs = ["alic3","bob","3","4","00000"]

Output:
 5

Explanation:
 
- "alic3" consists of both letters and digits, so its value is its length, i.e. 5.
- "bob" consists only of letters, so its value is also its length, i.e. 3.
- "3" consists only of digits, so its value is its numeric equivalent, i.e. 3.
- "4" also consists only of digits, so its value is 4.
- "00000" consists only of digits, so its value is 0.
Hence, the maximum value is 5, of "alic3".
```

 Example 2: 
 
```
Input:
 strs = ["1","01","001","0001"]

Output:
 1

Explanation:
 
Each string in the array has value 1. Hence, we return 1.
```

 Constraints: 

 1 <= strs.length <= 100 
 
 1 <= strs[i].length <= 9 
 
 strs[i] consists of only lowercase English letters and digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int maximumValue(vector<string>& strs){int ans=0;for(auto&s:strs){bool digits=all_of(s.begin(),s.end(),[](char c){return isdigit(c);});ans=max(ans,digits?stoi(s):(int)s.size());}return ans;}};
```


## 2515. Shortest Distance to Target String in a Circular Array

**Problem:** https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + L)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Scans n words; each equality comparison can inspect up to its length, giving L total inspected characters in the worst case.

### Problem description

You are given a 0-indexed circular string array words and a string target . A circular array means that the array's end connects to the array's beginning. 

 Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n] , where n is the length of words . 

 Starting from startIndex , you can move to either the next word or the previous word with 1 step at a time. 
 
 Return the shortest distance needed to reach the string target . If the string target does not exist in words , return -1 . 

 Example 1: 
 
```
Input:
 words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1

Output:
 1

Explanation:
 We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.
```

 Example 2: 
 
```
Input:
 words = ["a","b","leetcode"], target = "leetcode", startIndex = 0

Output:
 1

Explanation:
 We start from index 0 and can reach "leetcode" by
- moving 2 units to the right to reach index 2.
- moving 1 unit to the left to reach index 2.
The shortest distance to reach "leetcode" is 1.
```

 Example 3: 
 
```
Input:
 words = ["i","eat","leetcode"], target = "ate", startIndex = 0

Output:
 -1

Explanation:
 Since "ate" does not exist in 
words
, we return -1.
```

 Constraints: 

 1 <= words.length <= 100 
 
 1 <= words[i].length <= 100 
 
 words[i] and target consist of only lowercase English letters. 
 
 0 <= startIndex < words.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int closestTarget(vector<string>& words, string target, int startIndex) {
        int n = words.size(), ans = n + 1;
        for (int i = 0; i < n; ++i) {
            if (words[i] != target) continue;
            int diff = abs(i - startIndex);
            ans = min(ans, min(diff, n - diff));
        }
        return ans == n + 1 ? -1 : ans;
    }
};
```


## 2546. Apply Bitwise Operations to Make Strings Equal

**Problem:** https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Bit Manipulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Bit Manipulation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Two find calls each scan at most n characters to detect whether a one exists.

### Problem description

You are given two 0-indexed binary strings s and target of the same length n . You can do the following operation on s any number of times: 

 Choose two different indices i and j where 0 <= i, j < n . 
 
 Simultaneously, replace s[i] with ( s[i] OR s[j] ) and s[j] with ( s[i] XOR s[j] ). 

 For example, if s = "0110" , you can choose i = 0 and j = 2 , then simultaneously replace s[0] with ( s[0] OR s[2] = 0 OR 1 = 1 ), and s[2] with ( s[0] XOR s[2] = 0 XOR 1 = 1 ), so we will have s = "1110" . 
 
 Return true if you can make the string s equal to target , or false otherwise . 

 Example 1: 
 
```
Input:
 s = "1010", target = "0110"

Output:
 true

Explanation:
 We can do the following operations:
- Choose i = 2 and j = 0. We have now s = "
0
0
1
0".
- Choose i = 2 and j = 1. We have now s = "0
11
0".
Since we can make s equal to target, we return true.
```

 Example 2: 
 
```
Input:
 s = "11", target = "00"

Output:
 false

Explanation:
 It is not possible to make s equal to target with any number of operations.
```

 Constraints: 

 n == s.length == target.length 
 
 2 <= n <= 10 5 
 
 s and target consist of only the digits 0 and 1 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 bool makeStringsEqual(string s,string target){
  return (s.find('1')!=string::npos)==(target.find('1')!=string::npos);
 }
};
```


## 2575. Find the Divisibility Array of a String

**Problem:** https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Processes each digit once, maintaining a rolling remainder and appending one output entry per digit.

### Problem description

You are given a 0-indexed string word of length n  consisting of digits, and a positive integer  m . 
 
 The divisibility array div of word is an integer array of length n such that: 

 div[i] = 1 if the  numeric value  of  word[0,...,i] is divisible by m , or 
 
 div[i] = 0 otherwise. 

 Return the divisibility array of word . 

 Example 1: 
 
```
Input:
 word = "998244353", m = 3

Output:
 [1,1,0,0,0,1,1,0,0]

Explanation:
 There are only 4 prefixes that are divisible by 3: "9", "99", "998244", and "9982443".
```

 Example 2: 
 
```
Input:
 word = "1010", m = 10

Output:
 [0,1,0,1]

Explanation:
 There are only 2 prefixes that are divisible by 10: "10", and "1010".
```

 Constraints: 

 1 <= n <= 10 5 
 
 word.length == n 
 
 word consists of digits from 0  to 9 
 
 1 <= m <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int> divisibilityArray(string word,int m){long long rem=0;vector<int> ans;for(char c:word){rem=(rem*10+c-'0')%m;ans.push_back(rem==0);}return ans;}};
```


## 2609. Find the Longest Balanced Substring of a Binary String

**Problem:** https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Counts each consecutive zero run followed by a one run; the index only moves forward.

### Problem description

You are given a binary string s consisting only of zeroes and ones. 
 
 A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring. 
 
 Return the length of the longest balanced substring of s . 
 
 A substring is a contiguous sequence of characters within a string. 

 Example 1: 
 
```
Input:
 s = "01000111"

Output:
 6

Explanation:
 The longest balanced substring is "000111", which has length 6.
```

 Example 2: 
 
```
Input:
 s = "00111"

Output:
 4

Explanation:
 The longest balanced substring is "0011", which has length 4.
```

 Example 3: 
 
```
Input:
 s = "111"

Output:
 0

Explanation:
 There is no balanced substring except the empty substring, so the answer is 0.
```

 Constraints: 

 1 <= s.length <= 50 
 
 '0' <= s[i] <= '1'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 int findTheLongestBalancedSubstring(string s) {
  int ans=0,prev=0,i=0,n=s.size();
  while(i<n){
   int z=0,o=0;
   while(i<n && s[i]=='0'){++z;++i;}
   while(i<n && s[i]=='1'){++o;++i;}
   ans=max(ans,2*min(z,o));
  }
  return ans;
 }
};
```


## 2678. Number of Senior Citizens

**Problem:** https://leetcode.com/problems/number-of-senior-citizens/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Visits each record and reads two fixed-position age digits; n is the number of records.

### Problem description

You are given a 0-indexed array of strings details . Each element of details provides information about a given passenger compressed into a string of length 15 . The system is such that: 

 The first ten characters consist of the phone number of passengers. 
 
 The next character denotes the gender of the person. 
 
 The following two characters are used to indicate the age of the person. 
 
 The last two characters determine the seat allotted to that person. 

 Return the number of passengers who are strictly more than 60 years old . 

 Example 1: 
 
```
Input:
 details = ["7868190130M7522","5303914400F9211","9273338290F4010"]

Output:
 2

Explanation:
 The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. Thus, there are 2 people who are over 60 years old.
```

 Example 2: 
 
```
Input:
 details = ["1313579440F2036","2921522980M5644"]

Output:
 0

Explanation:
 None of the passengers are older than 60.
```

 Constraints: 

 1 <= details.length <= 100 
 
 details[i].length == 15 
 
 details[i] consists of digits from '0' to '9'. 
 
 details[i][10] is either 'M' or 'F' or 'O'. 
 
 The phone numbers and seat numbers of the passengers are distinct.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int countSeniors(vector<string>&details){int ans=0;for(const auto&s:details)if((s[11]-'0')*10+s[12]-'0'>60)ans++;return ans;}};
```


## 2696. Minimum String Length After Removing Substrings

**Problem:** https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Stack, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each character is pushed at most once and popped at most once from the auxiliary string stack.

### Problem description

You are given a string s consisting only of uppercase English letters. 
 
 You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s . 
 
 Return the minimum possible length of the resulting string that you can obtain . 
 
 Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings. 

 Example 1: 
 
```
Input:
 s = "ABFCACDB"

Output:
 2

Explanation:
 We can do the following operations:
- Remove the substring "
AB
FCACDB", so s = "FCACDB".
- Remove the substring "FCA
CD
B", so s = "FCAB".
- Remove the substring "FC
AB
", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.
```

 Example 2: 
 
```
Input:
 s = "ACBBD"

Output:
 5

Explanation:
 We cannot do any operations on the string so the length remains the same.
```

 Constraints: 

 1 <= s.length <= 100 
 
 s  consists only of uppercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int minLength(string s){string st;for(char c:s){if(!st.empty()&&((st.back()=='A'&&c=='B')||(st.back()=='C'&&c=='D')))st.pop_back();else st.push_back(c);}return st.size();}};
```


## 2710. Remove Trailing Zeros From a String

**Problem:** https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Removes trailing zeros in place from the by-value string; the input parameter itself occupies O(n) space.

### Problem description

Given a positive integer num represented as a string, return the integer num without trailing zeros as a string . 

 Example 1: 
 
```
Input:
 num = "51230100"

Output:
 "512301"

Explanation:
 Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".
```

 Example 2: 
 
```
Input:
 num = "123"

Output:
 "123"

Explanation:
 Integer "123" has no trailing zeros, we return integer "123".
```

 Constraints: 

 1 <= num.length <= 1000 
 
 num consists of only digits. 
 
 num doesn't have any leading zeros.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string removeTrailingZeros(string num){while(!num.empty()&&num.back()=='0')num.pop_back();return num;}};
```


## 2785. Sort Vowels in a String

**Problem:** https://leetcode.com/problems/sort-vowels-in-a-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Sorting

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Sorting / Divide and Conquer

**Data structures (inferred):** Sorted array, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + v log v)

**Space complexity:** O(v)

**Complexity reasoning:** Collects v vowels, sorts them, and scans the input again to place sorted vowels.

### Problem description

Given a 0-indexed string s , permute s to get a new string t such that: 

 All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i] . 
 
 The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i , j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j] . 

 Return the resulting string . 
 
 The vowels are 'a' , 'e' , 'i' , 'o' , and 'u' , and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels. 

 Example 1: 
 
```
Input:
 s = "lEetcOde"

Output:
 "lEOtcede"

Explanation:
 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
```

 Example 2: 
 
```
Input:
 s = "lYmpH"

Output:
 "lYmpH"

Explanation:
 There are no vowels in s (all characters in s are consonants), so we return "lYmpH".
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists only of letters of the English alphabet in uppercase and lowercase .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string sortVowels(string s){string v;auto isV=[](char c){return string("AEIOUaeiou").find(c)!=string::npos;};for(char c:s)if(isV(c))v+=c;sort(v.begin(),v.end());int j=0;for(char &c:s)if(isV(c))c=v[j++];return s;}};
```


## 2788. Split Strings by Separator

**Problem:** https://leetcode.com/problems/split-strings-by-separator/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(L)

**Space complexity:** O(L)

**Complexity reasoning:** Scans all characters and accumulates nonempty tokens in the output and a temporary token string.

### Problem description

Given an array of strings words and a character separator , split each string in words by separator . 
 
 Return an array of strings containing the new strings formed after the splits, excluding empty strings . 
 
 Notes 

 separator is used to determine where the split should occur, but it is not included as part of the resulting strings. 
 
 A split may result in more than two strings. 
 
 The resulting strings must maintain the same order as they were initially given. 

 Example 1: 
 
```
Input:
 words = ["one.two.three","four.five","six"], separator = "."

Output:
 ["one","two","three","four","five","six"]

Explanation: 
In this example we split as follows:

"one.two.three" splits into "one", "two", "three"
"four.five" splits into "four", "five"
"six" splits into "six" 

Hence, the resulting array is ["one","two","three","four","five","six"].
```

 Example 2: 
 
```
Input:
 words = ["$easy$","$problem$"], separator = "$"

Output:
 ["easy","problem"]

Explanation:
 In this example we split as follows: 

"$easy$" splits into "easy" (excluding empty strings)
"$problem$" splits into "problem" (excluding empty strings)

Hence, the resulting array is ["easy","problem"].
```

 Example 3: 
 
```
Input:
 words = ["|||"], separator = "|"

Output:
 []

Explanation:
 In this example the resulting split of "|||" will contain only empty strings, so we return an empty array [].
```

 Constraints: 

 1 <= words.length <= 100 
 
 1 <= words[i].length <= 20 
 
 characters in words[i] are either lowercase English letters or characters from the string ".,|$#@" (excluding the quotes) 
 
 separator is a character from the string ".,|$#@" (excluding the quotes)

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<string> splitWordsBySeparator(vector<string>& words,char separator){vector<string> ans;for(const string &w:words){string cur;for(char c:w){if(c==separator){if(!cur.empty())ans.push_back(cur);cur.clear();}else cur+=c;}if(!cur.empty())ans.push_back(cur);}return ans;}};
```


## 2802. Find The K-th Lucky Number

**Problem:** https://leetcode.com/problems/find-the-k-th-lucky-number/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Math, String, Bit Manipulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Bit Manipulation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(log k)

**Space complexity:** O(log k)

**Complexity reasoning:** Repeatedly shifts k+1 right, appending one symbol per binary digit, then reverses the result.

### Problem description

We know that 4 and 7 are lucky digits. Also, a number is called lucky  if it contains only lucky digits. 
 
 You are given an integer k , return the k th  lucky number represented as a string . 

 Example 1: 
 
```
Input:
 k = 4

Output:
 "47"

Explanation:
 The first lucky number is 4, the second one is 7, the third one is 44 and the fourth one is 47.
```

 Example 2: 
 
```
Input:
 k = 10

Output:
 "477"

Explanation:
 Here are lucky numbers sorted in increasing order:
4, 7, 44, 47, 74, 77, 444, 447, 474, 477. So the 10
th
 lucky number is 477.
```

 Example 3: 
 
```
Input:
 k = 1000

Output:
 "777747447"

Explanation:
 It can be shown that the 1000
th
 lucky number is 777747447.
```

 Constraints: 

 1 <= k <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string kthLuckyNumber(int k) {
        long long value = (long long)k + 1;
        string answer;
        while (value > 1) {
            answer.push_back((value & 1) ? '7' : '4');
            value >>= 1;
        }
        reverse(answer.begin(), answer.end());
        return answer;
    }
};
```


## 2810. Faulty Keyboard

**Problem:** https://leetcode.com/problems/faulty-keyboard/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(n)

**Complexity reasoning:** Every i reverses the entire accumulated string, potentially taking linear time for each of n characters.

### Problem description

Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written. Typing other characters works as expected. 
 
 You are given a 0-indexed string s , and you type each character of s using your faulty keyboard. 
 
 Return the final string that will be present on your laptop screen. 

 Example 1: 
 
```
Input:
 s = "string"

Output:
 "rtsng"

Explanation:
 
After typing first character, the text on the screen is "s".
After the second character, the text is "st". 
After the third character, the text is "str".
Since the fourth character is an 'i', the text gets reversed and becomes "rts".
After the fifth character, the text is "rtsn". 
After the sixth character, the text is "rtsng". 
Therefore, we return "rtsng".
```

 Example 2: 
 
```
Input:
 s = "poiinter"

Output:
 "ponter"

Explanation:
 
After the first character, the text on the screen is "p".
After the second character, the text is "po". 
Since the third character you type is an 'i', the text gets reversed and becomes "op". 
Since the fourth character you type is an 'i', the text gets reversed and becomes "po".
After the fifth character, the text is "pon".
After the sixth character, the text is "pont". 
After the seventh character, the text is "ponte". 
After the eighth character, the text is "ponter". 
Therefore, we return "ponter".
```

 Constraints: 

 1 <= s.length <= 100 
 
 s consists of lowercase English letters. 
 
 s[0] != 'i'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string finalString(string s){string ans;for(char c:s){if(c=='i')reverse(ans.begin(),ans.end());else ans+=c;}return ans;}};
```


## 2828. Check if a String Is an Acronym of Words

**Problem:** https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Checks lengths and compares one initial character per word.

### Problem description

Given an array of strings words and a string s , determine if s is an acronym of words. 
 
 The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order . For example, "ab" can be formed from ["apple", "banana"] , but it can't be formed from ["bear", "aardvark"] . 
 
 Return true if s is an acronym of words , and false otherwise. 

 Example 1: 
 
```
Input:
 words = ["alice","bob","charlie"], s = "abc"

Output:
 true

Explanation:
 The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym.
```

 Example 2: 
 
```
Input:
 words = ["an","apple"], s = "a"

Output:
 false

Explanation:
 The first character in the words "an" and "apple" are 'a' and 'a', respectively. 
The acronym formed by concatenating these characters is "aa". 
Hence, s = "a" is not the acronym.
```

 Example 3: 
 
```
Input:
 words = ["never","gonna","give","up","on","you"], s = "ngguoy"

Output:
 true

Explanation: 
By concatenating the first character of the words in the array, we get the string "ngguoy". 
Hence, s = "ngguoy" is the acronym.
```

 Constraints: 

 1 <= words.length <= 100 
 
 1 <= words[i].length <= 10 
 
 1 <= s.length <= 100 
 
 words[i] and s consist of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:bool isAcronym(vector<string>& words,string s){if(words.size()!=s.size())return false;for(int i=0;i<(int)s.size();++i)if(words[i][0]!=s[i])return false;return true;}};
```


## 2839. Check if Strings Can be Made Equal With Operations I

**Problem:** https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Sorts two fixed pairs of positions in each four-character string and compares the results.

### Problem description

You are given two strings s1 and s2 , both of length 4 , consisting of lowercase English letters. 
 
 You can apply the following operation on any of the two strings any number of times: 

 Choose any two indices i and j such that j - i = 2 , then swap the two characters at those indices in the string. 

 Return true if you can make the strings s1 and s2 equal, and false otherwise . 

 Example 1: 
 
```
Input:
 s1 = "abcd", s2 = "cdab"

Output:
 true

Explanation:
 We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
- Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.
```

 Example 2: 
 
```
Input:
 s1 = "abcd", s2 = "dacb"

Output:
 false

Explanation:
 It is not possible to make the two strings equal.
```

 Constraints: 

 s1.length == s2.length == 4 
 
 s1 and s2 consist only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {public:bool canBeEqual(string s1,string s2){if(s1[0]>s1[2])swap(s1[0],s1[2]);if(s1[1]>s1[3])swap(s1[1],s1[3]);if(s2[0]>s2[2])swap(s2[0],s2[2]);if(s2[1]>s2[3])swap(s2[1],s2[3]);return s1==s2;}};
```


## 2914. Minimum Number of Changes to Make Binary String Beautiful

**Problem:** https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Compares each adjacent pair once.

### Problem description

You are given a 0-indexed binary string s having an even length. 
 
 A string is beautiful if it's possible to partition it into one or more substrings such that: 

 Each substring has an even length . 
 
 Each substring contains only 1 's or only 0 's. 

 You can change any character in s to 0 or 1 . 
 
 Return the minimum number of changes required to make the string s beautiful . 

 Example 1: 
 
```
Input:
 s = "1001"

Output:
 2

Explanation:
 We change s[1] to 1 and s[3] to 0 to get string "1100".
It can be seen that the string "1100" is beautiful because we can partition it into "11|00".
It can be proven that 2 is the minimum number of changes needed to make the string beautiful.
```

 Example 2: 
 
```
Input:
 s = "10"

Output:
 1

Explanation:
 We change s[1] to 1 to get string "11".
It can be seen that the string "11" is beautiful because we can partition it into "11".
It can be proven that 1 is the minimum number of changes needed to make the string beautiful.
```

 Example 3: 
 
```
Input:
 s = "0000"

Output:
 0

Explanation:
 We don't need to make any changes as the string "0000" is beautiful already.
```

 Constraints: 

 2 <= s.length <= 10 5 
 
 s has an even length. 
 
 s[i] is either '0' or '1' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int minChanges(string s) {int ans=0;for(int i=0;i<(int)s.size();i+=2)ans+=s[i]!=s[i+1];return ans;} };
```


## 2937. Make Three Strings Equal

**Problem:** https://leetcode.com/problems/make-three-strings-equal/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(min(a,b,c))

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Scans the common prefix of the three strings and computes the number of deletions.

### Problem description

You are given three strings: s1 , s2 , and s3 . In one operation you can choose one of these strings and delete its rightmost character. Note that you cannot completely empty a string. 
 
 Return the minimum number of operations required to make the strings equal . If it is impossible to make them equal, return -1 . 

 Example 1: 

 Input: s1 = "abc", s2 = "abb", s3 = "ab" 
 
 Output: 2 
 
 Explanation:  Deleting the rightmost character from both s1 and s2 will result in three equal strings. 

 Example 2: 

 Input: s1 = "dac", s2 = "bac", s3 = "cac" 
 
 Output: -1 
 
 Explanation: Since the first letters of s1 and s2 differ, they cannot be made equal. 

 Constraints: 

 1 <= s1.length, s2.length, s3.length <= 100 
 
 s1 , s2 and s3 consist only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution{public:int findMinimumOperations(string s1,string s2,string s3){int n=min(s1.size(),min(s2.size(),s3.size())),i=0;while(i<n&&s1[i]==s2[i]&&s2[i]==s3[i])i++;return i==0?-1:(int)(s1.size()+s2.size()+s3.size()-3*i);}};
```


## 2942. Find Words Containing Character

**Problem:** https://leetcode.com/problems/find-words-containing-character/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(L)

**Space complexity:** O(n) output

**Complexity reasoning:** Searches each word for x; L is total word length, and up to n indices are returned.

### Problem description

You are given a 0-indexed array of strings words and a character x . 
 
 Return an array of indices representing the words that contain the character x . 
 
 Note that the returned array may be in any order. 

 Example 1: 
 
```
Input:
 words = ["leet","code"], x = "e"

Output:
 [0,1]

Explanation:
 "e" occurs in both words: "l
ee
t", and "cod
e
". Hence, we return indices 0 and 1.
```

 Example 2: 
 
```
Input:
 words = ["abc","bcd","aaaa","cbc"], x = "a"

Output:
 [0,2]

Explanation:
 "a" occurs in "
a
bc", and "
aaaa
". Hence, we return indices 0 and 2.
```

 Example 3: 
 
```
Input:
 words = ["abc","bcd","aaaa","cbc"], x = "z"

Output:
 []

Explanation:
 "z" does not occur in any of the words. Hence, we return an empty array.
```

 Constraints: 

 1 <= words.length <= 50 
 
 1 <= words[i].length <= 50 
 
 x is a lowercase English letter. 
 
 words[i] consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution{public:vector<int> findWordsContaining(vector<string>& words,char x){vector<int> ans;for(int i=0;i<(int)words.size();i++)if(words[i].find(x)!=string::npos)ans.push_back(i);return ans;}};
```


## 3019. Number of Changing Keys

**Problem:** https://leetcode.com/problems/number-of-changing-keys/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Compares adjacent characters after converting both to lowercase.

### Problem description

You are given a 0-indexed string s typed by a user. Changing a key is defined as using a key different from the last used key. For example, s = "ab" has a change of a key while s = "bBBb" does not have any. 
 
 Return the number of times the user had to change the key. 
 
 Note: Modifiers like shift or caps lock won't be counted in changing the key that is if a user typed the letter 'a' and then the letter 'A' then it will not be considered as a changing of key. 

 Example 1: 
 
```
Input:
 s = "aAbBcC"

Output:
 2

Explanation:
 
From s[0] = 'a' to s[1] = 'A', there is no change of key as caps lock or shift is not counted.
From s[1] = 'A' to s[2] = 'b', there is a change of key.
From s[2] = 'b' to s[3] = 'B', there is no change of key as caps lock or shift is not counted.
From s[3] = 'B' to s[4] = 'c', there is a change of key.
From s[4] = 'c' to s[5] = 'C', there is no change of key as caps lock or shift is not counted.
```

 Example 2: 
 
```
Input:
 s = "AaAaAaaA"

Output:
 0

Explanation:
 There is no change of key since only the letters 'a' and 'A' are
 pressed which does not require change of key.
```

 Constraints: 

 1 <= s.length <= 100 
 
 s consists of only upper case and lower case English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int countKeyChanges(string s){int ans=0;for(int i=1;i<(int)s.size();i++)ans+=tolower(s[i])!=tolower(s[i-1]);return ans;}};
```


## 3110. Score of a String

**Problem:** https://leetcode.com/problems/score-of-a-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Sums absolute differences of each adjacent character pair.

### Problem description

You are given a string s . The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters. 
 
 Return the score of s . 

 Example 1: 

 Input: s = "hello" 
 
 Output: 13 
 
 Explanation: 
 
 The ASCII values of the characters in s are: 'h' = 104 , 'e' = 101 , 'l' = 108 , 'o' = 111 . So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13 . 

 Example 2: 

 Input: s = "zaz" 
 
 Output: 50 
 
 Explanation: 
 
 The ASCII values of the characters in s are: 'z' = 122 , 'a' = 97 . So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50 . 

 Constraints: 

 2 <= s.length <= 100 
 
 s consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int scoreOfString(string s){int ans=0;for(int i=1;i<(int)s.size();i++)ans+=abs(s[i]-s[i-1]);return ans;}};
```


## 3114. Latest Time You Can Obtain After Replacing Characters

**Problem:** https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Enumeration

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Fills at most four fixed positions in the five-character time string.

### Problem description

You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?" . 
 
 12-hour times are formatted as "HH:MM" , where HH is between 00 and 11 , and MM is between 00 and 59 . The earliest 12-hour time is 00:00 , and the latest is 11:59 . 
 
 You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible. 
 
 Return the resulting string . 

 Example 1: 

 Input: s = "1?:?4" 
 
 Output: "11:54" 
 
 Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54" . 

 Example 2: 

 Input: s = "0?:5?" 
 
 Output: "09:59" 
 
 Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59" . 

 Constraints: 

 s.length == 5 
 
 s[2] is equal to the character ":" . 
 
 All characters except s[2] are digits or "?" characters. 
 
 The input is generated such that there is at least one time between "00:00" and "11:59" that you can obtain after replacing the "?" characters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string findLatestTime(string s){if(s[0]=='?')s[0]=(s[1]=='?'||s[1]<='1')?'1':'0';if(s[1]=='?')s[1]=(s[0]=='1')?'1':'9';if(s[3]=='?')s[3]='5';if(s[4]=='?')s[4]='9';return s;}};
```


## 3136. Valid Word

**Problem:** https://leetcode.com/problems/valid-word/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Checks each character for alphanumeric validity and tracks whether vowels and consonants occur.

### Problem description

A word is considered valid if: 

 It contains a minimum of 3 characters. 
 
 It contains only digits (0-9), and English letters (uppercase and lowercase). 
 
 It includes at least one vowel . 
 
 It includes at least one consonant . 

 You are given a string word . 
 
 Return true if word is valid, otherwise, return false . 
 
 Notes: 

 'a' , 'e' , 'i' , 'o' , 'u' , and their uppercases are vowels . 
 
 A consonant is an English letter that is not a vowel. 

 Example 1: 

 Input: word = "234Adas" 
 
 Output: true 
 
 Explanation: 
 
 This word satisfies the conditions. 

 Example 2: 

 Input: word = "b3" 
 
 Output: false 
 
 Explanation: 
 
 The length of this word is fewer than 3, and does not have a vowel. 

 Example 3: 

 Input: word = "a3$e" 
 
 Output: false 
 
 Explanation: 
 
 This word contains a '$' character and does not have a consonant. 

 Constraints: 

 1 <= word.length <= 20 
 
 word consists of English uppercase and lowercase letters, digits, '@' , '#' , and '$' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool isValid(string word){if(word.size()<3)return false;bool v=false,c=false;for(char ch:word){if(!isalnum((unsigned char)ch))return false;if(isalpha((unsigned char)ch)){char x=tolower(ch);if(string("aeiou").find(x)!=string::npos)v=true;else c=true;}}return v&&c;}};
```


## 3163. String Compression III

**Problem:** https://leetcode.com/problems/string-compression-iii/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each character belongs to one run of length at most nine, and each run contributes two output characters.

### Problem description

Given a string word , compress it using the following algorithm: 

 Begin with an empty string comp . While word is not empty, use the following operation:

 Remove a maximum length prefix of word made of a single character c repeating at most 9 times. 
 
 Append the length of the prefix followed by c to comp . 

 Return the string comp . 

 Example 1: 

 Input: word = "abcde" 
 
 Output: "1a1b1c1d1e" 
 
 Explanation: 
 
 Initially, comp = "" . Apply the operation 5 times, choosing "a" , "b" , "c" , "d" , and "e" as the prefix in each operation. 
 
 For each prefix, append "1" followed by the character to comp . 

 Example 2: 

 Input: word = "aaaaaaaaaaaaaabb" 
 
 Output: "9a5a2b" 
 
 Explanation: 
 
 Initially, comp = "" . Apply the operation 3 times, choosing "aaaaaaaaa" , "aaaaa" , and "bb" as the prefix in each operation. 

 For prefix "aaaaaaaaa" , append "9" followed by "a" to comp . 
 
 For prefix "aaaaa" , append "5" followed by "a" to comp . 
 
 For prefix "bb" , append "2" followed by "b" to comp . 

 Constraints: 

 1 <= word.length <= 2 * 10 5 
 
 word consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string compressedString(string word){string ans;for(int i=0;i<(int)word.size();){int j=i;while(j<(int)word.size()&&word[j]==word[i]&&j-i<9)++j;ans+=char('0'+j-i);ans+=word[i];i=j;}return ans;}};
```


## 3168. Minimum Number of Chairs in a Waiting Room

**Problem:** https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Tracks current occupancy and maximum occupancy in one scan.

### Problem description

You are given a string s . Simulate events at each second i : 

 If s[i] == 'E' , a person enters the waiting room and takes one of the chairs in it. 
 
 If s[i] == 'L' , a person leaves the waiting room, freeing up a chair. 

 Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty . 

 Example 1: 

 Input: s = "EEEEEEE" 
 
 Output: 7 
 
 Explanation: 
 
 After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed. 

 Example 2: 

 Input: s = "ELELEEL" 
 
 Output: 2 
 
 Explanation: 
 
 Let's consider that there are 2 chairs in the waiting room. The table below shows the state of the waiting room at each second. 

 Second 
 Event 
 People in the Waiting Room 
 Available Chairs 

 0 
 Enter 
 1 
 1 

 1 
 Leave 
 0 
 2 

 2 
 Enter 
 1 
 1 

 3 
 Leave 
 0 
 2 

 4 
 Enter 
 1 
 1 

 5 
 Enter 
 2 
 0 

 6 
 Leave 
 1 
 1 

 Example 3: 

 Input: s = "ELEELEELLL" 
 
 Output: 3 
 
 Explanation: 
 
 Let's consider that there are 3 chairs in the waiting room. The table below shows the state of the waiting room at each second. 

 Second 
 Event 
 People in the Waiting Room 
 Available Chairs 

 0 
 Enter 
 1 
 2 

 1 
 Leave 
 0 
 3 

 2 
 Enter 
 1 
 2 

 3 
 Enter 
 2 
 1 

 4 
 Leave 
 1 
 2 

 5 
 Enter 
 2 
 1 

 6 
 Enter 
 3 
 0 

 7 
 Leave 
 2 
 1 

 8 
 Leave 
 1 
 2 

 9 
 Leave 
 0 
 3 

 Constraints: 

 1 <= s.length <= 50 
 
 s consists only of the letters 'E' and 'L' . 
 
 s represents a valid sequence of entries and exits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int minimumChairs(string s){int cur=0,ans=0;for(char c:s){cur+=(c=='E'?1:-1);ans=max(ans,cur);}return ans;}};
```


## 3174. Clear Digits

**Problem:** https://leetcode.com/problems/clear-digits/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Stack, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Uses an output string as a stack; each letter is pushed once and removed at most once.

### Problem description

You are given a string s . 
 
 Your task is to remove all digits by doing this operation repeatedly: 

 Delete the first digit and the closest non-digit character to its left . 

 Return the resulting string after removing all digits. 
 
 Note that the operation cannot be performed on a digit that does not have any non-digit character to its left. 

 Example 1: 

 Input: s = "abc" 
 
 Output: "abc" 
 
 Explanation: 
 
 There is no digit in the string. 

 Example 2: 

 Input: s = "cb34" 
 
 Output: "" 
 
 Explanation: 
 
 First, we apply the operation on s[2] , and s becomes "c4" . 
 
 Then we apply the operation on s[1] , and s becomes "" . 

 Constraints: 

 1 <= s.length <= 100 
 
 s consists only of lowercase English letters and digits. 
 
 The input is generated such that it is possible to delete all digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string clearDigits(string s){string r;for(char c:s){if(isdigit(c)){if(!r.empty())r.pop_back();}else r+=c;}return r;}};
```


## 3210. Find the Encrypted String

**Problem:** https://leetcode.com/problems/find-the-encrypted-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Builds the rotated result from two substrings, copying n characters in total.

### Problem description

You are given a string s and an integer k . Encrypt the string using the following algorithm: 

 For each character c in s , replace c with the k th character after c in the string (in a cyclic manner). 

 Return the encrypted string . 

 Example 1: 

 Input: s = "dart", k = 3 
 
 Output: "tdar" 
 
 Explanation: 

 For i = 0 , the 3 rd character after 'd' is 't' . 
 
 For i = 1 , the 3 rd character after 'a' is 'd' . 
 
 For i = 2 , the 3 rd character after 'r' is 'a' . 
 
 For i = 3 , the 3 rd character after 't' is 'r' . 

 Example 2: 

 Input: s = "aaa", k = 1 
 
 Output: "aaa" 
 
 Explanation: 
 
 As all the characters are the same, the encrypted string will also be the same. 

 Constraints: 

 1 <= s.length <= 100 
 
 1 <= k <= 10 4 
 
 s consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string getEncryptedString(string s,int k){int n=s.size();k%=n;return s.substr(k)+s.substr(0,k);}};
```


## 3227. Vowels Game in a String

**Problem:** https://leetcode.com/problems/vowels-game-in-a-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String, Brainteaser, Game Theory

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Scans characters until a vowel is found; membership testing uses a constant-length literal.

### Problem description

Alice and Bob are playing a game on a string. 
 
 You are given a string s , Alice and Bob will take turns playing the following game where Alice starts first : 

 On Alice's turn, she has to remove any non-empty substring from s that contains an odd number of vowels. 
 
 On Bob's turn, he has to remove any non-empty substring from s that contains an even number of vowels. 

 The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play optimally . 
 
 Return true if Alice wins the game, and false otherwise. 
 
 The English vowels are: a , e , i , o , and u . 

 Example 1: 

 Input: s = "leetcoder" 
 
 Output: true 
 
 Explanation: 
Alice can win the game as follows: 

 Alice plays first, she can delete the underlined substring in s = " leetco der" which contains 3 vowels. The resulting string is s = "der" . 
 
 Bob plays second, he can delete the underlined substring in s = " d er" which contains 0 vowels. The resulting string is s = "er" . 
 
 Alice plays third, she can delete the whole string s = " er " which contains 1 vowel. 
 
 Bob plays fourth, since the string is empty, there is no valid play for Bob. So Alice wins the game. 

 Example 2: 

 Input: s = "bbcd" 
 
 Output: false 
 
 Explanation: 
There is no valid play for Alice in her first turn, so Alice loses the game. 

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: bool doesAliceWin(string s) { for(char c:s) if(string("aeiou").find(c)!=string::npos) return true; return false; } };
```


## 3234. Count the Number of Substrings With Dominant Ones

**Problem:** https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Enumeration

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n√n)

**Space complexity:** O(n)

**Complexity reasoning:** For each right endpoint, enumerates at most O(√n) possible zero counts and uses the stored zero positions for constant-time counting.

### Problem description

You are given a binary string s . 
 
 Return the number of substrings with dominant ones. 
 
 A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string. 

 Example 1: 

 Input: s = "00011" 
 
 Output: 5 
 
 Explanation: 
 
 The substrings with dominant ones are shown in the table below. 

 i 
 j 
 s[i..j] 
 Number of Zeros 
 Number of Ones 

 3 
 3 
 1 
 0 
 1 

 4 
 4 
 1 
 0 
 1 

 2 
 3 
 01 
 1 
 1 

 3 
 4 
 11 
 0 
 2 

 2 
 4 
 011 
 1 
 2 

 Example 2: 

 Input: s = "101101" 
 
 Output: 16 
 
 Explanation: 
 
 The substrings with non-dominant ones are shown in the table below. 
 
 Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones. 

 i 
 j 
 s[i..j] 
 Number of Zeros 
 Number of Ones 

 1 
 1 
 0 
 1 
 0 

 4 
 4 
 0 
 1 
 0 

 1 
 4 
 0110 
 2 
 2 

 0 
 4 
 10110 
 2 
 3 

 1 
 5 
 01101 
 2 
 3 

 Constraints: 

 1 <= s.length <= 4 * 10 4 
 
 s consists only of characters '0' and '1' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n=s.size();
        vector<int> zeros;
        zeros.push_back(-1);
        long long ans=0;
        int start=0;
        for (int r=0;r<n;++r) {
            if (s[r]=='0') zeros.push_back(r);
            int z=zeros.size()-1;
            ans+=r-zeros.back(); // zero-free substrings
            for (int count=1;count<=z && count*count+count<=r+1;++count) {
                int leftZero=zeros[z-count+1];
                int prevZero=zeros[z-count];
                int minLen=count*count+count;
                int leftLimit=r-minLen+1;
                int high=min(leftZero,leftLimit);
                if (high>prevZero) ans+=high-prevZero;
            }
        }
        return (int)ans;
    }
};
```


## 3248. Snake in Matrix

**Problem:** https://leetcode.com/problems/snake-in-matrix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(q)

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Processes q commands once, updating a single flattened position.

### Problem description

There is a snake in an n x n matrix grid and can move in four possible directions . Each cell in the grid is identified by the position: grid[i][j] = (i * n) + j . 
 
 The snake starts at cell 0 and follows a sequence of commands. 
 
 You are given an integer n representing the size of the grid and an array of strings commands where each command[i] is either "UP" , "RIGHT" , "DOWN" , and "LEFT" . It's guaranteed that the snake will remain within the grid boundaries throughout its movement. 
 
 Return the position of the final cell where the snake ends up after executing commands . 

 Example 1: 

 Input: n = 2, commands = ["RIGHT","DOWN"] 
 
 Output: 3 
 
 Explanation: 

 0 
 1 

 2 
 3 

 0 
 1 

 2 
 3 

 0 
 1 

 2 
 3 

 Example 2: 

 Input: n = 3, commands = ["DOWN","RIGHT","UP"] 
 
 Output: 1 
 
 Explanation: 

 0 
 1 
 2 

 3 
 4 
 5 

 6 
 7 
 8 

 0 
 1 
 2 

 3 
 4 
 5 

 6 
 7 
 8 

 0 
 1 
 2 

 3 
 4 
 5 

 6 
 7 
 8 

 0 
 1 
 2 

 3 
 4 
 5 

 6 
 7 
 8 

 Constraints: 

 2 <= n <= 10 
 
 1 <= commands.length <= 100 
 
 commands consists only of "UP" , "RIGHT" , "DOWN" , and "LEFT" . 
 
 The input is generated such the snake will not move outside of the boundaries.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int finalPositionOfSnake(int n,vector<string>& commands){int p=0;for(string &s:commands){if(s=="UP")p-=n;else if(s=="DOWN")p+=n;else if(s=="LEFT")--p;else ++p;}return p;} };
```


## 3271. Hash Divided String

**Problem:** https://leetcode.com/problems/hash-divided-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n/k) output

**Complexity reasoning:** Each of the n characters contributes once to a k-character block sum.

### Problem description

You are given a string s of length n and an integer k , where n is a multiple of k . Your task is to hash the string s into a new string called result , which has a length of n / k . 
 
 First, divide s into n / k substrings , each with a length of k . Then, initialize result as an empty string. 
 
 For each substring in order from the beginning: 

 The hash value of a character is the index of that characte r in the English alphabet (e.g., 'a' → 0 , 'b' → 1 , ..., 'z' → 25 ). 
 
 Calculate the sum of all the hash values of the characters in the substring. 
 
 Find the remainder of this sum when divided by 26, which is called hashedChar . 
 
 Identify the character in the English lowercase alphabet that corresponds to hashedChar . 
 
 Append that character to the end of result . 

 Return result . 

 Example 1: 

 Input: s = "abcd", k = 2 
 
 Output: "bf" 
 
 Explanation: 
 
 First substring: "ab" , 0 + 1 = 1 , 1 % 26 = 1 , result[0] = 'b' . 
 
 Second substring: "cd" , 2 + 3 = 5 , 5 % 26 = 5 , result[1] = 'f' . 

 Example 2: 

 Input: s = "mxz", k = 3 
 
 Output: "i" 
 
 Explanation: 
 
 The only substring: "mxz" , 12 + 23 + 25 = 60 , 60 % 26 = 8 , result[0] = 'i' . 

 Constraints: 

 1 <= k <= 100 
 
 k <= s.length <= 1000 
 
 s.length is divisible by k . 
 
 s consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: string stringHash(string s, int k) { string out; for(int i=0;i<(int)s.size();i+=k){int v=0;for(int j=i;j<i+k;++j)v+=s[j]-'a';out+=char('a'+v%26);}return out;} };
```


## 3274. Check if Two Chessboard Squares Have the Same Color

**Problem:** https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Compares the parity of two fixed-size chessboard coordinates.

### Problem description

You are given two strings, coordinate1 and coordinate2 , representing the coordinates of a square on an 8 x 8 chessboard. 
 
 Below is the chessboard for reference. 
 
 [Figure: https://assets.leetcode.com/uploads/2024/07/17/screenshot-2021-02-20-at-22159-pm.png] 
 
 Return true if these two squares have the same color and false otherwise. 
 
 The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), and the number second (indicating its row). 

 Example 1: 

 Input: coordinate1 = "a1", coordinate2 = "c3" 
 
 Output: true 
 
 Explanation: 
 
 Both squares are black. 

 Example 2: 

 Input: coordinate1 = "a1", coordinate2 = "h3" 
 
 Output: false 
 
 Explanation: 
 
 Square "a1" is black and "h3" is white. 

 Constraints: 

 coordinate1.length == coordinate2.length == 2 
 
 'a' <= coordinate1[0], coordinate2[0] <= 'h' 
 
 '1' <= coordinate1[1], coordinate2[1] <= '8'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: bool checkTwoChessboards(string a,string b){return ((a[0]-'a'+a[1]-'1')&1)==((b[0]-'a'+b[1]-'1')&1);} };
```


## 3280. Convert Date to Binary

**Problem:** https://leetcode.com/problems/convert-date-to-binary/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Parses three fixed-width date fields and converts bounded integers to binary.

### Problem description

You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format. 
 
 date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format. 
 
 Return the binary representation of date . 

 Example 1: 

 Input: date = "2080-02-29" 
 
 Output: "100000100000-10-11101" 
 
 Explanation: 
 
 100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively. 

 Example 2: 

 Input: date = "1900-01-01" 
 
 Output: "11101101100-1-1" 
 
 Explanation: 
 
 11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively. 

 Constraints: 

 date.length == 10 
 
 date[4] == date[7] == '-' , and all other date[i] 's are digits. 
 
 The input is generated such that date represents a valid Gregorian calendar date between Jan 1 st , 1900 and Dec 31 st , 2100 (both inclusive).

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { string bin(int x){string s;do{s+=char('0'+x%2);x/=2;}while(x);reverse(s.begin(),s.end());return s;}public:string convertDateToBinary(string date){return bin(stoi(date.substr(0,4)))+"-"+bin(stoi(date.substr(5,2)))+"-"+bin(stoi(date.substr(8,2)));} };
```


## 3303. Find the Occurrence of First Almost Equal Substring

**Problem:** https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

**Difficulty:** Hard | **Premium:** No

**Tags:** String, String Matching, Knuth–Morris–Pratt Algorithm

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + m)

**Space complexity:** O(n + m)

**Complexity reasoning:** Computes forward and reversed Z-arrays over pattern and text, then checks every alignment once.

### Problem description

You are given two strings s and pattern . 
 
 A string x is called almost equal to y if you can change at most one character in x to make it identical to y . 
 
 Return the smallest starting index of a substring in s that is almost equal to pattern . If no such index exists, return -1 . 
A substring is a contiguous non-empty sequence of characters within a string.

 Example 1: 

 Input: s = "abcdefg", pattern = "bcdffg" 
 
 Output: 1 
 
 Explanation: 
 
 The substring s[1..6] == "bcdefg" can be converted to "bcdffg" by changing s[4] to "f" . 

 Example 2: 

 Input: s = "ababbababa", pattern = "bacaba" 
 
 Output: 4 
 
 Explanation: 
 
 The substring s[4..9] == "bababa" can be converted to "bacaba" by changing s[6] to "c" . 

 Example 3: 

 Input: s = "abcd", pattern = "dba" 
 
 Output: -1 

 Example 4: 

 Input: s = "dde", pattern = "d" 
 
 Output: 0 

 Constraints: 

 1 <= pattern.length < s.length <= 10 5 
 
 s and pattern consist only of lowercase English letters. 

 Follow-up: Could you solve the problem if at most k consecutive characters can be changed?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { vector<int>zfunc(const string&s){int n=s.size();vector<int>z(n);for(int i=1,l=0,r=0;i<n;++i){if(i<=r)z[i]=min(r-i+1,z[i-l]);while(i+z[i]<n&&s[z[i]]==s[i+z[i]])++z[i];if(i+z[i]-1>r)l=i,r=i+z[i]-1;}return z;}public:int minStartingIndex(string s,string pattern){int n=s.size(),m=pattern.size();if(m>n)return -1;auto z=zfunc(pattern+'#'+s);string rs=s,rp=pattern;reverse(rs.begin(),rs.end());reverse(rp.begin(),rp.end());auto rev=zfunc(rp+'#'+rs);for(int i=0;i+m<=n;++i)if(z[m+1+i]+rev[m+1+n-(i+m)]>=m-1)return i;return -1;} };
```


## 3324. Find the Sequence of Strings Appeared on the Screen

**Problem:** https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(L + T)

**Space complexity:** O(T) output

**Complexity reasoning:** Builds each intermediate screen string; T is the total length of all emitted strings (at most 26 times the sum of target prefix lengths).

### Problem description

You are given a string target . 
 
 Alice is going to type target on her computer using a special keyboard that has only two keys: 

 Key 1 appends the character "a" to the string on the screen. 
 
 Key 2 changes the last character of the string on the screen to its next character in the English alphabet. For example, "c" changes to "d" and "z" changes to "a" . 

 Note that initially there is an empty string "" on the screen, so she can only press key 1. 
 
 Return a list of all strings that appear on the screen as Alice types target , in the order they appear, using the minimum key presses. 

 Example 1: 

 Input: target = "abc" 
 
 Output: ["a","aa","ab","aba","abb","abc"] 
 
 Explanation: 
 
 The sequence of key presses done by Alice are: 

 Press key 1, and the string on the screen becomes "a" . 
 
 Press key 1, and the string on the screen becomes "aa" . 
 
 Press key 2, and the string on the screen becomes "ab" . 
 
 Press key 1, and the string on the screen becomes "aba" . 
 
 Press key 2, and the string on the screen becomes "abb" . 
 
 Press key 2, and the string on the screen becomes "abc" . 

 Example 2: 

 Input: target = "he" 
 
 Output: ["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"] 

 Constraints: 

 1 <= target.length <= 400 
 
 target consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<string> stringSequence(string target){vector<string> ans;string cur;for(char c:target){cur+='a';ans.push_back(cur);while(cur.back()!=c){cur.back()++;ans.push_back(cur);}}return ans;}};
```


## 3330. Find the Original Typed String I

**Problem:** https://leetcode.com/problems/find-the-original-typed-string-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Counts adjacent equal characters in one pass.

### Problem description

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times. 
 
 Although Alice tried to focus on her typing, she is aware that she may still have done this at most once . 
 
 You are given a string word , which represents the final output displayed on Alice's screen. 
 
 Return the total number of possible original strings that Alice might have intended to type. 

 Example 1: 

 Input: word = "abbcccc" 
 
 Output: 5 
 
 Explanation: 
 
 The possible strings are: "abbcccc" , "abbccc" , "abbcc" , "abbc" , and "abcccc" . 

 Example 2: 

 Input: word = "abcd" 
 
 Output: 1 
 
 Explanation: 
 
 The only possible string is "abcd" . 

 Example 3: 

 Input: word = "aaaa" 
 
 Output: 4 

 Constraints: 

 1 <= word.length <= 100 
 
 word consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int possibleStringCount(string word){int ans=1;for(int i=1;i<(int)word.size();i++)if(word[i]==word[i-1])ans++;return ans;}};
```


## 3340. Check Balanced String

**Problem:** https://leetcode.com/problems/check-balanced-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Accumulates digit sums at alternating indices.

### Problem description

You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices. 
 
 Return true if num is balanced , otherwise return false . 

 Example 1: 

 Input: num = "1234" 
 
 Output: false 
 
 Explanation: 

 The sum of digits at even indices is 1 + 3 == 4 , and the sum of digits at odd indices is 2 + 4 == 6 . 
 
 Since 4 is not equal to 6, num is not balanced. 

 Example 2: 

 Input: num = "24123" 
 
 Output: true 
 
 Explanation: 

 The sum of digits at even indices is 2 + 1 + 3 == 6 , and the sum of digits at odd indices is 4 + 2 == 6 . 
 
 Since both are equal the num is balanced. 

 Constraints: 

 2 <= num.length <= 100 
 
 num consists of digits only

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool isBalanced(string num){int a=0,b=0;for(int i=0;i<(int)num.size();i++)(i%2?b:a)+=num[i]-'0';return a==b;}};
```


## 3407. Substring Matching Pattern

**Problem:** https://leetcode.com/problems/substring-matching-pattern/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, String Matching

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + m) average

**Space complexity:** O(m) auxiliary

**Complexity reasoning:** Splits the pattern around its wildcard and uses two substring searches; standard string::find has implementation-dependent worst-case behavior.

### Problem description

You are given a string s and a pattern string p , where p contains exactly one '*' character. 
 
 The '*' in p can be replaced with any sequence of zero or more characters. 
 
 Return true if p can be made a substring of s , and false otherwise. 

 Example 1: 

 Input: s = "leetcode", p = "ee*e" 
 
 Output: true 
 
 Explanation: 
 
 By replacing the '*' with "tcod" , the substring "eetcode" matches the pattern. 

 Example 2: 

 Input: s = "car", p = "c*v" 
 
 Output: false 
 
 Explanation: 
 
 There is no substring matching the pattern. 

 Example 3: 

 Input: s = "luck", p = "u*" 
 
 Output: true 
 
 Explanation: 
 
 The substrings "u" , "uc" , and "uck" match the pattern. 

 Constraints: 

 1 <= s.length <= 50 
 
 1 <= p.length <= 50 
 
 s contains only lowercase English letters. 
 
 p contains only lowercase English letters and exactly one '*'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool hasMatch(string s,string p){int pos=p.find('*');string a=p.substr(0,pos),b=p.substr(pos+1);size_t i=s.find(a);if(i==string::npos)return false;return s.find(b,i+a.size())!=string::npos;}};
```


## 3456. Find Special Substring of Length K

**Problem:** https://leetcode.com/problems/find-special-substring-of-length-k/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Scans maximal runs using two forward-moving indices.

### Problem description

You are given a string s and an integer k . 
 
 Determine if there exists a substring of length exactly k in s that satisfies the following conditions: 

 The substring consists of only one distinct character (e.g., "aaa" or "bbb" ). 
 
 If there is a character immediately before the substring, it must be different from the character in the substring. 
 
 If there is a character immediately after the substring, it must also be different from the character in the substring. 

 Return true if such a substring exists. Otherwise, return false . 

 Example 1: 

 Input: s = "aaabaaa", k = 3 
 
 Output: true 
 
 Explanation: 
 
 The substring s[4..6] == "aaa" satisfies the conditions. 

 It has a length of 3. 
 
 All characters are the same. 
 
 The character before "aaa" is 'b' , which is different from 'a' . 
 
 There is no character after "aaa" . 

 Example 2: 

 Input: s = "abc", k = 2 
 
 Output: false 
 
 Explanation: 
 
 There is no substring of length 2 that consists of one distinct character and satisfies the conditions. 

 Constraints: 

 1 <= k <= s.length <= 100 
 
 s consists of lowercase English letters only.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool hasSpecialSubstring(string s,int k){int n=s.size();for(int i=0,j;i<n;i=j){j=i+1;while(j<n&&s[j]==s[i])++j;if(j-i==k)return true;}return false;}};
```


## 3461. Check If Digits Are Equal in String After Operations I

**Problem:** https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String, Simulation, Combinatorics, Number Theory

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n^2)

**Space complexity:** O(n)

**Complexity reasoning:** Rebuilds a string of decreasing length in each round, totaling quadratic work.

### Problem description

You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits: 

 For each pair of consecutive digits in s , starting from the first digit, calculate a new digit as the sum of the two digits modulo 10. 
 
 Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed. 

 Return true if the final two digits in s are the same ; otherwise, return false . 

 Example 1: 

 Input: s = "3902" 
 
 Output: true 
 
 Explanation: 

 Initially, s = "3902" 
 
 First operation:

 (s[0] + s[1]) % 10 = (3 + 9) % 10 = 2 
 
 (s[1] + s[2]) % 10 = (9 + 0) % 10 = 9 
 
 (s[2] + s[3]) % 10 = (0 + 2) % 10 = 2 
 
 s becomes "292" 

 Second operation:

 (s[0] + s[1]) % 10 = (2 + 9) % 10 = 1 
 
 (s[1] + s[2]) % 10 = (9 + 2) % 10 = 1 
 
 s becomes "11" 

 Since the digits in "11" are the same, the output is true . 

 Example 2: 

 Input: s = "34789" 
 
 Output: false 
 
 Explanation: 

 Initially, s = "34789" . 
 
 After the first operation, s = "7157" . 
 
 After the second operation, s = "862" . 
 
 After the third operation, s = "48" . 
 
 Since '4' != '8' , the output is false . 

 Constraints: 

 3 <= s.length <= 100 
 
 s consists of only digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:bool hasSameDigits(string s){while(s.size()>2){string t;for(int i=1;i<(int)s.size();++i)t.push_back('0'+(s[i-1]-'0'+s[i]-'0')%10);s.swap(t);}return s[0]==s[1];}};
```


## 3463. Check If Digits Are Equal in String After Operations II

**Problem:** https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Math, String, Combinatorics, Number Theory

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log_5 n)

**Space complexity:** O(1)

**Complexity reasoning:** For each of n+1 binomial coefficients, Lucas decomposition examines O(log_5 n) base-5 digits.

### Problem description

You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits: 

 For each pair of consecutive digits in s , starting from the first digit, calculate a new digit as the sum of the two digits modulo 10. 
 
 Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed. 

 Return true if the final two digits in s are the same ; otherwise, return false . 

 Example 1: 

 Input: s = "3902" 
 
 Output: true 
 
 Explanation: 

 Initially, s = "3902" 
 
 First operation:

 (s[0] + s[1]) % 10 = (3 + 9) % 10 = 2 
 
 (s[1] + s[2]) % 10 = (9 + 0) % 10 = 9 
 
 (s[2] + s[3]) % 10 = (0 + 2) % 10 = 2 
 
 s becomes "292" 

 Second operation:

 (s[0] + s[1]) % 10 = (2 + 9) % 10 = 1 
 
 (s[1] + s[2]) % 10 = (9 + 2) % 10 = 1 
 
 s becomes "11" 

 Since the digits in "11" are the same, the output is true . 

 Example 2: 

 Input: s = "34789" 
 
 Output: false 
 
 Explanation: 

 Initially, s = "34789" . 
 
 After the first operation, s = "7157" . 
 
 After the second operation, s = "862" . 
 
 After the third operation, s = "48" . 
 
 Since '4' != '8' , the output is false . 

 Constraints: 

 3 <= s.length <= 10 5 
 
 s consists of only digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {int choose5(int n,int r){static int c[5][5]={{1},{1,1},{1,2,1},{1,3,3,1},{1,4,6,4,1}};int v=1;while(n||r){int a=n%5,b=r%5;if(b>a)return 0;v=v*c[a][b]%5;n/=5;r/=5;}return v;}
 public:bool hasSameDigits(string s){int n=s.size()-2,sum=0;for(int i=0;i<=n;++i){int c2=((i&n)==i);int c5=choose5(n,i);int c=(5*c2+6*c5)%10;sum=(sum+c*(s[i]-s[i+1]))%10;}return sum==0;}};
```


## 3498. Reverse Degree of a String

**Problem:** https://leetcode.com/problems/reverse-degree-of-a-string/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Accumulates one weighted contribution per character.

### Problem description

Given a string s , calculate its reverse degree . 
 
 The reverse degree is calculated as follows: 

 For each character, multiply its position in the reversed alphabet ( 'a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed) . 
 
 Sum these products for all characters in the string. 

 Return the reverse degree of s . 

 Example 1: 

 Input: s = "abc" 
 
 Output: 148 
 
 Explanation: 

 Letter 
 Index in Reversed Alphabet 
 Index in String 
 Product 

 'a' 
 26 
 1 
 26 

 'b' 
 25 
 2 
 50 

 'c' 
 24 
 3 
 72 

 The reversed degree is 26 + 50 + 72 = 148 . 

 Example 2: 

 Input: s = "zaza" 
 
 Output: 160 
 
 Explanation: 

 Letter 
 Index in Reversed Alphabet 
 Index in String 
 Product 

 'z' 
 1 
 1 
 1 

 'a' 
 26 
 2 
 52 

 'z' 
 1 
 3 
 3 

 'a' 
 26 
 4 
 104 

 The reverse degree is 1 + 52 + 3 + 104 = 160 . 

 Constraints: 

 1 <= s.length <= 1000 
 
 s contains only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int reverseDegree(string s){int ans=0;for(int i=0;i<(int)s.size();i++)ans+=(i+1)*('z'-s[i]+1);return ans;}};
```


## 3499. Maximize Active Section with Trade I

**Problem:** https://leetcode.com/problems/maximize-active-section-with-trade-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Enumeration

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Counts ones and builds run-length groups in linear time, then checks each eligible group.

### Problem description

You are given a binary string s of length n , where: 

 '1' represents an active section. 
 
 '0' represents an inactive section. 

 You can perform at most one trade to maximize the number of active sections in s . In a trade, you: 

 Convert a contiguous block of '1' s that is surrounded by '0' s to all '0' s. 
 
 Afterward, convert a contiguous block of '0' s that is surrounded by '1' s to all '1' s. 

 Return the maximum number of active sections in s after making the optimal trade. 
 
 Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1' . The augmented '1' s do not contribute to the final count. 

 Example 1: 

 Input: s = "01" 
 
 Output: 1 
 
 Explanation: 
 
 Because there is no block of '1' s surrounded by '0' s, no valid trade is possible. The maximum number of active sections is 1. 

 Example 2: 

 Input: s = "0100" 
 
 Output: 4 
 
 Explanation: 

 String "0100" → Augmented to "101001" . 
 
 Choose "0100" , convert "10 1 001" → "1 0000 1" → "1 1111 1" . 
 
 The final string without augmentation is "1111" . The maximum number of active sections is 4. 

 Example 3: 

 Input: s = "1000100" 
 
 Output: 7 
 
 Explanation: 

 String "1000100" → Augmented to "110001001" . 
 
 Choose "000100" , convert "11000 1 001" → "11 000000 1" → "11 111111 1" . 
 
 The final string without augmentation is "1111111" . The maximum number of active sections is 7. 

 Example 4: 

 Input: s = "01010" 
 
 Output: 4 
 
 Explanation: 

 String "01010" → Augmented to "1010101" . 
 
 Choose "010" , convert "10 1 0101" → "1 000 101" → "1 111 101" . 
 
 The final string without augmentation is "11110" . The maximum number of active sections is 4. 

 Constraints: 

 1 <= n == s.length <= 10 5 
 
 s[i] is either '0' or '1'

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int maxActiveSectionsAfterTrade(string s){int base=count(s.begin(),s.end(),'1'),gain=0;string t="1"+s+"1";vector<pair<char,int>>runs;for(char c:t){if(runs.empty()||runs.back().first!=c)runs.push_back({c,1});else runs.back().second++;}for(int i=1;i+1<(int)runs.size();i++)if(runs[i].first=='1'&&runs[i-1].first=='0'&&runs[i+1].first=='0')gain=max(gain,runs[i-1].second+runs[i+1].second);return base+gain;}};
```


## 3517. Smallest Palindromic Rearrangement I

**Problem:** https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Sorting, Counting Sort

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Sorting / Divide and Conquer

**Data structures (inferred):** Sorted array, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Counts letters and constructs two palindrome halves plus an optional middle character.

### Problem description

You are given a palindromic string s . 
 
 Return the lexicographically smallest palindromic permutation of s . 

 Example 1: 

 Input: s = "z" 
 
 Output: "z" 
 
 Explanation: 
 
 A string of only one character is already the lexicographically smallest palindrome. 

 Example 2: 

 Input: s = "babab" 
 
 Output: "abbba" 
 
 Explanation: 
 
 Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome. 

 Example 3: 

 Input: s = "daccad" 
 
 Output: "acddca" 
 
 Explanation: 
 
 Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome. 

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists of lowercase English letters. 
 
 s is guaranteed to be palindromic.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:string smallestPalindrome(string s){int f[26]={};for(char c:s)++f[c-'a'];string h,mid;for(int i=0;i<26;i++){h+=string(f[i]/2,char('a'+i));if(f[i]%2)mid=char('a'+i);}string r=h;reverse(r.begin(),r.end());return h+mid+r;}};
```


## 3561. Resulting String After Adjacent Removals

**Problem:** https://leetcode.com/problems/resulting-string-after-adjacent-removals/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Stack, String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Each character is pushed or removes one prior character from the string stack.

### Problem description

You are given a string s consisting of lowercase English letters. 
 
 You must repeatedly perform the following operation while the string s has at least two consecutive characters: 

 Remove the leftmost pair of adjacent characters in the string that are consecutive in the alphabet, in either order (e.g., 'a' and 'b' , or 'b' and 'a' ). 
 
 Shift the remaining characters to the left to fill the gap. 

 Return the resulting string after no more operations can be performed. 
 
 Note: Consider the alphabet as circular, thus 'a' and 'z' are consecutive. 

 Example 1: 

 Input: s = "abc" 
 
 Output: "c" 
 
 Explanation: 

 Remove "ab" from the string, leaving "c" as the remaining string. 
 
 No further operations are possible. Thus, the resulting string after all possible removals is "c" . 

 Example 2: 

 Input: s = "adcb" 
 
 Output: "" 
 
 Explanation: 

 Remove "dc" from the string, leaving "ab" as the remaining string. 
 
 Remove "ab" from the string, leaving "" as the remaining string. 
 
 No further operations are possible. Thus, the resulting string after all possible removals is "" . 

 Example 3: 

 Input: s = "zadb" 
 
 Output: "db" 
 
 Explanation: 

 Remove "za" from the string, leaving "db" as the remaining string. 
 
 No further operations are possible. Thus, the resulting string after all possible removals is "db" . 

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public:
 string resultingString(string s) {
  string st;
  for(char c:s){ if(!st.empty() && (abs(st.back()-c)==1 || abs(st.back()-c)==25)) st.pop_back(); else st+=c; }
  return st;
 }
};
```


## 3571. Find the Shortest Superstring II

**Problem:** https://leetcode.com/problems/find-the-shortest-superstring-ii/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O((a+b) * min(a,b)) worst case

**Space complexity:** O(a+b)

**Complexity reasoning:** Each merge checks containment and then compares suffix-prefix overlaps from longest to shortest; the returned strings occupy linear space.

### Problem description

You are given two strings, s1 and s2 . Return the shortest possible string that contains both s1 and s2 as substrings. If there are multiple valid answers, return any one of them. 
 
 A substring is a contiguous sequence of characters within a string. 

 Example 1: 

 Input: s1 = "aba", s2 = "bab" 
 
 Output: "abab" 
 
 Explanation: 
 
 "abab" is the shortest string that contains both "aba" and "bab" as substrings. 

 Example 2: 

 Input: s1 = "aa", s2 = "aaa" 
 
 Output: "aaa" 
 
 Explanation: 
 
 "aa" is already contained within "aaa" , so the shortest superstring is "aaa" . 

 Constraints: 

 1 <= s1.length <= 100 
 
 1 <= s2.length <= 100 
 
 s1 and s2 consist of lowercase English letters only.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    string merge(string a, string b) {
        if (a.find(b) != string::npos) {
            return a;
        }
        int limit = min(a.size(), b.size());
        for (int len = limit; len >= 0; --len) {
            if (a.compare(a.size() - len, len, b, 0, len) == 0) {
                return a + b.substr(len);
            }
        }
        return a + b;
    }
public:
    string shortestSuperstring(string a, string b) {
        string x = merge(a, b);
        string y = merge(b, a);
        if (x.size() != y.size()) {
            return x.size() < y.size() ? x : y;
        }
        return min(x, y);
    }
};
```


## 3582. Generate Tag for Video Caption

**Problem:** https://leetcode.com/problems/generate-tag-for-video-caption/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Tokenizes and normalizes each word once, building a capped output tag.

### Problem description

You are given a string caption representing the caption for a video. 
 
 The following actions must be performed in order to generate a valid tag for the video: 

 Combine all words in the string into a single camelCase string prefixed with '#' . A camelCase string is one where the first letter of all words except the first one is capitalized. All characters after the first character in each word must be lowercase. 

 Remove all characters that are not an English letter, except the first '#' . 

 Truncate the result to a maximum of 100 characters. 

 Return the tag after performing the actions on caption . 

 Example 1: 

 Input: caption = "Leetcode daily streak achieved" 
 
 Output: "#leetcodeDailyStreakAchieved" 
 
 Explanation: 
 
 The first letter for all words except "leetcode" should be capitalized. 

 Example 2: 

 Input: caption = "can I Go There" 
 
 Output: "#canIGoThere" 
 
 Explanation: 
 
 The first letter for all words except "can" should be capitalized. 

 Example 3: 

 Input: caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" 
 
 Output: "#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" 
 
 Explanation: 
 
 Since the first word has length 101, we need to truncate the last two letters from the word. 

 Constraints: 

 1 <= caption.length <= 150 
 
 caption consists only of English letters and ' ' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:
 string generateTag(string caption){
  stringstream ss(caption);string w,ans="#";bool first=true;
  while(ss>>w){for(char &c:w)c=tolower((unsigned char)c);if(!first)w[0]=toupper((unsigned char)w[0]);ans+=w;first=false;}
  if(ans.size()>100)ans.resize(100);return ans;
 }
};
```


## 3598. Longest Common Prefix Between Adjacent Strings After Removals

**Problem:** https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(S)

**Space complexity:** O(n) auxiliary plus O(n) output

**Complexity reasoning:** Computes adjacent LCPs and prefix/suffix maxima, then at most one bridging LCP per removal; S is total characters scanned across these comparisons.

### Problem description

You are given an array of strings words . For each index i in the range [0, words.length - 1] , perform the following steps: 

 Remove the element at index i from the words array. 
 
 Compute the length of the longest common prefix among all adjacent pairs in the modified array. 

 Return an array answer , where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i . If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0. 

 Example 1: 

 Input: words = ["jump","run","run","jump","run"] 
 
 Output: [3,0,0,3,3] 
 
 Explanation: 

 Removing index 0:

 words becomes ["run", "run", "jump", "run"] 
 
 Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3) 

 Removing index 1:

 words becomes ["jump", "run", "jump", "run"] 
 
 No adjacent pairs share a common prefix (length 0) 

 Removing index 2:

 words becomes ["jump", "run", "jump", "run"] 
 
 No adjacent pairs share a common prefix (length 0) 

 Removing index 3:

 words becomes ["jump", "run", "run", "run"] 
 
 Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3) 

 Removing index 4:

 words becomes ["jump", "run", "run", "jump"] 
 
 Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3) 

 Example 2: 

 Input: words = ["dog","racer","car"] 
 
 Output: [0,0,0] 
 
 Explanation: 

 Removing any index results in an answer of 0. 

 Constraints: 

 1 <= words.length <= 10 5 
 
 1 <= words[i].length <= 10 4 
 
 words[i] consists of lowercase English letters. 
 
 The sum of words[i].length is smaller than or equal 10 5 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:
 vector<int> longestCommonPrefix(vector<string>& words){
  int n=words.size();auto lcp=[&](const string&a,const string&b){int i=0;while(i<(int)min(a.size(),b.size())&&a[i]==b[i])++i;return i;};
  vector<int> p(n),s(n),v(n);
  for(int i=1;i<n;++i)v[i]=lcp(words[i-1],words[i]);
  for(int i=1;i<n;++i)p[i]=max(p[i-1],v[i]);
  for(int i=n-2;i>=0;--i)s[i]=max(s[i+1],v[i+1]);
  vector<int> ans(n);for(int i=0;i<n;++i){
   if(i>=2)ans[i]=max(ans[i],p[i-1]);
   if(i+2<n)ans[i]=max(ans[i],s[i+1]);
   if(i>0&&i+1<n)ans[i]=max(ans[i],lcp(words[i-1],words[i+1]));
  }return ans;
 }
};
```


## 3602. Hexadecimal and Hexatrigesimal Conversion

**Problem:** https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(log n)

**Space complexity:** O(log n)

**Complexity reasoning:** Converts n squared and n cubed into bases 16 and 36 by repeated division.

### Problem description

You are given an integer n . 
 
 Return the concatenation of the hexadecimal representation of n 2 and the hexatrigesimal representation of n 3 . 
 
 A hexadecimal number is defined as a base-16 numeral system that uses the digits 0 – 9 and the uppercase letters A - F to represent values from 0 to 15. 
 
 A hexatrigesimal number is defined as a base-36 numeral system that uses the digits 0 – 9 and the uppercase letters A - Z to represent values from 0 to 35. 

 Example 1: 

 Input: n = 13 
 
 Output: "A91P1" 
 
 Explanation: 

 n 2 = 13 * 13 = 169 . In hexadecimal, it converts to (10 * 16) + 9 = 169 , which corresponds to "A9" . 
 
 n 3 = 13 * 13 * 13 = 2197 . In hexatrigesimal, it converts to (1 * 36 2 ) + (25 * 36) + 1 = 2197 , which corresponds to "1P1" . 
 
 Concatenating both results gives "A9" + "1P1" = "A91P1" . 

 Example 2: 

 Input: n = 36 
 
 Output: "5101000" 
 
 Explanation: 

 n 2 = 36 * 36 = 1296 . In hexadecimal, it converts to (5 * 16 2 ) + (1 * 16) + 0 = 1296 , which corresponds to "510" . 
 
 n 3 = 36 * 36 * 36 = 46656 . In hexatrigesimal, it converts to (1 * 36 3 ) + (0 * 36 2 ) + (0 * 36) + 0 = 46656 , which corresponds to "1000" . 
 
 Concatenating both results gives "510" + "1000" = "5101000" . 

 Constraints: 

 1 <= n <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:
 string concatHex36(int n){
  auto conv=[](long long x,int base){string digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",s;
   do{s+=digits[x%base];x/=base;}while(x);reverse(s.begin(),s.end());return s;};
  return conv(1LL*n*n,16)+conv(1LL*n*n*n,36);
 }
};
```


## 3612. Process String with Special Operations I

**Problem:** https://leetcode.com/problems/process-string-with-special-operations-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n + W)

**Space complexity:** O(W)

**Complexity reasoning:** Appending or duplicating and reversing the evolving output costs time proportional to its current length; W sums the lengths processed by these operations.

### Problem description

You are given a string s consisting of lowercase English letters and the special characters: * , # , and % . 
 
 Build a new string result by processing s according to the following rules from left to right: 

 If the letter is a lowercase English letter append it to result . 
 
 A '*' removes the last character from result , if it exists. 
 
 A '#' duplicates the current result and appends it to itself. 
 
 A '%' reverses the current result . 

 Return the final string result after processing all characters in s . 

 Example 1: 

 Input: s = "a#b%*" 
 
 Output: "ba" 
 
 Explanation: 

 i 
 s[i] 
 Operation 
 Current result 

 0 
 'a' 
 Append 'a' 
 "a" 

 1 
 '#' 
 Duplicate result 
 "aa" 

 2 
 'b' 
 Append 'b' 
 "aab" 

 3 
 '%' 
 Reverse result 
 "baa" 

 4 
 '*' 
 Remove the last character 
 "ba" 

 Thus, the final result is "ba" . 

 Example 2: 

 Input: s = "z*#" 
 
 Output: "" 
 
 Explanation: 

 i 
 s[i] 
 Operation 
 Current result 

 0 
 'z' 
 Append 'z' 
 "z" 

 1 
 '*' 
 Remove the last character 
 "" 

 2 
 '#' 
 Duplicate the string 
 "" 

 Thus, the final result is "" . 

 Constraints: 

 1 <= s.length <= 20 
 
 s consists of only lowercase English letters and special characters * , # , and % .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 string processStr(string s){string t;for(char c:s){if(c=='*'){if(!t.empty())t.pop_back();}else if(c=='#')t+=t;else if(c=='%')reverse(t.begin(),t.end());else t+=c;}return t;}
};
```


## 3614. Process String with Special Operations II

**Problem:** https://leetcode.com/problems/process-string-with-special-operations-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Stores the output length after every operation and walks the operations backward to locate character k.

### Problem description

You are given a string s consisting of lowercase English letters and the special characters: '*' , '#' , and '%' . 
 
 You are also given an integer k . 
 
 Build a new string result by processing s according to the following rules from left to right: 

 If the letter is a lowercase English letter append it to result . 
 
 A '*' removes the last character from result , if it exists. 
 
 A '#' duplicates the current result and appends it to itself. 
 
 A '%' reverses the current result . 

 Return the k th character of the final string result . If k is out of the bounds of result , return '.' . 

 Example 1: 

 Input: s = "a#b%*", k = 1 
 
 Output: "a" 
 
 Explanation: 

 i 
 s[i] 
 Operation 
 Current result 

 0 
 'a' 
 Append 'a' 
 "a" 

 1 
 '#' 
 Duplicate result 
 "aa" 

 2 
 'b' 
 Append 'b' 
 "aab" 

 3 
 '%' 
 Reverse result 
 "baa" 

 4 
 '*' 
 Remove the last character 
 "ba" 

 The final result is "ba" . The character at index k = 1 is 'a' . 

 Example 2: 

 Input: s = "cd%#*#", k = 3 
 
 Output: "d" 
 
 Explanation: 

 i 
 s[i] 
 Operation 
 Current result 

 0 
 'c' 
 Append 'c' 
 "c" 

 1 
 'd' 
 Append 'd' 
 "cd" 

 2 
 '%' 
 Reverse result 
 "dc" 

 3 
 '#' 
 Duplicate result 
 "dcdc" 

 4 
 '*' 
 Remove the last character 
 "dcd" 

 5 
 '#' 
 Duplicate result 
 "dcddcd" 

 The final result is "dcddcd" . The character at index k = 3 is 'd' . 

 Example 3: 

 Input: s = "z*#", k = 0 
 
 Output: "." 
 
 Explanation: 

 i 
 s[i] 
 Operation 
 Current result 

 0 
 'z' 
 Append 'z' 
 "z" 

 1 
 '*' 
 Remove the last character 
 "" 

 2 
 '#' 
 Duplicate the string 
 "" 

 The final result is "" . Since index k = 0 is out of bounds, the output is '.' . 

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists of only lowercase English letters and special characters '*' , '#' , and '%' . 
 
 0 <= k <= 10 15 
 
 The length of result after processing s will not exceed 10 15 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
 char processStr(string s,long long k){
  const long long CAP=(long long)4e18;vector<long long>len(s.size()+1);for(int i=0;i<(int)s.size();++i){char c=s[i];long long x=len[i];if(c=='*')x=max(0LL,x-1);else if(c=='#')x=min(CAP,x>CAP/2?CAP:2*x);else if(c!='%')x=min(CAP,x+1);len[i+1]=x;}
  if(k>=len.back())return '.';
  for(int i=(int)s.size()-1;i>=0;--i){char c=s[i];if(c=='#'){if(len[i])k%=len[i];}else if(c=='%'){k=len[i]-1-k;}else if(c!='*'){if(k==len[i])return c;}}
  return '.';
 }
};
```


## 3696. Maximum Distance Between Unequal Words in Array I

**Problem:** https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n * L) worst case

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Checks each word against the first and last word; comparisons can scan up to L characters.

### Problem description

You are given a string array words . 
 
 Find the maximum distance between two distinct indices i and j such that: 

 words[i] != words[j] , and 
 
 the distance is defined as j - i + 1 . 

 Return the maximum distance among all such pairs. If no valid pair exists, return 0. 

 Example 1: 

 Input: words = ["leetcode","leetcode","codeforces"] 
 
 Output: 3 
 
 Explanation: 
 
 In this example, words[0] and words[2] are not equal, and they have the maximum distance 2 - 0 + 1 = 3 . 

 Example 2: 

 Input: words = ["a","b","c","a","a"] 
 
 Output: 4 
 
 Explanation: 
 
 In this example words[1] and words[4] have the largest distance of 4 - 1 + 1 = 4 . 

 Example 3: 

 Input: words = ["z","z","z"] 
 
 Output: 0 
 
 Explanation: 
 
 In this example all the words are equal, thus the answer is 0. 

 Constraints: 

 1 <= words.length <= 100 
 
 1 <= words[i].length <= 10 
 
 words[i] consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int maxDistance(vector<string>& words) {
        int n = words.size(), answer = 0;
        for (int i = 0; i < n; ++i) {
            if (words[i] != words[0]) answer = max(answer, i + 1);
            if (words[i] != words[n - 1]) answer = max(answer, n - i);
        }
        return answer;
    }
};
```


## 3703. Remove K-Balanced Substrings

**Problem:** https://leetcode.com/problems/remove-k-balanced-substrings/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Stack, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n)

**Complexity reasoning:** Uses run-length stack updates and removals, then materializes the surviving characters.

### Problem description

You are given a string s consisting of '(' and ')' , and an integer k . 
 
 A string is k-balanced if it is exactly k consecutive '(' followed by k consecutive ')' , i.e., '(' * k + ')' * k . 
 
 For example, if k = 3 , k-balanced is "((()))" . 
 
 You must repeatedly remove all non-overlapping k-balanced substrings from s , and then join the remaining parts. Continue this process until no k-balanced substring exists. 
 
 Return the final string after all possible removals. 

 ​​​​​​​ Example 1: 

 Input: s = "(())", k = 1 
 
 Output: "" 
 
 Explanation: 
 
 k-balanced substring is "()" 

 Step 
 Current s 
 k-balanced 
 Result s 

 1 
 (()) 
 ( () ) 
 () 

 2 
 () 
 () 
 Empty 

 Thus, the final string is "" . 

 Example 2: 

 Input: s = "(()(", k = 1 
 
 Output: "((" 
 
 Explanation: 
 
 k-balanced substring is "()" 

 Step 
 Current s 
 k-balanced 
 Result s 

 1 
 (()( 
 ( () ( 
 (( 

 2 
 (( 
 - 
 (( 

 Thus, the final string is "((" . 

 Example 3: 

 Input: s = "((()))()()()", k = 3 
 
 Output: "()()()" 
 
 Explanation: 
 
 k-balanced substring is "((()))" 

 Step 
 Current s 
 k-balanced 
 Result s 

 1 
 ((()))()()() 
 ((())) ()()() 
 ()()() 

 2 
 ()()() 
 - 
 ()()() 

 Thus, the final string is "()()()" . 

 Constraints: 

 2 <= s.length <= 10 5 
 
 s consists only of '(' and ')' . 
 
 1 <= k <= s.length / 2

### C++ solution

**Source:** accepted_cpp_submission

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


## 3706. Maximum Distance Between Unequal Words in Array II

**Problem:** https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n * L) worst case

**Space complexity:** O(1) auxiliary

**Complexity reasoning:** Checks each word against both endpoint words; string equality can take O(L).

### Problem description

You are given a string array words . 
 
 Find the maximum distance between two distinct indices i and j such that: 

 words[i] != words[j] , and 
 
 the distance is defined as j - i + 1 . 

 Return the maximum distance among all such pairs. If no valid pair exists, return 0. 

 Example 1: 

 Input: words = ["leetcode","leetcode","codeforces"] 
 
 Output: 3 
 
 Explanation: 
 
 In this example, words[0] and words[2] are not equal, and they have the maximum distance 2 - 0 + 1 = 3 . 

 Example 2: 

 Input: words = ["a","b","c","a","a"] 
 
 Output: 4 
 
 Explanation: 
 
 In this example words[1] and words[4] have the largest distance of 4 - 1 + 1 = 4 . 

 Example 3: 

 Input: words = ["z","z","z"] 
 
 Output: 0 
 
 Explanation: 
 
 ​​​​​​​ In this example all the words are equal, thus the answer is 0. 

 Constraints: 

 1 <= words.length <= 10 5 
 
 1 <= words[i].length <= 10 
 
 words[i] consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int maxDistance(vector<string>& words) {
        int n = words.size(), ans = 0;
        for (int i = 0; i < n; ++i) {
            if (words[i] != words[0]) ans = max(ans, i + 1);
            if (words[i] != words[n - 1]) ans = max(ans, n - i);
        }
        return ans;
    }
};
```


## 3744. Find Kth Character in Expanded String

**Problem:** https://leetcode.com/problems/find-kth-character-in-expanded-string/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Walks the input once, maintaining the current output position and repeat count.

### Problem description

You are given a string s consisting of one or more words separated by single spaces. Each word in s consists of lowercase English letters. 
 
 We obtain the expanded string t from s as follows: 

 For each word in s , repeat its first character once, then its second character twice, and so on. 

 For example, if s = "hello world" , then t = "heelllllllooooo woorrrllllddddd" . 
 
 You are also given an integer k , representing a valid index of the string t . 
 
 Return the k th character of the string t . 

 Example 1: 

 Input: s = "hello world", k = 0 
 
 Output: "h" 
 
 Explanation: 
 
 t = "heelllllllooooo woorrrllllddddd" . Therefore, the answer is t[0] = "h" . 

 Example 2: 

 Input: s = "hello world", k = 15 
 
 Output: " " 
 
 Explanation: 
 
 t = "heelllllllooooo woorrrllllddddd" . Therefore, the answer is t[15] = " " . 

 Constraints: 

 1 <= s.length <= 10 5 
 
 s contains only lowercase English letters and spaces ' ' . 
 
 s does not contain any leading or trailing spaces. 
 
 All the words in s are separated by a single space . 
 
 0 <= k < t.length . That is, k is a valid index of t .

### C++ solution

**Source:** accepted_cpp_submission

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


## 3798. Largest Even Number

**Problem:** https://leetcode.com/problems/largest-even-number/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) output

**Complexity reasoning:** Scans backward for the last even digit and returns the corresponding prefix.

### Problem description

You are given a string s consisting only of the characters '1' and '2' . 
 
 You may delete any number of characters from s without changing the order of the remaining characters. 
 
 Return the largest possible resultant string that represents an even integer. If there is no such string, return the empty string "" . 

 Example 1: 

 Input: s = "1112" 
 
 Output: "1112" 
 
 Explanation: 
 
 The string already represents the largest possible even number, so no deletions are needed. 

 Example 2: 

 Input: s = "221" 
 
 Output: "22" 
 
 Explanation: 
 
 Deleting '1' results in the largest possible even number which is equal to 22. 

 Example 3: 

 Input: s = "1" 
 
 Output: "" 
 
 Explanation: 
 
 There is no way to get an even number. 

 Constraints: 

 1 <= s.length <= 100 
 
 s consists only of the characters '1' and '2' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string largestEven(string s) {
        for(int i=(int)s.size()-1;i>=0;--i)
            if((s[i]-'0')%2==0) return s.substr(0,i+1);
        return "";
    }
};
```


## 3813. Vowel-Consonant Score

**Problem:** https://leetcode.com/problems/vowel-consonant-score/

**Difficulty:** Easy | **Premium:** No

**Tags:** String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** Examines each character and tests membership in a constant-size vowel string.

### Problem description

You are given a string s consisting of lowercase English letters, spaces, and digits. 
 
 Let v be the number of vowels in s and c be the number of consonants in s . 
 
 A vowel is one of the letters 'a' , 'e' , 'i' , 'o' , or 'u' , while any other letter in the English alphabet is considered a consonant. 
 
 The score of the string s is defined as follows: 

 If c > 0 , the score = floor(v / c) where floor denotes rounding down to the nearest integer. 
 
 Otherwise, the score = 0 . 

 Return an integer denoting the score of the string. 

 Example 1: 

 Input: s = "cooear" 
 
 Output: 2 
 
 Explanation: 
 
 The string s = "cooear" contains v = 4 vowels ('o', 'o', 'e', 'a') and c = 2 consonants ('c', 'r') . 
 
 The score is floor(v / c) = floor(4 / 2) = 2 . 

 Example 2: 

 Input: s = "axeyizou" 
 
 Output: 1 
 
 Explanation: 
 
 The string s = "axeyizou" contains v = 5 vowels ('a', 'e', 'i', 'o', 'u') and c = 3 consonants ('x', 'y', 'z') . 
 
 The score is floor(v / c) = floor(5 / 3) = 1 . 

 Example 3: 

 Input: s = "au 123" 
 
 Output: 0 
 
 Explanation: 
 
 The string s = "au 123" contains no consonants (c = 0) , so the score is 0. 

 Constraints: 

 1 <= s.length <= 100 
 
 s consists of lowercase English letters, spaces and digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int vowelConsonantScore(string s) {
        int v=0,c=0;
        for(char ch:s){
            ch=tolower((unsigned char)ch);
            if(ch<'a'||ch>'z') continue;
            if(string("aeiou").find(ch)!=string::npos) ++v;
            else ++c;
        }
        return c==0?0:v/c;
    }
};
```


## 3817. Good Indices in a Digit String

**Problem:** https://leetcode.com/problems/good-indices-in-a-digit-string/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n) output

**Complexity reasoning:** For each index, creates its decimal representation and compares up to O(log n) characters.

### Problem description

You are given a string s consisting of digits. 
 
 An index i is called good if there exists a substring of s that ends at index i and is equal to the decimal representation of i . 
 
 Return an integer array of all good indices in increasing order . 

 Example 1: 

 Input: s = "0234567890112" 
 
 Output: [0,11,12] 
 
 Explanation:​​​​​​​ 

 At index 0, the decimal representation of the index is "0" . The substring s[0] is "0" , which matches, so index 0 is good. 

 At index 11, the decimal representation is "11" . The substring s[10..11] is "11" , which matches, so index 11 is good. 

 At index 12, the decimal representation is "12" . The substring s[11..12] is "12" , which matches, so index 12 is good. 

 No other index has a substring ending at it that equals its decimal representation. Therefore, the answer is [0, 11, 12] . 

 Example 2: 

 Input: s = "01234" 
 
 Output: [0,1,2,3,4] 
 
 Explanation: 
 
 For every index i from 0 to 4, the decimal representation of i is a single digit, and the substring s[i] matches that digit. 
 
 Therefore, a valid substring ending at each index exists, making all indices good. 

 Example 3: 

 Input: s = "12345" 
 
 Output: [] 
 
 Explanation: 
 
 No index has a substring ending at it that matches its decimal representation. 
 
 Therefore, there are no good indices and the result is an empty array. 

 Constraints: 

 1 <= s.length <= 10 5 
 
 s only consists of digits from '0' to '9' .

### C++ solution

**Source:** accepted_cpp_submission

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


## 3838. Weighted Word Mapping

**Problem:** https://leetcode.com/problems/weighted-word-mapping/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(S)

**Space complexity:** O(w) output

**Complexity reasoning:** Sums weights over all S letters and appends one mapped character per word.

### Problem description

You are given an array of strings words , where each string represents a word containing lowercase English letters. 
 
 You are also given an integer array weights of length 26, where weights[i] represents the weight of the i th lowercase English letter. 
 
 The weight of a word is defined as the sum of the weights of its characters. 
 
 For each word, take its weight modulo 26 and map the result to a lowercase English letter using reverse alphabetical order ( 0 -> 'z', 1 -> 'y', ..., 25 -> 'a' ). 
 
 Return a string formed by concatenating the mapped characters for all words in order. 

 Example 1: 

 Input: words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2] 
 
 Output: "rij" 
 
 Explanation: 

 The weight of "abcd" is 5 + 3 + 12 + 14 = 34 . The result modulo 26 is 34 % 26 = 8 , which maps to 'r' . 
 
 The weight of "def" is 14 + 1 + 2 = 17 . The result modulo 26 is 17 % 26 = 17 , which maps to 'i' . 
 
 The weight of "xyz" is 7 + 7 + 2 = 16 . The result modulo 26 is 16 % 26 = 16 , which maps to 'j' . 

 Thus, the string formed by concatenating the mapped characters is "rij" . 

 Example 2: 

 Input: words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 
 
 Output: "yyy" 
 
 Explanation: 
 
 Each word has weight 1. The result modulo 26 is 1 % 26 = 1 , which maps to 'y' . 
 
 Thus, the string formed by concatenating the mapped characters is "yyy" . 

 Example 3: 

 Input: words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5] 
 
 Output: "g" 
 
 Explanation:​​​​​​​ 
 
 The weight of "abcd" is 7 + 5 + 3 + 4 = 19 . The result modulo 26 is 19 % 26 = 19 , which maps to 'g' . 
 
 Thus, the string formed by concatenating the mapped characters is "g" . 

 Constraints: 

 1 <= words.length <= 100 
 
 1 <= words[i].length <= 10 
 
 weights.length == 26 
 
 1 <= weights[i] <= 100 
 
 words[i] consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        string ans;
        for (const string& word : words) {
            int sum = 0;
            for (char c : word) sum = (sum + weights[c - 'a']) % 26;
            ans += char('z' - sum);
        }
        return ans;
    }
};
```


## 3856. Trim Trailing Vowels

**Problem:** https://leetcode.com/problems/trim-trailing-vowels/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) for the by-value string parameter; O(1) additional working space

**Complexity reasoning:** The loop removes at most n trailing characters. Each vowel check searches a fixed five-character string; the input string is copied because it is passed by value.

### Problem description

You are given a string s that consists of lowercase English letters. 
 
 Return the string obtained by removing all trailing vowels from s . 
 
 The vowels consist of the characters 'a' , 'e' , 'i' , 'o' , and 'u' . 

 Example 1: 

 Input: s = "idea" 
 
 Output: "id" 
 
 Explanation: 
 
 Removing "id ea " , we obtain the string "id" . 

 Example 2: 

 Input: s = "day" 
 
 Output: "day" 
 
 Explanation: 
 
 There are no trailing vowels in the string "day" . 

 Example 3: 

 Input: s = "aeiou" 
 
 Output: "" 
 
 Explanation: 
 
 Removing " aeiou " , we obtain the string "" . 

 Constraints: 

 1 <= s.length <= 100 
 
 s consists of only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string trimTrailingVowels(string s) {
        while(!s.empty() && string("aeiou").find(s.back())!=string::npos) s.pop_back();
        return s;
    }
};
```


## 3863. Minimum Operations to Sort a String

**Problem:** https://leetcode.com/problems/minimum-operations-to-sort-a-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(n) for the by-value string parameter; O(1) additional working space

**Complexity reasoning:** The sortedness check, minimum/maximum scans, and optional counts each traverse the string at most once; there is a constant number of such passes.

### Problem description

You are given a string s consisting of lowercase English letters. 
 
 In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order. 
 
 Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1. 

 Example 1: 

 Input: s = "dog" 
 
 Output: 1 
 
 Explanation: ​​​​​​​ 

 Sort substring "og" to "go" . 
 
 Now, s = "dgo" , which is sorted in ascending order. Thus, the answer is 1. 

 Example 2: 

 Input: s = "card" 
 
 Output: 2 
 
 Explanation: 

 Sort substring "car" to "acr" , so s = "acrd" . 
 
 Sort substring "rd" to "dr" , making s = "acdr" , which is sorted in ascending order. Thus, the answer is 2. 

 Example 3: 

 Input: s = "gf" 
 
 Output: -1 
 
 Explanation: 

 It is impossible to sort s under the given constraints. Thus, the answer is -1. 

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists of only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

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


## 3894. Traffic Signal Color

**Problem:** https://leetcode.com/problems/traffic-signal-color/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** A fixed number of integer comparisons determines the returned constant-size color string.

### Problem description

You are given an integer timer representing the remaining time (in seconds) on a traffic signal. 
 
 The signal follows these rules: 

 If timer == 0 , the signal is "Green" 
 
 If timer == 30 , the signal is "Orange" 
 
 If 30 < timer <= 90 , the signal is "Red" 

 Return the current state of the signal. If none of the above conditions are met, return "Invalid" . 

 Example 1: 

 Input: timer = 60 
 
 Output: "Red" 
 
 Explanation: 
 
 Since timer = 60 , and 30 < timer <= 90 , the answer is "Red" . 

 Example 2: 

 Input: timer = 5 
 
 Output: "Invalid" 
 
 Explanation: 
 
 Since timer = 5 , it does not satisfy any of the given conditions, the answer is "Invalid" . 

 Constraints: 

 0 <= timer <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string trafficSignal(int timer) {
        if (timer == 0) return "Green";
        if (timer == 30) return "Orange";
        if (timer > 30 && timer <= 90) return "Red";
        return "Invalid";
    }
};
```


## 3921. Score Validator

**Problem:** https://leetcode.com/problems/score-validator/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String, Simulation

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(E + L)

**Space complexity:** O(1) auxiliary space, excluding the fixed-size result

**Complexity reasoning:** The loop processes at most E events until ten wins; comparisons can inspect event text, with total examined length L. The score and win counter use constant space.

### Problem description

You are given a string array events . 
 
 Initially, score = 0 and counter = 0 . Each element in events is one of the following: 

 "0" , "1" , "2" , "3" , "4" , "6" : Add that value to the total score. 
 
 "W" : Increase the counter by 1. No score is added. 
 
 "WD" : Add 1 to the total score. 
 
 "NB" : Add 1 to the total score. 

 Process the array from left to right. Stop processing when either: 

 All elements in events have been processed, or 
 
 The counter becomes 10. 

 Return an integer array [score, counter] , where: 

 score is the final total score. 
 
 counter is the final counter value. 

 Example 1: 

 Input: events = ["1","4","W","6","WD"] 
 
 Output: [12,1] 
 
 Explanation: 

 Event 
 Score 
 Counter 

 "1" 
 1 
 0 

 "4" 
 5 
 0 

 "W" 
 5 
 1 

 "6" 
 11 
 1 

 "WD" 
 12 
 1 

 Final result: [12, 1] . 

 Example 2: 

 Input: events = ["WD","NB","0","4","4"] 
 
 Output: [10,0] 
 
 Explanation: 

 Event 
 Score 
 Counter 

 "WD" 
 1 
 0 

 "NB" 
 2 
 0 

 "0" 
 2 
 0 

 "4" 
 6 
 0 

 "4" 
 10 
 0 

 Final result: [10, 0] . 

 Example 3: 

 Input: events = ["W","W","W","W","W","W","W","W","W","W","W"] 
 
 Output: [0,10] 
 
 Explanation: 
 
 After 10 occurrences of "W" , the counter reaches 10, so processing stops. The remaining events are ignored. 

 Constraints: 

 1 <= events.length <= 1000 
 
 events[i] is one of "0" , "1" , "2" , "3" , "4" , "6" , "W" , "WD" , or "NB" .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<int> scoreValidator(vector<string>& events) {
        int score = 0, counter = 0;
        for (const string& event : events) {
            if (event == "W") ++counter;
            else if (event == "WD" || event == "NB") ++score;
            else score += event[0] - '0';
            if (counter == 10) break;
        }
        return {score, counter};
    }
};
```


## 3922. Minimum Flips to Make Binary String Coherent

**Problem:** https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

**Difficulty:** Medium | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1)

**Complexity reasoning:** For each of n characters, the DP examines 16 masks and two candidate bits, a constant number of transitions. Two fixed arrays of 16 integers store the states.

### Problem description

You are given a binary string s . 
 
 A string is considered coherent if it does not contain "011" or "110" as subsequences . 
 
 In one operation, you can flip any character in s ( '0' to '1' or '1' to '0' ). 
 
 Return an integer denoting the minimum number of operations required to make s coherent. 

 Example 1: 

 Input: s = "1010" 
 
 Output: 1 
 
 Explanation: 
 
 Flip s[0] to get "0010" , which contains no "011" or "110" subsequences. 

 Example 2: 

 Input: s = "0110" 
 
 Output: 1 
 
 Explanation: 
 
 Flip s[1] to get "0010" , removing all forbidden subsequences "011" and "110" . 

 Example 3: 

 Input: s = "1000" 
 
 Output: 0 
 
 Explanation: 
 
 The string already has no "011" or "110" subsequences, so no flips are needed. 

 Constraints: 

 1 <= s.length <= 10 5 
 
 s[i] is either '0' or '1' .

### C++ solution

**Source:** accepted_cpp_submission

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


## 3931. Check Adjacent Digit Differences

**Problem:** https://leetcode.com/problems/check-adjacent-digit-differences/

**Difficulty:** Easy | **Premium:** No

**Tags:** String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n)

**Space complexity:** O(1) auxiliary space

**Complexity reasoning:** The loop checks each adjacent character pair once and returns early if any difference exceeds two.

### Problem description

You are given a string s consisting of digits. 
 
 Return true if the absolute difference between every pair of adjacent digits is at most 2, otherwise return false . 
 
 The absolute difference between a and b is defined as abs(a - b) . 

 Example 1: 

 Input: s = "132" 
 
 Output: true 
 
 Explanation: 

 The absolute difference between digits at s[0] and s[1] is abs(1 - 3) = 2 . 
 
 The absolute difference between digits at s[1] and s[2] is abs(3 - 2) = 1 . 
 
 Since both differences are at most 2, the answer is true. 

 Example 2: 

 Input: s = "129" 
 
 Output: false 
 
 Explanation: 

 The absolute difference between digits at s[0] and s[1] is abs(1 - 2) = 1 . 
 
 The absolute difference between digits at s[1] and s[2] is abs(2 - 9) = 7 , which is greater than 2. 
 
 Therefore, the answer is false. 

 Constraints: 

 2 <= s.length <= 100 
 
 s consists only of digits.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool isAdjacentDiffAtMostTwo(string s) {
        for (int i = 1; i < (int)s.size(); ++i)
            if (abs(s[i] - s[i - 1]) > 2) return false;
        return true;
    }
};
```


## 3986. Number of Elapsed Seconds Between Two Times

**Problem:** https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

**Difficulty:** Easy | **Premium:** No

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(1)

**Space complexity:** O(1)

**Complexity reasoning:** Each timestamp has fixed HH:MM:SS length; extracting and parsing six two-digit fields requires constant time and temporary storage.

### Problem description

You are given two valid times startTime and endTime , each represented as a string in the format "HH:MM:SS" . 
 
 Return the number of seconds that have elapsed from startTime to endTime . 

 Example 1: 

 Input: startTime = "01:00:00", endTime = "01:00:25" 
 
 Output: 25 
 
 Explanation: 
 endTime is 25 seconds ahead of startTime . 
 
 Example 2: 

 Input: startTime = "12:34:56", endTime = "13:00:00" 
 
 Output: 1504 
 
 Explanation: 
 
 endTime is 25 minutes and 4 seconds ahead of startTime , which equals 1504 seconds. 

 Constraints: 

 startTime.length == 8 
 
 endTime.length == 8 
 
 startTime and endTime are valid times in the format "HH:MM:SS" 
 
 00 <= HH <= 23 
 
 00 <= MM <= 59 
 
 00 <= SS <= 59 
 
 endTime is not earlier than startTime

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int secondsBetweenTimes(string startTime, string endTime) {
        auto seconds = [](const string& t) {
            return stoi(t.substr(0, 2)) * 3600 + stoi(t.substr(3, 2)) * 60 + stoi(t.substr(6, 2));
        };
        return seconds(endTime) - seconds(startTime);
    }
};
```


## 4021. Minimum Operations to Make a Rotated Palindrome I

**Problem:** https://leetcode.com/problems/minimum-operations-to-make-a-rotated-palindrome-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, String, Enumeration

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n²)

**Space complexity:** O(n) for the by-value input string; O(1) auxiliary space

**Complexity reasoning:** The algorithm tries n rotations and compares n/2 mirrored character pairs for each, with constant work per pair.

### Problem description

You are given a string s consisting of lowercase English letters. 
 
 You can perform the following operations any number of times (including zero) and in any order: 

 Increment : Choose any index i and replace s[i] with the next lowercase English letter. The letter after 'z' is 'a' . 
 
 Left rotate : Move the first character of the string to the end. 

 Return the minimum number of operations required to make s a palindrome . 

 Example 1: 

 Input: s = "abc" 
 
 Output: 2 
 
 Explanation: 
One optimal solution:

 Left rotate the string: "abc" -> "bca" . 
 
 Increment 'a' to 'b' : "bca" -> "bcb" . 
 
 "bcb" is a palindrome. Thus, the answer is 2. 

 Example 2: 

 Input: s = "yb" 
 
 Output: 3 
 
 Explanation: 

 Increment the first character three times: "yb" -> "zb" -> "ab" -> "bb" . 
 
 "bb" is a palindrome. Thus, the answer is 3. 

 Constraints: 

 2 <= s.length <= 2000 
 
 s consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

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


## 4028. Minimum Operations to Make a Rotated Palindrome II

**Problem:** https://leetcode.com/problems/minimum-operations-to-make-a-rotated-palindrome-ii/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Math, String

**Primary pattern:** String Algorithms

**Related patterns:** String Algorithms, Math / Number Theory

**Data structures (inferred):** String, Vector

**Pattern recognition:** Prefix/suffix structure, substring matching, or character constraints.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** O(n log n)

**Space complexity:** O(n) auxiliary space, plus O(n) for the by-value input string

**Complexity reasoning:** There are 13 fixed feature passes. Each performs two FFTs and a pointwise product on the next power-of-two length at least 2n, plus linear scans; FFT dominates. The complex arrays and mismatch vector have O(n) elements.

### Problem description

You are given a string s consisting of lowercase English letters. 
 
 You can perform the following operations any number of times (including zero) and in any order: 

 Increment : Choose any index i and replace s[i] with the next lowercase English letter. The letter after 'z' is 'a' . 
 
 Left rotate : Move the first character of the string to the end. 

 Return the minimum number of operations required to make s a palindrome . 

 Example 1: 

 Input: s = "abc" 
 
 Output: 2 
 
 Explanation: 
One optimal solution:

 Left rotate the string: "abc" -> "bca" . 
 
 Increment 'a' to 'b' : "bca" -> "bcb" . 
 
 "bcb" is a palindrome. Thus, the answer is 2. 

 Example 2: 

 Input: s = "yb" 
 
 Output: 3 
 
 Explanation: 

 Increment the first character three times: "yb" -> "zb" -> "ab" -> "bb" . 
 
 "bb" is a palindrome. Thus, the answer is 3. 

 Constraints: 

 2 <= s.length <= 5 * 10 4 
 
 s​​​​​​​​​​​​​​ consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    using cd=complex<double>;
    const double PI=acos(-1.0);
    void fft(vector<cd>& a,bool invert) {
        int n=a.size();
        for(int i=1,j=0;i<n;++i) {
            int bit=n>>1;
            for(;j&bit;bit>>=1)j^=bit;
            j^=bit;
            if(i<j)swap(a[i],a[j]);
        }
        for(int len=2;len<=n;len<<=1) {
            double ang=2*PI/len*(invert?-1:1);
            cd wlen(cos(ang),sin(ang));
            for(int i=0;i<n;i+=len) {
                cd w(1);
                for(int j=0;j<len/2;++j) {
                    cd u=a[i+j],v=a[i+j+len/2]*w;
                    a[i+j]=u+v;
                    a[i+j+len/2]=u-v;
                    w*=wlen;
                }
            }
        }
        if(invert)for(cd &x:a)x/=n;
    }
public:
    int minOperations(string s) {
        int n=s.size(),size=1;
        while(size<2*n)size<<=1;
        vector<long long> mismatch(n,0);
        for(int feature=0;feature<13;++feature) {
            vector<cd> a(size);
            int cnt=0;
            for(int i=0;i<n;++i) {
                int x=s[i]-'a';
                int delta=(x-feature+26)%26;
                if(delta<13) {a[i]=1;++cnt;}
            }
            fft(a,false);
            for(cd &v:a)v*=v;
            fft(a,true);
            for(int c=0;c<n;++c) {
                long long conv=llround(a[c].real());
                if(c+n<2*n-1)conv+=llround(a[c+n].real());
                mismatch[c]+=cnt-conv;
            }
        }
        long long ans=LLONG_MAX;
        for(int r=0;r<n;++r) {
            int c=(2LL*r+n-1)%n;
            ans=min(ans,mismatch[c]+r);
        }
        return (int)ans;
    }
};
```

