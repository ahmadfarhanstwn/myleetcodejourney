class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : (x[0],x[1]))
        minny = intervals[0][0]
        maxxy = intervals[0][1]
        output = []
        for i in range(1,len(intervals)):
            if intervals[i][0] <= maxxy:
                maxxy = max(maxxy,intervals[i][1])
            else:
                output.append([minny,maxxy])
                minny = intervals[i][0]
                maxxy = intervals[i][1]
        output.append([minny,maxxy])
        return output
    
    # Time Complexity = O(n(nLog(n)))
    # Space Complexity = O(output)