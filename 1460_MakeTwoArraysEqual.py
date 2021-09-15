from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        targetCount = Counter(target)
        arrCount = Counter(arr)
        return targetCount == arrCount