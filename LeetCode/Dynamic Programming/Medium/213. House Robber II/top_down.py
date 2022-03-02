

class Solution(object):
    def rob(self, nums):
        def simple_rob(l, r):
            last, now = 0, 0
            while l < r:
                last, now, l = now, max(last + nums[l], now), l+1
            return now

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            n = len(nums)
            return max(simple_rob(1, n), simple_rob(0, n-1))
