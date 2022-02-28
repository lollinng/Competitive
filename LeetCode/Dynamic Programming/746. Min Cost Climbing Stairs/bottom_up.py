"""
Logic - In bottom up approch we calculate the cost to get to a stair from start amd iterate our way thorugh the stars
taking minimum out of the 2 stairs
new stair(n)  = min(stair(n-1) , stair(n-2)) + stair(n)
and the answer for that stair will be 
min(stair(n-1),min(stair(n-2)+stair(n),stair(n-1)+stair(n))) 
    (last stair)  or (second last stair + present stair) or (last stair+present stair) 
"""


class Solution:
    def minCostClimbingStairs(self, cost):

        if not cost:
            return 0

        curr = 0
        dp0 = cost[0]
        dp1 = cost[1]

        for i in range(2, len(cost)):
            curr = min(dp0, dp1) + cost[i]
            dp0 = dp1
            dp1 = curr

        return min(dp0, dp1)


s = Solution()
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
