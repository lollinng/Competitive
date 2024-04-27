"""
IN this code we try to see the problem statments  pattern in top down fashion
where we taking steps either up or down by keeping in mind of the value counter
value counter helps understand whterh we reach down or up and steps help decide
direction

We take array of numRows specified and updated all of them  on by on 
depeding on our value which is updated using step.
value intializes negative step at bottom and postivive step at top 

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

"""


class Solution:
    def convert(self, s: str, numRows):
        if numRows == 1:
            return s

        out = [""]*numRows
        value = 0
        step = 1 
        for i in s:
            if value==numRows-1:
                step=-1
            elif value==0:
                step=1
            out[value]+=i
            value+=step
        return "".join(out)
