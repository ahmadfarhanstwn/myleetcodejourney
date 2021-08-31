class Solution:
    def isThree(self, n: int) -> bool:
        divisor = 0
        for i in range(n, 0, -1):
            if divisor > 3:
                return False
            if n % i == 0:
                divisor += 1
        if divisor != 3:
            return False
        else:
            return True
                