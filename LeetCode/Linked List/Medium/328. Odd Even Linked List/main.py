# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):

        '''
        we will iteratre throughb the linked list

        1) we will make odd.next = odd.next.next
        2) AND MAKE even.next = even.next.next

        '''

        if not (head and head.next):
            return head
        
        odd,even = head,head.next
        evenhead = even

        while even and even.next :
            odd.next = odd.next.next 
            even.next = even.next.next
            even = even.next
            odd = odd.next
    
        
        odd.next = evenhead
        return head


        
