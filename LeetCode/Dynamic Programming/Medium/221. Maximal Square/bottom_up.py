"""
In this example we have to calculate the max area of square made by 1s in matrix
We use bottom up approach where we mark 2 for an element if its covered by all 1s left right above diag
1) check for element with 1 matrix
2) if its covered by 1 in dp mark the bottom right 1 in dp array as 2 
3) if the element 1 in matrix is covered with 2s we will marks 3 in dp array

dp arrays intially all 0 and after they go through one row , the first row is buffer for indexing
[[0, 0, 0, 0, 0, 0],   [[0, 0, 0, 0, 0, 0],  [[0, 0, 0, 0, 0, 0]  [[0, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 0, 0],     [0, 1, 0, 1, 0, 0],  [0, 1, 0, 1, 0, 0],   [0, 1, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0],     [0, 1, 0, 1, 1, 1],  [0, 1, 0, 1, 1, 1],    [0, 1, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 0],     [0, 0, 0, 0, 0, 0],  [0, 1, 1, 1, 2, 2],    [0, 1, 1, 1, 2, 2],
[0, 0, 0, 0, 0, 0]]    [0, 0, 0, 0, 0, 0]]   [0, 0, 0, 0, 0, 0]]    [0, 1, 0, 0, 1, 0]]

"""


class Solution:
    def maximalSquare(self, matrix):
        m, n = len(matrix), len(matrix[0])

        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":

                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    max_side = max(max_side, dp[i+1][j+1])
            print(dp)
        return max_side**2


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
obj = Solution()
print(obj.maximalSquare(matrix))
