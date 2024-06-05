
//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
/*
You can see the structure of the bst
left node < parent node < right node
Hence we can use this to find LCA 
The common ancester will have value between this two

*/
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int min_val = min(p->val,q->val);
        int max_val = max(p->val,q->val);
         while(true){
            if (min_val<=root->val && root->val<=max_val){
                return root;
            }else if(min_val>root->val){
                root = root->right;
            }else if (max_val<root->val){
                root = root->left;
            }
        }
        
    }
};




