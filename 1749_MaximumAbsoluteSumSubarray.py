class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        outputMax, tempoMax = 0,0
        for i in nums:
            tempoMax += i
            if tempoMax > outputMax:
                outputMax = tempoMax
            if tempoMax < 0:
                tempoMax = 0
                
        outputMin, tempoMin = 0,0
        for i in nums:
            tempoMin += i
            if tempoMin < outputMin:
                outputMin = tempoMin
            if tempoMin > 0:
                tempoMin = 0
        
        return max(abs(outputMin), outputMax)
        
        ## Time Complexity = O(n+n)
        ## Space Complecity / Aux Space = O(1)