class Solution:
    def canPartition(self, nums: List[int]) -> bool:
            total = sum(nums)
            # equal partition check
            if total % 2 != 0:
                return False 
            target = total // 2

            num_len = len(nums)
            
            dp = [[False]*(target + 1) for _ in range(num_len+1)]
            
            for i in range(num_len+1):
                dp[i][0] = True
            
            for row in range(1,num_len+1):
                for col in range(1,target+1):

                    dp[row][col] = dp[row-1][col]

                    if col - nums[row-1]>=0:
                        dp[row][col] = dp[row][col] or dp[row-1][col-nums[row-1]]
      
            return dp[-1][-1]

