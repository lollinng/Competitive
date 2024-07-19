class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        total_coins = len(coins)
        dp = [[0] * (amount+1) for _ in range(total_coins+1)]
        for row in range(total_coins+1):
            dp[row][0] = 1
        
        for row in range(1,total_coins+1):
            for amt in range(1,amount+1):
                
                # If new coin can be used based on previous amt-coin
                # else just use above value
                if amt - coins[row-1] >=0: # since i one is updated coz of extra buffer
                    dp[row][amt] = dp[row-1][amt] + dp[row][amt-coins[row-1]]
                else:
                    dp[row][amt] = dp[row-1][amt]
        
        return dp[-1][-1]

