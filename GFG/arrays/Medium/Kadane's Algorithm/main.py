
class Solution:

    def maxSubArraySum(self, arr, N):
        max_sum = arr[0]
        curr_sum = 0

        for i in range(0, N):
            curr_sum += arr[i]
            if max_sum < curr_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0

        return max_sum


obj = Solution()
print(obj.maxSubArraySum([1, 2, 3, -2, 5], 5))
