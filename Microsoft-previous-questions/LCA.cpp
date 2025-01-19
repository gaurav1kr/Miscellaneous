/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution 
{
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* n1, TreeNode* n2) 
    {
       if (root == NULL) 
           return NULL; 
       if (root->val == n1->val || root->val == n2->val) 
            return root; 
  
       TreeNode *left_lca  =  lowestCommonAncestor(root->left, n1, n2); 
       TreeNode *right_lca =  lowestCommonAncestor(root->right, n1, n2); 
  
       if (left_lca && right_lca)  return root; 
            return (left_lca != NULL)? left_lca: right_lca; 
    }
};
