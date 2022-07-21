"""
Logic - In bottom up approch we calculate the cost to get to a stair from start amd iterate our way thorugh the 
stairs taking minimum out of the 2 stairs
new stair(n)  = min(stair(n-1) , stair(n-2)) + stair(n)
and the answer for that stair will be
min(dp0,dp1)
min(stair(n-1),min(stair(n-2)+stair(n),stair(n-1)+stair(n))) 
min( (last stair)  or (min(second last stair or last stair) + present stair) )


so for example - [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
here we take first 2 elements 100 and 1
the cost to reach the first 2 elements is the cost themselves
and try to find the cost for 3rd element which will be minimum of cost of 1 and 2 i.e cost(n-1) and cost(n-2) + 3rd elemtn
and now for 5 the element the cost will be min(cost(2),cost(3)) + value(5) = min(dp0, dp1) + cost[i]
and we go on till last element which will be min(cost(n-1),cost(n-2)) + value(n)

for the first element it is   - nums[0]
second element it is - nums[1]
third element it is  - min(1 element,2 element) + 3rd element
4 th element it is  -  min(3 element,2 element)  + 4th element


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
            # here we updating the current cost for the element to use for next element
            dp1 = curr
            # print(curr, dp0, dp1)
        return min(dp0, dp1)


s = Solution()
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
