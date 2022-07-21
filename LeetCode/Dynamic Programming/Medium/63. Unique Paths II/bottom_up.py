"""
In this question we try to find the number of ways an Ai agent can go from top side of matrix to bottom right using down and right keys
We used bottom-up approach and caluclated the ways to go to a cell by adding the prrvious cells memory ways to it
by doing that we come with a colutino at the bottomost and righmost 2d matrix memoery showing alll the ways to reach it 

question = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
answers - 
[[1, 0, 0], [0, 0, 0], [0, 0, 0]]
[[1, 1, 0], [0, 0, 0], [0, 0, 0]]
[[1, 1, 1], [0, 0, 0], [0, 0, 0]]
[[1, 1, 1], [1, 0, 0], [0, 0, 0]]
[[1, 1, 1], [1, 0, 1], [0, 0, 0]]
[[1, 1, 1], [1, 0, 1], [1, 0, 0]]
[[1, 1, 1], [1, 0, 1], [1, 1, 0]]
[[1, 1, 1], [1, 0, 1], [1, 1, 2]]
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        # obstacleGrid[0][0] == 0 states that if not obstacle its true and 1 or if obstacle its 0
        dp[0][0] = int(obstacleGrid[0][0] == 0)

        for i in range(m):
            for j in range(n):

                # If it eccounters a block in the main problem we skip it in memrization
                if obstacleGrid[i][j] == 1:
                    continue

                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                # print(dp)
        return dp[m-1][n-1]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
# ans - 2
