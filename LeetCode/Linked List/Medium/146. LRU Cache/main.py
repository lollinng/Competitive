class Node:
    def __init__(self,key=None,val=None):
        
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity 
        self.head = self.tail = Node(-1,-1)
        self.head.next,self.tail.prev = self.tail,self.head
    
    def __remove(self,node):
        prev,next_ = node.prev,node.next
        prev.next,next_.prev = next_,prev

    def __insert(self,node):
        prev,tail = self.tail.prev,self.tail
        prev.next = tail.prev = node
        node.next,node.prev = tail,prev

    def get(self, key: int):
        if key not in self.cache:
            return -1
        
        # move element to tail
        self.__remove(self.cache[key])
        self.__insert(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int):
        # if new key 
        if key in self.cache:
            self.__remove(self.cache[key])
        
        new_node = Node(key,value)
        self.__insert(new_node)
        self.cache[key] = new_node
        
        # if capacitry exceeded
        if len(self.cache) > self.capacity:
            del_node = self.head.next
            self.__remove(del_node)
            del self.cache[del_node.key]
            






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)