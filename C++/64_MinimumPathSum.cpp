class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int x = grid.size();
        int y = grid[0].size();
        for (int i = 1; i < y; i++)
        {
            grid[0][i] += grid[0][i-1];
        }
        for (int j = 1; j < x; j++)
        {
            grid[j][0] += grid[j-1][0];
        }
        for (int m = 1; m < x; m++)
        {
            for(int n = 1; n < y; n++)
            {
                grid[m][n] += min(grid[m-1][n], grid[m][n-1]);
            }
        }
        return grid[x-1][y-1];
    }
};