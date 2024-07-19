class Solution:
    def numSplits(self, s: str) -> int:
    
        left = set()
        right = {}
        n = len(s)
        res = 0
        

        # Initialize the left and right data structures
        left.add(s[0])
        for i in range(1,n) :
            right[s[i]] = right.get(s[i],0) +1 

        # Check the first split scenario
        if len(left) == len(right):
            res+=1

        # Iterate through the string to count valid splits
        for i in range(1,n-1):
            left.add(s[i])

            if right[s[i]]==1:
                del right[s[i]]
            else:
                right[s[i]] -= 1

            if len(left) == len(right):
                res+=1

        return res

            