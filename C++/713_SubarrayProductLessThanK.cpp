class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int left = 0, right = 0, output = 0, product = 1;
        int lleft;
        while(right < nums.size()){
            if (nums[right] > k){
                left = right + 1;
                right++;
                product = 1;
                continue;
            }
            product *= nums[right];
            if (product < k){
                output += right - left + 1;
                right++;
            } else{
                lleft = left;
                while(product >= k && lleft <= right){
                    product /= nums[lleft];
                    lleft++;
                }
                output += right - lleft + 1;
                left = lleft;
                right++;
            } 
        }
        return output;
    }
};