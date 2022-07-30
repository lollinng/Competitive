"""
Here we are trying to find the no. of ways from left most top index to righmost bottom index given that
we can go only right and down

intuition-
1) we use dp here to find all the possible solution
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[0]*n for _ in range(m)]
        mem[0][0] = 1
        for i in range(m):
            for j in range(n):

                if(j > 0 and i > 0):
                    mem[i][j] = mem[i][j-1] + mem[i-1][j]
                elif(j > 0):
                    mem[i][j] = mem[i][j-1]
                elif(i > 0):
                    mem[i][j] = mem[i-1][j]

        return mem[m-1][n-1]


m = 3
n = 7
obj = Solution()
print(obj.uniquePaths(m, n))
