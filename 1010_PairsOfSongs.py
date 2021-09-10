class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remnant = [0] * 61
        output = 0
        for i in time:
            m = i % 60
            output += remnant[60-m]
            remnant[m if m else 60] += 1
        return output