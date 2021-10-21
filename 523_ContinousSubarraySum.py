class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dick = {0:1}
        modol = nums[0] % k
        prefix = modol
        if prefix in dick:
            dick[prefix] += 1
        else:
            dick[prefix] = 1
        for i in range(1,len(nums)):
            prefix = (prefix+nums[i]) % k
            if prefix in dick:
                if (prefix == modol and dick[prefix] > 1) or (prefix != modol and dick[prefix] > 0):
                    return True
                dick[prefix] += 1
            else:
                dick[prefix] = 1
            modol = prefix
        return False