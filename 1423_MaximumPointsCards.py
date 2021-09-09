class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k: return sum(cardPoints)
        smallest = sum(cardPoints)
        right = len(cardPoints) - k
        for left in range(k+1):
            smallest = min(smallest, sum(cardPoints[left:right]))
            right += 1
        return sum(cardPoints) - smallest