# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        
        if not head or k==1:
            return head

        # check if we need to reverse the group
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        # reverse the linked list and get the head out of it
        res = self.reverse_linked_list(head,k)

        # after reverse we know that head becomes tail of the group
        # hence next iteration of elements will be after the righmost head
        head.next = self.reverseKGroup(curr, k)
        return res
        

    def reverse_linked_list(self,head,k):
        prev= None
        curr = head
        for _ in range(k):
            temp = curr.next
            curr.next  = prev
            prev = curr
            curr = temp
        return prev