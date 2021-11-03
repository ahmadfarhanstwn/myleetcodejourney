class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        maxim = 0
        for i in range(len(nums)-2):
            maxim = max(maxim, nums[i])
            if maxim > nums[i+2]:
                return False
        return True