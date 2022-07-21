"""
Here we trying to see if we can reach the last digit of an array using digits jump inside it
We will be using greedy algorithm as we dont need the most optimal soltuion in this we just need a bool value
In this example we will be having a goal state
1) a goal state is set at last index of the array
2) we iterate through the second last index to 0 th index using for loop
3) if the goal state is reachable(i+nums[i]) from the i th index we reintialise the goal state to that index
4) keep iterating if goal state doesnt become 0 means we cant reach the goal state from 0 th index
"""


class Solution:
    def canJump(self, nums):
        goal = len(nums)-1

        for i in range(goal-1, -1, -1):
            if(i+nums[i] >= goal):
                goal = i

        return True if goal == 0 else False


obj = Solution()
print(obj.canJump([2, 3, 1, 1, 4]))
