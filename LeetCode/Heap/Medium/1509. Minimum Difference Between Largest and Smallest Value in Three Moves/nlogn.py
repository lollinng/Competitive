class Solution:
    def minDifference(self, nums):
        
        '''
        one move can change one value
        and have to use 3 moves
        and return minium difference in the array

        n = len(array)
        if n<4  return 0 # since I can change 3 values equal to the 4th element

        it will optimal sort the element so I can change minimum and maximum element
        if n>4  
        1)  XXX arr  
        2)  XX arr X
        3)  X arr XX
        4) arr XXX

        I have to caculate range of arr elements remaniing in the aboce scenario which will be
        1) arr[-1]-arr[3]
        2) arr[-2]-arr[2]
        3) arr[-3]-arr[1]
        4) arr[-4]-arr[0]
        
        I have to find max of these for the minimal difference
        
        Time complexity will be O(nlogn) + O(1) : mostly for sorting
        Space complexity will be O(1) 
        '''
        if len(nums)<5:
            return 0
        nums.sort()
        res =  min(nums[-1]-nums[3],nums[-2]-nums[2],nums[-3]-nums[1])
        res = min(res,nums[-3]-nums[1],nums[-4]-nums[0])
        return res