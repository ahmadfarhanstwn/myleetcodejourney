class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> countS(26,0), countP(26,0), output;
        if (p.size() > s.size()) return output;
        for(int i = 0; i < p.size(); ++i)
        {
            ++countP[p[i]-'a'];
            ++countS[s[i]-'a'];
        }
        if (countP == countS) output.push_back(0);
        for (int x = p.size(); x < s.size(); ++x){
            ++countS[s[x]-'a'];
            --countS[s[x-p.size()]-'a'];
            if (countS == countP){
                output.push_back(x-p.size()+1);
            }
        }
        return output;
    }
};