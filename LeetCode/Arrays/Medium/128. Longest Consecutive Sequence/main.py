class Solution:
    def longestConsecutive(self, nums):
        
        if nums == []:
            return 0
        
        nums.sort()
        '''
        [1,2,5,10,11,12,15,16]
        '''
        res = 1
        temp = 1
        for i,c in enumerate(nums):
            if i==0:
                continue
            if nums[i] == nums[i-1]+1:
                temp+=1
            elif nums[i] == nums[i-1]:
                pass
            else:
                res=max(temp,res)
                temp = 1

        res=max(temp,res)
        return res