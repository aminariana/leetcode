# It's just a math series.
# Be iterative and avoid memory-stacked recursion.
# Use multi assignment to keep it clean.
# Return the first, not the last, number in the sliding window to keep the return of base cases generic.
def tribonacci(n: int) -> int:
    t0, t1, t2 = 0, 1, 1
    for i in range(n):
        t0, t1, t2 = t1, t2, t0 + t1 + t2
    return t0
    