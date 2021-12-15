class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        std::map<int,vector<int>> pairs;
        std::vector<int> res;
        int nextPair;
        for (auto &i : adjacentPairs)
        {
            pairs[i[0]].push_back(i[1]);
            pairs[i[1]].push_back(i[0]);
        }
        for (auto it = pairs.begin(); it != pairs.end(); it++)
        {
            if (it->second.size() == 1)
            {
                res.push_back(it->first);
                res.push_back(it->second[0]);
                nextPair = it->second[0];
                break;
            }
        }
        while(res.size() < pairs.size())
        {
            auto tail = res.back(), prev = res[res.size() - 2];
            if (pairs[nextPair][0] != prev)
            {
                res.push_back(pairs[nextPair][0]);
                nextPair = pairs[nextPair][0];
            }
            else
            {
                res.push_back(pairs[nextPair][1]);
                nextPair = pairs[nextPair][1];    
            }
        }
        return res;
    }
};