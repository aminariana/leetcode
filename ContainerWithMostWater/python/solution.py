from typing import List

def max_area(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    max_area = 0
    while (l < r):
        max_area = max(max_area, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area
