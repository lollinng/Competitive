"""
we use binary search to find the bad element and loop till the end in its direction
"""


# The isBadVersion API is already defined for you.


def isBadVersion(version: int):
    return ""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        n = n - 1
        while(low <= n):
            mid = low + (n-low)//2
            if isBadVersion(mid):
                n = mid-1
            else:
                low = mid+1
        return low
