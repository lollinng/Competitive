import math


class Solution():

    def answer(self, a, n):
        max_dig = 0
        for i in range(n-1):
            if(a[i] < a[i+1]):
                max_dig = max(max_dig, (a[i+1]-a[i]+1))
                a[i+1] = a[i] - 1
        return int(math.sqrt(max_dig))


array = [-1, 1, 1, 1]
obj = Solution()
print(obj.answer(array, len(array)))
