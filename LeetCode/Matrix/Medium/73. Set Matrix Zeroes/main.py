"""
here we are tryign to convert rows and columns of zero number in matrix to zero.

Solution -
1) we will create a temporary matrix to store real zero values
2) we will update the input matrix every time zero comes in temp , and run helper func
3) hlper func will update all rows and cols to zero in matrix
"""


class Solution:
    def setZeroes(self, matrix):

        temp = [row[:] for row in matrix]  # for copying matrix

        self.rows = len(matrix)
        self.cols = len(matrix[0])
        
        for i in range(self.rows):
            for j in range(self.cols):
                if temp[i][j] == 0:
                    self.helper(i,j,matrix)

        return matrix

    
    def helper(self,i,j,matrix):
        for col in range(self.cols):
            matrix[i][col] = 0
        for row in range(self.rows):
            # print(row,j)
            matrix[row][j] = 0

obj = Solution()




"""
 row = len(matrix)
col = len(matrix[0])
flag = [row[:] for row in matrix]
for i in range(row):
    for j in range(col):
        if flag[i][j] == 0:
            for c in range(col):
                matrix[i][c] = 0
            for r in range(row):
                matrix[r][j] = 0
"""