class Solution:
    def pacificAtlantic(self, heights) :
        n = len(heights)
        m = len(heights[0])
        atl_matrx = pac_matrix = [[ False for _ in range(m)] for _ in range(n)]
        
        visit = set()
        def dfs(mat,i,j,prev):

            # break 
            if i<0 or j<0 or i>n-1 or j>m-1 or heights[i][j]<prev or (i,j) in visit or mat[i][j]==True :
                print('thrown',i,j,prev,visit)
                print(i<0 or j<0 or i>n-1 or j>m-1 or heights[i][j]<prev)
                # print(mat[i][j]==True)
                return  
            print(i,j,mat[i][j],visit)
            # logic
            print(mat,i,j)
            mat[i][j] = True
            print(mat)
            visit.add((i,j))

            # recusrion
            dfs(mat,i+1,j,heights[i][j])
            for u in range(n):
                print(atl_matrx[u])
            dfs(mat,i,j+1,heights[i][j])
            dfs(mat,i,j-1,heights[i][j])
            dfs(mat,i-1,j,heights[i][j])

            visit.remove((i,j))

            for i in range(n):
                print(atl_matrx[i])
        
        for i in range(n):
                print(atl_matrx[i])
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    print(i,j)
                    dfs(atl_matrx,i,j,0)
                    break
            break
        for i in range(n):
            print(atl_matrx[i])

obj = Solution()
obj.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])