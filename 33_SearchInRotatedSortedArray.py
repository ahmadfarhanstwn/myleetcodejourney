class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if target < nums[0]:
                if (nums[mid] >= nums[0] and nums[mid] > target) or (nums[mid] < nums[0] and nums[mid] < target):
                    left = mid + 1
                elif nums[mid] < nums[0] and nums[mid] > target:
                    right = mid
            elif target >= nums[0]:
                if nums[mid] < target and nums[mid] >= nums[0]:
                    left = mid+1
                elif nums[mid] > target or nums[mid] < nums[0]:
                    right = mid
        if nums[min(left,right)] == target:
            return min(left,right)
        return -1