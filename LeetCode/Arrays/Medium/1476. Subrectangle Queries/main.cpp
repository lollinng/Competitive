/*
Making a dict to store the indices and number value and checking after each iteration whether current iterations number is in the dict
m - dict
nums - vector/list
*/

#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class SubrectangleQueries
{

    vector<vector<int>> A;

public:
    // default constructor
    SubrectangleQueries(vector<vector<int>> &rectangle) : A(rectangle){};

    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
    {
        for (int i = row1; i < row2 + 1; i++)
        {
            for (int j = col1; j < col2 + 1; j++)
            {
                A[i][j] = newValue;
            }
        }
    }

    int getValue(int row, int col)
    {
        return A[row][col];
    }
};

//// for testing
// int main()
// {
//     vector<vector<int>> input{{1, 2, 1}, {4, 3, 4}, {3, 2, 1}, {1, 1, 1}};
//     SubrectangleQueries x(input);
//     x.getValue(0, 2);

//     return 0;
// }
