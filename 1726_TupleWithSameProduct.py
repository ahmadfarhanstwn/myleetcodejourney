class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dick = {}
        output = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product = nums[i] * nums[j]
                if product in dick:
                    dick[product] += 1
                else:
                    dick[product] = 1
        for key in dick:
            if dick[key] > 1:
                i = dick[key] - 1
                while i > 0:
                    output += i*8
                    i -= 1
        return output