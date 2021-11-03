class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        index = len(nums) - 1
        currSum = 0
        self.mem = {}
        return self.dp(nums, target, index, currSum)
        
    def dp(self, nums, target, index, currSum):
        if (index, currSum) in self.mem:
            return self.mem[(index,currSum)]
        if index < 0 and currSum == target:
            return 1
        if index < 0:
            return 0
        
        positive = self.dp(nums, target, index-1, currSum + nums[index])
        negative = self.dp(nums, target, index-1, currSum + -nums[index])
        
        self.mem[(index, currSum)] = positive + negative
        return self.mem[(index, currSum)]