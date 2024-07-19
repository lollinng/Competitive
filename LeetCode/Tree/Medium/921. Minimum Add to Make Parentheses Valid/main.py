class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = extra_closing = 0

        for i in s:
            if i=='(':
                opening+=1
            else:
                if opening:
                    opening-=1
                else:
                    extra_closing+=1
        
        return extra_closing+opening