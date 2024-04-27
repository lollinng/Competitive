"""
Here we to find elements which add up to the target
only diff btw this and 2sum , here is in ascending order

Here we employe two pointers l and r at left and right
if the sum is greater than target of l and r we 
decrease the r coz r is greater and do vice versa
is sum is smaller than target

"""


class Solution:
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1
        while(l<r):
            if numbers[l]+numbers[r]<target:
                l+=1
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                return [l+1,r+1]
