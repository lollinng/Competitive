# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):

        # Calculating length
        tail = head
        length = 0
        while(tail):
            length, tail = length+1, tail.next

        # printing edge cases
        if length == 1 and n == 1:
            return None
        if length == n:
            return head.next
        else:
            # goining to node before n and changing nth nodes next to n-1 th node next
            temp = head
            for _ in range(length-n-1):
                temp = temp.next
            temp.next = temp.next.next
            return head


s = Solution()
# head = [1,2,3,4,5], n = 2   ,  removing 4
ans = s.removeNthFromEnd(ListNode(1, ListNode(
    2, ListNode(3, ListNode(4, ListNode(5))))), 2)
while(ans):
    print(ans.val)
    ans = ans.next
