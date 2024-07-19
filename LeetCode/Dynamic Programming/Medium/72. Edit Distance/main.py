class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)
        dp = [[0]* (word1_len+1) for _ in range(word2_len+1)]
        # print(dp)
  
        for col in range(word1_len+1):
            dp[0][col] = col
        for row in range(word2_len+1):
            dp[row][0] = row


        for row in range(1,word2_len+1):
            for col in range(1,word1_len+1):
                
                # performing a single operation
                if word1[col-1] == word2[row-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] += 1 + min(
                        dp[row-1][col],   # deletion
                        dp[row][col-1],   # insertion
                        dp[row-1][col-1]  # substitution
                    )
        return dp[-1][-1]