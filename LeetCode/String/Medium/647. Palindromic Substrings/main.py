"""
here we have to find to find the count of all the palindromes in the string

Solution
1) count all the single character first that is res = len(s)
2) then iterate thought he loop one by one
3) palindrone can be even and odd hence we try to find the count of both of them
4) We have a helped function which has 2 pointers which check the validity of palindrome
here we check previous and next element if they same then thats a palindrone and increase the count
or else we break out of the function
4) odd palindrone can be found by giving previous element and next element to helper function
5) even palindrone can be found by giving current element and next element if they same it 
increases the count and iterate again with prev and next index if not we hit break 
and get out of loop returining count calculated and updating it main res resulst
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        for i in range(len(s)-1):

            # check if odd palindrone
            res+=self.helper(s,i-1,i+1)

            # check if even palindrone
            res+=self.helper(s,i,i+1)

        return res
        
    def helper(self,s,i,j):
        count = 0
        while i>-1 and j<len(s):
            if s[i] == s[j]:
                count+=1
            else:
                break
            i -=1
            j +=1
        return count
