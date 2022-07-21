"""
Here we change the curr next to previous and iterate our way from head to tail
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


# [1,2,3,4,5]
list_ = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
obj = Solution()
ans = obj.reverseList(list_)
while(ans):
    print(ans.val)
    ans = ans.next
