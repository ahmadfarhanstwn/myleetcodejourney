class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        output = 0
        v = nums[output]
        maxim = v
        for i in range(len(nums)):
            maxim = max(maxim,nums[i])
            if nums[i] < v:
                output = i
                v = maxim
        return output+1