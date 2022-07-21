"""
here we using 2 pointers . Fast poiter gets the headstart or starts from n and slow pointer starts from 0 . We then iterate 
till the fast pointer reaches the end of array after reaching end slow  will be aligned as total_lenght - n that is what we 
want and we skip the next element to form a list without nth element from the back 
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):

        # Calculating length
        slow = fast = head
        for _ in range(n):
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
