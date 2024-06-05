class Solution:
    def getMaximumGold(self, grid):
        """
        Intution:
        we will perform recursion on elements which dont have value as 0
        we will end when all the elements they viewing becomes zero
        we will have a mask to remembber the elements which are already visited
        
        """
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r,c,mask,res):
            
            if r>rows-1 or r<0 or c<0 or c>cols-1:
                return res
            if grid[r][c] == 0 or (r,c) in mask:
                return res

            
            res+= grid[r][c]

            # add mask element to avoid the index
            mask[(r,c)] = ''

            res = max([dfs(r-1,c,mask,res),dfs(r+1,c,mask,res),dfs(r,c+1,mask,res),dfs(r,c-1,mask,res)])
            
            # remove the mask element for backtracking
            del mask[(r,c)]
            return res
    



        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] !=0:
                    res = dfs(r,c,{},0)
                    ans = max(res,ans)
       
        return ans