from collections import defaultdict


class Solution:
    def getAncestors(self, n, edges):
        '''
        ele can have ancestors which are connected to them
        
        Intuition
        we can travse all the element from the first element 
        and mark the first ele to the children and keep appending
        the ancestor array

        {
            0 : [3,4],
            1: [3],
            2: [4,7],
            3: [5,6,7],
            4: [6]
        } 

        1) 0 -> 3 update ancestor of 3 as 0 -> 5 update ancestor 0 
                                            -> 6 update ancestor 0
        3) 0 -> 4 update ancestor of 4 as 0 


        4) 1 -> 3 update ancestor of 3 as 1 -> 5 update ancestor 1
                                            -> 6 update ancestor 1
                                            -> 7 update ancestor 1
        
        5) 2 -> 4 update ancestor of 2 -> 6 update ancestor of 2
        5) 2 -> 7 update ancestor of 2
            3 -> 5,6,7
            4 -> 6
        
        Solution : 
        time  O(V.E)
            1) Buidling adj_list takes O(E)
            2) DFS O(n*(n+E))
                i) Can traverl through all vertixes O(n)
                2) Can travel all edges O(E)
                3) inner loop is O(n+E)

        space : O(V^2+E)
            1) Adj list O(E)
            2) Result list O(V^2)
            3) Dfs Stack for every vertex O(V)

        '''

        adj_dict = defaultdict(list)
        for v1,v2 in edges:
            adj_dict[v1].append(v2)
        
        res = [[] for _ in range(n)]


        def dfs(ancestor,node):
            
            for child in adj_dict[node]:
                
                # making sure if we marked an vertext ancestor
                # we dont traverse it again
                if res[child] and res[child][-1] == ancestor:
                    continue

                # print(child,ancestor)
                res[child].append(ancestor)
                dfs(ancestor,child)

              
        for i in range(n):
            # print(res)
            dfs(i,i)

        return res

        
