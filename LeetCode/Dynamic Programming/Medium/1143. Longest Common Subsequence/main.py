class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len = len(text1)
        text2_len = len(text2)
        dp = [[0 for _ in range(text2_len+1)] for _ in range(text1_len+1)]
        
        for row in range(1,text1_len+1):
            for col in range(1,text2_len+1):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = 1+dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row][col-1],dp[row-1][col])


        return dp[text1_len][text2_len]