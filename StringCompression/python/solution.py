from typing import List

def compress(chars: List[str]) -> int:
    w = 0 # write index
    last, freq = chars[0], 0
    l = len(chars)
    for i in range(l + 1):
        if i < l and chars[i] == last:
            freq += 1
        else:
            # compress
            chars[w] = last
            w += 1
            if freq > 1:
                for num in str(freq):
                    chars[w] = num
                    w += 1
            # reset accumulator
            if i == l: break
            last = chars[i]
            freq = 1
    return w

def compress_before_space_optimization(chars: List[str]) -> int:
    res = []
    last, freq = chars[0], 0
    chars.append('') # to flush the last result
    for char in chars:
        if char == last:
            freq += 1
        else:
            res.append(last)
            if freq > 1:
                res.extend(list(str(freq)))
            last = char
            freq = 1
    chars.clear()
    chars.extend(res)
    return len(chars)
