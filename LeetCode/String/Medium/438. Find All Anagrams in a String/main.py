"""
Here we use sliding window approach and hasmaps for to find all the anagrams in the string

Solution : 
eg  =  "cbaebabacd" and "abc"

1) Create two hashmaps for checking the anagrams validity in s and p
2) Iterate though s and p till Len(p) as its anagram we have to find and then
   ount the occurance fo alphabets in both of them
   s = {'a': 1, 'b': 1, 'c': 1} p = {'c': 1, 'b': 1, 'a': 1}
3) now append result if both dict same at index 0
4) itertae though len(p) to len(s) as till p we convered in prev loop
and update new iterative value to dict and subtract left pointer value or behind the sliding window value
after subtraction if value is 0 then del or pop the value from dict since we dont wont 0 values to interfere
while checking equality condition
            p                   s                   res
{'a': 1, 'b': 1, 'c': 1} {'b': 1, 'a': 1, 'e': 1} [0]
{'a': 1, 'b': 1, 'c': 1} {'b': 1, 'a': 1, 'e': 1} [0]
{'a': 1, 'b': 1, 'c': 1} {'b': 1, 'a': 1, 'e': 1} [0]
{'a': 1, 'b': 1, 'c': 1} {'b': 2, 'a': 1} [0]
{'a': 1, 'b': 1, 'c': 1} {'b': 1, 'a': 2} [0]
{'a': 1, 'b': 1, 'c': 1} {'b': 1, 'a': 1, 'c': 1} [0, 6]
{'a': 1, 'b': 1, 'c': 1} {'a': 1, 'c': 1, 'd': 1} [0, 6]
5) check equality condition in each iteration and update left index to result if true
"""

class Solution:
    def findAnagrams(self, s,p):
        res = []        
        p_map,s_map = {} , {}

        if len(s)<len(p):
            return res
       
        # build map of character frequencies in p
        for i in range(len(p)):
            # if s[i] not in p_map then we get 0 defualt val from p_map.get(s[i]],0)
            p_map[p[i]] = 1 + p_map.get(p[i],0)
            s_map[s[i]]= 1 + s_map.get(s[i],0)

        if p_map == s_map:
            res.append(0)

        left = 0
        for i in range(len(p),len(s)):
            
            # incresing value of current number if first time then equal to one 
            # otherwise incremented by one
            s_map[s[i]] = 1 + s_map.get(s[i],0)
            # reducing value of previous number
            s_map[s[left]] -= 1

            # if s[i] not in s_map
            if s_map[s[left]] == 0:
                s_map.pop(s[left])
            left+=1

            # add index to res if dictionaries same
            if p_map == s_map:
                res.append(left)
            
        return res
    


