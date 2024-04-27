"""
In this We have to find quadruplets whose sum is equal to target
We hav to use 3SUM and 2SUM II knowledge in this problem

STEPS
1) Iterate through the first element while skipping consucative duplicates
2) Iterate through the second element while skippinf consecative duplicates
3) Perform 2SUM using left and right pointer trying to find double with sun equal to target
4) Use pointers l and r to find two elements optimally
5) If sum greater than 0 decrease r if smaller than increase r
6) iterte through same elemnts so same ans are not repeated

"""


class Solution:
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        
        # 4SUM problem
        for i,c in enumerate(nums[:-3]):
            if nums[i]==nums[i-1]and i>0:
                continue
            
            # 3SUM problem
            for j in range(i+1,len(nums)-2):
                if nums[j]==nums[j-1] and j>i+1:
                    continue
                
                # 2SUM II problem
                l = j+1
                r = len(nums)-1
                while(l<r):
                    s = c+nums[j]+nums[l]+nums[r]
                    if s>target:
                        r-=1
                    elif s<target:
                        l+=1
                    else:
                        res.append([c,nums[j],nums[l],nums[r]])
                        while(l<r and nums[l]==nums[l+1]):
                            l+=1
                        while(l<r and nums[r]==nums[r-1]):
                            r-=1
                        l+=1
                        r-=1    
        return res
                        
