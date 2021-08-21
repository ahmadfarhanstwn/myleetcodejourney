class Solution:
    def minSteps(self, s: str, t: str) -> int:
        for x in s:
            t = t.replace(x, '', 1)
            
        return len(t)