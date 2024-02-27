from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    candies_max = max(candies)
    return [kid + extraCandies >= candies_max for kid in candies]
