class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numberOfDuplicate = 0
        
        for i in range(1, len(nums)):
            if nums[numberOfDuplicate] != nums[i]:
                numberOfDuplicate += 1
                nums[numberOfDuplicate] = nums[i]
                
        return numberOfDuplicate + 1