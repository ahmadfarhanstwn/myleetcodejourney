class Solution:
    def minOperations(self, nums: List[int]) -> int:
        output = 0
        for i in nums:
            output += bin(i).count("1")
        output += len(bin(max(nums))) - 3
        return output