class Solution:
    def maxScore(self, grid) :
        """
        Intution
        n2 loop over every element
        check all possible values for right down for that element
        c1->ck = c2-c1 + c3-c2 + ck-c3 = ck-c1 hence points between source and destination is there difference

        At every point in dp array we will store the maxium value it can have as destination
        for example [0][0] will have iteself as valie
        [1][1] will have max([1][1] - [0][1],[1][1] - [1][0])  => min([0][1],[1][0])
        and we will store the min ()current element,or derived destination) for other elements to parse
        Here we are changing the matrix itself making it dp


        """
        n  = len(grid)
        m  = len(grid[0])
        res = -inf
        INF =  +inf

        for i in range(n):
            for j in range(m):

                if i==0:
                    prev_i =INF
                else:
                    prev_i = grid[i-1][j] 
                
                if j==0:
                    prev_j = INF
                else:
                    prev_j = grid[i][j-1]

                pre = min(prev_i,prev_j)
                res = max(res , grid[i][j]-pre)
                grid[i][j] = min(grid[i][j],pre)
                
            for i in range(n):
                print(grid[i][:])
            print()
       
        return res
