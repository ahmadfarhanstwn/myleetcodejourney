class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        output = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                output = min(output, abs(i-start))
        return output