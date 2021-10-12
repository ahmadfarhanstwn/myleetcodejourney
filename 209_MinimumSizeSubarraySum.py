class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        output = len(nums) + 1
        while left < len(nums) and right < len(nums):
            if output == 1: return output
            if left > right : right = left
            if sum(nums[left:right+1]) >= target:
                output = min(output, right-left+1)
                left += 1
            else:
                right += 1
        return output % (len(nums) + 1)