import heapq


class MedianFinder:
    
    '''
    Creating 2 heaps , and divide arra , left will be max heap and right will be min
    1) If number is odd the ans will top element of left heap
    2) if len is even the ans will be avg of top elements
    
    # handling heaps
    1) if new number comes it goes to left heap
    2) if left is +2 then right then left is pop and added to right

    3) if number is greater then left max then add to right
    and then if right becomes greater pop it and add one ele to left

    4) if number is samller then left max add it to left if it becomes 2 greater 
    pop it and add it to right
    '''
    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) :
   
        if not self.left_max_heap or num<=-self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap,-num)
        else:
            heapq.heappush(self.right_min_heap,num)


        # balance the heap if necessaary
        left_heap_len = len(self.left_max_heap)
        right_heap_len = len(self.right_min_heap)
        
        if  left_heap_len> right_heap_len+1:
            value = -heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap,value)

        elif left_heap_len < right_heap_len:
            value = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap,-value)
        
        
    def findMedian(self) -> float:

        left_heap_len = len(self.left_max_heap)
        right_heap_len = len(self.right_min_heap)

        if left_heap_len > right_heap_len:
            return -self.left_max_heap[0]

        return (-self.left_max_heap[0]+self.right_min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()