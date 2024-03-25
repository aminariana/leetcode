from typing import List


def pivotIndex(nums: List[int]) -> int:
    total = sum(nums)
    sub = 0
    for pivot, num in enumerate(nums):
        if sub * 2 == total - num:
            return pivot
        sub += num
    return -1
