#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    // vector<int> twoSum(vector<int>& numbers, int target) {
    //     unordered_map<int, int> num;
    //     for(int i = 0;i<numbers.size();i++){
    //         int val = target - numbers[i];
    //         if(num.count(val)){
    //             return {num[val]+1,i+1};
    //         }
    //         num[numbers[i]] = i;
    //     }
    //     return {};
    // }

    // Pointer approch relatively faster
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int l = 0, r = numbers.size() - 1;
        while (l < r)
        {
            if (target < numbers[l] + numbers[r])
                r--;
            else if (target > numbers[l] + numbers[r])
                l++;
            else
                return {l + 1, r + 1};
        }

        return {};
    }
};

int main()
{
    Solution obj;
    vector<int> v{2, 7, 11, 15};
    vector<int> ans;
    ans = obj.twoSum(v, 9);
    for (auto i = ans.begin(); i != ans.end(); ++i)
        cout << *i << " ";
}