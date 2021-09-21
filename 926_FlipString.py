class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero = s.count('0')
        one = 0
        output = min(zero,s.count('1'))
        for i in s:
            if i == '0':
                zero -= 1
            else:
                output = min(output,(one+zero))
                one += 1
        return output