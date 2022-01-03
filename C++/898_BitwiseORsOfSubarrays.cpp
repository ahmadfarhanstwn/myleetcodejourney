class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        vector<int> res;
        int left = 0, right;
        for (int a : arr)
        {
            right = res.size();
            res.push_back(a);
            for (int j = left; j < right; j++)
            {
                if (res.back() != (res[j] | a)) {
                    res.push_back(res[j] | a);
                }
            }
            left = right;
        }
        return unordered_set(res.begin(), res.end()).size(); 
    }
};