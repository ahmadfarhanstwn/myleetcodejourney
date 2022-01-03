class CombinationIterator {
public:
    vector<string> combination;
    string chars;
    int n, index = 0;
    
    void backtrack(string& c, string a, int l)
    {
        if (a.size() == n)
        {
            combination.push_back(a);
            return;
        }
        for (int i = l; i < c.size(); i++)
        {
            a += c[i];
            backtrack(c, a, i+1);
            a.pop_back();
        }
    }
    
    CombinationIterator(string characters, int combinationLength) {
        sort(characters.begin(), characters.end());
        chars = characters;
        n = combinationLength;
        backtrack(chars, "", 0);
    }
    
    string next() {
        index++;
        return combination[index-1];
    }
    
    bool hasNext() {
        return index < combination.size() ? true : false;
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */