class Trie {
private:
    unordered_map<char, Trie*> next = {};
    bool theEndOfWord = false;
    
public:
    Trie() {
        
    }
    
    // ~Trie() {
    //     delete Trie;
    // }
    
    void insert(string word) {
        Trie* pCrawler = this;
        for (char i : word){
            if (!pCrawler->next.count(i))
                pCrawler->next[i] = new Trie();
            pCrawler = pCrawler->next[i];
        }
        pCrawler->theEndOfWord = true;
    }
    
    bool search(string word) {
        Trie* pCrawler = this;
        for (char i : word){
            if (!pCrawler->next.count(i))
                return false;
            pCrawler = pCrawler->next[i];
        }
        return pCrawler->theEndOfWord;
    }
    
    bool startsWith(string prefix) {
        Trie* pCrawler = this;
        for (char i : prefix){
            if (!pCrawler->next.count(i))
                return false;
            pCrawler = pCrawler->next[i];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */