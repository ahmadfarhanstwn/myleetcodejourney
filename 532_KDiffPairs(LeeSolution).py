from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        unique = Counter(nums)
        output = 0
        for i in unique:
            if k > 0 and i + k in unique or k == 0 and unique[i] > 1:
                output += 1
        return output