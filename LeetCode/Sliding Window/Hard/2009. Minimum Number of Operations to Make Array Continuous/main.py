class Solution:
    def minOperations(self, nums):
        ''' 

        sliding window

        here we left and right pointers 

        [1,2,3,5,6]

        here left =1
            right = 1 => right=2,3,4,5,6
            hence window_size = right-left   # longest sequence
        and itertate left more



        '''



        nums_len = len(nums)
        nums = sorted(set(nums))

        
        res = nums_len
        right =  0
        new_length = len(nums)
        
        for left in range(nums_len):
   
            while right<new_length and nums[right]< nums[left]+nums_len: 
                right+=1
            
            window_size = right-left
            res = min(res,nums_len-window_size)

        return res
        
