class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        dick = defaultdict(int)
        for a,b,c in segments:
            dick[a] += c
            dick[b] -= c
        output = []
        prev, value = None, 0
        for i in sorted(dick):
            if prev != None and value != 0:
                output.append((prev, i, value))
            value += dick[i]
            prev = i
        return output