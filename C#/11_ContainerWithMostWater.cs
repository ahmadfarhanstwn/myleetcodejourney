public class Solution {
    public int MaxArea(int[] height) {
        int left = 0, right = height.Length - 1, maxArea = 0;
        while(left < right){
            if (height[left] < height[right]){
                maxArea = Math.Max(maxArea, height[left]*(right-left));
                left++;
            } else{
                maxArea = Math.Max(maxArea, height[right]*(right-left));
                right--;
            }
        }
        return maxArea;
    }
}