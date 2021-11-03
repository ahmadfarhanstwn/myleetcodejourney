class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        topTop = bottomBottom = 1
        topBottom = bottomTop = topSame = bottomSame = 0
        for i in range(1, len(tops)):
            if tops[i] == tops[0] and bottoms[i] == tops[0]:
                topTop += 1
                topBottom += 1
                topSame += 1
            elif tops[i] == tops[0]: 
                topTop += 1
            elif bottoms[i] == tops[0]:
                topBottom += 1
            if tops[i] == bottoms[0] and bottoms[i] == bottoms[0]:
                bottomBottom += 1
                bottomTop += 1
                bottomSame += 1
            elif bottoms[i] == bottoms[0]:
                bottomBottom += 1
            elif tops[i] == bottoms[0]:
                bottomTop += 1
        if (topTop + topBottom - topSame == len(tops)) and (bottomBottom + bottomTop - bottomSame == len(tops)):
            return min(topTop-topSame, topBottom-topSame, bottomBottom-bottomSame, bottomTop-bottomSame)
        elif topTop + topBottom - topSame == len(tops):
            return min(topTop- topSame, topBottom- topSame)
        elif bottomBottom + bottomTop - bottomSame == len(tops):
            return min(bottomBottom- bottomSame, bottomTop- bottomSame)
        else:
            return -1