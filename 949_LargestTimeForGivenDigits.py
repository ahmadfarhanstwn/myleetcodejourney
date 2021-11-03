class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        return max(["%d%d:%d%d" % time for time in itertools.permutations(arr) if time[:2] < (2,4) and time[2]<6] or [""])