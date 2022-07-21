"""
Here we trying to see if we can reach the last digit of an array using digits jump inside it
We will be using greedy algorithm as we dont need the most optimal soltuion in this we just need a bool value4
We will be using max reachable variable to understand to check if the last index is reachable from the i th postion
1) use for loop from 0 to last index
2) reintialise max reachable if were able to go far from the index
3) keep itearting and updating the reachable 
4) if reachble equeal to or greater than last index return True else return False 
"""


class Solution:
    def canJump(self, nums):
        n = len(nums)
        reachable = i = 0

        while(i <= reachable and i < n-1):
            reachable = max(reachable, nums[i]+i)
            i += 1
            # print(reachable,i)
        return True if reachable >= n-1 else False


obj = Solution()
print(obj.canJump([2, 3, 1, 1, 4]))
