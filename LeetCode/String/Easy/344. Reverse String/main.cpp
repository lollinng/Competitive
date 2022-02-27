#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void reverseString(vector<char> &s)
    {
        int l = 0;
        int r = s.size() - 1;

        while (l < r)
        {
            int temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            r--;
            l++;
        }

        for (auto i = s.begin(); i != s.end(); ++i)
            cout << *i << " ";
    }
};

int main()
{
    Solution obj;
    vector<char> input{'h', 'e', 'l', 'l', 'o'};
    obj.reverseString(input);
}