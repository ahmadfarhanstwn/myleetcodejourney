class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::string, vector<std::string>> map;
        int index;
        std::vector<std::vector<std::string>> res;
        for(std::string &i : strs)
        {
            std::string j = i;
            sort(j.begin(), j.end());
            map[j].push_back(i);
        }
        for (auto& x : map)
        {
            res.push_back(x.second);
        }
        return res;
    }
};