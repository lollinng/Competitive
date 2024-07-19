from typing import List

class Solution:
    def solveNQueens(self, n: int):
        """
        Solve the N-Queens problem, where we need to place queens on an nxn chessboard
        such that no two queens threaten each other.

        Parameters:
        - n (int): Size of the chessboard and number of queens to place.

        Returns:
        - List[List[str]]: List of all distinct solutions where queens are placed such that no two queens threaten each other.
                           Each solution is represented as a list of strings, where each string represents a row on the chessboard.
                           'Q' denotes a queen, and '.' denotes an empty cell.

        Approach:
        - Use backtracking to recursively explore all possible placements of queens.
        - Maintain sets to track columns and diagonals that are threatened by queens already placed.

        Complexity:
        - Time Complexity: O(N!), where N is the size of the chessboard (number of queens).
        - Space Complexity: O(N^2), for the board and auxiliary data structures.
        """

        # Initialize the chessboard with empty cells '.'
        board = [['.'] * n for _ in range(n)]
        solutions = []

        # Sets to track threatened columns and diagonals
        threatened_columns = set()
        threatened_diagonals = set()
        threatened_antidiagonals = set()

        def backtrack(row: int) -> None:
            """
            Backtracking function to recursively explore queen placements.

            Parameters:
            - row (int): Current row being explored for queen placement.
            """
            # Base case: All queens placed, add current board configuration to solutions
            if row == n:
                solutions.append([''.join(row) for row in board])
                return

            for col in range(n):
                diag_sum = row + col
                diag_diff = row - col

                # Check if current column or diagonals are threatened
                if col in threatened_columns or diag_diff in threatened_diagonals or diag_sum in threatened_antidiagonals:
                    continue

                # Place queen and mark threatened columns and diagonals
                board[row][col] = 'Q'
                threatened_columns.add(col)
                threatened_diagonals.add(diag_diff)
                threatened_antidiagonals.add(diag_sum)

                # Recursively place queens in the next row
                backtrack(row + 1)

                # Backtrack: Remove queen and mark as unthreatened
                board[row][col] = '.'
                threatened_columns.remove(col)
                threatened_diagonals.remove(diag_diff)
                threatened_antidiagonals.remove(diag_sum)

        # Start backtracking from the first row
        backtrack(0)

        return solutions