"""
Here we are trying to find the only on unique solution for a car to complete a circle using gas and cost arrays
We will be using greedy algorithm coz only one solution needed
1) we run a for loop from starting index to end in the array
2) we use total_surplus variable to check whether it has a solution if gas is less then cost we dont have a solution
3) we keep a surplus variable to check for starting point if it become negative at any point in interation which 
means the starting point is not to its left so we keep starting point at next iteration and resintialise surplus
variable to 0 to check validation of starting point hence forht

For Eg - 
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

iteration surplus  total_surplus start
0           0          -2          1
1           0          -4          2
2           0          -6          3
3           3          -3          3
4           6           0          3
hence we will start from 3

"""


class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        start = total_surplus = surplus = 0
        for i in range(n):
            surplus += gas[i]-cost[i]
            total_surplus += gas[i]-cost[i]
            # if surplus becomes negative means the path taken wasnt worth it
            # coz it resulted in negative fuel which is wrong
            if(surplus < 0):
                # surplus 0 to start our journey again but we know there is only
                # one unique solution so previous all indexes aren't start
                surplus = 0
                start = i+1
        # total surplus negative means no solution
        if(total_surplus < 0):
            return -1
        else:
            return start


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
obj = Solution()
print(obj.canCompleteCircuit(gas, cost))
