class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if nums[0] < 1:
            startValue = 1 - nums[0]
        else:
            startValue = 1
        sum = startValue + nums[0]
        
        for _ in range(startValue, startValue+2000):
            for i in range(1, len(nums)):
                sum += nums[i]
                if sum < 1:
                    startValue += 1
                    break
            if sum > 0:
                return startValue
                break
            else:
                sum = startValue + nums[0]