class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        countP = [0] * 26
        countS = [0] * 26
        output = []
        n = len(p)
        for i in p:
            countP[ord(i)-97] += 1
        for i in range(len(p)):
            countS[ord(s[i])-97] += 1
        if countP == countS: output.append(0)
        for i in range(1,len(s)-n+1):
            countS[ord(s[i-1])-97] -= 1
            countS[ord(s[i+n-1])-97] += 1
            if countS == countP:
                output.append(i)
        return output