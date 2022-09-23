"""
Here we are trying to solve the zig zag pattern mentioned in the question.

intutions -
1) we can think zig zag as going down and up in vertically
2) we can reach bottom by adding 1 stepp to value counter
3) Each time we reach bottom we should change step to -1 and add it to value counter to go up until we reach up
4) hence by going up and down multiple times we can achive the goal

"""


class Solution:
    def convert(self, s, numRow):
        
        if numRow == 1 or numRow >= len(s):
            return s
        
        out = ['']*numRow
        value,step = 0,1
        
        for i in s:
            if(value==0):
                step = 1
            elif(value == numRow-1):
                step = -1
            

            out[value] += i
            value+=step
            
        return "".join(out)

obj = Solution()
print(obj.convert("PAYPALISHIRING",3))
print(obj.convert('PAYPALISHIRING',4))