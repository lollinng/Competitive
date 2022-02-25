"""
Here we create a linked list sum and refer our ans linked list to it .
If the value of input node is 0 and the 0 isn't last element , we add the node to our sum list and move the sum list to next node .
Otherwise if we encounter a number we adds it value to current sum node
while returning we return ans with 2 next , coz we wanna go to sum node and print the intial 0 value that we used to intialise the sum node

"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head):
        sum = ListNode(0)
        ans = ListNode(0, sum)
        while(head):
            if(head.val == 0 and head.next):
                sum.next = ListNode(0)
                sum = sum.next
            else:
                sum.val += head.val
            head = head.next

        return ans.next.next

# For testing


x = ListNode(0, ListNode(3, ListNode(1, ListNode(
    0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
obj = Solution()
ans = obj.mergeNodes(x)
while(ans):
    print(ans.val)
    ans = ans.next
