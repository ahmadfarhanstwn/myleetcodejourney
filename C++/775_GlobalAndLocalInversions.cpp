class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) {
        int maxim = 0;
        int n = nums.size();
        for (int i = 0; i < n-2;++i){
            maxim = max(maxim, nums[i]);
            if (maxim > nums[i+2]){
                return false;
            }
        }
        return true;
    }
};