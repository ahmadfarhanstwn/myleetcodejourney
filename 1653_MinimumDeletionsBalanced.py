class Solution:
    def minimumDeletions(self, s: str) -> int:
        output = 0
        countB = 0
        for i in s:
            if i == 'a':
                output = min(output+1, countB)
            else:
                countB += 1
        return output