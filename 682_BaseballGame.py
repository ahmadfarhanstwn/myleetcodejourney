class Solution:
    def calPoints(self, ops: List[str]) -> int:
        point = []
        for i in ops:
            if i not in '+DC':
                point.append(int(i))
            elif i == '+':
                point.append(point[-1]+point[-2])
            elif i == 'D':
                point.append(2*point[-1])
            elif i == 'C':
                point.pop(-1)
        return sum(point)