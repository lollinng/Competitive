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

/*
Intuition:
Here we want to get most optimal path

now we can start from the leftmost 


here temp is looking for lon string where as res looking for short solution
*/

class Solution {
public:
    int res= -300001;
    int dfs(TreeNode* root){
        
        if (!root) return 0;

        
        // Compute the maximum path sum for the left and right subtrees.
        int l = max(dfs(root->left), 0);
        int r = max(dfs(root->right), 0);

        // calculate curent pathsum
        int pathsum = root->val + l + r;

        // update the pathsum is greater then res
        res = max(res,pathsum);

        // return either left subtree/right subtree or root->val
        return  root->val + max(l,r) ;       
    }

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return res;
    }
};