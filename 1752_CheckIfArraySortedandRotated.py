class Solution:
    def check(self, nums: List[int]) -> bool:
        lessThan = 0
        if nums[0] < nums[-1]: lessThan += 1
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                lessThan += 1
        return lessThan < 2