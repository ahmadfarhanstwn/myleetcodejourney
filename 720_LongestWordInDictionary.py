class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x),x))
        for i in words:
            length = 0
            for x in range(len(i)-1,0,-1):
                if i[:x] not in words:
                    break
                length += 1
            if length == len(i)-1:
                return i
        return ""