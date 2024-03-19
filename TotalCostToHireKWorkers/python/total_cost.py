from heapq import heappop, heappush
from typing import List


def totalCost(costs: List[int], k: int, candidates: int) -> int:
    left_index: int = 0
    right_index: int = len(costs) - 1
    cost_total = 0
    heap = []
    # populate the heap with `candidates` costs
    while left_index < candidates and left_index <= right_index:
        heappush(heap, (costs[left_index], left_index))
        left_index += 1
        if right_index >= left_index:
            heappush(heap, (costs[right_index], right_index))
            right_index -= 1
    for session in range(k):
        # hire lowest cost
        (cost_min, cost_index) = heappop(heap)
        cost_total += cost_min
        # heap up more
        if left_index <= right_index:
            if cost_index < left_index:
                heappush(heap, (costs[left_index], left_index))
                left_index += 1
            elif cost_index > right_index:
                heappush(heap, (costs[right_index], right_index))
                right_index -= 1
    return cost_total
