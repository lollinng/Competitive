# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        
        def helper(root,min_no,max_no):
            if not root:
                return True

            if min_no<root.val<max_no:
                return helper(root.left,min_no,root.val) and helper(root.right,root.val,max_no) 

            return False

        if not root:
            return True
        max_no = float(+inf)
        min_no = float(-inf) 
        return helper(root,min_no,max_no)

        