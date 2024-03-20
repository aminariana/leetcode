def uniquePaths(m: int, n: int) -> int:
    paths = [1] * n
    for row in range(1, m):
        for col in range(1, n):
            paths[col] += paths[col-1]
    return paths[-1]
