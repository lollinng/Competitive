class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        cache = {}
        # def dfs(index,buy):


        #     if (index,buy) in cache:
        #         return cache[index,buy]

        #     if index>=n:
        #         return 0

        #     if buy:
        #         res = max(dfs(index+1,True) , dfs(index+1,False)-prices[index])
        #     elif not buy and index!=0:
        #         res = max(dfs(index+1,False) , dfs(index+2,True)+prices[index])    
          
            
        #     cache[index,buy] = res
        #     return res


        # return dfs(0,True)

        dp = [[0]*(2) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(2-1,-1,-1):
                if j==1:
                    # if buying choose to buy or skip
                    res = max(dp[i+1][1] , dp[i+1][0]-prices[i])
                else:
                    if i+2<n+1:
                        res = max(dp[i+1][0] , dp[i+2][1]+prices[i])
                    else:
                        res = max(dp[i+1][0] , prices[i])    
                dp[i][j] = res

        return dp[0][1]