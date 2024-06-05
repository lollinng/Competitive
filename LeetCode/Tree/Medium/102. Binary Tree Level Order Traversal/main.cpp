#include <vector>
using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}


class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        
        vector<vector<int>> res;  
        if(root==NULL)return res;

        // using queue to store and remove nodes in bfs
        queue<TreeNode*>q;
        q.push(root);
        
        while(!q.empty()){

            int s = q.size();
            vector<int> cur_vec;
            for(int i=0;i<s;i++){
                TreeNode *node=q.front();
                q.pop();
                if(node->left!=NULL)q.push(node->left);
                if(node->right!=NULL)q.push(node->right);
                cur_vec.push_back(node->val);
            }
            res.push_back(cur_vec);
        }
        return res;
    }

};