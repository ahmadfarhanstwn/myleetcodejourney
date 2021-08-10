class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum = 0
        startValue = 1
        Answer = []
        
        for num in nums:
            sum += num
            Answer.append(max(startValue,1-sum))
            
        return max(Answer)