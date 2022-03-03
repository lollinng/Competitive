"""
We use dfs to traverse a single side till the depth(which is calculated sperately in o(n2)) and its value to our sum and 
do the same thing
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0
    max_depth = 1

    def deepestLeavesSum(self, root):
        self.sumofleaves(root, 0)
        return self.sum

    def sumofleaves(self, node, curr):
        if(node):
            if curr > self.max_depth:
                print(curr)
                self.sum, self.max_depth = 0, curr
            if curr == self.max_depth:
                # print(node.val)
                self.sum += node.val
            self.sumofleaves(node.left, curr+1)
            self.sumofleaves(node.right, curr+1)


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
