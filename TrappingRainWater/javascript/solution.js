exports.trap = function trap(height) {
    trapped = 0; watermark = 0; l = 0; r = height.length - 1;
    while (l <= r) {
        if (height[l] <= height[r]) {
            watermark = Math.max(watermark, height[l]);
            trapped += watermark - height[l++];
        } else {
            watermark = Math.max(watermark, height[r]);
            trapped += watermark - height[r--];
        }
    }
    return trapped;
};
