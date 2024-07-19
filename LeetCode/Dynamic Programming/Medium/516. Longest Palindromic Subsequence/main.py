class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        str_len = len(s)
        curr = [0]*(str_len+1) 
        prev = [0]*(str_len+1)

        
        rev_str = s[::-1]
        for row in range(1,str_len+1):
            for col in range(1,str_len+1):

                if s[row-1] == rev_str[col-1]:
                    curr[col] = 1 + prev[col-1]
                else:
                    curr[col] = max(prev[col],curr[col-1])

            prev = curr[:]
        return prev[str_len]
    

# not space optimized
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        str_len = len(s)
        dp = [[0]*(str_len+1) for _ in range(str_len+1) ]

        rev_str = s[::-1]
        for row in range(1,str_len+1):
            for col in range(1,str_len+1):

                if s[row-1] == rev_str[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col],dp[row][col-1])
        return dp[str_len][str_len]
'''