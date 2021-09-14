class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        output, tempMax, tempMin = 0,0,0
        for i in nums:
            tempMax = max(0, tempMax + i)
            tempMin = min(0, tempMin + i)
            output = max(output, tempMax, abs(tempMin))
        return output
    
        ## Time Complexity = O(n)
        ## Space Complexity = O(1)