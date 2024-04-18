from collections import deque
from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    q = deque(sorted([tuple(point) for point in points]))
    # print(q)
    arrows: int = 0
    seen = None
    while len(q):
        left, right = q.popleft()
        if seen is not None and seen >= left:
            # overlap detected, no dart needed
            seen = min(seen, right)
        else:
            arrows += 1
            seen = right
    return arrows
