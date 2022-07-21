"""
Here the question ask us to find the minimum path from left top to right bottom using
down and right keys

since we have to find minimum path and there are many possibilities of it we use borrom up 
dynamic approch
1) we calculate the path value for every element and store it in the matrix itself
2) we use the stored value till that elemtnt to find value of path for next element
3) we keep iterating till we reach bottom right .
4) In case of middle elements we take minium of both the possiblities available to get there



question and first iteration - [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
[[1, 4, 1], [1, 5, 1], [4, 2, 1]]
[[1, 4, 5], [1, 5, 1], [4, 2, 1]]
[[1, 4, 5], [2, 5, 1], [4, 2, 1]]
[[1, 4, 5], [2, 7, 1], [4, 2, 1]]
[[1, 4, 5], [2, 7, 6], [4, 2, 1]]
[[1, 4, 5], [2, 7, 6], [6, 2, 1]]
[[1, 4, 5], [2, 7, 6], [6, 8, 1]]
[[1, 4, 5], [2, 7, 6], [6, 8, 7]]
7
"""


class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                # added so that middle element gets the least value
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                # j=0 elements
                elif i > 0:
                    grid[i][j] += grid[i-1][j]
                # i=0 elements
                elif j > 0:
                    grid[i][j] += grid[i][j-1]
                print(grid)
        return grid[m-1][n-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
s = Solution()
print(s.minPathSum(grid))
