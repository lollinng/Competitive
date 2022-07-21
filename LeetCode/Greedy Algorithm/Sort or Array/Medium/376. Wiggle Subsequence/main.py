"""
We are trying to solve a problem for finding maximum subsequnce representing wiggle patteen(big samll cons.)
Here We are trying to use gridy search because we only have to specify maximum number out of many subsequences

intitution - 
1) We will be taking each digit as points and represent the relationship as up-hill or down hill
2) pointer will increase only when uphill gets followed by downhill and vice versa
3) refer the photo attached

Solution-
1) we will be using 2 variables up and down , both intialised as 1 in intial state
2) we will be incrementing the variable depending upon the hill we reach across
3) to avoid incrementing on consecative uphill we increment the up variable with down + 1 hence only 1 is added 
out of all calculated downhills.
4) we calculate max of all up and down to get out required answer
"""


class Solution:
    def wiggleMaxLength(self, nums):
        up = 1
        down = 1
        n = len(nums)
        # print(nums)
        
        for i in range(1, n):
            # downhill
            if(nums[i] < nums[i-1]):
                down = up + 1
            #uphill
            elif(nums[i] > nums[i-1]):
                up = down+1
            # print(up,down,i)
        return max(down, up)


obj = Solution()
print(obj.wiggleMaxLength([3, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
