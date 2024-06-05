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

recursion : Inorder traversal

beak condition : root null return ans(k)
parse: left , got to leftmost

calculation : subtract 1 from k if equal to zero print the value

parse right : 

*/

class Solution {
public:

    void inorder_trav(TreeNode* root,int &k, int &ans){
        if (root==NULL){
            return;
        }

        inorder_trav(root->left,k,ans);
       
        k--;
        if(k==0){
            ans = root->val;
            return;
        }
        
        inorder_trav(root->right,k,ans);
    }

    int kthSmallest(TreeNode* root, int k) {
        int ans = -1;
        inorder_trav(root,k,ans);
        return ans;

    
    }
};