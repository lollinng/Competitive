class Solution:
    

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        rows_set = defaultdict(set)
        cols_set = defaultdict(set)
        squares_set = defaultdict(set)


        for row in range(rows):
            for col in range(cols):

                board_value = board[row][col]
                curr_square = (row//3,col//3)
                
                if  board_value== ".":
                    continue
                elif board[row][col] in rows_set[row] or board[row][col] in cols_set[col] or board[row][col] in squares_set[curr_square]:
                    return False
                else:
                    rows_set[row].add(board[row][col])
                    cols_set[col].add(board[row][col])
                    squares_set[curr_square].add(board[row][col])

        return True