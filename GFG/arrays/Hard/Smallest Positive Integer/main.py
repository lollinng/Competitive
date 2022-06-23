class Solution:
    def smallestpositive(self, array, n):
        array.sort()
        res = 1
        i = 0
        while(i < n and array[i] <= res):
            res = res+array[i]
            i += 1
        return res


obj = Solution()
print(obj.smallestpositive([1, 1, 4], 3))
