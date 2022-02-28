class Solution:

    def hammingWeight(self, n: int) -> int:
        res = 0
        # n not equal to 0
        while(n):
            res += n % 2                   # increse the counter if the rightmost element is 1
            n = n >> 1                     # to move the bit to right
        return res

    def hammingWeight1(self, n: int) -> int:
        res = 0
        # n not equal to 0
        while(n):
            n &= (n-1)      # anding with n-1 decrease the count of 1 in thearray
            res += 1
        return res

# Input: n = 00000000000000000000000000001011
# Output: 3
