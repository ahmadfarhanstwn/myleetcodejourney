class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        oneDMat = [j for sub in mat for j in sub]
        if len(oneDMat) != (r*c):
            return mat
        
        ans = []
        column = []
        index = 0
        
        for x in range(r):
            for y in range(c):
                column.append(oneDMat[index])
                index += 1
            ans.append(column)
            column = []
        
        return ans