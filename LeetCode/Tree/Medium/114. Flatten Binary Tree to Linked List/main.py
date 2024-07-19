# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
       1
    2      5
 3    4       6

        1
            2
        3      4
                    5
                  7     6
         

'''

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:

            # check left
            if curr.left:
                prev = curr.left
                # go to rightmost leaf of left
                while(prev.right):
                    prev = prev.right
                # Assign right sub tree to right's rightmost leaf of lef
                prev.right = curr.right
                # Move left sub tree to its right 
                curr.right = curr.left
                # Remove left
                curr.left = None
            
            # move to next node
            curr = curr.right
            
        

        