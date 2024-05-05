
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1->2->3
# 1.prev = 1.next , 1.next = None, curr = 1.next
# 1<-2<-3

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return None


        # Getting half index in the linked list
        '''
        # Locate the mid point of linked list
        # First half is the linked list before mid point
        # Second half is the linked list after mid point
        '''
        fast , slow = head,head
        while fast and fast.next :
            slow,fast = slow.next,fast.next.next
        mid = slow

        print(slow.val)

        # revserse the second part of the list , curr will go out of index,prev will store the head
        curr,prev = mid,None
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        
        head_of_second_rev = prev
        
        # ------------------------------------------
        # Update link between first half and reversed second half
        
        first, second = head, head_of_second_rev
        
        while second.next:
            
            next_hop = first.next
            first.next = second
            first = next_hop
            
            next_hop = second.next
            second.next = first
            second = next_hop


        
        