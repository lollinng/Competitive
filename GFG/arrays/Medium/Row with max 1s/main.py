"""
Here instead of using brute of complexity m*n . We take into consideration that the elements are sorted in matrices
and at each row we start from behind and iterate till we have 1s in the left and keep our pointer there . If there 
are more 1s in a row the iterator goes more to left as well as writing the ans row in the variable if no more one found
it goes down to next row
"""


class Solution:
    def rowWithMax1s(self, arr, n, m):
        row = 0
        r = m-1  # right pointer
        ans = -1
        while(row < n and r >= 0):
            if arr[row][r] == 1:
                r = r-1
                ans = row
                #  print(ans,r,row)
            else:
                #  print(ans,r,row)
                row += 1
        return ans


obj = Solution()
print(obj.rowWithMax1s([[0, 1, 1, 1],
                        [0, 0, 1, 1],
                        [1, 1, 1, 1],
                        [0, 0, 0, 0]], 4, 4))
