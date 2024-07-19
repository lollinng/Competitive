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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        head = root
        iterator = stationary = Node(0)  # kid is ptr for traversing the child level, temp is dummy ptr to just store kid starting position
        
        while head:


            # terverse the level
            while head:
                if head.left:
                    # applying next to left
                    iterator.next = head.left
                    iterator = iterator.next

                if head.right:
                    iterator.next = head.right
                    iterator = iterator.next
                
                # move to right if its not righmost in the level
                head = head.next
            
            head = stationary.next
            iterator = stationary
            iterator.next = None                     # Reset the dummy node's next for the next level
        return root
