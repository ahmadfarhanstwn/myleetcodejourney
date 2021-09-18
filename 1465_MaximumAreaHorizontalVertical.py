class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.insert(0,0)
        verticalCuts.insert(0,0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        maxH = maxW = 0
        for i in range(1,len(horizontalCuts)):
            maxH = max(horizontalCuts[i]-horizontalCuts[i-1], maxH)
        for i in range(1,len(verticalCuts)):
            maxW = max(verticalCuts[i]-verticalCuts[i-1], maxW)
        return (maxH * maxW) % ((10 ** 9) + 7)
    
        # Time Complexity = O(h + w + hlog(h) + wlog(w))
        # Space Complexity = O(h + w) / O(1) ??