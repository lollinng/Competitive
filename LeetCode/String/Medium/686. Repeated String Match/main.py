class Solution:
    def repeatedStringMatch(self, a, b):
        
        created = ''
        res = 0
        while len(created)<len(b):
            created+=a
            res+=1
            if b in created:
                return res
        
        created+=a
        res+=1
        if b in created:
            return res
        return -1
