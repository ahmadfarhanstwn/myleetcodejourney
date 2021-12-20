class Solution {
public:
    vector<string> simplifiedFractions(int n) {
        vector<string> res;
        for (int x = 2; x <= n; x++)
        {
            for(int y = 1; y < x; y++)
            {
                if (this->gcd(x,y) == 1)
                {
                    res.push_back(to_string(y) + "/" + to_string(x));
                }
            }
        }
        return res;
    }
    
    int gcd(int x, int y)
    {
        while(y)
        {
            int temp = x;
            x = y;
            y = temp % y;
        }
        return x;
    }
};