class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_t = len(t)
        len_s = len(s)
    
        if len(t)>len(s):
            return 0

        # creatin dp with buffer row as 1
        # since we will iterating down and using it to add 1
        dp = [[0] * (len_s+1) for _ in range(len_t+1)]
        dp[0] = [1]*(len_s+1)


        for t_index in range(1,len_t+1):
            for s_index in range(1,len_s+1):
                dp[t_index][s_index] += dp[t_index][s_index-1] 

                # if elements are equal
                if s[s_index-1] == t[t_index-1]:
                    dp[t_index][s_index] += dp[t_index-1][s_index-1] 
        
        return dp[-1][-1]
