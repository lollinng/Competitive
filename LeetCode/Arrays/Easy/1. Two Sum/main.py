"""
Making a dict to store the indices and number value and checking after each iteration whether current iterations number is in the dict

variables - 
nums,target - list input , target input
i - index of every iteration
num - number of every iteration
index_dict - dict created to store numbers
"""


class Solution:
    def twoSum(self, nums, target):
        dict_ = {}
        for i,ele in enumerate(nums):
            if ele in dict_:
                return ([dict_[ele],i])
            dict_[target - ele] = i


# For testing diff cases
# x = Solution()
# print(x.twoSum([2, 7, 11, 15], 9))
