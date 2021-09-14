class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n).replace("0b", "")
        for i in range(1,len(binary)):
            if binary[i] == binary[i-1]: return False
        return True