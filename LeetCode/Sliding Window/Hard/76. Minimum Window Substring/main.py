'''
s = ADOBECODEBANC , t = "ABC"

here we will iterate from left to right in s 
with two pointrs giving us resultand string between them

we will a need dictionary to remember the count of th elements
2 dictinaries to compare the reultant 

we will calculate dict of t pehla
and keep updating dict for s in the loop according to sliding window


ITERATION
ADOBECODEBANC

A better way to solve is required characters with dict approach
last time we were checking dict values count to understand the keys
now we will put another variable to confirm if all required keys there

'''

class Solution:
    
    def minWindow(self, s: str, t: str):
        if t=="":return ""

        window,countT = {},{}

        for c in t:
            countT[c] = 1 + countT.get(c,0) 

        have,need = 0,len(countT)
        res,resLen = [-1,-1],float('+inf')
        l = 0

        for r in range(len(s)):

            # adding r to dict (very element to the dict)
            c = s[r]
            window[c] = 1+ window.get(c,0)

            # check if c has made the dict equal
            if c in countT and window[c] == countT[c]:
                have+=1

            # while we have perfect substring
            while have==need:

                # udpate the result
                if (r-l+1)<resLen : 
                    res = [l,r]
                    resLen = (r-l+1)
                
                # remove from the left of the window
                window[s[l]] -= 1
                
                # checking if we removed on of the main chracters
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1

                # iterating the left pointer
                l+=1

        l,r = res
        return s[l:r+1] if resLen!=float('+inf') else "" 







    '''
    def minWindow(self, s: str, t: str):

        # Count characters in string t
        target_count = Counter(t)

        # INTIALIZE THE pointers and variable
        left = 0
        right = 0
        min_length = float('inf')
        res = ""
        required_chars = len(target_count)

        while right<len(s):
            
            #expand the window to right , and add the occurance
            if s[right] in target_count:
                target_count[s[right]] -=1     # reduce target_count if char found
                if target_count[s[right]] == 0:
                    required_chars -=1       # reduce required_chars if char reaches atleas 0 means perfect char count
            

            # Contract the left pointer if all chracters found
            while required_chars == 0:
                
                # add to the result
                if right-left + 1 < min_length:
                    min_length = right - left + 1
                    res = s[left:right + 1]

                # remove the last element 
                if s[left] in  target_count:
                    target_count[s[left]] +=1
                    if target_count[s[left]] > 0:
                        required_chars +=1
                left+=1
            
            right+=1
        return res
        '''

    '''
    def minWindow0(self, s: str, t: str) -> str:

        m = len(s)
        n = len(t)
        if n>m:
            return ""
        elif t==s:
            return s

        n_dict = {}
        for i in range(n):
            n_dict[t[i]] = n_dict.get(t[i],0) - 1


        # Initialize pointers and variables
        l  = 0
        r = 0
        res = s+"a"

        def valid(l,r,res):
            neg_flag = False 
            for i in n_dict.values() :
                if i<0:
                    neg_flag = True
            if neg_flag == False:
                if len(s[l:r])<len(res):
                    res = s[l:r]
                return res,True
            return res,False


        while True:

            if r>m:
                break
            elif l>=m:
                break

            # Loop r , makes all element postive , means captures all chracters
            while r<m:
              
                res,flag = valid(l,r,res)
                if flag==True:
                    break
                #reduce the dict
                if s[r] in n_dict:
                    n_dict[s[r]] +=1
                r+=1
                    
            res,_ = valid(l,r,res)
            if s[l] in n_dict:
                n_dict[s[l]] -= 1
            l+=1
            

        
        return res if res!=s+"a" else ""
        '''
            
            
        