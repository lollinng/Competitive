"""
here we are told to find the max increasing sequence if u can delete or ignore any number of number in 
array
So to solve this problem since there can be many routes and we need to find maximum we use DP

Here we use bottom_up approach and save the value of max sequence formed for every element in the
dp array
1) we have 2 pointers 1 pointer to locate an element and other to go from 0 to that element 
2) if the element of left pointer is smaller than right we increase the value of right index in dp
3) only if the left pointer index is smaller than right pounter index val the value in r pointer is not
updated becoz of 

uneven increasing sequence : like 2 same elements or like below
[4,10,4,3,8]   here when right=8 pointer
1) at left = 0 dp['4'] = 1 and dp[right] = 1 which made dp[right] = 2
2) at left = 2 dp['4'] = 1 and dp[right] = 2 which nullifies are equeation and doesnt update pointer
3) at left = 3 dp['3'] = 1 and dp[right] = 2 again its doesnt get updated
saving us from making dp = 3 which is wrong in this case


normal example - [10, 9, 2, 5, 3, 7, 101, 18]
1) at left=2 and right=3 dp['2'] = 1 and dp['5'] =1 =>dp['5']=2
2) at left=2 and right=4 dp['2'] = 1 and dp['3'] =1 =>dp['3']=2
3) at left=2 and right=5 dp['2'] = 1 and dp['7'] =1 =>dp['7']=2
4) at left=3 and right=4 dp['5'] = 2 and dp['7'] =2 =>dp['7']=3
5) at left=3 and right=5 dp['3'] = 2 and dp['7'] =3 =>dp['7']=3 remains same coz of inregularity
.... so on
"""


class Solution:
    def lengthOfLIS(self, nums):
        Len = len(nums)
        if Len == 1:
            return 1
        dp = [1]*Len
        for right in range(1, Len):
            for left in range(right):
                if(nums[right] > nums[left] and dp[right] < dp[left]+1):
                    dp[right] += 1
            print(dp)

        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
obj = Solution()
print(obj.lengthOfLIS(nums))
