# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
            return 
        

        curr = head
        dummy = prev  = ListNode(0,head)
        duplicate = -101

        while curr.next:
            
            # check if current element and next element is duplicate
            if curr.val == curr.next.val:
                duplicate = curr.val

            # curretn element duplidcate
            if curr.val == duplicate:
                prev.next = curr.next
            # if curetn elementn  is  not duplicate
            else:
                prev = prev.next 
        
            curr = curr.next  # iteration

        # if last element is also duplicate
        if curr.val==duplicate:
            prev.next = None
        
        return  dummy.next
            