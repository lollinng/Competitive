# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        curr = ListNode(0)
        ans = curr
        while(l1 and l2):
            if(l1.val > l2.val):
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        curr.next = l2 or l1
        return ans.next


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
obj = Solution()
ans = obj.mergeTwoLists(l1, l2)
while(ans):
    print(ans.val)
    ans = ans.next
