class Solution:
    def findAnagrams(self, s,p):
        res = []
        p = sorted(p)
        l = 0
        for i in range(len(p),len(s)+1):
            if self.Checkana(s[l:i],p):
                res.append(l)
            l+=1
        return res

    def Checkana(self,substr,p):
        if sorted(substr) == p:
            return True
        return False