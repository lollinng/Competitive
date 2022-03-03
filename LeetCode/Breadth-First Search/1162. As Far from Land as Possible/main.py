class Solution:
    def maxDistance(self, grid):
        h, w = len(grid), len(grid[0])
        x = [-1, 0, 1, 0]
        y = [0, 1, 0, -1]

        q = []

        # we first add land to our queue
        for i in range(h):
            for j in range(w):
                if(grid[i][j] == 1):
                    q.append((i, j))

        # if matrix has no water then ans =-1
        if(len(q) == h*w):
            return -1

        dist = 0

        while(True):
            size = len(q)
            if(size == 0):
                break
            dist = dist+1
            while(True):
                if(size == 0):
                    break
                print(q, dist)
                size -= 1
                si, sj = q.pop(0)
                for i in range(4):
                    newi = si + x[i]
                    newj = sj + y[i]
                    if(newi >= 0 and newi < h and newj >= 0 and newj < w and grid[newi][newj] == 0):
                        q.append((newi, newj))
                        grid[newi][newj] = 1

        return dist-1


s = Solution()
print(s.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
print("hello")

"""
ans-  0         1        2
dist  1         2        3
    1 0 1     1 1 1    1 1 1
    0 0 0 =>  1 0 1 => 1 1 1
    1 0 1     1 1 1    1 1 1

1st loop
[(0, 0), (0, 2), (2, 0), (2, 2)]
[(0, 0), (0, 2), (2, 0), (2, 2)] 1         
[(0, 2), (2, 0), (2, 2), (0, 1), (1, 0)] 1 
[(2, 0), (2, 2), (0, 1), (1, 0), (1, 2)] 1 
[(2, 2), (0, 1), (1, 0), (1, 2), (2, 1)] 1 
[(2, 2), (0, 1), (1, 0), (1, 2), (2, 1)] 2 

2nd loop
[(0, 1), (1, 0), (1, 2), (2, 1)] 2      - last element(water is counted and earased)    
[(1, 0), (1, 2), (2, 1), (1, 1)] 2         
[(1, 2), (2, 1), (1, 1)] 2 
[(2, 1), (1, 1)] 2  

"""
