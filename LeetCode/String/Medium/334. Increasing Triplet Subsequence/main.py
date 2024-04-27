from math import inf

"""
Here we are trying to find smallest left and mid values and check if right value exist
1) Here we iterating though loop with max left and mid values
2) If ith element bigger than mid we return True
3) If ith element smaller than left we update left
4) If ithe element smaller than mid but bigger than left we update mid
5) Hence we wait for ith bigger right element to wrirtten True

"""


class Solution:
    def increasingTriplet(self, nums):

        left,mid = inf,inf

        for num in nums:
            if num>mid:
                return True
            
            if num<=left:
                left=num
            elif num<=mid:
                mid = num
            
        return False
                 


        
