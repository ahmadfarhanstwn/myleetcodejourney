class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right , maxArea = 0, len(height)-1, 0
        while left < right:
            if height[left] < height[right]:
                maxArea = max(maxArea, height[left]*(right-left))
                left += 1
            else:
                maxArea = max(maxArea, height[right]*(right-left))
                right -= 1
        return maxArea