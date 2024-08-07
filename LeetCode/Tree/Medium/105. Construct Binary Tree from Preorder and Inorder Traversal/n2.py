# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        '''
        preorder - val,left,right : stores node in start
        inorder - left,val,right : stores the node in beetween left one becomes subtree
        '''
        if not (preorder and inorder):
            return None
            
        root = TreeNode()
        root.val = preorder[0]
        root_index = inorder.index(root.val)  # find the root_element index
        
        root.left = self.buildTree(preorder[1:root_index+1],inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:],inorder[root_index+1:])
        return root



