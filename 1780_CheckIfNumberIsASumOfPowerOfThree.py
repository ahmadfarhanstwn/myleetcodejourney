class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powerOfThree = [3**i for i in range(15)]
        for i in range(len(powerOfThree)-1,-1,-1):
            if n >= powerOfThree[i]:
                n -= powerOfThree[i]
        return n == 0
            