class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        a = str(n)
        sign = i = 0
        b = ''
        while i < len(a)-1:
            for j in range (i+1, len(a)):
                if a[i] < a[j]:
                    i += 1
                    break
                elif a[i] > a[j]:
                    sign = i
                    b = a[:sign] + str(int(a[sign])-1) + ('9' * (len(a)-(sign+1)))
                    i = len(a) + 1
                    break
            else:
                i += 1
        return int(b) if b != '' else n