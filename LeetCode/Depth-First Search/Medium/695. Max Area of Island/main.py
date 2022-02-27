class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        max_area = 0
        self.h, self.w = len(grid), len(grid[0])
        for i in range(self.h):
            for j in range(self.w):
                if(grid[i][j] == 1):
                    max_area = max(max_area, self.dfs(grid, i, j, 0))

        return max_area

    def dfs(self, grid, i, j, area):

        if(i < 0 or j < 0 or i >= self.h or j >= self.w or grid[i][j] == 0):
            return area

        area += 1
        grid[i][j] = 0

        area = self.dfs(grid, i+1, j, area)
        area = self.dfs(grid, i-1, j, area)
        area = self.dfs(grid, i, j+1, area)
        area = self.dfs(grid, i, j-1, area)

        return area


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]
s = Solution()
print(s.maxAreaOfIsland(grid))
