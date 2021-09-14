class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = str(n)
        product = 1
        summy = 0
        for i in a:
            product *= int(i)
            summy += int(i)
        return product - summy