"""
Intution :

1) have a list 
2) update the list and check if -i of element presrent in it
3) if yes check if its larger then previous res element if yes then make it res



"""


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        """
        #Using two pointers and sort , second fastest
        nums.sort()
        l = 0
        r = len(nums)-1
        while(l<r and nums[l]<0):
            if abs(nums[l]) == nums[r]:
                return nums[r]
            elif abs(nums[l])>nums[r]:
                l+=1
            else:
                r-=1
        return -1
        """


        

        '''
        # Using sets (fastest)
        res = -1
        nums = set(nums)
        for num in nums:
            if num * -1 in nums:
                res = max(res, num)
        return res
        '''
        '''
        # Using list
        res = -1
        data = []
        for i in nums:
            if -i in data and res<abs(i):
                res = abs(i)        
            data.append(i) 
        return res
        '''