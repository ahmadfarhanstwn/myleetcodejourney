class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        output = []
        sett = set(nums2)
        for i in sett:
            if i in nums1:
                output.append(i)
        return output