class Solution:
    def arrangeCoins(self, n: int) -> int:
        output = 0
        index = 1
        while n >= index:
            n -= index
            index += 1
            output += 1
        return output