class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numberOfElement = {}
        output = []
        for i in nums:
            if i in numberOfElement:
                numberOfElement[i] += 1
            else:
                numberOfElement[i] = 1
            if numberOfElement[i] > len(nums)/3 and i not in output:
                output.append(i)
        return output