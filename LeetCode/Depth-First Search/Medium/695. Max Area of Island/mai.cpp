#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        int max_area = 0;
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (grid[i][j] == 1)
                {
                    max_area = max(max_area, dfs(grid, i, j, 0));
                }
            }
        }
        return max_area;
    }

    int dfs(vector<vector<int>> &grid, int i, int j, int area)
    {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == 0)
            return area;

        area += 1;
        grid[i][j] = 0;

        area = dfs(grid, i + 1, j, area);
        area = dfs(grid, i - 1, j, area);
        area = dfs(grid, i, j + 1, area);
        area = dfs(grid, i, j - 1, area);

        return area;
    }
};

int main()
{
    Solution obj;
    vector<vector<int>> grid = {
        {0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
        {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
        {0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0}};
    int ans = obj.maxAreaOfIsland(grid);
    cout << ans;
}