class Solution:
    def maxProfit(self, prices):
        total_days = len(prices)
        # dp array which signifies how much profit at 1th day
        dp = [0 for _ in range(total_days)]

        for i in range(1,total_days):
            if prices[i] > prices[i-1]:
                dp[i] = prices[i]-prices[i-1] 
            dp[i]+=dp[i-1]

        return dp[-1]

    