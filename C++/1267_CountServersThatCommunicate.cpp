class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        unordered_map<int,int> col;
        int row, dob, m = grid.size(), n = grid[0].size(), res = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j])
                {
                    col[i]++;
                }
            }
            if (col[i] > 1) res += col[i];
        }
        for (int y = 0; y < n; y++)
        {
            row = 0;
            dob = 0;
            for (int x = 0; x < m; x++)
            {
                if (grid[x][y])
                {
                    if (col[x] > 1)
                        dob++;
                    else row++;
                }
            }
            if (row + dob > 1) res += row;
        }
        return res;
    }
};