from collections import deque
from typing import List

def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    unlocked = [False] * len(rooms)
    # we have the key to room 0
    bag = deque([0])
    while len(bag):
        key = bag.pop()
        if not unlocked[key]:
            unlocked[key] = True
            for new_key in rooms[key]:
                bag.append(new_key)
    return all(unlocked)
