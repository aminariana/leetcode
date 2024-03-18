from heapq import heapify, heappop, heappushpop
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    heapify(nums)
    while len(nums) > k: heappop(nums)
    return nums[0]

def findKthLargest_optimal(nums: List[int], k: int) -> int:
    pq = nums[:k]
    heapify(pq)
    for num in nums[k:]:
        heappushpop(pq, num)
    return pq[0]