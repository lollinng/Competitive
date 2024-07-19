class Solution:
    def subsets(self, nums):
        
        nums_len = len(nums)
        subsets  = []

        def dfs(index,subset):

            # base statement
            if index==nums_len:
                subsets.append(subset)
                return

            # recursion
            dfs(index+1,subset)
            dfs(index+1,subset+[nums[index]])

        dfs(0,[])
        return subsets  

                

        