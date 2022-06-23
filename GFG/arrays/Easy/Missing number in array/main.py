from numpy import array


class Solution:
    def MissingNumber(self, array, n):
        counter = 1
        array.sort()
        for i in array:
            if i != counter:
                return counter
            counter += 1
        return counter


arrays = [6, 1, 2, 8, 3, 4, 7, 10, 5]
n = 10
obj = Solution()
print(obj.MissingNumber(arrays, n))
