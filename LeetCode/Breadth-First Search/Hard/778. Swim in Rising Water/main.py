class Solution:
    '''
    Intuition:

    We take elements in grid as height
    and our goal will to go through path with minimum max element
    so that less time is required for swimming

    here we will use Djikstras algorithm with a greedy approach
    

    we will start with 0,0 and update the next elements in minHeap

    we will pop the min_heap and go to the direction of the lowest
    element since we have infinite speed distance doesnt matter
    only max element we encounter matters

    We will use bfs from 0,0 add other adjacent elements to minheap
    then do bfs on the recently popped heap*(lowest adjacent elemtnet) of other elements

    we will check if its e bottom right square if not then run bfs on it adding its adjancent element
    
    one thing we take care is throughout the path we store maximum value as an the sort key in minheap
    hence the elements with lowest path maximum will be popped first then other loawest path maximum
    this will make sure we get the greeddy optimal solution


    '''
    
    
    def swimInWater(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        heap = []   
        visit = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        # we adding the (height,(r,c)) in heap to sort it with height
        def bfs(r,c,time):
            for dr,dc in directions:
                nr , nc = r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit:
                    
                    visit.add((nr,nc))
                    max_time = max(time,grid[nr][nc]) # highest time till now
                    heapq.heappush(heap,(max_time,(nr,nc)))
        


        
    
        heapq.heappush(heap,(grid[0][0],(0,0))) #(time/max-height,r,c)
        visit.add((0,0))
        while(heap):
            time ,(r,c) = heapq.heappop(heap)

            if r== rows-1 and c == cols-1:
                return time 
            bfs(r,c,time)
        return -1
         