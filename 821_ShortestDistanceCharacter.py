class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        right = left = 0
        output = []
        for i in range(len(s)):
            if s[i] == c:
                output.append(0)
                continue
            for r in range(i, len(s)):
                if s[r] == c:
                    right = r - i
                    break
            for l in range(i, -1, -1):
                if s[l] == c:
                    left = i - l
                    break
            output.append(min(left,right) if left and right != 0 else max(left,right))
            left = right = 0
        return output