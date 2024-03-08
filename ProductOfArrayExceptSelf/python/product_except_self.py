from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    answer = [1] * len(nums)
    prefix, suffix = 1, 1
    for i in range(len(nums)):
        answer[i] *= prefix
        answer[-1-i] *= suffix
        prefix *= nums[i]
        suffix *= nums[-1-i]
    return answer
