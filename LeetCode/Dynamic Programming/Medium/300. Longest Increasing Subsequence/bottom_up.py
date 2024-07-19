from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        '''
        Memoziation giving error
        '''

        # def dfs(index,prev):
        #     key = (index,prev)
        #     if key in cache:
        #         return cache[key]

        #     # breaking condition / base case
        #     if index==len(nums):
        #         return 0

            
        #     # take and not take
        #     res = dfs(index+1,prev)
        #     # take
        #     if prev==-1 or nums[index]>nums[prev]:
        #         res = max(res,1+dfs(index+1,index))
       
        #     cache[key] = res
        #     # recurse
        #     return res


        # cache = {}
        # return dfs(0,-1)



        n = len(nums)

        # hee base case is 0 hence no need to write anything else
        dp = [[0]*(n) for _ in range(n+1)]

        # we are moving from index n->0 and prev n-1->-1 or index-1->0
        for index in range(n-1,-1,-1):
            for prev in range(index-1,-1,-1):
                # take and not take
                dp[index][prev] = dp[index+1][prev]
                # take
                if prev==0 or nums[index]>nums[prev]:
                    dp[index][prev] = max(dp[index][prev],1+dp[index+1][prev])
        
        return dp[0][0]