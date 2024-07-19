class Solution:
    def findPeakElement(self, nums):
        '''
        1d Arrays can be viewed 2 dimensionally using thier values
                        6
                     5    4
            2     3
        1      1     


        here you can see the array has incrementing sequence

        if we catch such incrementing sequence using binary search and go to end of it 
        we will get our top peak element

        [ 1 ,   2  ,1,     3,  5   ,   6   ,   4]

        0 , 7
        start with middle index 3 ie 3 
        check if 3 is peak if not 

        now one element is greater coz its not peak
        go to that element side and do binary search in that part
        if no bigger elements then the one we saw then
        we know atleast we will get that element as answer
        '''

        n = len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        low,high = 0 ,n-1 
        while low<=high:
            mid = low+(high-low)//2

            # checking peak condition
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]>nums[mid]:
                high = mid-1
            else:
                low = mid+1
    
        return -1
        '''
        [1,2,1,3,5,6,4]
        low,mid,high
        0 3 7
        4 5 7 
        6 6 7
        '''
    
