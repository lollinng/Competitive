
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        '''

        if new element is between left and right inclisive
        [a]        a will be r-l = 0-1 = 1 
        [a,b]      2 will be added (a,b and b) to sinc r-l = 1-(-1) = 2  
        [a,b,c]    at c 3 will be added (a,b,c b,c c) r-l = 2-(-1) = 3 
      
        if new element is  greater then right
        [a,b,c]    count till now make it 0 and move left to current index

        if new element is less then left
        [a,b,c]    c will add only a,b b,a and not c  hence it will  prev r-l=2 which means curr_count
        '''
        res = 0
        l = -1
        curr_count = 0
        for r,ele in enumerate(nums):
            # if its less then left
            if ele<left and r>0:
                res+=curr_count
            # if its grater then right
            elif ele>right:
                curr_count = 0
                l = r
            # if its between left and right
            elif left<=ele<=right:
                curr_count = r-l
                res+=curr_count

        return res