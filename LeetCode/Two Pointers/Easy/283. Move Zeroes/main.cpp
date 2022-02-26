/*
We intialise a zero index to take into consideration of left most zero .
If the present number isnt zero we swap it with the leftmost zero index
and add one to the zero index show that the zero number has one index towards right .
this works coz we swap as soon as we saw non zero element its mostly consective elements swapping postion for 1 zero
if 2 zero there we swapleftmost zero and the next zero becomes our zero_index
try to visualise it from visualise_code.txt in datastructure files
if no zero present in the list zero_index = i which means they keeping swapping itslef
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void moveZeroes(vector<int> &nums)
    {
        int zero_index = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] != 0)
            {
                int temp = nums[i];
                nums[i] = nums[zero_index];
                nums[zero_index] = temp;
                zero_index++;
            }
        }
        // for (auto i = nums.begin(); i != nums.end(); ++i)
        //     cout << *i << " ";
    }
};

int main()
{
    Solution obj;
    vector<int> input{0, 1, 0, 3, 12};
    obj.moveZeroes(input);
}