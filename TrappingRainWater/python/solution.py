def trap(height):
    l = 0
    r = len(height) - 1
    trapped = 0
    watermark = 0
    while l <= r:
        if height[l] <= height[r]:
            watermark = max(watermark, height[l])
            trapped += watermark - height[l]
            l += 1
        else:
            watermark = max(watermark, height[r])
            trapped += watermark - height[r]
            r -= 1
    return trapped
