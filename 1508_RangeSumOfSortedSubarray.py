class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        array = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                array.append(sum(nums[i:j]))
        array.sort()
        return sum(array[left-1:right]) % (10**9+7)