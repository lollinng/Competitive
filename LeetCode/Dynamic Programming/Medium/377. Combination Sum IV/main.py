"""
intuition -
1) we use intuition that a n.o ways for one rupees sum is equal to addition of all ways of past no. of coing
present eg - here coins present were 3 therefore we only adding and iterating using those 3 to make new
values/target like 10 in this case.
2) We calculate of total ways of RS2 by 2 and 1 ways which is 2 ways
3) hence dp[Rs2] = dp[Rs2] + dp[2-1] + dp[2-2] + dp[2-3] but we dont want 2-3 hence we discard it using
if condition
here 

Solution -
1) first iteration
only num=1 is elgible and we it add dp[1-1] to dp[1] which will make dp[1]=1
2) second iteration
only num=1,2 is elgible and we it add dp[2-1] and dp[2-2] to dp[2] which will make dp[2]=dp[1]+dp[0]
3) third iteration
all num=1,2,3 are eligible and we add dp[3-1],dp[3-2],dp[3-3] which will make dp[3]=dp[0]+dp[1]+dp[2]
4) forth iteration
all num=1,2,3 are eligible and we add dp[4-1],dp[4-2],dp[4-3] which will make dp[3]=dp[1]+dp[2]+dp[3]
hence ans is dp[target] wher target is last iteration
5) view attach picture
"""


class Solution:
    def combinationSum4(self, nums, target):
        # bottom up approach
        dp = [0]*(target+1)
        dp[0] = 1

        for total in range(1, target+1):
            for num in nums:
                if(total-num >= 0):
                    dp[total] += dp[total-num]

        # print(dp)
        return dp[target]


obj = Solution()
print(obj.combinationSum4([1, 2, 3], 5))
