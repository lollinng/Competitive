"""
Here we trying to find the minimum jumps to reach the last index
We are using greedy algorithm using bfs concept to solve the problem
1) we will be using two ladders curr and big ladder one will store current ladder/jump value using the array values 
and the other will store ladder bigger than current
2) we select the bigger ladder when current ladder/jump reaches its course of value,hence we increment the jump
at each change of ladders
3) we keep iterating thorught the arrya keeping in mind of the current ladder and updating the biggest lader if we 
have to it and make it current ladder when current ladder ends
4) all the jumps are the ladder/jump/value changes in the array.

For Eg - [2,3,1,1,4,5]
intialisation : curr=0 big=0
index0: curr=2     jump=1 big=2
index1: curr=2     jump=1 big=4=3+1
index2  curr=big=4 jump=2 big=4
index3: curr=4     jump=2 big=4
index4: curr=big=8   jump=3 big=8
breaked from the loop coz curr>last index
"""


class Solution:
    def jump(self, nums):
        jump = 0
        currladder = 0
        bigladder = 0
        for i in range(len(nums)-1):
            bigladder = max(bigladder, i+nums[i])

            # if current ladder/element has reached its potential of carrying,then we switch ladder as in use jump
            if(currladder == i):
                currladder = bigladder
                jump += 1
                if(currladder >= len(nums) - 1):
                    break
        return jump


obj = Solution()
print(obj.jump([2, 3, 1, 1, 4, 5]))
