class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : (x[1],x[0]))
        output = 1
        x = points[0][1]
        for i in range(1,len(points)):
            if x < points[i][0] or x > points[i][1]:
                output += 1
                x = points[i][1]
        return output
                