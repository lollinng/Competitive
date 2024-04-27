"""
Here we have to calculate roman numerals

The pattern is to calculate and add roman numeral backwards 
and subtract when we get smaller numeral like IX here I is smaller numeral

We iteratre the list backward and add roman values when the greaters then
prvious or else subtract

"""


class Solution:
    def romanToInt(self, s: str) -> int:
        prev = 0
        res = 0
        _dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in s[::-1]:
            if _dict[i] >= prev:
                res+=_dict[i]
            else:
                res-=_dict[i]
            prev = _dict[i]
        return res
         