from collections import deque


class Solution:
    
    def __bfs(self,q,visited,adj):
        
        while q:
            vex,prev = q.popleft()
        
            if vex in visited:
                return True
        
            visited.add(vex)
            
            for adj_vex in adj[vex]:
                if prev != adj_vex:
                    q.append((adj_vex,vex))
                        
        return False
    
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
		#Code here
        visited = set()
        q = deque()
        
        for i in range(len(adj)):
            if i not in visited:
                q.append((i,-1))
                if self.__bfs(q,visited,adj):
                    return True
        return False
