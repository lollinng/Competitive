class Solution:
    def spiralOrder(self, matrix):
        '''

        taverse in right,down,left,up order


        1   2  3   4  
        5   6   7  8 
        9   10  11  12
        13  14  15  16

        index 0

        row = 0
        col = cols-1
        row = rows-1
        col = 0

        index 1
        row = 1
        col = cols-2
        row = rows-2
        col = 1 


        row = 3 and col is 3 is
        index 1  row =1 ,col=1,row=1 , col=1 , 

        row =3 col 4
        index1  row = 1,col=1,row=1,col=2
        hennce we can use for loop and iterate for max(row,col)-1
        '''
        rows,cols = len(matrix),len(matrix[0])

        rows_start,rows_end = 0,rows-1
        cols_start,cols_end = 0,cols-1
        res = []
        while(rows_start<=rows_end and cols_start<=cols_end):

            for col in range(cols_start,cols_end+1):
                res.append(matrix[rows_start][col])    
            rows_start+=1


            for row in range(rows_start,rows_end+1):
                res.append(matrix[row][cols_end])
            cols_end-=1


            for col in range(cols_end,cols_start-1,-1):
                res.append(matrix[rows_end][col])

            rows_end-=1
            
            for row in range(rows_end,rows_start-1,-1):
                res.append(matrix[row][cols_start])

            cols_start+=1
        
                       
        return res[:rows*cols]

