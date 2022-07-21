"""
Here we keep updating the array according to the particular recursive value of that particular element
"""


# Fastest out of the three coz it doesn hav recursive calls which dynamic have which hurts in long run
class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        # We taking 0 and 1 in context so we will need extra space for inputed index(n)
        array = [None]*(n+1)
        array[1] = array[2] = 1
        for i in range(3, n+1):
            array[i] = array[i-1]+array[i-2]
        print(array)
        return array[n]


s = Solution()
print(s.fib(4))
