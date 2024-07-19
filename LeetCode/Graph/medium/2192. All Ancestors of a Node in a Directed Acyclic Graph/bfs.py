from collections import defaultdict, deque


class Solution:
    def getAncestors(self, n: int, edges):
        
        '''
        time complexity: O(n^3)
            1) Adj_list - O(E)
            2) BFS for each node = O(n*(V+E)) = O(n^3)
                i) outer n loop
                ii) innner for each node (V+E) loop
                iii) 𝐸≈𝑉2=𝑛^2 if graphs is densly populated
            
        space complexity: O(n^2+E)
            1)  Adj_list  : O(E)
            2)  res       : O(n^2)
            3)  BFS queue : O(n)

        '''

        adj_list = defaultdict(list)
        res = [[] for _ in range(n)]
        for v1,v2 in edges:
            adj_list[v1].append(v2)


        def bfs(ancestor):
            queue = deque([ancestor])
            while queue:
                vertex  = queue.pop()

                for child_node in adj_list[vertex]:

                    if res[child_node] and res[child_node][-1] == ancestor:
                        continue

                    res[child_node].append(ancestor)
                    queue.append(child_node)

        
        for i in range(n):
            bfs(i)
        return res