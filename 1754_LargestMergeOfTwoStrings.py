class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        listWord1 = list(word1)
        listWord2 = list(word2)
        merge = []
        while listWord1 or listWord2:
            if listWord1 >= listWord2:
                merge.append(listWord1.pop(0))
            elif listWord2 >= listWord1:
                merge.append(listWord2.pop(0))
                
        return ''.join(merge)