class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        indexLeft = left = right = output = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                left += 1
                indexLeft = i+1
            else:
                indexLeft = i+1
                break
        for i in range(indexLeft, len(nums)):
            if nums[i] == 1:
                right += 1
            else:
                output = max(output,left+right)
                left = right
                right = 0
        output = max(output,left+right)
        if output == len(nums):  return output-1
        return output
        
        # Time Complexity = O(n)
        # Space Complexity = O(1)