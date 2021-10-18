class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dick = {}
        output = 0
        for i in nums:
            diff = i-int(str(i)[::-1])
            if diff in dick:
                dick[diff] += 1
            else:
                dick[diff] = 1
        for i in nums:
            diff = i-int(str(i)[::-1])
            dick[diff] -= 1
            output += dick[diff]
        return output % (10**9+7)