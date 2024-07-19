# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):

        if not root:
            return 0
        self.res = float(-inf)
        self.helper(root)
        return self.res

    def helper(self,root):
        if not root:
            return 0

        left_sum = max(self.helper(root.left),0)
        right_sum = max(self.helper(root.right),0)
        curr_sum = left_sum+root.val+right_sum
        self.res = max(self.res,curr_sum)

        return root.val+max(left_sum,right_sum)