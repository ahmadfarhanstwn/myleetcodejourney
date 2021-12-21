class Solution {
private:
    map<string, double> dp;   
public:
    double knightProbability(int n, int k, int row, int column) {
        string key = to_string(row) + "," + to_string(column) + "," + to_string(k);
        if(dp.count(key) > 0) return dp[key];
        if(row < 0 || row >= n || column < 0 || column >= n) return 0.0;
        if(k == 0) return 1.0;
        double total = (knightProbability(n, k-1, row+1, column+2) + knightProbability(n, k-1, row+2, column+1) + knightProbability(n, k-1, row+2, column-1) + knightProbability(n, k-1, row+1, column-2) + knightProbability(n, k-1, row-1, column-2) + knightProbability(n, k-1, row-2, column-1) + knightProbability(n, k-1, row-2, column+1) + knightProbability(n, k-1, row-1, column+2))/8.0;
        dp[key] = total;
        return total;
    }
};