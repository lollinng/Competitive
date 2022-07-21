"""
Here we are trying to divide an 4 digit integere into 2 numbers s.t we get minimum number of sum betw them
We are trying to solve this using greddy approch as we trying to get best answer without seeing all possibilities
1) convert number into string
2) sort the integers in the string using sorted
3) keep 0,1 index number in aarray in the 10 th place of addtion
4) keep 2,3 index number in array in the ones place for addition
5) add the number to get the least output

For Eg - 
2932 => ['2','2','3,'9']
now answer = (2*10+3) + (2*10+9) = 23+29
"""


class Solution:
    def minimumSum(self, num):
        # output list/variables of sorted 4 digits
        a, b, c, d = sorted(str(num))

        # taking a,b smallest intger in 10s value and additng b and d as ones value
        # return (int(a)*10+int(c)) + (int(b)*10+int(d))
        return int(a+c) + int(b+d)


obj = Solution()
print(obj.minimumSum(2932))
# 23+29=52
