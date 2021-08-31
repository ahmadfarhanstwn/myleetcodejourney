class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibonacci = [1,1]
        n = fibonacci[0] + fibonacci[1]
        while n <= k:
            fibonacci.append(n)
            n = fibonacci[-1] + fibonacci[-2]
        output = 1
        add = fibonacci[-1]
        for i in range(len(fibonacci)-2, -1, -1):
            if k == add:
                break
            if fibonacci[i] + add <= k:
                add += fibonacci[i]
                output += 1
            else:
                continue
        return output