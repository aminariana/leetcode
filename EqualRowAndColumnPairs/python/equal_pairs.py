from collections import Counter
from typing import List

def equalPairs(grid: List[List[int]]) -> int:
    n = len(grid)
    row_hashes = [0] * n
    col_hashes = [0] * n
    for i in range(n):
        for j in range(n):
            # alternatively hash as tuples
            row_hashes[i] = row_hashes[i] * 100000 + grid[i][j]
            col_hashes[j] = col_hashes[j] * 100000 + grid[i][j]
    row_hist = Counter(row_hashes)
    col_hist = Counter(col_hashes)
    return sum(row_hist[key] * col_hist[key] for key in row_hist if key in col_hist)
