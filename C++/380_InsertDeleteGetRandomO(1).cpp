class RandomizedSet {
public:
    unordered_map<int,int> map;
    vector<int> list;
    
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (map.count(val)) return false;
        map[val] = list.size();
        list.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (!map.count(val)) return false;
        int valRemove = map[val];
        map.erase(val);
        if (valRemove != list.size()-1)
        {
            int lastVal = list[list.size()-1];
            list[valRemove] = lastVal;
            map[lastVal] = valRemove;
        }
        list.pop_back();
        return true;
    }
    
    int getRandom() {
        return list[rand() % list.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */