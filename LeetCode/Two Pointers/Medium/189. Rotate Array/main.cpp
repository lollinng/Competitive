/*
2 methods to solve the problem

1) Replcaing element one by one (rotate1)- like insertion sort go through each consecative elements and move thier respective
positon to right k times . Space complexity O(n2) will give time limit error for large arrays

# Better way
2) Reversing the array acc to k - This method is shown in the algo.jpg left side , we revrse whole array followed by reversing the
first k elements and later reversing the remaining elemetns after k
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void reverse(vector<int> &nums, int start, int end)
    {
        while (start < end)
        {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    void rotate(vector<int> &nums, int k)
    {
        k = k % nums.size();
        reverse(nums, 0, nums.size() - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.size() - 1);
        for (auto i = nums.begin(); i != nums.end(); ++i)
            cout << *i << " ";
    }

    // this method has time complexity o(n2) so it takes too much time for big arrays
    void rotate1(vector<int> &nums, int k)
    {
        for (int i = 0; i < k; i++)
        {
            int replaced_element = nums[nums.size() - 1];
            for (int j = 0; j < nums.size(); j++)
            {
                int temp = nums[j];
                nums[j] = replaced_element;
                replaced_element = temp;
            }
        }
        for (auto i = nums.begin(); i != nums.end(); ++i)
            cout << *i << " ";
    }
};
int main()
{
    Solution x;
    vector<int> input = {1, 2, 3, 4, 5, 6, 7};
    x.rotate(input, 3);
    return 0;
}