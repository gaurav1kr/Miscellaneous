# Tree / Trie

**Problems:** 107

## Quick revision checklist

Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

## Problem index

- [14. Longest Common Prefix](#14-longest-common-prefix) — Easy; code: yes
- [105. Construct Binary Tree from Preorder and Inorder Traversal](#105-construct-binary-tree-from-preorder-and-inorder-traversal) — Medium; code: yes
- [106. Construct Binary Tree from Inorder and Postorder Traversal](#106-construct-binary-tree-from-inorder-and-postorder-traversal) — Medium; code: yes
- [108. Convert Sorted Array to Binary Search Tree](#108-convert-sorted-array-to-binary-search-tree) — Easy; code: yes
- [109. Convert Sorted List to Binary Search Tree](#109-convert-sorted-list-to-binary-search-tree) — Medium; code: yes
- [173. Binary Search Tree Iterator](#173-binary-search-tree-iterator) — Medium; code: yes
- [208. Implement Trie (Prefix Tree)](#208-implement-trie-prefix-tree) — Medium; code: yes
- [212. Word Search II](#212-word-search-ii) — Hard; code: yes
- [218. The Skyline Problem](#218-the-skyline-problem) — Hard; code: yes
- [307. Range Sum Query - Mutable](#307-range-sum-query---mutable) — Medium; code: yes
- [308. Range Sum Query 2D - Mutable](#308-range-sum-query-2d---mutable) — Medium; code: yes
- [331. Verify Preorder Serialization of a Binary Tree](#331-verify-preorder-serialization-of-a-binary-tree) — Medium; code: yes
- [336. Palindrome Pairs](#336-palindrome-pairs) — Hard; code: yes
- [406. Queue Reconstruction by Height](#406-queue-reconstruction-by-height) — Medium; code: yes
- [421. Maximum XOR of Two Numbers in an Array](#421-maximum-xor-of-two-numbers-in-an-array) — Medium; code: yes
- [425. Word Squares](#425-word-squares) — Hard; code: yes
- [427. Construct Quad Tree](#427-construct-quad-tree) — Medium; code: yes
- [440. K-th Smallest in Lexicographical Order](#440-k-th-smallest-in-lexicographical-order) — Hard; code: yes
- [450. Delete Node in a BST](#450-delete-node-in-a-bst) — Medium; code: yes
- [510. Inorder Successor in BST II](#510-inorder-successor-in-bst-ii) — Medium; code: yes
- [527. Word Abbreviation](#527-word-abbreviation) — Hard; code: yes
- [558. Logical OR of Two Binary Grids Represented as Quad-Trees](#558-logical-or-of-two-binary-grids-represented-as-quad-trees) — Medium; code: yes
- [588. Design In-Memory File System](#588-design-in-memory-file-system) — Hard; code: yes
- [616. Add Bold Tag in String](#616-add-bold-tag-in-string) — Medium; code: yes
- [648. Replace Words](#648-replace-words) — Medium; code: yes
- [677. Map Sum Pairs](#677-map-sum-pairs) — Medium; code: yes
- [692. Top K Frequent Words](#692-top-k-frequent-words) — Medium; code: yes
- [699. Falling Squares](#699-falling-squares) — Hard; code: yes
- [700. Search in a Binary Search Tree](#700-search-in-a-binary-search-tree) — Easy; code: yes
- [701. Insert into a Binary Search Tree](#701-insert-into-a-binary-search-tree) — Medium; code: yes
- [703. Kth Largest Element in a Stream](#703-kth-largest-element-in-a-stream) — Easy; code: yes
- [715. Range Module](#715-range-module) — Hard; code: yes
- [720. Longest Word in Dictionary](#720-longest-word-in-dictionary) — Medium; code: yes
- [745. Prefix and Suffix Search](#745-prefix-and-suffix-search) — Hard; code: yes
- [758. Bold Words in String](#758-bold-words-in-string) — Medium; code: yes
- [776. Split BST](#776-split-bst) — Medium; code: yes
- [820. Short Encoding of Words](#820-short-encoding-of-words) — Medium; code: yes
- [850. Rectangle Area II](#850-rectangle-area-ii) — Hard; code: yes
- [889. Construct Binary Tree from Preorder and Postorder Traversal](#889-construct-binary-tree-from-preorder-and-postorder-traversal) — Medium; code: yes
- [998. Maximum Binary Tree II](#998-maximum-binary-tree-ii) — Medium; code: yes
- [1032. Stream of Characters](#1032-stream-of-characters) — Hard; code: yes
- [1065. Index Pairs of a String](#1065-index-pairs-of-a-string) — Easy; code: yes
- [1104. Path In Zigzag Labelled Binary Tree](#1104-path-in-zigzag-labelled-binary-tree) — Medium; code: yes
- [1166. Design File System](#1166-design-file-system) — Medium; code: yes
- [1178. Number of Valid Words for Each Puzzle](#1178-number-of-valid-words-for-each-puzzle) — Hard; code: yes
- [1316. Distinct Echo Substrings](#1316-distinct-echo-substrings) — Hard; code: yes
- [1409. Queries on a Permutation With Key](#1409-queries-on-a-permutation-with-key) — Medium; code: yes
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](#1505-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits) — Hard; code: yes
- [1586. Binary Search Tree Iterator II](#1586-binary-search-tree-iterator-ii) — Medium; code: yes
- [1597. Build Binary Expression Tree From Infix Expression](#1597-build-binary-expression-tree-from-infix-expression) — Hard; code: yes
- [1622. Fancy Sequence](#1622-fancy-sequence) — Hard; code: yes
- [1628. Design an Expression Tree With Evaluate Function](#1628-design-an-expression-tree-with-evaluate-function) — Medium; code: yes
- [1698. Number of Distinct Substrings in a String](#1698-number-of-distinct-substrings-in-a-string) — Medium; code: yes
- [1707. Maximum XOR With an Element From Array](#1707-maximum-xor-with-an-element-from-array) — Hard; code: yes
- [1803. Count Pairs With XOR in a Range](#1803-count-pairs-with-xor-in-a-range) — Hard; code: yes
- [1804. Implement Trie II (Prefix Tree)](#1804-implement-trie-ii-prefix-tree) — Medium; code: yes
- [1902. Depth of BST Given Insertion Order](#1902-depth-of-bst-given-insertion-order) — Medium; code: yes
- [2158. Amount of New Area Painted Each Day](#2158-amount-of-new-area-painted-each-day) — Hard; code: yes
- [2196. Create Binary Tree From Descriptions](#2196-create-binary-tree-from-descriptions) — Medium; code: yes
- [2213. Longest Substring of One Repeating Character](#2213-longest-substring-of-one-repeating-character) — Hard; code: yes
- [2227. Encrypt and Decrypt Strings](#2227-encrypt-and-decrypt-strings) — Hard; code: yes
- [2236. Root Equals Sum of Children](#2236-root-equals-sum-of-children) — Easy; code: yes
- [2261. K Divisible Elements Subarrays](#2261-k-divisible-elements-subarrays) — Medium; code: yes
- [2276. Count Integers in Intervals](#2276-count-integers-in-intervals) — Hard; code: yes
- [2416. Sum of Prefix Scores of Strings](#2416-sum-of-prefix-scores-of-strings) — Hard; code: yes
- [2452. Words Within Two Edits of Dictionary](#2452-words-within-two-edits-of-dictionary) — Medium; code: yes
- [2509. Cycle Length Queries in a Tree](#2509-cycle-length-queries-in-a-tree) — Hard; code: yes
- [2569. Handling Sum Queries After Update](#2569-handling-sum-queries-after-update) — Hard; code: yes
- [2907. Maximum Profitable Triplets With Increasing Prices I](#2907-maximum-profitable-triplets-with-increasing-prices-i) — Medium; code: yes
- [2913. Subarrays Distinct Element Sum of Squares I](#2913-subarrays-distinct-element-sum-of-squares-i) — Easy; code: yes
- [2916. Subarrays Distinct Element Sum of Squares II](#2916-subarrays-distinct-element-sum-of-squares-ii) — Hard; code: yes
- [2921. Maximum Profitable Triplets With Increasing Prices II](#2921-maximum-profitable-triplets-with-increasing-prices-ii) — Hard; code: yes
- [3009. Maximum Number of Intersections on the Chart](#3009-maximum-number-of-intersections-on-the-chart) — Hard; code: yes
- [3042. Count Prefix and Suffix Pairs I](#3042-count-prefix-and-suffix-pairs-i) — Easy; code: yes
- [3043. Find the Length of the Longest Common Prefix](#3043-find-the-length-of-the-longest-common-prefix) — Medium; code: yes
- [3045. Count Prefix and Suffix Pairs II](#3045-count-prefix-and-suffix-pairs-ii) — Hard; code: yes
- [3072. Distribute Elements Into Two Arrays II](#3072-distribute-elements-into-two-arrays-ii) — Hard; code: yes
- [3076. Shortest Uncommon Substring in an Array](#3076-shortest-uncommon-substring-in-an-array) — Medium; code: yes
- [3093. Longest Common Suffix Queries](#3093-longest-common-suffix-queries) — Hard; code: yes
- [3187. Peaks in Array](#3187-peaks-in-array) — Hard; code: yes
- [3245. Alternating Groups III](#3245-alternating-groups-iii) — Hard; code: yes
- [3380. Maximum Area Rectangle With Point Constraints I](#3380-maximum-area-rectangle-with-point-constraints-i) — Medium; code: yes
- [3382. Maximum Area Rectangle With Point Constraints II](#3382-maximum-area-rectangle-with-point-constraints-ii) — Hard; code: yes
- [3480. Maximize Subarrays After Removing One Conflicting Pair](#3480-maximize-subarrays-after-removing-one-conflicting-pair) — Hard; code: yes
- [3485. Longest Common Prefix of K Strings After Removal](#3485-longest-common-prefix-of-k-strings-after-removal) — Hard; code: yes
- [3491. Phone Number Prefix](#3491-phone-number-prefix) — Easy; code: yes
- [3525. Find X Value of Array II](#3525-find-x-value-of-array-ii) — Hard; code: yes
- [3526. Range XOR Queries with Subarray Reversals](#3526-range-xor-queries-with-subarray-reversals) — Hard; code: yes
- [3569. Maximize Count of Distinct Primes After Split](#3569-maximize-count-of-distinct-primes-after-split) — Hard; code: yes
- [3597. Partition String ](#3597-partition-string) — Medium; code: yes
- [3624. Number of Integers With Popcount-Depth Equal to K II](#3624-number-of-integers-with-popcount-depth-equal-to-k-ii) — Hard; code: yes
- [3632. Subarrays with XOR at Least K](#3632-subarrays-with-xor-at-least-k) — Hard; code: yes
- [3671. Sum of Beautiful Subsequences](#3671-sum-of-beautiful-subsequences) — Hard; code: yes
- [3691. Maximum Total Subarray Value II](#3691-maximum-total-subarray-value-ii) — Hard; code: yes
- [3719. Longest Balanced Subarray I](#3719-longest-balanced-subarray-i) — Medium; code: yes
- [3721. Longest Balanced Subarray II](#3721-longest-balanced-subarray-ii) — Hard; code: yes
- [3737. Count Subarrays With Majority Element I](#3737-count-subarrays-with-majority-element-i) — Medium; code: yes
- [3739. Count Subarrays With Majority Element II](#3739-count-subarrays-with-majority-element-ii) — Hard; code: yes
- [3758. Convert Number Words to Digits](#3758-convert-number-words-to-digits) — Medium; code: yes
- [3777. Minimum Deletions to Make Alternating Substring](#3777-minimum-deletions-to-make-alternating-substring) — Hard; code: yes
- [3901. Good Subsequence Queries](#3901-good-subsequence-queries) — Hard; code: yes
- [3930. Power Update After K-th Largest Insertion II](#3930-power-update-after-k-th-largest-insertion-ii) — Hard; code: yes
- [3935. Power Update After K-th Largest Insertion I](#3935-power-update-after-k-th-largest-insertion-i) — Medium; code: yes
- [3962. Maximum Subarray Sum After at Most K Swaps](#3962-maximum-subarray-sum-after-at-most-k-swaps) — Hard; code: yes
- [4011. Count Subarrays With Even Odd Ratio I](#4011-count-subarrays-with-even-odd-ratio-i) — Medium; code: yes
- [4013. Count Subarrays With Even Odd Ratio II](#4013-count-subarrays-with-even-odd-ratio-ii) — Hard; code: yes
- [4017. Peaks in Array II](#4017-peaks-in-array-ii) — Hard; code: yes

---

## 14. Longest Common Prefix

**Problem:** https://leetcode.com/problems/longest-common-prefix/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Write a function to find the longest common prefix string amongst an array of strings. 
 
 If there is no common prefix, return an empty string "" . 

 Example 1: 
 
```
Input:
 strs = ["flower","flow","flight"]

Output:
 "fl"
```

 Example 2: 
 
```
Input:
 strs = ["dog","racecar","car"]

Output:
 ""

Explanation:
 There is no common prefix among the input strings.
```

 Constraints: 

 1 <= strs.length <= 200 
 
 0 <= strs[i].length <= 200 
 
 strs[i] consists of only lowercase English letters if it is non-empty.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        for (int i = 0; i < (int)strs[0].size(); ++i) {
            char c = strs[0][i];
            for (int j = 1; j < (int)strs.size(); ++j) {
                if (i >= (int)strs[j].size() || strs[j][i] != c)
                    return strs[0].substr(0, i);
            }
        }
        return strs[0];
    }
};
```


## 105. Construct Binary Tree from Preorder and Inorder Traversal

**Problem:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Divide and Conquer, Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Binary tree, Hash map / hash set, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/02/19/tree.jpg] 
 
```
Input:
 preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

Output:
 [3,9,20,null,null,15,7]
```

 Example 2: 
 
```
Input:
 preorder = [-1], inorder = [-1]

Output:
 [-1]
```

 Constraints: 

 1 <= preorder.length <= 3000 
 
 inorder.length == preorder.length 
 
 -3000 <= preorder[i], inorder[i] <= 3000 
 
 preorder and inorder consist of unique values. 
 
 Each value of inorder also appears in preorder . 
 
 preorder is guaranteed to be the preorder traversal of the tree. 
 
 inorder is guaranteed to be the inorder traversal of the tree.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution 
{
public:
    
    TreeNode* build(vector<int>& preorder, vector<int>& inorder,int preS,int preE,int inS,int inE)
    {
        if(preS>preE || inS>inE)
            return NULL;
        
        TreeNode* root=new TreeNode(preorder[preS]);
        
        int rootindex=-1;
        for(int i=inS;i<=inE;i++)
        {
            if(inorder[i]==preorder[preS])
               rootindex=i; 
        }
        
        int inSL=inS;
        int inEL=rootindex-1;
        int preSL=preS+1;
        int preEL=inEL-inSL+preSL;
        
        int preSR=preEL+1;
        int preER=preE;
        int inSR=rootindex+1;
        int inER=inE;
        
        
        root->left=build(preorder,inorder,preSL,preEL,inSL,inEL);
        root->right=build(preorder,inorder,preSR,preER,inSR,inER);
        
        return root;
        
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) 
	{ 
        int n=preorder.size();
        TreeNode* ans=build(preorder,inorder,0,n-1,0,n-1);
        return ans;
    }
};
```


## 106. Construct Binary Tree from Inorder and Postorder Traversal

**Problem:** https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Divide and Conquer, Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Binary tree, Hash map, Hash map / hash set, Ordered map, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/02/19/tree.jpg] 
 
```
Input:
 inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]

Output:
 [3,9,20,null,null,15,7]
```

 Example 2: 
 
```
Input:
 inorder = [-1], postorder = [-1]

Output:
 [-1]
```

 Constraints: 

 1 <= inorder.length <= 3000 
 
 postorder.length == inorder.length 
 
 -3000 <= inorder[i], postorder[i] <= 3000 
 
 inorder and postorder consist of unique values. 
 
 Each value of postorder also appears in inorder . 
 
 inorder is guaranteed to be the inorder traversal of the tree. 
 
 postorder is guaranteed to be the postorder traversal of the tree.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        // Map to store the index of each value in inorder traversal
        unordered_map<int, int> inorderIndexMap;
        for (int i = 0; i < inorder.size(); i++) {
            inorderIndexMap[inorder[i]] = i;
        }

        // Start building the tree
        int postIndex = postorder.size() - 1;
        return constructTree(inorder, postorder, inorderIndexMap, postIndex, 0, inorder.size() - 1);
    }

private:
    TreeNode* constructTree(const vector<int>& inorder, const vector<int>& postorder,
                            unordered_map<int, int>& inorderIndexMap, int& postIndex,
                            int inStart, int inEnd) {
        // Base case: no elements to construct the subtree
        if (inStart > inEnd) return nullptr;

        // Get the current root value and create a TreeNode
        int rootValue = postorder[postIndex--];
        TreeNode* root = new TreeNode(rootValue);

        // Find the index of the root value in the inorder array
        int rootIndex = inorderIndexMap[rootValue];

        // Recursively build the right and left subtrees
        root->right = constructTree(inorder, postorder, inorderIndexMap, postIndex, rootIndex + 1, inEnd);
        root->left = constructTree(inorder, postorder, inorderIndexMap, postIndex, inStart, rootIndex - 1);

        return root;
    }
};
```


## 108. Convert Sorted Array to Binary Search Tree

**Problem:** https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Binary tree, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array nums where the elements are sorted in ascending order , convert it to a height-balanced binary search tree . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg] 
 
```
Input:
 nums = [-10,-3,0,5,9]

Output:
 [0,-3,9,-10,null,5]

Explanation:
 [0,-10,5,null,-3,null,9] is also accepted:
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/02/18/btree.jpg] 
 
```
Input:
 nums = [1,3]

Output:
 [3,1]

Explanation:
 [1,null,3] and [3,1] are both height-balanced BSTs.
```

 Constraints: 

 1 <= nums.length <= 10 4 
 
 -10 4 <= nums[i] <= 10 4 
 
 nums is sorted in a strictly increasing order.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return helper(nums, 0, nums.size() - 1);
    }
    TreeNode* helper(vector<int>& nums, int left, int right) {
        if (left > right) return nullptr;
        int mid = left + (right - left) / 2;
        TreeNode* node = new TreeNode(nums[mid]);
        node->left = helper(nums, left, mid - 1);
        node->right = helper(nums, mid + 1, right);
        return node;
    }
};
```


## 109. Convert Sorted List to Binary Search Tree

**Problem:** https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

**Difficulty:** Medium | **Premium:** No

**Tags:** Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Sorting / Divide and Conquer, Linked List / Pointers

**Data structures (inferred):** Binary tree, Linked list, Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given the head of a singly linked list where elements are sorted in ascending order , convert it to a height-balanced binary search tree . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/08/17/linked.jpg] 
 
```
Input:
 head = [-10,-3,0,5,9]

Output:
 [0,-3,9,-10,null,5]

Explanation:
 One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
```

 Example 2: 
 
```
Input:
 head = []

Output:
 []
```

 Constraints: 

 The number of nodes in head is in the range [0, 2 * 10 4 ] . 
 
 -10 5 <= Node.val <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (!head) return nullptr;

        // Count the number of nodes in the linked list
        int size = getSize(head);

        // Use a pointer reference to simulate in-order traversal
        ListNode* current = head;
        return buildTree(current, 0, size - 1);
    }

private:
    // Helper function to count the size of the linked list
    int getSize(ListNode* head) {
        int count = 0;
        while (head) {
            ++count;
            head = head->next;
        }
        return count;
    }

    // Helper function to build the BST
    TreeNode* buildTree(ListNode*& current, int left, int right) {
        if (left > right) return nullptr;

        // Find the middle of the current range
        int mid = left + (right - left) / 2;

        // Recursively build the left subtree
        TreeNode* leftChild = buildTree(current, left, mid - 1);

        // Create the root node with the current value
        TreeNode* root = new TreeNode(current->val);
        root->left = leftChild;

        // Move to the next list node
        current = current->next;

        // Recursively build the right subtree
        root->right = buildTree(current, mid + 1, right);

        return root;
    }
};
```


## 173. Binary Search Tree Iterator

**Problem:** https://leetcode.com/problems/binary-search-tree-iterator/

**Difficulty:** Medium | **Premium:** No

**Tags:** Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Stack / Queue

**Data structures (inferred):** Binary tree, Stack, Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST): 

 BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST. 
 
 boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false . 
 
 int next() Moves the pointer to the right, then returns the number at the pointer. 

 Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST. 
 
 You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png] 
 
```
Input

["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]

Output

[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation

BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next(); // return 3
bSTIterator.next(); // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next(); // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next(); // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next(); // return 20
bSTIterator.hasNext(); // return False
```

 Constraints: 

 The number of nodes in the tree is in the range [1, 10 5 ] . 
 
 0 <= Node.val <= 10 6 
 
 At most 10 5 calls will be made to hasNext , and next . 

 Follow up: 

 Could you implement next() and hasNext() to run in average O(1) time and use  O(h) memory, where h is the height of the tree?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
 
 class BSTIterator {
private:
    stack<TreeNode*> st; // Stack to hold nodes during traversal

    // Helper function to push all left nodes onto the stack
    void pushLeft(TreeNode* node) {
        while (node) {
            st.push(node);
            node = node->left;
        }
    }

public:
    // Constructor initializes the stack with the leftmost path
    BSTIterator(TreeNode* root) {
        pushLeft(root);
    }

    // Return the next smallest number in the BST
    int next() {
        TreeNode* topNode = st.top();
        st.pop();
        if (topNode->right) {
            pushLeft(topNode->right);
        }
        return topNode->val;
    }

    // Return whether there are more nodes to traverse
    bool hasNext() {
        return !st.empty();
    }
};
```


## 208. Implement Trie (Prefix Tree)

**Problem:** https://leetcode.com/problems/implement-trie-prefix-tree/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, String, Design, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Stack / Queue

**Data structures (inferred):** Hash map, Hash map / hash set, Ordered map, String, Trie

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker. 
 
 Implement the Trie class: 

 Trie() Initializes the trie object. 
 
 void insert(String word) Inserts the string word into the trie. 
 
 boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise. 
 
 boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix , and false otherwise. 

 Example 1: 
 
```
Input

["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output

[null, null, true, false, true, null, true]

Explanation

Trie trie = new Trie();
trie.insert("apple");
trie.search("apple"); // return True
trie.search("app"); // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app"); // return True
```

 Constraints: 

 1 <= word.length, prefix.length <= 2000 
 
 word and prefix consist only of lowercase English letters. 
 
 At most 3 * 10 4 calls in total will be made to insert , search , and startsWith .

### C++ solution

**Source:** accepted_cpp_submission

```cpp

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;

    TrieNode() : isEndOfWord(false) {}
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* current = root;
        for (char ch : word) {
            if (current->children.find(ch) == current->children.end()) {
                current->children[ch] = new TrieNode();
            }
            current = current->children[ch];
        }
        current->isEndOfWord = true;
    }

    bool search(string word) {
        TrieNode* current = root;
        for (char ch : word) {
            if (current->children.find(ch) == current->children.end()) {
                return false;
            }
            current = current->children[ch];
        }
        return current->isEndOfWord;
    }

    bool startsWith(string prefix) {
        TrieNode* current = root;
        for (char ch : prefix) {
            if (current->children.find(ch) == current->children.end()) {
                return false;
            }
            current = current->children[ch];
        }
        return true;
    }
};
```


## 212. Word Search II

**Problem:** https://leetcode.com/problems/word-search-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, String, Backtracking, Trie, Matrix

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Backtracking / Bitmask, String Algorithms, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an m x n board  of characters and a list of strings words , return all words on the board . 
 
 Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/07/search1.jpg] 
 
```
Input:
 board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]

Output:
 ["eat","oath"]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/11/07/search2.jpg] 
 
```
Input:
 board = [["a","b"],["c","d"]], words = ["abcb"]

Output:
 []
```

 Constraints: 

 m == board.length 
 
 n == board[i].length 
 
 1 <= m, n <= 12 
 
 board[i][j] is a lowercase English letter. 
 
 1 <= words.length <= 3 * 10 4 
 
 1 <= words[i].length <= 10 
 
 words[i] consists of lowercase English letters. 
 
 All the strings of words are unique.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    struct TrieNode {
        TrieNode* children[26] = {nullptr};
        string word = "";
    };

    void insert(TrieNode* root, const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (!node->children[index]) 
                node->children[index] = new TrieNode();
            node = node->children[index];
        }
        node->word = word; // Store the word at the end node
    }

    void dfs(vector<vector<char>>& board, int i, int j, TrieNode* node, vector<string>& result) {
        char c = board[i][j];
        if (c == '#' || !node->children[c - 'a']) return;

        node = node->children[c - 'a'];
        if (!node->word.empty()) { // Found a word
            result.push_back(node->word);
            node->word = ""; // Avoid duplicates
        }

        board[i][j] = '#'; // Mark as visited
        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (auto& dir : dirs) {
            int x = i + dir[0], y = j + dir[1];
            if (x >= 0 && x < board.size() && y >= 0 && y < board[0].size()) {
                dfs(board, x, y, node, result);
            }
        }
        board[i][j] = c; // Restore the cell
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            insert(root, word);
        }

        vector<string> result;
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                dfs(board, i, j, root, result);
            }
        }

        return result;
    }
};
```


## 218. The Skyline Problem

**Problem:** https://leetcode.com/problems/the-skyline-problem/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Sweep Line, Sorting, Heap (Priority Queue), Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Heap / Priority Queue, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Ordered set, Priority queue / heap, Segment tree, Sorted array, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively . 
 
 The geometric information of each building is given in the array buildings where buildings[i] = [left i , right i , height i ] : 

 left i is the x coordinate of the left edge of the i th building. 
 
 right i is the x coordinate of the right edge of the i th building. 
 
 height i is the height of the i th building. 

 You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0 . 
 
 The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x 1 ,y 1 ],[x 2 ,y 2 ],...] . Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour. 
 
 Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...] 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/12/01/merged.jpg] 
 
```
Input:
 buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

Output:
 [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

Explanation:

Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
```

 Example 2: 
 
```
Input:
 buildings = [[0,2,3],[2,5,3]]

Output:
 [[0,3],[5,0]]
```

 Constraints: 

 1 <= buildings.length <= 10 4 
 
 0 <= left i < right i <= 2 31 - 1 
 
 1 <= height i <= 2 31 - 1 
 
 buildings is sorted by left i in non-decreasing order.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int>> h;
		
        // Convert each building into two segments.
        for (auto b : buildings) {
            h.push_back({b[0], -b[2]});
            h.push_back({b[1], b[2]});
        }
        
        // Sort the segments.
        sort(h.begin(), h.end());
        int prev = 0, cur = 0;
        
        multiset<int> m;
        vector<vector<int>> res;
        
        m.insert(0);
        for (auto i:h) {
            
            // If i.second is less than zero, then it means it is left boundary.
            if (i.second < 0) {
                m.insert(-i.second);
            } else { // else it is right boundary.
                m.erase(m.find(i.second));
            } 
            
            cur = *m.rbegin();
            
            // If current maximum height is not equal to maximum previuous height, it is a key point.
            if (cur != prev) {
                res.push_back({i.first, cur});
                prev = cur;
            }
        }
        return res;
}
};
```


## 307. Range Sum Query - Mutable

**Problem:** https://leetcode.com/problems/range-sum-query-mutable/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Divide and Conquer, Design, Binary Indexed Tree, Segment Tree, Sqrt Decomposition

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Sorting / Divide and Conquer, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array nums , handle multiple queries of the following types: 

 Update the value of an element in nums . 
 
 Calculate the sum of the elements of nums between indices left and right inclusive where left <= right . 

 Implement the NumArray class: 

 NumArray(int[] nums) Initializes the object with the integer array nums . 
 
 void update(int index, int val) Updates the value of nums[index] to be val . 
 
 int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right] ). 

 Example 1: 
 
```
Input

["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]

Output

[null, 9, null, 8]

Explanation

NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2); // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
```

 Constraints: 

 1 <= nums.length <= 3 * 10 4 
 
 -100 <= nums[i] <= 100 
 
 0 <= index < nums.length 
 
 -100 <= val <= 100 
 
 0 <= left <= right < nums.length 
 
 At most 3 * 10 4 calls will be made to update and sumRange .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class NumArray {
    vector<int> values, bit;
    int n;

    void add(int index, int delta) {
        for (++index; index <= n; index += index & -index)
            bit[index] += delta;
    }
    int prefixSum(int index) const {
        int result = 0;
        for (++index; index > 0; index -= index & -index)
            result += bit[index];
        return result;
    }
public:
    NumArray(vector<int>& nums)
        : values(nums), bit(nums.size() + 1, 0), n(nums.size()) {
        for (int i = 0; i < n; ++i) add(i, values[i]);
    }
    void update(int index, int val) {
        add(index, val - values[index]);
        values[index] = val;
    }
    int sumRange(int left, int right) {
        return prefixSum(right) - (left ? prefixSum(left - 1) : 0);
    }
};
```


## 308. Range Sum Query 2D - Mutable

**Problem:** https://leetcode.com/problems/range-sum-query-2d-mutable/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Design, Binary Indexed Tree, Segment Tree, Matrix, Sqrt Decomposition

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Fenwick tree, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a 2D matrix matrix , handle multiple queries of the following types: 

 Update the value of a cell in matrix . 
 
 Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2) . 

 Implement the NumMatrix class: 

 NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix . 
 
 void update(int row, int col, int val) Updates the value of matrix[row][col] to be val . 
 
 int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2) . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/03/14/summut-grid.jpg] 
 
```
Input

["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]

Output

[null, 8, null, 10]

Explanation

NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e. sum of the left red rectangle)
numMatrix.update(3, 2, 2); // matrix changes from left image to right image
numMatrix.sumRegion(2, 1, 4, 3); // return 10 (i.e. sum of the right red rectangle)
```

 Constraints: 

 m == matrix.length 
 
 n == matrix[i].length 
 
 1 <= m, n <= 200 
 
 -1000 <= matrix[i][j] <= 1000 
 
 0 <= row < m 
 
 0 <= col < n 
 
 -1000 <= val <= 1000 
 
 0 <= row1 <= row2 < m 
 
 0 <= col1 <= col2 < n 
 
 At most 5000 calls will be made to sumRegion and update .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class NumMatrix
{
    vector<vector<int>> bit, values;
    int m, n;
    void add(int r, int c, int delta)
    {
        for (int i = r + 1; i <= m; i += i & -i)
        {
            for (int j = c + 1; j <= n; j += j & -j)
            {
                bit[i][j] += delta;
            }
        }
    }
    int prefix(int r, int c) const
    {
        int result = 0;
        for (int i = r; i > 0; i -= i & -i)
        {
            for (int j = c; j > 0; j -= j & -j)
            {
                result += bit[i][j];
            }
        }
        return result;
    }
public:
    NumMatrix(vector<vector<int>>& matrix)
    {
        m = matrix.size();
        n = m ? matrix[0].size() : 0;
        bit.assign(m + 1, vector<int>(n + 1, 0));
        values.assign(m, vector<int>(n, 0));
        for (int r = 0; r < m; ++r)
        {
            for (int c = 0; c < n; ++c)
            {
                update(r, c, matrix[r][c]);
            }
        }
    }
    void update(int row, int col, int val)
    {
        int delta = val - values[row][col];
        values[row][col] = val;
        add(row, col, delta);
    }
    int sumRegion(int row1, int col1, int row2, int col2)
    {
        return prefix(row2 + 1, col2 + 1) - prefix(row1, col2 + 1)
             - prefix(row2 + 1, col1) + prefix(row1, col1);
    }
};
```


## 331. Verify Preorder Serialization of a Binary Tree

**Problem:** https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

**Difficulty:** Medium | **Premium:** No

**Tags:** String, Stack, Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms, Stack / Queue

**Data structures (inferred):** Binary tree, Stack, String, Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

One way to serialize a binary tree is to use preorder traversal . When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#' . 
 [Figure: https://assets.leetcode.com/uploads/2021/03/12/pre-tree.jpg] 
 
 For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#" , where '#' represents a null node. 
 
 Given a string of comma-separated values preorder , return true if it is a correct preorder traversal serialization of a binary tree. 
 
 It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer. 
 
 You may assume that the input format is always valid. 

 For example, it could never contain two consecutive commas, such as "1,,3" . 

 Note:  You are not allowed to reconstruct the tree. 

 Example 1: 
 
```
Input:
 preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"

Output:
 true
```
 
 Example 2: 
 
```
Input:
 preorder = "1,#"

Output:
 false
```
 
 Example 3: 
 
```
Input:
 preorder = "9,#,#,1"

Output:
 false
```

 Constraints: 

 1 <= preorder.length <= 10 4 
 
 preorder consist of integers in the range [0, 100] and '#' separated by commas ',' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    bool isValidSerialization(string preorder) {
        int slots = 1;
        int n = preorder.size();
        
        for (int i = 0; i < n; i++) {
            if (preorder[i] == ',') continue;
            if (--slots < 0) return false;
            if (preorder[i] != '#') slots += 2;
            while (i < n && preorder[i] != ',') i++;
        }
        
        return slots == 0;
    }
};
```


## 336. Palindrome Pairs

**Problem:** https://leetcode.com/problems/palindrome-pairs/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, String, Trie, Hash Function

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 0-indexed array of unique strings words . 
 
 A palindrome pair is a pair of integers (i, j) such that: 

 0 <= i, j < words.length , 
 
 i != j , and 
 
 words[i] + words[j] (the concatenation of the two strings) is a palindrome . 

 Return an array of all the palindrome pairs of words . 
 
 You must write an algorithm with  O(sum of words[i].length)  runtime complexity. 

 Example 1: 
 
```
Input:
 words = ["abcd","dcba","lls","s","sssll"]

Output:
 [[0,1],[1,0],[3,2],[2,4]]

Explanation:
 The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
```

 Example 2: 
 
```
Input:
 words = ["bat","tab","cat"]

Output:
 [[0,1],[1,0]]

Explanation:
 The palindromes are ["battab","tabbat"]
```

 Example 3: 
 
```
Input:
 words = ["a",""]

Output:
 [[0,1],[1,0]]

Explanation:
 The palindromes are ["a","a"]
```

 Constraints: 

 1 <= words.length <= 5000 
 
 0 <= words[i].length <= 300 
 
 words[i] consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#define INDEX(c) (int)c - (int)'a'
struct Node 
{
    Node* child[26];
    int end;
    vector<int> palindromes_below;
    
    Node() 
	{
        for (int i = 0; i < 26; i++) 
		{
            child[i] = NULL;
        }
        end = -1;
    }
};

class Solution 
{
    Node* root = new Node();
    
	public:
		vector<vector<int>> ans;
		bool check(const string& s, int i, int j) 
		{
			while (i < j) 
			{
				if (s[i++] != s[j--]) return false;
			}
			return true;
		}

		void insert(string& s, int ind) 
		{
			Node* temp = root;
			for (int i = s.size() - 1; i >= 0; i--) 
			{
				if (check(s, 0, i)) 
				{
					temp->palindromes_below.push_back(ind);
				}
				if (temp->child[INDEX(s[i])] == NULL) 
				{
					temp->child[INDEX(s[i])] = new Node;
				}
				temp = temp->child[INDEX(s[i])];
			}
			temp->end = ind;
			temp->palindromes_below.push_back(ind);
		}

		void search(string& s, int ind) 
		{
			Node* temp = root;
			for (int i = 0; i < s.size(); i++) 
			{
				if (temp->end != -1 && temp->end != ind && check(s, i, s.size() - 1)) 
				{
					ans.push_back({ind, temp->end});
				}
				
				if (temp->child[INDEX(s[i])] == NULL) 
					return;
				
				temp = temp->child[INDEX(s[i])];
			}
			for (int idx : temp->palindromes_below) 
			{
				if (ind != idx) ans.push_back({ind, idx});
			}
		}

		vector<vector<int>> palindromePairs(vector<string>& words) 
		{
			for (int i = 0; i < words.size(); i++) 
			{
				insert(words[i], i);
			}
			for (int i = 0; i < words.size(); i++) 
			{
				search(words[i], i);
			}
			return ans;
		}
};
```


## 406. Queue Reconstruction by Height

**Problem:** https://leetcode.com/problems/queue-reconstruction-by-height/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Binary Indexed Tree, Segment Tree, Sorting

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Segment tree, Sorted array, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array of people, people , which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [h i , k i ] represents the i th person of height h i with exactly k i other people in front who have a height greater than or equal to h i . 
 
 Reconstruct and return the queue that is represented by the input array people . The returned queue should be formatted as an array queue , where queue[j] = [h j , k j ] is the attributes of the j th person in the queue ( queue[0] is the person at the front of the queue). 

 Example 1: 
 
```
Input:
 people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

Output:
 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

Explanation:

Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
```

 Example 2: 
 
```
Input:
 people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]

Output:
 [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
```

 Constraints: 

 1 <= people.length <= 2000 
 
 0 <= h i <= 10 6 
 
 0 <= k i < people.length 
 
 It is guaranteed that the queue can be reconstructed.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        // Sort by height in descending order, and by k in ascending order if heights are equal
        sort(people.begin(), people.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] > b[0] || (a[0] == b[0] && a[1] < b[1]);
        });

        vector<vector<int>> result;
        // Insert each person at the index specified by their k value
        for (const auto& person : people) {
            result.insert(result.begin() + person[1], person);
        }

        return result;
    }
};
```


## 421. Maximum XOR of Two Numbers in an Array

**Problem:** https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Bit Manipulation, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array nums , return the maximum result of nums[i] XOR nums[j] , where 0 <= i <= j < n . 

 Example 1: 
 
```
Input:
 nums = [3,10,5,25,2,8]

Output:
 28

Explanation:
 The maximum result is 5 XOR 25 = 28.
```

 Example 2: 
 
```
Input:
 nums = [14,70,53,83,49,91,36,80,92,51,66,70]

Output:
 127
```

 Constraints: 

 1 <= nums.length <= 2 * 10 5 
 
 0 <= nums[i] <= 2 31 - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution 
{
public:
    struct trieNode 
    {
        trieNode* left = nullptr; // 0
        trieNode* right = nullptr; // 1
    };

    void insert(trieNode* root, int num) 
    {
        trieNode* pcrawl = root;

        for (int i = 31; i >= 0; i--) 
        {
            int ith_bit = (num >> i) & 1;
            if (ith_bit == 0) 
            {
                if (pcrawl->left == NULL) 
                {
                    pcrawl->left = new trieNode();
                }
                pcrawl = pcrawl->left;
            } 
			else 
            {
                if (pcrawl->right == NULL) 
                {
                    pcrawl->right = new trieNode();
                }
                pcrawl = pcrawl->right;
            }
        }
    }

    int findMaxXor(trieNode* root, int num)
    {
        int maxi = 0;
        trieNode* pcrawl = root;

        for (int i = 31; i >= 0; i--) 
        {
            int ith_bit = (num >> i) & 1;
            if (ith_bit == 1) 
            {
                if (pcrawl->left != NULL) 
                {
                    maxi += pow(2, i);
                    pcrawl = pcrawl->left;
                } 
                else 
                {
                    pcrawl = pcrawl->right;
                }
            } 
            else 
            {
                if (pcrawl->right != NULL) 
                {
                    maxi += pow(2, i);
                    pcrawl = pcrawl->right;
                } 
                else 
                {
                    pcrawl = pcrawl->left;
                }
            }
        }
        return maxi;
    }

    int findMaximumXOR(std::vector<int>& nums) 
    {
        trieNode* root = new trieNode();
        for (int& num : nums) 
        {
            insert(root, num);
        }

        int maxResult = 0;
        for (int i = 0; i < nums.size(); i++) 
        {
            int temp = findMaxXor(root, nums[i]);
            maxResult = std::max(maxResult, temp);
        }
        return maxResult;
    }
};
```


## 425. Word Squares

**Problem:** https://leetcode.com/problems/word-squares/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, String, Backtracking, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Backtracking / Bitmask, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Ordered map, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array of unique strings words , return all the word squares you can build from words . The same word from words can be used multiple times . You can return the answer in any order . 
 
 A sequence of strings forms a valid word square if the k th row and column read the same string, where 0 <= k < max(numRows, numColumns) . 

 For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically. 

 Example 1: 
 
```
Input:
 words = ["area","lead","wall","lady","ball"]

Output:
 [["ball","area","lead","lady"],["wall","area","lead","lady"]]

Explanation:

The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
```

 Example 2: 
 
```
Input:
 words = ["abat","baba","atan","atal"]

Output:
 [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]

Explanation:

The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
```

 Constraints: 

 1 <= words.length <= 1000 
 
 1 <= words[i].length <= 4 
 
 All words[i] have the same length. 
 
 words[i] consists of only lowercase English letters. 
 
 All words[i] are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution
{
    unordered_map<string, vector<string>> prefixWords;
    vector<vector<string>> result;
    vector<string> square;
    int side;
    void dfs(int depth)
    {
        if (depth == side)
        {
            result.push_back(square);
            return;
        }
        string prefix;
        for (const string& row : square) prefix += row[depth];
        auto it = prefixWords.find(prefix);
        if (it == prefixWords.end()) return;
        for (const string& candidate : it->second) {
            square.push_back(candidate);
            dfs(depth + 1);
            square.pop_back();
        }
    }
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        result.clear();
        prefixWords.clear();
        square.clear();
        if (words.empty()) return result;
        side = words[0].size();
        for (const string& word : words) {
            for (int len = 0; len < side; ++len)
            {
                prefixWords[word.substr(0, len)].push_back(word);
            }
        }
        dfs(0);
        return result;
    }
};
```


## 427. Construct Quad Tree

**Problem:** https://leetcode.com/problems/construct-quad-tree/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Divide and Conquer, Tree, Matrix

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** 2D array / matrix, Array / vector, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree. 
 
 Return the root of the Quad-Tree representing grid . 
 
 A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes: 

 val : True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer. 
 
 isLeaf : True if the node is a leaf node on the tree or False if the node has four children. 

```
class Node {
 public boolean val;
 public boolean isLeaf;
 public Node topLeft;
 public Node topRight;
 public Node bottomLeft;
 public Node bottomRight;
}
```

 We can construct a Quad-Tree from a two-dimensional area using the following steps: 

 If the current grid has the same value (i.e all 1's or all 0's ) set isLeaf True and set val to the value of the grid and set the four children to Null and stop. 
 
 If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo. 
 
 Recurse for each of the children with the proper sub-grid. 
 
 [Figure: https://assets.leetcode.com/uploads/2020/02/11/new_top.png] 
 
 If you want to know more about the Quad-Tree, you can refer to the wiki . 
 
 Quad-Tree format: 
 
 You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below. 
 
 It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val] . 
 
 If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0 . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/02/11/grid1.png] 
 
```
Input:
 grid = [[0,1],[1,0]]

Output:
 [[0,1],[1,0],[1,1],[1,1],[1,0]]

Explanation:
 The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.
```

 Example 2: 
 
 [Figure: https://assets.leetcode.com/uploads/2020/02/12/e2mat.png] 
 
```
Input:
 grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]

Output:
 [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]

Explanation:
 All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:
```

 Constraints: 

 n == grid.length == grid[i].length 
 
 n == 2 x where 0 <= x <= 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp

Node* zero = new Node(false, true);
Node* one = new Node(true, true);

class Solution {
public:
    Node* create(vector<vector<int>>& grid, int x, int y, int n) {
        if (n == 1) {
            return grid[x][y] == 1 ? one : zero;
        }
        int mid = n / 2;
        Node *topLeft = create(grid, x, y, mid);
        Node *topRight = create(grid, x, y+mid, mid);
        Node *botLeft = create(grid, x+mid, y, mid);
        Node *botRight = create(grid, x+mid, y+mid, mid);
        if (topLeft == topRight and botLeft == botRight and topLeft == botLeft) {
            return topLeft;
        }
        return new Node(false, false, topLeft, topRight, botLeft, botRight);
    }
    
    Node* construct(vector<vector<int>>& grid) {
        return create(grid, 0, 0, grid.size());    
    }
};
```


## 440. K-th Smallest in Lexicographical Order

**Problem:** https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

**Difficulty:** Hard | **Premium:** No

**Tags:** Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie

**Data structures (inferred):** Trie

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given two integers n and k , return the k th lexicographically smallest integer in the range [1, n] . 

 Example 1: 
 
```
Input:
 n = 13, k = 2

Output:
 10

Explanation:
 The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
```

 Example 2: 
 
```
Input:
 n = 1, k = 1

Output:
 1
```

 Constraints: 

 1 <= k <= n <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int findKthNumber(int n, int k) {
        int curr = 1;
        k -= 1;

        while (k > 0) {
            long steps = calcSteps(n, curr, curr + 1);
            if (steps <= k) {
                curr += 1;
                k -= steps;
            } else {
                curr *= 10;
                k -= 1;
            }
        }

        return curr;
    }

    long calcSteps(long n, long curr, long next) {
        long steps = 0;
        while (curr <= n) {
            steps += min(n + 1, next) - curr;
            curr *= 10;
            next *= 10;
        }
        return steps;
    }
};
```


## 450. Delete Node in a BST

**Problem:** https://leetcode.com/problems/delete-node-in-a-bst/

**Difficulty:** Medium | **Premium:** No

**Tags:** Tree, Binary Search Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie

**Data structures (inferred):** Binary tree, Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST . 
 
 Basically, the deletion can be divided into two stages: 

 Search for a node to remove. 
 
 If the node is found, delete the node. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg] 
 
```
Input:
 root = [5,3,6,2,4,null,7], key = 3

Output:
 [5,4,6,2,null,null,7]

Explanation:
 Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
```

 Example 2: 
 
```
Input:
 root = [5,3,6,2,4,null,7], key = 0

Output:
 [5,3,6,2,4,null,7]

Explanation:
 The tree does not contain a node with value = 0.
```

 Example 3: 
 
```
Input:
 root = [], key = 0

Output:
 []
```

 Constraints: 

 The number of nodes in the tree is in the range [0, 10 4 ] . 
 
 -10 5 <= Node.val <= 10 5 
 
 Each node has a unique value. 
 
 root is a valid binary search tree. 
 
 -10 5 <= key <= 10 5 

 Follow up: Could you solve it with time complexity O(height of tree) ?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr; // Base case: Node not found
        if (key < root->val) {
            root->left = deleteNode(root->left, key); // Search in left subtree
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key); // Search in right subtree
        } else {
            // Node found
            if (!root->left) return root->right; // No left child
            if (!root->right) return root->left; // No right child

            // Node with two children: Replace with inorder successor
            TreeNode* minNode = getMin(root->right);
            root->val = minNode->val;
            root->right = deleteNode(root->right, minNode->val); // Delete the successor
        }
        return root;
    }

private:
    TreeNode* getMin(TreeNode* node) {
        while (node->left) node = node->left;
        return node; // Find the leftmost (smallest) node
    }
};
```


## 510. Inorder Successor in BST II

**Problem:** https://leetcode.com/problems/inorder-successor-in-bst-ii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Tree, Binary Search Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie

**Data structures (inferred):** Binary tree, Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a node in a binary search tree, return the in-order successor of that node in the BST . If that node has no in-order successor, return null . 
 
 The successor of a node is the node with the smallest key greater than node.val . 
 
 You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node : 
 
```
class Node {
 public int val;
 public Node left;
 public Node right;
 public Node parent;
}
```

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2019/01/23/285_example_1.PNG] 
 
```
Input:
 tree = [2,1,3], node = 1

Output:
 2

Explanation:
 1's in-order successor node is 2. Note that both the node and the return value is of Node type.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2019/01/23/285_example_2.PNG] 
 
```
Input:
 tree = [5,3,6,2,4,null,null,1], node = 6

Output:
 null

Explanation:
 There is no in-order successor of the current node, so the answer is null.
```

 Constraints: 

 The number of nodes in the tree is in the range [1, 10 4 ] . 
 
 -10 5 <= Node.val <= 10 5 
 
 All Nodes will have unique values. 

 Follow up: Could you solve it without looking up any of the node's values?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    Node* inorderSuccessor(Node* node) {
        if (node->right) {
            node = node->right;
            while (node->left) {
                node = node->left;
            }
            return node;
        }
        while (node->parent && node == node->parent->right) {
            node = node->parent;
        }
        return node->parent;
    }
};
```


## 527. Word Abbreviation

**Problem:** https://leetcode.com/problems/word-abbreviation/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, String, Greedy, Trie, Sorting

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Greedy / Intervals, String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Ordered map, Sorted array, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array of distinct strings words , return the minimal possible abbreviations for every word . 
 
 The following are the rules for a string abbreviation: 

 The initial abbreviation for each word is: the first character, then the number of characters in between, followed by the last character. 
 
 If more than one word shares the same abbreviation, then perform the following operation:

 Increase the prefix (characters in the first part) of each of their abbreviations by 1 .

 For example, say you start with the words ["abcdef","abndef"] both initially abbreviated as "a4f" . Then, a sequence of operations would be ["a4f","a4f"] -> ["ab3f","ab3f"] -> ["abc2f","abn2f"] . 

 This operation is repeated until every abbreviation is unique . 

 At the end, if an abbreviation did not make a word shorter, then keep it as the original word. 

 Example 1: 
 
```
Input:
 words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]

Output:
 ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
```
 
 Example 2: 
 
```
Input:
 words = ["aa","aaa"]

Output:
 ["aa","aaa"]
```

 Constraints: 

 1 <= words.length <= 400 
 
 2 <= words[i].length <= 400 
 
 words[i] consists of lowercase English letters. 
 
 All the strings of words are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    string abbreviate(const string& word, int prefix) {
        int remaining = static_cast<int>(word.size()) - prefix - 1;
        if (remaining <= 1) {
            return word;
        }
        return word.substr(0, prefix) + to_string(remaining) + word.back();
    }

public:
    vector<string> wordsAbbreviation(vector<string>& words) {
        int n = words.size();
        vector<int> prefix(n, 1);
        vector<string> result(n);
        while (true) {
            unordered_map<string, vector<int>> groups;
            for (int i = 0; i < n; ++i) {
                result[i] = abbreviate(words[i], prefix[i]);
                groups[result[i]].push_back(i);
            }
            bool changed = false;
            for (const auto& group : groups) {
                if (group.second.size() > 1) {
                    for (int index : group.second) {
                        ++prefix[index];
                        changed = true;
                    }
                }
            }
            if (!changed) {
                return result;
            }
        }
    }
};
```


## 558. Logical OR of Two Binary Grids Represented as Quad-Trees

**Problem:** https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

**Difficulty:** Medium | **Premium:** No

**Tags:** Divide and Conquer, Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Sorting / Divide and Conquer

**Data structures (inferred):** Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A Binary Matrix is a matrix in which all the elements are either 0 or 1 . 
 
 Given quadTree1 and quadTree2 . quadTree1 represents a n * n binary matrix and quadTree2 represents another n * n binary matrix. 
 
 Return a Quad-Tree representing the n * n binary matrix which is the result of logical bitwise OR of the two binary matrixes represented by quadTree1 and quadTree2 . 
 
 Notice that you can assign the value of a node to True or False when isLeaf is False , and both are accepted in the answer. 
 
 A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes: 

 val : True if the node represents a grid of 1's or False if the node represents a grid of 0's. 
 
 isLeaf : True if the node is leaf node on the tree or False if the node has the four children. 

```
class Node {
 public boolean val;
 public boolean isLeaf;
 public Node topLeft;
 public Node topRight;
 public Node bottomLeft;
 public Node bottomRight;
}
```

 We can construct a Quad-Tree from a two-dimensional area using the following steps: 

 If the current grid has the same value (i.e all 1's or all 0's ) set isLeaf True and set val to the value of the grid and set the four children to Null and stop. 
 
 If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo. 
 
 Recurse for each of the children with the proper sub-grid. 
 
 [Figure: https://assets.leetcode.com/uploads/2020/02/11/new_top.png] 
 
 If you want to know more about the Quad-Tree, you can refer to the wiki . 
 
 Quad-Tree format: 
 
 The input/output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below. 
 
 It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val] . 
 
 If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0 . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/02/11/qt1.png] [Figure: https://assets.leetcode.com/uploads/2020/02/11/qt2.png] 
 
```
Input:
 quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
, quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]

Output:
 [[0,0],[1,1],[1,1],[1,1],[1,0]]

Explanation:
 quadTree1 and quadTree2 are shown above. You can see the binary matrix which is represented by each Quad-Tree.
If we apply logical bitwise OR on the two binary matrices we get the binary matrix below which is represented by the result Quad-Tree.
Notice that the binary matrices shown are only for illustration, you don't have to construct the binary matrix to get the result tree.
```

 Example 2: 
 
```
Input:
 quadTree1 = [[1,0]], quadTree2 = [[1,0]]

Output:
 [[1,0]]

Explanation:
 Each tree represents a binary matrix of size 1*1. Each matrix contains only zero.
The resulting matrix is of size 1*1 with also zero.
```

 Constraints: 

 quadTree1 and quadTree2 are both valid Quad-Trees each representing a n * n grid. 
 
 n == 2 x where 0 <= x <= 9 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    Node* intersect(Node* a, Node* b) {
        if (a->isLeaf) return a->val ? a : b;
        if (b->isLeaf) return b->val ? b : a;
        Node* tl = intersect(a->topLeft, b->topLeft);
        Node* tr = intersect(a->topRight, b->topRight);
        Node* bl = intersect(a->bottomLeft, b->bottomLeft);
        Node* br = intersect(a->bottomRight, b->bottomRight);
        if (tl->isLeaf && tr->isLeaf && bl->isLeaf && br->isLeaf &&
            tl->val == tr->val && tl->val == bl->val && tl->val == br->val)
            return new Node(tl->val, true);
        return new Node(false, false, tl, tr, bl, br);
    }
};
```


## 588. Design In-Memory File System

**Problem:** https://leetcode.com/problems/design-in-memory-file-system/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Hash Table, String, Design, Trie, Sorting

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Sorting / Divide and Conquer, Stack / Queue

**Data structures (inferred):** Hash map / hash set, Ordered map, Sorted array, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Design a data structure that simulates an in-memory file system. 
 
 Implement the FileSystem class: 

 FileSystem() Initializes the object of the system. 
 
 List<String> ls(String path) 

 If path is a file path, returns a list that only contains this file's name. 
 
 If path is a directory path, returns the list of file and directory names in this directory . 
 
 The answer should in lexicographic order . 
 
 void mkdir(String path) Makes a new directory according to the given path . The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well. 
 
 void addContentToFile(String filePath, String content) 

 If filePath does not exist, creates that file containing given content . 
 
 If filePath already exists, appends the given content to original content. 

 String readContentFromFile(String filePath) Returns the content in the file at filePath . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/04/28/filesystem.png] 
 
```
Input

["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]

Output

[null, [], null, null, ["a"], "hello"]

Explanation

FileSystem fileSystem = new FileSystem();
fileSystem.ls("/"); // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/"); // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
```

 Constraints: 

 1 <= path.length, filePath.length <= 100 
 
 path and filePath  are absolute paths which begin with '/'  and do not end with '/'  except that the path is just  "/" . 
 
 You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory. 
 
 You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist. 
 
 You can assume that the parent directory for the file in addContentToFile will exist. 
 
 1 <= content.length <= 50 
 
 At most 300 calls will be made to ls , mkdir ,  addContentToFile , and  readContentFromFile .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class FileSystem {
    struct Entry {
        map<string, unique_ptr<Entry>> children;
        string content;
        bool file = false;
    };
    Entry root;

    vector<string> parts(const string& path) {
        vector<string> result;
        stringstream in(path);
        string segment;
        while (getline(in, segment, '/')) {
            if (!segment.empty()) {
                result.push_back(segment);
            }
        }
        return result;
    }

    Entry* walk(const string& path) {
        Entry* node = &root;
        for (const string& part : parts(path)) {
            if (!node->children.count(part)) {
                node->children[part].reset(new Entry());
            }
            node = node->children[part].get();
        }
        return node;
    }

public:
    vector<string> ls(string path) {
        Entry* node = walk(path);
        if (node->file) {
            vector<string> p = parts(path);
            return {p.back()};
        }
        vector<string> names;
        for (const auto& child : node->children) {
            names.push_back(child.first);
        }
        return names;
    }

    void mkdir(string path) {
        walk(path);
    }

    void addContentToFile(string filePath, string content) {
        Entry* node = walk(filePath);
        node->file = true;
        node->content += content;
    }

    string readContentFromFile(string filePath) {
        return walk(filePath)->content;
    }
};
```


## 616. Add Bold Tag in String

**Problem:** https://leetcode.com/problems/add-bold-tag-in-string/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Hash Table, String, Trie, String Matching, Aho–Corasick Algorithm

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string s and an array of strings words . 
 
 You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words . 

 If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag. 
 
 If two substrings wrapped by bold tags are consecutive, you should combine them. 

 Return s after adding the bold tags . 

 Example 1: 
 
```
Input:
 s = "abcxyz123", words = ["abc","123"]

Output:
 "<b>abc</b>xyz<b>123</b>"

Explanation:
 The two strings of words are substrings of s as following: "
abc
xyz
123
".
We add <b> before each substring and </b> after each substring.
```

 Example 2: 
 
```
Input:
 s = "aaabbb", words = ["aa","b"]

Output:
 "<b>aaabbb</b>"

Explanation:
 
"aa" appears as a substring two times: "
aa
abbb" and "a
aa
bbb".
"b" appears as a substring three times: "aaa
b
bb", "aaab
b
b", and "aaabb
b
".
We add <b> before each substring and </b> after each substring: "<b>a<b>a</b>a</b><b>b</b><b>b</b><b>b</b>".
Since the first two <b>'s overlap, we merge them: "<b>aaa</b><b>b</b><b>b</b><b>b</b>".
Since now the four <b>'s are consecutive, we merge them: "<b>aaabbb</b>".
```

 Constraints: 

 1 <= s.length <= 1000 
 
 0 <= words.length <= 100 
 
 1 <= words[i].length <= 1000 
 
 s and words[i] consist of English letters and digits. 
 
 All the values of words are unique . 

 Note: This question is the same as 758. Bold Words in String .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string addBoldTag(string s, vector<string>& dict) {
        int n = s.size();
        vector<bool> bold(n, false);
        for (const string& word : dict) {
            if (word.empty()) {
                continue;
            }
            size_t position = s.find(word);
            while (position != string::npos) {
                for (size_t j = position; j < position + word.size(); ++j) {
                    bold[j] = true;
                }
                position = s.find(word, position + 1);
            }
        }
        string result;
        for (int i = 0; i < n;) {
            if (!bold[i]) {
                result += s[i++];
                continue;
            }
            result += "<b>";
            while (i < n && bold[i]) {
                result += s[i++];
            }
            result += "</b>";
        }
        return result;
    }
};
```


## 648. Replace Words

**Problem:** https://leetcode.com/problems/replace-words/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, String, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

In English, we have a concept called root , which can be followed by some other word to form another longer word - let's call this word derivative . For example, when the root "help" is followed by the word "ful" , we can form a derivative "helpful" . 
 
 Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root , replace it with the root that has the shortest length . 
 
 Return the sentence after the replacement. 

 Example 1: 
 
```
Input:
 dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"

Output:
 "the cat was rat by the bat"
```

 Example 2: 
 
```
Input:
 dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"

Output:
 "a a b c"
```

 Constraints: 

 1 <= dictionary.length <= 1000 
 
 1 <= dictionary[i].length <= 100 
 
 dictionary[i] consists of only lower-case letters. 
 
 1 <= sentence.length <= 10 6 
 
 sentence consists of only lower-case letters and spaces. 
 
 The number of words in sentence is in the range [1, 1000] 
 
 The length of each word in sentence is in the range [1, 1000] 
 
 Every two consecutive words in sentence will be separated by exactly one space. 
 
 sentence does not have leading or trailing spaces.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    string word;
};

class Solution {
public:
    void insert(TrieNode* root, string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->word = word;
    }

    string replaceWords(vector<string>& dictionary, string sentence) {
        TrieNode* root = new TrieNode();
        for (string& word : dictionary) {
            insert(root, word);
        }

        stringstream ss(sentence);
        string word, result = "";
        while (ss >> word) {
            TrieNode* node = root;
            for (char c : word) {
                if (!node->children.count(c) || !node->word.empty()) break;
                node = node->children[c];
            }
            result += (node->word.empty() ? word : node->word) + " ";
        }
        result.pop_back();
        return result;
    }
};
```


## 677. Map Sum Pairs

**Problem:** https://leetcode.com/problems/map-sum-pairs/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, String, Design, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Stack / Queue

**Data structures (inferred):** Hash map, Hash map / hash set, Ordered map, String, Trie

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Design a map that allows you to do the following: 

 Maps a string key to a given value. 
 
 Returns the sum of the values that have a key with a prefix equal to a given string. 

 Implement the MapSum class: 

 MapSum() Initializes the MapSum object. 
 
 void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one. 
 
 int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix . 

 Example 1: 
 
```
Input

["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]

Output

[null, null, 3, null, 5]

Explanation

MapSum mapSum = new MapSum();
mapSum.insert("apple", 3); 
mapSum.sum("ap"); // return 3 (
ap
ple = 3)
mapSum.insert("app", 2); 
mapSum.sum("ap"); // return 5 (
ap
ple + 
ap
p = 3 + 2 = 5)
```

 Constraints: 

 1 <= key.length, prefix.length <= 50 
 
 key and prefix consist of only lowercase English letters. 
 
 1 <= val <= 1000 
 
 At most 50 calls will be made to insert and sum .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <unordered_map>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    int value = 0;
};

class MapSum {
private:
    TrieNode* root;
    unordered_map<string, int> keyMap;

public:
    MapSum() {
        root = new TrieNode();
    }

    void insert(string key, int val) {
        int delta = val - keyMap[key];
        keyMap[key] = val;
        TrieNode* node = root;
        for (char ch : key) {
            if (!node->children.count(ch)) {
                node->children[ch] = new TrieNode();
            }
            node = node->children[ch];
            node->value += delta;
        }
    }

    int sum(string prefix) {
        TrieNode* node = root;
        for (char ch : prefix) {
            if (!node->children.count(ch)) {
                return 0;
            }
            node = node->children[ch];
        }
        return node->value;
    }
};
```


## 692. Top K Frequent Words

**Problem:** https://leetcode.com/problems/top-k-frequent-words/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, String, Trie, Sorting, Heap (Priority Queue), Bucket Sort, Counting

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Heap / Priority Queue, Hashing / Frequency Counting, String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, Priority queue, Priority queue / heap, Queue, Sorted array, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array of strings words and an integer k , return the k most frequent strings . 
 
 Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order . 

 Example 1: 
 
```
Input:
 words = ["i","love","leetcode","i","love","coding"], k = 2

Output:
 ["i","love"]

Explanation:
 "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
```

 Example 2: 
 
```
Input:
 words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4

Output:
 ["the","is","sunny","day"]

Explanation:
 "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
```

 Constraints: 

 1 <= words.length <= 500 
 
 1 <= words[i].length <= 10 
 
 words[i] consists of lowercase English letters. 
 
 k is in the range [1, The number of unique words[i]] 

 Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        // Step 1: Count the frequency of each word
        unordered_map<string, int> frequency;
        for (const string& word : words) {
            frequency[word]++;
        }

        // Step 2: Use a min-heap to store the top k frequent words
        auto cmp = [](const pair<string, int>& a, const pair<string, int>& b) {
            return a.second > b.second || (a.second == b.second && a.first < b.first);
        };

        priority_queue<pair<string, int>, vector<pair<string, int>>, decltype(cmp)> minHeap(cmp);

        for (const auto& [word, count] : frequency) {
            minHeap.push({word, count});
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }

        // Step 3: Extract the words from the heap into a vector
        vector<string> result;
        while (!minHeap.empty()) {
            result.push_back(minHeap.top().first);
            minHeap.pop();
        }

        // Step 4: Reverse the vector since the heap gives the least frequent words first
        reverse(result.begin(), result.end());

        return result;
    }
};
```


## 699. Falling Squares

**Problem:** https://leetcode.com/problems/falling-squares/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Segment Tree, Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There are several squares being dropped onto the X-axis of a 2D plane. 
 
 You are given a 2D integer array positions where positions[i] = [left i , sideLength i ] represents the i th square with a side length of sideLength i that is dropped with its left edge aligned with X-coordinate left i . 
 
 Each square is dropped one at a time from a height above any landed squares. It then falls downward (negative Y direction) until it either lands on the top side of another square or on the X-axis . A square brushing the left/right side of another square does not count as landing on it. Once it lands, it freezes in place and cannot be moved. 
 
 After each square is dropped, you must record the height of the current tallest stack of squares . 
 
 Return an integer array ans where ans[i] represents the height described above after dropping the i th square . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/04/28/fallingsq1-plane.jpg] 
 
```
Input:
 positions = [[1,2],[2,3],[6,1]]

Output:
 [2,5,5]

Explanation:

After the first drop, the tallest stack is square 1 with a height of 2.
After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
After the third drop, the tallest stack is still squares 1 and 2 with a height of 5.
Thus, we return an answer of [2, 5, 5].
```

 Example 2: 
 
```
Input:
 positions = [[100,100],[200,100]]

Output:
 [100,100]

Explanation:

After the first drop, the tallest stack is square 1 with a height of 100.
After the second drop, the tallest stack is either square 1 or square 2, both with heights of 100.
Thus, we return an answer of [100, 100].
Note that square 2 only brushes the right side of square 1, which does not count as landing on it.
```

 Constraints: 

 1 <= positions.length <= 1000 
 
 1 <= left i <= 10 8 
 
 1 <= sideLength i <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    map < long long , long long > segment;
    map < long long , long long > lazy;
void lazy_prog ( long long seed , long long low , long long high )
{
    if ( lazy[seed] )
    {
        segment[seed] = lazy[seed];
        if ( low != high )
        {
            lazy[seed*2+1] = lazy[seed];
            lazy[seed*2+2] = lazy[seed];
        }
        lazy[seed] = 0;
        
    }
}
long long findhighest ( long long seed , long long blow , long long bhigh , long long low , long long high )
{
    lazy_prog ( seed , blow , bhigh );
    if ( blow >= low && bhigh <= high ) return segment[seed];
    if ( blow > high || bhigh < low ) return 0;
    long long mid = ( blow + bhigh ) / 2;
    return max ( findhighest( seed*2 + 1 , blow , mid , low , high )
                , findhighest ( seed*2 + 2 , mid + 1, bhigh , low , high ) );
}
void add ( long long seed , long long blow , long long bhigh , long long low , long long high , long long key )
{
    lazy_prog ( seed , blow , bhigh );
    if ( blow >= low && bhigh <= high ){
        segment[seed] = key;
        lazy[seed] = key;
        return;
    }
    if ( blow > high || bhigh < low ) return;
    
    long long mid = ( blow + bhigh ) / 2;
    add ( seed*2 + 1 , blow , mid , low , high , key );
    add ( seed*2 + 2 , mid + 1 , bhigh , low , high , key );
    segment[seed] = max(segment[seed*2+1] , segment[seed*2+2] );
}
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        vector < int > result ;
        long long l , r, height;
        for ( int i = 0 ; i < positions.size() ; i ++ )
        {
            for ( int j = 0 ; j < 2 ; j ++ )
            {
                if ( j == 0 ) l = positions[i][j];
                else {
                    r = l + positions[i][j] - 1;
                    height = positions[i][j];
                }
            }
            long long highest = findhighest ( 0 , 0 , 101000005, l , r );
            add ( 0 , 0 , 101000005, l , r, highest + height );
            result.push_back(segment[0]);
        }
        return result ;
    }
};
```


## 700. Search in a Binary Search Tree

**Problem:** https://leetcode.com/problems/search-in-a-binary-search-tree/

**Difficulty:** Easy | **Premium:** No

**Tags:** Tree, Binary Search Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie

**Data structures (inferred):** Binary tree, Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given the root of a binary search tree (BST) and an integer val . 
 
 Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg] 
 
```
Input:
 root = [4,2,7,1,3], val = 2

Output:
 [2,1,3]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg] 
 
```
Input:
 root = [4,2,7,1,3], val = 5

Output:
 []
```

 Constraints: 

 The number of nodes in the tree is in the range [1, 5000] . 
 
 1 <= Node.val <= 10 7 
 
 root is a binary search tree. 
 
 1 <= val <= 10 7

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root || root->val == val) return root;
        return val < root->val ? searchBST(root->left, val) : searchBST(root->right, val);
    }
};
```


## 701. Insert into a Binary Search Tree

**Problem:** https://leetcode.com/problems/insert-into-a-binary-search-tree/

**Difficulty:** Medium | **Premium:** No

**Tags:** Tree, Binary Search Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie

**Data structures (inferred):** Binary tree, Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion . It is guaranteed that the new value does not exist in the original BST. 
 
 Notice  that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg] 
 
```
Input:
 root = [4,2,7,1,3], val = 5

Output:
 [4,2,7,1,3,5]

Explanation:
 Another accepted tree is:
```

 Example 2: 
 
```
Input:
 root = [40,20,60,10,30,50,70], val = 25

Output:
 [40,20,60,10,30,50,70,null,null,25]
```

 Example 3: 
 
```
Input:
 root = [4,2,7,1,3,null,null,null,null,null,null], val = 5

Output:
 [4,2,7,1,3,5]
```

 Constraints: 

 The number of nodes in the tree will be in the range [0, 10 4 ] . 
 
 -10 8 <= Node.val <= 10 8 
 
 All the values Node.val are unique . 
 
 -10 8 <= val <= 10 8 
 
 It's guaranteed that val does not exist in the original BST.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution 
{
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) 
    {
        if(root == NULL)
        {
            return new TreeNode(val) ;
        }
        else if(root->val == val)
        {
            return root ;
        }
        else if(root->val < val)
        {
            root->right = insertIntoBST(root->right , val) ;
        }
        else
        {
            root->left = insertIntoBST(root->left , val) ;
        }
        return root ;
    }
};
```


## 703. Kth Largest Element in a Stream

**Problem:** https://leetcode.com/problems/kth-largest-element-in-a-stream/

**Difficulty:** Easy | **Premium:** No

**Tags:** Tree, Design, Binary Search Tree, Heap (Priority Queue), Binary Tree, Data Stream

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Heap / Priority Queue, Stack / Queue

**Data structures (inferred):** Binary tree, Priority queue, Priority queue / heap, Queue, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores. 
 
 You are tasked to implement a class which, for a given integer  k , maintains a stream of test scores and continuously returns the  k th highest test score  after  a new score has been submitted. More specifically, we are looking for the k th highest score in the sorted list of all scores. 
 
 Implement the  KthLargest class: 

 KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores  nums . 
 
 int add(int val) Adds a new test score  val to the stream and returns the element representing the k th largest element in the pool of test scores so far. 

 Example 1: 

 Input: 
 ["KthLargest", "add", "add", "add", "add", "add"] 
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]] 
 
 Output: [null, 4, 5, 5, 8, 8] 
 
 Explanation: 
 
 KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]); 
kthLargest.add(3); // return 4 
kthLargest.add(5); // return 5 
kthLargest.add(10); // return 5 
kthLargest.add(9); // return 8 
kthLargest.add(4); // return 8 

 Example 2: 

 Input: 
 ["KthLargest", "add", "add", "add", "add"] 
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]] 
 
 Output: [null, 7, 7, 7, 8] 
 
 Explanation: 
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]); 
kthLargest.add(2); // return 7 
kthLargest.add(10); // return 7 
kthLargest.add(9); // return 7 
kthLargest.add(9); // return 8 

 Constraints: 

 0 <= nums.length <= 10 4 
 
 1 <= k <= nums.length + 1 
 
 -10 4 <= nums[i] <= 10 4 
 
 -10 4 <= val <= 10 4 
 
 At most 10 4 calls will be made to add .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class KthLargest {
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int K;
public:
    KthLargest(int k, vector<int>& nums) {
        K = k;
        for (int num : nums) add(num);
    }
    int add(int val) {
        minHeap.push(val);
        if (minHeap.size() > K) minHeap.pop();
        return minHeap.top();
    }
};
```


## 715. Range Module

**Problem:** https://leetcode.com/problems/range-module/

**Difficulty:** Hard | **Premium:** No

**Tags:** Design, Segment Tree, Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Stack / Queue

**Data structures (inferred):** Ordered set, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them. 
 
 A half-open interval [left, right) denotes all the real numbers x where left <= x < right . 
 
 Implement the RangeModule class: 

 RangeModule() Initializes the object of the data structure. 
 
 void addRange(int left, int right) Adds the half-open interval [left, right) , tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked. 
 
 boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise. 
 
 void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right) . 

 Example 1: 
 
```
Input

["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]

Output

[null, null, null, true, false, true]

Explanation

RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
```

 Constraints: 

 1 <= left < right <= 10 9 
 
 At most 10 4 calls will be made to addRange , queryRange , and removeRange .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <set>

using namespace std;

class RangeModule {
    set<pair<int, int>> intervals;

public:
    void addRange(int left, int right) {
        auto it = intervals.lower_bound({left, 0});
        if (it != intervals.begin()) --it;
        while (it != intervals.end() && it->first <= right) {
            if (it->second < left) ++it;
            else {
                left = min(left, it->first);
                right = max(right, it->second);
                it = intervals.erase(it);
            }
        }
        intervals.insert({left, right});
    }

    bool queryRange(int left, int right) {
        auto it = intervals.upper_bound({left, INT_MAX});
        if (it == intervals.begin()) return false;
        --it;
        return it->first <= left && it->second >= right;
    }

    void removeRange(int left, int right) {
        auto it = intervals.lower_bound({left, 0});
        if (it != intervals.begin()) --it;
        vector<pair<int, int>> toAdd;
        while (it != intervals.end() && it->first < right) {
            if (it->second <= left) {
                ++it;
                continue;
            }
            if (it->first < left) toAdd.emplace_back(it->first, left);
            if (it->second > right) toAdd.emplace_back(right, it->second);
            it = intervals.erase(it);
        }
        for (auto& p : toAdd) intervals.insert(p);
    }
};
```


## 720. Longest Word in Dictionary

**Problem:** https://leetcode.com/problems/longest-word-in-dictionary/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, String, Trie, Sorting

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Hash set, Queue, Sorted array, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words . 
 
 If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string. 
 
 Note that the word should be built from left to right with each additional character being added to the end of a previous word.  

 Example 1: 
 
```
Input:
 words = ["w","wo","wor","worl","world"]

Output:
 "world"

Explanation:
 The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
```

 Example 2: 
 
```
Input:
 words = ["a","banana","app","appl","ap","apply","apple"]

Output:
 "apple"

Explanation:
 Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
```

 Constraints: 

 1 <= words.length <= 1000 
 
 1 <= words[i].length <= 30 
 
 words[i] consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <string>
#include <unordered_set>
#include <queue>
using namespace std;

class TrieNode {
public:
    TrieNode* children[26] = {};
    bool isEnd = false;
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            TrieNode* node = root;
            for (char ch : word) {
                if (!node->children[ch - 'a']) {
                    node->children[ch - 'a'] = new TrieNode();
                }
                node = node->children[ch - 'a'];
            }
            node->isEnd = true;
        }

        queue<pair<TrieNode*, string>> q;
        q.push({root, ""});
        string result = "";

        while (!q.empty()) {
            auto [node, word] = q.front();
            q.pop();
            for (int i = 0; i < 26; i++) {
                if (node->children[i] && node->children[i]->isEnd) {
                    string nextWord = word + char(i + 'a');
                    q.push({node->children[i], nextWord});
                    if (nextWord.size() > result.size() || (nextWord.size() == result.size() && nextWord < result)) {
                        result = nextWord;
                    }
                }
            }
        }
        return result;
    }
};
```


## 745. Prefix and Suffix Search

**Problem:** https://leetcode.com/problems/prefix-and-suffix-search/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, String, Design, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Design a special dictionary that searches the words in it by a prefix and a suffix. 
 
 Implement the WordFilter class: 

 WordFilter(string[] words) Initializes the object with the words in the dictionary. 
 
 f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff . If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1 . 

 Example 1: 
 
```
Input

["WordFilter", "f"]
[[["apple"]], ["a", "e"]]

Output

[null, 0]

Explanation

WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
```

 Constraints: 

 1 <= words.length <= 10 4 
 
 1 <= words[i].length <= 7 
 
 1 <= pref.length, suff.length <= 7 
 
 words[i] , pref and suff consist of lowercase English letters only. 
 
 At most 10 4 calls will be made to the function f .

### C++ solution

**Source:** accepted_cpp_submission

```cpp

#include <vector>
#include <unordered_map>
using namespace std;

class WordFilter {
    unordered_map<string, int> prefixSuffixMap;
    
public:
    WordFilter(vector<string>& words) {
        for (int i = 0; i < words.size(); ++i) {
            for (int j = 0; j <= words[i].size(); ++j) {
                for (int k = 0; k <= words[i].size(); ++k) {
                    prefixSuffixMap[words[i].substr(0, j) + "-" + words[i].substr(words[i].size() - k)] = i;
                }
            }
        }
    }

    int f(string prefix, string suffix) {
        string key = prefix + "-" + suffix;
        if (prefixSuffixMap.count(key)) return prefixSuffixMap[key];
        return -1;
    }
};
```


## 758. Bold Words in String

**Problem:** https://leetcode.com/problems/bold-words-in-string/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Hash Table, String, Trie, String Matching, Aho–Corasick Algorithm

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array of keywords words and a string s , make all appearances of all keywords words[i] in s bold. Any letters between <b> and </b> tags become bold. 
 
 Return s after adding the bold tags . The returned string should use the least number of tags possible, and the tags should form a valid combination. 

 Example 1: 
 
```
Input:
 words = ["ab","bc"], s = "aabcd"

Output:
 "a<b>abc</b>d"

Explanation:
 Note that returning 
"a<b>a<b>b</b>c</b>d"
 would use more tags, so it is incorrect.
```

 Example 2: 
 
```
Input:
 words = ["ab","cb"], s = "aabcd"

Output:
 "a<b>ab</b>cd"
```

 Constraints: 

 1 <= s.length <= 500 
 
 0 <= words.length <= 50 
 
 1 <= words[i].length <= 10 
 
 s and words[i] consist of lowercase English letters. 

 Note: This question is the same as 616. Add Bold Tag in String .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string boldWords(vector<string>& words, string s) {
        int n = s.size();
        vector<bool> bold(n, false);
        for (const string& word : words) {
            size_t pos = s.find(word);
            while (pos != string::npos) {
                for (size_t i = pos; i < pos + word.size(); ++i) {
                    bold[i] = true;
                }
                pos = s.find(word, pos + 1);
            }
        }
        string answer;
        for (int i = 0; i < n;) {
            if (!bold[i]) {
                answer += s[i++];
                continue;
            }
            answer += "<b>";
            while (i < n && bold[i]) {
                answer += s[i++];
            }
            answer += "</b>";
        }
        return answer;
    }
};
```


## 776. Split BST

**Problem:** https://leetcode.com/problems/split-bst/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Tree, Binary Search Tree, Recursion, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie

**Data structures (inferred):** Binary tree, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given the root of a binary search tree (BST) and an integer target , split the tree into two subtrees where the first subtree has nodes that are all smaller or equal to the target value, while the second subtree has all nodes that are greater than the target value. It is not necessarily the case that the tree contains a node with the value target . 
 
 Additionally, most of the structure of the original tree should remain. Formally, for any child c with parent p in the original tree, if they are both in the same subtree after the split, then node c should still have the parent p . 
 
 Return an array of the two roots of the two subtrees in order . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/06/13/split-tree.jpg] 
 
```
Input:
 root = [4,2,6,1,3,5,7], target = 2

Output:
 [[2,1],[4,3,6,null,null,5,7]]
```

 Example 2: 
 
```
Input:
 root = [1], target = 1

Output:
 [[1],[]]
```

 Constraints: 

 The number of nodes in the tree is in the range [1, 50] . 
 
 0 <= Node.val, target <= 1000

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<TreeNode*> splitBST(TreeNode* root, int target) {
        if (!root) {
            return {nullptr, nullptr};
        }
        if (root->val <= target) {
            vector<TreeNode*> parts = splitBST(root->right, target);
            root->right = parts[0];
            return {root, parts[1]};
        }
        vector<TreeNode*> parts = splitBST(root->left, target);
        root->left = parts[1];
        return {parts[0], root};
    }
};
```


## 820. Short Encoding of Words

**Problem:** https://leetcode.com/problems/short-encoding-of-words/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, String, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Hash set, Ordered set, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A valid encoding of an array of words is any reference string s and array of indices indices such that: 

 words.length == indices.length 
 
 The reference string s ends with the '#' character. 
 
 For each index indices[i] , the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i] . 

 Given an array of words , return the length of the shortest reference string s possible of any valid encoding of words . 

 Example 1: 
 
```
Input:
 words = ["time", "me", "bell"]

Output:
 10

Explanation:
 A valid encoding would be s = 
"time#bell#" and indices = [0, 2, 5
].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "
time
#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "ti
me
#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#
bell
#"
```

 Example 2: 
 
```
Input:
 words = ["t"]

Output:
 2

Explanation:
 A valid encoding would be s = "t#" and indices = [0].
```

 Constraints: 

 1 <= words.length <= 2000 
 
 1 <= words[i].length <= 7 
 
 words[i] consists of only lowercase letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        unordered_set<string> s(words.begin(), words.end());
        for (string w : words)
            for (int i = 1; i < w.size(); ++i)
                s.erase(w.substr(i));

        int res = 0;
        for (const string& w : s)
            res += w.size() + 1;
        return res;
    }
};
```


## 850. Rectangle Area II

**Problem:** https://leetcode.com/problems/rectangle-area-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Segment Tree, Sweep Line, Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 2D array of axis-aligned rectangles . Each rectangle[i] = [x i1 , y i1 , x i2 , y i2 ] denotes the i th rectangle where (x i1 , y i1 ) are the coordinates of the bottom-left corner , and (x i2 , y i2 ) are the coordinates of the top-right corner . 
 
 Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once . 
 
 Return the total area . Since the answer may be too large, return it modulo 10 9 + 7 . 

 Example 1: 
 [Figure: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png] 
 
```
Input:
 rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]

Output:
 6

Explanation:
 A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.
```

 Example 2: 
 
```
Input:
 rectangles = [[0,0,1000000000,1000000000]]

Output:
 49

Explanation:
 The answer is 10
18
 modulo (10
9
 + 7), which is 49.
```

 Constraints: 

 1 <= rectangles.length <= 200 
 
 rectanges[i].length == 4 
 
 0 <= x i1 , y i1 , x i2 , y i2 <= 10 9 
 
 x i1 <= x i2 
 
 y i1 <= y i2 
 
 All rectangles have non zero area.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        const int MOD = 1e9 + 7;
        vector<int> X;
        for (auto& r : rectangles) {
            X.push_back(r[0]);
            X.push_back(r[2]);
        }

        sort(X.begin(), X.end());
        X.erase(unique(X.begin(), X.end()), X.end());

        long res = 0;
        for (int i = 1; i < X.size(); ++i) {
            int x1 = X[i - 1], x2 = X[i];
            if (x1 == x2) continue;
            vector<pair<int, int>> segs;
            for (auto& r : rectangles)
                if (r[0] <= x1 && r[2] >= x2)
                    segs.emplace_back(r[1], r[3]);

            sort(segs.begin(), segs.end());
            int total = 0, start = -1, end = -1;
            for (auto& [y1, y2] : segs) {
                start = max(start, y1);
                if (y2 > end) {
                    total += y2 - max(end, y1);
                    end = y2;
                }
            }
            res = (res + (long)(x2 - x1) * total) % MOD;
        }

        return res;
    }
};
```


## 889. Construct Binary Tree from Preorder and Postorder Traversal

**Problem:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Divide and Conquer, Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Binary tree, Hash map / hash set, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree . 
 
 If there exist multiple answers, you can return any of them. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/07/24/lc-prepost.jpg] 
 
```
Input:
 preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]

Output:
 [1,2,3,4,5,6,7]
```

 Example 2: 
 
```
Input:
 preorder = [1], postorder = [1]

Output:
 [1]
```

 Constraints: 

 1 <= preorder.length <= 30 
 
 1 <= preorder[i] <= preorder.length 
 
 All the values of preorder are unique . 
 
 postorder.length == preorder.length 
 
 1 <= postorder[i] <= postorder.length 
 
 All the values of postorder are unique . 
 
 It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution 
{
    int preidx = 0;
    int postidx = 0 ;
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) 
    {
        TreeNode * root = new TreeNode(preorder[preidx++]) ;
        if(root->val != postorder[postidx])
        {
            root->left = constructFromPrePost(preorder,postorder) ;   
        }   
        if(root->val != postorder[postidx])
        {
            root->right = constructFromPrePost(preorder,postorder) ;   
        }   
        postidx++ ;
        return root ;      
    }
};
```


## 998. Maximum Binary Tree II

**Problem:** https://leetcode.com/problems/maximum-binary-tree-ii/

**Difficulty:** Medium | **Premium:** No

**Tags:** Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie

**Data structures (inferred):** Binary tree, Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A maximum tree is a tree where every node has a value greater than any other value in its subtree. 
 
 You are given the root of a maximum binary tree and an integer val . 
 
 Just as in the previous problem , the given tree was constructed from a list a ( root = Construct(a) ) recursively with the following Construct(a) routine: 

 If a is empty, return null . 
 
 Otherwise, let a[i] be the largest element of a . Create a root node with the value a[i] . 
 
 The left child of root will be Construct([a[0], a[1], ..., a[i - 1]]) . 
 
 The right child of root will be Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]]) . 
 
 Return root . 

 Note that we were not given a directly, only a root node root = Construct(a) . 
 
 Suppose b is a copy of a with the value val appended to it. It is guaranteed that b has unique values. 
 
 Return Construct(b) . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/08/09/maxtree1.JPG] 
 
```
Input:
 root = [4,1,3,null,null,2], val = 5

Output:
 [5,4,null,1,3,null,null,2]

Explanation:
 a = [1,4,2,3], b = [1,4,2,3,5]
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/08/09/maxtree21.JPG] 
 
```
Input:
 root = [5,2,4,null,1], val = 3

Output:
 [5,2,4,null,1,null,3]

Explanation:
 a = [2,1,5,4], b = [2,1,5,4,3]
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/08/09/maxtree3.JPG] 
 
```
Input:
 root = [5,2,3,null,1], val = 4

Output:
 [5,2,4,null,1,3]

Explanation:
 a = [2,1,5,3], b = [2,1,5,3,4]
```

 Constraints: 

 The number of nodes in the tree is in the range [1, 100] . 
 
 1 <= Node.val <= 100 
 
 All the values of the tree are unique . 
 
 1 <= val <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    TreeNode* insertIntoMaxTree(TreeNode* root, int val) {
        if (!root || val > root->val) {
            TreeNode* node = new TreeNode(val);
            node->left = root;
            return node;
        }
        root->right = insertIntoMaxTree(root->right, val);
        return root;
    }
};
```


## 1032. Stream of Characters

**Problem:** https://leetcode.com/problems/stream-of-characters/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, String, Design, Trie, Data Stream, Aho–Corasick Algorithm

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Deque, Hash map, Hash set, Ordered map, Ordered set, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words . 
 
 For example, if words = ["abc", "xyz"]  and the stream added the four characters (one by one) 'a' , 'x' , 'y' , and 'z' , your algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words . 
 
 Implement the StreamChecker class: 

 StreamChecker(String[] words) Initializes the object with the strings array words . 
 
 boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words . 

 Example 1: 
 
```
Input

["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]

Output

[null, false, false, false, true, false, true, false, false, false, false, false, true]

Explanation

StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // return False
streamChecker.query("b"); // return False
streamChecker.query("c"); // return False
streamChecker.query("d"); // return True, because 'cd' is in the wordlist
streamChecker.query("e"); // return False
streamChecker.query("f"); // return True, because 'f' is in the wordlist
streamChecker.query("g"); // return False
streamChecker.query("h"); // return False
streamChecker.query("i"); // return False
streamChecker.query("j"); // return False
streamChecker.query("k"); // return False
streamChecker.query("l"); // return True, because 'kl' is in the wordlist
```

 Constraints: 

 1 <= words.length <= 2000 
 
 1 <= words[i].length <= 200 
 
 words[i] consists of lowercase English letters. 
 
 letter is a lowercase English letter. 
 
 At most 4 * 10 4 calls will be made to query.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <deque>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class StreamChecker {
private:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isEnd = false;
    };

    TrieNode* root;
    deque<char> stream;
    size_t maxWordLen;  // Maximum word length

public:
    StreamChecker(vector<string>& words) {
        root = new TrieNode();
        maxWordLen = 0;

        // Remove duplicate words
        unordered_set<string> uniqueWords(words.begin(), words.end());

        // Insert words into the Trie in reverse order
        for (const string& word : uniqueWords) {
            TrieNode* node = root;
            maxWordLen = max(maxWordLen, word.size());
            for (int i = word.size() - 1; i >= 0; i--) {
                if (!node->children.count(word[i])) {
                    node->children[word[i]] = new TrieNode();
                }
                node = node->children[word[i]];
            }
            node->isEnd = true;
        }
    }

    bool query(char letter) {
        stream.push_front(letter);
        if (stream.size() > maxWordLen) {
            stream.pop_back();  // Keep the stream size within the longest word length
        }

        TrieNode* node = root;
        for (char c : stream) {
            if (!node->children.count(c)) return false;
            node = node->children[c];
            if (node->isEnd) return true;
        }
        return false;
    }
};
```


## 1065. Index Pairs of a String

**Problem:** https://leetcode.com/problems/index-pairs-of-a-string/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, String, Trie, Sorting, Aho–Corasick Algorithm

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a string text and an array of strings words , return an array of all index pairs [i, j] so that the substring text[i...j] is in words . 
 
 Return the pairs [i, j] in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate). 

 Example 1: 
 
```
Input:
 text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]

Output:
 [[3,7],[9,13],[10,17]]
```

 Example 2: 
 
```
Input:
 text = "ababa", words = ["aba","ab"]

Output:
 [[0,1],[0,2],[2,3],[2,4]]

Explanation:
 Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
```

 Constraints: 

 1 <= text.length <= 100 
 
 1 <= words.length <= 20 
 
 1 <= words[i].length <= 50 
 
 text and words[i] consist of lowercase English letters. 
 
 All the strings of words are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    vector<vector<int>> indexPairs(string text, vector<string>& words) {
        vector<vector<int>> answer;
        for (const string& word : words) {
            size_t pos = text.find(word);
            while (pos != string::npos) {
                answer.push_back({static_cast<int>(pos),
                                  static_cast<int>(pos + word.size() - 1)});
                pos = text.find(word, pos + 1);
            }
        }
        sort(answer.begin(), answer.end());
        return answer;
    }
};
```


## 1104. Path In Zigzag Labelled Binary Tree

**Problem:** https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

**Difficulty:** Medium | **Premium:** No

**Tags:** Math, Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Math / Number Theory

**Data structures (inferred):** Binary tree, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

In an infinite binary tree where every node has two children, the nodes are labelled in row order. 
 
 In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left. 
 
 [Figure: https://assets.leetcode.com/uploads/2019/06/24/tree.png] 
 
 Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label . 

 Example 1: 
 
```
Input:
 label = 14

Output:
 [1,3,4,14]
```

 Example 2: 
 
```
Input:
 label = 26

Output:
 [1,2,6,10,26]
```

 Constraints: 

 1 <= label <= 10^6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        vector<int> path;
        int level = log2(label);
        while (label > 0) {
            path.insert(path.begin(), label);
            int total = pow(2, level) + pow(2, level + 1) - 1;
            label = (total - label) / 2;
            level--;
        }
        return path;
    }
};
```


## 1166. Design File System

**Problem:** https://leetcode.com/problems/design-file-system/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Hash Table, String, Design, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Stack / Queue

**Data structures (inferred):** Hash map, Hash map / hash set, Ordered map, String, Trie

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are asked to design a file system that allows you to create new paths and associate them with different values. 
 
 The format of a path is one or more concatenated strings of the form:  / followed by one or more lowercase English letters. For example, " /leetcode"  and " /leetcode/problems"  are valid paths while an empty string "" and "/"  are not. 
 
 Implement the  FileSystem class: 

 bool createPath(string path, int value)  Creates a new path and associates a value to it if possible and returns true . Returns false  if the path already exists or its parent path doesn't exist . 
 
 int get(string path)  Returns the value associated with path or returns  -1  if the path doesn't exist. 

 Example 1: 
 
```
Input:
 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]

Output:
 
[null,true,1]

Explanation:
 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
```

 Example 2: 
 
```
Input:
 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]

Output:
 
[null,true,true,2,false,-1]

Explanation:
 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
```

 Constraints: 

 2 <= path.length <= 100 
 
 1 <= value <= 10 9 
 
 Each path is valid and consists of lowercase English letters and '/' . 
 
 At most 10 4 calls in total will be made to createPath and get .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class FileSystem {
    unordered_map<string, int> values;

public:
    FileSystem() {}

    bool createPath(string path, int value) {
        if (path.empty() || path == "/" || values.count(path)) {
            return false;
        }
        int slash = path.find_last_of('/');
        string parent = path.substr(0, slash);
        if (!parent.empty() && !values.count(parent)) {
            return false;
        }
        values[path] = value;
        return true;
    }

    int get(string path) {
        auto it = values.find(path);
        return it == values.end() ? -1 : it->second;
    }
};
```


## 1178. Number of Valid Words for Each Puzzle

**Problem:** https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, String, Bit Manipulation, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:

 word contains the first letter of puzzle . 
 
 For each letter in word , that letter is in puzzle .

 For example, if the puzzle is "abcdefg" , then valid words are "faced" , "cabbage" , and "baggage" , while 
 
 invalid words are "beefed" (does not include 'a' ) and "based" (includes 's' which is not in the puzzle). 

Return an array answer , where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i] .

 Example 1: 
 
```
Input:
 words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]

Output:
 [1,1,3,2,4,0]

Explanation:
 
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
```

 Example 2: 
 
```
Input:
 words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]

Output:
 [0,1,3,2,0]
```

 Constraints: 

 1 <= words.length <= 10 5 
 
 4 <= words[i].length <= 50 
 
 1 <= puzzles.length <= 10 4 
 
 puzzles[i].length == 7 
 
 words[i] and puzzles[i] consist of lowercase English letters. 
 
 Each puzzles[i] does not contain repeated characters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        unordered_map<int, int> freq;
        for (auto& word : words) {
            int mask = 0;
            for (char c : word)
                mask |= 1 << (c - 'a');
            if (__builtin_popcount(mask) <= 7)
                freq[mask]++;
        }

        vector<int> res;
        for (auto& p : puzzles) {
            int total = 0;
            int mask = 0;
            for (int i = 0; i < 7; ++i)
                mask |= 1 << (p[i] - 'a');

            int sub = mask;
            int first = 1 << (p[0] - 'a');
            while (sub) {
                if (sub & first)
                    total += freq[sub];
                sub = (sub - 1) & mask;
            }
            res.push_back(total);
        }
        return res;
    }
};
```


## 1316. Distinct Echo Substrings

**Problem:** https://leetcode.com/problems/distinct-echo-substrings/

**Difficulty:** Hard | **Premium:** No

**Tags:** String, Trie, Rolling Hash, Suffix Array, Hash Function, Suffix Automaton, Suffix Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms

**Data structures (inferred):** Hash set, Ordered set, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Return the number of distinct non-empty substrings of text  that can be written as the concatenation of some string with itself (i.e. it can be written as a + a  where a is some string). 

 Example 1: 
 
```
Input:
 text = "abcabcabc"

Output:
 3

Explanation: 
The 3 substrings are "abcabc", "bcabca" and "cabcab".
```

 Example 2: 
 
```
Input:
 text = "leetcodeleetcode"

Output:
 2

Explanation: 
The 2 substrings are "ee" and "leetcodeleetcode".
```

 Constraints: 

 1 <= text.length <= 2000 
 
 text  has only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int distinctEchoSubstrings(string text) {
        int n = text.size();
        unordered_set<string> found;
        for (int start = 0; start < n; ++start) {
            int m = n - start;
            vector<int> z(m, 0);
            for (int i = 1, l = 0, r = 0; i < m; ++i) {
                if (i <= r) z[i] = min(r - i + 1, z[i - l]);
                while (i + z[i] < m && text[start + z[i]] == text[start + i + z[i]]) ++z[i];
                if (i + z[i] - 1 > r) l = i, r = i + z[i] - 1;
            }
            for (int len = 1; 2 * len <= m; ++len)
                if (z[len] >= len) found.insert(text.substr(start, 2 * len));
        }
        return found.size();
    }
};
```


## 1409. Queries on a Permutation With Key

**Problem:** https://leetcode.com/problems/queries-on-a-permutation-with-key/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Binary Indexed Tree, Simulation, Sqrt Decomposition

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given the array queries of positive integers between 1 and m , you have to process all queries[i] (from i=0 to i=queries.length-1 ) according to the following rules: 

 In the beginning, you have the permutation P=[1,2,3,...,m] . 
 
 For the current i , find the position of queries[i] in the permutation P ( indexing from 0 ) and then move this at the beginning of the permutation P . Notice that the position of queries[i] in P is the result for queries[i] . 

 Return an array containing the result for the given queries . 

 Example 1: 
 
```
Input:
 queries = [3,1,2,1], m = 5

Output:
 [2,1,2,1] 

Explanation:
 The queries are processed as follow: 
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 
2
, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5]. 
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 
1
, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5]. 
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 
2
, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5]. 
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 
1
, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5]. 
Therefore, the array containing the result is [2,1,2,1].
```

 Example 2: 
 
```
Input:
 queries = [4,1,2,2], m = 4

Output:
 [3,1,2,0]
```

 Example 3: 
 
```
Input:
 queries = [7,5,5,8,3], m = 8

Output:
 [6,5,0,7,5]
```

 Constraints: 

 1 <= m <= 10^3 
 
 1 <= queries.length <= m 
 
 1 <= queries[i] <= m

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> processQueries(vector<int>& queries, int m) {
        vector<int> perm(m);
        for (int i = 0; i < m; ++i) perm[i] = i + 1;
        vector<int> res;
        for (int q : queries) {
            for (int i = 0; i < m; ++i) {
                if (perm[i] == q) {
                    res.push_back(i);
                    perm.erase(perm.begin() + i);
                    perm.insert(perm.begin(), q);
                    break;
                }
            }
        }
        return res;
    }
};
```


## 1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits

**Problem:** https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

**Difficulty:** Hard | **Premium:** No

**Tags:** String, Greedy, Binary Indexed Tree, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Greedy / Intervals, String Algorithms

**Data structures (inferred):** Fenwick tree, Segment tree, String

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string num representing the digits of a very large integer and an integer k . You are allowed to swap any two adjacent digits of the integer at most k times. 
 
 Return the minimum integer you can obtain also as a string . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/06/17/q4_1.jpg] 
 
```
Input:
 num = "4321", k = 4

Output:
 "1342"

Explanation:
 The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.
```

 Example 2: 
 
```
Input:
 num = "100", k = 1

Output:
 "010"

Explanation:
 It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.
```

 Example 3: 
 
```
Input:
 num = "36789", k = 1000

Output:
 "36789"

Explanation:
 We can keep the number without any swaps.
```

 Constraints: 

 1 <= num.length <= 3 * 10 4 
 
 num consists of only digits and does not contain leading zeros . 
 
 1 <= k <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    string minInteger(string num, int k) {
        string res = num;
        int n = res.size();
        for (int i = 0; i < n && k > 0; ++i) {
            char min_digit = res[i];
            int min_pos = i;
            for (int j = i + 1; j < n && j - i <= k; ++j) {
                if (res[j] < min_digit) {
                    min_digit = res[j];
                    min_pos = j;
                    if (min_digit == '0') break;
                }
            }
            for (int j = min_pos; j > i; --j)
                swap(res[j], res[j - 1]);
            k -= (min_pos - i);
        }
        return res;
    }
};
```


## 1586. Binary Search Tree Iterator II

**Problem:** https://leetcode.com/problems/binary-search-tree-iterator-ii/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Stack / Queue

**Data structures (inferred):** Binary tree, Stack, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST): 

 BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST. 
 
 boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false . 
 
 int next() Moves the pointer to the right, then returns the number at the pointer. 
 
 boolean hasPrev() Returns true if there exists a number in the traversal to the left of the pointer, otherwise returns false . 
 
 int prev() Moves the pointer to the left, then returns the number at the pointer. 

 Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST. 
 
 You may assume that next() and prev() calls will always be valid. That is, there will be at least a next/previous number in the in-order traversal when next() / prev() is called. 

 Example 1: 
 
 [Figure: https://assets.leetcode.com/uploads/2020/09/14/untitled-diagram-1.png] 
 
```
Input

["BSTIterator", "next", "next", "prev", "next", "hasNext", "next", "next", "next", "hasNext", "hasPrev", "prev", "prev"]
[[[7, 3, 15, null, null, 9, 20]], [null], [null], [null], [null], [null], [null], [null], [null], [null], [null], [null], [null]]

Output

[null, 3, 7, 3, 7, true, 9, 15, 20, false, true, 15, 9]

Explanation

// The underlined element is where the pointer currently is.
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]); // state is 
 
 [3, 7, 9, 15, 20]
bSTIterator.next(); // state becomes [
3
, 7, 9, 15, 20], return 3
bSTIterator.next(); // state becomes [3, 
7
, 9, 15, 20], return 7
bSTIterator.prev(); // state becomes [
3
, 7, 9, 15, 20], return 3
bSTIterator.next(); // state becomes [3, 
7
, 9, 15, 20], return 7
bSTIterator.hasNext(); // return true
bSTIterator.next(); // state becomes [3, 7, 
9
, 15, 20], return 9
bSTIterator.next(); // state becomes [3, 7, 9, 
15
, 20], return 15
bSTIterator.next(); // state becomes [3, 7, 9, 15, 
20
], return 20
bSTIterator.hasNext(); // return false
bSTIterator.hasPrev(); // return true
bSTIterator.prev(); // state becomes [3, 7, 9, 
15
, 20], return 15
bSTIterator.prev(); // state becomes [3, 7, 
9
, 15, 20], return 9
```

 Constraints: 

 The number of nodes in the tree is in the range [1, 10 5 ] . 
 
 0 <= Node.val <= 10 6 
 
 At most 10 5 calls will be made to hasNext , next , hasPrev , and prev . 

 Follow up: Could you solve the problem without precalculating the values of the tree?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class BSTIterator {
    stack<TreeNode*> pending;
    vector<int> history;
    int index = -1;

    void pushLeft(TreeNode* node) {
        while (node) {
            pending.push(node);
            node = node->left;
        }
    }

public:
    BSTIterator(TreeNode* root) { pushLeft(root); }

    bool hasNext() { return index + 1 < static_cast<int>(history.size()) || !pending.empty(); }
    int next() {
        if (index + 1 < static_cast<int>(history.size())) return history[++index];
        TreeNode* node = pending.top();
        pending.pop();
        pushLeft(node->right);
        history.push_back(node->val);
        ++index;
        return node->val;
    }
    bool hasPrev() { return index > 0; }
    int prev() { return history[--index]; }
};
```


## 1597. Build Binary Expression Tree From Infix Expression

**Problem:** https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** String, Stack, Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms, Stack / Queue

**Data structures (inferred):** Binary tree, Stack, String, Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with 2 children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division). 
 
 For each internal node with operator o , the infix expression it represents is (A o B) , where A is the expression the left subtree represents and B is the expression the right subtree represents. 
 
 You are given a string s , an infix expression containing operands, the operators described above, and parentheses '(' and ')' . 
 
 Return any valid binary expression tree , whose in-order traversal reproduces s after omitting the parenthesis from it. 
 
 Please note that order of operations applies in s . That is, expressions in parentheses are evaluated first, and multiplication and division happen before addition and subtraction. 
 
 Operands must also appear in the same order in both s and the in-order traversal of the tree. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/10/02/ex1-4.png] 
 
```
Input:
 s = "3*4-2*5"

Output:
 [-,*,*,3,4,2,5]

Explanation:
 The tree above is the only valid tree whose inorder traversal produces s.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/10/02/ex1-2.png] 
 
```
Input:
 s = "2-3/(5*2)+1"

Output:
 [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]

Explanation:
 The inorder traversal of the tree above is 2-3/5*2+1 which is the same as s without the parenthesis. The tree also produces the correct result and its operands are in the same order as they appear in s.
The tree below is also a valid binary expression tree with the same inorder traversal as s, but it not a valid answer because it does not evaluate to the same value.

The third tree below is also not valid. Although it produces the same result and is equivalent to the above trees, its inorder traversal does not produce s and its operands are not in the same order as s.
```

 Example 3: 
 
```
Input:
 s = "1+2+3+4+5"

Output:
 [+,+,5,+,4,null,null,+,3,null,null,1,2]

Explanation:
 The tree [+,+,5,+,+,null,null,1,2,3,4] is also one of many other valid trees.
```

 Constraints: 

 1 <= s.length <= 100 
 
 s consists of digits and the characters '(' , ')' , '+' , '-' , '*' , and '/' . 
 
 Operands in s are exactly 1 digit. 
 
 It is guaranteed that s is a valid expression.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    int priority(char op) { return (op == '+' || op == '-') ? 1 : 2; }

public:
    Node* expTree(string s) {
        stack<Node*> nodes;
        stack<char> ops;
        auto reduce = [&]() {
            char op = ops.top(); ops.pop();
            Node* right = nodes.top(); nodes.pop();
            Node* left = nodes.top(); nodes.pop();
            Node* root = new Node(op);
            root->left = left;
            root->right = right;
            nodes.push(root);
        };
        for (char c : s) {
            if (isdigit(static_cast<unsigned char>(c))) {
                nodes.push(new Node(c));
            } else if (c == '(') {
                ops.push(c);
            } else if (c == ')') {
                while (ops.top() != '(') reduce();
                ops.pop();
            } else {
                while (!ops.empty() && ops.top() != '(' && priority(ops.top()) >= priority(c)) reduce();
                ops.push(c);
            }
        }
        while (!ops.empty()) reduce();
        return nodes.top();
    }
};
```


## 1622. Fancy Sequence

**Problem:** https://leetcode.com/problems/fancy-sequence/

**Difficulty:** Hard | **Premium:** No

**Tags:** Math, Design, Segment Tree, Number Theory, Fermat's Little Theorem

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Math / Number Theory, Stack / Queue

**Data structures (inferred):** Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Write an API that generates fancy sequences using the append , addAll , and multAll operations. 
 
 Implement the Fancy class: 

 Fancy() Initializes the object with an empty sequence. 
 
 void append(val) Appends an integer val to the end of the sequence. 
 
 void addAll(inc) Increments all existing values in the sequence by an integer inc . 
 
 void multAll(m) Multiplies all existing values in the sequence by an integer m . 
 
 int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 10 9 + 7 . If the index is greater or equal than the length of the sequence, return -1 . 

 Example 1: 
 
```
Input

["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]

Output

[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

Explanation

Fancy fancy = new Fancy();
fancy.append(2); // fancy sequence: [2]
fancy.addAll(3); // fancy sequence: [2+3] -> [5]
fancy.append(7); // fancy sequence: [5, 7]
fancy.multAll(2); // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3); // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10); // fancy sequence: [13, 17, 10]
fancy.multAll(2); // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20
```

 Constraints: 

 1 <= val, inc, m <= 100 
 
 0 <= idx <= 10 5 
 
 At most 10 5 calls total will be made to append , addAll , multAll , and getIndex .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <vector>
#include <cmath>
using namespace std;

class Fancy {
    static constexpr int MOD = 1e9 + 7;
    vector<long long> seq;
    long long add = 0, mult = 1;

    long long modinv(long long x) {
        long long res = 1, p = MOD - 2;
        while (p) {
            if (p & 1) res = res * x % MOD;
            x = x * x % MOD;
            p >>= 1;
        }
        return res;
    }

public:
    Fancy() {}

    void append(int val) {
        seq.push_back(((val - add + MOD) % MOD) * modinv(mult) % MOD);
    }

    void addAll(int inc) {
        add = (add + inc) % MOD;
    }

    void multAll(int m) {
        add = add * m % MOD;
        mult = mult * m % MOD;
    }

    int getIndex(int idx) {
        if (idx >= seq.size()) return -1;
        return (seq[idx] * mult + add) % MOD;
    }
};
```


## 1628. Design an Expression Tree With Evaluate Function

**Problem:** https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Math, Stack, Tree, Design, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Math / Number Theory, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Binary tree, Stack, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression. 
 
 Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. For example, the postfix tokens of the expression 4*(5-(7+2)) are represented in the array postfix = ["4","5","7","2","+","-","*"] . 
 
 The class Node is an interface you should use to implement the binary expression tree. The returned tree will be tested using the evaluate function, which is supposed to evaluate the tree's value. You should not remove the Node class; however, you can modify it as you wish, and you can define other classes to implement it if needed. 
 
 A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with two children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division). 
 
 It's guaranteed that no subtree will yield a value that exceeds 10 9 in absolute value, and all the operations are valid (i.e., no division by zero). 
 
 Follow up: Could you design the expression tree such that it is more modular? For example, is your design able to support additional operators without making changes to your existing evaluate implementation? 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2020/10/15/untitled-diagram.png] 
 
```
Input:
 s = ["3","4","+","2","*","7","/"]

Output:
 2

Explanation:
 this expression evaluates to the above binary tree with expression (
(3+4)*2)/7) = 14/7 = 2.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2020/10/15/untitled-diagram2.png] 
 
```
Input:
 s = ["4","5","2","7","+","-","*"]

Output:
 -16

Explanation:
 this expression evaluates to the above binary tree with expression 4*(5-
(2+7)) = 4*(-4) = -16.
```

 Constraints: 

 1 <= s.length < 100 
 
 s.length is odd. 
 
 s consists of numbers and the characters '+' , '-' , '*' , and '/' . 
 
 If s[i] is a number, its integer representation is no more than 10 5 . 
 
 It is guaranteed that s is a valid expression. 
 
 The absolute value of the result and intermediate values will not exceed 10 9 . 
 
 It is guaranteed that no expression will include division by zero.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Node {
public:
    virtual ~Node() {}
    virtual int evaluate() const=0;
};
class ExprNode:public Node {
    string op;
    Node *l,*r;
public:
    ExprNode(string s,Node *a=nullptr,Node *b=nullptr):op(s),l(a),r(b){}
    ~ExprNode(){delete l;delete r;}
    int evaluate() const override {
        if(!l)return stoi(op);
        int a=l->evaluate(),b=r->evaluate();
        if(op=="+")return a+b;
        if(op=="-")return a-b;
        if(op=="*")return a*b;
        return a/b;
    }
};
class TreeBuilder {
public:
    Node* buildTree(vector<string>& postfix) {
        stack<Node*> st;
        for(const string &s:postfix){
            if(s=="+"||s=="-"||s=="*"||s=="/"){
                Node *b=st.top();st.pop();Node *a=st.top();st.pop();
                st.push(new ExprNode(s,a,b));
            }else st.push(new ExprNode(s));
        }
        return st.top();
    }
};
```


## 1698. Number of Distinct Substrings in a String

**Problem:** https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** String, Trie, Rolling Hash, Suffix Array, Hash Function

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms

**Data structures (inferred):** String, Trie

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a string s , return the number of distinct substrings of   s . 
 
 A substring of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string. 

 Example 1: 
 
```
Input:
 s = "aabbaba"

Output:
 21

Explanation:
 The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
```

 Example 2: 
 
```
Input:
 s = "abcdefg"

Output:
 28
```

 Constraints: 

 1 <= s.length <= 500 
 
 s consists of lowercase English letters. 

 Follow up: Can you solve this problem in O(n) time complexity?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    struct TrieNode {
        array<TrieNode*, 26> next;
        TrieNode() { next.fill(nullptr); }
        ~TrieNode() { for (TrieNode* child : next) delete child; }
    };
public:
    int countDistinct(string s) {
        TrieNode root;
        int count = 0;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            TrieNode* node = &root;
            for (int j = i; j < static_cast<int>(s.size()); ++j) {
                int c = s[j] - 'a';
                if (!node->next[c]) { node->next[c] = new TrieNode(); ++count; }
                node = node->next[c];
            }
        }
        return count;
    }
};
```


## 1707. Maximum XOR With an Element From Array

**Problem:** https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Bit Manipulation, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Bitset, Ordered set, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [x i , m i ] . 
 
 The answer to the i th query is the maximum bitwise XOR value of x i and any element of nums that does not exceed m i . In other words, the answer is max(nums[j] XOR x i ) for all j such that nums[j] <= m i . If all elements in nums are larger than m i , then the answer is -1 . 
 
 Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the i th query. 

 Example 1: 
 
```
Input:
 nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]

Output:
 [3,3,7]

Explanation:

1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.
```

 Example 2: 
 
```
Input:
 nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]

Output:
 [15,-1,5]
```

 Constraints: 

 1 <= nums.length, queries.length <= 10 5 
 
 queries[i].length == 2 
 
 0 <= nums[j], x i , m i <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    struct TrieNode {
        TrieNode* left = 0, * right = 0;
    };

    void addNode(TrieNode* head, int st)
    {
        bitset<32> p = bitset<32>(st);
        for (int i = 31; i >= 0; i--)
        {
            if (p.test(i))
            {
                if (!head->right)
                    head->right = new TrieNode();
                head = head->right;
            }
            else
            {
                if (!head->left)
                    head->left = new TrieNode();
                head = head->left;
            }
        }
    }

    int getMax(TrieNode* head, int st)
    {
        if (!head)
            return -1;
        bitset<32> p = bitset<32>(st);

        int ans = 0;
  
        for (int i = 31; i >= 0; i--)
        {
            if (!head->right && !head->left)
                return -1;
            ans *= 2;

            if (p.test(i))
            {
                if (head->left)
                    head = head->left;
                else
                {
                    head = head->right;
                    ans++;
                }
            }
            else   
            {
                if (head->right)
                {
                    head = head->right;
                    ans++;
                }
                else
                    head = head->left;
            }
        }

        return ans;
    }

    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& que) {
        sort(nums.begin(), nums.end());
        for (int  i = 0; i < que.size(); i++)
        {
            reverse(que[i].begin(), que[i].end());
            que[i].push_back(i);
        }
        vector<int> ans(que.size());

        sort(que.begin(), que.end());

        TrieNode* head = new TrieNode();

        int ind = 0;

        for (auto e : que)
        {
            while (nums[ind] <= e[0] && ind < nums.size())
            {
                addNode(head, nums[ind]);
                ind++;
            }

            ans[e[2]] = getMax(head, e[1]);
            if (ans[e[2]] != -1)
                ans[e[2]] ^= e[1];
        }

        return ans;
    }
};
```


## 1803. Count Pairs With XOR in a Range

**Problem:** https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Bit Manipulation, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a (0-indexed) integer array nums and two integers low and high , return the number of nice pairs . 
 
 A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high . 

 Example 1: 
 
```
Input:
 nums = [1,4,2,7], low = 2, high = 6

Output:
 6

Explanation:
 All nice pairs (i, j) are as follows:
 - (0, 1): nums[0] XOR nums[1] = 5 
 - (0, 2): nums[0] XOR nums[2] = 3
 - (0, 3): nums[0] XOR nums[3] = 6
 - (1, 2): nums[1] XOR nums[2] = 6
 - (1, 3): nums[1] XOR nums[3] = 3
 - (2, 3): nums[2] XOR nums[3] = 5
```

 Example 2: 
 
```
Input:
 nums = [9,8,4,2,1], low = 5, high = 14

Output:
 8

Explanation:
 All nice pairs (i, j) are as follows:
​​​​​ - (0, 2): nums[0] XOR nums[2] = 13
  - (0, 3): nums[0] XOR nums[3] = 11
  - (0, 4): nums[0] XOR nums[4] = 8
  - (1, 2): nums[1] XOR nums[2] = 12
  - (1, 3): nums[1] XOR nums[3] = 10
  - (1, 4): nums[1] XOR nums[4] = 9
  - (2, 3): nums[2] XOR nums[3] = 6
  - (2, 4): nums[2] XOR nums[4] = 5
```

 Constraints: 

 1 <= nums.length <= 2 * 10 4 
 
 1 <= nums[i] <= 2 * 10 4 
 
 1 <= low <= high <= 2 * 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
struct TrieNode {
    TrieNode* child[2] = {};
    int count = 0;
};

class Solution {
    TrieNode* root = new TrieNode();

    void insert(int num) {
        TrieNode* node = root;
        for (int i = 14; i >= 0; --i) {
            int bit = (num >> i) & 1;
            if (!node->child[bit]) node->child[bit] = new TrieNode();
            node = node->child[bit];
            node->count++;
        }
    }

    int countLess(int num, int limit) {
        TrieNode* node = root;
        int res = 0;
        for (int i = 14; i >= 0 && node; --i) {
            int nBit = (num >> i) & 1;
            int lBit = (limit >> i) & 1;
            if (lBit == 1) {
                if (node->child[nBit]) res += node->child[nBit]->count;
                node = node->child[1 - nBit];
            } else {
                node = node->child[nBit];
            }
        }
        return res;
    }

public:
    int countPairs(vector<int>& nums, int low, int high) {
        int res = 0;
        for (int num : nums) {
            res += countLess(num, high + 1) - countLess(num, low);
            insert(num);
        }
        return res;
    }
};
```


## 1804. Implement Trie II (Prefix Tree)

**Problem:** https://leetcode.com/problems/implement-trie-ii-prefix-tree/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Hash Table, String, Design, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Stack / Queue

**Data structures (inferred):** Hash map / hash set, String, Trie

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker. 
 
 Implement the Trie class: 

 Trie() Initializes the trie object. 
 
 void insert(String word) Inserts the string word into the trie. 
 
 int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie. 
 
 int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix. 
 
 void erase(String word) Erases the string word from the trie. 

 Example 1: 
 
```
Input

["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]

Output

[null, null, null, 2, 2, null, 1, 1, null, 0]

Explanation

Trie trie = new Trie();
trie.insert("apple"); // Inserts "apple".
trie.insert("apple"); // Inserts another "apple".
trie.countWordsEqualTo("apple"); // There are two instances of "apple" so return 2.
trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
trie.erase("apple"); // Erases one "apple".
trie.countWordsEqualTo("apple"); // Now there is only one instance of "apple" so return 1.
trie.countWordsStartingWith("app"); // return 1
trie.erase("apple"); // Erases "apple". Now the trie is empty.
trie.countWordsStartingWith("app"); // return 0
```

 Constraints: 

 1 <= word.length, prefix.length <= 2000 
 
 word and prefix consist only of lowercase English letters. 
 
 At most 3 * 10 4 calls in total will be made to insert , countWordsEqualTo , countWordsStartingWith , and erase . 
 
 It is guaranteed that for any function call to erase , the string word will exist in the trie.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Trie {
    struct Node {
        array<Node*, 26> child;
        int prefix = 0;
        int terminal = 0;
        Node() { child.fill(nullptr); }
        ~Node() { for (Node* p : child) delete p; }
    };
    Node root;
    Node* follow(const string& word) const {
        Node* node = const_cast<Node*>(&root);
        for (char c : word) {
            node = node->child[c - 'a'];
            if (!node) return nullptr;
        }
        return node;
    }
public:
    Trie() {}
    void insert(string word) {
        Node* node = &root;
        for (char c : word) {
            int index = c - 'a';
            if (!node->child[index]) node->child[index] = new Node();
            node = node->child[index];
            ++node->prefix;
        }
        ++node->terminal;
    }
    int countWordsEqualTo(string word) {
        Node* node = follow(word);
        return node ? node->terminal : 0;
    }
    int countWordsStartingWith(string prefix) {
        Node* node = follow(prefix);
        return node ? node->prefix : 0;
    }
    void erase(string word) {
        if (!countWordsEqualTo(word)) return;
        Node* node = &root;
        for (char c : word) {
            node = node->child[c - 'a'];
            --node->prefix;
        }
        --node->terminal;
    }
};
```


## 1902. Depth of BST Given Insertion Order

**Problem:** https://leetcode.com/problems/depth-of-bst-given-insertion-order/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Tree, Binary Search Tree, Binary Tree, Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Binary tree, Ordered map, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 0-indexed integer array order of length n , a permutation of integers from 1 to n representing the order of insertion into a binary search tree . 
 
 A binary search tree is defined as follows: 

 The left subtree of a node contains only nodes with keys less than the node's key. 
 
 The right subtree of a node contains only nodes with keys greater than the node's key. 
 
 Both the left and right subtrees must also be binary search trees. 

 The binary search tree is constructed as follows: 

 order[0] will be the root of the binary search tree. 
 
 All subsequent elements are inserted as the child of any existing node such that the binary search tree properties hold. 

 Return the depth of the binary search tree . 
 
 A binary tree's depth is the number of nodes along the longest path from the root node down to the farthest leaf node. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2021/06/15/1.png] 
 
```
Input:
 order = [2,1,4,3]

Output:
 3

Explanation: 
The binary search tree has a depth of 3 with path 2->3->4.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2021/06/15/2.png] 
 
```
Input:
 order = [2,1,3,4]

Output:
 3

Explanation: 
The binary search tree has a depth of 3 with path 2->3->4.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2021/06/15/3.png] 
 
```
Input:
 order = [1,2,3,4]

Output:
 4

Explanation: 
The binary search tree has a depth of 4 with path 1->2->3->4.
```

 Constraints: 

 n == order.length 
 
 1 <= n <= 10 5 
 
 order is a permutation of integers between 1 and n .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int maxDepthBST(vector<int>& order) {
        map<int, int> depth;
        int answer = 0;
        for (int value : order) {
            auto it = depth.lower_bound(value);
            int left = 0, right = 0;
            if (it != depth.end()) {
                right = it->second;
            }
            if (it != depth.begin()) {
                left = prev(it)->second;
            }
            int d = max(left, right) + 1;
            depth[value] = d;
            answer = max(answer, d);
        }
        return answer;
    }
};
```


## 2158. Amount of New Area Painted Each Day

**Problem:** https://leetcode.com/problems/amount-of-new-area-painted-each-day/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Segment Tree, Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n , where paint[i] = [start i , end i ] . This means that on the i th day you need to paint the area between start i and end i . 
 
 Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once . 
 
 Return an integer array worklog of length n , where worklog[i] is the amount of new area that you painted on the i th day. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/01/screenshot-2022-02-01-at-17-16-16-diagram-drawio-diagrams-net.png] 
 
```
Input:
 paint = [[1,4],[4,7],[5,8]]

Output:
 [3,3,1]

Explanation:

On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/01/screenshot-2022-02-01-at-17-17-45-diagram-drawio-diagrams-net.png] 
 
```
Input:
 paint = [[1,4],[5,8],[4,7]]

Output:
 [3,3,1]

Explanation:

On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 5 and 8.
The amount of new area painted on day 1 is 8 - 5 = 3.
On day 2, paint everything between 4 and 5.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 5 - 4 = 1.
```

 Example 3: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/01/screenshot-2022-02-01-at-17-19-49-diagram-drawio-diagrams-net.png] 
 
```
Input:
 paint = [[1,5],[2,4]]

Output:
 [4,0]

Explanation:

On day 0, paint everything between 1 and 5.
The amount of new area painted on day 0 is 5 - 1 = 4.
On day 1, paint nothing because everything between 2 and 4 was already painted on day 0.
The amount of new area painted on day 1 is 0.
```

 Constraints: 

 1 <= paint.length <= 10 5 
 
 paint[i].length == 2 
 
 0 <= start i < end i <= 5 * 10 4

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    vector<int> parent;
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
public:
    vector<int> amountPainted(vector<vector<int>>& paint) {
        int maximum = 0;
        for (const auto& p : paint) maximum = max(maximum, p[1]);
        parent.resize(maximum + 1);
        iota(parent.begin(), parent.end(), 0);
        vector<int> answer;
        for (const auto& p : paint) {
            int count = 0;
            int pos = find(p[0]);
            while (pos < p[1]) {
                ++count;
                parent[pos] = find(pos + 1);
                pos = find(pos);
            }
            answer.push_back(count);
        }
        return answer;
    }
};
```


## 2196. Create Binary Tree From Descriptions

**Problem:** https://leetcode.com/problems/create-binary-tree-from-descriptions/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Simulation / Implementation

**Data structures (inferred):** Array / vector, Binary tree, Hash map, Hash map / hash set, Hash set, Ordered map, Ordered set, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 2D integer array descriptions where descriptions[i] = [parent i , child i , isLeft i ] indicates that parent i is the parent of child i in a binary tree of unique values. Furthermore, 

 If isLeft i == 1 , then child i is the left child of parent i . 
 
 If isLeft i == 0 , then child i is the right child of parent i . 

 Construct the binary tree described by descriptions and return its root . 
 
 The test cases will be generated such that the binary tree is valid . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/09/example1drawio.png] 
 
```
Input:
 descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]

Output:
 [50,20,80,15,17,19]

Explanation:
 The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/02/09/example2drawio.png] 
 
```
Input:
 descriptions = [[1,2,1],[2,3,0],[3,4,1]]

Output:
 [1,2,null,null,3,4]

Explanation:
 The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
```

 Constraints: 

 1 <= descriptions.length <= 10 4 
 
 descriptions[i].length == 3 
 
 1 <= parent i , child i <= 10 5 
 
 0 <= isLeft i <= 1 
 
 The binary tree described by descriptions is valid.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution { public:
 TreeNode* createBinaryTree(vector<vector<int>>& descriptions){unordered_map<int,TreeNode*> nodes;unordered_set<int> child;
  for(auto&d:descriptions){int p=d[0],c=d[1];if(!nodes.count(p))nodes[p]=new TreeNode(p);if(!nodes.count(c))nodes[c]=new TreeNode(c);
   if(d[2])nodes[p]->left=nodes[c];else nodes[p]->right=nodes[c];child.insert(c);
  }for(auto&kv:nodes)if(!child.count(kv.first))return kv.second;return nullptr;
 }
};
```


## 2213. Longest Substring of One Repeating Character

**Problem:** https://leetcode.com/problems/longest-substring-of-one-repeating-character/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, String, Segment Tree, Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Segment tree, String, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 0-indexed string s . You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k , both of which are used to describe k queries. 
 
 The i th query updates the character in s at index queryIndices[i] to the character queryCharacters[i] . 
 
 Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the i th query is performed. 

 Example 1: 
 
```
Input:
 s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]

Output:
 [3,3,4]

Explanation:
 
- 1
st
 query updates s = "
b
b
b
acc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2
nd
 query updates s = "bbb
c
cc
". 
 The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3
rd
 query updates s = "
bbb
b
cc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].
```

 Example 2: 
 
```
Input:
 s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]

Output:
 [2,3]

Explanation:

- 1
st
 query updates s = "ab
a
zz
". The longest substring consisting of one repeating character is "zz" with length 2.
- 2
nd
 query updates s = "
a
a
a
zz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].
```

 Constraints: 

 1 <= s.length <= 10 5 
 
 s consists of lowercase English letters. 
 
 k == queryCharacters.length == queryIndices.length 
 
 1 <= k <= 10 5 
 
 queryCharacters consists of lowercase English letters. 
 
 0 <= queryIndices[i] < s.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
 struct Node{int len=0,pre=0,suf=0,best=0;char first=0,last=0;};
 string s;vector<Node> tr;
 Node merge(Node a,Node b){if(!a.len)return b;if(!b.len)return a;Node x;x.len=a.len+b.len;x.first=a.first;x.last=b.last;
  x.pre=a.pre+(a.pre==a.len&&a.last==b.first?b.pre:0);
  x.suf=b.suf+(b.suf==b.len&&a.last==b.first?a.suf:0);
  x.best=max(a.best,b.best);if(a.last==b.first)x.best=max(x.best,a.suf+b.pre);return x;
 }
 void build(int p,int l,int r){if(l==r){tr[p]={1,1,1,1,s[l],s[l]};return;}int m=(l+r)/2;build(p*2,l,m);build(p*2+1,m+1,r);tr[p]=merge(tr[p*2],tr[p*2+1]);}
 void update(int p,int l,int r,int idx,char c){if(l==r){tr[p]={1,1,1,1,c,c};return;}int m=(l+r)/2;
  if(idx<=m)update(p*2,l,m,idx,c);else update(p*2+1,m+1,r,idx,c);tr[p]=merge(tr[p*2],tr[p*2+1]);
 }
 public:
 vector<int> longestRepeating(string str,string queryCharacters,vector<int>& queryIndices){s=str;int n=s.size();tr.resize(4*n+4);build(1,0,n-1);vector<int> ans;
  for(int i=0;i<(int)queryIndices.size();++i){update(1,0,n-1,queryIndices[i],queryCharacters[i]);ans.push_back(tr[1].best);}return ans;
 }
};
```


## 2227. Encrypt and Decrypt Strings

**Problem:** https://leetcode.com/problems/encrypt-and-decrypt-strings/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, String, Design, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Stack / Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a character array keys containing unique characters and a string array values containing strings of length 2. You are also given another string array dictionary that contains all permitted original strings after decryption. You should implement a data structure that can encrypt or decrypt a 0-indexed string. 
 
 A string is encrypted with the following process: 

 For each character c in the string, we find the index i satisfying keys[i] == c in keys . 
 
 Replace c with values[i] in the string. 

 Note that in case a character of the string is not present in keys , the encryption process cannot be carried out, and an empty string "" is returned. 
 
 A string is decrypted with the following process: 

 For each substring s of length 2 occurring at an even index in the string, we find an i such that values[i] == s . If there are multiple valid i , we choose any one of them. This means a string could have multiple possible strings it can decrypt to. 
 
 Replace s with keys[i] in the string. 

 Implement the Encrypter class: 

 Encrypter(char[] keys, String[] values, String[] dictionary) Initializes the Encrypter class with keys, values , and dictionary . 
 
 String encrypt(String word1) Encrypts word1 with the encryption process described above and returns the encrypted string. 
 
 int decrypt(String word2) Returns the number of possible strings word2 could decrypt to that also appear in dictionary . 

 Example 1: 
 
```
Input

["Encrypter", "encrypt", "decrypt"]
[[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]

Output

[null, "eizfeiam", 2]

Explanation

Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]);
encrypter.encrypt("abcd"); // return "eizfeiam". 
  // 'a' maps to "ei", 'b' maps to "zf", 'c' maps to "ei", and 'd' maps to "am".
encrypter.decrypt("eizfeiam"); // return 2. 
 // "ei" can map to 'a' or 'c', "zf" maps to 'b', and "am" maps to 'd'. 
 // Thus, the possible strings after decryption are "abad", "cbad", "abcd", and "cbcd". 
 // 2 of those strings, "abad" and "abcd", appear in dictionary, so the answer is 2.
```

 Constraints: 

 1 <= keys.length == values.length <= 26 
 
 values[i].length == 2 
 
 1 <= dictionary.length <= 100 
 
 1 <= dictionary[i].length <= 100 
 
 All keys[i] and dictionary[i] are unique . 
 
 1 <= word1.length <= 2000 
 
 2 <= word2.length <= 200 
 
 All word1[i] appear in keys . 
 
 word2.length is even. 
 
 keys , values[i] , dictionary[i] , word1 , and word2 only contain lowercase English letters. 
 
 At most 200 calls will be made to encrypt and decrypt in total .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Encrypter {
 unordered_map<char,string> mp;unordered_map<string,int> freq;
 public:
 Encrypter(vector<char>& keys,vector<string>& values,vector<string>& dictionary){for(int i=0;i<(int)keys.size();++i)mp[keys[i]]=values[i];
  for(auto&w:dictionary){string enc=encrypt(w);if(!enc.empty())++freq[enc];}
 }
 string encrypt(string word1){string s;for(char c:word1){auto it=mp.find(c);if(it==mp.end())return "";s+=it->second;}return s;}
 int decrypt(string word2){auto it=freq.find(word2);return it==freq.end()?0:it->second;}
};
```


## 2236. Root Equals Sum of Children

**Problem:** https://leetcode.com/problems/root-equals-sum-of-children/

**Difficulty:** Easy | **Premium:** No

**Tags:** Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie

**Data structures (inferred):** Binary tree, Tree adjacency list

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child. 
 
 Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise . 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/04/08/graph3drawio.png] 
 
```
Input:
 root = [10,4,6]

Output:
 true

Explanation:
 The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/04/08/graph3drawio-1.png] 
 
```
Input:
 root = [5,3,1]

Output:
 false

Explanation:
 The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.
```

 Constraints: 

 The tree consists only of the root, its left child, and its right child. 
 
 -100 <= Node.val <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool checkTree(TreeNode* root) {
        if(root && root->left && root->right)
        {
            return (root->val == root->left->val + root->right->val) ;
        }
        return false ;
    }
};
```


## 2261. K Divisible Elements Subarrays

**Problem:** https://leetcode.com/problems/k-divisible-elements-subarrays/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Trie, Rolling Hash, Hash Function, Enumeration

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Ordered map, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an integer array nums and two integers k and p , return the number of distinct subarrays, which have at most k elements that are divisible by p . 
 
 Two arrays nums1 and nums2 are said to be distinct if: 

 They are of different lengths, or 
 
 There exists at least one index i where nums1[i] != nums2[i] . 

 A subarray is defined as a non-empty contiguous sequence of elements in an array. 

 Example 1: 
 
```
Input:
 nums = [
2
,3,3,
2
,
2
], k = 2, p = 2

Output:
 11

Explanation:

The elements at indices 0, 3, and 4 are divisible by p = 2.
The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are:
[2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2].
Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once.
The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.
```

 Example 2: 
 
```
Input:
 nums = [1,2,3,4], k = 4, p = 1

Output:
 10

Explanation:

All element of nums are divisible by p = 1.
Also, every subarray of nums will have at most 4 elements that are divisible by 1.
Since all subarrays are distinct, the total number of subarrays satisfying all the constraints is 10.
```

 Constraints: 

 1 <= nums.length <= 200 
 
 1 <= nums[i], p <= 200 
 
 1 <= k <= nums.length 

 Follow up: 
 
 Can you solve this problem in O(n 2 ) time complexity?

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {struct Node {unordered_map<int,int> child;};public:int countDistinct(vector<int>& nums,int k,int p){vector<Node> trie(1);int ans=0,n=nums.size();for(int i=0;i<n;++i){int node=0,bad=0;for(int j=i;j<n;++j){bad+=nums[j]%p==0;if(bad>k)break;int x=nums[j];if(!trie[node].child.count(x)){int id=trie.size();trie[node].child[x]=id;trie.emplace_back();++ans;}node=trie[node].child[x];}}return ans;} };
```


## 2276. Count Integers in Intervals

**Problem:** https://leetcode.com/problems/count-integers-in-intervals/

**Difficulty:** Hard | **Premium:** No

**Tags:** Design, Segment Tree, Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Stack / Queue

**Data structures (inferred):** Ordered map, Segment tree

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an empty set of intervals, implement a data structure that can: 

 Add an interval to the set of intervals. 
 
 Count the number of integers that are present in at least one interval. 

 Implement the CountIntervals class: 

 CountIntervals() Initializes the object with an empty set of intervals. 
 
 void add(int left, int right) Adds the interval [left, right] to the set of intervals. 
 
 int count() Returns the number of integers that are present in at least one interval. 

 Note that an interval [left, right] denotes all the integers x where left <= x <= right . 

 Example 1: 
 
```
Input

["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]

Output

[null, null, null, 6, null, 8]

Explanation

CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals. 
countIntervals.add(2, 3); // add [2, 3] to the set of intervals.
countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
countIntervals.count(); // return 6
 // the integers 2 and 3 are present in the interval [2, 3].
 // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
countIntervals.add(5, 8); // add [5, 8] to the set of intervals.
countIntervals.count(); // return 8
 // the integers 2 and 3 are present in the interval [2, 3].
 // the integers 5 and 6 are present in the interval [5, 8].
 // the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
 // the integers 9 and 10 are present in the interval [7, 10].
```

 Constraints: 

 1 <= left <= right <= 10 9 
 
 At most 10 5 calls in total will be made to add and count . 
 
 At least one call will be made to count .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class CountIntervals {map<int,int> ranges;long long total=0;public:CountIntervals(){}void add(int left,int right){auto it=ranges.lower_bound(left);if(it!=ranges.begin()){auto prev=it;--prev;if(prev->second>=left)it=prev;}while(it!=ranges.end()&&it->first<=right){if(it->second<left){++it;continue;}left=min(left,it->first);right=max(right,it->second);total-=1LL*it->second-it->first+1;it=ranges.erase(it);}ranges[left]=right;total+=1LL*right-left+1;}int count(){return (int)total;}};
```


## 2416. Sum of Prefix Scores of Strings

**Problem:** https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, String, Trie, Counting

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array words of size n consisting of non-empty strings. 
 
 We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i] . 

 For example, if words = ["a", "ab", "abc", "cab"] , then the score of "ab" is 2 , since "ab" is a prefix of both "ab" and "abc" . 

 Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i] . 
 
 Note that a string is considered as a prefix of itself. 

 Example 1: 
 
```
Input:
 words = ["abc","ab","bc","b"]

Output:
 [5,4,3,2]

Explanation:
 The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".
- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.
- "ab" has 2 prefixes: "a" and "ab".
- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.
- "bc" has 2 prefixes: "b" and "bc".
- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.
- "b" has 1 prefix: "b".
- There are 2 strings with the prefix "b".
The total is answer[3] = 2.
```

 Example 2: 
 
```
Input:
 words = ["abcd"]

Output:
 [4]

Explanation:

"abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.
```

 Constraints: 

 1 <= words.length <= 1000 
 
 1 <= words[i].length <= 1000 
 
 words[i] consists of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {struct Node{int next[26],count;Node():count(0){fill(next,next+26,-1);}};public:vector<int> sumPrefixScores(vector<string>& words){vector<Node>trie(1);for(auto&w:words){int u=0;for(char c:w){int x=c-'a';if(trie[u].next[x]==-1){int v=trie.size();trie[u].next[x]=v;trie.emplace_back();}u=trie[u].next[x];trie[u].count++;}}vector<int>ans;for(auto&w:words){int u=0,sum=0;for(char c:w){u=trie[u].next[c-'a'];sum+=trie[u].count;}ans.push_back(sum);}return ans;}};
```


## 2452. Words Within Two Edits of Dictionary

**Problem:** https://leetcode.com/problems/words-within-two-edits-of-dictionary/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, String, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two string arrays, queries and dictionary . All words in each array comprise of lowercase English letters and have the same length. 
 
 In one edit you can take a word from queries , and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary . 
 
 Return a list of all words from queries , that match with some word from dictionary after a maximum of two edits . Return the words in the same order they appear in queries . 

 Example 1: 
 
```
Input:
 queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]

Output:
 ["word","note","wood"]

Explanation:

- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
- It would take more than 2 edits for "ants" to equal a dictionary word.
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return ["word","note","wood"].
```

 Example 2: 
 
```
Input:
 queries = ["yes"], dictionary = ["not"]

Output:
 []

Explanation:

Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.
```

 Constraints: 

 1 <= queries.length, dictionary.length <= 100 
 
 n == queries[i].length == dictionary[j].length 
 
 1 <= n <= 100 
 
 All queries[i] and dictionary[j] are composed of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: vector<string> twoEditWords(vector<string>& queries,vector<string>& dictionary){vector<string> ans;for(auto &q:queries)for(auto &d:dictionary){int diff=0;for(int i=0;i<(int)q.size();++i)diff+=q[i]!=d[i];if(diff<=2){ans.push_back(q);break;}}return ans;} };
```


## 2509. Cycle Length Queries in a Tree

**Problem:** https://leetcode.com/problems/cycle-length-queries-in-a-tree/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Tree, Binary Tree, Binary Lifting, Lowest Common Ancestor

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Binary tree, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer n . There is a complete binary tree with 2 n - 1 nodes. The root of that tree is the node with the value 1 , and every node with a value val in the range [1, 2 n - 1 - 1] has two children where: 

 The left node has the value 2 * val , and 
 
 The right node has the value 2 * val + 1 . 

 You are also given a 2D integer array queries of length m , where queries[i] = [a i , b i ] . For each query, solve the following problem: 

 Add an edge between the nodes with values a i and b i . 
 
 Find the length of the cycle in the graph. 
 
 Remove the added edge between nodes with values a i and b i . 

 Note that: 

 A cycle is a path that starts and ends at the same node, and each edge in the path is visited only once. 
 
 The length of a cycle is the number of edges visited in the cycle. 
 
 There could be multiple edges between two nodes in the tree after adding the edge of the query. 

 Return an array answer of length m where answer[i] is the answer to the i th query. 

 Example 1: 
 [Figure: https://assets.leetcode.com/uploads/2022/10/25/bexample1.png] 
 
```
Input:
 n = 3, queries = [[5,3],[4,7],[2,3]]

Output:
 [4,5,3]

Explanation:
 The diagrams above show the tree of 2
3
 - 1 nodes. Nodes colored in red describe the nodes in the cycle after adding the edge.
- After adding the edge between nodes 3 and 5, the graph contains a cycle of nodes [5,2,1,3]. Thus answer to the first query is 4. We delete the added edge and process the next query.
- After adding the edge between nodes 4 and 7, the graph contains a cycle of nodes [4,2,1,3,7]. Thus answer to the second query is 5. We delete the added edge and process the next query.
- After adding the edge between nodes 2 and 3, the graph contains a cycle of nodes [2,1,3]. Thus answer to the third query is 3. We delete the added edge.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/uploads/2022/10/25/aexample2.png] 
 
```
Input:
 n = 2, queries = [[1,2]]

Output:
 [2]

Explanation:
 The diagram above shows the tree of 2
2
 - 1 nodes. Nodes colored in red describe the nodes in the cycle after adding the edge.
- After adding the edge between nodes 1 and 2, the graph contains a cycle of nodes [2,1]. Thus answer for the first query is 2. We delete the added edge.
```

 Constraints: 

 2 <= n <= 30 
 
 m == queries.length 
 
 1 <= m <= 10 5 
 
 queries[i].length == 2 
 
 1 <= a i , b i <= 2 n - 1 
 
 a i != b i

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<int> cycleLengthQueries(int n,vector<vector<int>>& queries){vector<int>ans;for(auto&q:queries){int a=q[0],b=q[1],len=1;while(a!=b){if(a>b)a/=2;else b/=2;len++;}ans.push_back(len);}return ans;}};
```


## 2569. Handling Sum Queries After Update

**Problem:** https://leetcode.com/problems/handling-sum-queries-after-update/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two 0-indexed arrays nums1 and nums2 and a 2D array queries of queries. There are three types of queries: 

 For a query of type 1, queries[i] = [1, l, r] . Flip the values from 0 to 1 and from 1 to 0 in nums1  from index l to index r . Both l and r are 0-indexed . 
 
 For a query of type 2, queries[i] = [2, p, 0] . For every index 0 <= i < n , set  nums2[i] = nums2[i] + nums1[i] * p . 
 
 For a query of type 3, queries[i] = [3, 0, 0] . Find the sum of the elements in nums2 . 

 Return an array containing all the answers to the third type queries. 

 Example 1: 
 
```
Input:
 nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]

Output:
 [3]

Explanation:
 After the first query nums1 becomes [1,1,1]. After the second query, nums2 becomes [1,1,1], so the answer to the third query is 3. Thus, [3] is returned.
```

 Example 2: 
 
```
Input:
 nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]

Output:
 [5]

Explanation:
 After the first query, nums2 remains [5], so the answer to the second query is 5. Thus, [5] is returned.
```

 Constraints: 

 1 <= nums1.length,nums2.length <= 10 5 
 
 nums1.length = nums2.length 
 
 1 <= queries.length <= 10 5 
 
 queries[i].length = 3 
 
 0 <= l <= r <= nums1.length - 1 
 
 0 <= p <= 10 6 
 
 0 <= nums1[i] <= 1 
 
 0 <= nums2[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
 vector<int> ones,lazy; int n;
 void build(int p,int l,int r,vector<int>& a){if(l==r){ones[p]=a[l];return;}int m=(l+r)/2;build(p*2,l,m,a);build(p*2+1,m+1,r,a);ones[p]=ones[p*2]+ones[p*2+1];}
 void flip(int p,int l,int r){ones[p]=r-l+1-ones[p];lazy[p]^=1;}
 void push(int p,int l,int r){if(!lazy[p]||l==r)return;int m=(l+r)/2;flip(p*2,l,m);flip(p*2+1,m+1,r);lazy[p]=0;}
 void update(int p,int l,int r,int a,int b){if(a<=l&&r<=b){flip(p,l,r);return;}push(p,l,r);int m=(l+r)/2;if(a<=m)update(p*2,l,m,a,b);if(b>m)update(p*2+1,m+1,r,a,b);ones[p]=ones[p*2]+ones[p*2+1];}
public: vector<long long> handleQuery(vector<int>& nums1,vector<int>& nums2,vector<vector<int>>& queries){n=nums1.size();ones.assign(4*n,0);lazy.assign(4*n,0);build(1,0,n-1,nums1);long long sum=accumulate(nums2.begin(),nums2.end(),0LL);vector<long long> ans;for(auto &q:queries){if(q[0]==1)update(1,0,n-1,q[1],q[2]);else if(q[0]==2)sum+=1LL*q[1]*ones[1];else ans.push_back(sum);}return ans;}
};
```


## 2907. Maximum Profitable Triplets With Increasing Prices I

**Problem:** https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Binary Indexed Tree, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given the 0-indexed arrays prices and profits of length n . There are n items in an store where the i th item has a price of prices[i] and a profit of profits[i] . 
 
 We have to pick three items with the following condition: 

 prices[i] < prices[j] < prices[k] where i < j < k . 

 If we pick items with indices i , j and k satisfying the above condition, the profit would be profits[i] + profits[j] + profits[k] . 
 
 Return the maximum profit we can get, and -1 if it's not possible to pick three items with the given condition. 

 Example 1: 
 
```
Input:
 prices = [10,2,3,4], profits = [100,2,7,10]

Output:
 19

Explanation:
 We can't pick the item with index i=0 since there are no indices j and k such that the condition holds.
So the only triplet we can pick, are the items with indices 1, 2 and 3 and it's a valid pick since prices[1] < prices[2] < prices[3].
The answer would be sum of their profits which is 2 + 7 + 10 = 19.
```

 Example 2: 
 
```
Input:
 prices = [1,2,3,4,5], profits = [1,5,3,4,6]

Output:
 15

Explanation:
 We can select any triplet of items since for each triplet of indices i, j and k such that i < j < k, the condition holds.
Therefore the maximum profit we can get would be the 3 most profitable items which are indices 1, 3 and 4.
The answer would be sum of their profits which is 5 + 4 + 6 = 15.
```

 Example 3: 
 
```
Input:
 prices = [4,3,2,1], profits = [33,20,19,87]

Output:
 -1

Explanation:
 We can't select any triplet of indices such that the condition holds, so we return -1.
```

 Constraints: 

 3 <= prices.length == profits.length <= 2000 
 
 1 <= prices[i] <= 10 6 
 
 1 <= profits[i] <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices,vector<int>& profits) {
        int n=prices.size(),answer=-1;
        for(int j=1;j+1<n;++j) {
            int left=-1,right=-1;
            for(int i=0;i<j;++i)if(prices[i]<prices[j])left=max(left,profits[i]);
            for(int k=j+1;k<n;++k)if(prices[k]>prices[j])right=max(right,profits[k]);
            if(left!=-1&&right!=-1)answer=max(answer,left+profits[j]+right);
        }
        return answer;
    }
};
```


## 2913. Subarrays Distinct Element Sum of Squares I

**Problem:** https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, Hash Table, Binary Indexed Tree, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Hash map / hash set, Hash set, Ordered set, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 0-indexed integer array nums . 
 
 The distinct count of a subarray of nums is defined as: 

 Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length . Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j] . 

 Return the sum of the squares of distinct counts of all subarrays of nums . 
 
 A subarray is a contiguous non-empty sequence of elements within an array. 

 Example 1: 
 
```
Input:
 nums = [1,2,1]

Output:
 15

Explanation:
 Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1
2
 + 1
2
 + 1
2
 + 2
2
 + 2
2
 + 2
2
 = 15.
```

 Example 2: 
 
```
Input:
 nums = [1,1]

Output:
 3

Explanation:
 Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1
2
 + 1
2
 + 1
2
 = 3.
```

 Constraints: 

 1 <= nums.length <= 100 
 
 1 <= nums[i] <= 100

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution { public: int sumCounts(vector<int>& nums) { int ans=0,n=nums.size(); for(int i=0;i<n;i++){unordered_set<int> seen;for(int j=i;j<n;j++){seen.insert(nums[j]);int d=seen.size();ans+=d*d;}}return ans;} };
```


## 2916. Subarrays Distinct Element Sum of Squares II

**Problem:** https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, Binary Indexed Tree, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Hash map, Hash map / hash set, Ordered map, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 0-indexed integer array nums . 
 
 The distinct count of a subarray of nums is defined as: 

 Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length . Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j] . 

 Return the sum of the squares of distinct counts of all subarrays of nums . 
 
 Since the answer may be very large, return it modulo 10 9 + 7 . 
 
 A subarray is a contiguous non-empty sequence of elements within an array. 

 Example 1: 
 
```
Input:
 nums = [1,2,1]

Output:
 15

Explanation:
 Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1
2
 + 1
2
 + 1
2
 + 2
2
 + 2
2
 + 2
2
 = 15.
```

 Example 2: 
 
```
Input:
 nums = [2,2]

Output:
 3

Explanation:
 Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1
2
 + 1
2
 + 1
2
 = 3.
```

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {static const int MOD=1000000007;struct Node{long long sum=0,sq=0,lazy=0;};vector<Node> tr;void apply(int p,int l,int r,long long x){long long len=r-l+1;tr[p].sq=(tr[p].sq+2*x*tr[p].sum%MOD+x*x%MOD*len)%MOD;tr[p].sum=(tr[p].sum+x*len)%MOD;tr[p].lazy=(tr[p].lazy+x)%MOD;}void push(int p,int l,int r){if(tr[p].lazy&&l<r){int m=(l+r)/2;apply(p*2,l,m,tr[p].lazy);apply(p*2+1,m+1,r,tr[p].lazy);tr[p].lazy=0;}}void upd(int p,int l,int r,int ql,int qr){if(ql<=l&&r<=qr){apply(p,l,r,1);return;}push(p,l,r);int m=(l+r)/2;if(ql<=m)upd(p*2,l,m,ql,qr);if(qr>m)upd(p*2+1,m+1,r,ql,qr);tr[p].sum=(tr[p*2].sum+tr[p*2+1].sum)%MOD;tr[p].sq=(tr[p*2].sq+tr[p*2+1].sq)%MOD;}public:int sumCounts(vector<int>& nums){int n=nums.size();tr.assign(4*n+4,Node());unordered_map<int,int> last;long long ans=0;for(int i=0;i<n;i++){int start=last.count(nums[i])?last[nums[i]]+1:0;upd(1,0,n-1,start,i);last[nums[i]]=i;ans=(ans+tr[1].sq)%MOD;}return ans;}};
```


## 2921. Maximum Profitable Triplets With Increasing Prices II

**Problem:** https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Binary Indexed Tree, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given the 0-indexed arrays prices and profits of length n . There are n items in an store where the i th item has a price of prices[i] and a profit of profits[i] . 
 
 We have to pick three items with the following condition: 

 prices[i] < prices[j] < prices[k] where i < j < k . 

 If we pick items with indices i , j and k satisfying the above condition, the profit would be profits[i] + profits[j] + profits[k] . 
 
 Return the maximum profit we can get, and -1 if it's not possible to pick three items with the given condition. 

 Example 1: 
 
```
Input:
 prices = [10,2,3,4], profits = [100,2,7,10]

Output:
 19

Explanation:
 We can't pick the item with index i=0 since there are no indices j and k such that the condition holds.
So the only triplet we can pick, are the items with indices 1, 2 and 3 and it's a valid pick since prices[1] < prices[2] < prices[3].
The answer would be sum of their profits which is 2 + 7 + 10 = 19.
```

 Example 2: 
 
```
Input:
 prices = [1,2,3,4,5], profits = [1,5,3,4,6]

Output:
 15

Explanation:
 We can select any triplet of items since for each triplet of indices i, j and k such that i < j < k, the condition holds.
Therefore the maximum profit we can get would be the 3 most profitable items which are indices 1, 3 and 4.
The answer would be sum of their profits which is 5 + 4 + 6 = 15.
```

 Example 3: 
 
```
Input:
 prices = [4,3,2,1], profits = [33,20,19,87]

Output:
 -1

Explanation:
 We can't select any triplet of indices such that the condition holds, so we return -1.
```

 Constraints: 

 3 <= prices.length == profits.length <= 50000 
 
 1 <= prices[i] <= 5000 
 
 1 <= profits[i] <= 10 6

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    struct BIT {
        vector<int> t;
        BIT(int n) : t(n + 1, -1000000000) {}
        void update(int i, int v) { for (; i < (int)t.size(); i += i & -i) t[i] = max(t[i], v); }
        int query(int i) { int v = -1000000000; for (; i; i -= i & -i) v = max(v, t[i]); return v; }
    };
public:
    int maxProfit(vector<int>& prices, vector<int>& profits) {
        vector<int> vals = prices;
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        int n = prices.size(), m = vals.size();
        vector<int> left(n), right(n);
        BIT bit(m);
        for (int i = 0; i < n; ++i) {
            int r = lower_bound(vals.begin(), vals.end(), prices[i]) - vals.begin() + 1;
            left[i] = bit.query(r - 1);
            bit.update(r, profits[i]);
        }
        BIT rev(m);
        for (int i = n - 1; i >= 0; --i) {
            int r = lower_bound(vals.begin(), vals.end(), prices[i]) - vals.begin() + 1;
            right[i] = rev.query(m - r);
            rev.update(m - r + 1, profits[i]);
        }
        int ans = -1;
        for (int i = 0; i < n; ++i) if (left[i] >= 0 && right[i] >= 0) ans = max(ans, left[i] + profits[i] + right[i]);
        return ans;
    }
};
```


## 3009. Maximum Number of Intersections on the Chart

**Problem:** https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Hash Table, Math, Binary Indexed Tree, Geometry, Sweep Line, Sorting

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Math / Number Theory, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Hash map / hash set, Ordered map, Sorted array, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There is a line chart consisting of n points connected by line segments. You are given a 1-indexed integer array y . The k th point has coordinates (k, y[k]) . There are no horizontal lines; that is, no two consecutive points have the same y-coordinate. 
 
 We can draw an infinitely long horizontal line. Return the maximum number of points of intersection of the line with the chart . 

 Example 1: 
 [Figure: https://assets.leetcode.com/static_assets/others/20231208-020549.jpeg] 
 
```
Input:
 y = [1,2,1,2,1,3,2]

Output:
 5

Explanation:
 As you can see in the image above, the line y = 1.5 has 5 intersections with the chart (in red crosses). You can also see the line y = 2 which intersects the chart in 4 points (in red crosses). It can be shown that there is no horizontal line intersecting the chart at more than 5 points. So the answer would be 5.
```

 Example 2: 
 [Figure: https://assets.leetcode.com/static_assets/others/20231208-020557.jpeg] 
 
```
Input:
 y = [2,1,3,4,5]

Output:
 2

Explanation:
 As you can see in the image above, the line y = 1.5 has 2 intersections with the chart (in red crosses). You can also see the line y = 2 which intersects the chart in 2 points (in red crosses). It can be shown that there is no horizontal line intersecting the chart at more than 2 points. So the answer would be 2.
```

 Constraints: 

 2 <= y.length <= 10 5 
 
 1 <= y[i] <= 10 9 
 
 y[i] != y[i + 1] for i in range [1, n - 1]

### C++ solution

**Source:** accepted_cpp_submission

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


## 3042. Count Prefix and Suffix Pairs I

**Problem:** https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

**Difficulty:** Easy | **Premium:** No

**Tags:** Array, String, Trie, Rolling Hash, String Matching, Hash Function

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 0-indexed string array words . 
 
 Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2 : 

 isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2 , and false otherwise. 

 For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false . 
 
 Return an integer denoting the number of index pairs (i, j) such that i < j , and isPrefixAndSuffix(words[i], words[j]) is true . 

 Example 1: 
 
```
Input:
 words = ["a","aba","ababa","aa"]

Output:
 4

Explanation:
 In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
Therefore, the answer is 4.
```

 Example 2: 
 
```
Input:
 words = ["pa","papa","ma","mama"]

Output:
 2

Explanation:
 In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("pa", "papa") is true.
i = 2 and j = 3 because isPrefixAndSuffix("ma", "mama") is true.
Therefore, the answer is 2.
```

 Example 3: 
 
```
Input:
 words = ["abab","ab"]

Output:
 0

Explanation: 
In this example, the only valid index pair is i = 0 and j = 1, and isPrefixAndSuffix("abab", "ab") is false.
Therefore, the answer is 0.
```

 Constraints: 

 1 <= words.length <= 50 
 
 1 <= words[i].length <= 10 
 
 words[i] consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int countPrefixSuffixPairs(vector<string>&words){int ans=0;for(int i=0;i<(int)words.size();i++)for(int j=i+1;j<(int)words.size();j++){string&a=words[i],&b=words[j];int n=a.size(),m=b.size();if(n<=m&&b.compare(0,n,a)==0&&b.compare(m-n,n,a)==0)ans++;}return ans;}};
```


## 3043. Find the Length of the Longest Common Prefix

**Problem:** https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, String, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Hash set, Ordered set, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two arrays with positive integers arr1 and arr2 . 
 
 A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345 , while 234 is not . 
 
 A common prefix of two integers a and b is an integer c , such that c is a prefix of both a and b . For example, 5655359 and 56554 have common prefixes 565 and 5655 while 1223 and 43456 do not have a common prefix. 
 
 You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2 . 
 
 Return the length of the longest common prefix among all pairs . If no common prefix exists among them , return 0 . 

 Example 1: 
 
```
Input:
 arr1 = [1,10,100], arr2 = [1000]

Output:
 3

Explanation:
 There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.
```

 Example 2: 
 
```
Input:
 arr1 = [1,2,3], arr2 = [4,4,4]

Output:
 0

Explanation:
 There exists no common prefix for any pair (arr1[i], arr2[j]), hence we return 0.
Note that common prefixes between elements of the same array do not count.
```

 Constraints: 

 1 <= arr1.length, arr2.length <= 5 * 10 4 
 
 1 <= arr1[i], arr2[i] <= 10 8

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int longestCommonPrefix(vector<int>&arr1,vector<int>&arr2){unordered_set<string>st;for(int x:arr1){string s=to_string(x);for(int j=1;j<=(int)s.size();j++)st.insert(s.substr(0,j));}int ans=0;for(int x:arr2){string s=to_string(x);for(int j=1;j<=(int)s.size();j++)if(st.count(s.substr(0,j)))ans=max(ans,j);}return ans;}};
```


## 3045. Count Prefix and Suffix Pairs II

**Problem:** https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, String, Trie, Rolling Hash, String Matching, Hash Function, Z Algorithm

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Ordered map, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 0-indexed string array words . 
 
 Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2 : 

 isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2 , and false otherwise. 

 For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false . 
 
 Return an integer denoting the number of index pairs (i , j) such that i < j , and isPrefixAndSuffix(words[i], words[j]) is true . 

 Example 1: 
 
```
Input:
 words = ["a","aba","ababa","aa"]

Output:
 4

Explanation:
 In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
Therefore, the answer is 4.
```

 Example 2: 
 
```
Input:
 words = ["pa","papa","ma","mama"]

Output:
 2

Explanation:
 In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("pa", "papa") is true.
i = 2 and j = 3 because isPrefixAndSuffix("ma", "mama") is true.
Therefore, the answer is 2.
```

 Example 3: 
 
```
Input:
 words = ["abab","ab"]

Output:
 0

Explanation: 
In this example, the only valid index pair is i = 0 and j = 1, and isPrefixAndSuffix("abab", "ab") is false.
Therefore, the answer is 0.
```

 Constraints: 

 1 <= words.length <= 10 5 
 
 1 <= words[i].length <= 10 5 
 
 words[i] consists only of lowercase English letters. 
 
 The sum of the lengths of all words[i] does not exceed 5 * 10 5 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {struct Node{unordered_map<int,int>next;int ends=0;};public:long long countPrefixSuffixPairs(vector<string>&words){vector<Node>tr(1);long long ans=0;for(const string&s:words){int u=0,n=s.size();for(int i=0;i<n;i++){int key=(s[i]-'a')*26+s[n-1-i]-'a';auto it=tr[u].next.find(key);if(it==tr[u].next.end()){int id=tr.size();tr[u].next[key]=id;tr.emplace_back();u=id;}else u=it->second;ans+=tr[u].ends;}tr[u].ends++;}return ans;}};
```


## 3072. Distribute Elements Into Two Arrays II

**Problem:** https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Binary Indexed Tree, Segment Tree, Simulation

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a 1-indexed array of integers nums of length n . 
 
 We define a function greaterCount such that greaterCount(arr, val) returns the number of elements in arr that are strictly greater than val . 
 
 You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1 . In the second operation, append nums[2] to arr2 . Afterwards, in the i th operation: 

 If greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]) , append nums[i] to arr1 . 
 
 If greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]) , append nums[i] to arr2 . 
 
 If greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]) , append nums[i] to the array with a lesser number of elements. 
 
 If there is still a tie, append nums[i] to arr1 . 

 The array result is formed by concatenating the arrays arr1 and arr2 . For example, if arr1 == [1,2,3] and arr2 == [4,5,6] , then result = [1,2,3,4,5,6] . 
 
 Return the integer array result . 

 Example 1: 
 
```
Input:
 nums = [2,1,3,3]

Output:
 [2,3,1,3]

Explanation:
 After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3
rd
 operation, the number of elements greater than 3 is zero in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
In the 4
th
 operation, the number of elements greater than 3 is zero in both arrays. As the length of arr2 is lesser, hence, append nums[4] to arr2.
After 4 operations, arr1 = [2,3] and arr2 = [1,3].
Hence, the array result formed by concatenation is [2,3,1,3].
```

 Example 2: 
 
```
Input:
 nums = [5,14,3,1,2]

Output:
 [5,3,1,2,14]

Explanation:
 After the first 2 operations, arr1 = [5] and arr2 = [14].
In the 3
rd
 operation, the number of elements greater than 3 is one in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
In the 4
th
 operation, the number of elements greater than 1 is greater in arr1 than arr2 (2 > 1). Hence, append nums[4] to arr1.
In the 5
th
 operation, the number of elements greater than 2 is greater in arr1 than arr2 (2 > 1). Hence, append nums[5] to arr1.
After 5 operations, arr1 = [5,3,1,2] and arr2 = [14].
Hence, the array result formed by concatenation is [5,3,1,2,14].
```

 Example 3: 
 
```
Input:
 nums = [3,3,3,3]

Output:
 [3,3,3,3]

Explanation:
 At the end of 4 operations, arr1 = [3,3] and arr2 = [3,3].
Hence, the array result formed by concatenation is [3,3,3,3].
```

 Constraints: 

 3 <= n <= 10 5 
 
 1 <= nums[i] <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
 struct BIT {vector<int> t; BIT(int n):t(n+1){} void add(int i){for(int n=t.size();i<n;i+=i&-i)++t[i];} int sum(int i){int s=0;for(;i;i-=i&-i)s+=t[i];return s;}};
public: vector<int> resultArray(vector<int>& nums) {
 vector<int> vals=nums;sort(vals.begin(),vals.end());vals.erase(unique(vals.begin(),vals.end()),vals.end());
 int n=nums.size(),m=vals.size();BIT a(m),b(m);vector<int> x{nums[0]},y{nums[1]};
 auto idx=[&](int v){return int(lower_bound(vals.begin(),vals.end(),v)-vals.begin())+1;};
 a.add(idx(nums[0]));b.add(idx(nums[1]));
 for(int i=2;i<n;i++){int p=idx(nums[i]),ca=(int)x.size()-a.sum(p),cb=(int)y.size()-b.sum(p);
 if(ca>cb||(ca==cb&&x.size()<=y.size())){x.push_back(nums[i]);a.add(p);}else{y.push_back(nums[i]);b.add(p);}}
 x.insert(x.end(),y.begin(),y.end());return x;
}};
```


## 3076. Shortest Uncommon Substring in an Array

**Problem:** https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, String, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map, Hash map / hash set, Hash set, Ordered map, Ordered set, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array arr of size n consisting of non-empty strings. 
 
 Find a string array answer of size n such that: 

 answer[i] is the shortest substring of arr[i] that does not occur as a substring in any other string in arr . If multiple such substrings exist, answer[i] should be the lexicographically smallest . And if no such substring exists, answer[i] should be an empty string. 

 Return the array answer . 

 Example 1: 
 
```
Input:
 arr = ["cab","ad","bad","c"]

Output:
 ["ab","","ba",""]

Explanation:
 We have the following:
- For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
- For the string "ad", there is no substring that does not occur in any other string.
- For the string "bad", the shortest substring that does not occur in any other string is "ba".
- For the string "c", there is no substring that does not occur in any other string.
```

 Example 2: 
 
```
Input:
 arr = ["abc","bcd","abcd"]

Output:
 ["","","abcd"]

Explanation:
 We have the following:
- For the string "abc", there is no substring that does not occur in any other string.
- For the string "bcd", there is no substring that does not occur in any other string.
- For the string "abcd", the shortest substring that does not occur in any other string is "abcd".
```

 Constraints: 

 n == arr.length 
 
 2 <= n <= 100 
 
 1 <= arr[i].length <= 20 
 
 arr[i] consists only of lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:vector<string> shortestSubstrings(vector<string>& arr){
 unordered_map<string,int> count;
 for(auto &s:arr){unordered_set<string> seen;for(int i=0;i<(int)s.size();i++)for(int len=1;i+len<=(int)s.size();len++)seen.insert(s.substr(i,len));for(auto &v:seen)++count[v];}
 vector<string> ans;for(auto &s:arr){string best="";for(int i=0;i<(int)s.size();i++)for(int len=1;i+len<=(int)s.size();len++){
 string v=s.substr(i,len);if(count[v]==1&&(best.empty()||v.size()<best.size()||(v.size()==best.size()&&v<best)))best=v;
 }ans.push_back(best);}return ans;
}};
```


## 3093. Longest Common Suffix Queries

**Problem:** https://leetcode.com/problems/longest-common-suffix-queries/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, String, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given two arrays of strings wordsContainer and wordsQuery . 
 
 For each wordsQuery[i] , you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i] . If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer . 
 
 Return an array of integers ans , where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i] . 

 Example 1: 

 Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"] 
 
 Output: [1,1,1] 
 
 Explanation: 
 
 Let's look at each wordsQuery[i] separately: 

 For wordsQuery[0] = "cd" , strings from wordsContainer that share the longest common suffix "cd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3. 
 
 For wordsQuery[1] = "bcd" , strings from wordsContainer that share the longest common suffix "bcd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3. 
 
 For wordsQuery[2] = "xyz" , there is no string from wordsContainer that shares a common suffix. Hence the longest common suffix is "" , that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3. 

 Example 2: 

 Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"] 
 
 Output: [2,0,2] 
 
 Explanation: 
 
 Let's look at each wordsQuery[i] separately: 

 For wordsQuery[0] = "gh" , strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6. 
 
 For wordsQuery[1] = "acbfgh" , only the string at index 0 shares the longest common suffix "fgh" . Hence it is the answer, even though the string at index 2 is shorter. 
 
 For wordsQuery[2] = "acbfegh" , strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6. 

 Constraints: 

 1 <= wordsContainer.length, wordsQuery.length <= 10 4 
 
 1 <= wordsContainer[i].length <= 5 * 10 3 
 
 1 <= wordsQuery[i].length <= 5 * 10 3 
 
 wordsContainer[i] consists only of lowercase English letters. 
 
 wordsQuery[i] consists only of lowercase English letters. 
 
 Sum of wordsContainer[i].length is at most 5 * 10 5 . 
 
 Sum of wordsQuery[i].length is at most 5 * 10 5 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {struct Node{int nxt[26],best;Node():best(-1){fill(nxt,nxt+26,-1);}};
public:vector<int> stringIndices(vector<string>& wordsContainer,vector<string>& wordsQuery){
 vector<Node> t(1);auto improve=[&](int u,int i){int old=t[u].best;if(old==-1||wordsContainer[i].size()<wordsContainer[old].size())t[u].best=i;};
 for(int i=0;i<(int)wordsContainer.size();i++){int u=0;improve(u,i);for(auto it=wordsContainer[i].rbegin();it!=wordsContainer[i].rend();it++){
 int c=*it-'a';if(t[u].nxt[c]==-1){int id=t.size();t[u].nxt[c]=id;t.emplace_back();}u=t[u].nxt[c];improve(u,i);}}
 vector<int> ans;for(auto &s:wordsQuery){int u=0;for(auto it=s.rbegin();it!=s.rend();it++){int v=t[u].nxt[*it-'a'];if(v==-1)break;u=v;}ans.push_back(t[u].best);}return ans;
}};
```


## 3187. Peaks in Array

**Problem:** https://leetcode.com/problems/peaks-in-array/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Binary Indexed Tree, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

A peak in an array arr is an element that is greater than its previous and next element in arr . 
 
 You are given an integer array nums and a 2D integer array queries . 
 
 You have to process queries of two types: 

 queries[i] = [1, l i , r i ] , determine the count of peak elements in the subarray nums[l i ..r i ] . 
 
 queries[i] = [2, index i , val i ] , change nums[index i ] to val i . 

 Return an array answer containing the results of the queries of the first type in order. 
 
 Notes: 

 The first and the last element of an array or a subarray cannot be a peak. 

 Example 1: 

 Input: nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]] 
 
 Output: [0] 
 
 Explanation: 
 
 First query: We change nums[3] to 4 and nums becomes [3,1,4,4,5] . 
 
 Second query: The number of peaks in the [3,1,4,4,5] is 0. 

 Example 2: 

 Input: nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]] 
 
 Output: [0,1] 
 
 Explanation: 
 
 First query: nums[2] should become 4, but it is already set to 4. 
 
 Second query: The number of peaks in the [4,1,4] is 0. 
 
 Third query: The second 4 is a peak in the [4,1,4,2,1] . 

 Constraints: 

 3 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 5 
 
 1 <= queries.length <= 10 5 
 
 queries[i][0] == 1 or queries[i][0] == 2 
 
 For all i that:

 queries[i][0] == 1 : 0 <= queries[i][1] <= queries[i][2] <= nums.length - 1 
 
 queries[i][0] == 2 : 0 <= queries[i][1] <= nums.length - 1 , 1 <= queries[i][2] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {struct BIT{int n;vector<int>b;BIT(int n):n(n),b(n+1){}void add(int i,int v){for(++i;i<=n;i+=i&-i)b[i]+=v;}int sum(int i){int r=0;for(++i;i>0;i-=i&-i)r+=b[i];return r;}int range(int l,int r){return l>r?0:sum(r)-(l?sum(l-1):0);}};public:vector<int> countOfPeaks(vector<int>& nums,vector<vector<int>>& queries){int n=nums.size();BIT ft(n);vector<int>p(n);auto peak=[&](int i){return i>0&&i<n-1&&nums[i]>nums[i-1]&&nums[i]>nums[i+1];};for(int i=1;i<n-1;++i){p[i]=peak(i);ft.add(i,p[i]);}vector<int>ans;for(auto&q:queries){if(q[0]==1)ans.push_back(ft.range(q[1]+1,q[2]-1));else{int idx=q[1];nums[idx]=q[2];for(int i=max(1,idx-1);i<=min(n-2,idx+1);++i){int v=peak(i);ft.add(i,v-p[i]);p[i]=v;}}}return ans;}};
```


## 3245. Alternating Groups III

**Problem:** https://leetcode.com/problems/alternating-groups-iii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Binary Indexed Tree, Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Ordered set, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There are some red and blue tiles arranged circularly. You are given an array of integers colors and a 2D integers array queries . 
 
 The color of tile i is represented by colors[i] : 

 colors[i] == 0 means that tile i is red . 
 
 colors[i] == 1 means that tile i is blue . 

 An alternating group is a contiguous subset of tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its adjacent tiles in the group). 
 
 You have to process queries of two types: 

 queries[i] = [1, size i ] , determine the count of alternating groups with size size i . 
 
 queries[i] = [2, index i , color i ] , change colors[index i ] to color i . 

 Return an array answer containing the results of the queries of the first type in order . 
 
 Note that since colors represents a circle , the first and the last tiles are considered to be next to each other. 

 Example 1: 

 Input: colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]] 
 
 Output: [2] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-14-44.png] 
 
 First query: 
 
 Change colors[1] to 0. 
 
 [Figure: https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-20-25.png] 
 
 Second query: 
 
 Count of the alternating groups with size 4: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-25-02-2.png] [Figure: https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-24-12.png] 

 Example 2: 

 Input: colors = [0,0,1,0,1,1], queries = [[1,3],[2,3,0],[1,5]] 
 
 Output: [2,0] 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-35-50.png] 
 
 First query: 
 
 Count of the alternating groups with size 3: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-37-13.png] [Figure: https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-36-40.png] 
 
 Second query: colors will not change. 
 
 Third query: There is no alternating group with size 5. 

 Constraints: 

 4 <= colors.length <= 5 * 10 4 
 
 0 <= colors[i] <= 1 
 
 1 <= queries.length <= 5 * 10 4 
 
 queries[i][0] == 1 or queries[i][0] == 2 
 
 For all i that:

 queries[i][0] == 1 : queries[i].length == 2 , 3 <= queries[i][1] <= colors.length - 1 
 
 queries[i][0] == 2 : queries[i].length == 3 , 0 <= queries[i][1] <= colors.length - 1 , 0 <= queries[i][2] <= 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
 struct BIT {int n;vector<long long> t;BIT(int n):n(n),t(n+1){}void add(int i,long long v){for(;i<=n;i+=i&-i)t[i]+=v;}long long sum(int i){long long s=0;for(;i>0;i-=i&-i)s+=t[i];return s;}};
public:
 vector<int> numberOfAlternatingGroups(vector<int>& colors,vector<vector<int>>& queries){
  int n=colors.size();set<int> breaks;BIT count(n),length(n);
  auto insertRun=[&](int len,int sign){count.add(len,sign);length.add(len,1LL*sign*len);};
  for(int i=0;i<n;++i)if(colors[i]==colors[(i+1)%n])breaks.insert(i);
  auto runLen=[&](int a,int b){int d=(b-a+n)%n;return d?d:n;};
  if(!breaks.empty()){for(int a:breaks){auto it=breaks.upper_bound(a);int b=it==breaks.end()?*breaks.begin():*it;insertRun(runLen(a,b),1);}}
  auto toggle=[&](int x,bool add){if(add){if(breaks.empty()){breaks.insert(x);insertRun(n,1);return;}auto it=breaks.lower_bound(x);int b=it==breaks.end()?*breaks.begin():*it;int a=it==breaks.begin()?*breaks.rbegin():*prev(it);insertRun(runLen(a,b),-1);insertRun(runLen(a,x),1);insertRun(runLen(x,b),1);breaks.insert(x);}else{if(breaks.size()==1){insertRun(n,-1);breaks.erase(x);return;}auto it=breaks.find(x);int a=it==breaks.begin()?*breaks.rbegin():*prev(it);int b=next(it)==breaks.end()?*breaks.begin():*next(it);insertRun(runLen(a,x),-1);insertRun(runLen(x,b),-1);insertRun(runLen(a,b),1);breaks.erase(it);}};
  vector<int> ans;for(auto &q:queries){if(q[0]==1){int k=q[1];if(breaks.empty())ans.push_back(n);else if(k>n)ans.push_back(0);else{long long c=count.sum(n)-count.sum(k-1),s=length.sum(n)-length.sum(k-1);ans.push_back((int)(s-(k-1)*c));}}
   else{int i=q[1],v=q[2];if(colors[i]==v)continue;int a=(i-1+n)%n,b=i;bool oldA=colors[a]==colors[i],oldB=colors[i]==colors[(i+1)%n];if(oldA)toggle(a,false);if(oldB)toggle(b,false);colors[i]=v;if(colors[a]==colors[i])toggle(a,true);if(colors[i]==colors[(i+1)%n])toggle(b,true);}}
  return ans;
 }
};
```


## 3380. Maximum Area Rectangle With Point Constraints I

**Problem:** https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Math, Binary Indexed Tree, Segment Tree, Geometry, Sorting, Enumeration

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Math / Number Theory, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Ordered set, Segment tree, Sorted array, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array points where points[i] = [x i , y i ] represents the coordinates of a point on an infinite plane. 
 
 Your task is to find the maximum area of a rectangle that: 

 Can be formed using four of these points as its corners. 
 
 Does not contain any other point inside or on its border. 
 
 Has its edges  parallel to the axes. 

 Return the maximum area that you can obtain or -1 if no such rectangle is possible. 

 Example 1: 

 Input: points = [[1,1],[1,3],[3,1],[3,3]] 
 
 Output: 4 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2026/02/23/3380_ex0.png] 
 
 We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border . Hence, the maximum possible area would be 4. 

 Example 2: 

 Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]] 
 
 Output: -1 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2026/02/23/3380_ex1.png] 
 
 There is only one rectangle possible is with points [1,1], [1,3], [3,1] and [3,3] but [2,2] will always lie inside it. Hence, returning -1. 

 Example 3: 

 Input: points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]] 
 
 Output: 2 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2026/02/23/3380_ex2.png] 
 
 The maximum area rectangle is formed by the points [1,3], [1,2], [3,2], [3,3] , which has an area of 2. Additionally, the points [1,1], [1,2], [3,1], [3,2] also form a valid rectangle with the same area. 

 Constraints: 

 1 <= points.length <= 10 
 
 points[i].length == 2 
 
 0 <= x i , y i <= 100 
 
 All the given points are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:int maxRectangleArea(vector<vector<int>>&points){int n=points.size(),ans=-1;set<pair<int,int>>s;for(auto&p:points)s.insert({p[0],p[1]});for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){int x1=min(points[i][0],points[j][0]),x2=max(points[i][0],points[j][0]),y1=min(points[i][1],points[j][1]),y2=max(points[i][1],points[j][1]);if(x1==x2||y1==y2||!s.count({x1,y1})||!s.count({x1,y2})||!s.count({x2,y1})||!s.count({x2,y2}))continue;int cnt=0;for(auto&p:points)if(p[0]>=x1&&p[0]<=x2&&p[1]>=y1&&p[1]<=y2)cnt++;if(cnt==4)ans=max(ans,(x2-x1)*(y2-y1));}return ans;}};
```


## 3382. Maximum Area Rectangle With Point Constraints II

**Problem:** https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Math, Binary Indexed Tree, Segment Tree, Geometry, Sorting

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Math / Number Theory, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Ordered map, Segment tree, Sorted array, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

There are n points on an infinite plane. You are given two integer arrays xCoord and yCoord where (xCoord[i], yCoord[i]) represents the coordinates of the i th point. 
 
 Your task is to find the maximum area of a rectangle that: 

 Can be formed using four of these points as its corners. 
 
 Does not contain any other point inside or on its border. 
 
 Has its edges  parallel to the axes. 

 Return the maximum area that you can obtain or -1 if no such rectangle is possible. 

 Example 1: 

 Input: xCoord = [1,1,3,3], yCoord = [1,3,1,3] 
 
 Output: 4 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/11/02/example1.png] 
 
 We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border. Hence, the maximum possible area would be 4. 

 Example 2: 

 Input: xCoord = [1,1,3,3,2], yCoord = [1,3,1,3,2] 
 
 Output: -1 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/11/02/example2.png] 
 
 There is only one rectangle possible is with points [1,1], [1,3], [3,1] and [3,3] but [2,2] will always lie inside it. Hence, returning -1. 

 Example 3: 

 Input: xCoord = [1,1,3,3,1,3], yCoord = [1,3,1,3,2,2] 
 
 Output: 2 
 
 Explanation: 
 
 [Figure: https://assets.leetcode.com/uploads/2024/11/02/example3.png] 
 
 The maximum area rectangle is formed by the points [1,3], [1,2], [3,2], [3,3] , which has an area of 2. Additionally, the points [1,1], [1,2], [3,1], [3,2] also form a valid rectangle with the same area. 

 Constraints: 

 1 <= xCoord.length == yCoord.length <= 2 * 10 5 
 
 0 <= xCoord[i], yCoord[i] <= 8 * 10 7 
 
 All the given points are unique .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {struct BIT{int n;vector<int>b;BIT(int n):n(n),b(n+1){}void add(int i){for(++i;i<=n;i+=i&-i)b[i]++;}int sum(int i){int s=0;for(++i;i>0;i-=i&-i)s+=b[i];return s;}int range(int l,int r){return sum(r)-(l?sum(l-1):0);}};public:long long maxRectangleArea(vector<int>&xCoord,vector<int>&yCoord){int n=xCoord.size();vector<int>ys=yCoord;sort(ys.begin(),ys.end());ys.erase(unique(ys.begin(),ys.end()),ys.end());map<int,vector<int>>cols;for(int i=0;i<n;i++)cols[xCoord[i]].push_back(lower_bound(ys.begin(),ys.end(),yCoord[i])-ys.begin());BIT bit(ys.size());map<pair<int,int>,pair<int,int>>last;long long ans=-1;for(auto &entry:cols){int x=entry.first;auto &v=entry.second;sort(v.begin(),v.end());for(int y:v)bit.add(y);for(int i=1;i<(int)v.size();i++){int a=v[i-1],b=v[i];auto key=make_pair(a,b);int cnt=bit.range(a,b);auto it=last.find(key);if(it!=last.end()&&cnt-it->second.second==2){long long area=1LL*(x-it->second.first)*(ys[b]-ys[a]);ans=max(ans,area);}last[key]={x,cnt};}}return ans;}};
```


## 3480. Maximize Subarrays After Removing One Conflicting Pair

**Problem:** https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Segment Tree, Enumeration, Prefix Sum

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Prefix Sum / Difference Array, Simulation / Implementation

**Data structures (inferred):** Array / vector, Prefix-sum array, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer n which represents an array nums containing the numbers from 1 to n in order. Additionally, you are given a 2D array conflictingPairs , where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair. 
 
 Remove exactly one element from conflictingPairs . Afterward, count the number of non-empty subarrays of nums which do not contain both a and b for any remaining conflicting pair [a, b] . 
 
 Return the maximum number of subarrays possible after removing exactly one conflicting pair. 

 Example 1: 

 Input: n = 4, conflictingPairs = [[2,3],[1,4]] 
 
 Output: 9 
 
 Explanation: 

 Remove [2, 3] from conflictingPairs . Now, conflictingPairs = [[1, 4]] . 
 
 There are 9 subarrays in nums where [1, 4] do not appear together. They are [1] , [2] , [3] , [4] , [1, 2] , [2, 3] , [3, 4] , [1, 2, 3] and [2, 3, 4] . 
 
 The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 9. 

 Example 2: 

 Input: n = 5, conflictingPairs = [[1,2],[2,5],[3,5]] 
 
 Output: 12 
 
 Explanation: 

 Remove [1, 2] from conflictingPairs . Now, conflictingPairs = [[2, 5], [3, 5]] . 
 
 There are 12 subarrays in nums where [2, 5] and [3, 5] do not appear together. 
 
 The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 12. 

 Constraints: 

 2 <= n <= 10 5 
 
 1 <= conflictingPairs.length <= 2 * n 
 
 conflictingPairs[i].length == 2 
 
 1 <= conflictingPairs[i][j] <= n 
 
 conflictingPairs[i][0] != conflictingPairs[i][1]

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:long long maxSubarrays(int n,vector<vector<int>>& conflictingPairs){vector<vector<pair<int,int>>> at(n+1);int q=conflictingPairs.size();for(int i=0;i<q;i++){int a=min(conflictingPairs[i][0],conflictingPairs[i][1]),b=max(conflictingPairs[i][0],conflictingPairs[i][1]);at[b].push_back({a,i});}long long base=0;vector<long long> gain(q);int first=0,second=0,who=-1;for(int r=1;r<=n;r++){for(auto e:at[r]){int x=e.first,id=e.second;if(x>first){second=first;first=x;who=id;}else if(x>second)second=x;}base+=r-first;if(who!=-1)gain[who]+=first-second;}return base+*max_element(gain.begin(),gain.end());}};
```


## 3485. Longest Common Prefix of K Strings After Removal

**Problem:** https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, String, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Array / vector, Ordered set, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array of strings words and an integer k . 
 
 For each index i in the range [0, words.length - 1] , find the length of the longest common prefix among any k strings (selected at distinct indices ) from the remaining array after removing the i th element. 
 
 Return an array answer , where answer[i] is the answer for i th element. If removing the i th element leaves the array with fewer than k strings, answer[i] is 0. 

 Example 1: 

 Input: words = ["jump","run","run","jump","run"], k = 2 
 
 Output: [3,4,4,3,4] 
 
 Explanation: 

 Removing index 0 ( "jump" ):

 words becomes: ["run", "run", "jump", "run"] . "run" occurs 3 times. Choosing any two gives the longest common prefix "run" (length 3). 

 Removing index 1 ( "run" ):

 words becomes: ["jump", "run", "jump", "run"] . "jump" occurs twice. Choosing these two gives the longest common prefix "jump" (length 4). 

 Removing index 2 ( "run" ):

 words becomes: ["jump", "run", "jump", "run"] . "jump" occurs twice. Choosing these two gives the longest common prefix "jump" (length 4). 

 Removing index 3 ( "jump" ):

 words becomes: ["jump", "run", "run", "run"] . "run" occurs 3 times. Choosing any two gives the longest common prefix "run" (length 3). 

 Removing index 4 ("run"):

 words becomes: ["jump", "run", "run", "jump"] . "jump" occurs twice. Choosing these two gives the longest common prefix "jump" (length 4). 

 Example 2: 

 Input: words = ["dog","racer","car"], k = 2 
 
 Output: [0,0,0] 
 
 Explanation: 

 Removing any index results in an answer of 0. 

 Constraints: 

 1 <= k <= words.length <= 10 5 
 
 1 <= words[i].length <= 10 4 
 
 words[i] consists of lowercase English letters. 
 
 The sum of words[i].length is smaller than or equal 10 5 .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {struct Node{int ch[26],cnt,dep;Node(int d=0):cnt(0),dep(d){fill(ch,ch+26,-1);}};public:vector<int> longestCommonPrefix(vector<string>&words,int k){int n=words.size();vector<int> ans(n);if(n<=k)return ans;vector<Node> tr(1);vector<vector<int>> paths(n);int maxD=0;for(int i=0;i<n;i++){int u=0;for(char c:words[i]){int t=c-'a';if(tr[u].ch[t]<0){int id=tr.size();tr[u].ch[t]=id;tr.emplace_back(tr[u].dep+1);}u=tr[u].ch[t];tr[u].cnt++;paths[i].push_back(u);maxD=max(maxD,tr[u].dep);}}vector<int> good(maxD+1);for(auto &v:tr)if(v.dep&&v.cnt>=k)good[v.dep]++;set<int> depths;for(int d=1;d<=maxD;d++)if(good[d])depths.insert(d);for(int i=0;i<n;i++){vector<int> gone;for(int u:paths[i])if(tr[u].cnt==k&&good[tr[u].dep]==1){depths.erase(tr[u].dep);gone.push_back(tr[u].dep);}ans[i]=depths.empty()?0:*depths.rbegin();for(int d:gone)depths.insert(d);}return ans;}};
```


## 3491. Phone Number Prefix

**Problem:** https://leetcode.com/problems/phone-number-prefix/

**Difficulty:** Easy | **Premium:** Yes

**Tags:** Array, String, Trie, Sorting

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Sorted array, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string array numbers that represents phone numbers. Return true if no phone number is a prefix of any other phone number; otherwise, return false . 

 Example 1: 

 Input: numbers = ["1","2","4","3"] 
 
 Output: true 
 
 Explanation: 
 
 No number is a prefix of another number, so the output is true . 

 Example 2: 

 Input: numbers = ["001","007","15","00153"] 
 
 Output: false 
 
 Explanation: 
 
 The string "001" is a prefix of the string "00153" . Thus, the output is false . 

 Constraints: 

 2 <= numbers.length <= 50 
 
 1 <= numbers[i].length <= 50 
 
 All numbers contain only digits '0' to '9' .

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    bool phonePrefix(vector<string>& numbers) {
        sort(numbers.begin(), numbers.end());
        for (int i = 1; i < (int)numbers.size(); ++i) {
            const string& a = numbers[i - 1];
            const string& b = numbers[i];
            if (b.compare(0, a.size(), a) == 0) return false;
        }
        return true;
    }
};
```


## 3525. Find X Value of Array II

**Problem:** https://leetcode.com/problems/find-x-value-of-array-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Math, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** Array / vector, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an array of positive integers nums and a positive integer k . You are also given a 2D array queries , where queries[i] = [index i , value i , start i , x i ] . 
 
 You are allowed to perform an operation once on nums , where you can remove any suffix from nums such that nums remains non-empty . 
 
 The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k . 
 
 For each query in queries you need to determine the x-value of nums for x i after performing the following actions: 

 Update nums[index i ] to value i . Only this step persists for the rest of the queries. 
 
 Remove the prefix nums[0..(start i - 1)] (where nums[0..(-1)] will be used to represent the empty prefix). 

 Return an array result of size queries.length where result[i] is the answer for the i th query. 
 
 A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it. 
 
 A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array. 
 
 Note that the prefix and suffix to be chosen for the operation can be empty . 
 
 Note that x-value has a different definition in this version. 

 Example 1: 

 Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]] 
 
 Output: [2,2,2] 
 
 Explanation: 

 For query 0, nums becomes [1, 2, 2, 4, 5] , and the empty prefix must be removed. The possible operations are:

 Remove the suffix [2, 4, 5] . nums becomes [1, 2] . 
 
 Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3. 

 For query 1, nums becomes [1, 2, 2, 3, 5] , and the prefix [1, 2, 2] must be removed. The possible operations are:

 Remove the empty suffix. nums becomes [3, 5] . 
 
 Remove the suffix [5] . nums becomes [3] . 

 For query 2, nums becomes [1, 2, 2, 3, 5] , and the empty prefix must be removed. The possible operations are:

 Remove the suffix [2, 2, 3, 5] . nums becomes [1] . 
 
 Remove the suffix [3, 5] . nums becomes [1, 2, 2] . 

 Example 2: 

 Input: nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]] 
 
 Output: [1,0] 
 
 Explanation: 

 For query 0, nums becomes [2, 2, 4, 8, 16, 32] . The only possible operation is:

 Remove the suffix [2, 4, 8, 16, 32] . 

 For query 1, nums becomes [2, 2, 4, 8, 16, 32] . There is no possible way to perform the operation. 

 Example 3: 

 Input: nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]] 
 
 Output: [5] 

 Constraints: 

 1 <= nums[i] <= 10 9 
 
 1 <= nums.length <= 10 5 
 
 1 <= k <= 5 
 
 1 <= queries.length <= 2 * 10 4 
 
 queries[i] == [index i , value i , start i , x i ] 
 
 0 <= index i <= nums.length - 1 
 
 1 <= value i <= 10 9 
 
 0 <= start i <= nums.length - 1 
 
 0 <= x i <= k - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {struct Node{int prod;array<int,5> cnt;Node(){prod=1;cnt.fill(0);}};int K;Node merge(Node a,Node b){Node c;c.prod=a.prod*b.prod%K;c.cnt=a.cnt;for(int i=0;i<K;i++)c.cnt[a.prod*i%K]+=b.cnt[i];return c;}public:vector<int> resultArray(vector<int>& nums,int k,vector<vector<int>>& queries){K=k;int n=nums.size(),B=1;while(B<n)B*=2;vector<Node>tr(2*B);auto leaf=[&](int v){Node a;a.prod=v%K;a.cnt[a.prod]=1;return a;};for(int i=0;i<n;i++)tr[B+i]=leaf(nums[i]);for(int i=B-1;i;i--)tr[i]=merge(tr[i*2],tr[i*2+1]);vector<int>ans;for(auto&q:queries){int p=B+q[0];tr[p]=leaf(q[1]);for(p/=2;p;p/=2)tr[p]=merge(tr[p*2],tr[p*2+1]);int l=B+q[2],r=B+n;Node left,right;while(l<r){if(l&1)left=merge(left,tr[l++]);if(r&1)right=merge(tr[--r],right);l/=2;r/=2;}ans.push_back(merge(left,right).cnt[q[3]]);}return ans;} };
```


## 3526. Range XOR Queries with Subarray Reversals

**Problem:** https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Bit Manipulation, Tree, Binary Search Tree, Binary Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Binary tree, Tree adjacency list, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of length n and a 2D integer array queries of length q , where each query is one of the following three types: 

 Update : queries[i] = [1, index, value] 
 Set nums[index] = value . 

 Range XOR Query : queries[i] = [2, left, right] 
 Compute the bitwise XOR of all elements in the subarray nums[left...right] , and record this result. 

 Reverse Subarray : queries[i] = [3, left, right] 
 Reverse the subarray nums[left...right] in place. 

 Return an array of the results of all range XOR queries in the order they were encountered. 

 Example 1: 

 Input: nums = [1,2,3,4,5], queries = [[2,1,3],[1,2,10],[3,0,4],[2,0,4]] 
 
 Output: [5,8] 
 
 Explanation: 

 Query 1 : [2, 1, 3] – Compute XOR of subarray [2, 3, 4] resulting in 5. 

 Query 2: [1, 2, 10] – Update nums[2] to 10, updating the array to [1, 2, 10, 4, 5] . 

 Query 3: [3, 0, 4] – Reverse the entire array to get [5, 4, 10, 2, 1] . 

 Query 4: [2, 0, 4] – Compute XOR of subarray [5, 4, 10, 2, 1] resulting in 8. 

 Example 2: 

 Input: nums = [7,8,9], queries = [[1,0,3],[2,0,2],[3,1,2]] 
 
 Output: [2] 
 
 Explanation: 

 Query 1: [1, 0, 3] – Update nums[0] to 3, updating the array to [3, 8, 9] . 

 Query 2: [2, 0, 2] – Compute XOR of subarray [3, 8, 9] resulting in 2. 

 Query 3: [3, 1, 2] – Reverse the subarray [8, 9] to get [9, 8] . 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 0 <= nums[i] <= 10 9 
 
 1 <= queries.length <= 10 5 
 
 queries[i].length == 3​ 
 
 queries[i][0] ∈ {1, 2, 3}​ 
 
 If queries[i][0] == 1 : ​ 

 0 <= index < nums.length​ 
 
 0 <= value <= 10 9 

 If queries[i][0] == 2 or queries[i][0] == 3 : ​ 

 0 <= left <= right < nums.length​

### C++ solution

**Source:** accepted_cpp_submission

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


## 3569. Maximize Count of Distinct Primes After Split

**Problem:** https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, Math, Segment Tree, Number Theory, Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Ordered set, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums having length n and a 2D integer array queries where queries[i] = [idx, val] . 
 
 For each query: 

 Update nums[idx] = val . 
 
 Choose an integer k with 1 <= k < n to split the array into the non-empty prefix nums[0..k-1] and suffix nums[k..n-1] such that the sum of the counts of distinct prime values in each part is maximum . 

 Note: The changes made to the array in one query persist into the next query. 
 
 Return an array containing the result for each query, in the order they are given. 

 Example 1: 

 Input: nums = [2,1,3,1,2], queries = [[1,2],[3,3]] 
 
 Output: [3,4] 
 
 Explanation: 

 Initially nums = [2, 1, 3, 1, 2] . 
 
 After 1 st query, nums = [2, 2, 3, 1, 2] . Split nums into [2] and [2, 3, 1, 2] . [2] consists of 1 distinct prime and [2, 3, 1, 2] consists of 2 distinct primes. Hence, the answer for this query is 1 + 2 = 3 . 
 
 After 2 nd query, nums = [2, 2, 3, 3, 2] . Split nums into [2, 2, 3] and [3, 2] with an answer of 2 + 2 = 4 . 
 
 The output is [3, 4] . 

 Example 2: 

 Input: nums = [2,1,4], queries = [[0,1]] 
 
 Output: [0] 
 
 Explanation: 

 Initially nums = [2, 1, 4] . 
 
 After 1 st query, nums = [1, 1, 4] . There are no prime numbers in nums , hence the answer for this query is 0. 
 
 The output is [0] . 

 Constraints: 

 2 <= n == nums.length <= 5 * 10 4 
 
 1 <= queries.length <= 5 * 10 4 
 
 1 <= nums[i] <= 10 5 
 
 0 <= queries[i][0] < nums.length 
 
 1 <= queries[i][1] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp

class Solution {
    static const int MAXV = 100000;

    struct SegTree {
        int n;
        vector<int> mx, lazy;

        SegTree(const vector<int>& a)
            : n((int)a.size()),
              mx(4 * n + 4, 0),
              lazy(4 * n + 4, 0) {
            if (n) build(1, 0, n - 1, a);
        }

        void build(int p, int l, int r,
                   const vector<int>& a) {
            if (l == r) {
                mx[p] = a[l];
                return;
            }

            int m = (l + r) / 2;
            build(p * 2, l, m, a);
            build(p * 2 + 1, m + 1, r, a);

            mx[p] = max(mx[p * 2], mx[p * 2 + 1]);
        }

        void update(int p, int l, int r,
                    int ql, int qr, int v) {
            if (ql <= l && r <= qr) {
                mx[p] += v;
                lazy[p] += v;
                return;
            }

            int m = (l + r) / 2;

            if (ql <= m)
                update(p * 2, l, m, ql, qr, v);

            if (qr > m)
                update(p * 2 + 1, m + 1, r,
                       ql, qr, v);

            mx[p] = lazy[p] +
                    max(mx[p * 2], mx[p * 2 + 1]);
        }

        void add(int l, int r, int v) {
            if (n && l < r)
                update(1, 0, n - 1, l, r - 1, v);
        }

        int maximum() const {
            return n ? mx[1] : 0;
        }
    };

public:
    vector<int> maximumCount(
        vector<int>& nums,
        vector<vector<int>>& queries) {

        int n = nums.size();

        vector<char> prime(MAXV + 1, true);
        prime[0] = prime[1] = false;

        for (int i = 2; i * i <= MAXV; ++i) {
            if (!prime[i]) continue;

            for (int j = i * i; j <= MAXV; j += i)
                prime[j] = false;
        }

        vector<set<int>> positions(MAXV + 1);

        for (int i = 0; i < n; ++i) {
            if (prime[nums[i]])
                positions[nums[i]].insert(i);
        }

        int distinct = 0;
        vector<int> diff(n + 1, 0);

        for (int p = 2; p <= MAXV; ++p) {
            const set<int>& s = positions[p];

            if (s.empty()) continue;

            ++distinct;

            if (s.size() >= 2) {
                int l = *s.begin();
                int r = *s.rbegin();

                ++diff[l];
                --diff[r];
            }
        }

        vector<int> cover(max(0, n - 1), 0);

        int running = 0;

        for (int i = 0; i < n - 1; ++i) {
            running += diff[i];
            cover[i] = running;
        }

        // Direct updates for workloads where
        // scanning is cheaper than tree overhead.
        bool small =
            1LL * n * queries.size() <= 30000000LL;

        SegTree seg(small ? vector<int>() : cover);

        auto addRange = [&](int l, int r, int delta) {
            if (l >= r) return;

            if (small) {
                for (int i = l; i < r; ++i)
                    cover[i] += delta;
            } else {
                seg.add(l, r, delta);
            }
        };

        vector<int> answer;
        answer.reserve(queries.size());

        for (const auto& q : queries) {
            int idx = q[0];
            int val = q[1];
            int old = nums[idx];

            if (old != val) {

                if (prime[old]) {
                    set<int>& s = positions[old];

                    int oldL = *s.begin();
                    int oldR = *s.rbegin();

                    s.erase(idx);

                    if (s.empty()) {
                        --distinct;
                        addRange(oldL, oldR, -1);
                    } else {
                        int newL = *s.begin();
                        int newR = *s.rbegin();

                        addRange(oldL, newL, -1);
                        addRange(newR, oldR, -1);
                    }
                }

                if (prime[val]) {
                    set<int>& s = positions[val];

                    if (s.empty()) {
                        ++distinct;
                        s.insert(idx);
                    } else {
                        int oldL = *s.begin();
                        int oldR = *s.rbegin();

                        s.insert(idx);

                        int newL = *s.begin();
                        int newR = *s.rbegin();

                        addRange(newL, oldL, 1);
                        addRange(oldR, newR, 1);
                    }
                }

                nums[idx] = val;
            }

            int best = 0;

            if (small) {
                for (int x : cover)
                    best = max(best, x);
            } else {
                best = seg.maximum();
            }

            answer.push_back(distinct + best);
        }

        return answer;
    }
};
```


## 3597. Partition String 

**Problem:** https://leetcode.com/problems/partition-string/

**Difficulty:** Medium | **Premium:** No

**Tags:** Hash Table, String, Trie, Simulation

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, String Algorithms, Simulation / Implementation

**Data structures (inferred):** Hash map / hash set, Hash set, Ordered set, String, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given a string s , partition it into unique segments according to the following procedure: 

 Start building a segment beginning at index 0. 
 
 Continue extending the current segment character by character until the current segment has not been seen before. 
 
 Once the segment is unique, add it to your list of segments, mark it as seen, and begin a new segment from the next index. 
 
 Repeat until you reach the end of s . 

 Return an array of strings segments , where segments[i] is the i th segment created. 

 Example 1: 

 Input: s = "abbccccd" 
 
 Output: ["a","b","bc","c","cc","d"] 
 
 Explanation: 

 Index 
 Segment After Adding 
 Seen Segments 
 Current Segment Seen Before? 
 New Segment 
 Updated Seen Segments 

 0 
 "a" 
 [] 
 No 
 "" 
 ["a"] 

 1 
 "b" 
 ["a"] 
 No 
 "" 
 ["a", "b"] 

 2 
 "b" 
 ["a", "b"] 
 Yes 
 "b" 
 ["a", "b"] 

 3 
 "bc" 
 ["a", "b"] 
 No 
 "" 
 ["a", "b", "bc"] 

 4 
 "c" 
 ["a", "b", "bc"] 
 No 
 "" 
 ["a", "b", "bc", "c"] 

 5 
 "c" 
 ["a", "b", "bc", "c"] 
 Yes 
 "c" 
 ["a", "b", "bc", "c"] 

 6 
 "cc" 
 ["a", "b", "bc", "c"] 
 No 
 "" 
 ["a", "b", "bc", "c", "cc"] 

 7 
 "d" 
 ["a", "b", "bc", "c", "cc"] 
 No 
 "" 
 ["a", "b", "bc", "c", "cc", "d"] 

 Hence, the final output is ["a", "b", "bc", "c", "cc", "d"] . 

 Example 2: 

 Input: s = "aaaa" 
 
 Output: ["a","aa"] 
 
 Explanation: 

 Index 
 Segment After Adding 
 Seen Segments 
 Current Segment Seen Before? 
 New Segment 
 Updated Seen Segments 

 0 
 "a" 
 [] 
 No 
 "" 
 ["a"] 

 1 
 "a" 
 ["a"] 
 Yes 
 "a" 
 ["a"] 

 2 
 "aa" 
 ["a"] 
 No 
 "" 
 ["a", "aa"] 

 3 
 "a" 
 ["a", "aa"] 
 Yes 
 "a" 
 ["a", "aa"] 

 Hence, the final output is ["a", "aa"] . 

 Constraints: 

 1 <= s.length <= 10 5 
 
 s contains only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {public:
 vector<string> partitionString(string s){
  unordered_set<string> seen;vector<string> ans;string cur;
  for(char c:s){cur+=c;if(!seen.count(cur)){seen.insert(cur);ans.push_back(cur);cur.clear();}}
  return ans;
 }
};
```


## 3624. Number of Integers With Popcount-Depth Equal to K II

**Problem:** https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Divide and Conquer, Binary Indexed Tree, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . 
 
 For any positive integer x , define the following sequence: 

 p 0 = x 
 
 p i+1 = popcount(p i ) for all i >= 0 , where popcount(y) is the number of set bits (1's) in the binary representation of y . 

 This sequence will eventually reach the value 1. 
 
 The popcount-depth of x is defined as the smallest integer d >= 0 such that p d = 1 . 
 
 For example, if x = 7 (binary representation "111" ). Then, the sequence is: 7 → 3 → 2 → 1 , so the popcount-depth of 7 is 3. 
 
 You are also given a 2D integer array queries , where each queries[i] is either: 

 [1, l, r, k] - Determine the number of indices j such that l <= j <= r and the popcount-depth of nums[j] is equal to k . 
 
 [2, idx, val] - Update nums[idx] to val . 

 Return an integer array answer , where answer[i] is the number of indices for the i th query of type [1, l, r, k] . 

 Example 1: 

 Input: nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]] 
 
 Output: [2,1] 
 
 Explanation: 

 i 
 queries[i] 
 nums 
 binary( nums ) 
 popcount- 
 depth 
 [l, r] 
 k 
 Valid 
 nums[j] 
 updated 
 nums 
 Answer 

 0 
 [1,0,1,1] 
 [2,4] 
 [10, 100] 
 [1, 1] 
 [0, 1] 
 1 
 [0, 1] 
 — 
 2 

 1 
 [2,1,1] 
 [2,4] 
 [10, 100] 
 [1, 1] 
 — 
 — 
 — 
 [2,1] 
 — 

 2 
 [1,0,1,0] 
 [2,1] 
 [10, 1] 
 [1, 0] 
 [0, 1] 
 0 
 [1] 
 — 
 1 

 Thus, the final answer is [2, 1] . 

 Example 2: 

 Input: nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]] 
 
 Output: [3,1,0] 
 
 Explanation: 

 i 
 queries[i] 
 nums 
 binary( nums ) 
 popcount- 
 depth 
 [l, r] 
 k 
 Valid 
 nums[j] 
 updated 
 nums 
 Answer 

 0 
 [1,0,2,2] 
 [3, 5, 6] 
 [11, 101, 110] 
 [2, 2, 2] 
 [0, 2] 
 2 
 [0, 1, 2] 
 — 
 3 

 1 
 [2,1,4] 
 [3, 5, 6] 
 [11, 101, 110] 
 [2, 2, 2] 
 — 
 — 
 — 
 [3, 4, 6] 
 — 

 2 
 [1,1,2,1] 
 [3, 4, 6] 
 [11, 100, 110] 
 [2, 1, 2] 
 [1, 2] 
 1 
 [1] 
 — 
 1 

 3 
 [1,0,1,0] 
 [3, 4, 6] 
 [11, 100, 110] 
 [2, 1, 2] 
 [0, 1] 
 0 
 [] 
 — 
 0 

 Thus, the final answer is [3, 1, 0] . 

 Example 3: 

 Input: nums = [1,2], queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]] 
 
 Output: [1,0,1] 
 
 Explanation: 

 i 
 queries[i] 
 nums 
 binary( nums ) 
 popcount- 
 depth 
 [l, r] 
 k 
 Valid 
 nums[j] 
 updated 
 nums 
 Answer 

 0 
 [1,0,1,1] 
 [1, 2] 
 [1, 10] 
 [0, 1] 
 [0, 1] 
 1 
 [1] 
 — 
 1 

 1 
 [2,0,3] 
 [1, 2] 
 [1, 10] 
 [0, 1] 
 — 
 — 
 — 
 [3, 2] 

 2 
 [1,0,0,1] 
 [3, 2] 
 [11, 10] 
 [2, 1] 
 [0, 0] 
 1 
 [] 
 — 
 0 

 3 
 [1,0,0,2] 
 [3, 2] 
 [11, 10] 
 [2, 1] 
 [0, 0] 
 2 
 [0] 
 — 
 1 

 Thus, the final answer is [1, 0, 1] . 

 Constraints: 

 1 <= n == nums.length <= 10 5 
 
 1 <= nums[i] <= 10 15 
 
 1 <= queries.length <= 10 5 
 
 queries[i].length == 3 or 4 

 queries[i] == [1, l, r, k] or, 
 
 queries[i] == [2, idx, val] 
 
 0 <= l <= r <= n - 1 
 
 0 <= k <= 5 
 
 0 <= idx <= n - 1 
 
 1 <= val <= 10 15

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
 int depth(long long x){if(x==1)return 0;int d=0;while(x!=1){x=__builtin_popcountll(x);++d;}return d;}
public:
 vector<int> popcountDepth(vector<long long>& nums,vector<vector<long long>>& queries){
  int n=nums.size();vector<vector<int>>bit(7,vector<int>(n+1));auto upd=[&](int d,int i,int v){for(++i;i<=n;i+=i&-i)bit[d][i]+=v;};
  auto pref=[&](int d,int i){int s=0;for(++i;i>0;i-=i&-i)s+=bit[d][i];return s;};
  for(int i=0;i<n;++i)upd(depth(nums[i]),i,1);vector<int>ans;
  for(auto&q:queries){if(q[0]==1){int l=q[1],r=q[2],k=q[3];ans.push_back(k>=0&&k<7?pref(k,r)-(l?pref(k,l-1):0):0);}
   else{int i=q[1];upd(depth(nums[i]),i,-1);nums[i]=q[2];upd(depth(nums[i]),i,1);}}
  return ans;
 }
};
```


## 3632. Subarrays with XOR at Least K

**Problem:** https://leetcode.com/problems/subarrays-with-xor-at-least-k/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Bit Manipulation, Trie, Prefix Sum

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Prefix Sum / Difference Array, Bit Manipulation, Simulation / Implementation

**Data structures (inferred):** Array / vector, Prefix-sum array, Trie, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

Given an array of positive integers nums of length n and a non‑negative integer k . 
 
 Return the number of contiguous subarrays whose bitwise XOR of all elements is greater than or equal to k . 

 Example 1: 

 Input: nums = [3,1,2,3], k = 2 
 
 Output: 6 
 
 Explanation: 
 
 The valid subarrays with XOR >= 2 are [3] at index 0, [3, 1] at indices 0 - 1, [3, 1, 2, 3] at indices 0 - 3, [1, 2] at indices 1 - 2, [2] at index 2, and [3] at index 3; there are 6 in total. 

 Example 2: 

 Input: nums = [0,0,0], k = 0 
 
 Output: 6 
 
 Explanation: 
 
 Every contiguous subarray yields XOR = 0 , which meets k = 0 . There are 6 such subarrays in total. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 0 <= nums[i] <= 10 9 
 
 0 <= k <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    struct Node {
        int child[2],cnt;
        Node():child{-1,-1},cnt(0) {}
    };
public:
    long long countXorSubarrays(vector<int>& nums,int k) {
        vector<Node> trie(1);
        auto insert=[&](int x) {
            int p=0;++trie[p].cnt;
            for(int b=30;b>=0;--b) {
                int t=(x>>b)&1;
                if(trie[p].child[t]==-1) {
                    trie[p].child[t]=trie.size();trie.emplace_back();
                }
                p=trie[p].child[t];++trie[p].cnt;
            }
        };
        auto lessThan=[&](int x) {
            long long count=0;int p=0;
            for(int b=30;b>=0 && p!=-1;--b) {
                int xb=(x>>b)&1,kb=(k>>b)&1;
                if(kb) {
                    int v=trie[p].child[xb];
                    if(v!=-1) count+=trie[v].cnt;
                    p=trie[p].child[xb^1];
                } else p=trie[p].child[xb];
            }
            return count;
        };
        insert(0);
        long long below=0;int pref=0;
        for(int x:nums) {
            pref^=x;
            below+=lessThan(pref);
            insert(pref);
        }
        long long n=nums.size();
        return n*(n+1)/2-below;
    }
};
```


## 3671. Sum of Beautiful Subsequences

**Problem:** https://leetcode.com/problems/sum-of-beautiful-subsequences/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Math, Binary Indexed Tree, Number Theory

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of length n . 
 
 For every positive integer g , we define the beauty of g as the product of g and the number of strictly increasing subsequences of nums whose greatest common divisor (GCD) is exactly g . 
 
 Return the sum of beauty values for all positive integers g . 
 
 Since the answer could be very large, return it modulo 10 9 + 7 . 

 Example 1: 

 Input: nums = [1,2,3] 
 
 Output: 10 
 
 Explanation: 
 
 All strictly increasing subsequences and their GCDs are: 

 Subsequence 
 GCD 

 [1] 
 1 

 [2] 
 2 

 [3] 
 3 

 [1,2] 
 1 

 [1,3] 
 1 

 [2,3] 
 1 

 [1,2,3] 
 1 

 Calculating beauty for each GCD: 

 GCD 
 Count of subsequences 
 Beauty (GCD × Count) 

 1 
 5 
 1 × 5 = 5 

 2 
 1 
 2 × 1 = 2 

 3 
 1 
 3 × 1 = 3 

 Total beauty is 5 + 2 + 3 = 10 . 

 Example 2: 

 Input: nums = [4,6] 
 
 Output: 12 
 
 Explanation: 
 
 All strictly increasing subsequences and their GCDs are: 

 Subsequence 
 GCD 

 [4] 
 4 

 [6] 
 6 

 [4,6] 
 2 

 Calculating beauty for each GCD: 

 GCD 
 Count of subsequences 
 Beauty (GCD × Count) 

 2 
 1 
 2 × 1 = 2 

 4 
 1 
 4 × 1 = 4 

 6 
 1 
 6 × 1 = 6 

 Total beauty is 2 + 4 + 6 = 12 . 

 Constraints: 

 1 <= n == nums.length <= 10 4 
 
 1 <= nums[i] <= 7 * 10 4

### C++ solution

**Source:** accepted_cpp_submission

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


## 3691. Maximum Total Subarray Value II

**Problem:** https://leetcode.com/problems/maximum-total-subarray-value-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Greedy, Segment Tree, Heap (Priority Queue)

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Greedy / Intervals, Heap / Priority Queue, Simulation / Implementation

**Data structures (inferred):** Array / vector, Priority queue, Priority queue / heap, Queue, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of length n and an integer k . 
 
 You must select exactly k distinct subarrays nums[l..r] of nums . Subarrays may overlap, but the exact same subarray (same l and r ) cannot be chosen more than once. 
 
 The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]) . 
 
 The total value is the sum of the values of all chosen subarrays. 
 
 Return the maximum possible total value you can achieve. 

 Example 1: 

 Input: nums = [1,3,2], k = 2 
 
 Output: 4 
 
 Explanation: 
 
 One optimal approach is: 

 Choose nums[0..1] = [1, 3] . The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2 . 
 
 Choose nums[0..2] = [1, 3, 2] . The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2 . 

 Adding these gives 2 + 2 = 4 . 

 Example 2: 

 Input: nums = [4,2,5,1], k = 3 
 
 Output: 12 
 
 Explanation: 
 
 One optimal approach is: 

 Choose nums[0..3] = [4, 2, 5, 1] . The maximum is 5 and the minimum is 1, giving a value of 5 - 1 = 4 . 
 
 Choose nums[1..3] = [2, 5, 1] . The maximum is 5 and the minimum is 1, so the value is also 4 . 
 
 Choose nums[2..3] = [5, 1] . The maximum is 5 and the minimum is 1, so the value is again 4 . 

 Adding these gives 4 + 4 + 4 = 12 . 

 Constraints: 

 1 <= n == nums.length <= 5 * 10 ​​​​​​​4 
 
 0 <= nums[i] <= 10 9 
 
 1 <= k <= min(10 5 , n * (n + 1) / 2)

### C++ solution

**Source:** accepted_cpp_submission

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


## 3719. Longest Balanced Subarray I

**Problem:** https://leetcode.com/problems/longest-balanced-subarray-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Divide and Conquer, Segment Tree, Prefix Sum

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Prefix Sum / Difference Array, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Hash set, Ordered set, Prefix-sum array, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . 
 
 A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers. 
 
 Return the length of the longest balanced subarray. 

 Example 1: 

 Input: nums = [2,5,4,3] 
 
 Output: 4 
 
 Explanation: 

 The longest balanced subarray is [2, 5, 4, 3] . 
 
 It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3] . Thus, the answer is 4. 

 Example 2: 

 Input: nums = [3,2,2,5,4] 
 
 Output: 5 
 
 Explanation: 

 The longest balanced subarray is [3, 2, 2, 5, 4] . 
 
 It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5] . Thus, the answer is 5. 

 Example 3: 

 Input: nums = [1,2,3,2] 
 
 Output: 3 
 
 Explanation: 

 The longest balanced subarray is [2, 3, 2] . 
 
 It has 1 distinct even number [2] and 1 distinct odd number [3] . Thus, the answer is 3. 

 Constraints: 

 1 <= nums.length <= 1500 
 
 1 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

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


## 3721. Longest Balanced Subarray II

**Problem:** https://leetcode.com/problems/longest-balanced-subarray-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, Divide and Conquer, Segment Tree, Prefix Sum

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Prefix Sum / Difference Array, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Prefix-sum array, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums . 
 
 A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers. 
 
 Return the length of the longest balanced subarray. 

 Example 1: 

 Input: nums = [2,5,4,3] 
 
 Output: 4 
 
 Explanation: 

 The longest balanced subarray is [2, 5, 4, 3] . 
 
 It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3] . Thus, the answer is 4. 

 Example 2: 

 Input: nums = [3,2,2,5,4] 
 
 Output: 5 
 
 Explanation: 

 The longest balanced subarray is [3, 2, 2, 5, 4] . 
 
 It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5] . Thus, the answer is 5. 

 Example 3: 

 Input: nums = [1,2,3,2] 
 
 Output: 3 
 
 Explanation: 

 The longest balanced subarray is [2, 3, 2] . 
 
 It has 1 distinct even number [2] and 1 distinct odd number [3] . Thus, the answer is 3. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

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


## 3737. Count Subarrays With Majority Element I

**Problem:** https://leetcode.com/problems/count-subarrays-with-majority-element-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Hash Table, Divide and Conquer, Segment Tree, Merge Sort, Counting, Prefix Sum

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Prefix Sum / Difference Array, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Prefix-sum array, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and an integer target . 
 
 Return the number of subarrays of nums in which target is the majority element . 
 
 The majority element of a subarray is the element that appears strictly more than half of the times in that subarray. 

 Example 1: 

 Input: nums = [1,2,2,3], target = 2 
 
 Output: 5 
 
 Explanation: 
 
 Valid subarrays with target = 2 as the majority element: 

 nums[1..1] = [2] 
 
 nums[2..2] = [2] 
 
 nums[1..2] = [2,2] 
 
 nums[0..2] = [1,2,2] 
 
 nums[1..3] = [2,2,3] 

 So there are 5 such subarrays. 

 Example 2: 

 Input: nums = [1,1,1,1], target = 1 
 
 Output: 10 
 
 Explanation: 
 
 ​​​​​​​ All 10 subarrays have 1 as the majority element. 

 Example 3: 

 Input: nums = [1,2,3], target = 4 
 
 Output: 0 
 
 Explanation: 
 
 target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0. 

 Constraints: 

 1 <= nums.length <= 1000 
 
 1 <= nums[i] <= 10 ​​​​​​​9 
 
 1 <= target <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    int countMajoritySubarrays(vector<int>& nums, int target) {
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            int balance = 0;
            for (int j = i; j < (int)nums.size(); ++j) {
                balance += nums[j] == target ? 1 : -1;
                if (balance > 0) ++ans;
            }
        }
        return ans;
    }
};
```


## 3739. Count Subarrays With Majority Element II

**Problem:** https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, Divide and Conquer, Segment Tree, Merge Sort, Prefix Sum

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Prefix Sum / Difference Array, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Prefix-sum array, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and an integer target . 
 
 Return the number of subarrays of nums in which target is the majority element . 
 
 The majority element of a subarray is the element that appears strictly more than half of the times in that subarray. 

 Example 1: 

 Input: nums = [1,2,2,3], target = 2 
 
 Output: 5 
 
 Explanation: 
 
 Valid subarrays with target = 2 as the majority element: 

 nums[1..1] = [2] 
 
 nums[2..2] = [2] 
 
 nums[1..2] = [2,2] 
 
 nums[0..2] = [1,2,2] 
 
 nums[1..3] = [2,2,3] 

 So there are 5 such subarrays. 

 Example 2: 

 Input: nums = [1,1,1,1], target = 1 
 
 Output: 10 
 
 Explanation: 
 
 ​​​​​​​ All 10 subarrays have 1 as the majority element. 

 Example 3: 

 Input: nums = [1,2,3], target = 4 
 
 Output: 0 
 
 Explanation: 
 
 target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0. 

 Constraints: 

 1 <= nums.length <= 10 ​​​​​​​5 
 
 1 <= nums[i] <= 10 ​​​​​​​9 
 
 1 <= target <= 10 9

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums,int target) {
        int n=nums.size(),offset=n+2;
        vector<int> bit(2*n+5,0);
        auto add=[&](int x) {
            for(;x<(int)bit.size();x+=x&-x) ++bit[x];
        };
        auto sum=[&](int x) {
            int ans=0;
            for(;x>0;x-=x&-x) ans+=bit[x];
            return ans;
        };
        int pref=0;long long answer=0;
        add(offset);
        for(int x:nums) {
            pref+=(x==target?1:-1);
            answer+=sum(pref+offset-1);
            add(pref+offset);
        }
        return answer;
    }
};
```


## 3758. Convert Number Words to Digits

**Problem:** https://leetcode.com/problems/convert-number-words-to-digits/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** String, Trie

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms

**Data structures (inferred):** String, Trie

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string s consisting of lowercase English letters. s may contain valid concatenated English words representing the digits 0 to 9, without spaces. 
 
 Your task is to extract each valid number word in order and convert it to its corresponding digit, producing a string of digits. 
 
 Parse s from left to right. At each position: 

 If a valid number word starts at the current position, append its corresponding digit to the result and advance by the length of that word. 
 
 Otherwise, skip exactly one character and continue parsing. 

 Return the resulting digit string. If no number words are found, return an empty string. 

 Example 1: 

 Input: s = "onefourthree" 
 
 Output: "143" 
 
 Explanation: 

 Parsing from left to right, extract the valid number words "one", "four", "three". 
 
 These map to digits 1, 4, 3. Thus, the final result is "143" . 

 Example 2: 

 Input: s = "ninexsix" 
 
 Output: "96" 
 
 Explanation: 

 The substring "nine" is a valid number word and maps to 9. 
 
 The character "x" does not match any valid number word prefix and is skipped. 
 
 Then, the substring "six" is a valid number word and maps to 6, so the final result is "96" . 

 Example 3: 

 Input: s = "zeero" 
 
 Output: "" 
 
 Explanation: 

 No substring forms a valid number word during left-to-right parsing. 
 
 All characters are skipped and incomplete fragments are ignored, so the result is an empty string. 

 Example 4: 

 Input: s = "tw" 
 
 Output: "" 
 
 Explanation: 

 No substring forms a valid number word during left-to-right parsing. 
 
 All characters are skipped and incomplete fragments are ignored, so the result is an empty string. 

 Constraints: 

 1 <= s.length <= 10 5 
 
 s contains only lowercase English letters.

### C++ solution

**Source:** accepted_cpp_submission

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


## 3777. Minimum Deletions to Make Alternating Substring

**Problem:** https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

**Difficulty:** Hard | **Premium:** No

**Tags:** String, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, String Algorithms

**Data structures (inferred):** Segment tree, String, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given a string s of length n consisting only of the characters 'A' and 'B' . 
 
 You are also given a 2D integer array queries of length q , where each queries[i] is one of the following: 

 [1, j] : Flip the character at index j of s i.e. 'A' changes to 'B' (and vice versa). This operation mutates s and affects subsequent queries. 
 
 [2, l, r] : Compute the minimum number of character deletions required to make the substring s[l..r] alternating . This operation does not modify s ; the length of s remains n . 

 A substring is alternating if no two adjacent characters are equal . A substring of length 1 is always alternating. 
 
 Return an integer array answer , where answer[i] is the result of the i th query of type [2, l, r] . 

 Example 1: 

 Input: s = "ABA", queries = [[2,1,2],[1,1],[2,0,2]] 
 
 Output: [0,2] 
 
 Explanation: 

 i 
 queries[i] 
 j 
 l 
 r 
 s before query 
 s[l..r] 
 Result 
 Answer 

 0 
 [2, 1, 2] 
 - 
 1 
 2 
 "ABA" 
 "BA" 
 Already alternating 
 0 

 1 
 [1, 1] 
 1 
 - 
 - 
 "ABA" 
 - 
 Flip s[1] from 'B' to 'A' 
 - 

 2 
 [2, 0, 2] 
 - 
 0 
 2 
 "AAA" 
 "AAA" 
 Delete any two 'A' s to get "A" 
 2 

 Thus, the answer is [0, 2] . 

 Example 2: 

 Input: s = "ABB", queries = [[2,0,2],[1,2],[2,0,2]] 
 
 Output: [1,0] 
 
 Explanation: 

 i 
 queries[i] 
 j 
 l 
 r 
 s before query 
 s[l..r] 
 Result 
 Answer 

 0 
 [2, 0, 2] 
 - 
 0 
 2 
 "ABB" 
 "ABB" 
 Delete one 'B' to get "AB" 
 1 

 1 
 [1, 2] 
 2 
 - 
 - 
 "ABB" 
 - 
 Flip s[2] from 'B' to 'A' 
 - 

 2 
 [2, 0, 2] 
 - 
 0 
 2 
 "ABA" 
 "ABA" 
 Already alternating 
 0 

 Thus, the answer is [1, 0] . 

 Example 3: 

 Input: s = "BABA", queries = [[2,0,3],[1,1],[2,1,3]] 
 
 Output: [0,1] 
 
 Explanation: 

 i 
 queries[i] 
 j 
 l 
 r 
 s before query 
 s[l..r] 
 Result 
 Answer 

 0 
 [2, 0, 3] 
 - 
 0 
 3 
 "BABA" 
 "BABA" 
 Already alternating 
 0 

 1 
 [1, 1] 
 1 
 - 
 - 
 "BABA" 
 - 
 Flip s[1] from 'A' to 'B' 
 - 

 2 
 [2, 1, 3] 
 - 
 1 
 3 
 "BBBA" 
 "BBA" 
 Delete one 'B' to get "BA" 
 1 

 Thus, the answer is [0, 1] . 

 Constraints: 

 1 <= n == s.length <= 10 5 
 
 s[i] is either 'A' or 'B' . 
 
 1 <= q == queries.length <= 10 5 
 
 queries[i].length == 2 or 3 

 queries[i] == [1, j] or, 
 
 queries[i] == [2, l, r] 
 
 0 <= j <= n - 1 
 
 0 <= l <= r <= n - 1

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    struct BIT {
        vector<int> bit;
        BIT(int n) : bit(n + 1, 0) {}
        void add(int x, int d) {
            for (++x; x < (int)bit.size(); x += x & -x) bit[x] += d;
        }
        int pref(int x) {
            int z = 0;
            for (++x; x > 0; x -= x & -x) z += bit[x];
            return z;
        }
    };
public:
    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
        int n = s.size();
        BIT bit(n);
        for (int i = 1; i < n; ++i) if (s[i] == s[i - 1]) bit.add(i, 1);
        vector<int> ans;
        for (auto &q : queries) {
            if (q[0] == 2) {
                ans.push_back(bit.pref(q[2]) - bit.pref(q[1]));
            } else {
                int j = q[1];
                for (int i = max(1, j); i <= min(n - 1, j + 1); ++i)
                    if (s[i] == s[i - 1]) bit.add(i, -1);
                s[j] = (s[j] == 'A') ? 'B' : 'A';
                for (int i = max(1, j); i <= min(n - 1, j + 1); ++i)
                    if (s[i] == s[i - 1]) bit.add(i, 1);
            }
        }
        return ans;
    }
};
```


## 3901. Good Subsequence Queries

**Problem:** https://leetcode.com/problems/good-subsequence-queries/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Math, Segment Tree, Number Theory

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Math / Number Theory, Simulation / Implementation

**Data structures (inferred):** Array / vector, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of length n and an integer p . 
 
 A non-empty subsequence of nums is called good if: 

 Its length is strictly less than n . 
 
 The greatest common divisor (GCD) of its elements is exactly p . 

 You are also given a 2D integer array queries of length q , where each queries[i] = [ind i , val i ] indicates that you should update nums[ind i ] to val i . 
 
 After each query, determine whether there exists any good subsequence in the current array. 
 
 Return the number of queries for which a good subsequence exists. 
The term gcd(a, b) denotes the greatest common divisor of a and b .

 Example 1: 

 Input: nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]] 
 
 Output: 1 
 
 Explanation: 

 i 
 [ind i , val i ] 
 Operation 
 Updated nums 
 Any good Subsequence 

 0 
 [0, 3] 
 Update nums[0] to 3 
 [3, 8, 12, 16] 
 No, as no subsequence has GCD exactly p = 2 

 1 
 [2, 6] 
 Update nums[2] to 6 
 [3, 8, 6, 16] 
 Yes, subsequence [8, 6] has GCD exactly p = 2 

 Thus, the answer is 1. 

 Example 2: 

 Input: nums = [4,5,7,8], p = 3, queries = [[0,6],[1,9],[2,3]] 
 
 Output: 2 
 
 Explanation: 

 i 
 [ind i , val i ] 
 Operation 
 Updated nums 
 Any good Subsequence 

 0 
 [0, 6] 
 Update nums[0] to 6 
 [6, 5, 7, 8] 
 No, as no subsequence has GCD exactly p = 3 

 1 
 [1, 9] 
 Update nums[1] to 9 
 [6, 9, 7, 8] 
 Yes, subsequence [6, 9] has GCD exactly p = 3 

 2 
 [2, 3] 
 Update nums[2] to 3 
 [6, 9, 3, 8] 
 Yes, subsequence [6, 9, 3] has GCD exactly p = 3 

 Thus, the answer is 2. 

 Example 3: 

 Input: nums = [5,7,9], p = 2, queries = [[1,4],[2,8]] 
 
 Output: 0 
 
 Explanation: 

 i 
 [ind i , val i ] 
 Operation 
 Updated nums 
 Any good Subsequence 

 0 
 [1, 4] 
 Update nums[1] to 4 
 [5, 4, 9] 
 No, as no subsequence has GCD exactly p = 2 

 1 
 [2, 8] 
 Update nums[2] to 8 
 [5, 4, 8] 
 No, as no subsequence has GCD exactly p = 2 

 Thus, the answer is 0. 

 Constraints: 

 2 <= n == nums.length <= 5 * 10 4 
 
 1 <= nums[i] <= 5 * 10 4 
 
 1 <= queries.length <= 5 * 10 4 
 
 queries[i] = [ind i , val i ] 
 
 1 <= val i , p <= 5 * 10 4 
 
 0 <= ind i <= n - 1

### C++ solution

**Source:** accepted_cpp_submission

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


## 3930. Power Update After K-th Largest Insertion II

**Problem:** https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

**Difficulty:** Hard | **Premium:** Yes

**Tags:** Array, Hash Table, Math, Segment Tree, Sorting

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Hashing / Frequency Counting, Math / Number Theory, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Segment tree, Sorted array, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and an integer p . 
 
 You are also given a 2D integer array queries , where each queries[i] = [val i , k i ] . 
 
 For each query: 

 Insert val i into nums . 
 
 Let x be the k i th largest element in the current nums . 
 
 Update p to p x % (10 9 + 7) . 

 Return an array ans where the ans[i] represents the value of p after processing the i th query. 

 Example 1: 

 Input: nums = [2], p = 4, queries = [[3,1],[1,2]] 
 
 Output: [64,4096] 
 
 Explanation: 

 i 
 val i 
 Current 
 nums 
 k i 
 k i th 
 largest 
 p 
 New p = p k % (10 9 + 7) 

 0 
 3 
 [2, 3] 
 1 
 3 
 4 
 4 3 % (10 9 + 7) = 64 

 1 
 1 
 [2, 3, 1] 
 2 
 2 
 64 
 64 2 % (10 9 + 7) = 4096 

 Thus, ans = [64, 4096] . 

 Example 2: 

 Input: nums = [7,5], p = 6, queries = [[4,3],[7,2]] 
 
 Output: [1296,220296870] 
 
 Explanation: 

 i 
 val i 
 Current​​​​​​​ 
 nums 
 k i 
 k i th 
 largest 
 p 
 New p = p k % (10 9 + 7) 

 0 
 4 
 [7, 5, 4] 
 3 
 4 
 6 
 6 4 % (10 9 + 7) = 1296 

 1 
 7 
 [7, 5, 4, 7] 
 2 
 7 
 1296 
 1296 7 % (10 9 + 7) = 220296870 

 Thus, ans = [1296, 220296870] 

 Constraints: 

 1 <= nums.length <= 2 * 10 4 
 
 1 <= nums[i] <= 10 9 
 
 ​​​​​​​1 <= p <= 10 9 
 
 1 <= queries.length <= 2 * 10 4 
 
 ​​​​​​​ 1 <= val i <= 10 9 
 
 1 <= k i <= n + i + 1 ​​​​​​​

### C++ solution

**Source:** accepted_cpp_submission

```cpp
class Solution {
    static const int MOD = 1000000007;
    long long power(long long a, long long b) {
        long long ans = 1;
        while (b) {
            if (b & 1) ans = ans * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return ans;
    }
public:
    vector<int> powerUpdate(vector<int>& nums, int p,
                            vector<vector<int>>& queries) {
        vector<int> vals = nums;
        for (auto& q : queries) vals.push_back(q[0]);
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        int n = vals.size();
        vector<int> bit(n + 1, 0);
        auto add = [&](int x) {
            for (++x; x <= n; x += x & -x) ++bit[x];
        };
        for (int v : nums)
            add(lower_bound(vals.begin(), vals.end(), v) - vals.begin());
        int total = nums.size();
        vector<int> ans;
        for (auto& q : queries) {
            add(lower_bound(vals.begin(), vals.end(), q[0]) - vals.begin());
            ++total;
            int rank = total - q[1] + 1;
            int pos = 0, step = 1;
            while (step <= n) step <<= 1;
            for (step >>= 1; step; step >>= 1) {
                int next = pos + step;
                if (next <= n && bit[next] < rank) {
                    rank -= bit[next];
                    pos = next;
                }
            }
            int x = vals[pos];
            p = (int)power(p, x);
            ans.push_back(p);
        }
        return ans;
    }
};
```


## 3935. Power Update After K-th Largest Insertion I

**Problem:** https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

**Difficulty:** Medium | **Premium:** Yes

**Tags:** Array, Hash Table, Math, Segment Tree, Sorting, Heap (Priority Queue)

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Heap / Priority Queue, Hashing / Frequency Counting, Math / Number Theory, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Hash map / hash set, Priority queue / heap, Segment tree, Sorted array, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and an integer p . 
 
 You are also given a 2D integer array queries , where each queries[i] = [val i , k i ] and the difference between consecutive k i values is always less than 10. 
 
 For each query: 

 Insert val i into nums . 
 
 Let x be the k i th largest element in the current nums . 
 
 Update p to p x % (10 9 + 7) . 

 Return an array ans where the ans[i] represents the value of p after processing the i th query. 

 Example 1: 

 Input: nums = [2], p = 4, queries = [[3,1],[1,2]] 
 
 Output: [64,4096] 
 
 Explanation: 

 i 
 val i 
 Current 
 nums 
 k i 
 k i th 
 largest 
 p 
 New p = p k % (10 9 + 7) 

 0 
 3 
 [2, 3] 
 1 
 3 
 4 
 4 3 % (10 9 + 7) = 64 

 1 
 1 
 [2, 3, 1] 
 2 
 2 
 64 
 64 2 % (10 9 + 7) = 4096 

 Thus, ans = [64, 4096] . 

 Example 2: 

 Input: nums = [7,5], p = 6, queries = [[4,3],[7,2]] 
 
 Output: [1296,220296870] 
 
 Explanation: 

 i 
 val i 
 Current​​​​​​​ 
 nums 
 k i 
 k i th 
 largest 
 p 
 New p = p k % (10 9 + 7) 

 0 
 4 
 [7, 5, 4] 
 3 
 4 
 6 
 6 4 % (10 9 + 7) = 1296 

 1 
 7 
 [7, 5, 4, 7] 
 2 
 7 
 1296 
 1296 7 % (10 9 + 7) = 220296870 

 Thus, ans = [1296, 220296870] 

 Constraints: 

 1 <= nums.length <= 2 × 10 4 
 
 1 <= nums[i] <= 10 6 
 
 ​​​​​​​1 <= p <= 10 6 
 
 1 <= queries.length <= 2 × 10 4 
 
 ​​​​​​​ 1 <= val i <= 10 6 
 
 1 <= k i <= n + i + 1 
 
 |k i - k i - 1 | < 10 for i > 0

### C++ solution

**Source:** accepted_cpp_submission

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


## 3962. Maximum Subarray Sum After at Most K Swaps

**Problem:** https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Hash Table, Greedy, Binary Indexed Tree, Sorting, Heap (Priority Queue), Ordered Set

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Greedy / Intervals, Heap / Priority Queue, Hashing / Frequency Counting, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Hash map / hash set, Priority queue / heap, Sorted array, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and an integer k . 
 
 You are allowed to perform at most k swap operations on the array. 
 
 In one swap operation, you may choose any two indices i and j and swap nums[i] and nums[j] . 
 
 Return an integer denoting the maximum possible subarray sum after performing the swaps. 

 Example 1: 

 Input: nums = [1,-1,0,2], k = 1 
 
 Output: 3 
 
 Explanation: 

 We can swap on indices 1 and 3, resulting in the array [1, 2, 0, -1] . 
 
 The subarray [1, 2] has a sum of 3, which is the maximum possible subarray sum after at most k = 1 ​​​​​​​ swap. 

 Example 2: 

 Input: nums = [4,3,2,4], k = 2 
 
 Output: 13 
 
 Explanation: 
 
 The maximum possible subarray sum after at most k = 2 swaps is the sum of the entire array, which is 13. 

 Example 3: 

 Input: nums = [-1,-2], k = 0 
 
 Output: -1 
 
 Explanation: 

 k = 0 swaps are allowed. 
 
 The possible subarrays are [-1] , [-2] , and [-1, -2] , with sums -1, -2, and -3 respectively. 
 
 Among these sums, the maximum is -1. 

 Constraints: 

 1 <= nums.length <= 1500 
 
 -10 5 <= nums[i] <= 10 5 
 
 0 <= k <= nums.length

### C++ solution

**Source:** accepted_cpp_submission

```cpp

class Solution {
    using ll = long long;

    struct Fenwick {
        int n;
        vector<int> cnt;
        vector<ll> sum;
        const vector<int>& values;

        Fenwick(const vector<int>& v)
            : n((int)v.size()),
              cnt(n + 1, 0),
              sum(n + 1, 0),
              values(v) {}

        void add(int idx, int delta) {
            int val = values[idx - 1];

            for (int i = idx; i <= n; i += i & -i) {
                cnt[i] += delta;
                sum[i] += 1LL * delta * val;
            }
        }

        // Find the 1-based index of the kth smallest value.
        int kth(int k) const {
            int idx = 0;
            int step = 1;

            while ((step << 1) <= n)
                step <<= 1;

            for (; step > 0; step >>= 1) {
                int next = idx + step;

                if (next <= n && cnt[next] < k) {
                    idx = next;
                    k -= cnt[next];
                }
            }

            return idx + 1;
        }

        // Sum of the smallest k elements.
        ll smallestSum(int k) const {
            if (k == 0)
                return 0;

            int idx = 0;
            int step = 1;
            ll result = 0;

            while ((step << 1) <= n)
                step <<= 1;

            for (; step > 0; step >>= 1) {
                int next = idx + step;

                if (next <= n && cnt[next] < k) {
                    idx = next;
                    k -= cnt[next];
                    result += sum[next];
                }
            }

            return result + 1LL * k * values[idx];
        }
    };

public:
    long long maxSum(vector<int>& nums, int k) {
        int n = (int)nums.size();

        vector<int> values = nums;
        sort(values.begin(), values.end());
        values.erase(
            unique(values.begin(), values.end()),
            values.end()
        );

        vector<int> id(n);

        for (int i = 0; i < n; ++i) {
            id[i] = lower_bound(
                values.begin(), values.end(), nums[i]
            ) - values.begin() + 1;
        }

        ll answer = LLONG_MIN;

        for (int left = 0; left < n; ++left) {
            Fenwick inside(values);
            Fenwick outside(values);

            for (int i = 0; i < n; ++i)
                outside.add(id[i], 1);

            ll windowSum = 0;
            ll outsideSum = 0;

            for (int x : nums)
                outsideSum += x;

            int swaps = 0;

            for (int right = left; right < n; ++right) {
                inside.add(id[right], 1);
                outside.add(id[right], -1);

                windowSum += nums[right];
                outsideSum -= nums[right];

                int len = right - left + 1;
                int out = n - len;

                // The optimal number of beneficial swaps
                // changes by at most one when right advances.
                if (swaps < k &&
                    swaps < len &&
                    swaps < out &&
                    inside.kth(swaps + 1) <
                    outside.kth(out - swaps)) {

                    ++swaps;

                } else if (swaps > 0 &&
                           inside.kth(swaps) >=
                           outside.kth(out - swaps + 1)) {

                    --swaps;
                }

                ll removed = inside.smallestSum(swaps);

                ll incoming = outsideSum -
                    outside.smallestSum(out - swaps);

                ll current = windowSum
                           - removed
                           + incoming;

                answer = max(answer, current);
            }
        }

        return answer;
    }
};
```


## 4011. Count Subarrays With Even Odd Ratio I

**Problem:** https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

**Difficulty:** Medium | **Premium:** No

**Tags:** Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Prefix Sum

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Prefix Sum / Difference Array, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Prefix-sum array, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and two integers a and b . 
 
 For a subarray , let: 

 x be the number of even elements. 
 
 y be the number of odd elements. 

 The ratio of even to odd elements in a subarray is defined as x / y , where ratios are compared by their exact rational values. 
 
 A subarray is considered valid if: 

 y > 0 , and 
 
 x / y <= a / b . 

 Return the number of valid subarrays in nums . 

 Example 1: 

 Input: nums = [1,2,1,2], a = 3, b = 2 
 
 Output: 7 
 
 Explanation: 
 
 The following are the valid subarrays: 

 Subarray 
 Values 
 Even Count 
 Odd Count 
 Ratio 

 nums[0..0] 
 [1] 
 0 
 1 
 0 / 1 

 nums[0..1] 
 [1, 2] 
 1 
 1 
 1 / 1 

 nums[0..2] 
 [1, 2, 1] 
 1 
 2 
 1 / 2 

 nums[0..3] 
 [1, 2, 1, 2] 
 2 
 2 
 2 / 2 

 nums[1..2] 
 [2, 1] 
 1 
 1 
 1 / 1 

 nums[2..2] 
 [1] 
 0 
 1 
 0 / 1 

 nums[2..3] 
 [1, 2] 
 1 
 1 
 1 / 1 

 Thus, the number of valid subarrays is 7. 

 Example 2: 

 Input: nums = [2,2,1], a = 2, b = 1 
 
 Output: 3 
 
 Explanation: 
 
 The following are the valid subarrays: 

 Subarray 
 Values 
 Even Count 
 Odd Count 
 Ratio 

 nums[0..2] 
 [2, 2, 1] 
 2 
 1 
 2 / 1 

 nums[1..2] 
 [2, 1] 
 1 
 1 
 1 / 1 

 nums[2..2] 
 [1] 
 0 
 1 
 0 / 1 

 Thus, the number of valid subarrays is 3. 

 Example 3: 

 Input: nums = [2,2,2], a = 1, b = 1 
 
 Output: 0 
 
 Explanation: 
 
 Every subarray contains 0 odd numbers, so no subarray is valid. 

 Constraints: 

 1 <= nums.length <= 1000 
 
 1 <= nums[i] <= 1000 
 
 1 <= a, b <= 1000

### C++ solution

**Source:** accepted_cpp_submission

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


## 4013. Count Subarrays With Even Odd Ratio II

**Problem:** https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Prefix Sum

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Prefix Sum / Difference Array, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Fenwick tree, Prefix-sum array, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums and two integers a and b . 
 
 For a subarray , let: 

 x be the number of even elements. 
 
 y be the number of odd elements. 

 The ratio of even to odd elements in a subarray is defined as x / y , where ratios are compared by their exact rational values. 
 
 A subarray is considered valid if: 

 y > 0 , and 
 
 x / y <= a / b . 

 Return the number of valid subarrays in nums . 

 Example 1: 

 Input: nums = [1,2,1,2], a = 3, b = 2 
 
 Output: 7 
 
 Explanation: 
 
 The following are the valid subarrays: 

 Subarray 
 Values 
 Even Count 
 Odd Count 
 Ratio 

 nums[0..0] 
 [1] 
 0 
 1 
 0 / 1 

 nums[0..1] 
 [1, 2] 
 1 
 1 
 1 / 1 

 nums[0..2] 
 [1, 2, 1] 
 1 
 2 
 1 / 2 

 nums[0..3] 
 [1, 2, 1, 2] 
 2 
 2 
 2 / 2 

 nums[1..2] 
 [2, 1] 
 1 
 1 
 1 / 1 

 nums[2..2] 
 [1] 
 0 
 1 
 0 / 1 

 nums[2..3] 
 [1, 2] 
 1 
 1 
 1 / 1 

 Thus, the number of valid subarrays is 7. 

 Example 2: 

 Input: nums = [2,2,1], a = 2, b = 1 
 
 Output: 3 
 
 Explanation: 
 
 The following are the valid subarrays: 

 Subarray 
 Values 
 Even Count 
 Odd Count 
 Ratio 

 nums[0..2] 
 [2, 2, 1] 
 2 
 1 
 2 / 1 

 nums[1..2] 
 [2, 1] 
 1 
 1 
 1 / 1 

 nums[2..2] 
 [1] 
 0 
 1 
 0 / 1 

 Thus, the number of valid subarrays is 3. 

 Example 3: 

 Input: nums = [2,2,2], a = 1, b = 1 
 
 Output: 0 
 
 Explanation: 
 
 Every subarray contains 0 odd numbers, so no subarray is valid. 

 Constraints: 

 1 <= nums.length <= 10 5 
 
 1 <= nums[i] <= 10 9 
 
 1 <= a, b <= 10 9 ​​​​​​​

### C++ solution

**Source:** accepted_cpp_submission

```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    long long countRatioSubarrays(vector<int>& a,int x,int y){
        int n=a.size();vector<long long>p(n+1);
        for(int i=0;i<n;i++)p[i+1]=p[i]+(a[i]%2?-1LL*x:1LL*y);
        vector<long long>v=p;sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());
        vector<int>bit(n+3);auto upd=[&](int i){for(;i<(int)bit.size();i+=i&-i)bit[i]++;};
        auto qry=[&](int i){int s=0;for(;i;i-=i&-i)s+=bit[i];return s;};
        long long ans=0;
        for(int i=0;i<=n;i++){
            int id=lower_bound(v.begin(),v.end(),p[i])-v.begin()+1;
            ans+=i-qry(id-1);upd(id);
        }
        return ans;
    }
};
```


## 4017. Peaks in Array II

**Problem:** https://leetcode.com/problems/peaks-in-array-ii/

**Difficulty:** Hard | **Premium:** No

**Tags:** Array, Divide and Conquer, Segment Tree

**Primary pattern:** Tree / Trie

**Related patterns:** Tree / Trie, Sorting / Divide and Conquer, Simulation / Implementation

**Data structures (inferred):** Array / vector, Segment tree, Vector

**Pattern recognition:** Hierarchical traversal, ancestor queries, prefix lookup, or range structure.

**Approach verification:** topic-tag heuristic; NOT a verified per-solution explanation

**Time complexity:** Needs manual or AI-assisted code analysis

**Space complexity:** Needs manual or AI-assisted code analysis

### Problem description

You are given an integer array nums of length n and a 2D integer array queries . 
 
 A subarray nums[i..j] is called a peak subarray if: 

 Its length is at least 3. 
 
 There exists an index k such that i < k < j and:

 nums[k] > nums[k - 1] 
 
 nums[k] > nums[k + 1] 

 You have to process queries of two types: 

 [1, l i , r i ] : Calculate the number of peak subarrays fully contained within nums[l i ..r i ] . 
 
 [2, index i , val i ] : Update nums[index i ] to val i . This update applies to all subsequent queries. 

 Return an array answer , where answer[i] is the answer to the i th query of type 1 in the order they appear. 

 Example 1: 

 Input: nums = [1,3,2,4], queries = [[1,0,3],[2,1,1],[1,0,3]] 
 
 Output: [2,0] 
 
 Explanation: ​​​​​​​ 

 Query [1, 0, 3] :

 [1, 3, 2] : choose k = 1 . Then nums[k] = 3 , nums[k - 1] = 1 , and nums[k + 1] = 2 . Since 3 > 1 and 3 > 2 , this is a peak subarray. 
 
 [1, 3, 2, 4] : choose k = 1 . Then nums[k] = 3 , nums[k - 1] = 1 , and nums[k + 1] = 2 . Since 3 > 1 and 3 > 2 , this is a peak subarray. 

 Query [2, 1, 1] : Update nums[1] to 1. The array becomes [1, 1, 2, 4] . 
 
 Query [1, 0, 3] : There are no peak subarrays now. 
 
 Thus, answer = [2, 0] . 

 Example 2: 

 Input: nums = [9,8,9,8], queries = [[1,1,3],[2,2,1],[1,0,2]] 
 
 Output: [1,0] 
 
 Explanation: 

 Query [1, 1, 3] :

 nums[1..3] = [8, 9, 8] : choose k = 2 . Then nums[k] = 9 , nums[k - 1] = 8 , and nums[k + 1] = 8 . Since 9 > 8 and 9 > 8 , this is a peak subarray. 

 Query [2, 2, 1] : Update nums[2] to 1. The array becomes [9, 8, 1, 8] . 
 
 Query [1, 0, 2] : There are no peak subarrays. 
 
 Thus, answer = [1, 0] . 

 Example 3: 

 Input: nums = [3,6,2,7,1], queries = [[1,1,3],[2,3,0],[1,0,4]] 
 
 Output: [0,3] 
 
 Explanation: 

 Query [1, 1, 3] : The only subarray of length at least 3 is [6, 2, 7] . Its only possible peak index is k = 2 , but nums[2] = 2 is less than both nums[1] = 6 and nums[3] = 7 , so it is not a peak subarray. 
 
 Query [2, 3, 0] : Update nums[3] to 0. The array becomes [3, 6, 2, 0, 1] . 
 
 Query [1, 0, 4] :

 [3, 6, 2] : choose k = 1 . Then nums[k] = 6 , nums[k - 1] = 3 , and nums[k + 1] = 2 . Since 6 > 3 and 6 > 2 , this is a peak subarray. 
 
 [3, 6, 2, 0] : choose k = 1 . Then nums[k] = 6 , nums[k - 1] = 3 , and nums[k + 1] = 2 . Since 6 > 3 and 6 > 2 , this is a peak subarray. 
 
 [3, 6, 2, 0, 1] : choose k = 1 . Then nums[k] = 6 , nums[k - 1] = 3 , and nums[k + 1] = 2 . Since 6 > 3 and 6 > 2 , this is a peak subarray. 

 Thus, answer = [0, 3] . 

 Constraints: 

 3 <= n == nums.length <= 10 5 
 
 0 <= nums[i] <= 10 5 
 
 1 <= queries.length <= 10 5 
 
 queries[i] = [1, l i , r i ] or queries[i] = [2, index i , val i ] 
 
 0 <= l i < r i <= n - 1 
 
 0 <= index i <= n - 1 
 
 0 <= val i <= 10 5

### C++ solution

**Source:** accepted_cpp_submission

```cpp

class Solution {
    using ll = long long;

    struct Node {
        int len;
        ll prefix, suffix, noPeak;

        Node(int l = 0, ll p = 0,
             ll s = 0, ll z = 0)
            : len(l), prefix(p), suffix(s), noPeak(z) {}
    };

    vector<Node> tree;
    vector<int> peak;
    int n;

    Node merge(const Node& a, const Node& b) {
        if (a.len == 0) return b;
        if (b.len == 0) return a;

        Node res;
        res.len = a.len + b.len;

        res.prefix = (a.prefix == a.len)
                   ? a.len + b.prefix : a.prefix;

        res.suffix = (b.suffix == b.len)
                   ? b.len + a.suffix : b.suffix;

        res.noPeak = a.noPeak + b.noPeak
                   + a.suffix * b.prefix;

        return res;
    }

    Node leaf(int isPeak) {
        if (isPeak)
            return Node(1, 0, 0, 0);

        return Node(1, 1, 1, 1);
    }

    void build(int node, int l, int r) {
        if (l == r) {
            tree[node] = leaf(peak[l]);
            return;
        }

        int mid = l + (r - l) / 2;

        build(node * 2, l, mid);
        build(node * 2 + 1, mid + 1, r);

        tree[node] = merge(
            tree[node * 2],
            tree[node * 2 + 1]
        );
    }

    void update(int node, int l, int r,
                int index, int value) {
        if (l == r) {
            tree[node] = leaf(value);
            return;
        }

        int mid = l + (r - l) / 2;

        if (index <= mid)
            update(node * 2, l, mid, index, value);
        else
            update(node * 2 + 1, mid + 1, r,
                   index, value);

        tree[node] = merge(
            tree[node * 2],
            tree[node * 2 + 1]
        );
    }

    Node query(int node, int l, int r,
               int ql, int qr) {
        if (qr < l || r < ql)
            return Node();

        if (ql <= l && r <= qr)
            return tree[node];

        int mid = l + (r - l) / 2;

        return merge(
            query(node * 2, l, mid, ql, qr),
            query(node * 2 + 1, mid + 1, r,
                  ql, qr)
        );
    }

public:
    vector<long long> countOfPeaks(
        vector<int>& nums,
        vector<vector<int>>& queries) {

        n = (int)nums.size();

        peak.assign(n, 0);
        tree.resize(4 * n + 5);

        auto isPeak = [&](int i) -> int {
            if (i <= 0 || i >= n - 1)
                return 0;

            return nums[i] > nums[i - 1] &&
                   nums[i] > nums[i + 1];
        };

        for (int i = 1; i < n - 1; ++i)
            peak[i] = isPeak(i);

        build(1, 0, n - 1);

        vector<long long> answer;

        for (const auto& q : queries) {
            if (q[0] == 1) {
                int l = q[1];
                int r = q[2];

                if (r - l + 1 < 3) {
                    answer.push_back(0);
                    continue;
                }

                // Only interior positions can be peaks.
                int left = l + 1;
                int right = r - 1;

                Node result = query(
                    1, 0, n - 1, left, right
                );

                ll len = right - left + 1;

                ll total = len * (len + 1) / 2;

                answer.push_back(
                    total - result.noPeak
                );

            } else {
                int index = q[1];
                int val = q[2];

                nums[index] = val;

                // Only three positions can change.
                for (int i = max(1, index - 1);
                     i <= min(n - 2, index + 1);
                     ++i) {

                    int now = isPeak(i);

                    if (peak[i] != now) {
                        peak[i] = now;
                        update(1, 0, n - 1, i, now);
                    }
                }
            }
        }

        return answer;
    }
};
```

