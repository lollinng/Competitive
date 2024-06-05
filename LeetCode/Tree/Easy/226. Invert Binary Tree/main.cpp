// Definition for a binary tree node.
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
    TreeNode* invertTree(TreeNode* root) {
        // case 1
        if (root==nullptr){
            return root;
        // case 2
        }else if ((root->left==nullptr) && (root->right==nullptr)){ 
            return root;
        // case 3 recursive inverting
        }else{
            TreeNode* temp_root_right = root->right;
            root->right = invertTree(root->left);
            root->left = invertTree(temp_root_right);
            return root;
        }

    }

  

};