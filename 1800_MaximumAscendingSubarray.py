class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        subArraySum = []
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                subArraySum.append(sum)
                sum = nums[i]
            else:
                sum += nums[i]
        subArraySum.append(sum)
        return max(subArraySum)