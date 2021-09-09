class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        now = 0
        highest = 0
        for i in gain:
            now += i
            highest = max(highest,now)
        return highest