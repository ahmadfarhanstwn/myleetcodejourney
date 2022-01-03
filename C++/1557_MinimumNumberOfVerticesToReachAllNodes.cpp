class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int> res, notStart(n);
        for (auto& i : edges) notStart[i[1]] = 1;
        for (int j = 0; j < n; j++)
            if (notStart[j] == 0) res.push_back(j);
        return res;
    }
};