"""
Here we are trying to multiply each array elment with everyone leaving itslef

intuition =
1) to solve the problem in O(n) time we have to use 2 loops adjacent,
2) 1st loop will multiply all th elements to the left of an index to its value
3) 2nd loop will multiply all the elemnets to the right of an index to it's value
4) look at the img for reference

For eg - [2, 3, 4, 5]
                     *2  *2*3 *2*3*4
after 1st loop - [1,   2,   6,   24]
                 *3   *4  *5
after 2nd lop -  [60, 40, 30, 24]

"""


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*n
        # print(nums)
        temp = 1
        for i in range(1, n):
            temp *= nums[i-1]
            res[i] *= temp
        # print(res)
        temp = 1
        for j in range(n-2, -1, -1):
            temp *= nums[j+1]
            res[j] *= temp
        return res


obj = Solution()
print(obj.productExceptSelf([2, 3, 4, 5]))
