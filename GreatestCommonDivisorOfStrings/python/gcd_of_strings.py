from math import gcd

def gcdOfStrings(str1: str, str2: str) -> str:
    return "" if str1+str2 != str2+str1 else str1[:gcd(len(str1), len(str2))]

def gcdOfStringsLongWay(str1: str, str2: str) -> str:
    l1, l2 = len(str1), len(str2)
    for divisor in reversed(range(1, min(l1, l2) + 1)):
        if l1 % divisor == 0 and l2 % divisor == 0:
            # test divisibility at `divisor` length
            i = 0
            good = True
            while i < l1 or i < l2:
                c = str1[i % l1 % divisor]
                c1 = str1[i % l1]
                c2 = str2[i % l2]
                if (c1 != c or c2 != c):
                    good = False
                    break
                i += 1
            if good:
                return str1[:divisor]
    return ""
