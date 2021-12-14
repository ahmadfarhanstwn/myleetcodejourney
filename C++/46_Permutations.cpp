class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        this->permutate(nums, 0, res);
        return res;
    }
    
    void permutate(vector<int>& nums, int i, vector<vector<int>>& res)
    {
        if(i == nums.size())
        {
            res.push_back(nums);
            return;
        }
        else
        {
            for(int j = i; j < nums.size(); j++)
            {
                swap(nums[j], nums[i]);
                permutate(nums, i+1, res);
                swap(nums[j],nums[i]);
            }
        }
    }
};