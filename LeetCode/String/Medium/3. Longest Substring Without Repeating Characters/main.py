class Solution:
    def lengthOfLongestSubstring(self, s) :
        l = 0
        dict_ = {}
        res = 0
        
        for r,char in enumerate(s):
            # duplicate
            if char in dict_ :
                
                # if duplicate inside l and r
                if dict_[char] >= l:  
                    l = dict_[char]+1
         
            dict_[char] = r
            res = max(res,r-l +1)
            
        return res

obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))
# print(obj.lengthOfLongestSubstring("bbbbb"))
print(obj.lengthOfLongestSubstring("pwwkep"))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        res = curr = 0
        voc = dict() 
        for r in range(len(s)):
            if s[r] in voc and voc[s[r]]>=l:
                l = voc[s[r]]+1
                voc[s[r]] = r    
                curr = r-l +1
            else:
                voc[s[r]] = r
                curr+=1
            if curr>res:
                res = curr
        return res  

        