class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        prefix = 0
        dick = dict()
        dick[0] = 1
        for i in nums:
            prefix += i
            output += dick.get(prefix-k,0)
            dick[prefix] = dick.get(prefix,0) + 1
        return output