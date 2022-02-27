class Solution:
    def countOdds(self, low, high):
        return (high+1) // 2 - low//2


s = Solution()
print(s.countOdds(5, 7))
