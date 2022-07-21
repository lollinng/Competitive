"""
Here we use recurssion with memory of an array to calculate fibonnacchi
1) if its 0 or 1 its returned 0 or 1 according to question
2) if its calculated its returned the calculated recursive value from array memory
3) return the newly calculated value in the recursive function

[None, None, 1, None, None]
[None, None, 1, 2, None]
[None, None, 1, 2, 3]
3
"""


class Solution:

    def fib(self, n):
        # used one to forget about 0 and 1 index and start storing number with 2 index
        memo = [None]*(n+1)

        def recursion(n, memo):

            # to return number already calculated in the list and save computation
            if(memo[n] != None):
                return memo[n]

            # for returning 0 and 1
            if(n <= 1):
                return n

            memo[n] = recursion(n-1, memo)+recursion(n-2, memo)
            print(memo)
            return memo[n]

        return recursion(n, memo)


s = Solution()
print(s.fib(4))
