# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Go to tail and iterate your way back checking the highest elemment yet
'''

class Solution:
    def removeNodes(self, head):
        
        '''
        [5,15,2,9,4,13,2,1,3,8] , 8  
        [15,13,8]
        '''

        def reverse(head_):     
            head_,tail = head_,None
            while(head_):
                temp = head_.next
                head_.next = tail 
                tail = head_
                head_ = temp
            return tail

        # Reversing the linked list (tail)
        cur = prev = reverse(head)

        # iterating from cur and removing elements smaller then the left elements
        max_ele = cur.val
        while cur.next:
            if cur.next.val < max_ele:
                cur.next = cur.next.next
            else:
                cur = cur.next
                max_ele = cur.val
        
        # Reversing the linked list (prev)
        return (reverse(prev))
       