class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        if (nums.size() < 3) return 0;
        int consecutive = 2, res = 0, diff = nums[1] - nums[0];
        for (int i = 2; i < nums.size(); i++)
        {
            if (nums[i] - nums[i-1] == diff)
            {
                consecutive++;
                if (consecutive >= 3)
                    res += consecutive - 3 + 1;
            }
            else
            {
                consecutive = 2;
                diff = nums[i] - nums[i-1];
            }
        }
        return res;
    }
};