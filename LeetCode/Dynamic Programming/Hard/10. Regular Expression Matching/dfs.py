class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len,p_len = len(s),len(p)
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            

            if i>=s_len and j>=p_len:
                return True
            # if s is reamining and j is over
            if j>= p_len:
                return False

            match = i<s_len and (s[i]==p[j] or p[j]=='.')
            if j+1<p_len and p[j+1]=='*':
                cache[(i,j)] = dfs(i,j+2) or (match and dfs(i+1,j))
                return cache[(i,j)] 

            if match:
                cache[(i,j)] = dfs(i+1,j+1)
                return cache[(i,j)]

            

        return dfs(0,0)