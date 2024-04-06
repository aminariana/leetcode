from collections import deque
from typing import List


def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    # for line in maze: print(line)
    m = len(maze)
    n = len(maze[0]) if m else 0
    row, col = entrance
    visited = set([(row, col)])
    q = deque([(row, col, 0)])
    def adjacents(row, col):
        if row > 0: yield(row - 1, col)
        if row < m-1: yield(row + 1, col)
        if col > 0: yield(row, col - 1)
        if col < n-1: yield(row, col + 1)
    while len(q):
        here = q.popleft()
        r, c, moves = here
        # print(here)
        if (r == 0 or r == m-1 or c == 0 or c == n-1) and moves > 0:
            return moves
        for row, col in adjacents(r, c):
            if maze[row][col] == "." and (row, col) not in visited:
                visited.add((row, col))
                q.append((row, col, moves + 1))
    return -1