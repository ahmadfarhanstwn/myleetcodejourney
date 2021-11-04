class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = sorted([j for sub in grid for j in sub])
        median = a[len(a)//2]
        output = 0
        for i in a:
            if abs(median-i) % x == 0:
                output += abs(median-i) // x
            else:
                return -1
        return output
            