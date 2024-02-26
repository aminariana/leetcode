from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    # sliding window of (nums[left] ... nums[right])
    left = -k
    subtotal = 0
    best = 0
    for right, value in enumerate(nums):
        # enter window
        subtotal += value
        # leave window
        if left >= 0:
            subtotal -= nums[left]
        left += 1
        # initialize or track best window
        if left == 0 or best < subtotal:
            best = subtotal
    return best / k
