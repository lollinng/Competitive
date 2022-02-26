/*
Here we use 3 pointers , 2 pointers for lowest and highest position in array and one pointer as highest nmumber of the ans array.
We first check both corner elements and put the bigger the element in the right side of the ans array
we decrease the high pointer if bigger element was from right side of the list or we increase the low pointer if its from left side of the list
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> ans(n);
        int lower_pointer = 0;
        int higher_pointer = n - 1;
        int pos = n - 1;
        while (pos >= 0)
        {
            // cout << lower_pointer << pos << higher_pointer << endl;
            if (abs(nums[lower_pointer]) > abs(nums[higher_pointer]))
            {
                ans[pos--] = nums[lower_pointer] * nums[lower_pointer];
                lower_pointer++;
            }
            else
            {
                ans[pos--] = nums[higher_pointer] * nums[higher_pointer];
                higher_pointer--;
            }

            // cout << lower_pointer << pos << higher_pointer << endl;
        }
        return ans;
    }
};

int main()
{
    Solution x;
    vector<int> input = {-4, -1, 0, 3, 10};
    int n = input.size();
    vector<int> ans(n);
    ans = x.sortedSquares(input);
    for (auto i = ans.begin(); i != ans.end(); ++i)
        cout << *i << " ";

    return 0;
}