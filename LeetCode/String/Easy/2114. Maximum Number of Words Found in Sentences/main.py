class Solution:
    def mostWordsFound(self, sentences):
        res = 0
        for i in sentences:
            res = max(len(i.split(" ")), res)
        return res


s = Solution()
input = ["alice and bob love leetcode",
         "i think so too", "this is great thanks very much"]
print(s.mostWordsFound(input))
