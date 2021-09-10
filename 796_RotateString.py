class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i] == goal[0] and s[i:len(s)] == goal[:len(s)-i] and s[:i] == goal[len(s)-i:]:
                return True
        return False