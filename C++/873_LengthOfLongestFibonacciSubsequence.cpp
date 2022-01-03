class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        unordered_set<int> ar(arr.begin(),arr.end());
        int res = 0;
        for (int i = 0; i < arr.size(); i++)
        {
            for (int j = i+1; j < arr.size(); j++)
            {
                int a = arr[i], b = arr[j], length = 2;
                while(ar.count(a+b))
                {
                    b = a+b, a = b-a, length++;
                }
                res = max(res,length);
            }
        }
        return res > 2 ? res : 0;
    }
};