class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        similarity = 0
        for i in range(left, right+1):
            for x in ranges:
                if i >= x[0] and i <= x[1]:
                    similarity += 1
                    break
        return similarity == right+1-left