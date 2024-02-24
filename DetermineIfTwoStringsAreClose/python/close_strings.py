from collections import defaultdict

def closeStrings(word1: str, word2: str) -> bool:
    dict1, dict2 = defaultdict(int), defaultdict(int)
    for c in word1: dict1[c] += 1
    for c in word2: dict2[c] += 1
    return dict1.keys() == dict2.keys() and \
        sorted(dict1.values()) == sorted(dict2.values())
