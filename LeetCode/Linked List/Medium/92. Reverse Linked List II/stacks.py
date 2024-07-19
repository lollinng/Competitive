# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head

        # Creating a dummy node since left can be 1 
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # creating temp(prev_state) to store previous postions
        # this position stores value of node left to reversing 
        for _ in range(left-1):
            prev = prev.next
        
        # Adding all elements in the range to stack
        stack = deque()
        current = prev.next # goto element which needs stack
        for i in range(left,right+1): 
            stack.append(current)
            current = current.next
        
        rightmost = current
        while stack:
            prev.next = stack.pop()
            prev = prev.next

        # Connecting the last part of the list
        prev.next = rightmost
        return dummy.next


