"""
here we are trying to create a cicular queue working on FIFO concept using linked list

Solution:
1) we create linked list class for creating and acessing linkList Nodes
2) we create basic fucntions front,rear,isEmpty,isFull for basic opartoins
3) Enqeue function add node to queue if empty it creates first node or else it updates tail pntr
4) Deque function removes the oldest node added i.e the head node
"""


class ListNode:
    def __init__(self,value=None,nxt=None):
        self.value = value
        self.next = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.head = None
        self.tail = None
        
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        newNode = ListNode(value)
        if self.isEmpty():
            self.head = self.tail =  newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.size+=1
        return True    
            
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = self.head.next 
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.value 

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
    
        


# Your MyCircularQueue object will be instantiated and called as such:

# ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
# [[3],[1],[2],[3],[4],[],[],[],[4],[]]

obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
print(param_1)
param_1 = obj.enQueue(2)
print(param_1)
param_1 = obj.enQueue(3)
print(param_1)
param_1 = obj.enQueue(4)
print(param_1)
param_4 = obj.Rear()
print(param_4)
param_6 = obj.isFull()
print(param_6)
param_2 = obj.deQueue()
print(param_2)
param_1 = obj.enQueue(4)
print(param_1)
param_4 = obj.Rear()
print(param_4)
