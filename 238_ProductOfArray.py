class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        p = 1
        
        for i in range(len(nums)):
            output.append(p)
            p *= nums[i]
            
        p = 1
        
        for x in range(len(nums)-1, -1, -1):
            output[x] *= p
            p *= nums[x]
            
        return output