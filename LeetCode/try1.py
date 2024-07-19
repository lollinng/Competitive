'''
m*n , 0 , 1 obs , (0,0) (m-1,n-1) 

minium number moves
right,down,up,left 

[
    0   0   0
    1   0   1
    0   1   0
]


f



(0,0) == 1 
return -1

'''
from collections import deque

def traverse(mat):
    
    
    rows = len(mat)
    cols = len(mat[0])

    if mat[0][0] == 1 or mat[rows-1][cols-1]==1:
        return -1



    iterator = [(0,1),(-1,0),(0,-1),(1,0)]
    
    queue = deque((0,0,0))
    visited = set((0,0))


    while queue:
        row,col,moves = queue.popleft()
        
        if (row,col) == (rows-1,cols-1):
            return moves


        for dx,dy in iterator:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and mat[new_row][new_col] == 0:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, moves + 1))

    return -1
a = [
    [0 , 0  , 0],
    [1  , 0  , 1],
    [0  , 0  , 0]
]

print(traverse(a))