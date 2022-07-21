class Solution:
    def getPairsCount(self, arr, n, k):
        dicti = {}
        ans = 0
        for i in arr:
            need = k - i
            if need in dicti:
                ans += dicti[need]
            if i in dicti:
                dicti[i] += 1
            else:
                dicti[i] = 1
        return ans


obj = Solution()
print(obj.getPairsCount([1, 5, 7, 1], 4, 6))
