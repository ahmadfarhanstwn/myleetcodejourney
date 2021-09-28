class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        output = arr[:k]
        for i in range(k,len(arr)):
            if abs(arr[i]-x) < abs(output[0]-x):
                output.pop(0)
                output.append(arr[i])
        return output