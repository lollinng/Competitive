class Solution:

    def fib(self, n):
        # please one to forget about 0 index and start storing number with 1 index
        memo = [None]*(n+1)

        def recursion(self, n, memo):
            if(memo[n] != None):
                return memo[n]

            if(n <= 1):
                return n
            memo[n] = self.recursion(n-1, memo)+self.recursion(n-2, memo)
            return memo[n]

        return self.recursion(n, memo)


s = Solution()
print(s.memo(4))
