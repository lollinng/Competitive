"""
Here we are trying to solve if we can use all tomato slices and chesse to make burgers

intitution - 
1) give in question 1(large) = 4(tom)+1(che) and 1(small) = 2(tom)+1(che)
2) We can create below equation through it  , where x is number of larger burgers and y is no. of small burgers
4*x + 2*y = tomatoSlices , x + y = cheeseSlices 
x = (tomatoSlices - 2*cheeseSlices)/2
y =  cheeseSlices - x 
3) we use this formulas to find number of burgers
4) if burger making isnt possible it wont return int for x or positive no. for x or y

"""


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int):

        x = (tomatoSlices - 2*cheeseSlices)/2
        y = cheeseSlices - x
        print(x)
        if int(x) == x and x >= 0 and y >= 0:
            return [int(x), int(y)]
        return []

        # 4*x + 2*y = tomatoSlices , x + y = cheeseSlices
        # x = (tomatoSlices - 2*cheeseSlices)/2
        # y =  cheeseSlices - x
