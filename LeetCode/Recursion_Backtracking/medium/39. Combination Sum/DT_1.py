"""
Here we are trying to solve find integers from array to achive target as total sum
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]



"""


class Solution:
    def combinationSum(self, candidate, target):
        
        res = []
        n = len(candidate)

        def dfs(start,temp):

            # break condition
            if start>=n or sum(temp)>=target:
                # add to solution if target acheived
                if sum(temp) == target:
                    res.append(temp[:])
                return

            # looping condition
            for i in range(start,len(candidate)):
                # appending/selecting current index to temp array for recursion
                temp.append(candidate[i])
                # performing recursion in current index branch
                dfs(i,temp)
                # popping to backtrack
                temp.pop()

        dfs(0,[])
        return res


