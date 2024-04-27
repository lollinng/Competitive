"""
Here we have to rotate an 2d matrix in clockwise 90*

By looking at the pattern we select an left top element 
put it in temp and rotate all related elements 
We do same for the other index elements using a for loop between
l and r pointers

we use 4 pointers here to top,bottom l and r

after exchanging the elements in outermost layer we go inside
and exhcnage element in inner layer by updating l,r,bottom and top
since its square matrix l always equal to top 
and bottom equal to r

"""


class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix)-1
        while(l<r):
            for i in range(r-l):
                top,bottom = l,r
                
                # save the topLeft
                topLeft = matrix[top][l+i]

                # move bottom left into top left
                matrix[top][l+i] = matrix[bottom-i][l]

                # move bottom right into bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]

                # move top right inot bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                # move topleft into top right
                matrix[top+i][r] = topLeft

            # go inside the square
            l+=1
            r-=1