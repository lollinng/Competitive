from cmath import inf


class Solution:
    def minFallingPathSum(self, grid) -> int:
        n = len(grid)

        dp = [[-1]*n for _ in range(n)]
        dp[0] = grid[0]
        
        def check_shortest_path(row,col):
            short = +inf
            for i in range(n):
                if short>dp[row-1][i] and i!=col:
                    short = dp[row-1][i]
            return short

        for row in range(1,n):
            for col in range(n):
                dp[row][col] = check_shortest_path(row,col) + grid[row][col]
        return min(dp[-1])      
    


if __name__ == "__main__":
    obj = Solution()
    print(obj.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
    print(obj.minFallingPathSum([[7]]))