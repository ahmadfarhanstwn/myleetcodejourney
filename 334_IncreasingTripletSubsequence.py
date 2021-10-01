class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        increase = [float("inf")] * 2
        for i in nums:
            if i < increase[0] : 
                increase[0] = i
            if i < increase[1] and i > increase[0]:
                increase[1] = i
            if i > increase[1]:
                return True
        return False