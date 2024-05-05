class Solution:
    def isPalindrome(self, s: str) -> bool:
      
        if len(s) == 1:
            return True
        
        s  = [ch.upper() for ch in s if ch.isalnum()==True]
        l = 0
        r = len(s)-1  
        while (l<r):
            if s[l]!=s[r]:
                return False        
            l+=1
            r-=1

        return True