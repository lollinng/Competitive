import math


class Solution:
    def minEatingSpeed(self, piles,h):
        
        '''
        since here the problem/bottle neck is lower bananaas
        hence we sort array

        [3,6,7,11]
        
        Solution 1: Binary search on k and check validation later  O(nlogn)
        1) max speed of eating i.e k will be 
            max element in the array
        2) minimum speed should be which may or may not follow constraint be
            sum()//8 
        and we can run binary serach on the the k values between them and check if conditions are true

        '''

        def check_valid(eating_speed):
            hours_took = 0 
            for bananas in piles:
                # math.cield return 
                # 6/4 as 2 , 7/4 as 2 and 11/4 as 3
                hours_took += math.ceil(bananas/eating_speed)
            return hours_took<=h


        total_sum = sum(piles)
        low = max(1,total_sum//h)
        high = max(piles)

        while low<=high:
            mid = low + (high-low)//2
            if check_valid(mid)==True:
                result = mid          # updating reusle since we need first ocurrance
                high = mid-1
            else:
                low = mid+1

        return result
