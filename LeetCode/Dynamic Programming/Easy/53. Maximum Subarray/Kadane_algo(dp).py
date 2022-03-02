class Solution:
    # kasanes algo
    def maxSubArray(self, nums):
        max_sum = max_value = nums[0]
        for i in (nums[1:]):
            max_value = max(i, max_value+i)
            max_sum = max(max_sum, max_value)
            print(max_value, i)
        return max_sum

    # to keep track of the sums
    def maxSubArray1(self, nums):
        maxsum = 0
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
            maxsum = max(maxsum, nums[i])
        return maxsum


obj = Solution()
print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
