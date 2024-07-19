#User function Template for python3
from collections import defaultdict,deque

class Solution:
    
    def buildGraph(self,alien_dict,N):
        adj_list = {c:set() for word in alien_dict for c in word}
        for i in range(1,N):
            w1 = alien_dict[i-1]
            w2 = alien_dict[i]
            min_len = min(len(w1),len(w2))

            for j in range(min_len):
                if  w1[j]!=w2[j] :
                    adj_list[w1[j]].add(w2[j])
                    break
        return adj_list
    
            
    def topsort(self,graph,K):        
        stack = deque()
        visited = {}
        
        def dfs(vertex):    
            if vertex in visited and visited[vertex] ==-1:
                return False
            if vertex in visited and visited[vertex]==1:
                return True
                
            visited[vertex]=-1
            for neighbour in graph[vertex]:
                
                if dfs(neighbour)==False:
                    return False
                    
            visited[vertex]=1
            stack.append(vertex)
            return True
            
        for vertex in list(graph):
            if vertex not in visited:
                if dfs(vertex) == False:
                    return []
                    
        return list(stack)[::-1]
    
    
    def findOrder(self,alien_dict, N, K):
        
        graph = self.buildGraph(alien_dict, N)
        sorted_dict = self.topsort(graph,K) 
        return sorted_dict
            
