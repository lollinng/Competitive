"""
here we have to convert string to integer according to given condiotns
1) removing the whitespaces before number or its sing
2) sign depicts its singed values
3) Number is accomponied after sign
4) Convert the char_number to int
5) Ans shouldnt be greater than int_max and int_min


Solution
We use left pointer to point to sign or first digit of number
We use right pointer to parse through number to last digit

1) For removing the whitespaces we use while loop and iterate our left pointer till no whitespace
2) we update left pointer if sign and parse through the whole number in next loop
3) we check if left:right is a number if yes then return vale solving the min,max edgecase
4) we also check if sign there coz .isnumeric() doesnt consider sign as int hence 
we check if skipping sign its int if yes then we return the values as above
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        
        n = len(s)
        if n == 0:
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31       

        left = 0 
        # removing white space        
        while  left<n and s[left]==" ":
            left+=1

        # updating right if sign present
        right = left
        sign= False
        if right<n and s[right] in  ["+","-"]:
            sign= True
            right=right+1
        
        # parsing through the number
        while right<n and s[right].isnumeric():
            right+=1

        # converting char_number into integer , using is_numeric to check if we found suitable char_number
        # isnumeric() ignore signed hence if signed true skipping the signing for function
        if s[left:right].isnumeric() or (sign==True and  s[left+1:right].isnumeric()):
            value =  int(s[left:right])
            # edge case given
            value = min(value,INT_MAX)
            value = max(INT_MIN, value)
            return value
        
        return 0