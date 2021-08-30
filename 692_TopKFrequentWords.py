class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsDict = {}
        for i in words:
            if i in wordsDict:
                wordsDict[i] += 1
            else:
                wordsDict[i] = 1
        sortedWords = sorted(wordsDict, key=lambda x: (-wordsDict[x], x))
        return sortedWords[:k]