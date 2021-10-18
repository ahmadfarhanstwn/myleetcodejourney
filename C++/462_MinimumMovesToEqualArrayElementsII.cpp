class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int median = nums.size()/2;
        int output = 0;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++){
            output += abs(nums[i]-nums[median]);
        }
        return output;
    }
};