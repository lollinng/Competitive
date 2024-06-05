
// Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };


/*


if its end return False
if its not equal then False
if its contains extra root other doesnt False


*/

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        
        if(!root) return false;
        // checking if main tree is subtree
        if (dfs(root,subRoot)) return true;
        // check if its kids are subtree
        return isSubtree(root->left,subRoot) || isSubtree(root->right,subRoot);
    }
    bool dfs(TreeNode* root, TreeNode* subRoot){
        //breaking condition
        if(root == nullptr && subRoot==nullptr){
            return true;
        }else if(root == nullptr || subRoot==nullptr){
            return false;
        }else if(root->val!=subRoot->val){
            return false;
        }
        // requirements conditions
        return dfs(root->left, subRoot->left) && dfs(root->right, subRoot->right);
    }    
};