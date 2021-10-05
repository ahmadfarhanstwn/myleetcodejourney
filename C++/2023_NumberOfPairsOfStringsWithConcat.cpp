class Solution {
public:
    int numOfPairs(vector<string>& nums, string target) {
        int output = 0, index = 0;
        while(index < nums.size()){
            int jIndex = 0;
            while(jIndex < nums.size()){
                if (index == jIndex){
                    jIndex++;
                    continue;
                }
                if (nums[index] + nums[jIndex] == target){
                    output += 1;
                }
                jIndex++;
            }
            index++;
        }
        return output;
    }
};