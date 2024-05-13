from typing import List


def removeDuplicates(nums: List[int], dup_max = 2) -> int:
    k = 0
    for num in nums:
        if k < dup_max or num > nums[k - dup_max]:
            nums[k] = num
            k += 1
    return k
