class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dict = {}
        for n in words:
            for m in n:
                if m not in dict:
                    dict[m] = 1
                else:
                    dict[m] += 1
        for i in dict:
            if dict[i] % len(words) != 0:
                return False
        return True