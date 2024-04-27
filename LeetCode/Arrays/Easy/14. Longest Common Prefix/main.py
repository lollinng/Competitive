"""

344,557,1281,2114,


Here we have to find longest string from  the start

We Sort the array so that we get two most dissimillar strings as 
first and last and compare them for common string

Before : ["flower","flow","flight"]
After  : ["flight","flow","flower"]

Hencer we only compare index 0 and -1 and common chars to res string
to get our final output
"""


class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        strs.sort()

        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                res += strs[0][i]
            else:
                break
        return 
    


"""
Simple Costlier method

iterate through the strings and check if the index is common with 
index 0 if not or index over return answer
"""
class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res