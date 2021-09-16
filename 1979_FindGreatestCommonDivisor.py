class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minny = min(nums)
        maxim = max(nums)
        for i in range(minny, 0, -1):
            if minny % i == 0 and maxim % i == 0:
                return i