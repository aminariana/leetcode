package trappingrainwater

func trap(height []int) int {
	trapped := 0
	l := 0
	r := len(height) - 1
	watermark := 0
	for l <= r {
		if height[l] <= height[r] {
			if height[l] > watermark {
				watermark = height[l]
			}
			trapped += watermark - height[l]
			l++
		} else {
			if height[r] > watermark {
				watermark = height[r]
			}
			trapped += watermark - height[r]
			r--
		}
	}
	return trapped
}
