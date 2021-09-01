class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        output = 0
        index = 0
        while index < len(arr1):
            for y in arr2:
                if abs(arr1[index]-y) <= d:
                    index += 1
                    break
            else:
                output += 1
                index += 1
        return output