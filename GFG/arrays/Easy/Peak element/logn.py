"""
We using binary Search to achive logn complxity coz we need to see which element is not sorted and give its index
"""


class Solution:
    def peakElement(self, arr, n):

        l = 0
        r = n-1
        while(l < r):
            mid = int(l + (r-l)/2)
            if(arr[mid] < arr[mid+1]):
                l = mid+1
            else:
                r = mid
        return l
