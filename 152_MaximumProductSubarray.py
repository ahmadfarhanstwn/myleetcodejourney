class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        onlyPositive, whole, outputPrefix = 1, 1, float("-inf")
        for i in range(len(nums)):
            whole *= nums[i]
            onlyPositive *= nums[i]
            outputPrefix = max(outputPrefix,max(whole,onlyPositive))
            if whole == 0: whole = 1
            if onlyPositive <= 0: onlyPositive = 1
        onlyPositive, whole, outputSuffix = 1, 1, float("-inf")
        for i in range(len(nums)-1,-1,-1):
            whole *= nums[i]
            onlyPositive *= nums[i]
            outputSuffix = max(outputSuffix,max(whole,onlyPositive))
            if whole == 0: whole = 1
            if onlyPositive <= 0: onlyPositive = 1
        return max(outputPrefix, outputSuffix)