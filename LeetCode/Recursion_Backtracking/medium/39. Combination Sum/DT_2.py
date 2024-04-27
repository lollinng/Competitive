class Solution:
    def combinationSum(self, candidate, target):
        
        res = []
        n = len(candidate)

        def dfs(start,temp,total):
            
            # acheiving solution
            if total == target:
                res.append(temp[:])
                return

            # break condition
            if start>=n or total>target:
                return

            temp.append(candidate[start])
            # here we are adding the same index and giving choice to add the element once again
            dfs(start,temp,total+candidate[start])
            temp.pop()

            # going to next index without adding current elment
            dfs(start+1,temp,total)

        dfs(0,[],0)
        return res