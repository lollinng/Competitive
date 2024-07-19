from collections import deque


class Solution:
    
    def checkBipartite(self,queue,graph,color):
        while queue:
            vertex = queue.popleft()

            for new_vertex in graph[vertex]:
                if color[new_vertex] == -1:
                    color[new_vertex] = 1- color[vertex]  # flip the bit
                    queue.append(new_vertex)
                elif color[new_vertex]==color[vertex]:
                    return False
        return True

    def isBipartite(self, graph):
        
        if not graph:
            return graph

        no_vertices = len(graph)
        color = [-1]*no_vertices
        

        # raning over multiple disconnected components
        for start in range(no_vertices):
            if color[start] == -1:
                queue = deque([start])
                color[start] = 0
                if not self.checkBipartite(queue,graph,color):
                    return False
        
        return True
