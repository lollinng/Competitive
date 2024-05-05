# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


list_ = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
question = list_.next.next

obj = Solution()
ans = obj.deleteNode(question)
while(list_):
    print(list_.val)
    list_ = list_.next
