"""
Here we have to find a sequence whose sum is equal to target 
using infinte frequency of elements present in the cadidate array

Since its a probability of option in which we have to select if we want
to take each element or not we use recursion and backtracking
Recursion is used to check all possibilities
and backtracking navigates through all the states in space_tree
shown in the image

"""


class Solution:
    def combinationSum(self, candidate, target):
        res = []
        arr = []
        n = len(candidate)


        # DFS function for recursion
        def dfs(index,total,arr):

            # return if outofBonds
            if index>=n or total<0:
                return

            # condition satisfied
            if total == 0:
                res.append(arr.copy())
                return
            
            # select element
            arr.append(candidate[index])
            dfs(index,total-candidate[index],arr)
            
            # backtrack and dont select element
            arr.pop()
            dfs(index+1,total,arr)


        dfs(0,target,arr)
        return res

