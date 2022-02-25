#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> runningSum(vector<int> &nums)
    {
        int i = 0;
        int sum = 0;
        while (i < nums.size())
        {
            nums[i] = nums[i] + sum;
            sum = nums[i];
            i++;
        }
        // for (auto i = nums.begin(); i != nums.end(); ++i)
        //     cout << *i << " ";
        return nums;
    }
};

int main()
{
    Solution x;
    vector<int> input = {1, 1, 1, 1, 1};
    x.runningSum(input);

    return 0;
}