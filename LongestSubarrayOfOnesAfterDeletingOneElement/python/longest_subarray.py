from typing import List

def longestSubarray(nums: List[int]) -> int:
    k = 1
    best = 0
    left = 0
    dist = [0, 0]
    for right, value in enumerate(nums):
        # maintain the distribution seen
        dist[value] += 1
        # shrink window if delete allowance exceeded
        while dist[0] > k:
            dist[nums[left]] -= 1
            left += 1
        # count ones but use up unused deletes
        # subtotal would be dist[1] - (k - dist[0])
        subtotal = sum(dist) - k
        if best < subtotal:
            best = subtotal
    return best
    