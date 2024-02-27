from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i <= 0 or flowerbed[i-1] == 0) and (i+1 >= len(flowerbed) or flowerbed[i+1] == 0):
            i += 1 # skip next spot
            n -= 1
        i += 1
    return n <= 0