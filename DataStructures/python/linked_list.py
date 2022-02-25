class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


x = ListNode(0)
y = ListNode(1)
z = ListNode(12)
x.next = y
y.next = z


# or

x = ListNode(0, ListNode(1, ListNode(12)))

while(x):
    print(x.val)
    x = x.next
