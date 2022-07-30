"""
In this question we were ask to decode a code which can have multiple ways to decode depening upon the ascci characters
26 can be decoded as 2 and 6 or 26 as well as - so there will be 2 ways in this example

1)We use bottom up approach to using 1d array keeping in mind of the value of ways in indexes of the dp array
2)we check if at a index , string char has single digit or double digit from past attached to it
3) if it does either of those we add the value of last index or second last index respectively to the dp array

eg - s = 226 will have 3 ways to decode , 2 26 or 22 6 or 2 2 6
iterations - 
1) [1, 1, 0, 0] 
2) [1, 1, 2, 0]
3) [1, 1, 2, 3]
here we can see it undestand 2 26 and 22 6 in 1st iteration
and 2 2 6 in 2nd iteration

"""


class Solution:
    def numDecodings(self, s):

        Len = len(s)

        # given as constraint any number followed by 0 at start is 0
        if s[0] == '0':
            return 0

        # creating a dp allowing first element at index 1 for being string index 0 so it gives 1 as ouput neverthless
        dp = [0 for x in range(Len+1)]
        dp[0:2] = [1, 1]
        print(dp)
        # len+1 coz we assigning number directly to dp index and and skipping 0th dp index
        for i in range(2, Len+1):

            # for taking signle digit number and allocating them last number value calculated
            if 0 < int(s[i-1:i]) <= 9:
                # can also be written as dp[i] += dp[i-1]
                dp[i] = dp[i-1]

            # Two step jump for getting those double digit number and adding dp the last to last times calculated value
            # most probably it will be 1 so 1+1 or 1+0 will be added .
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            print(dp)

        print(dp)

        return dp[-1]


s = "226"
obj = Solution()
print(obj.numDecodings(s))
