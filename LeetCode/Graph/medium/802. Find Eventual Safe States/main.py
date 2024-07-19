class Solution:
    def eventualSafeNodes(self, graph):
        '''
        uses cycele detection in directed graph
        since only nodes connected to cycle or not in cycle are not safe nodes
        ''' 
        no_of_vertices = len(graph)
        visited = [0]*no_of_vertices
        check  = [False]*no_of_vertices

        def check_cycle(x):
            
            # currently in path hence element in cycle
            if visited[x] == -1:
                return False 

            # element already marked safe
            if visited[x] == 1:
                return True

            # make cycle visited saying its in current path
            visited[x] = -1

            for new_vertex in graph[x]:
                if check_cycle(new_vertex) == False:
                    return False

            
            # remove the visited x from current path
            # butt letting it know to be visited
            visited[x] = 1  # mark node as visited
            check[x] = True  # mark node as safe
            return True

        for vertex in range(no_of_vertices):
            if visited[vertex]==0:
                check_cycle(vertex)

        res = []
        for i in range(no_of_vertices):
            if check[i]==True:
                res.append(i)
        return res