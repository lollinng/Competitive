# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        '''

        find mid
        and then parition the linked list using mid
        recursivelly sort the linked list 
        
        now i will get left and right pointer of partitioned linked list
        and then I will merge the linked list in sorted order one by one using demo node

        '''

        # handling the base case
        if not head or not head.next:
            return head

        # finding mid
        slow  , fast = head,head.next
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next

        # partionaining the linked list
        mid = slow.next
        slow.next = None   

        # recursing the array
        left = self.sortList(head)
        right = self.sortList(mid)


        # merging the partitons
        dummy = ListNode(0)
        curr = dummy
        while left and right: 
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            
            curr = curr.next

        # append the remaining nodes
        curr.next = left or right   

        return dummy.next