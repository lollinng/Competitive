class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [0]*n  # initializing the dp table
        # filling the the first dp table --> low_price = prices[0] max_profit=0
        dp[0] = [prices[0], 0]
        min_price = max_profit = 0
        # Note that ---> indixing the dp table --> dp[i-1][0] stores minimum price and dp[i-1][1] stores maximum profit
        for i in range(1, n):
            # min(previous_min_price, cur_min_price)
            min_price = min(dp[i-1][0], prices[i])
            # max(previoius_max_profit, current_profit)
            max_profit = max(dp[i-1][1], prices[i]-dp[i-1][0])
            dp[i] = [min_price, max_profit]

        return dp[n-1][1]
