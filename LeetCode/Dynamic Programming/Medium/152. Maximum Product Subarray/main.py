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
        '''
        in largest product we keep count of negative values
        since negative multiplication can become poistive later
        hence we will store minimum product as well as max product
        we will return max product

        [2,3,-2,4,-6]

        min 2   2  -12  
        max 2   6   6

        possibilities
        1) curr_ele is negative , want max_product to multiple with it
        2) curr_ele is small , 
        3) curr_ele is big

        '''

        min_product = max_product = res =  nums[0]
        for num in nums[1:]:
            
            if num<0:
                min_product,max_product = max_product,min_product

            min_product = min(min_product*num,num)
            max_product = max(max_product*num,num)
            res = max(res,max_product)
        
        return res


obj = Solution()
print(obj.maxProduct([-3, 2, -4, 6, 0, -8, -5]))
