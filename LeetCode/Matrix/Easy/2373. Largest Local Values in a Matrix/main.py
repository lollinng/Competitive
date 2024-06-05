class Solution:
    def largestLocal(self, grid):
        n = len(grid)
        m = len(grid[0])

        ans = []
        for i in range(1,n-1):
            first = True
            res = []
            for j in range(1,m-1):
                
                if first:
                    i1,i2,i3 =  [arr[j-1:j+2] for arr in grid[i-1:i+2] ] 
                    first=False
                else:      
                    i1.pop(0)
                    i2.pop(0)
                    i3.pop(0)
                    i1.append(grid[i-1][j+1])
                    i2.append(grid[i][j+1])
                    i3.append(grid[i+1][j+1])

                i1_max = max(i1)
                i2_max = max(i2)
                i3_max = max(i3)
                res.append(max([i1_max,i2_max,i3_max]))
            
            ans.append(res)
        return ans