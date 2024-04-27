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
    def threeSum(self, nums):
        res =  []
        nums.sort()
        for i,c in enumerate(nums[:-2]): 

            # previous element if same and index greater than 0 is skipped (or it takes last element if index -1)
            if c == nums[i-1] and i>0:    # this step makes sure that we do not have any duplicates in our result output
                continue 

            l = i+1
            r = len(nums)-1
            while(l<r):
                s = nums[l]+nums[r]+nums[i]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append([c,nums[l],nums[r]])
                    
                    # We trying to avoid duplicates hence iterating over them
                    while l < r and nums[l] == nums[l+1]: #  conditional for not calculating duplicates
                        l += 1
                    while l < r and nums[r] == nums[r-1]:  # Avoiding duplicates check
                        r -= 1
                    l += 1
                    r -= 1
                
        return res
