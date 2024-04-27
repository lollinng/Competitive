"""
Here we are trying to solve the zig zag pattern mentioned in the question.

intutions -
1) we can think zig zag as going down and up in vertically
2) we can reach bottom by adding 1 direction to loc counter
3) Each time we reach bottom we should change direction to -1 and add it to loc counter to go up until we reach up
4) hence by going up and down multiple times we can achive the goal

"""

class Solution:
    def convert(self, s: str, numRows):


        if numRows>=len(s) or numRows==1:
            return s 

        direction = 1
        loc = 0
        res = [""]*numRows
        
        for i in s:
            res[loc] += i
            
            if loc == 0:
                direction=1
            elif loc==numRows-1:
                direction=-1
            loc+=direction

        return "".join(res)

        

obj = Solution()
print(obj.convert("PAYPALISHIRING",3))
print(obj.convert('PAYPALISHIRING',4))