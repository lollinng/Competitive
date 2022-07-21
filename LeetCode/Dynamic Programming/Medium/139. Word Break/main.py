"""
here we trying to see if all words in strings are present in dictionary
since multiple words can be arranged in any order so we are using dynamic 
programming's bottom up approach.

1) we will be creating an dp array with intialised false value
2) we will be marking true for words/index till from left to right index where word in word_dict
3) we will be checking if the left index has true in dp and left to right index are making another word in dict
then only we mark true in the dp array for catching another word


[True, False, False, False, False, False, False, False, False]
[True, False, False, False, False, False, False, False, False]
[True, False, False, False, False, False, False, False, False]
[True, False, False, False, False, False, False, False, False]
[True, False, False, False, True, False, False, False, False]  # here left=0 and right = 4 finding leet
[True, False, False, False, True, False, False, False, False]
[True, False, False, False, True, False, False, False, False]
[True, False, False, False, True, False, False, False, False]
[True, False, False, False, True, False, False, False, True]  
# here left=4 and right =8 finding code and making leetcode
"""


class Solution:
    def wordBreak(self, s, wordDict):
        Len = len(s)
        dp = [False]*(Len+1)
        dp[0] = True
        print(dp)
        for right in range(1, Len+1):
            for left in range(right):
                if dp[left] == True and s[left:right] in wordDict:
                    dp[right] = True
            print(dp)
        return dp[-1]


s = "leetcode"
wordDict = ["leet", "code"]

# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
obj = Solution()
print(obj.wordBreak(s, wordDict))
