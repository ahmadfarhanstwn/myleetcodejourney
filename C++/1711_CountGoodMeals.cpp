class Solution {
public:
    int countPairs(vector<int>& deliciousness) {
        unordered_map<int,int> deli;
        long long res = 0;
        for (int& j : deliciousness)
        {
            for(int p = 1; p <= (1<<22); p*=2)
            {
                if(deli.count(p-j)) res += deli[p-j];
            }
            deli[j]+=1;
        }
        return res % (int)(1e9 + 7);
    }
};