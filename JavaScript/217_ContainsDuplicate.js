/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let unique = new Set()
    for(i = 0; i < nums.length; i++){
        if(unique.has(nums[i])){
            return true;
        }
        unique.add(nums[i])
    }
    return false;
};