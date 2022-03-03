# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deepestLeavesSum(self, root):
        depth = self.maxdepth(root)
        return self.sumofleaves(root, depth, 0)

    def maxdepth(self, node):
        if(node == None):
            return -1
        return 1 + max(self.maxdepth(node.left), self.maxdepth(node.right))

    def sumofleaves(self, node, depth, curr):
        if(node):
            if curr == depth:
                print(node.val)
                return node.val
            else:
                return self.sumofleaves(node.left, depth, curr+1) + self.sumofleaves(node.right, depth, curr+1)


s = Solution()
# root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
"""
left node - 2n+1
right node - 2n+2
                        1
                    2        3
                4      5        6
            7                      8      
"""
input = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)),
                 TreeNode(3, TreeNode(6, TreeNode(8))))
print(s.deepestLeavesSum(input))
