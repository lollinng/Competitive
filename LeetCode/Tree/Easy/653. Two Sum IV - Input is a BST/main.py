# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.cache = {}

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        if root==None:
            return False

        if root.val in self.cache:
            return True

        
        self.cache[k-root.val] = True
        
        return self.findTarget(root.left,k) or self.findTarget(root.right,k)