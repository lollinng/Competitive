
"""
here we trying to add number in a pascal format.

Solution - 
1) we create a temp list according to the index of the iteation with all ones
2) We append previous itrations values according to the logic of their indeces and itartion values
"""

class Solution:
    def generate(self, numRows):
        arr = [[1]]
    
        for i in range(1,numRows):
            temp = [1]*(i+1)            
            arr.append(temp)

            """
                1
              1 2 1
            1 3  3  1
            """
            for j in range(1,i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        return arr
            

obj = Solution()
print(obj.generate(5))