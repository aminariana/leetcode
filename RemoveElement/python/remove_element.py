from typing import List


def removeElement(nums: List[int], val: int) -> int:
    k = 0
    for i, num in enumerate(nums):
        if num != val:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
    return k
