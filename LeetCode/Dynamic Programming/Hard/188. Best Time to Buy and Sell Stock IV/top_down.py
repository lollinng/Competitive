class Solution:
    
    def __helper(self,index,counter,prices,n,k):
        
        # Base case: Index reachers  end of price return profit
        if index==n or counter==k:
            return 0

        key = (index,counter)
        if key in self.memo:
            return self.memo[key]

        if counter%2==0:
            self.memo[key] = max(-prices[index] + self.__helper(index+1,counter+1,prices,n,k) , self.__helper(index+1,counter,prices,n,k))
        else:
            self.memo[key] = max(prices[index] + self.__helper(index+1,counter+1,prices,n,k) , self.__helper(index+1,counter,prices,n,k))
        
        return self.memo[key] 

    def maxProfit(self, k, prices):

        self.memo = {}
        n = len(prices)
        return self.__helper(0,0,prices,n,2*k)