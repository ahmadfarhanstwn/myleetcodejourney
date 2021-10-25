class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = 0
        output = 0
        product = 1
        while right < len(nums):
            if nums[right] >= k:
                left = right + 1
                right += 1
                product = 1
                continue
            product *= nums[right]
            if product < k:
                output += right-left+1
                right += 1
            else:
                lleft = left
                while product >= k and lleft <= right:
                    product /= nums[lleft]
                    lleft += 1
                output += right - lleft + 1
                left = lleft
                right += 1
        return output