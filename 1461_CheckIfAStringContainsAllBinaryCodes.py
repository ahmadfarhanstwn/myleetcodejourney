class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        appeared = set()
        for i in range(len(s)-(k-1)):
            a = s[i:i+k]
            if a not in appeared:
                appeared.add(a)
        return len(appeared) == 2**k