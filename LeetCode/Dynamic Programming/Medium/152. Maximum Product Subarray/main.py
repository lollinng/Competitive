"""
Here we are trying to find the largest product of subarray .

Intuition - 
1) if no negtive numbers the multplication of all array is max
2) if we encounter a negative number its multiplication with min of the subarray till then is max
For Eg - if max sum 10 meets -1 it becomes -10 but min sum -3 meets -1 it becomes 3 which is max possible for them
3) Now we iterate through the aarray keeping curr_max and min and store the overall result in res

Solution - 
1) we temp for keeping that iteration;s curr_max stored so we can use in curr_min.
for Eg - [-3, 2, -4, 6, 0, -8, -5] iterations - 
max ,min, res
1) -3 -3 -3
2) 2 -6 2     
3) 24 -8 24   
4) 144 -48 144
5) 0 0 144    
6) 0 -8 144
7) 40 -5 144
ans = 144

"""


class Solution:
    def maxProduct(self, nums):
        res = nums[0]
        curr_max = 1
        curr_min = 1
        for n in nums:
            temp = curr_max*n
            curr_max = max(n, curr_max*n, curr_min*n)
            curr_min = min(n, temp, curr_min*n)
            res = max(curr_max, res)
            print(curr_max, curr_min, res)
        return res


obj = Solution()
print(obj.maxProduct([-3, 2, -4, 6, 0, -8, -5]))
