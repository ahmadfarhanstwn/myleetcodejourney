class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        lastMinusIndex = firstMinusIndex = minusCount = output = index = longestSubArrayNow = startSubArray = 0
        while index < len(nums):
            if nums[index] > 0 :
                longestSubArrayNow += 1
            elif nums[index] < 0:
                if minusCount == 0:
                    firstMinusIndex = index
                lastMinusIndex = index
                minusCount += 1
                longestSubArrayNow += 1
            else:
                if minusCount % 2 == 1:
                    longestSubArrayNow = max(lastMinusIndex-startSubArray,index-1-lastMinusIndex, index-1-firstMinusIndex)
                output = max(longestSubArrayNow, output)
                startSubArray = index + 1
                longestSubArrayNow = 0
                lastMinusIndex = 0
                minusCount = 0
            index += 1
        if minusCount % 2 == 1:
            longestSubArrayNow = max(lastMinusIndex-startSubArray,index-1-lastMinusIndex, index-1-firstMinusIndex)
        output = max(longestSubArrayNow, output)
        return output