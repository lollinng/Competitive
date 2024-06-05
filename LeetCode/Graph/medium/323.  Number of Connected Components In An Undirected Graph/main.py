class Solution:
    def countComponents(self, n: int, edges) -> int:
        adj = {i : [] for i in range(n)}
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)


        visit = set()
        def dfs(i,prev):
            
            # break
            if i in visit:
                return

            # logic
            visit.add(i)


            # recursion
            for j in adj[i]:
                if j==prev:
                    continue
                else:
                    dfs(j,i)


        res = 0
        for i in range(n):
            if i not in visit:
                res+=1
                dfs(i,-1)

        return res

