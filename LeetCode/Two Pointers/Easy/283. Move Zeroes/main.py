"""
We intialise a zero index to take into consideration of left most zero . 
If the present number isnt zero we swap it with the leftmost zero index 
and add one to the zero index show that the zero number has one index towards right .
this works coz we swap as soon as we saw non zero element its mostly consective elements swapping postion for 1 zero
if 2 zero there we swapleftmost zero and the next zero becomes our zero_index
try to visualise it from visualise_code.txt in datastructure files 
if no zero present in the list zero_index = i which means they keeping swapping itslef
"""


class Solution:
    def moveZeroes(self, nums):
        zero_index = 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
        print(nums)


s = Solution()
s.moveZeroes([1, 1, 2, 3, 12])
