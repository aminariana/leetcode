from typing import List


def largestAltitude(gain: List[int]) -> int:
    height = 0
    height_max = 0
    for delta in gain:
        height += delta
        height_max = max(height_max, height)
    return height_max
