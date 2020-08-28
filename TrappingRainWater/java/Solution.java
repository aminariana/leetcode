package TrappingRainWater.java;

class Solution {
    public static int trap(int[] height) {
        int trapped = 0, l = 0, r = height.length - 1, watermark = 0;
        while(l <= r) {
            if (height[l] <= height[r]) {
                watermark = Math.max(watermark, height[l]);
                trapped += watermark - height[l++];
            } else {
                watermark = Math.max(watermark, height[r]);
                trapped += watermark - height[r--];
            }
        }
        return trapped;
    }
}