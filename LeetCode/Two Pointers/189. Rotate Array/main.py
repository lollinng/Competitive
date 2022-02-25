

class Solution:

    def inverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start = start + 1
            end = end-1

    # O(n) time complexity loop used in inverse
    def rotate(self, nums, k):
        # % remainder, to avoid doing a 360 circle
        k = k % len(nums)
        self.inverse(nums, 0, len(nums)-1)
        self.inverse(nums, 0, k-1)
        self.inverse(nums, k, len(nums)-1)
        print(nums)

    # this method has time complexity o(n2) so it takes too much time for big arrays
    def rotate1(self, nums, k) -> None:
        for _ in range(k):
            replaced_element = nums[-1]
            for i in range(len(nums)):
                temp = nums[i]
                nums[i] = replaced_element
                replaced_element = temp


x = Solution()
x.rotate([1, 2, 3, 4, 5, 6, 7], 3)
