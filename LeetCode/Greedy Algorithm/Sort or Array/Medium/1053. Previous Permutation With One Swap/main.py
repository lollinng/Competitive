"""
Here we trying to find lexicographically largest permutation that is smaller than arrary, which means we gotta convert number
to its next smaller form. Eg - 19436579 to 19435679 

Intuition - 
1) we can see from the examples that we want to have ascending ordered element in the last
2) so while plotting the numbers as point as shown in the example we see a pattern that first element in descending order 
from last is replaced with max of the ascending order in the last s.t that the max is lesser than the number itself
3) We use prevPeropt1 function to find the first descending order for right and send the index(i) of the number  which is 
supposed to be swap  and break from the loop
4) We use find_max function to find_max from the right of index i such that max is smaller than index i element

Examples shown in the diagram
[1,9,4,6,7]                    =>   [1, 7, 4, 6, 9]
[3,17,5,10,13,15,10,5,16,8]    =>   [1, 9, 3, 4, 6, 7]
[1,9,4,3,6,5,7,9]              =>   [1, 9, 4, 3, 5, 6, 7, 9]
"""


class Solution:

    def find_max(self, i, a, n):
        maxs = i+1
        for j in range(n-1, i, -1):
            # if only j is greater than max and smaller than first descending element
            if(a[maxs] <= a[j] and a[j] < a[i]):
                maxs = j
        # Swap
        a[i], a[maxs] = a[maxs], a[i]
        return a

    def prevPermOpt1(self, arr):
        n = len(arr)
        for i in range(n-1, 0, -1):
            if(arr[i] < arr[i-1]):
                # sending the first descending element  from right to max_function
                arr = self.find_max(i-1, arr, n)
                break
        return arr


obj = Solution()
print(obj.prevPermOpt1([1, 9, 4, 6, 7]))
