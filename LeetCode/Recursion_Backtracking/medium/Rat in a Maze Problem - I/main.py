class Solution:
    def findPath(self, m, n):
        # code here
        res = []
        visited = set()
        path_list = [(1,0,'D'),(0,1,'R'),(0,-1,'L'),(-1,0,'U')]
        def dfs(row,col,path):
        
            # breaking condition
            if row>=n or col >=n or col<0 or row<0 or m[row][col]==0 or (row,col) in visited:
                return
            
            # add to  visited
            visited.add((row,col))
            
            if row==n-1 and col==n-1:
                res.append(path)
                # before return we have to remove the visited elements for other paths
                visited.remove((row,col)) 
                return 
            
            for dx,dy,pt in path_list :
                dfs(dx+row,dy+col,path+pt)
                
            visited.remove((row,col))
    
        
        dfs(0,0,"")
        return res