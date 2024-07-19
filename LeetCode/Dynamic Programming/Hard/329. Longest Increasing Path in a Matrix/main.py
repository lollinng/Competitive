class Solution:
    def longestIncreasingPath(self, matrix):
        rows,cols = len(matrix),len(matrix[0])
        cache = {}
        
        iteration = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(row,col):
            
            if (row,col) in cache:
                return cache[(row,col)]

            path_len = 1
            for dx,dy in iteration:
                x,y = row+ dx,col+dy
                if x>=0 and y>=0 and y<cols and x<rows and matrix[row][col]<matrix[x][y]:
                    path_len = max(path_len,1+dfs(x,y)) 
            
            
            cache[(row,col)] = path_len
            # print(cache)
            return path_len
        
        res = 1 
        for row in range(rows):
            for col in range(cols):
                res=max(res,dfs(row,col)) 
        return res
        