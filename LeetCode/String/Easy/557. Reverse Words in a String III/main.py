"""
Steps to reverse words in a string
1) split the string of words into array of words
2) reverse each word personally
3) join them back
"""


class Solution:
    def reverseWords(self, s):
        s = s.split(" ")
        for i in range(len(s)):
            s[i] = s[i][::-1]
        s = " ".join(s)
        print(s)
        return s


obj = Solution()
obj.reverseWords("Hi Iam Prat")
