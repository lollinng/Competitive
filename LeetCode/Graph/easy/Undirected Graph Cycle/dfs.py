from collections import deque
class Solution:
    
    def __dfs(self,vex,prev,visited):
        if vex in visited:
            return True
    
        visited.add(vex)
        
        for adj_vex in adj[vex]:
            if prev != adj_vex:
                if self.__dfs(adj_vex,vex,visited):
                    return True
        return False
    
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj):
		#Code here
        visited = set()
    
        for i in range(len(adj)):
            if i not in visited:
                if self.__dfs(i,-1,visited):
                    return True
        return False
