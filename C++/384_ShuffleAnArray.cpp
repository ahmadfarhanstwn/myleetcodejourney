class Solution {
    vector<int> original;
public:
    Solution(vector<int>& nums) {
        this->original = nums;
    }
    
    vector<int> reset() {
        return this->original;
    }    
    vector<int> shuffle() {
        vector<int> shuffled(original);
        for (int i = 0; i < shuffled.size();i++)
        {
            int random = rand()% shuffled.size();
            swap(shuffled[i], shuffled[random]);
        }
        return shuffled;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */