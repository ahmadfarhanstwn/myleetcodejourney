class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int indexLeft = 0, left = 0, right = 0, output = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == 1){
                indexLeft = i + 1;
                left += 1;
            } else{
                indexLeft = i + 1;
                break;
            }
        }
        for (int j = indexLeft; j < nums.size(); j++){
            if (nums[j] == 1){
                right += 1;
            } else{
                output = std::max(output,left+right);
                left = right;
                right = 0;
            }
        }
        output = std::max(output, left+right);
        if (output == nums.size()){
            return output-1;
        }
        return output;
    }
};