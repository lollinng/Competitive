
//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {

        if(root == nullptr){
            return 0;
        }

       return dfs(root,1);

    }

    int dfs(TreeNode* root,int res){
        // return condition
        if(root->left==nullptr && root->right==nullptr){
            return res;
        }

        // traversal / recursion
        int res1= 0;
        int res2 = 0;
        if(root->left!=nullptr)
            res1 = dfs(root->left,res+1);

        if (root->right!=nullptr)  
            res2 = dfs(root->right,res+1);

        // returning value
        return max(res1,res2);
    }

};