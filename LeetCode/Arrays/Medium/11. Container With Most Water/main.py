"""
Here we are trying to find the largerst area length and breadth 
wise for a container. 

We are trying to start from maximum by keeping x axis max
and then iteration through pointers removing the bottlenecks

hence we start with big x axis gap and calculate area
hence we increase the pointer whose rod was smaller hence 
increasing our chances on getting bigger area.
"""


class Solution:
    def maxArea(self, height):
        l = 0
        res = 0
        r = len(height)-1
        while l<r:
            area = min(height[l],height[r]) * (r-l)
            res = max(res,area)
            if height[l]>=height[r]:
                r-=1
            else:
                l+=1
        return res
