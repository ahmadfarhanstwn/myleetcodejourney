class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = output = 0
        tempSum = sum(arr[:k])
        if tempSum >= k*threshold: 
            output += 1
        for i in range(k-1,len(arr)-1):
            tempSum = tempSum - arr[left] + arr[i+1]
            if tempSum >= k*threshold:
                output += 1
            left += 1
        return output
    
        # Time Complexity = O(n)
        # Space Complexity = O(1)