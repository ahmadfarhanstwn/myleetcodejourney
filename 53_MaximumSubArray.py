class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        allSum = 0 
        maxSum = nums[0]
        for i in nums:
            allSum += i
            maxSum = max(allSum, maxSum)
            if allSum < 0:
                allSum = 0
        return maxSum