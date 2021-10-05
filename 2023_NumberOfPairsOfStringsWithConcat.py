class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        output = 0
        index = 0
        while index < len(nums):
            jIndex = 0
            while jIndex < len(nums):
                if index == jIndex:
                    jIndex += 1
                    continue
                if nums[index] + nums[jIndex] == target:
                    output += 1
                jIndex += 1
            index += 1
        return output