class Solution:

    def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        # c2 (course 2) is a prerequisite of c1 (course 1)
        # i.e c2c1 is a directed edge in the graph
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList

    def canFinish(self, numCourses: int, prerequisites):
        '''
        It seems like a directed graph problem , where prerequisites array is used to show 
        which graphs node directes to the other
        '''

        # Initialize graph adjacency list and visited list
    
        visited = [0 for _ in range(numCourses)]

        graph = self.buildAdjacencyList(numCourses, prerequisites)
        

        def hasCycle(x):
            
            # cycle
            if visited[x] == -1:
                return False
            # not a cycle since in different path
            if visited[x] == 1:
                return True
            
            # this shows visited and in path    
            visited[x] = -1
        
            for vertex in graph[x]:
                if hasCycle(vertex)==False:
                    return False

            # this represent visited but not in path
            visited[x] = 1  
            return True

        for i in range(numCourses):
            if visited[i]==0:
                if hasCycle(i) == False:
                    return False
        return True
