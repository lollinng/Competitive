class Solution:
    def jump(self, nums):
        
        res = 0
        l = 0
        farthest = 0
        end = 0
        while l<len(nums)-1:
            farthest = max(farthest,l+nums[l])

            if farthest==len(nums)-1:
                res+=1
                return res


            if l==end:
                res+=1
                end = farthest

            l+=1
        return res


