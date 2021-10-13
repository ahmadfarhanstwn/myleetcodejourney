class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(rowSum)):
            arr = []
            for j in range(len(colSum)):
                minny = min(rowSum[i], colSum[j])
                arr.append(minny)
                rowSum[i] -= minny
                colSum[j] -= minny
            output.append(arr)
        return output