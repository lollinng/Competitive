"""
Here we can see the pattern that swaps each next element leaving the last element if the input lenght is odd
"""


class Solution:
    def convertToWave(self, n, a):
        for i in range(0, n-1, 2):
            a[i], a[i+1] = a[i+1], a[i]
        return a


obj = Solution()
print(obj.convertToWave(6, [2, 4, 7, 8, 9, 10]))
