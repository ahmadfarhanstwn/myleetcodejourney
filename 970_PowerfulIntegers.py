class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xPowerBound = yPowerBound = index = 0
        output = []
        if x > 1:
            while index >= 0:
                if x**index > bound:
                    break
                xPowerBound = index
                index += 1
        index = 0
        if y > 1:
            while index >= 0:
                if y**index > bound:
                    break
                yPowerBound = index
                index += 1
        for xindex in range(xPowerBound+1):
            for yindex in range(yPowerBound+1):
                if (x**xindex) + (y**yindex) <= bound and (x**xindex) + (y**yindex) not in output:
                    output.append((x**xindex) + (y**yindex))
        return output