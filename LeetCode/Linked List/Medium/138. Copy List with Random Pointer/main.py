
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head

        # copy each node
        node = head
        while node:
            copy = Node(node.val)   # creating deep copy
            copy.next = node.next   # aligning deep copy
            node.next = copy        # aligning deep copy
            node = copy.next        # parsing
            
        # ALIGNING THE RANDOM POINTERS
        node = head
        while node:
            if node.random:                           # If ranomd is a null ptr 
                node.next.random =  node.random.next   
            node = node.next.next
        
        # decoupling the copy and the main node
        node = head
        deepcopyhead = dcnode = node.next  if node else None
        while node:
            # if deepcopy exist
            if dcnode:
                node.next = dcnode.next
            else:
                node.next = None
            node = node.next         # iterate tho next valid node which was intialised above
            
            # if valid node exist 
            if node:
                dcnode.next = node.next
            else:
                dcnode.next = None
            dcnode = dcnode.next
        return deepcopyhead
            

            
