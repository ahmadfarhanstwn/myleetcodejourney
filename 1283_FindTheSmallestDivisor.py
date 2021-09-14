import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left+right) // 2
            summy = sum([math.ceil(i/mid) for i in nums])
            if summy <= threshold:
                right = mid
            else:
                left = mid + 1
        return right