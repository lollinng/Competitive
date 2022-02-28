# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        length = 0
        tail = head
        while(tail.next):
            length += 1
            tail = tail.next
        if(length % 2 == 0):
            length = int(length/2)
        else:
            length = int(length/2)+1
        for i in range(length):
            head = head.next
        return head


obj = Solution()
# input  - [1,2,3,4,5,6]
ans = obj.middleNode(ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5, ListNode(6,)))))))
while(ans):
    print(ans.val)
    ans = ans.next
