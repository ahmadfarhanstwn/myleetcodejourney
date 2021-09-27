class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(l)):
            arr = sorted(nums[l[i]:r[i]+1])
            diff = arr[1] - arr[0]
            for i in range(2,len(arr)):
                if arr[i] - arr[i-1] != diff:
                    output.append(False)
                    break
            else:
                output.append(True)
        return output