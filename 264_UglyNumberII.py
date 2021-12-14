class Solution:
    def nthUglyNumber(self, n: int) -> int:
        two = three = five = 0
        nextTwo = 2
        nextThree = 3
        nextFive = 5
        ugly = [0] * n
        ugly[0] = 1
        for i in range(1,n):
            ugly[i] = min( nextTwo, nextThree, nextFive)
            if nextTwo == ugly[i]: 
                two += 1 
                nextTwo = ugly[two]*2
            if nextThree == ugly[i]: 
                three+= 1
                nextThree = ugly[three]*3
            if nextFive == ugly[i]: 
                five+= 1
                nextFive = ugly[five]*5
        return ugly[-1]