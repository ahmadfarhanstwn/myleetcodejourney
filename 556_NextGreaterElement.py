class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1
        n = list(map(int, str(n)))
        swapper = -1
        
        for i in range(len(n)-1, 0, -1):
            if n[i] > n[i-1]:
                swapper = i - 1
                break
        if swapper == -1:
            return -1
        for i in range(len(n)-1, swapper, -1):
            if n[i] > n[swapper]:
                n[swapper], n[i] = n[i], n[swapper]
                break
        n[swapper+1:] = sorted(n[swapper+1:])
        ans = int("".join(map(str, n)))
        return ans if ans < 2**31 else -1