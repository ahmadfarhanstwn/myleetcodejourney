class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int iMin = min_element(begin(nums),end(nums)) - begin(nums), iMax = max_element(begin(nums),end(nums)) - begin(nums);
        int n = nums.size();
        if(iMin > iMax)
        {
            swap(iMin, iMax);
        }
        return min({iMax+1, n-iMin, iMin + 1 + n - iMax});
    }
};