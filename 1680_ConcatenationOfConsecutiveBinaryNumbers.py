class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary = ''
        for i in range(1,n+1):
            binary += "{0:b}".format(i)
        return int(binary, 2) % (10**9+7)