from collections import defaultdict
from typing import List


def minReorder(n: int, connections: List[List[int]]) -> int:
    # index them
    destinations_of = defaultdict(set)
    origins_of = defaultdict(set)
    for origin, destination in connections:
        destinations_of[origin].add(destination)
        origins_of[destination].add(origin)
    # traverse them
    inversion_cost = 0
    visited = [False] * n
    q = [0]
    while len(q):
        city = q.pop()
        visited[city] = True
        for origin in origins_of[city]:
            if not visited[origin]:
                q.append(origin)
        for destination in destinations_of[city]:
            if not visited[destination]:
                inversion_cost += 1
                q.append(destination)
    return inversion_cost
