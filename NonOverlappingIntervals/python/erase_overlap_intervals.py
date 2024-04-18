from collections import deque
from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals_sorted = [(start, end) for [start, end] in intervals]
    intervals_sorted.sort()
    q = deque(intervals_sorted)
    # print(q)
    dropped = 0
    seen = q[0][0]
    while len(q):
        interval_start, interval_end = q.popleft()
        if seen > interval_start:
            # print(f"overlap: {seen} > {interval_start}")
            dropped += 1
            seen = min(seen, interval_end)
        else:
            seen = interval_end
    return dropped
