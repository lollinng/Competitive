def maxProfit(self, k: int, prices):
        n = len(prices)
        dp = [[0]*(2*k+1) for _ in range(n+1) ]

        for index in range(n-1,-1,-1):
            for counter in range(2*k-1,-1,-1):

                if counter%2==0:
                    dp[index][counter] = max(-prices[index] + dp[index+1][counter+1] , dp[index+1][counter])
                else:
                    dp[index][counter] = max(prices[index] + dp[index+1][counter+1] , dp[index+1][counter])

        return dp[0][0]