class MedianFinder:
    
    """
    Intution:
    We have to find median of an array but in most optimal time
    Hence we add the array such that the left portion of median is max_heap and left portion is min_heap
    So we return the left maximum when elemetns odd  as median and avg top of heap if list is even

    first 
    1) We add element to left heap 
    2) pop the maximum element(max_heap) add it to right heap
    3) if right len is > left heap pop smallest elmenet and add it to left_heap
    4) this will helps us get median as left heap top when odd number elments 
        or unequal elements in both left heap will be greater or equal to righ heap by 1
    5) if both heap equal return the avg of both top heaps as median
    """

    def __init__(self):
        self.left_heap = [] # max heap
        self.right_heap = [] # min heao


    def addNum(self, num: int) -> None:
        r_len = len(self.right_heap)
        l_len = len(self.left_heap)
        
        heapq.heappush(self.left_heap,-num)
        heapq.heappush(self.right_heap,-self.left_heap[0])
        heapq.heappop(self.left_heap)

        if len(self.right_heap) > len(self.left_heap):
            heapq.heappush(self.left_heap,-self.right_heap[0])
            heapq.heappop(self.right_heap)
        
    def findMedian(self) -> float:
        r_len = len(self.right_heap)
        l_len = len(self.left_heap)
        if r_len==l_len:
            return (-self.left_heap[0]+self.right_heap[0])/2
        else:
            return -self.left_heap[0]
               


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()