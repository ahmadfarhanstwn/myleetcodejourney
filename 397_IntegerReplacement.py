class Solution:
    def integerReplacement(self, n: int) -> int:
        step = 0
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                if n % 4 == 1 or n == 3:
                    n -= 1
                else:
                    n += 1
            step += 1
        return step