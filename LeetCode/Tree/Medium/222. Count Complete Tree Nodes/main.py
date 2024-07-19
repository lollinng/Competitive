# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def depthOfNode(node,direction):
            d = 0
            while node:
                d+=1
                if direction=='left':
                    node = node.left
                else:
                    node = node.right
            return d

        
        ld = depthOfNode(root.left,'left') 
        rd = depthOfNode(root.right,'right')
        if ld==rd:
            return 2**(ld+1)-1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1