/**
 * Definition for a binary tree node. 
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

/*
Intuition:
Here we have 
convert tree to string using : serialize
convert string to tree usign : deserialize

One way to do this is by using preorder(val,left,right)

1) we can parse through every node append its value to string
2) we will append null for its childrens

3) for creating the tree we will append string into queue
4) at each recursion we access the queue front and pop it
5) poped element is added to tree it its node accoridn to preorder algo
6) else if its null then we return null 
*/


class Codec {
public:
    
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string ans="";
        buildString(root,ans);
        return ans;
    }

    void buildString(TreeNode* root, string &res)
    {
        if(root == NULL)
        {   res += "null,";
            return;
        }
        
        res += to_string(root->val) + ",";
        buildString(root->left, res);
        buildString(root->right, res);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        // we will be using queue to acces the elements from the string
        string ele = "";
        queue<string> q;
        for (char c: data){
            if(c==','){
                q.push(ele);
                ele="";
            }else{
                ele+=c;
            }
        }
        return buildtree(q);
    }

    TreeNode* buildtree(queue<string> &q){
        string s = q.front();
        q.pop();

        if (s=="null"){
            return NULL;
        }

        TreeNode* root = new TreeNode(stoi(s));
        root->left = buildtree(q);
        root->right = buildtree(q);
        return root;
        
    }


};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));