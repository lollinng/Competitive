"""
We create a linked list to store the addition of the 2 linked list . we loop if we have elements in l1 or l2 or if carry is not 0;
We add values to carry using if statmetns to avoid accessing .val of a null type node of liked list.
then we add remainder of the 10 modulus to ans liked list and send carry for the next loop

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ans = sums = ListNode(0)
        # or carry coz we run loop if carry has some value
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, remainder = divmod(carry, 10)
            # remainder = carry%10
            # carry = int(carry/10)
            sums.next = ListNode(remainder)
            sums = sums.next
        return ans.next


# testing
obj = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
ans = obj.addTwoNumbers(l1, l2)
while(ans):
    print(ans.val)
    ans = ans.next
