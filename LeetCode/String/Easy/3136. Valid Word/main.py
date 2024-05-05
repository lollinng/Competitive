class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False

        vowel = ['A','E','I','O','U']
        has_vowel = False
        has_consonent = False

        for i in word:
            if i.isalnum()==False:
                return False
            
            if i.upper() in vowel:
                has_vowel = True
            elif i.isalpha()==True and i.upper() not in vowel:
                has_consonent = True
        
        if has_vowel==True and has_consonent==True:
            return True
        else:
            return False 
