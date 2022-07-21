# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        length = 0
        curr = head
        while(curr):
            length += 1
            curr = curr.next
        # if its odd it will give list starting from mid if its even it wil give list starting from second mid
        # Eg - int(5/2) = 2      and int(6/2) = 3
        for _ in range(0, int(length/2)):
            head = head.next
        return head


obj = Solution()
# input  - [1,2,3,4,5,6]
ans = obj.middleNode(ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5, ListNode(6,)))))))
while(ans):
    print(ans.val)
    ans = ans.next
