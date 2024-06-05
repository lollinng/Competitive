"""
Intuition:
We have to find the treasure 'zero' from all cells without accessing
going through water '-1' path
we have to find total distance of all 
1) We use dfs on the zeros 'treasure' present in the matrix
2) and iterate its neighboring  recursively in bfs manner with all 
zeros together
3) And we keep visit flask to avoid already visited or updated values
4) Hence each element will have smallest distance from treasure '0'

"""

class Solution:
    def islandsAndTreasure(self, grid):
        r,c = len(grid) , len(grid[0])
        visit = set()   # keeping a visiting set in bfs  
        queue = []
        def add_cel(i,j):

            # break statements
            if i>r-1 or j>c-1 or min(i,j)<0 or grid[i][j]==-1 or (i,j) in visit:
                return 
            
            # returning logic           
            visit.add((i,j))
            queue.append([i,j])

        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    queue.append([i,j])
                    visit.add((i,j))

        
        dist = 0
        # parsing in bfs
        while queue:
            for _ in range(len(queue)):
                i,j = queue.pop(0)
                grid[i][j] = dist # in the start distance will be zero or curent dist from '0'
                add_cel(i+1,j)
                add_cel(i,j+1)
                add_cel(i-1,j)
                add_cel(i,j-1)

            dist+=1
        return grid

"""
For eg:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

will have recursion as 

Element updated:  0
[2147483647, -1, 0, 2147483647]
[2147483647, 2147483647, 2147483647, -1]
[2147483647, -1, 2147483647, -1]
[0, -1, 2147483647, 2147483647]

Element updated:  0
[2147483647, -1, 0, 2147483647]
[2147483647, 2147483647, 2147483647, -1]
[2147483647, -1, 2147483647, -1]
[0, -1, 2147483647, 2147483647]

one iteration done
Element updated:  1
[2147483647, -1, 0, 2147483647]
[2147483647, 2147483647, 1, -1]
[2147483647, -1, 2147483647, -1]
[0, -1, 2147483647, 2147483647]

Element updated:  1
[2147483647, -1, 0, 1]
[2147483647, 2147483647, 1, -1]
[2147483647, -1, 2147483647, -1]
[0, -1, 2147483647, 2147483647]

Element updated:  1
[2147483647, -1, 0, 1]
[2147483647, 2147483647, 1, -1]
[1, -1, 2147483647, -1]
[0, -1, 2147483647, 2147483647]

one iteration done
Element updated:  2
[2147483647, -1, 0, 1]
[2147483647, 2147483647, 1, -1]
[1, -1, 2, -1]
[0, -1, 2147483647, 2147483647]

Element updated:  2
[2147483647, -1, 0, 1]
[2147483647, 2, 1, -1]
[1, -1, 2, -1]
[0, -1, 2147483647, 2147483647]

Element updated:  2
[2147483647, -1, 0, 1]
[2, 2, 1, -1]
[1, -1, 2, -1]
[0, -1, 2147483647, 2147483647]

one iteration done
Element updated:  3
[2147483647, -1, 0, 1]
[2, 2, 1, -1]
[1, -1, 2, -1]
[0, -1, 3, 2147483647]

Element updated:  3
[3, -1, 0, 1]
[2, 2, 1, -1]
[1, -1, 2, -1]
[0, -1, 3, 2147483647]

one iteration done
Element updated:  4
[3, -1, 0, 1]
[2, 2, 1, -1]
[1, -1, 2, -1]
[0, -1, 3, 4]

one iteration done
"""