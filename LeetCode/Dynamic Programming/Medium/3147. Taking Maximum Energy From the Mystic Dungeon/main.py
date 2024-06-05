'''
Intuition
We want to find the maxmium possible enerfy we can gain , hence we have to use dp here checking all the possible cases.

Approach
First we will intialize a dp array to store the maximum energy at each index.
Insert 0th index energy and loop over the length of list
Then inside while loop we will loop over all the element smaller then k and intialize their values as same energy mentioned in the list since we can't jump over them from behind
We will add validation if i==n to break , coz of the while loop
Now comes the main part here we select the maximum possible value for that index , which will the either list value or a jump from k elements behind
We will return the max of last k-1 elements since we can jump from last k-1 elements to finish the process
Complexity
Time complexity:
O(n)

Space complexity:
$O(n)

'''
class Solution:
    def maximumEnergy(self, energy, k):
        n = len(energy)
        
        # dp array to store max magic value at each index
        dp_array = []
        dp_array.insert(0,energy[0]) 

        i = 1
        while(i<n):
            
            # storing all starting non jumpable values from list
            while(i<k):
                dp_array.insert(i,energy[i])   
                i+=1

            #  This break statement will solve the k==n edge case
            if i == n:
                break

            # geting max energy which will be either current magic  
            # value or last jump value added with curr
            res = max(energy[i],energy[i] + dp_array[i-k])            
            dp_array.insert(i,res)

            i+=1 
        return max(dp_array[-1:-k-1:-1])