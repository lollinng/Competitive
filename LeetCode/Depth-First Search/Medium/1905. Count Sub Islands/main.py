"""
Logic - Since we have to find the sub islands present in g2 which also has land on g1 
as in g2 island land shouldnt be water in g1 for even in one cell
so we use dfs to find islands in g2 and check simultaneoulsy 
whether it has water in g1 if it does we return false 
"""


class Solution:
    def countSubIslands(self, grid1, grid2):
        ans = 0
        visited = set()
        h, w = len(grid1), len(grid1[0])

        def dfs(row, col):
            if(0 > row or 0 > col or row >= h or col >= w or grid2[row][col] == 0 or (row, col) in visited):
                return True

            visited.add((row, col))

            res = True
            # if there is water in place of land in grid2 then it not a subisland
            if(grid1[row][col] == 0):
                res = False

            res = dfs(row+1, col) and res
            res = dfs(row, col+1) and res
            res = dfs(row-1, col) and res
            res = dfs(row, col-1) and res
            return res

        for i in range(h):
            for j in range(w):
                if grid2[i][j] == 1 and ((i, j) not in visited) and dfs(i, j):
                    ans = ans + 1
        return ans


s = Solution()
print(s.countSubIslands(
    [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1]
    ],
    [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0]
    ]
))
