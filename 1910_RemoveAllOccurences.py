class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        index = 0
        while index < len(s):
            if s[index:len(part)+index] == part:
                s = s[0:index] + s[len(part)+index:len(s)]
                index = 0
            else:
                index += 1
        return s