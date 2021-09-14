class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == len(nums): return nums
        elif k > len(nums):
            for i in range(k-len(nums)):
                nums.insert(0,nums.pop())
        else:
            for i in range(k):
                nums.insert(0,nums.pop())