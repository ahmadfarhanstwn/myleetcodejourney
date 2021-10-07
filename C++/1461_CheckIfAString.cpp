class Solution {
public:
    bool hasAllCodes(string s, int k) {
        if (k > s.size()) return false;
        unordered_set<string> appeared;
        for (int i = 0; i <= s.size()-k; i++){
            appeared.insert(s.substr(i,k));
        }
        return appeared.size() == pow(2,k);
    }
};