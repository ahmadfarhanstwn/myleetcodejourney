class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        x = y = maxDistance = 0
        while x < len(nums1) and y < len(nums2):
            if nums1[x] > nums2[y]:
                x += 1
            else:
                maxDistance = max(maxDistance, y - x)
                y += 1
        return maxDistance