/*
we use binary search to find the bad element and loop till the end in its direction
*/

// The API isBadVersion is defined for you.
bool isBadVersion(int version);

class Solution
{
public:
    int firstBadVersion(int n)
    {
        int low = 0;
        int high = n - 1;
        while (low <= high)
        {
            int mid = low + (high - low + 1) / 2;
            if (isBadVersion(mid))
                high = mid - 1;
            else
                low = mid + 1;
        }
        return low;
    }
};
