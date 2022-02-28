class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sums = 0
        for i in str(n):
            product *= int(i)
            sums += int(i)
        return product - sums


s = Solution()
print(s.subtractProductAndSum(4421))
