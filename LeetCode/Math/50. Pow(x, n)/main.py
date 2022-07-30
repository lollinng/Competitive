"""
Here we are trying to find the power of a number

intuition -
1) we use recursive function returning 0 when we reach n(power)=0
2) if n is negative we inverse the number and call the pow functions using +ve integer
3) if n is odd we mutiply extra x(number) and run the same recursive call as even.
4) we calculate the ans by dividing the n(power) by 2 and mutplying the x*n/2 values which will also
be called recursively to get its value
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        # We do +1 to avoid Integere overflow as in question negative values can have val upto 2raiseto31
        # but the built in integer range is till 2raiseto31 - 1 , hence we add value to negative n to decrease it
        if n < 0:
            return 1/x * self.myPow(1/x, -(n+1))

        recursive_call = self.myPow(x, n//2)
        # print(n)
        if(n % 2 != 0):
            return x*recursive_call*recursive_call
        else:
            # to depict square of a number and dividing x^4 = x^2*x^2
            return recursive_call*recursive_call


obj = Solution()
print(obj.myPow(2, 19))
