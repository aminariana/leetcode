from collections import deque
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0]) if m else 0
    minute = 0
    inventory = set()
    q = deque()
    def adjacent(r, c):
        if r > 0: yield (r - 1, c)
        if r < m-1: yield (r + 1, c)
        if c > 0: yield (r, c - 1)
        if c < n-1: yield (r, c + 1)

    for r, row in enumerate(grid):
        print(row)
        for c, cell in enumerate(row):
            if cell == 2:
                q.appendleft((r, c, minute))
            elif cell == 1:
                inventory.add((r, c))
    # print(inventory)
    # print(q)

    while len(q):
        current_r, current_c, minute = q.pop()
        for r, c in adjacent(current_r, current_c):
            if grid[r][c] == 1 and (r, c) in inventory:
                # print(f"rot: {(r, c)}")
                q.appendleft((r, c, minute + 1))
                inventory.remove((r, c))

    return -1 if len(inventory) else minute
