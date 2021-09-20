class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIndex, nonZeroIndex = 0,1
        while zeroIndex < len(nums) and nonZeroIndex < len(nums):
            if nums[zeroIndex] != 0:
                zeroIndex += 1
                nonZeroIndex += 1
            elif nums[nonZeroIndex] == 0:
                nonZeroIndex += 1
            else:
                temp = nums[zeroIndex]
                nums[zeroIndex] = nums[nonZeroIndex]
                nums[nonZeroIndex] = temp
                zeroIndex += 1
                nonZeroIndex += 1