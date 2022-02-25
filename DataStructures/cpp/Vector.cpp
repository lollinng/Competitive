#include <iostream>
#include <vector>
using namespace std;

class test
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> y{2, 7, 11, 15};
        return y;
    }
};

int main()
{

    vector<int> y{2, 7, 11, 15};
    vector<vector<int>> A; // 2d matrix
    vector<int> ans(5);    // to intialise a vector of length 5

    test x;
    vector<int> output{x.twoSum(y, 9)}; // to store object vector of object x

    // print vector
    for (auto i = output.begin(); i != output.end(); ++i)
        cout << *i << " ";

    // built ins
    y[2]; // to access an element
    output.size();
};
