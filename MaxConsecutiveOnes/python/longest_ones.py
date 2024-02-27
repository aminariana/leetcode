from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    best = 0
    left = 0
    # zero zeroes and zero ones
    dist = [0, 0]
    for right, value in enumerate(nums):
        # enter window
        dist[value] += 1
        # leave window if >k zeroes
        while dist[0] > k:
            dist[nums[left]] -= 1
            left += 1
        subtotal = sum(dist)
        if best < subtotal:
            best = subtotal
    return best
