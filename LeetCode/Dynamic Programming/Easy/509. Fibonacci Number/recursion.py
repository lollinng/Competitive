"""
This is recurssion without dynmic memory so we dont keep in track of the output hence we might have to run
recursion for same value more than once 
"""


class Solution:
    def fib(self, n: int) -> int:
        if(n <= 1):
            return n
        return self.fib(n-1)+self.fib(n-2)


s = Solution()
print(s.fib(4))
