# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head

        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy

        # getting to pre left index
        for _ in range(left-1):
            prev = prev.next

        # reverse from left to right
        bkwd_node = None 
        fwd_node = prev.next
        '''
        iterator , temp , prev_ele
        2           3       None
        3           4       2
        4           5       3
        '''
        for _ in range(left,right+1):
            temp = fwd_node.next 
            fwd_node.next = bkwd_node
            bkwd_node = fwd_node
            fwd_node = temp

        # Adjust the broken linkage
        temp = prev.next
        prev.next = bkwd_node
        temp.next = fwd_node

        return dummy.next


