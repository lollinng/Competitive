"""
Here we are trying to find triplets with sum as 0

Here we will be iterating over a array taking one element at a time
and running two sum 2 problem for finding if other 2 element pair with 
current i element

we sort the array for getting easy to use pointers (2sum 2 problem)

STEPS:
1) Iterate over array one element at a time
2) ccurrent goal (2 sum two): FIND 2 elements which add to 0 with iterating element
3) Use pointers l and r to find two elements optimally
4) If sum greater than 0 decrease r if smaller than increase r
5) iterte through same elemnts so same ans are not repeated
"""

class Solution:
    
    def twoSumPointer(self,nums,ele1,res):
        nums_len = len(nums)

        
        low,high = ele1+1,nums_len-1

        # this aint binary search just normal loop
        while low<high:
            mid = nums[ele1] +  nums[low] + nums[high]
            if mid<0:
                low+=1
            elif mid>0:
                high-=1
            else:
                res.append([nums[ele1],nums[low],nums[high]])
                high-=1
                low+=1
                # get rid of duplicates 
                while low<high and nums[low]==nums[low-1]:
                    low+=1 


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)

        # to avoid duplicate we can sort the array
        nums.sort()

        res = []
        for ele1_index in range(nums_len):
            
            # all element greeater then 0 cant make the sum as 0
            if nums[ele1_index]>0:
                break

            if ele1_index==0 or nums[ele1_index-1]!=nums[ele1_index]:
                self.twoSumPointer(nums,ele1_index,res)          
        return res
                

