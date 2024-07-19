from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Intuition

        1. Binary search for the whole matrix treating them
        as flatten using the % and // indexs for  
        7 
        row - 2 = 7//3 division
        col - 1 = 7%3  remainder
 
        TIME COMPlexity will be
        O(logn*logm)

        Space complexity will be
        O(1)
        
        '''
        rows,cols = len(matrix),len(matrix[0])
        left,right = 0, rows*cols-1

        while left<=right:
            mid = left + (right-left)//2
            
            value = matrix[mid//cols][mid%cols]
            
            if value>target:
                right = mid-1
            elif value==target:
                return True
            else:
                left=mid+1

        return False

