def maxVowels(s: str, k: int) -> int:
    vowels = { 'a', 'e', 'i', 'o', 'u' }
    best = 0
    score = 0
    left = 0
    for right, c in enumerate(s):
        # per vowel encounter increase score
        if c in vowels:
            score += 1
        # as the window left closes, adjust the score
        while right - left + 1 > k:
            if s[left] in vowels:
                score -= 1
            left += 1
        # keep best score
        if score > best:
            best = score
    return best
