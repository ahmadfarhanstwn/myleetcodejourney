class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in range(len(nums1)):
            for x in range(nums2.index(nums1[i]), len(nums2)):
                if nums2[x] > nums1[i]:
                    output.append(nums2[x])
                    break
            else:
                output.append(-1)
        return output