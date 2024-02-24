from typing import List

def uniqueOccurrences(arr: List[int]) -> bool:
    freq = {}
    for element in arr:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return len(freq) == len(set(freq.values()))
