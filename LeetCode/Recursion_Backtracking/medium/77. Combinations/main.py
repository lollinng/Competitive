"""
here the problem is to given a range of digits we have to select subarray with fixed lenght of k
So we have to select whether an element should be pick/select at thier iteration
Hence we will use backtracking and recursion for this 

Intution:
Here after looking at the Decsioin Tree we find that we have to use a loop 
for ietrating through elements with index bigger than present index.
we append the temp_array with current index and then use recursion and
pop the element later to backtrack

Solution:
1) create res array
2) add end conditoin with len(array) as k
3) Use loop to iterate through various possibilities of adding other elements as we given range of elements
4) appending/selecting current index of loop to temp array hence all ranges will be covered
5) use recursion with next index in the loop to add the current index temp array
5) pop the curent index from temp_array and perform 3,4,5 with next index

"""


class Solution:
    def combine(self, n: int, k: int):
        
        res = []

        def dfs(start,comb):
            # end condition
            if len(comb)==k:
                res.append(comb[:])
                return

            
            for i in range(start,n+1):
                # using/appending start since we want the curent element to add up to next
                comb.append(i)
                # calling for next index to add to the current temp element
                dfs(i+1,comb)
                # popping the last element to backtrack
                comb.pop()
    
        dfs(1,[])
        return res
       

