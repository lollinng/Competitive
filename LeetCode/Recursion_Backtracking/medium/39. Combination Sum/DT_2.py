class Solution:
    def combinationSum(self, candidates, target) :
        '''
        [2,3,5]
        unlimited combination
        ''' 

        res = []
        no_of_candidates = len(candidates)

        def dfs_on_array_elements(index,path,remaining):
            
            if remaining == 0:
                res.append(path)
                return 

            if remaining<0:
                return

            # recursion
            for i in range(index,no_of_candidates):
                ele = candidates[i]
                dfs_on_array_elements(i,path+[ele],remaining-ele)
            
        dfs_on_array_elements(0,[],target)
        return res
