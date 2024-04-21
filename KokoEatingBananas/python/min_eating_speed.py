from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    def calc_hours(k):
        result = 0
        for pile in piles:
            result += (pile // k) + (1 if pile % k > 0 else 0)
        # print(f"{k}: {result}")
        return result

    left = 1
    right = max(piles)
    actual = None
    best = right
    while right > left:
        # print((left, right))
        k = (left + right) // 2
        actual = calc_hours(k)
        if actual > h:
            left = k + 1
        elif actual <= h:
            right = k
            best = min(best, k)
    return best
