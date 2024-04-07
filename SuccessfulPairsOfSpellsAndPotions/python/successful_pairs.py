import bisect
from math import ceil
from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()
    return list(map(lambda spell: len(potions) - bisect.bisect_left(potions, ceil(success / spell)), spells))
