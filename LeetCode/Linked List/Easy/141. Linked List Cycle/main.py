"""
In order to find a cycle we use tortoise and rabbit analogy where we keep the rabbit running faster then tortaise only to hope that they
meet later in circle list . If the list isnt circle and rabbit meets None we return -1
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head):

        try:
            slow = head
            fast = head.next
            while(slow != fast):
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


head = ListNode(1, ListNode(2))
tail = ListNode(0, ListNode(4))
head.next.next = tail
tail.next.next = head.next
i = 0
# while(head):
#     i += 1
#     print(head.val)
#     head = head.next
#     if(i == 9):
#         break


obj = Solution()
ans = obj.hasCycle(head)
print(ans)
