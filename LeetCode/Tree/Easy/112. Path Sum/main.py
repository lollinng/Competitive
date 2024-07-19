# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        return self.helper(root,targetSum)
        
    def helper(self,root,targetSum):
        
        if not root:
            return False
        
        targetSum -= root.val
        if targetSum==0 and not (root.left or root.right):
            return True

        return self.helper(root.left,targetSum) or self.helper(root.right,targetSum)