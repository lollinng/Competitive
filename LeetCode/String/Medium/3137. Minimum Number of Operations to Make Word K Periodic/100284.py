class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        
        chars = {}
        l  = 0
        for i in range(k,len(word)+1,k):
            chars[word[l:i]] = chars.get(word[l:i],0)+1
            l = i

        max_substring = max(chars,key=chars.get)
        not_max_substring = [x for x in chars.keys() if x!=max_substring]

        res = 0
        for i in not_max_substring:
            res += chars[i]
        return res