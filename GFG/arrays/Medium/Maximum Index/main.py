"""
Here we are supposed to find maximum differnec in btw the index of right and left element such that right element is bigger than left one
To avoid 0n2 complexity we use window sliding or 2 pointer method where r is kept as rightmost and the leftmost element makes the r parse
towards it untill they meet or we find a bigger element for l . After either two we increase l and do the same steps again.
"""


class Solution:
    def maxIndexDiff(self, A, N):
        l = 0
        r = N-1
        maxs = -1
        while(l <= r):
            if(A[l] <= A[r]):
                maxs = max(maxs, r-l)
                # print(maxs,l,r)
                l = l + 1         # we increase the l
                r = N-1           # and reset the r to right again for new l
            else:
                r -= 1
        return maxs


obj = Solution()
print(obj.maxIndexDiff([34, 8, 10, 3, 2, 80, 30, 33, 1], 9))
