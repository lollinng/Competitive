"""

Here we are trying to find longest substring in a string

We are using two pointers l and r for sliding window implementation 
this pointers help us navigate the size of the each iteration's biggest substring  

We use dictionary to remmeber occurance of index of particular element and to 
add element or to update elements index when repeated

the left pointer gets updated to repeated words's previous occurance +1
and right pointe gets updated at every iteration
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0 
        r = 0
        used_char = {}

        while r<len(s):
            # print(res,l,r,used_char)

            # used_char[s[r]]<l used to remmber and allow repeated elements if its previous index is beyond our left pointer
            if s[r] not in used_char or used_char[s[r]]<l:
                # to get max of current string and the main answer
                res = max(r-l+1,res)
            else:
                # take left pointer to current repeated element
                l = used_char[s[r]] + 1
            # update index on dict
            used_char[s[r]] = r
            r+=1
        return res