from typing import List

class Solution:
    # Do not return anything, modify nums in-place instead.
    def moveZeroes(self, nums: List[int]) -> None:
        # j is the first zero's index (the write-head)
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0 and j < 0:
                j = i
            elif nums[i] != 0 and j >= 0:
                # defrag data 
                nums[j], nums[i], j = nums[i], nums[j], j + 1
