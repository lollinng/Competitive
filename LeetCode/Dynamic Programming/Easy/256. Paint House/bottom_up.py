"""
In this question we have to find the min number of  money required to paint houses given that no adjancent house
have some paint

So we understand this question is simmilar to robing house but its 2d in nature

1) we try to use bottom up approch by finding the min cost of every color on the house
2) since we using three colors we add minimum of the other two colors used for a particular houses
3) and add the last we calculate the minium cost by calculating min of terminal array in the matrix afet iterations

# in the below example there are 4 houses and 3 colors 
[                            
    [1, 5, 7],    # below u can see we add 5+min(5,7),8+min(1,7),4+min(1,5)  to next stage 
    [5, 8, 4],    =>  [10,9,5]
    [3, 2, 9],                    => [8,7,18]
    [1, 2, 4]                                   => [8,10,11]
]
"""


class Solution:

    def paint(self, matris):
        leng = len(matris)

        if(matris == None or leng == 0):
            return 0

        if leng == 1:
            return min(matris[0])

        for row in range(1, leng):
            matris[row][0] = min(
                matris[row-1][1], matris[row-1][2]) + matris[row][0]
            matris[row][1] = min(
                matris[row-1][2], matris[row-1][0]) + matris[row][1]
            matris[row][2] = min(
                matris[row-1][0], matris[row-1][1]) + matris[row][2]
            print(matris)
        return min(matris[-1])


matris = [
    [1, 5, 7],
    [5, 8, 4],
    [3, 2, 9],
    [1, 2, 4]
]
# ans-8
obj = Solution()
print(obj.paint(matris))
