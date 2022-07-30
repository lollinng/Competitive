"""


"""


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [amount+1]*(amount+1)
        print(len(dp))
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i-coin < 0:
                    break
                if dp[i-coin] != amount+1:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        print(dp)
        return dp[-1] if dp[-1] != (amount+1) else -1


coins = [474, 83, 404, 3]
amount = 264
obj = Solution()
print(obj.coinChange(coins, amount))
