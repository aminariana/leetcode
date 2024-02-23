from typing import List

def rob(nums: List[int]) -> int:
    # Rationale: At house i, either rob it and the best of up to two houses ago, or
    # the best of one house ago.
    last, best = 0, 0
    for i in range(len(nums)):
        last, best = best, max(nums[i] + last, best)
    return best
    