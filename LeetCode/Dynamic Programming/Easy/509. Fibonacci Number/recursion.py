class Solution:
    def fib(self, n: int) -> int:
        if(n <= 1):
            return n

        return self.fib(n-1)+self.fib(n-2)


s = Solution()
print(s.fib(4))
