"""
Making a dict to store the indices and number value and checking after each iteration whether current iterations number is in the dict

variables - 
nums,target - list input , target input
i - index of every iteration
num - number of every iteration
index_dict - dict created to store numbers
"""


class Solution(object):
    def twoSum(self, nums, target):
        index_dict = {}

        for i, num in enumerate(nums):
            print(num)
            diff = target - num
            if diff in index_dict:
                return([index_dict[diff], i])
            index_dict[num] = i


# For testing diff cases
# x = Solution()
# print(x.twoSum([2, 7, 11, 15], 9))
