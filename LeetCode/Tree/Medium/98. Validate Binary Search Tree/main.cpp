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
Intuition
1) recursion/DFS problem since I have to check for every node if bst propperty is present
2) all the the children node should have thier return 'and'since we want to check if its false
3) It can have one child also
4) if child not there return True
5) 

*/


class Solution {
public:

    bool dfs(TreeNode* root,long long max,long long min){
        if (root==NULL) return true;


        cout<<max;
        if (root->val > min and root->val<max){
            // if both subtree are bst parent will also be bst
            // updating max in left subtree(so that no element goes beyond parent parent node) and min in right subtree
            // for eg - 5 left-> 1 right-> 6  this shouldnt happen hence we keeping check with max value for left side
            // and 
            return dfs(root->left,root->val,min) and dfs(root->right,max,root->val);
        }

        return false;

    }


    bool isValidBST(TreeNode* root) {
        long long max = 2147483649;
        long long min = -2147483649;
        return dfs(root,max,min);
    }
};