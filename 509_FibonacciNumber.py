class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        fibonacci = [0,1]
        
        for i in range(2, n):
            fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
            
        return fibonacci[n-1] + fibonacci[n-2]