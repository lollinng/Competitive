/*
Making a dict to store the indices and number value and checking after each iteration whether current iterations number is in the dict
m - dict
nums - vector/list
*/

#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> m;

        for (int i = 0; i < nums.size(); ++i)
        {
            int diff = target - nums[i];
            if (m.count(diff))
                return {m[diff], i};
            m[nums[i]] = i;
        }
        return nums;
    }
};

int main()
{
    Solution x;
    vector<int> y{2, 7, 11, 15};
    vector<int> output{x.twoSum(y, 9)};
    for (auto i = output.begin(); i != output.end(); ++i)
        cout << *i << " ";

    return 0;
}