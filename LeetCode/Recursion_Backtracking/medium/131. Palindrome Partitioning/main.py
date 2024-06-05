class Solution:
    
    def __init__(self):
        self.memory = {}

    # running recursion
    def partition(self, s):
        
        # break
        if not s: return [[]]
        if s in self.memory:return self.memory[s]

        ans = []
        for i in range(1,len(s)+1):
            if s[:i] == s[:i][::-1]:  # checking if palindrome

                sufix  = self.partition(s[i:]) # prcoess recursively
                for suf in sufix:
                    ans.append([s[:i]]+suf)
        self.memory[s] = ans
        return ans
            
                

    
            
