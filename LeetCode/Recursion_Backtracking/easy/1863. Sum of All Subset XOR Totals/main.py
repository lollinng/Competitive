class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        def dfs(i,xor_val):
            
            # logic
            if i==n:
                return xor_val                   
            return  dfs(i+1,xor_val^nums[i]) + dfs(i+1,xor_val)

        return dfs(0,0)
        