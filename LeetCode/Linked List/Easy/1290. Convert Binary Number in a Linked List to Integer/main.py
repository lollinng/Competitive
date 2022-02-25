# Definition for singly-linked list. # for testing
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
we conevert binary to decimal by multiplying existing sum by 2 and adding the liked list binary value
as shown in the picture
"""


class Solution():
    def getDecimalValue(self, head):
        sum = 0
        while head:
            sum = 2*sum + head.val
            head = head.next
        return sum


# For testing
x = ListNode(1, ListNode(0, ListNode(1)))
obj = Solution()
print(obj.getDecimalValue(x))
