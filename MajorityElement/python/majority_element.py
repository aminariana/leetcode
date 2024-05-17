# Intuition: Ranges of collapsing rise in anyone's popularity can be ignored, with the same result.

# e.g. [3,2,3] has the same result as [3]
# e.g. [2,2,1,1,1,2,2] has the same result as [1,2,2]
# e.g. [4,4,1,2,4] same as [4]
# e.g. [1,4,4,2,4] same as [4,2,4] (i.e. 1 loses popularity) same as [4]
# e.g. [1,4,4,4,2,1,4,4,2] same as [4,4,2,1,4,4,2] same as [4,4,2] result 4

# Assume the first element is the correct candidate. Each vote for or against modifies their popularity. If the popularity collapses back to zero, start over picking the next candidate as head. Assuming there exists a real majority, a bad head candidate always gets neutralized by majority's votes and eventually majority becomes head.

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List


def majorityElement(nums: List[int]) -> int:
    candidate = None
    votes = 0
    for num in nums:
        if votes == 0:
            candidate = num

        if num == candidate:
            votes += 1
        else:
            votes -= 1
    return candidate
