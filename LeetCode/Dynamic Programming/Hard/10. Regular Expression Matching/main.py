class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len,p_len = len(s),len(p)
        dp = [[False]* (p_len+1) for _ in range(s_len+1)]
        dp[0][0] = True


        # Handle patterns with '*' at the start
        # correcting a base case for "a*" , 
        for col in range(1, p_len + 1):
            if p[col - 1] == '*':
                dp[0][col] = dp[0][col - 2]


        for row in range(1,s_len+1):
            for col in range(1,p_len+1):
                
                # check previous path
                if s[row-1]==p[col-1] or p[col-1]=='.':
                    dp[row][col] = dp[row-1][col-1]
                
                
                elif p[col-1] == '*':
                    
                    # zero occurance skipping prev element
                    dp[row][col] = dp[row][col-2]

                    # consedering prev element
                    if p[col-2]=='.' or s[row-1]==p[col-2]:
                        # here we are using row-1 to check if above element's path 

                        dp[row][col] = dp[row][col] or dp[row-1][col]
                    
                # else let it remain False
            
        return dp[-1][-1]