"""
Using 3 pointers we try to parse the array keeping count of the 
1) No. of elements in the patern using left pointer
2) The rightmost elements in the pattern using right pointer
3) And the index to write usign the write pointer

Steps:
1) We only right at rightmost element in the pattern and at the end of the array
2) We first write the character
3) And write the number of elements in pattern after that if it greater than1
4) then we add edge case for more than 10 count we use for loop to add them one by one
5) and at each writing we update the write pointer
6) at each pattern end we updated the left pointer
"""


class Solution:
    def compress(self, chars):
        n = len(chars)
        left = 0
        write = 0

        for right,char in enumerate(chars):
            
            # we skip those element which arent the rightmost elements

            #  last element or  next element not equal
            if right+1==n or char!=chars[right+1]:

                # Writting the element
                chars[write] = char 
                write+=1
                
                # if current element has been repeating in the past we will have anchar far way
                # and calculate repeated by subtracting curr pos with anchor
                if right>left:
                    repeated_times = right - left + 1

                    # if string has 2 digit value it gets added seperate in the array
                    for num in str(repeated_times):
                        chars[write] = num 
                        write+=1
                
                left = right+1

        # write gives index for the array we edited
        return write


