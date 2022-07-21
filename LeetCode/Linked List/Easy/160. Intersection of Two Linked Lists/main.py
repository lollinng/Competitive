"""
Here we can have to check the intersect of 2 linked lists . We will use 2 pointers a and b since there are multiple cases of types of
lists the lists can be as shown in explainiation.txt we have to iterated through the list intill a and b meet at a common point or both
of them becom null . At the second iteration the a and b will always meet either at common node or at last.Coz they will be travelling same distsance
that is the lenght of both lists.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB
        while(a != b):
            if(a != None):
                a = a.next
            else:
                a = headB
            if(b != None):
                b = b.next
            else:
                b = headA
        return a


# l1 = ListNode(1, ListNode(9, ListNode(1, ListNode(2, ListNode(4)))))
# l2 = ListNode(3, ListNode(2, ListNode(4)))
# obj = Solution()
# ans = obj.getIntersectionNode(l1, l2)
# while(ans):
#     print(ans.val)
#     ans = ans.next
