class Solution():
      def relativeSortArray(self,arr1,arr2):

        non_elements = []
        elements = {}

        arr2_set = set(arr2)

        for i in arr1:
            if i not in arr2_set:
                non_elements.append(i)
            else:
                if i in elements:
                    elements[i]+=1
                else:
                    elements[i]=1
        
        res = []
        for i in arr2:
            res += [i]*elements[i]
        
        non_elements.sort()
        return res+non_elements


"""
What comes to mind first is

I have to use pointer in both arrays
if they both equal


what come to my mind now is calculating how much
elements using hashmap
and then print it while iterating using the pointer in right array
and sort all the remaining elements

ok now the edge cases
what if elments not in arr1,arr2

time complexity : o(len(arr1))
space complexity : o(n)

The better solution was to use set
Since finding element in array is costlier o(N) and not 0(1) as compared to finding element in set

"""

