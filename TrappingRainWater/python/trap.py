def trap(height):
    left = 0
    right = len(height) - 1
    trapped = 0
    watermark = 0
    while left <= right:
        if height[left] <= height[right]:
            watermark = max(watermark, height[left])
            trapped += watermark - height[left]
            left += 1
        else:
            watermark = max(watermark, height[right])
            trapped += watermark - height[right]
            right -= 1
    return trapped
