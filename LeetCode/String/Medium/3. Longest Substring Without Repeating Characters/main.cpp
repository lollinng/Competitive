#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int start = 0;
        int max_len = 0;
        unordered_map<char, int> used;
        for (int i = 0; i < s.length(); i++)
        {
            // s[i] is current iterations char
            if (used.count(s[i]) && start <= used[s[i]])
            {
                cout << s[i] << i << endl;
                start = used[s[i]] + 1;
            }
            else
            {

                max_len = max(max_len, i - start + 1);
                cout << max_len << "\t" << i - start << endl;
            }
            used[s[i]] = i;
        }
        return max_len;
    }
};

int main()
{
    Solution obj;
    int ans = obj.lengthOfLongestSubstring("abcabcbb");
    cout << ans;
}