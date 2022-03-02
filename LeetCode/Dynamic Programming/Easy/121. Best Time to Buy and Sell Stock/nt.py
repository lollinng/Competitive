class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy_price = prices[0]
        for c in prices:
            if(c > buy_price):
                profit = max(profit, c-buy_price)
            buy_price = min(buy_price, c)
        return profit
