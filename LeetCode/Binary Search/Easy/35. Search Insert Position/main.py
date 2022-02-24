class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1
        while(low <= high):
            mid = low + (high-low+1)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = high - 1
        return low+1


# for testing
x = Solution()
print(x.searchInsert([1, 3, 5, 6], 5))
