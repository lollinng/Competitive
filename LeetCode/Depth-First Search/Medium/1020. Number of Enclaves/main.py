"""
Logic - So as we dont want edge lands(1) and the land connected to edges(coz we can walk through it to edge) we will use dfs on all the
first, last element of row and column to add them to visited
And then we will see for the reamaining 1's and increase the counter as per number of ones remaining without using dfs. 
"""


class Solution:
    def numEnclaves(self, A):
        row, col = len(A), len(A[0])
        visited = set()

        if not A or not A[0]:
            return 0

        # dfs will only get called for findin binary connected elements
        def dfs(x, y, A):
            if 0 <= x < row and 0 <= y < col and A[x][y] == 1 and (x, y) not in visited:
                visited.add((x, y))
                dfs(x+1, y, A)
                dfs(x-1, y, A)
                dfs(x, y+1, A)
                dfs(x, y-1, A)

        # we visit every elements in leftmost and rightmost columns and iterate through the dfs to other 1s connected to it
        # and mark them as connected so that we dont visit them later while using the counter to get ans
        for x in range(row):
            dfs(x, 0, A)
            dfs(x, col-1, A)

        # we visit every elements in leftmost and rightmost row and iterate through the dfs to other 1s and mark them visited
        for y in range(1, col-1):
            dfs(0, y, A)
            dfs(row-1, y, A)

        count = 0
        for x in range(row):
            for y in range(col):
                # not calling bfs here
                if A[x][y] == 1 and (x, y) not in visited:
                    count += 1
        return count


s = Solution()
print(s.numEnclaves([
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]))
