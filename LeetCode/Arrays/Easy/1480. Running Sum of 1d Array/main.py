class Solution(object):
    def runningSum(self, nums):
        sum = 0
        for i in range(len(nums)):
            nums[i] += sum
            sum = nums[i]
        return nums


x = Solution()
print(x.runningSum([1, 2, 3, 4]))
