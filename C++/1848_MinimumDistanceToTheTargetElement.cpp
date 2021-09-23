class Solution {
public:
    int getMinDistance(vector<int>& nums, int target, int start) {
        int output = nums.size();
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == target){
                output = std::min(output, std::abs(i-start));
            }
        }
        return output;
    }
};