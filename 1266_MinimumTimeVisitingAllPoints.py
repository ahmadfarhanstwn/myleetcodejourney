class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        output = 0
        for i in range(1, len(points)):
            output += max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))
        return output