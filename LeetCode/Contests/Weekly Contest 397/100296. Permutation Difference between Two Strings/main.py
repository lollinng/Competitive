class Solution:
    def findPermutationDifference(self, s, t):

        i = 0
        dict_ = {}
        while(i<len(s)):
            if s[i] in dict_:
                dict_[s[i]] = abs(i - dict_[s[i]])  
            else:
                dict_[s[i]] = i
            if t[i] in dict_:
                dict_[t[i]] = abs(i - dict_[t[i]])  
            else:
                dict_[t[i]] = i
            i+=1
        
        return sum(dict_.values())
    


obj  =Solution()
k = [['abc','bac'],['abcde','edbac']]
k.append(['a','a'])
k.append(['bacd','bacd'])
for i in k:
    print(obj.findPermutationDifference(i[0],i[1]))