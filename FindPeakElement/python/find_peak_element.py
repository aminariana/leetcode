from typing import List


def findPeakElement(nums: List[int]) -> int:
    stack = [(0, len(nums))]
    while len(stack):
        left, right = stack.pop()
        # print((left, right))
        mid = (left + right) // 2
        is_peak = (mid==0 or nums[mid] > nums[mid-1]) and (mid+1==len(nums) or nums[mid] > nums[mid+1])
        if is_peak:
            return mid
        elif right - left > 1:
            stack.append((left, mid))
            stack.append((mid, right))
    return -1
