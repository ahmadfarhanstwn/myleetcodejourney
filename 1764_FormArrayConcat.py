class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        index = 0
        concat = 0
        for i in groups:
            if index >= len(nums):
                break
            while index < len(nums):
                if i == nums[index:index+len(i)]:
                    concat += 1 
                    index += len(i)
                    break
                else:
                    index += 1
        if concat == len(groups):
            return True
        return False