class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                    break
        elif target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
                    break