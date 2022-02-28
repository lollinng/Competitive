# Definition for singly-linked list.
from sympy import Le


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):

        # Calculating length
        slow = fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        print(fast.val, slow.val)
        while(fast.next):
            fast, slow = fast.next, slow.next
        print(fast.val, slow.val)
        slow.next = slow.next.next
        return head


s = Solution()
# head = [1,2,3,4,5], n = 2   ,  removing 4
ans = s.removeNthFromEnd(ListNode(1, ListNode(
    2, ListNode(3, ListNode(4, ListNode(5))))), 2)
while(ans):
    print(ans.val)
    ans = ans.next
