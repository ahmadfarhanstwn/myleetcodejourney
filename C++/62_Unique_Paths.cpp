class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> current(n, 1);
        for (int x = 1; x < m; x++)
        {
            for (int y = 1; y < n; y++)
            {
                current[y] += current[y-1];
            }
        }
        return current[n-1];
    }
};