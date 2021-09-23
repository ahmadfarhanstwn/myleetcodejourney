class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while (left < right){
            int mid = (left+right)/2;
            if (nums[mid] == target){
                return mid;
            }
            if (target < nums[0]){
                if (nums[mid] >= nums[0] && nums[mid] > target){
                    left = mid + 1;
                } else if (nums[mid] < nums[0] && nums[mid] < target){
                    left = mid + 1;
                } else if (nums[mid] < nums[0] and nums[mid] > target){
                    right = mid;
                }
            } else{
                if (nums[mid] < target && nums[mid] >= nums[0]){
                    left = mid + 1;
                } else if (nums[mid] > target || nums[mid] < nums[0]){
                    right = mid;
                }
            }
        }
        if (nums[std::min(left,right)] == target){
            return std::min(left,right);
        }
        return -1;
    }
};