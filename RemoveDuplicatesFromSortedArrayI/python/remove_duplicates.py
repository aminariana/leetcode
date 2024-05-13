from typing import List


def removeDuplicates(nums: List[int]) -> int:
    k = 1
    for num in nums[1:]:
        if nums[k-1] != num:
            nums[k] = num
            k += 1
    return k
