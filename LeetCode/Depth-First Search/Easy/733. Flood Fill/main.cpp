#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int newColor)
    {

        dfs(image, sr, sc, image[sr][sc], newColor);
        return image;
    }

    void dfs(vector<vector<int>> &image, int r, int c, int color, int newColor)
    {

        if (r < 0 || c < 0 || r >= image.size() || c >= image[0].size() || image[r][c] == newColor || image[r][c] != color)
            return;

        image[r][c] = newColor;

        dfs(image, r + 1, c, color, newColor);
        dfs(image, r - 1, c, color, newColor);
        dfs(image, r, c + 1, color, newColor);
        dfs(image, r, c - 1, color, newColor);
    }
};

// testing
int main()
{
    Solution obj;
    vector<vector<int>>
        input{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
    vector<vector<int>> ans;
    ans = obj.floodFill(input, 1, 1, 2);
    for (int i = 0; i < ans.size(); i++)
    {
        for (int j = 0; j < ans[i].size(); j++)
        {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
}