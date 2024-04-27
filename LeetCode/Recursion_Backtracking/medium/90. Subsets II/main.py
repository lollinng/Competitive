"""
Here we are trying to find all the subsets of the list which have duplicate elemenets
Its an extension of the subset problem with duplicate elements
duplicate elements causes teh subsets to duplicate hence we will try to tackle that

Since the problem revolves around selecting and not selecting element for subset
we use backtracking to solve the problem
Upon drawing the decision tree You can see the pattern causing the duplication of
subarray hence we try to skip that node

We can skip that leaf node marked in dark blue by skipping the duplicate element/node
by iterting i if next element is duplicate and when we dont to select current element
hence skipping all the duplicates

Solution:
1) Sort the elements so that duplicate are stacked consecutively
2) Crete a recursive function taking index and temp array as params.
3) add breakin condition for out of bond and append the temp array to the result as
all all our answers are present in the leaf node and return for backtracking
4) 2 ways to solve problem
    i) Select current element/index      : by appending it to temp_array and running dfs 
    ii) Not select current element/index : by popping temp_array last element and skipping
    the next duplicate elements and running recursion on the remaining elements

"""


class Solution:
    def subsetsWithDup(self, nums):
        
        # since we want duplicates together
        nums.sort()
        res = []
  
        def dfs(i,curr_subarray):
            # breaking condition
            if i>=len(nums):
                res.append(curr_subarray[:])    
                return
       
            # if element is selected
            curr_subarray.append(nums[i])
            dfs(i+1,curr_subarray)
            curr_subarray.pop()

            # if elemeent is not selected
            # iterating till no duplicate in next element or the length ending 
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            # to run the dfs/recurssion on remaining elements in the tree
            dfs(i+1,curr_subarray)
            

        dfs(0,[])
        return res