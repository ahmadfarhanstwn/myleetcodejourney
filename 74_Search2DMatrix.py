class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1] or target < matrix[0][0]: return False
        leftm, rightm = 0,len(matrix)
        while leftm < rightm:
            midm = (leftm+rightm)//2
            if matrix[midm][-1] == target:
                return True
            elif matrix[midm][-1] > target:
                rightm = midm
            else:
                leftm = midm + 1
        n = matrix[leftm]
        leftn, rightn = 0, len(n)
        while leftn < rightn:
            midn = (leftn+rightn)//2
            if n[midn] == target:
                return True
            elif n[midn] > target:
                rightn = midn
            else:
                leftn = midn+1
        return False