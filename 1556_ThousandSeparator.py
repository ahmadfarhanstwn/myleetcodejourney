class Solution:
    def thousandSeparator(self, n: int) -> str:
        strN = str(n)
        output = ''
        for i in range(-1, -len(strN)-1, -1):
            if (-i - 1) % 3 == 0 and i != -1:
                output = strN[i] + '.' + output
            else:
                output = strN[i] + output
        return output