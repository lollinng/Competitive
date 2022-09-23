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
    def longestPalindrome(self, s):
        res = ""
        max_len = 0
        for i in range(len(s)):
            
            # for targetting odd palindromes # gabac
            temp = self.helper(s,i,i)
            if len(temp) > max_len:
                max_len = len(temp)
                res = temp
            
            # instead of i being same its consecative for even palindrome # abbc
            temp = self.helper(s,i,i+1)
            if len(temp) > max_len:
                max_len = len(temp)
                res = temp
            
        return res
        
        
    def helper(self,s,left,right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return s[left+1:right]
        
obj = Solution()
print(obj.longestPalindrome('babad'))
print(obj.longestPalindrome('cbbd'))