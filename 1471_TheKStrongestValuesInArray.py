class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr)-1)//2]
        output = []
        left, right = 0, -1
        while len(output) < k:
            if abs(arr[right]-median) > abs(arr[left]-median):
                output.append(arr[right])
                right -= 1
            elif abs(arr[left]-median) > abs(arr[right]-median):
                output.append(arr[left])
                left += 1
            else:
                output.append(max(arr[left],arr[right]))
                if arr[left] > arr[right]:
                    left += 1
                else:
                    right -= 1
        return output