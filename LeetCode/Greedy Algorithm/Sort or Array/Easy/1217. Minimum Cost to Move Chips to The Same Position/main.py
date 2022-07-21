"""
Here we are trying to find the cost required to move all coins to one index. We know moving coin
to consecative postions takes one cost and moving two places further takes 0 cost

Intituion-
1) We bring all the coins to either 1 or 2 index by using 2 places method for simplicity
2) All even coins get to 2 and all odd gets to 0 that we think without implimenting
3) we find whether even number are greater or odd number which will help us understand what will be
greater coins at 1 or 2
4) so which will be minimum it will moved to consecative in 1 and 2 . Hence the cost will be min.
1 of 2 i.e minimum of odd numbers and even numbers


Eg - Essentially, we're counting how many odd numbers and even numbers there are and returning the smaller count.
chips = [1,2,3]. 2 odd numbers and 1 even number. Return 1.
chips = [2,2,2,3,3]. 2 odd numbers and 3 even numbers. Return 2.
chips = [1,3,5,7,9,11,2,4]. 6 odd numbers and 2 even numbers. Return 2.
"""


class Solution:
    def minCostToMoveChips(self, position):
        odd = 0
        even = 0
        for i in position:
            if(i % 2 != 0):
                odd += 1
            else:
                even += 1
        return min(odd, even)


obj = Solution()
print(obj.minCostToMoveChips([2, 2, 2, 3, 3]))
