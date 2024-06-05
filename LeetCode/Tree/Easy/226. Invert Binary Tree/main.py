# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root_):
            
            if root_ is None :
                return 

            temp = root_.right
            root_.right = root_.left
            root_.left = temp
            dfs(root_.right)
            dfs(root_.left)

        dfs(root)
        return root

        