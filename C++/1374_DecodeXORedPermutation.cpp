class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        vector<int> decoded;
        int a = 0;
        int n = encoded.size() + 1;
        for (int i = 1; i <= n; i++)
        {
            a ^= i;
            if (i < n && (i % 2) == 1)
            {
                a ^= encoded[i];
            }
        }
        decoded.push_back(a);
        for (int j : encoded)
        {
            decoded.push_back(decoded.back() ^ j);
        }
        return decoded;
    }
};