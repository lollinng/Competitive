class Solution:
    def finalValueAfterOperations(self, operations):
        ans = 0
        for x in operations:
            if x == "++X" or x == "X++":
                ans += 1
            else:
                ans -= 1
        return ans


s = Solution()
print(s.finalValueAfterOperations(["--X", "X++", "X++"]))
