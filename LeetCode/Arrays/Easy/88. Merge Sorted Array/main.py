"""
Here we are trying to go descending 

[4, 5, 6, 0, 0, 0] [1, 2, 3]
[4,5,6] | [1,2,3]

Here we update the last zero with bigger elements and decrease m or n counter/pointers8 accoridngly
this helps filling the zeros and then override left side
If m beomes zero we override all left contents of n to the array
"""



class Solution:
    def merge(self, nums1, m, nums2, n):

        while m>0 and n>0:
            # k will autmatically decrease as either m or n decresing in every iteration
            k = m+n
            if nums1[m-1] >= nums2[n-1]:
                nums1[k-1] = nums1[m-1]
                m-=1
            else:
                nums1[k-1] = nums2[n-1]
                n-=1
            k-=1
            # all the n value from n which didnt got remolded into nums1 coz m got zero
        nums1[:n] = nums2[:n]


s = Solution()
s.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
