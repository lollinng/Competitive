class Solution:
    def pacificAtlantic(self, heights):
        n = len(heights)
        m = len(heights[0])
        atl_matrx =  [[ False for _ in range(m)] for _ in range(n)]
        pac_matrix =  [[ False for _ in range(m)] for _ in range(n)]
        
        visit = set()
        def dfs(mat,i,j,prev):

            # break 
            if i<0 or j<0 or i>n-1 or j>m-1 or heights[i][j]<prev or (i,j) in visit or mat[i][j]==True :
                return  

            # logic
            mat[i][j] = True
            visit.add((i,j))

            # recusrion
            dfs(mat,i+1,j,heights[i][j])
            dfs(mat,i,j+1,heights[i][j])
            dfs(mat,i,j-1,heights[i][j])
            dfs(mat,i-1,j,heights[i][j])

            visit.remove((i,j))
        
        # visiting those with  j=0 an j=m-1
        for i in range(n):
            dfs(atl_matrx,i,0,0)
            dfs(pac_matrix,i,m-1,0)
        
        # visiting those with i=0 an i=n-1 
        for j in range(m):
            dfs(atl_matrx,0,j,0)    
            dfs(pac_matrix,n-1,j,0)


        res = []
        for i in range(n):
            for j in range(m):
                if atl_matrx[i][j] == True and pac_matrix[i][j] == True:
                    res.append([i,j])
    
        return res