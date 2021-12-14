class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> comb;
        this->combinations(comb, 1, res, n, k);
        return res;
    }
    
    void combinations(vector<int>& comb, int i, vector<vector<int>>& res, int n, int k)
    {
        if (comb.size() == k)
        {
            res.push_back(comb);
            return;
        }
        for(int j = i; j < n+1; j++)
        {
            comb.push_back(j);
            combinations(comb, j+1, res, n, k);
            comb.pop_back();
        }
    }
};