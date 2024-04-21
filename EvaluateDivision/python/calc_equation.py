from collections import defaultdict, deque
from typing import List


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = defaultdict(str)
    # result = []
    for (left, right), value in zip(equations, values):
        # print(f"{(left, right)} -> {value}")
        if left not in graph: graph[left] = defaultdict(str)
        if right not in graph: graph[right] = defaultdict(str)
        graph[left][right] = value
        graph[right][left] = 1 / value
    # print(graph)

    def query(left, right):
        q = deque()
        visited = set()
        if left in graph:
            q.append((left, 1))
            visited.add(left)
        while len(q):
            current, ratio = q.popleft()
            if current == right:
                return ratio
            else:
                for child in graph[current]:
                    if child not in visited:
                        visited.add(child)
                        q.append((child, ratio * graph[current][child]))
        return -1

    return list(map(lambda q: query(*q), queries))
