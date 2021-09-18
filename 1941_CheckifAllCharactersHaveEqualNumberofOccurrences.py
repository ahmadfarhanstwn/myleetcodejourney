class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = {}
        letters = set()
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for i in count.values():
            letters.add(i)
        return len(letters) == 1