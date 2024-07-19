class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        i = 0
        n = len(needle)
        while i<len(haystack):
            if haystack[i]==needle[0]:
                if i+n<=len(haystack) and haystack[i:i+n] == needle:
                    return i
            i+=1
        
        return -1
