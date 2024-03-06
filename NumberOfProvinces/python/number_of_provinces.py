from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        unseen = set(range(n))
        province_count = 0
        while len(unseen):
            capital = unseen.pop()
            province_count += 1
            # paint one province dfs
            stack = deque([capital])
            while len(stack):
                city = stack.pop()
                for neighbor, connected in enumerate(isConnected[city]):
                    if connected and neighbor in unseen:
                        stack.append(neighbor)
                        unseen.remove(neighbor)
        return province_count
