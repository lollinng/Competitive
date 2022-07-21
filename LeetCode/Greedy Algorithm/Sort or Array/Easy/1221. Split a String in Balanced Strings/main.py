class Solution:
    def balancedStringSplit(self, s):
        count = ans = 0
        for i in s:
            if(i == "R"):
                count += 1
            else:
                count -= 1
            if(count == 0):
                ans += 1
        return ans


obj = Solution()
print(obj.balancedStringSplit("RLRRLLRLRL"))
