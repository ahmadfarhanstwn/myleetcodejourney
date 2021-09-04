class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        output = nums[0]
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
            if dict[i] > dict[output]:
                output = i
        return output