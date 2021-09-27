import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c))+1):
            z = c - (i*i)
            if sqrt(z) % 1 == 0:
                return True
        return False