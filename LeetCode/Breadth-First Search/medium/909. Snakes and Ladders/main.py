from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        '''

        queue 
            pop prev elemen

            range over (1,7)

                new_number  = number + 1
                calc row,col and verif it being -1

                it its not calculate its new desitnation

                if element is equal or greter then target return 
                if prev element not visited visit,
                    add elmenet to vissit
                    by appending the number value , and moves+1
        '''
        
        
        rows = len(board)
        cols = len(board[0])

        def label_to_position(label):
            quotient, remaineder = divmod(label-1, cols)
            row = rows - 1 - quotient
            # checking the direction is it left to right or right to left
            if quotient % 2 == 0:
                col = remaineder
            else:
                col = cols - 1 - remaineder
            return row, col

        target = rows*cols    
        queue = deque([(1,0)])
        visited = set()

        while queue:
            label, moves  = queue.popleft()
            for i in range(1,7):
                
                new_label = label + i
                if new_label > target:
                    break

                row,col = label_to_position(new_label)

                if board[row][col] != -1:
                    new_label = board[row][col]
                

                if new_label == target:
                    return moves+1
                
                if new_label not in visited:
                    visited.add(new_label)
                    queue.append((new_label,moves+1))


        return -1