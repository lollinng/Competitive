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

preorder is : val , left , right
inorder is : left , val , right

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

1) so root is preorder[0]
2) get the index of  the root in inorder 
3) now root->left(left subrtree) = everything before root index in inorder
4) root->right(left subrtree) = everything after root index in inorder

4) we increase one in preorder_index for recursion to access the next left root node
5) we increase one+relative_index of root in preorder_index for recursion to access the next right root node


*/

class Solution {
public:

    TreeNode*  constructTree(vector<int>&preorder,int preStart,int preEnd,vector<int> &inorder,int inStart,int inEnd,map <int,int> &inorder_map){
        
        // if pointers out of current subtree limits
        if (preStart>preEnd || inStart>inEnd) return NULL;

        TreeNode* root = new TreeNode(preorder[preStart]);
        int root_index = inorder_map[root->val];  // root index in inorder map //divides left and right subtree
        int reltive_root_index = root_index - inStart;  //no. of left elements
        preStart += 1; // going froward from the current root node 

        //  going left we want preEND as reltive_root_index+1  and inEnd subtracted as root -1      
        int l_preEnd = preStart+reltive_root_index; // indicates left side elements
        int l_inEnd = root_index -1;          // till left subtree end
        root->left = constructTree(preorder,preStart,l_preEnd,inorder,inStart,l_inEnd,inorder_map);

        // goinf right we want preStart and inStart added by the nElem
        int r_preStart = preStart + reltive_root_index ; // skipping left elements for root node
        int r_inStart = root_index + 1;      // right subtree

        root->right = constructTree(preorder,r_preStart,preEnd,inorder,r_inStart,inEnd,inorder_map);
        return root;

    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        
        // using poointers to locate elements in left and right side
        int preStart = 0,preEnd = preorder.size()-1;
        int inStart = 0,inEnd = inorder.size()-1;

        map<int, int> inorder_map;

        // collecting all the indexes in the arry
        for (int i = 0; i < inorder.size(); i++) {
            inorder_map[inorder[i]] = i;
        }
        return constructTree(preorder, preStart, preEnd, inorder, inStart, inEnd, inorder_map); 
    }
};