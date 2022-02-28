class Solution:
    def countGoodSubstrings(self, s):
        good = 0
        if len(s) < 2:
            return 0
        for r in range(2, len(s)):
            if s[r-2] != s[r-1] and s[r-1] != s[r] and s[r-2] != s[r]:
                good += 1

        return good
