"""
Steps to reverse strings in list-
1) Reverse last and first word
2) decrease and increase the right and left pointers respectively
"""


class Solution:
    def reverseString(self, s):
        l = 0
        r = len(s)-1
        while(l < r):
            s[r], s[l] = s[l], s[r]
            l += 1
            r -= 1
        print(s)


obj = Solution()
obj.reverseString(["h", "e", "l", "l", "o"])
