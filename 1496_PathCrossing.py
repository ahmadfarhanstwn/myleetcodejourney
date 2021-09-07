class Solution:
    def isPathCrossing(self, path: str) -> bool:
        history = {(0,0)}
        x, y = 0, 0
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'E':
                x += 1
            elif i == 'W':
                x -= 1
            else:
                y -= 1
            if (x,y) in history:
                return True
            history.add((x,y))
        return False