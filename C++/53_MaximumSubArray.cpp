class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int allSum = 0;
        int maxSum = nums[0];
        for (int i : nums){
            allSum += i;
            maxSum = std::max(allSum, maxSum);
            if (allSum < 0) {
                allSum = 0;
            }
        }
        return maxSum;
    }
};