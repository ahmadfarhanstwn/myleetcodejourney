class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        orderedHeights = sorted(heights)
        indices = 0
        for i in range(len(heights)):
            if orderedHeights[i] != heights[i]:
                indices += 1
        return indices