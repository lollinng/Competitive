#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int low = 0, high = nums.size() - 1;
        while (low <= high)
        {
            int mid = low + (high - low + 1) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return low;
    }
};

//// for testing
// int main()
// {
//     vector<int> input{1, 3, 5, 6};
//     Solution x;
//     int ans = x.searchInsert(input, 5);
//     cout << ans;
//     return 0;
// }
