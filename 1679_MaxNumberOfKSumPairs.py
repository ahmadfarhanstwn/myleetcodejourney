class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        output = 0
        seen = defaultdict(int)
        for i in nums:
            x = k - i
            if seen[x] > 0:
                output += 1
                seen[x] -= 1
            else:
                seen[i] += 1
        return output