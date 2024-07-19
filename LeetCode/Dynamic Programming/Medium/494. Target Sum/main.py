class Solution:
    def findTargetSumWays(self, nums, target):
        
        n = len(nums)
        cache = {}
        def dfs(index,total):
            key = (index,total)
            if key in cache:
                return cache[key]
            

            if n==index and total == target:
                return 1
            elif n==index:
                return 0
        
            res = dfs(index+1,total+nums[index]) + dfs(index+1,total-nums[index]) 
            cache[key] = res 
            return res
        
        return dfs(0,0)