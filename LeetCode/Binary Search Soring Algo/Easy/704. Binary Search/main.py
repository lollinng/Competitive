"""
Binary Search -  we recursively divide the array in half to find the element 
"""


class Solution:
    def search(self, nums, target):
        # print(nums,target)
        low = 0
        high = len(nums)-1
        while(low <= high):
            mid = low + (high-low+1)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1               # mid is excluded
            else:
                low = mid + 1                   # mid is included
            # print(high, low, mid)
        return -1
        return mid # if we want to return where element can be pushed in array


x = Solution()
print(x.search([-1, 0, 3, 5, 9, 12], 9))
