class Solution:
    def deleteAndEarn(self, nums):

        # [1,1,1,2,4,5,5,5,6] -----> [0, 3, 2, 0, 4, 15, 6, 0, 0]
        points = [0]*len(nums)
        for num in nums:
            points[num] += num
        print(points)

        return self.rob(points)

    def rob(points):
        l = 0
        sum = 0

        for i in range(len(points)):
            sum = max(+points[i-2], points[i-1])


s = Solution()
print(s.deleteAndEarn([1, 1, 1, 2, 4, 5, 5, 5, 6]))

# [1,1,1,2,4,5,5,5,6]
# 18
