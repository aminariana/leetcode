from bisect import bisect_left
from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    window = []
    for i, num in enumerate(nums):
        pos = bisect_left(window, num)
        if pos == len(window):
            window.append(num)
        else:
            window[pos] = num
    return len(window) >= 3
