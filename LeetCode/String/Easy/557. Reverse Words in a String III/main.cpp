#include <iostream>
#include <algorithm>
using namespace std;
class Solution
{

public:
    string reverseWords(string s)
    {
        string ans = "";
        int l = 0;
        int r = 0;
        while (r <= s.length())
        {
            if (s[r] == ' ' || r == s.size())
            {
                reverse(s.begin() + l, s.begin() + r);
                l = r + 1;
            }
            r++;
        }
        return s;
    }
};

int main()
{
    Solution obj;
    string input = "Hi Iam Prathamesh";
    string ans = obj.reverseWords(input);
    cout << ans;
}