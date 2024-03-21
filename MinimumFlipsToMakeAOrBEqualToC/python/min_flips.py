def minFlips(a: int, b: int, c: int) -> int:
    return (bin(a & b & ~c).count("1") * 2) + bin(~(a & b) & (a ^ b ^ c)).count("1")

def minFlips_whileLoop(a: int, b: int, c: int) -> int:
    res = 0
    while (a | b | c) > 0:
        if c & 1 > 0:
            res += (a & 1 == 0 and b & 1 == 0)
        else:
            res += (a & 1 > 0) + (b & 1 > 0)
        a >>= 1
        b >>= 1
        c >>= 1
    return res
