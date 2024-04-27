class Solution:
    def reverseWords(self, s):
        lst = s.split(' ')
        res = ""
        for i in range(len(lst)-1,-1,-1):
            if lst[i]!="":
                res+=" "+lst[i]

        # 1: to remove the starting extra spac created in aboce formulae
        return res[1:]
 
