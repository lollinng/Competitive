class Solution:
    def closedIsland(self, grid):
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        invalid_island = False
        Land = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isValidCell(i, j):
            if 0 <= i < rows and 0 <= j < cols:
                return True
            return False

        def InEdge(i, j):
            if (i == 0 or j == 0 or j == cols-1 or i == rows-1):
                return True
            return False

        def dfs(i, j):
            # print("inside", i, j)
            nonlocal visited, invalid_island
            if not invalid_island and InEdge(i, j):
                invalid_island = True
                return

            visited.add((i, j))

            for dx, dy in dirs:
                if isValidCell(i+dx, j+dy) and (i+dx, j+dy) not in visited and grid[i+dx][j+dy] == Land:
                    dfs(i+dx, j+dy)

        for i in range(rows):
            for j in range(cols):
                invalid_island = False
                if grid[i][j] == Land and (i, j) not in visited:
                    dfs(i, j)
                    islands += (0 if invalid_island else 1)

        return islands


#             1
"""
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
"""


s = Solution()
print(
    s.closedIsland(
        [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]
        ]
    )
)
