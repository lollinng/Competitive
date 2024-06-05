
'''

grid = [
  [1,0,2],
  [1,0,2]
]

'''

import json

def run(grid):
    temp = float('+inf')
    for j in range(len(grid[0])):
        if grid[0][j] == temp:
            return False
        temp  = grid[0][j]
        for i in range(len(grid)):
            if grid[i][j]!=temp:
                return False
    return True

grid = json.loads(input())
print(run(grid))