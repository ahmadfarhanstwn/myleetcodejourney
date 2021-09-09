class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = b = c = ''
        for x in firstWord:
            a += str(ord(x)-97)
        for y in secondWord:
            b += str(ord(y)-97)
        for z in targetWord:
            c += str(ord(z)-97)
        if int(a) + int(b) == int(c): return True
        return False