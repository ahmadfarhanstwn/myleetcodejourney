class Solution {
public:
    vector<int> processQueries(vector<int>& queries, int m) {
        vector<int> res;
        int index;
        vector<int> p;
        vector<int>::iterator itr;
        for(int i = 1; i <= m; i++)
        {
            p.push_back({i});
        }
        for(int i=0; i<queries.size(); i++)
        {
            itr = find(p.begin(), p.end(), queries[i]);
            index = itr-p.begin();
            res.push_back(index);
            p.erase(itr);
            p.insert(p.begin(), queries[i]);
        }
        return res;
    }
};