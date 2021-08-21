class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = late = 0
        if s[0] == 'A':
            absent += 1
        elif s[0] == 'L':
            late += 1
        for i in range(1, len(s)):
            if absent >= 2 or late >= 3:
                return False
            if s[i] == 'A':
                late = 0
                absent += 1
            elif s[i] == 'L':
                late += 1
            else:
                late = 0
        if absent >= 2 or late >= 3:
            return False
        else:
            return True