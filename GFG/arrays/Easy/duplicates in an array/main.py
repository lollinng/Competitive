class Solution:
    def duplicates(self, arr, n):
        dicti = {}
        sets = set()
        for i in arr:
            if i not in dicti:
                dicti[i] = 0
            else:
                sets.add(i)
        if len(sets) == 0:
            return [-1]
        ans = list(sets)
        ans.sort()
        return ans


obj = Solution()
print(obj.duplicates([2, 3, 1, 2, 3], 5))
