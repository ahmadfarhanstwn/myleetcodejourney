class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] % 2 == 1: continue
            for x in range(len(arr)):
                if i == x: continue
                if arr[i] / 2 == arr[x]:
                    return True
        return False