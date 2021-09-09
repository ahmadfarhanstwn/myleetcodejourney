class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        unique = set()
        l,r = 0,1
        output = 0
        while l < len(nums):
            while r < len(nums):
                if abs(nums[l] - nums[r]) == k and tuple(sorted([nums[l],nums[r]])) not in unique:
                    unique.add(tuple(sorted([nums[l],nums[r]])))
                    output += 1
                r += 1
            l += 1
            r = l + 1
        return output