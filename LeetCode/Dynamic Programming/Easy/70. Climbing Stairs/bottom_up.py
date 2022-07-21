'''
Here we are trying to find number of ways to reach the top of ladder taking 1 and 2 steps
we sart from 1 we have 2 possibilities take 1 step or 2

Intuition - 
1) Since it requiures number of ways which means all possible solution , we will use dynamic programming
2) We will be using bottom up approacha for this problem
3) Each steps is reached by last 2 steps so the ways to reach present step is addition of ways to reach last 2 
step 
4) we take intial 1=1 and 2=2 as both the index have 1 and 2 ways to reach the number of steps
5) we keep iterating and adding keep the count of number of ways for each step till we reach top

For Eg - 5 stairs
[0,1,2]
[0,1,2,3]         # the third step can be reached in 3 ways = 1+2
[0,1,2,3,5]
[0,1,2,3,5,8]       # 5 stairs can be reached in 8 ways      
'''


class Solution:
    def climbStairs(self, n: int):
        if(n == 1):
            return 1
        if(n == 2):
            return 2

        memo = [None]*(n+1)
        memo[1] = 1
        memo[2] = 2

        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]

        return memo[n]


s = Solution()
print(s.climbStairs(5))
