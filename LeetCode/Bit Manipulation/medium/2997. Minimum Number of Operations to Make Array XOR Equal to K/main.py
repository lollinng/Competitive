"""

Here the intuition is that 

we dont have to change any bit in any character
but we take xor of all and check how many beats
to change with the result they want

hence in
final_xor and k we check how many bits different



"""

class Solution:
    def minOperations(self, nums,k):
        
        """
        010
        001
        011
        100

        100    final_xor
        
        001    k=1
        
        2      ans: 2 bits to change between final_xor and k 
        """

        final_xor = 0 
        # getting all the total_xor value first
        for n in nums:
            final_xor = final_xor ^ n
        
        count = 0
        # print(final_xor) # its represented as 4 not as 100 same with k as 1 not as 001
        # iterate till ither of these are not zero
        while k or final_xor:

            # checking if we need to change bit
            if (k%2) != (final_xor%2):
                count+=1
            
            # remove the last digit from the numer
            k = k//2  # integer division
            # hence 1//2 = 0 , 4//2 = 2 => 0,1 => 0,0
            final_xor = final_xor//2
            # print(k,final_xor)


        return count