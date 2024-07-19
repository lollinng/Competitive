import heapq


class Solution:
    def minDifference(self, nums):
        k = 3+1
        if len(nums)<k:
            return 0

        # the solution is to Sort elements and then
        #  subtract 0,-4 , 1,-3 , 2,-2 , 3,-1
        # hence instead of sorting array we sorting only k elements
        big = heapq.nlargest(k,nums)[::-1]
        small = heapq.nsmallest(k,nums)
   
        res = float(inf)
        for i in range(k):
            next_small_ele = small.pop()
            next_big_ele = big.pop()
            res = min(res,(next_big_ele-next_small_ele))
        return res