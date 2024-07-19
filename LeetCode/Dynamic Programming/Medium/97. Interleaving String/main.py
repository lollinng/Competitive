class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        rows = len(s1)
        cols = len(s2)
        if rows+cols != len(s3):
            return False
        dp = [[False for _ in range(cols+1)] for _ in range(rows+1)]
        dp[0][0] = True

        '''
        we utilize a 2D array dp[i][j] to represent whether 
        the substring s3[:i+j] can be formed by interleaving s1[:i] and s2[:j].
        '''
        # in first column
        # its checking if previous is true
        # means if previous is a good string start
        # then if curent row_id/pointer matches with s3
        # return true
        # this is for rows which means the s1 string
        for row in range(1,rows+1):
            dp[row][0] = dp[row-1][0] and s1[row-1] == s3[row-1]

        # in fist row
        # since s2 doestnt start in s3 all will be false
        for col in range(1,cols+1):
            dp[0][col] = dp[0][col-1] and s2[col-1] == s3[col-1]

        # skipping first row , col
        for row in range(1,rows+1):
            for col in range(1,cols+1):
                # checking if new element in s1 , which means last element was in s2
                # which means we have to confirm one row above is True
                s1_check = dp[row-1][col] and s1[row-1] == s3[row+col-1] 

                s2_check = dp[row][col-1] and s2[col-1] == s3[row+col-1] 
                dp[row][col] = s1_check or s2_check

        return dp[rows][cols]
        