class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        output = 0
        prefix = 0
        count = [1] + [0] * (k-1)
        for i in nums:
            prefix = (prefix + i) % k
            output += count[prefix]
            count[prefix] += 1
        return output