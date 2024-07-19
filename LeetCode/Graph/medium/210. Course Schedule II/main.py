from collections import deque


class Solution:
    
    def build_graph(self,numCourses,prerequisites):
        graph = [[] for _ in range(numCourses)]

        for dependent_course,independet_course in prerequisites:
            graph[independet_course].append(dependent_course)

        return graph


    def findOrder(self, numCourses, prerequisites):
        '''
        It seems like a directed graph problem , where prerequisites array is used to show 
        which graphs node directes to the other
        where we can use topo sort sort the DAG (directed acyclic graph)
        '''
        
        stack = deque()
        visited = [0]*numCourses
        graph = self.build_graph(numCourses,prerequisites)
 

        def dfs(vertex):

            if visited[vertex]==-1: # if vertex in path , hence its a cycle
                return False

            if visited[vertex]==1: # if vertex is differnt path , but visited
                return True

            visited[vertex] = -1        # adding vertex as current path

            for neighbor in graph[vertex]:
                if dfs(neighbor)==False:
                    return False
            
            visited[vertex] = 1        # remvoign vertex from current path
            stack.append(vertex)
            return True

            

        for vertex in range(numCourses):
            if visited[vertex]==0:
                if not dfs(vertex):
                    # if graph is cyclic 
                    return []

        return list(stack)[::-1]