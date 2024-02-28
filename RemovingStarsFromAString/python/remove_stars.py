def removeStars(s: str) -> str:
    chars = []
    for c in s:
        if c == '*':
            chars.pop()
        else:
            chars.append(c)
    return ''.join(chars)
