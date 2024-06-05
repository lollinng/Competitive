class Solution:
    def matrixScore(self, grid):
        
        """
        Since we want get the largest binary digit out of every row
        row in example : 2^3 2^2 2^1 2^0
        1) we have to keep leftmost bit 1
        2) Hence out row toggling startegy will be to keep leftmost bit highest which has more value
        3) our column toggeling startegy we just check if we can have more ones 
        """

        rows = len(grid)
        cols = len(grid[0])
  
        # running toggling in rows if first element aint one
        for r in range(rows):
            # toggle to make it 1
            if grid[r][0] != 1:
                for c in range(cols):
                    grid[r][c] = 1 - grid[r][c]
        
        # running toggling on column if more ones then zero
        # since j=0 will have all ones
        for j in range(1,cols):
            col  = [grid[i][j] for i in range(rows)]
            # toggle
            if col.count(1)<col.count(0):
                for i in range(rows):
                    if grid[i][j]==1:
                        grid[i][j]=0
                    else:
                        grid[i][j]=1


        # caclualte res / binary values
        res = 0
        for i in range(rows):
            temp = grid[i]
            temp.reverse()
            for j in range(cols):
                res+= temp[j]*(2**j)

       
        return res

