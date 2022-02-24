/*
Binary Search -  we recursively divide the array in half to find the element
*/

#include <vector>
#include <iostream>

using namespace std;
class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int low = 0;
        int high = nums.size() - 1;
        while (low <= high)
        {
            int mid = low + (high - low + 1) / 2;
            cout << low << mid << high << endl;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
            cout << low << mid << high << endl;
        }
        return -1;
    }
};

int main()
{
    Solution x;
    vector<int> y{-1, 0, 3, 5, 9, 12};
    int out{x.search(y, 9)};
    cout << out;
    return 0;
}