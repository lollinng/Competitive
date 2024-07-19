class Solution:
    
    def checkValidity(self,row,col,board):
        board_value = board[row][col]

        for index in range(9):
            
            # check rows
            if col!=index:
                if board[row][index] == board_value:
                    return False

            # check columns
            if row!=index:
                if board[index][col] == board_value:
                    return False


            # Check inner 3x3 block
            block_row_start = (row // 3) * 3
            block_col_start = (col // 3) * 3
            inner_block_row = block_row_start + index // 3
            inner_block_col = block_col_start + index % 3

            if (inner_block_row, inner_block_col) != (row, col) and board[inner_block_row][inner_block_col] == board_value:
                return False

        return True




    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                board_value = board[row][col]
                if  board_value!= ".":
                    if not self.checkValidity(row,col,board):
                        return False

        return True