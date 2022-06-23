class Solution:
    def count(self, S, n, m):
        self.dp = [[-1]*m] * (n+1)
        self.dp = [[-1]*m] * (n+1)
        print(len(self.dp))
        print(len(self.dp[1]))
        return self.solve(S, m-1, n)

    def solve(self, a, m, n):
        if(m == -1 and n > 0):
            return 0
        if(n == 0):
            return 1
        if(n < 0):
            return 0
        print(m, n)
        if(self.dp[m][n] != -1):
            return self.dp[m][n]

        self.dp[m][n] = self.solve(a, m, n-a[m]) + self.solve(a, m-1, n)
        return self.dp[m][n]


obj = Solution()
obj.count([1, 2, 3], 4, 3)
