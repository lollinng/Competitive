#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int finalValueAfterOperations(vector<string> &operations)
    {
        int ans = 0;
        for (int i = 0; i < operations.size(); i++)
        {
            (operations[i][1] == '+') ? ans++ : ans--;
        }
        return ans;
    }
};

int main()
{
    vector<string> input{"--X", "X++", "X++"};
    Solution obj;
    int ans = obj.finalValueAfterOperations(input);
    cout << ans;
}