class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        output = []
        for i in nums:
            if i % 2 == 1:
                output.append(i)
            else:
                output.insert(0,i)
        return output