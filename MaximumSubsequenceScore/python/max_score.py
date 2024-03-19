from heapq import heappop, heappush
from typing import List

# I had zero intuition. This took me 3 hours to get wrong, then 6 more hours to get right.
# It's a hard question.
#
# Approach:
# Sort num1s by num2s desc.
# Then as you enumerate num2s, you're only visiting them going to lower and lower minimums.
# So finding the minimum for the last k elements is just looking at the current num2.
# What you need then is to add the corresponding num1 to the working sum,
# and to throw away the least valuable num1 seen so far; that can be tracked using a heap.
def maxScore(nums1: List[int], nums2: List[int], k: int) -> int:
    num2_num1_desc = list(reversed(sorted(list(zip(nums2, nums1)))))
    max_score = 0
    heap_sum = 0
    heap = []
    for (num2, num1) in num2_num1_desc:
        heappush(heap, num1)
        heap_sum += num1
        if len(heap) > k:
            heap_sum -= heappop(heap)
        if len(heap) == k:
            max_score = max(heap_sum * num2, max_score)

    return max_score
