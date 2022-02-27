class Solution:
    def average(self, salary):
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)


s = Solution()
print(s.average([4000, 3000, 1000, 2000]))
