class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                a = max(a+nums[i], b)
            else:
                b = max(a, b+nums[i])
        return max(a, b)