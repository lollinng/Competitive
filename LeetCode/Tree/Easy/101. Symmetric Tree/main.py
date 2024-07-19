# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        if root==None:
            return True
        return self.CheckSymmetric(root.left,root.right)
        

    def CheckSymmetric(self,leftNode,rightNode):
        if leftNode==None and rightNode==None:
            return True
        if leftNode==None or rightNode == None:
            return False

        if leftNode.val!=rightNode.val:
            return False
        
        return self.CheckSymmetric(leftNode.left,rightNode.right) and self.CheckSymmetric(leftNode.right,rightNode.left)
        
