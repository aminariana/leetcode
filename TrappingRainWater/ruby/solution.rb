def trap(height)
    l, r = 0, height.count - 1
    trapped = 0
    watermark = 0
    while l <= r do
        if (height[l] <= height[r])
            watermark = [watermark, height[l]].max
            trapped += watermark - height[l]
            l += 1
        else
            watermark = [watermark, height[r]].max
            trapped += watermark - height[r]
            r -= 1
        end
    end
    return trapped
end
