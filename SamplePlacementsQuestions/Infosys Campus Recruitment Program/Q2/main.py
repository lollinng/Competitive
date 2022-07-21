from audioop import reverse


class Solution():
    def answer(self, villain, villain_no, hero, hero_no):
        sums_h = hero*hero_no
        villain.sort(reverse=True)
        for i in range(villain_no):
            if(villain[i] > sums_h):
                return villain_no-i-1
            else:
                sums_h -= villain[i]
        return 0


villain = [1, 2, 3, 1, 3]
hero = 4
hero_no = 1
villain_no = len(villain)
obj = Solution()
print(obj.answer(villain, villain_no, hero, hero_no))
