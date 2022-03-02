"""
Logic - since 1st house and last house cant be robbed together we need to use prev house robber forumula for 2 cases one without 1st house and
1 without last house

                                    nums = [1,2,3,1]
                        [2,3,1]                          [1,2,3]
                        [2,3,3]                          [1,2,4]
                            3                               4
                                         4
                        
"""


class Solution:

    # bottom up  memorisation
    def rob(self, nums):
        n = len(nums)
        if n < 3:
            return max(nums)

        dp1 = [0]*n
        dp2 = [0]*n
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        dp2[1] = nums[1]
        dp2[2] = max(nums[2], nums[1])
        for i in range(2, n):

            if(i == n-1):
                dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])
                continue

            if(i == 2):
                dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])

                continue

            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])

        return max(dp2[n-1], dp1[n-2])

    # without memorisation
    def rob1(self, nums):
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


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 3, 2]))
