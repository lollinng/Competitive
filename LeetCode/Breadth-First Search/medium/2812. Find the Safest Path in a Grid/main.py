class Solution:
    
    """
    Intuition:
    1) here firstly we have to get distance of all elements from the ones
    2) And then find the path with highest minimum element / safest distance from the number 1
    3) Here we can use bfs for all 1st together in queue to store safe distance of each element
    4) then we can use djikstras algorithm with greedy approach to find highest minimum element by
       using max heap to find the largest element out of all posibilites to go to
    5) we store the lowest element of the path in max_heap hence preffering higher element  
    """

    def maximumSafenessFactor(self, grid):
        rows,cols = len(grid),len(grid[0])
        direction = [[0,1],[1,0],[-1,0],[0,-1]]

        # Initialize the BFS queue and visited set
        q = []
        visit = set()

        # Pre-compute BFS to calculate the safeness factor for each cell
        def pre_compute_bfs():
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        visit.add((r,c))
                        q.append((r,c))
                        
            count = 0
            while(q):
                for  _ in range(len(q)):
                    r,c = q.pop(0)
                    grid[r][c] = count
                    for dr , dc in direction:
                        nr,nc = dr+r,dc+c
                        if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit:
                            visit.add((nr,nc))
                            q.append((nr,nc))
                count+=1
        
        # gives us grid with safe value distances from 1 
        pre_compute_bfs()


        # Running greedy Djikstras algorithm using max_heap
        # Use a max-heap to find the path with the highest minimum safeness factor
        heap = []
        heapq.heappush(heap,(-grid[0][0],(0,0)))
        visit = set()
        visit.add((0,0))

        while(heap):
            dist,(r,c) = heapq.heappop(heap)
            dist = -dist  # Convert back to positive since we stored negative for max-heap
            if r==rows-1 and c==cols-1:
                return dist
            for dr , dc in direction:
                nr,nc = dr+r,dc+c
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    dist_min = min(dist,grid[nr][nc])
                    heapq.heappush(heap,(-dist_min,(nr,nc)))

        return -1