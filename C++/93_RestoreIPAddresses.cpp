class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        std::string ans;
        for(int a = 1; a <= 3; a++)
        {
            for(int b = 1; b <= 3; b++)
            {
                for(int c = 1; c <= 3; c++)
                {
                    for (int d = 1; d <= 3; d++)
                    {
                        if (a + b + c + d == s.length())
                        {
                            int aS = stoi(s.substr(0,a));
                            int bS = stoi(s.substr(a,b));
                            int cS = stoi(s.substr(a+b,c));
                            int dS = stoi(s.substr(a+b+c, d));
                            if (aS <= 255 && bS <= 255 && cS <= 255 && dS <= 255)
                            {
                                ans = to_string(aS) + "." + to_string(bS) + "." + to_string(cS) + "." + to_string(dS);
                                if (ans.length() == s.length() + 3)
                                {
                                    res.push_back(ans);
                                }
                            }
                        }    
                    }
                }
            }
        }
        return res;
    }
};