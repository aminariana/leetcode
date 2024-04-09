from typing import List


def combinationSum3_dp(k: int, n: int) -> List[List[int]]:
    combos = [[]]
    def combo_enlarger(i: int):
        for combo in combos:
            last_seen_digit = combo[-1] if len(combo) else 0
            for digit in range(last_seen_digit + 1, 10):
                if (i==k and digit + sum(combo) == n) or (i < k and digit + sum(combo) < n):
                    yield combo + [digit]
    for i in range(1, k+1):
        combos = list(combo_enlarger(i))
        # print(f"{i}: {combos}")
    return combos

def combinationSum3_recursive(k: int, n: int, is_exact: bool = True) -> List[List[int]]:
    if k == 0:
        return [[]]
    else:
        combos = []
        for combo in combinationSum3_recursive(k - 1, n, False):
            last_seen_digit = combo[-1] if len(combo) else 0
            for digit in range(last_seen_digit + 1, 10):
                if (is_exact and digit + sum(combo) == n) or (not is_exact and digit + sum(combo) < n):
                    combos.append(combo + [digit])
        # print(f"{k}: {combos}")
        return combos

