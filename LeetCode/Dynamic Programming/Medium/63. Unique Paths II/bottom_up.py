from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        rows,cols = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        dp[0][0] = 1

        # get ways for upper row
        for col in range(1,cols):
            if obstacleGrid[0][col] != 1:
                dp[0][col] = dp[0][col-1]

        # get ways for left col
        for row in range(1,rows):
            if obstacleGrid[row][0] != 1:
                dp[row][0] = dp[row-1][0]

        for row in range(1,rows):
            for col in range(1,cols):
                if obstacleGrid[row][col] != 1:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1] 
                    
        return dp[-1][-1]