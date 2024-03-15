from typing import List


def letterCombinations(digits: str) -> List[str]:
    if not len(digits):
        return []
    letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }
    combo = [l for l in letters[digits[0]]]
    for digit in digits[1:]:
        combo = [c + letter for c in combo for letter in letters[digit]]
    return combo
