"""
Logic is to find the best possible loot at every iteration of the array
for the first element it is   - nums[0]
second element it is - max(nums[1],nums[0])
third element it is  - max(2 element,1stelement + 3rd element)
4 th element it is  -  max(3 element,2 element  + 4th element)

"""


class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        res = 0
        l = nums[0]
        # r = nums[1]
        res = r = max(nums[1], l)

        for i in range(2, len(nums)):

            res = max(l+nums[i], r)
            l = r
            r = res
        return res

    # with memorizition
    def rob1(self, nums):
        n = len(nums)
        dp = [0]*n

        if(n == 1):
            return nums[0]

        dp[0] = nums[0]

        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[n-1]


s = Solution()
print(s.rob1([2, 1, 1, 2]))
# ans - 4
