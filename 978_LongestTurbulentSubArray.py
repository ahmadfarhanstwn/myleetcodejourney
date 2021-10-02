class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        moreThan = arr[0] > arr[1]
        output = 0
        subarray = 2 if arr[0] != arr[1] else 1
        for i in range(1,len(arr)-1):
            if moreThan:
                if arr[i] < arr[i+1]:
                    subarray += 1
                    moreThan = False
                elif arr[i] > arr[i+1]:
                    output = max(output, subarray)
                    subarray = 2
                else:
                    output = max(output, subarray)
                    subarray = 1
            else:
                if arr[i] > arr[i+1]:
                    subarray += 1
                    moreThan = True
                elif arr[i] < arr[i+1]:
                    output = max(output, subarray)
                    subarray = 2
                else:
                    output = max(output, subarray)
                    subarray = 1
        output = max(output, subarray)
        return output
    
    ## Time Complexity = O(n)
    ## Space Complexity = O(1)