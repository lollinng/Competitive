class Solution:
    def answer(self, energy, Len, array):
        ans = 0
        array.sort(reverse=True)
        for i in array:
            if(i <= energy):
                ans += 1
                energy -= i
                if(i <= energy):
                    ans += 1
                    energy -= i
        return ans if energy <= 0 else -1


energy = 2
array = [1, 5, 2]

obj = Solution()
print(obj.answer(energy, len(array), array))
