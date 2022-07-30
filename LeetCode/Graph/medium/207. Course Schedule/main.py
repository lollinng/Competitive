"""
Here we are trying to see if we can finish all the nodes/courses which is only possible we dont come in contact with 
a loop while we iterta through each subjects prerequisites using dfs

Intuition - 
1) use 2d graph 1d for node index and the second D for its prereuisite
2) use visit , -1 for visited and 1 for validated that node doesnt leads to loop 

Solution - 
1) add prerequisites and nodes no. in graph
2) run dfs algo for every node in graph and later run dfs in dfs for its prerequisites
3) return -1 , if it encounters the same node again
4) return 1 , if it doesn leads to loop again
"""


class Solution:
    def canFinish(self, numCourse, prerequisites):

        graph = [[] for _ in range(numCourse)]
        visit = [0 for _ in range(numCourse)]

        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(x):
            # print(x)
            # print(visit)
            if visit[x] == -1:
                return False
            if visit[x] == 1:
                return True

            visit[x] = -1

            # running dfs on its child nodes/prerequisites
            for j in graph[x]:
                # if loop or -1 return , return false to parent
                if dfs(j) == False:
                    return False

            # if no loop or false return true
            visit[x] = 1
            return True

        for j in range(len(graph)):
            if dfs(j) == False:
                return False
        return True


obj = Solution()
print(obj.canFinish(2, [[1, 0], [0, 1]]))
