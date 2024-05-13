def intToRoman(num: int) -> str:
    roman_to_value = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ]
    s_arr = []
    while num > 0:
        for roman, value in roman_to_value:
            if num >= value:
                s_arr.append(roman)
                num -= value
                break
    return "".join(s_arr)
