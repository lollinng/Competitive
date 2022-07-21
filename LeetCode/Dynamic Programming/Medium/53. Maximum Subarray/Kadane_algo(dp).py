"""
Here we try to implement an algorithm as follows
1) we keep max value as 0th element
2) max_value of the present list either gets value of only next element or add the next element is added with
    previous max_value whichever is gretter 
    For Eg - if [1,2,5,-2] , here 5<5+3 there fore we keep 8 and now -2<8-2 so we max 6 and 8 to get max as 8
"""


class Solution:
    # kadanes algo
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
