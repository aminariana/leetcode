from functools import reduce
from typing import List


def singleNumber(nums: List[int]) -> int:
    return reduce(lambda num, result: result ^ num, nums, 0)
