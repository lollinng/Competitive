"""
Here we try to use pointers and sliding windows concept to find minimum
number of jumps required to last index
here we start from first index with option to jump max of its index_val

we create left and right pointers which shows farthest jump and +1 jump
from last farthest that we can take at each jump

Then we iterate through left and right pointer to find next farthest jump


"""




class Solution:
    def jump(self, nums):
        
        jump = 0
        l = 0
        r = 0
        while r<len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
            l = r+1
            r = farthest
            jump+=1
        
        return jump


