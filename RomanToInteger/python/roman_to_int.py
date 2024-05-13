def romanToInt(s: str) -> int:
    value_of = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    c_right_neighbor = s[-1]
    for c in s[::-1]:
        if value_of[c] >= value_of[c_right_neighbor]:
            result += value_of[c]
        else:
            result -= value_of[c]
        c_right_neighbor = c
    return result
