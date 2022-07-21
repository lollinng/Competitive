"""
To solve the stock problem of buying and selling stocks for maximum profit we using following ways
1) Create a dp table of dimension n*2, 
    where n is no. of elements and dp[i-1][0] and dp[i-1][1] depicts minimum price and maxium profit
2) Now we keep iterating throught the array using those 2 varibales in dp table and update if we find a better
    max profit or min_price in the array
"""


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
        print(dp)
        return dp[n-1][1]

    # or instead of using dp table we can use variables to store the values of max_profiy and min_price
    def maxProfit1(self, prices):
        n = len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]-min_price)
        return max_profit


s = Solution()
print(s.maxProfit1([7, 1, 5, 3, 6, 4]))
