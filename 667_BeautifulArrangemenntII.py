class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        output = [1]
        result = 1
        distinc = k
        while distinc != 0:
            output.append(result + distinc)
            result += distinc
            distinc = (distinc-1) * -1 if distinc > 0 else (distinc+1) * -1
        if len(output) == n: return output
        for i in range(k+2,n+1):
            output.append(i)
        return output
    
        # Time Complexity = O(n)
        # Space Complexity = O(n)