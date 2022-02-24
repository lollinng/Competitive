class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue
        # print(self.rectangle)

        # for faster speed
        # temp = [newValue]*(col2-col1+1)
        # for i in range(row1, row2+1):
        #     self.rec[i][col1:col2+1] = temp

    def getValue(self, row: int, col: int) -> int:
        print(self.rectangle[row][col])


# Your SubrectangleQueries object will be instantiated and called as such:
obj = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
param_2 = obj.getValue(0, 2)
print(param_2)
obj.updateSubrectangle(0, 0, 3, 2, 5)
