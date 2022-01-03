class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        vector<int> res;
        int m = grid[0].size(), n = grid.size();
        for (int y = 0; y < m; y++)
        {
            int j = y;
            for (int x = 0; x < n; x++)
            {
                if (j < 0 || j >= m ||  grid[x][j] == 1 && j + 1 < m && grid[x][j+1] == -1 || grid[x][j] == -1 && j - 1 > 0 && grid[x][j-1] == 1)
                {
                    res.push_back(-1);
                    break;
                }
                j += grid[x][j];
            }
            if (res.size() == y) 
            {
                if ( j >= 0 && j < m) res.push_back(j);
                else res.push_back(-1);
            }
        }
        return res;
    }
};