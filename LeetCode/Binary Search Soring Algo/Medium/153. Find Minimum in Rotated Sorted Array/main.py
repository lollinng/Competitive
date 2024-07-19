class Solution:
    def findMin(self, nums):
        
        low = 0
        high = len(nums)-1

        if nums[0] < nums[-1]:
            return nums[0]

        while low<=high:
            mid = low + (high-low)//2

            # check if left element bigger
            if nums[mid] < nums[mid-1]:
                return nums[mid]

            # non sorted array to right hence go to right to find small element
            if nums[mid]>=nums[high]:
                low = mid+1
            # sorted array to right
            else:
                high = mid-1

        return nums[0]



