from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        allDict = dict(Counter(s))
        leftDict = {}
        output = 0
        for i in range(len(s)-1):
            if s[i] in leftDict:
                leftDict[s[i]] += 1
            else:
                leftDict[s[i]] = 1
            allDict[s[i]] -= 1
            if allDict[s[i]] == 0:
                del allDict[s[i]]
            if len(leftDict) == len(allDict):
                output += 1
        return output