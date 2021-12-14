class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::map<int, int> maps;
        for(int &i : nums)
        {
            maps[i] += 1;
        }
        vector<int> res;
        priority_queue<pair<int,int>> priority;
        for(auto it = maps.begin(); it != maps.end(); it++)
        {
            priority.push(make_pair(it->second,it->first));
            if (priority.size() > maps.size() - k)
            {
                res.push_back(priority.top().second);
                priority.pop();
            }
        }
        return res;
    }
};