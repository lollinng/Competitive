class Solution:
    def closedIsland(self, grid):
        islands = 0
        self.w, self.h = len(grid), len(grid[0])
        for i in range(self.w):
            for j in range(self.h):
                if grid[i][j] == 0 and self.dfs(grid, i, j) == True:
                    # print(i, j)
                    islands += 1
                    # for k in range(self.w):
                    #     print(grid[k])
                    # print()
        return islands

    def dfs(self, grid, i, j):

        if grid[i][j] == 'F':
            return False

        # print("inside", i, j)

        if (i == 0 or j == 0 or i == self.w-1 or j == self.h-1) and grid[i][j] == 0:
            grid[i][j] = 'F'
            return False

        if i < 0 or j < 0 or i >= self.w or j >= self.h or grid[i][j] == "T":
            return True

        if(grid[i][j] == 1):
            return True

        grid[i][j] = "T"
        # return (
        #     self.dfs(grid, i+1, j) and self.dfs(grid, i-1, j)
        #     and self.dfs(grid, i, j-1) and self.dfs(grid, i, j+1)
        # )

        if(self.dfs(grid, i+1, j) and self.dfs(grid, i-1, j) and self.dfs(grid, i, j-1) and self.dfs(grid, i, j+1)) == True:
            grid[i][j] = "T"
            return (True)
        else:
            grid[i][j] = "F"
            return False


#             1
"""
[0,0,1,1,0,1,0,0,1,0],
[1,1,5,1,1,0,1,1,1,0],
[1,5,1,1,1,0,0,1,1,0],
[0,1,1,0,0,0,0,1,5,1],
[0,0,0,0,0,0,1,1,1,0],
[0,1,0,1,0,1,0,1,1,1],
[1,5,1,5,1,1,0,0,0,1],
[1,1,1,1,1,1,0,0,0,0],
[1,1,1,0,0,1,0,1,0,1],
[1,1,1,0,1,1,0,1,1,0]
"""


s = Solution()
print(
    s.closedIsland(
        [
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        ]
    )
)
