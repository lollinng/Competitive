"""
Steps we follow to rotate a linked list
1) Capture the value of the linedlist using tail node
2) use modulas to divide k (breaking value) by lenght to avoid loop rotations in 360*
3) use temp node to break at kth point and intialise ur answer node from there
4) later put temp,next to null so that element becomes last element
4) now join tail node to head node , hence we get our ans
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        # if list is empty
        if not head:
            return head

        # Get length of the liked list
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length = length + 1

        k = k % length
        if k == 0:
            return head

        # Mov to pivot(where we delete the connections) and rotate
        tempNode = head
        for i in range(length-k-1):
            tempNode = tempNode.next
        Ans = tempNode.next                  # saving the nodes after k into ans
        tempNode.next = None                 # removing links between node afet k
        # Adding last node(from Ans) to the head
        tail.next = head
        return Ans


obj = Solution()
ans = obj.rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2)
while(ans.next):
    print(ans.val)
    ans = ans.next
