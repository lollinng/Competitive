"""
In this problem weather a partiular element should be selected/takend for making subset is consider
In such selection problem we use decision trees

Solution:
1) Create res and a temp curr_subset array
2) create dfs function inside function for recursion purpose and parsing Decision tree in dfs manner
3) Add breaking point condition in dfs function from which the nodes will backtrack using return statement
4) add the 2 conditions for decision which are
    i) element is selected : add element in temp array and run dfs as recursion with next index
    ii) element is not selected : if current ith index element is not selected then its popped off of the array and recursion is ran for next index
5) We add temp array to the res in the lead node or state as we can see the diag in this case leaf state contains our answer


"""

class Solution:
    def subsets(self, nums):
        res = []


        curr_subset = []
        def dfs(i):
            
            # Breaking point condition
            if i>=len(nums):
                res.append(curr_subset.copy())
                return

            # if we want add element of index i
            curr_subset.append(nums[i])
            dfs(i+1)

            # if we dont want to add element of index i
            # removing previously added element and running dfs
            # This helps in popping only one element even if we have appended many elements before then it will be at leaf ndoe
            curr_subset.pop()  

            dfs(i+1)

            
        dfs(0)
        return res

