"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        if not root:
            return None
        
        curr = root

        
        while curr.left :
            
            # One LEVEL TRAVERLSAl
            head = curr
            while head:
                
                # attach next to left
                head.left.next = head.right

                
                # if node is not righmost
                if head.next:
                    # attach next to left
                    head.right.next = head.next.left
                
                # move to right in level order
                head = head.next
             
            # iterating to below level
            curr = curr.left

        return root