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


def traverse(mat):
    
    
    rows = len(mat)
    cols = len(mat[0])

    if mat[0][0] == 1 or mat[rows-1][cols-1]==1:
        return -1



    iterator = [(0,1),(-1,0),(0,-1),(1,0)]
    visited = {}

    def dfs(row,col):
        
        if (row,col) in visited:
            return visited[(row,col)]

        # success full condition
        if (row,col) == (rows-1,cols-1):
            return 0

        visited[(row,col)] = -1

        min_moves = float("inf")
        # recursion
        for dx,dy in iterator:
            x,y= row+dx,col+dy
            # boundary
            
            # print(x,y,row,col)
            if x>=0 and y>=0 and x<rows and y<cols and (x,y) not in visited and mat[x][y]==0:
                print('inside if',x,y,row,col,min_moves)
                min_moves = min(min_moves,1+dfs(x,y))
                print(min_moves,visited)

        visited[(row,col)] = min_moves
        return min_moves 


    res  = dfs(0,0)

    if (rows-2,cols-1) not in visited and (rows-1,cols-2) not in visited:
        return -1
    return res
    
    
a = [
    [0 , 0  , 0],
    [1  , 0  , 1],
    [0  , 0  , 0]
]

print(traverse(a))