class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        if nums == sortedNums: return 0
        left, right = 0,0
        for i in range(len(sortedNums)):
            if sortedNums[i] != nums[i]:
                left = i
                break
        for i in range(len(sortedNums)-1,-1,-1):
            if sortedNums[i] != nums[i]:
                right = i
                break
        return right - left + 1