"""
here we are trying to find the largest palindrome

intution -
1) we have to check if every element is a orgin of palindrome
2) ther are 2 methods
    i) Brute force => looping over each element (n) -> checking its substring for all substring in array(n^2)
    ii) (n^2) => looping over each element (n) -> taking it as midpoint and goin left and righ simulatnosuly for checkign palin (n)
3) for odd palindromes we take one middle element and check for biggest palindrome from its orgin
4) for even palindrome we take 2 middle elements i,i+1 and check for biggest element from there
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxlen = 0
        n = len(s)
        

        for i in range(n):
           
           # Checking for odd palindrome by giving left and right same
            temp = self.helper(s,i,i)
            if len(temp) > maxlen:
                maxlen =  len(temp)
                res = temp
            
            # Checking for even palindrome by giving left as i and right one increented coz we not taking n-1 in loop 
            temp = self.helper(s,i,i+1)
            if len(temp) > maxlen:
                maxlen =  len(temp)
                res = temp

        return res
            
    def helper(self,s,l,r):
        res = ""
        # l+1 coz curent l not good  
        while(l>=0 and r<len(s) and s[l]==s[r]):
            res = s[l:r+1]
            l-=1
            r+=1
        return res
