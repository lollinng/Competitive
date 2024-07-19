# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if node is None:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)

        traversal = dfs(root)
        

        def build(l,r):
            if r < l:
                return None

            m = (l+r)//2

            node = TreeNode()
            node.val = traversal[m]

            node.left = build(l,m-1)
            node.right = build(m+1,r)
            return node

        return build(0,len(traversal)-1)

