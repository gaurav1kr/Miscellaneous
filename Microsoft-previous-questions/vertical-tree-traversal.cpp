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
    vector<vector<int>> verticalTraversal(TreeNode* root) 
    {
       vector< vector<int>>ans;
        if(!root) 
        {
            return ans;
        }

        map<int,vector<pair<int,int>>>m;
        queue<pair<TreeNode*,pair<int,int>>>q;
        q.push({root,{0,0}});

        while(!q.empty())
        {
            auto it=q.front();
            q.pop();

            TreeNode* node = it.first;
            int line = it.second.first;
            int level = it.second.second;

            m[line].emplace_back(level,node->val);
           
            if(node->left!=NULL)
            {
                q.push({node->left,{line-1,level+1}});
            }
             if(node->right!=NULL)
            {
                q.push({node->right,{line+1,level+1}});
            }
        }
        
        for(auto it:m)
        {
            vector<int>level;
            sort(it.second.begin(),it.second.end());
            for(auto p : it.second)
            {
                level.push_back(p.second);
            }
            ans.push_back(level);
        }
        return ans;
    }
};
